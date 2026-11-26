import csv
from pathlib import Path
p=Path(__file__).parent
rows={r['id']:r for r in csv.DictReader((p/'p2c-wording-questions.csv').open(encoding='utf-8-sig'))}
rr=[rows['C013'],rows['E019']]
rr[0]['source_url']='https://www.nps.gov/stli/learn/historyculture/places_creating_statue.htm'
rr[0]['source_locator']='1865-1886 account, paragraph describing construction in France and construction of the pedestal'
rr[1]['stem']='With rainfall, slope and vegetation otherwise comparable, which soil would generally produce more surface runoff?'
with (p/'p2c-citation-questions.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rr[0]));w.writeheader();w.writerows(rr)
print('2 key-free items for fresh review')
