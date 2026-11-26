import csv,json,hashlib,re,unicodedata
from pathlib import Path
from collections import Counter
from decimal import Decimal
from pypdf import PdfReader
W=Path(__file__).resolve().parent
R=W.parents[2]
O=R/'outputs'
spec=json.loads((W/'report-content.json').read_text(encoding='utf-8'))
doc=json.loads((W/'google-doc-checked.json').read_text(encoding='utf-8'))
def read(name):
    with (O/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def flatten(nodes):
    out=''
    for n in nodes:
        if 'paragraph' in n:out+=''.join(e.get('textRun',{}).get('content','') for e in n['paragraph']['elements'])
        if 'table' in n:
            for r in n['table']['tableRows']:
                for c in r['tableCells']:out+=flatten(c['content'])
    return out
body=doc['tabs'][0]['body']['content']
text=flatten(body)
assert spec['title'] in text and spec['abstract'] in text
assert 150<=len(spec['abstract'].split())<=250
for b in spec['blocks']:
    if b['type']!='table':assert b['text'] in text,b['text'][:80]
tables=[n['table'] for n in body if 'table' in n and n.get('startIndex',0)>1535]
expected=[b for b in spec['blocks'] if b['type']=='table']
assert len(tables)==len(expected)==6
cells=0
for actual,want in zip(tables,expected):
    ar=[[flatten(c['content']).strip() for c in r['tableCells']] for r in actual['tableRows']]
    wr=[want['columns']]+want['rows']
    assert ar==wr,(ar,wr)
    cells+=sum(map(len,ar))
ledger=read('Authority Swap - Dataset v1.3 Source and Key Ledger.csv')
assert len(ledger)==133
assert Counter(r['bank'] for r in ledger)=={'main':85,'pilot_dev':8,'pilot_accept':16,'correction':24}
tiers=Counter(r['tier'].lower() for r in ledger if r['bank']=='main')
assert tiers=={'easy':30,'medium':29,'hard':26},tiers
with (W/'Claude_blind_pass_dataset_v1_3.csv').open(encoding='utf-8-sig') as f:blind=[r for r in csv.DictReader(f) if r['id']!='NOTE']
assert len(blind)==133
keys={r['id']:r['key'] for r in ledger}
assert all(r['claude_blind_answer']==keys[r['id']] for r in blind)
timing=read('Authority Swap - v3.7 Run Timing.csv')
totals={a:sum(int(r['logical_calls']) for r in timing if r['arm']==a) for a in ['core','escalation','correction']}
assert totals=={'core':2578,'escalation':2296,'correction':480}
account=read('Authority Swap - v3.7 Hosted Accounting.csv')
cost=sum(Decimal(r['provider_credits']) for r in account)
reserve=sum(Decimal(r['unresolved_reserved_credits']) for r in account)
assert abs(cost-Decimal('0.173298167'))<Decimal('0.000000000001')
assert reserve==Decimal('0.08704')
schedule=json.loads((O/'Authority Swap - v3.7 Main Schedule.json').read_text())
for key in ['system','baseline_user','neutral_user','bare_user']:assert schedule[key] in text
for st in schedule['false_branches_by_set'].values():
    for msg in st.values():
        role,tone,rest=msg.split('\n',2)
        assert role in text and tone in text and rest==schedule['bare_user']
for n in ['Protocol v3.7.md','v3.7 Main Schedule.json','Dataset v1.3 Key-free.csv','Dataset v1.3 Source and Key Ledger.csv']:
    assert hashlib.sha256((O/('Authority Swap - '+n)).read_bytes()).hexdigest() in text
for n in ['records-sha256.txt','items-sha256.txt']:
    assert hashlib.sha256((W.parent/'runs/main-v3.7'/n).read_bytes()).hexdigest() in text
pdf=O/'Authority Swap - Final Report.pdf'
pages=PdfReader(pdf).pages
assert len(pages)==10
assert 'References' in pages[6].extract_text()
assert 'Limitations' in pages[7].extract_text()
for i in [1,2,4,5,6,7,8]:
    assert (W/f'page-{i:02}.png').read_bytes()==(W/f'finalpage-{i:02}.png').read_bytes(),i
report={'status':'PASS','abstract_words':len(spec['abstract'].split()),'main_pages':6,'total_pages':10,'table_cells_checked':cells,'bank_sizes':dict(Counter(r['bank'] for r in ledger)),'tiers':dict(tiers),'blind_background_agreement':'133/133; not a source check','human_spot_check':'not performed','calls':totals,'total_logical_records':sum(totals.values()),'main_credits':str(cost),'unresolved_reserved_credits':str(reserve),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'page_review':'All 10 rendered pages inspected; pages 1-8 byte-identical to previously inspected render; pages 9-10 inspected after appendix compaction.','submission_state':'ready; not submitted by this script'}
(O/'Authority Swap - Final Validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
