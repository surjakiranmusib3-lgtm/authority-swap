"""Freeze verified research questions. This program never calls a model/API."""
from pathlib import Path
import csv, json, hashlib, random, re, math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
OUT=ROOT/'outputs'
SEED=2026111402
VERSION='v1.3'
DROP={'C027','C028','S017','S025','S027'}
QUESTION_FIELDS=['id','bank','tier','domain_group','domain','stem','option_a','option_b','source_url','source_locator']
PACKETS=['replacement','diversify','wording','adjudication','citation','locator']

def readcsv(p):
    return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def readjsonl(p):
    return [json.loads(s) for s in p.read_text(encoding='utf-8-sig').splitlines() if s.strip()]
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest().upper()
def writecsv(p,rows,fields):
    with p.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
def jsonwrite(p,data):
    p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def normalize_review(v,q):
    """Preserve the full original record while mapping the reviewers' schemas."""
    v=v.copy()
    v['derived_key']=v.get('derived_key',v.get('answer','UNRESOLVED'))
    v['alternative_false']=v.get('alternative_false',v.get('why_alternative_false',''))
    v['reviewer']=v.get('reviewer',v.get('reviewer_identity',{}).get('agent_id',''))
    v['issue']=v.get('issue',json.dumps(v.get('issues',[]),ensure_ascii=False))
    if 'sources' in v:
        usable=[s for s in v['sources'] if s.get('exact_passages') or s.get('exact_table_cells') or s.get('exact_excerpt')]
        preferred=next((s for s in usable if sourcepage(s['url'])==sourcepage(q['source_url'])),usable[0] if usable else {})
        v['source_url']=preferred.get('url',q['source_url'])
        v['access_date']=preferred.get('accessed_utc_date',v.get('recorded_utc_date',''))
        v['locator']=preferred.get('locator',q['source_locator'])
        v['exact_excerpt']=json.dumps([dict(url=s['url'],locator=s.get('locator',''),passages=s.get('exact_passages',[]),table_cells=s.get('exact_table_cells',[])) for s in usable],ensure_ascii=False)
    return v
def sourcepage(url):
    u=urlsplit(url.strip());host=u.netloc.lower()
    if host in ('www.nps.gov','home.nps.gov'):host='nps.gov'
    if host.startswith('www.'):host=host[4:]
    query=[(k,v) for k,v in parse_qsl(u.query,keep_blank_values=True) if not k.startswith('utm_') and k not in ('pvs','section')]
    return urlunsplit(('https',host,u.path.rstrip('/'),urlencode(query),'') )
def words(s):
    return re.findall(r"[\w]+(?:[.'’^-][\w]+)*",s)
ABSOLUTES=re.compile(r'\b(?:all|only|always|never|must|none|every|solely|entirely|exclusively|alone|completely)\b',re.I)
def cue_stats(rows,keyfield='key'):
    c=Counter();details=[]
    for r in rows:
        k=r.get(keyfield,'')
        if k not in ('A','B'):continue
        co=r['option_a' if k=='A' else 'option_b'];wo=r['option_b' if k=='A' else 'option_a']
        wc,ww=len(words(co)),len(words(wo));cc,cw=len(co),len(wo)
        rel='shorter' if wc<ww else 'longer' if wc>ww else 'equal'
        crel='shorter' if cc<cw else 'longer' if cc>cw else 'equal'
        c['keyed_rows']+=1;c['correct_words_'+rel]+=1;c['correct_characters_'+crel]+=1
        ac,aw=ABSOLUTES.findall(co),ABSOLUTES.findall(wo)
        c['correct_options_with_absolute']+=bool(ac);c['wrong_options_with_absolute']+=bool(aw)
        c['correct_absolute_tokens']+=len(ac);c['wrong_absolute_tokens']+=len(aw)
        details.append(dict(id=r['id'],correct_word_count=wc,wrong_word_count=ww,word_relation=rel,correct_character_count=cc,wrong_character_count=cw,correct_absolute_words=';'.join(ac),wrong_absolute_words=';'.join(aw)))
    return dict(c),details

