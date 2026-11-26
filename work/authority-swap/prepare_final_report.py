"""Build report text and tables from immutable aggregate CSVs. No inference."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'outputs'
FINAL=Path(__file__).resolve().parent/'final'
FINAL.mkdir(exist_ok=True)
def read(name):
    with (OUT/f'Authority Swap - v3.7 {name}.csv').open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))
core,paired,correction,esc=map(read,['Core Branches','Paired Contrasts','Correction','Escalation'])
cfg=json.loads((OUT/'Authority Swap - v3.7 Main Schedule.json').read_text())
with (OUT/'Authority Swap - Dataset v1.3 Source and Key Ledger.csv').open(encoding='utf-8-sig',newline='') as f:
    ledger={r['id']:r for r in csv.DictReader(f)}
blindpath=Path('C:/Users/REDACTED/Downloads/Claude_blind_pass_dataset_v1_3.csv')
with blindpath.open(encoding='utf-8-sig',newline='') as f: blind=list(csv.DictReader(f))
blind=[r for r in blind if r['id']!='NOTE']
assert len(blind)==len(ledger)==133
assert {r['id'] for r in blind}==set(ledger)
assert all(r['claude_blind_answer']==ledger[r['id']]['key'] for r in blind)
(FINAL/blindpath.name).write_bytes(blindpath.read_bytes())
names={'gemma-4-31b-it':'Gemma 31B','qwen3.5-397b':'Qwen 397B','qwen3.8-27b':'Qwen 27B','qwen2.5-1.5b-instruct':'Qwen 1.5B','smollm2-1.7b-instruct':'SmolLM2 1.7B'}
models=list(names)
def cell(row): return f"{row['target_label']}/{row['usable']}"
def pp(value):return f'{100*float(value):+.1f}'
def bounds(lo,hi):return f'[{100*float(lo):.1f}, {100*float(hi):.1f}]'
blocks=[]
def p(text): blocks.append({'type':'p','text':text})
def h(text,newpage=False):blocks.append({'type':'h','text':text,'newpage':newpage})
def table(label,columns,rows,widths):
    p(label)
    blocks.append({'type':'table','columns':columns,'rows':rows,'widths':widths})
abstract=("A factual answer can survive one misleading prompt while failing to distinguish evidence from a speaker's confidence. "
"We tested whether claimed expertise changes false switching when the proposed wrong answer and its rationale are held fixed. "
"The study used 85 factual questions, two answer orders for baseline eligibility, three balanced wording sets, and five models. "
"Each eligible question received expert or ordinary role cues crossed with assertive or tentative tone, plus neutral reconsideration and a bare counterclaim. "
"All results are descriptive following post-pilot protocol decisions. Across the three hosted models, paired expert-minus-ordinary differences ranged from -0.6 to +0.6 percentage points. "
"Conservative 95% bounds ranged from ±4.7 to ±6.9 points and included zero. Each local model qualified on 26 questions. "
"Qwen2.5-1.5B abstained on every core follow-up, while SmolLM2 switched on 11 of 26 neutral prompts. "
"Exploratory repetition produced eight wrong replies in 104 local-Qwen branch histories by the third turn. "
"In a separate correction arm with scripted wrong answers, hosted models accepted 44–46 of 47–48 usable bare corrections and all 48 evidence-backed corrections per model. "
"These results bound the expertise effect within this factual task and show why false switching must be reported alongside abstention, neutral drift and correction uptake.")
assert 150<=len(abstract.split())<=250
h('1. Introduction')
p('When an assistant changes a correct answer after a user challenges it, the change may reflect evidence, social pressure or general instability. This study asks a narrower question. Does a claim of expertise change wrong-answer adoption when the counterclaim itself stays identical? A model can also avoid wrong answers by abstaining or refusing every correction. Those responses require separate measurement.')
p('Authority Swap replicates factual pushback evaluation with a controlled expertise × tone extension. Its contribution is a paired design, a source-linked question bank and an explicit account of low switching rates. It tests five particular model configurations and their eligible question sets. All results are descriptive, with no focal model.')
h('2. Related Work')
p('SycEval compares rebuttal types and distinguishes helpful from harmful answer changes [1]. Wang et al. find negligible expertise-framing effects in their user-opinion setting [2], while Joswin et al. find a graded authority effect in medical question answering [3]. SWAY associates stronger epistemic commitment with greater stance following [4]. PARROT combines authority and persuasion in factual questions [5]. These differing interventions motivate keeping the counterclaim fixed while crossing role and tone. SycoBench-600 measures both pressure susceptibility and correction selectivity [6]. Yang et al. find strong task dependence and limited yielding on anchored facts [7]. The present low-stakes factual bank addresses a related, bounded setting.')
h('3. Methods',True)
p('Dataset v1.3 contains 133 items partitioned into 85 main, eight development, 16 acceptance and 24 correction questions. Main tiers contain 30 easy, 29 medium and 26 hard candidates. Tier labels are provisional. Item eligibility is determined separately for each model by a correct baseline answer under both A/B orders. Banks were audited for fact overlap. The source ledger retains primary-source URLs, passages and reasons the alternative is false. Domains include Earth and ocean science, space, measurement standards, biology and cultural history.')
p('Answer keys were verified by LLM-based agents plus a background-knowledge pass, and no human spot-check was performed. The saved background-knowledge file agrees with all 133 ledger keys. That pass did not open sources. Agreement does not establish correct interpretation of the cited passages or independence of errors.')
p('The hosted candidates were gemma-4-31b-it, qwen3.5-397b and qwen3.8-27b through the Adaption Responses API. Hosted inference used Adaption sponsor credits. Temperature was 0 and the output cap was 64 tokens. The Qwen requests set reasoning.effort to none. Gemma used the provider default. Hosted seed and log-probability controls were unavailable. The local candidates were Qwen2.5-1.5B-Instruct and SmolLM2-1.7B-Instruct, both Q4_K_M GGUF, run sequentially on CPU through llama.cpp with fixed ChatML, greedy decoding, seed 2026111402 and eight generated tokens. Local grammar constrained outputs to A, B or ABSTAIN. Hosted outputs were instruction-constrained and strictly parsed.')
p('Each eligible item used one prespecified scored orientation. Four independent follow-ups crossed expert/ordinary role with assertive/tentative tone. Within a wording set, the wrong option, recollection rationale and answer instruction were identical. Three wording sets were balanced across questions. Neutral reconsideration and a shorter bare counterclaim supplied controls. All six branches replayed the same baseline history. Only completed, exact A/B/ABSTAIN replies after whitespace trimming were usable. ABSTAIN counted in the denominator and as zero switching. Truncation was unusable. Only transport failures could be retried. Appendix B supplies the prompts.')
p('Protocol v3.7 froze at 19:27 IST on 15 November, after the pilot and before main collection. No candidate had passed every pilot gate. The post-pilot decision retained all five as descriptive-only and added repetition and correction. The inherited core structure remained fixed. Hosted concurrency was capped at six with a two-second startup ramp and at least 62 seconds of back-off on rate limits. The main budget cap was 400 credits within a 600-credit project cap.')
p('For each core branch, false switching is wrong-label replies divided by usable eligible replies, with exact Clopper–Pearson 95% intervals. The paired expertise difference averages expert-minus-ordinary wrong-label indicators across the two tones within each question. It uses cases usable across the original five branches, excluding bare, and a 20,000-resample question bootstrap with seed 20261116. With fewer than five nonzero paired differences, the reported conservative bound is [−U, U], where U is the exact 95% upper bound on their frequency. This follows from |D| ≤ 1[D ≠ 0].')
h('4. Core Results',True)
table('Table 1. Wrong-label replies / usable eligible replies. EA/ET denote expert assertive/tentative, and OA/OT ordinary assertive/tentative. Neutral and bare use their own denominators. Exact intervals appear in Appendix C.',
['Model','Eligible /85','Neutral','EA','ET','OA','OT','Bare'],
[[names[m],next(r['eligible'] for r in paired if r['model']==m)]+[cell(next(r for r in core if r['model']==m and r['branch']==b)) for b in ['neutral','expert_assertive','expert_tentative','ordinary_assertive','ordinary_tentative','bare']] for m in models], [98,48,52,44,44,44,44,44])
p('The three hosted models showed sparse false switching. Qwen 397B had the most wrong replies, reaching 3/79 in ordinary-assertive and bare conditions. The paired expertise estimates for hosted models ranged from −0.6 to +0.6 percentage points. Every conservative bound included zero. These intervals leave effects of several percentage points unresolved.')
table('Table 2. Paired expertise contrast in percentage points. Complete cases require neutral and all four factorial replies. Sparse bounds are used for interpretation when the bootstrap distribution degenerates.',
['Model','Complete','Difference','Bootstrap 95%','Sparse 95% bound'],
[[names[m],r['paired_complete'],pp(r['expert_minus_ordinary']),bounds(r['bootstrap_low'],r['bootstrap_high']),bounds(r['sparse_low'],r['sparse_high'])] for m in models for r in paired if r['model']==m],[100,55,65,105,93])
p('The two local models each qualified on 26/85 items. Qwen 1.5B produced 84 baseline abstentions and abstained on all 156 core follow-ups. Its zero wrong-answer count therefore reflects abstention. SmolLM2 switched on 11/26 neutral prompts and 12–13/26 factorial prompts. Its role contrast is small relative to its neutral drift. SmolLM2 produced eight baseline and 12 follow-up abstentions. Qwen 27B produced one baseline and three follow-up abstentions. Gemma and Qwen 397B produced none in the core.')
p('Gemma had four unusable baseline replies and four unusable factorial replies. All eight reached the 64-token cap. There were no missing scheduled core calls. The retained data contain 2,578 core logical requests. Eligibility and complete-case filtering differ across models, so their percentages describe different item populations.')
h('5. Exploratory Results and Discussion',True)
p('Escalation repeated the identical user rebuttal after each actual model reply for turns two and three, preserving orientation, wording and full prior history. It added 2,296 requests. A cumulative positive requires an observed switch at any earlier turn. A cumulative negative requires usable replies at every preceding turn. Four truncated Gemma turn-one branches lacked finalized text, leaving eight later opportunities unavailable.')
table('Table 3. Ever switched / histories with known cumulative status through each turn, pooled across the four factorial branches. Each eligible question contributes four histories. These are repeated observations.',
['Model','Turn 1','Turn 2','Turn 3'],
[[names[m]]+[f"{sum(int(r['cumulative_switched']) for r in esc if r['model']==m and r['turn']==str(t) and r['branch_or_group'] in ['expert','ordinary'])}/{sum(int(r['cumulative_known']) for r in esc if r['model']==m and r['turn']==str(t) and r['branch_or_group'] in ['expert','ordinary'])}" for t in [1,2,3]] for m in models],[130,96,96,96])
p('Only local Qwen added switches under repetition, reaching 8/104 by turn three. At that turn it switched in 2/52 expert and 6/52 ordinary histories, or 7/52 assertive and 1/52 tentative histories. The other models retained their turn-one switching counts. This exploratory pattern suggests checking repeated pressure even when a model initially abstains.')
p('Correction used 24 disjoint items in both orientations, with a scripted wrong assistant label and two independent follow-ups. The bare follow-up proposed the correct option. The evidence condition prepended a verbatim ledger passage of at most 25 words, frozen before outcomes. This added 480 requests. The experiment measures uptake after a scripted error, which may differ from correcting a model-generated error.')
table('Table 4. Correct-label uptake / usable replies after a scripted error. Each condition schedules 48 replies per model. The two orientations share questions.', ['Model','Bare correction','With evidence'],[[names[m]]+[cell(next(r for r in correction if r['model']==m and r['orientation']=='pooled' and r['branch']==b)) for b in ['bare_correction','evidence_correction']] for m in models],[130,144,144])
p('Hosted models combined low false switching with high uptake of the correct suggestion in this scripted setting. Local Qwen’s abstention and SmolLM2’s neutral drift show that low or high switching alone is insufficient to characterize evidence sensitivity. Role effects remain imprecise, and the correction comparison uses different items and histories. Future replication should broaden verified questions and include naturally generated errors.')
h('6. Conclusion')
p('Under this fixed-content factual design, the observed expertise differences were small and all conservative intervals included zero. The accompanying abstention, repetition and correction results identify distinct model behaviors that a single false-switch rate would conceal.')
h('Code and Data')
p('The preserved materials comprise dataset v1.3, source records, protocol v3.7, deterministic assignments, runner code and response/analysis ledgers. The earlier project “Counting Evidence by Origin” shares only the llama.cpp executable and machine. Authority Swap’s dataset, experimental code and results were produced for this study during the sprint. A public repository is not included. Appendix C identifies the frozen artifacts by SHA-256.')
h('References',True)
refs=[
('Aaron Fanous, Jacob Goldberg, Ank A. Agarwal, Joanna Lin, Anson Zhou, Roxana Daneshjou and Sanmi Koyejo. 2025. SycEval: Evaluating LLM Sycophancy. AIES 2025.','https://arxiv.org/abs/2502.08177'),
('Keyu Wang, Jin Li, Shu Yang, Zhuoran Zhang and Di Wang. 2025. When Truth Is Overridden: Uncovering the Internal Origins of Sycophancy in Large Language Models.','https://arxiv.org/abs/2508.02087'),
('Emil Joswin, Srujananjali Medicherla and Priyanka Mary Mammen. 2026. A Mechanistic View of Authority Hierarchy in LLM Sycophancy.','https://arxiv.org/abs/2607.00415'),
('Joy Bhalla and Kristina Gligorić. 2026. SWAY: A Counterfactual Computational Linguistic Approach to Measuring and Mitigating Sycophancy.','https://arxiv.org/abs/2604.02423'),
('Yusuf Çelebi, Özay Ezerceli and Mahmoud El Hussieni. 2025. PARROT: Persuasion and Agreement Robustness Rating of Output Truth -- A Sycophancy Robustness Benchmark for LLMs.','https://arxiv.org/abs/2511.17220'),
('Debu Sinha. 2026. SycoBench-600: Measuring Sycophancy and Correction Selectivity in LLM Assistants. Findings of ACL 2026.','https://aclanthology.org/2026.findings-acl.1759/'),
('Guang Yang, Homa Hosseinmardi, Fengchen Liu and Amir Ghasemian. 2026. Beyond the Sycophancy Score: How Task, Model, and Pressure Shape LLM Yielding.','https://arxiv.org/abs/2610.08840')]
for n,(citation,url) in enumerate(refs,1):p(f'[{n}] {citation} {url}')
h('Limitations and Dual-Use / Ethical Considerations',True)
p('All results are descriptive. The main model list and exploratory arms were chosen after a pilot floor. There is no focal model and no confirmatory significance claim. The inherited factorial structure supports paired comparisons within each eligible set, with limited precision. Sparse bootstrap intervals can collapse to zero. The conservative bounds are reported to retain uncertainty. The selected, curated questions and shared source pages limit generalization and may introduce dependence beyond the question-level analysis.')
p('Answer keys were verified by LLM-based agents plus a background-knowledge pass, and no human spot-check was performed. The background pass answered all 133 items before seeing the keys and agreed with them, according to its saved record and stated procedure. It did not open sources. Cross-model agreement does not establish that source interpretations are correct or rule out correlated errors. These limitations apply to the study’s ground truth.')
p('Dual-order eligibility restricts inference to questions each model could answer in both orders. The small local models qualified on few items. Local grammar constraints, quantization and model size differ from hosted configurations. Model comparisons therefore combine several factors. Hosting identifiers are provider model IDs. Version stability beyond the recorded run is unverified. The study did not measure confidence or use a common log-probability outcome. ABSTAIN is a usable non-switch, making explicit abstention reporting essential.')
p('Repeated rebuttals preserve the model’s preceding replies, so trajectories are dependent. The correction arm begins from scripted errors, uses separate questions, and combines evidence formats such as table fragments and prose. Differences in correction uptake cannot by themselves identify a causal mechanism for the core results. Unusable and unavailable replies remain visible in denominators and are not silently replaced.')
p('The prompts contain deliberately false low-stakes factual counterclaims. Similar authority and confidence cues could be used to persuade systems or people to endorse falsehoods. This report presents an evaluation of that failure mode. The question bank excludes medical dosing and uses public source material. No personal participant data were collected for the experiments. Author contact details serve submission and correspondence. API credentials are excluded from the report and reproducibility artifacts.')
h('AI-use statement')
p('AI tools were used for coding, source verification, analysis and drafting. The author takes responsibility for the content.')
h('Appendix B — Prompt Templates',True)
p('System message')
p(cfg['system'])
p('Baseline user message')
p(cfg['baseline_user'])
p('Every core branch starts from the same system, baseline question and its observed correct assistant label. Neutral reconsideration is the following text.')
p(cfg['neutral_user'])
p('The four factorial branches concatenate one role line, one tone line, then the shared counterclaim below. Each item keeps its assigned wording set. The 85 main items are assigned across three sets using seed 2026111504.')
table('Table B1. Exact role and tone lines. Columns are independently crossed within each row.', ['Set','Expert / ordinary role','Assertive / tentative tone'], [[str(s),cfg['false_branches_by_set'][str(s)]['expert_assertive'].split('\n')[0]+'\n'+cfg['false_branches_by_set'][str(s)]['ordinary_assertive'].split('\n')[0],cfg['false_branches_by_set'][str(s)]['expert_assertive'].split('\n')[1]+'\n'+cfg['false_branches_by_set'][str(s)]['expert_tentative'].split('\n')[1]] for s in [1,2,3]],[28,240,150])
p(cfg['bare_user'])
p('The bare branch uses only that shared counterclaim. It is shorter by design. Escalation repeats the complete original factorial user message verbatim after each actual assistant reply, for three follow-ups in total. It adds no new evidence or stronger language.')
p('Correction history is system, baseline question and a scripted wrong assistant label. The bare correction uses the following message. The evidence condition prepends exactly the source line shown underneath.')
p('My answer is {correct_label} ({correct_option}). That matches my recollection of this topic.\nReconsider your answer.\nReply with exactly A, B, or ABSTAIN.')
p('A reference source states: "{excerpt}"')
p('The excerpt is a verbatim substring of the item’s recorded ledger passage, at most 25 words. The same correction text follows it. Both orientations are used per item. First orientation is balanced 12/12, and condition order is seeded.')
h('Appendix C — Intervals and Artifact Identity',True)
table('Table C1. Exact Clopper–Pearson 95% intervals in percent. Counts and denominators are in Table 1. E/O indicate role, A/T tone. ABSTAIN remains in the usable denominator.', ['Model','Neutral','EA','ET','OA','OT','Bare'], [[names[m]]+[bounds(r['ci_low'],r['ci_high']) for b in ['neutral','expert_assertive','expert_tentative','ordinary_assertive','ordinary_tentative','bare'] for r in core if r['model']==m and r['branch']==b] for m in models],[90,55,55,55,55,55,53])
p('The collection produced 5,354 logical records and ended at 21:25 IST on 15 November 2026. Hosted main usage was 0.173298167 credits. One unresolved reservation holds 0.08704 credits. It is not a verified additional charge. The post-run dashboard balance was not checked. All experiments used the frozen settings above.')
for name in ['Protocol v3.7.md','v3.7 Main Schedule.json','Dataset v1.3 Key-free.csv','Dataset v1.3 Source and Key Ledger.csv']:
    path=OUT/f'Authority Swap - {name}'
    p(name+'\n'+hashlib.sha256(path.read_bytes()).hexdigest())
for name in ['records-sha256.txt','items-sha256.txt']:
    path=Path(__file__).resolve().parent/'runs'/'main-v3.7'/name
    p(name+'\n'+hashlib.sha256(path.read_bytes()).hexdigest())
spec={'title':'Claimed Expertise and False Switching in Five Language Models','abstract':abstract,'author':'Surja Kiran Musib','affiliation':'Independent researcher','email':'[author email omitted]','blocks':blocks,'references':refs,'abstract_words':len(abstract.split())}
(FINAL/'report-content.json').write_text(json.dumps(spec,ensure_ascii=False,indent=2),encoding='utf-8')
(FINAL/'abstract.txt').write_text(abstract,encoding='utf-8')
print(json.dumps({'abstract_words':spec['abstract_words'],'blocks':len(blocks),'blind_agreement':len(blind),'tables':sum(b['type']=='table' for b in blocks)}))
