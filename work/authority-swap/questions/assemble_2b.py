"""Freeze independent source derivations before opening provisional draft keys."""
import csv,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
here=Path(__file__).resolve().parent
root=here.parents[2]
out=root/'outputs'
def readcsv(p):
    return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
working=readcsv(out/'Authority Swap - Part 2b Working Questions.csv')
original={r['id']:r for r in readcsv(out/'Authority Swap - Part 2a Draft Questions.csv')}
evidence={}; manifest=[]
for group in 'ces':
    p=here/f'verified-{group}.jsonl'
    records=[json.loads(x) for x in p.read_text(encoding='utf-8-sig').splitlines() if x.strip()]
    if len(records)!=46:raise ValueError(f'{p.name}: expected46 got{len(records)}')
    for r in records:
        if r['id'] in evidence:raise ValueError('duplicate '+r['id'])
        for field in ['id','derived_key','source_url','access_date','locator','exact_excerpt','reasoning','alternative_false','status','issue']:
            if field not in r:raise ValueError(f'{r["id"]}: missing {field}')
        if r['derived_key'] not in ['A','B','UNRESOLVED']:raise ValueError(r['id']+' invalid key')
        if r['status'] not in ['SOURCE_PASS','SOURCE_FLAG']:raise ValueError(r['id']+' invalid status')
        if r['status']=='SOURCE_PASS' and (r['derived_key']=='UNRESOLVED' or not r['exact_excerpt'] or not r['alternative_false']):raise ValueError(r['id']+' insufficient pass evidence')
        r['reviewer']='fresh_blind_'+group
        evidence[r['id']]=r
    manifest.append({'file':str(p),'sha256':digest(p),'records':len(records)})
if set(evidence)!={r['id'] for r in working}:raise ValueError('ID mismatch')
freeze={'frozen_at_utc':datetime.now(timezone.utc).isoformat(),'derivations':manifest,'working_questions_sha256':digest(out/'Authority Swap - Part 2b Working Questions.csv'),'note':'Independent derivations saved and hashed before this script opens draft keys.'}
(here/'blind-derivations-manifest.json').write_text(json.dumps(freeze,indent=2),encoding='utf-8')
# The key file is first read only after the independent evidence has been frozen above.
keys={r['id']:r['draft_key'] for r in readcsv(here/'draft-keys-v1.csv')}
ledger=[]
for r in working:
    ev=evidence[r['id']]; old=original[r['id']]
    revised=any(r[f]!=old[f] for f in ['stem','option_a','option_b'])
    comparison='REVISED_NOT_COMPARABLE' if revised else ('UNRESOLVED' if ev['derived_key']=='UNRESOLVED' else 'MATCH' if ev['derived_key']==keys[r['id']] else 'DISAGREEMENT')
    row={**r,**{f:ev[f] for f in ev if f!='id'}}
    row['draft_key_comparison']=comparison
    row['verification_status']=ev['status']
    row['use_status']='EXCLUDE_PENDING_REPLACEMENT_2C' if r['use_status'].startswith('EXCLUDE') else 'SOURCE_OR_WORDING_FLAG_2C' if ev['status']=='SOURCE_FLAG' or comparison=='DISAGREEMENT' else 'SOURCE_CHECKED_AWAITING_2C'
    ledger.append(row)
fields=list(dict.fromkeys(k for r in ledger for k in r))
with (out/'Authority Swap - Part 2b Source and Key Ledger.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(ledger)
summary={'items':len(ledger),'source_status':dict(Counter(r['status'] for r in ledger)),'use_status':dict(Counter(r['use_status'] for r in ledger)),'comparison':dict(Counter(r['draft_key_comparison'] for r in ledger)),'flagged_ids':[r['id'] for r in ledger if r['status']=='SOURCE_FLAG'],'disagreements':[r['id'] for r in ledger if r['draft_key_comparison']=='DISAGREEMENT'],'source_checked_main_tiers':dict(Counter(r['tier'] for r in ledger if r['bank']=='main' and r['use_status']=='SOURCE_CHECKED_AWAITING_2C'))}
(here/'part2b-summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