old=readcsv(OUT/'Authority Swap - Part 2b Source and Key Ledger.csv')
oldby={r['id']:r for r in old}
changes={}
evidence={}
freeze=[]
for packet in PACKETS:
    inp=HERE/f'p2c-{packet}-questions.csv'
    ev=HERE/f'p2c-verified-{packet}.jsonl'
    assert inp.exists() and ev.exists(),f'Missing review packet {packet}'
    qr=readcsv(inp);vr=readjsonl(ev)
    assert {r['id'] for r in qr}=={r['id'] for r in vr},f'Incomplete review {packet}'
    assert len(vr)==len({r['id'] for r in vr}),f'Duplicate review {packet}'
    freeze.extend([dict(file=str(inp.relative_to(ROOT)),sha256=sha(inp)),dict(file=str(ev.relative_to(ROOT)),sha256=sha(ev))])
    for r in qr:changes[r['id']]=r
    qb={r['id']:r for r in qr}
    for r in vr:evidence[r['id']]=normalize_review(r,qb[r['id']])

# Preserve the two independently authored pieces of the merged replacement packet.
for suffix in ('a','b'):
    p=HERE/f'p2c-verified-replacements-{suffix}.jsonl'
    freeze.append(dict(file=str(p.relative_to(ROOT)),sha256=sha(p)))
# Hash evidence before any comparison; draft-key files are intentionally never opened.
jsonwrite(HERE/'p2c-blind-evidence-manifest.json',dict(created_utc=datetime.now(timezone.utc).isoformat(),reviewer_input='key-free packets only',draft_key_files_opened=False,files=freeze))

audit=json.loads((HERE/'p2c-fact-audit.json').read_text(encoding='utf-8-sig'))
oldatoms={r['id']:r for r in audit['items']}
catalog={r['id']:r for r in audit['fact_catalog']}
rows=[];excluded=[]
for ident,orig in oldby.items():
    if ident in DROP:
        excluded.append(dict(id=ident,reason='Retired after overlap/prefix-concentration audit; no replacement accepted for this slot',previous_status=orig['use_status']))
        continue
    q={k:orig[k] for k in QUESTION_FIELDS}
    if ident in changes:
        q.update(changes[ident]);v=evidence[ident]
        if v['status'] not in ('PASS','SOURCE_PASS') or v['derived_key'] not in ('A','B'):
            excluded.append(dict(id=ident,reason='Fresh verification flag: '+str(v.get('issue','')),previous_status=orig['use_status']))
            continue
        key=v['derived_key'];facts=v.get('fact_atoms',[])
        provenance='fresh key-file-blind source derivation, Part 2c'
        verification_fields={k:v.get(k,'') for k in ['source_url','access_date','locator','exact_excerpt','reasoning','alternative_false','reviewer','issue']}
        if verification_fields['source_url']:q['source_url']=verification_fields['source_url']
        if verification_fields['locator']:q['source_locator']=verification_fields['locator']
    else:
        assert orig['use_status']=='SOURCE_CHECKED_AWAITING_2C',f'Unresolved original {ident}'
        key=orig['derived_key'];v=orig
        atoms=oldatoms[ident]['fact_atoms']+oldatoms[ident].get('supporting_fact_atoms',[])
        facts=[dict(atom_id=a,description=catalog[a]['property'],value=catalog[a]['value']) for a in atoms]
        provenance='unchanged content; blind source derivation inherited from Part 2b'
        verification_fields={k:orig.get(k,'') for k in ['source_url','access_date','locator','exact_excerpt','reasoning','alternative_false','reviewer','issue']}
    assert key in ('A','B')
    # Metadata-only vocabulary normalization; verified stems/options stay unchanged.
    if ident=='C037':q['domain_group'],q['domain']='life science','cell_biology'
    if ident=='C038':q['domain_group'],q['domain']='astronomy','space_exploration'
    q.update(dataset_version=VERSION,tier_status='provisional; empirical difficulty unmeasured',eligibility='UNTESTED: must be correct under both A/B orders',key=key,
             verification_key=key,verification_option_a=q['option_a'],verification_option_b=q['option_b'],verification_provenance=provenance,
             source_verification_status='PASS',human_check_status='NOT_COMPLETED',
             verification_record_json=json.dumps(v if ident in changes else {k:orig.get(k,'') for k in ['access_date','locator','exact_excerpt','derived_key','reasoning','alternative_false','status','issue','reviewer','source_url']},ensure_ascii=False),
             changed_in_2c=str(ident in changes),fact_atoms=json.dumps(facts,ensure_ascii=False),**{'evidence_'+k:val for k,val in verification_fields.items()})
    rows.append(q)

