import csv,json
from pathlib import Path
root=Path(__file__).resolve().parents[3]
src=root/'outputs/Authority Swap - Part 2a Draft Questions.csv'
rows=list(csv.DictReader(src.open(encoding='utf-8-sig')))
issues={}
def flag(ids,text):
    for i in ids: issues.setdefault(i,[]).append(text)
hard=[f'E{i:03d}' for i in range(21,31)]+['E033','E037']
flag(hard,'Supplied-number arithmetic; exclude until replaced with factual or nontrivial source question in 2c.')
flag(['C021'],'Nested intervals tautology; revised to non-overlapping administration periods, independent verification pending.')
flag(['C005'],'Specify typical human somatic body cell; revised, independent verification pending.')
flag(['S038','S029'],'Cross-bank silver/cadmium underlying-fact overlap; replace S038 in 2c.')
flag(['E017','E027'],'Kaibab/Tapeats underlying-fact overlap; replace E027 in 2c.')
flag(['E007','E028'],'Spring-tide phase fact overlap; replace E028 in 2c.')
flag(['C015','C027'],'Gutenberg vellum fraction/count overlap; replace C027 in 2c.')
flag(['S016','S017','S025','S027'],'SI prefix concentration; retain S016 provisionally, diversify others in 2c; full fact audit pending.')
flag(['C005','C028'],'Chromosome total/autosome overlap; replace C028 in 2c.')
flag(['E009','C041','E040','E041','E045','E046'],'Giveaway distractor revised; independent source/key check still pending.')
flag(['E011'],'Canonical USGS URL timed out; alternative USGS page returned robot check. Source access remains unresolved.')
flag(['C013'],'Reviewer reported cited page omits pedestal start; alternate NPS source required.')
flag(['C024'],'Reviewer reported 154 ft means ground-to-pedestal, not pedestal alone; clarification required.')
revisions={
'C005':('How many chromosome pairs are usually found in a typical human somatic (body) cell?','22','23'),
'C021':('Which Yellowstone administration period lasted longer: the initial civilian administration before the U.S. Army, or U.S. Army administration before NPS took over?','Initial civilian administration','U.S. Army administration'),
'C041':('In which language was the Gutenberg Bible printed?','Latin','German'),
'E009':('What chiefly creates the brackish water of a typical coastal estuary?','Mixing river fresh water with seawater','Evaporation concentrating river water'),
'E040':('Which is a major natural source of dissolved salts in the ocean?','Evaporation creating new dissolved salts','Weathering of rocks on land'),
'E041':('What does the term tephra include after an explosive eruption?','Ejected rock fragments ranging from ash to blocks','Only ejected particles smaller than two millimetres'),
'E045':('In the ocean sound channel, sound can travel great distances because it does what?','Refracts up and down within the channel','Repeatedly reflects off the sea surface and seafloor'),
'E046':('Which process produces much of the clay in Yellowstone mudpots?','Mechanical grinding of rock by fast surface streams','Acid breaks down surrounding rock')}
excluded=set(hard+['S038','C027','C028','S017','S025','S027'])
for r in rows:
    ident=r['id']; r['audit_findings']=' | '.join(issues.get(ident,[]))
    r['verification_status']='PENDING_BLIND_CHECK'
    r['use_status']='HELD_FOR_2B_2C'
    if ident in excluded:r['use_status']='EXCLUDE_PENDING_REPLACEMENT_2C'
    if ident in revisions:
        r['stem'],r['option_a'],r['option_b']=revisions[ident]
        r['draft_status']='REVISED_UNVERIFIED_2B'
    if ident=='C041':r['source_locator']='Catalog link: [Bible in Latin], 1454-1455'
    if ident=='C021':r['source_locator']='Timeline entries 1872, 1886 and 1918; durations must be derived from source, not supplied in prompt'
out=root/'outputs/Authority Swap - Part 2b Working Questions.csv'
with out.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
audit=root/'outputs/Authority Swap - Part 2b Audit Dispositions.csv'
with audit.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['id','findings','action']);w.writeheader()
    for r in rows:
        if r['id'] in issues:w.writerow({'id':r['id'],'findings':r['audit_findings'],'action':r['use_status']})
print(json.dumps({'records':len(rows),'revised':len(revisions),'excluded_pending_replacement':len(excluded),'blind_verified':0,'keys_opened':False}))
