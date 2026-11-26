"""Verify the public release and reproduce saved v3.7 tables offline (no inference)."""
from pathlib import Path
import csv, hashlib, json, shutil, sqlite3, sys, tarfile

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'_reproduction'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    # The release manifest covers all distributed files except itself.
    manifest=ROOT/'SHA256SUMS'
    if manifest.exists():
        for line in manifest.read_text(encoding='utf-8').splitlines():
            checksum, name=line.split('  ',1)
            assert sha(ROOT/name)==checksum, 'Release checksum mismatch: '+name
    OUT.mkdir(exist_ok=True)
    sandbox=OUT/'workspace'
    sandbox.mkdir(exist_ok=True)
    for name in ['outputs','work']:
        shutil.copytree(ROOT/name,sandbox/name,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','secrets','runs'))
    expected={v['path']:v for v in json.loads((ROOT/'data/archive-manifest.json').read_text(encoding='utf-8'))}
    with tarfile.open(ROOT/'data/research-records.tar.gz','r:gz') as archive:
        assert len(archive.getmembers())==len(expected)
        for member in archive:
            assert member.isfile() and member.name in expected
            target=(sandbox/member.name).resolve()
            assert target.is_relative_to(sandbox.resolve())
            data=archive.extractfile(member).read()
            assert hashlib.sha256(data).hexdigest()==expected[member.name]['sha256']
            target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    project=sandbox/'work/authority-swap'
    # Reconstruct only the accounting columns used by analysis, in this disposable workspace.
    dbpath=project/'runs/adaption/calls.sqlite3';dbpath.parent.mkdir(parents=True,exist_ok=True)
    if dbpath.exists():dbpath.unlink()
    integers={'reserved_microcredits','input_tokens','cached_tokens','output_tokens','reasoning_tokens','uncached_microcredits'}
    with (ROOT/'data/hosted-accounting.csv').open(encoding='utf-8',newline='') as f, sqlite3.connect(dbpath) as db:
        reader=csv.DictReader(f);fields=reader.fieldnames
        db.execute('CREATE TABLE calls ('+','.join(n+(' INTEGER' if n in integers else ' TEXT') for n in fields)+')')
        db.executemany('INSERT INTO calls VALUES ('+','.join('?' for _ in fields)+')',
                      [[None if r[k]=='' else (int(r[k]) if k in integers else r[k]) for k in fields] for r in reader])
    sys.path.insert(0,str(project))
    import analyze_v37 as a
    a.OUTPUT=OUT/'tables';a.OUTPUT.mkdir(exist_ok=True)
    cfg,_,items=a.read_schedule()
    core=[];paired=[];escalation=[];correction=[];diagnostics=[];record_count=0
    for model in cfg['model_settings']:
        records=a.read_records(model);record_count+=len(records)
        c,e,x=a.observations(model,cfg,items,records)
        core.extend(a.core_rows(model,c));paired.append(a.paired_row(model,c))
        escalation.extend(a.escalation_rows(model,e));correction.extend(a.correction_rows(model,x))
        diagnostics.extend(a.diagnostic_rows(model,records))
    usage,exposure=a.accounting_rows()
    tables={'Core Branches':core,'Paired Contrasts':paired,'Escalation':escalation,
            'Escalation Contrasts':a.escalation_contrasts(escalation),'Correction':correction,
            'Unusable Diagnostics':diagnostics,'Run Timing':a.timing_rows(cfg['model_settings']),
            'Hosted Accounting':usage}
    checked=[]
    for name, rows in tables.items():
        path=a.write_csv(name,rows)
        expected_path=ROOT/'outputs'/path.name
        with path.open(encoding='utf-8',newline='') as f, expected_path.open(encoding='utf-8',newline='') as e:
            assert list(csv.DictReader(f))==list(csv.DictReader(e)), 'Table mismatch: '+name
        checked.append({'name':name,'rows':len(rows),'sha256':sha(path),'matches_saved_table':True})
    # Also verify the original main-data manifests, not just the publication archive.
    for name in ['records','items']:
        p=project/'runs/main-v3.7'/f'{name}-sha256.txt'
        for line in p.read_text(encoding='utf-8').splitlines():
            checksum,relative=line.split('  ',1)
            assert sha(p.parent/relative)==checksum,'Original main-record mismatch'
    result={'status':'PASS','logical_records_audited':record_count,'models':len(cfg['model_settings']),
            'tables':checked,'conservative_project_credit_exposure':str(exposure),
            'network_calls':0,'model_inference_calls':0,'credits_spent':0,
            'note':'Recomputed from preserved records; independent of provider availability. AI-only source verification remains a limitation.'}
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