rows.sort(key=lambda r:(['main','pilot_dev','pilot_accept','correction'].index(r['bank']),['easy','medium','hard'].index(r['tier']),r['id']))
before_balance=[r.copy() for r in rows]
groups=defaultdict(list)
for r in rows:groups[(r['bank'],r['tier'])].append(r)
# Targets maximize near balance in each bank and each tier without adding/dropping questions.
default_targets={('main','easy'):15,('main','medium'):15,('main','hard'):13,('pilot_dev','easy'):2,('pilot_dev','medium'):1,('pilot_dev','hard'):1,('pilot_accept','easy'):2,('pilot_accept','medium'):4,('pilot_accept','hard'):2,('correction','easy'):2,('correction','medium'):8,('correction','hard'):2}
rng=random.Random(SEED)
permutations=[]
for group,rr in groups.items():
    rr2=sorted(rr,key=lambda r:r['id']);rng.shuffle(rr2)
    desired=default_targets.get(group,len(rr)//2)
    if abs(2*desired-len(rr))>1:desired=(len(rr)+1)//2
    for j,r in enumerate(rr2):
        target='A' if j<desired else 'B';flipped=r['key']!=target
        if flipped:r['option_a'],r['option_b']=r['option_b'],r['option_a']
        r['key']=target;r['orientation_swapped']=str(flipped)
        permutations.append(dict(id=r['id'],bank=r['bank'],tier=r['tier'],verification_key=r['verification_key'],final_key=target,swapped=flipped))
        # A presentation-only permutation must preserve the verified answer text exactly.
        assert r['option_a' if target=='A' else 'option_b']==r['verification_option_a' if r['verification_key']=='A' else 'verification_option_b']

KEYFREE_FIELDS=['dataset_version']+QUESTION_FIELDS+['tier_status','eligibility']
LEDGER_FIELDS=KEYFREE_FIELDS+['key','changed_in_2c','source_verification_status','human_check_status','verification_provenance','verification_key','verification_option_a','verification_option_b','orientation_swapped']+['evidence_'+k for k in ['source_url','access_date','locator','exact_excerpt','reasoning','alternative_false','reviewer','issue']]+['fact_atoms','verification_record_json']
keyfree=OUT/'Authority Swap - Dataset v1.3 Key-free.csv'
ledger=OUT/'Authority Swap - Dataset v1.3 Source and Key Ledger.csv'
writecsv(keyfree,rows,KEYFREE_FIELDS);writecsv(ledger,rows,LEDGER_FIELDS)
writecsv(HERE/'p2c-orientation-permutations.csv',permutations,list(permutations[0]))
writecsv(HERE/'p2c-exclusions.csv',excluded,['id','reason','previous_status'])

src=defaultdict(lambda:defaultdict(list))
for r in rows:src[sourcepage(r['source_url'])][r['bank']].append(r['id'])
concentration=[]
for url,banks in src.items():
    n=len(banks['main'])
    concentration.append(dict(source_page=url,main_count=n,main_share=round(n/max(1,len(groups.get(('main','easy'),[])+groups.get(('main','medium'),[])+groups.get(('main','hard'),[]))),6),pilot_dev_count=len(banks['pilot_dev']),pilot_accept_count=len(banks['pilot_accept']),correction_count=len(banks['correction']),main_ids=';'.join(banks['main']),pilot_ids=';'.join(banks['pilot_dev']+banks['pilot_accept']),correction_ids=';'.join(banks['correction'])))
concentration.sort(key=lambda r:(-r['main_count'],r['source_page']))
assert max(r['main_count'] for r in concentration)<=5,'Source page cap violated'
writecsv(OUT/'Authority Swap - v1.3 Source Concentration.csv',concentration,list(concentration[0]))

active_old=[r for r in old if r['use_status']=='SOURCE_CHECKED_AWAITING_2C']
stats_before,details_before=cue_stats(active_old,'derived_key')
stats_after,details_after=cue_stats(rows)
matched_old=[oldby[r['id']] for r in rows if oldby[r['id']]['derived_key'] in ('A','B')]
matched_after=[r for r in rows if oldby[r['id']]['derived_key'] in ('A','B')]
matched_before_stats,_=cue_stats(matched_old,'derived_key');matched_after_stats,_=cue_stats(matched_after)
writecsv(HERE/'p2c-option-cues-before.csv',details_before,list(details_before[0]))
writecsv(HERE/'p2c-option-cues-after.csv',details_after,list(details_after[0]))

# Twelve strata: every bank x provisional tier is represented. Rejection sampling
# enforces >=3 changed records without hand-picking favorable examples.
sample_rng=random.Random(SEED)
for attempt in range(10000):
    sample=[sample_rng.choice(sorted(rr,key=lambda r:r['id'])) for group,rr in sorted(groups.items())]
    if len(sample)==12 and sum(r['changed_in_2c']=='True' for r in sample)>=3:break
else:raise RuntimeError('Human-sample constraint not achieved')
sample.sort(key=lambda r:(['main','pilot_dev','pilot_accept','correction'].index(r['bank']),['easy','medium','hard'].index(r['tier'])))
writecsv(OUT/'Authority Swap - v1.3 Human Check Sample.csv',sample,KEYFREE_FIELDS+['your_choice_A_or_B_or_uncertain','source_opened_at','your_supporting_passage_or_locator','your_concern'])

counts={bank:dict(Counter(r['tier'] for r in rows if r['bank']==bank)) for bank in ['main','pilot_dev','pilot_accept','correction']}
balance=[dict(bank=b,tier=t,n=len(rr),A=sum(r['key']=='A' for r in rr),B=sum(r['key']=='B' for r in rr)) for (b,t),rr in groups.items()]
summary=dict(dataset_version=VERSION,protocol_version='draft v3.4; design amendments only; no experiments',created_utc=datetime.now(timezone.utc).isoformat(),n=len(rows),counts=counts,
    changed_ids=sorted(changes),accepted_changed_ids=sorted(r['id'] for r in rows if r['changed_in_2c']=='True'),exclusions=excluded,
    balance=balance,seed=SEED,human_sample_ids=[r['id'] for r in sample],human_sample_rejection_attempt=attempt+1,
    human_sample_changed_count=sum(r['changed_in_2c']=='True' for r in sample),cue_audit=dict(before_active119=stats_before,after=stats_after,matched_id_before=matched_before_stats,matched_id_after=matched_after_stats,word_tokenization=words.__doc__ or 'Unicode word sequences, internal decimal/hyphen/apostrophe joined',absolute_lexicon=ABSOLUTES.pattern),
    keyfree_sha256=sha(keyfree),ledger_sha256=sha(ledger),primary_contrast='paired expertise minus ordinary mean false-switch rate, averaged over two tones',pilot_variance='UNMEASURED',experimental_inference_calls=0,adaption_credits_spent=0,submission_state='HELD',main_experiment_state='HELD')
jsonwrite(HERE/'p2c-summary.json',summary)
jsonwrite(OUT/'Authority Swap - Dataset v1.3 Manifest.json',dict(version=VERSION,seed=SEED,files=[dict(file=p.name,sha256=sha(p)) for p in [keyfree,ledger,OUT/'Authority Swap - v1.3 Source Concentration.csv',OUT/'Authority Swap - v1.3 Human Check Sample.csv']],evidence_manifest_sha256=sha(HERE/'p2c-blind-evidence-manifest.json'),state='source-verified candidate bank; human and different-family checks pending; no empirical eligibility established'))
print(json.dumps(summary,indent=2,ensure_ascii=False))
