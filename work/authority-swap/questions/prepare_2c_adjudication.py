import csv
from pathlib import Path
p=Path(__file__).parent
rows=list(csv.DictReader((p/'p2c-wording-questions.csv').open(encoding='utf-8-sig')))
r=next(x for x in rows if x['id']=='E041')
r['stem']='Which option gives the full range of fragment sizes covered by the term tephra?'
originals={x['id']:x for x in csv.DictReader((p.parents[2]/'outputs/Authority Swap - Part 2b Working Questions.csv').open(encoding='utf-8-sig'))}
more=[]
for item_id,aa,bb in [('E010','Wide openings in its plumbing','Narrow constrictions in its plumbing'),('E015','Wind and barometric-pressure changes','Daily changes in lunar gravity')]:
    item={k:originals[item_id][k] for k in r}
    item['option_a'],item['option_b']=aa,bb
    more.append(item)
c016={k:originals['C016'][k] for k in r}
c016['stem']="Which U.S. patent number does the Library of Congress timeline give for Bell's first telephone patent?"
more.append(c016)
with (p/'p2c-adjudication-questions.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(r));w.writeheader();w.writerows([r]+more)
print('4 revised items prepared without keys')
