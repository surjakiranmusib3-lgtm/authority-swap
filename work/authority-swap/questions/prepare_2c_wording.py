"""Prepare key-free wording amendments for a fresh reviewer; no draft keys read."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
source = ROOT / 'outputs/Authority Swap - Part 2b Working Questions.csv'
rows = {r['id']: r for r in csv.DictReader(source.open(encoding='utf-8-sig'))}
changes = {
    'S006': dict(stem='Which SI base unit measures thermodynamic temperature, kelvin or second?', option_a='second', option_b='kelvin', source_locator='SI base units table, thermodynamic temperature and time rows'),
    'S022': dict(stem='Which planet, Neptune or Saturn, has both a longer orbital period and a lower mean temperature than Uranus?'),
    'S029': dict(stem='Which element is exactly one atomic number above silver, cadmium or indium?', source_locator='2022 periodic-table PDF, atomic numbers of silver, cadmium and indium'),
    'E034': dict(option_a='Breccia', option_b='Coal', source_locator='Clastic Sedimentary Rock and Biologic Sedimentary Rock sections'),
    'E035': dict(option_a='Yes', option_b='No'),
    'E041': dict(option_a='Ejected rock fragments ranging from ash to blocks', option_b='Ejected rock fragments smaller than two millimetres'),
    'E046': dict(option_a='Streams mechanically grind surrounding rock', option_b='Acid chemically breaks down rock'),
    'C013': dict(option_a='Statue construction in France', option_b='Pedestal construction in America'),
    'E014': dict(option_a='Wind and tides', option_b='Temperature and salinity'),
    'E018': dict(option_a='Rapid cooling above ground', option_b='Slow cooling deep underground'),
    'E019': dict(option_a='Clay soil', option_b='Sandy soil'),
    'C037': dict(domain_group='culture_biology', domain='Cell biology', stem='Which organelle helps process and package proteins and lipids for export from a cell?', option_a='Mitochondrion', option_b='Golgi apparatus', source_url='https://www.genome.gov/genetics-glossary/golgi-body?id=95', source_locator='Definition and Narration'),
    'C038': dict(domain_group='science_standards', domain='Space exploration', stem='Which probe made the first successful landing on Titan?', option_a='Huygens', option_b='Galileo', source_url='https://www.esa.int/Newsroom/Press_Releases/Europe_reaches_new_frontier_Huygens_lands_on_Titan', source_locator='14 January 2005 press release, opening account and successful landing paragraphs'),
}
fields = ['id','bank','tier','domain_group','domain','stem','option_a','option_b','source_url','source_locator']
out = Path(__file__).parent / 'p2c-wording-questions.csv'
with out.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
    for i,change in changes.items():
        r={k:rows[i][k] for k in fields};r.update(change);w.writerow(r)
print(str(out),len(changes))
