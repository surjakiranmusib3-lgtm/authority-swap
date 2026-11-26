"""Produce Part 2c review artifacts from the frozen dataset and actual audits."""
from pathlib import Path
import csv,json,hashlib,math
from collections import Counter,defaultdict
from datetime import datetime,timezone

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];OUT=ROOT/'outputs'
def readcsv(p):return list(csv.DictReader(p.open(encoding='utf-8-sig')))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest().upper()
def writecsv(p,rows,fields):
    with p.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
summary=json.loads((HERE/'p2c-summary.json').read_text(encoding='utf-8'))
rows=readcsv(OUT/'Authority Swap - Dataset v1.3 Source and Key Ledger.csv');by={r['id']:r for r in rows}
audit=json.loads((HERE/'p2c-final-fact-audit.json').read_text(encoding='utf-8-sig'))
audited={r['id']:r for r in audit['items']}
for r in rows:
    assert r['id'] in audited
    # Presentation permutations do not change a fact; substantive stems must match the audit.
    assert r['stem']==audited[r['id']]['stem'],('Fact audit stale for',r['id'])
factrows=[]
for r in rows:
    a=audited[r['id']];atoms=a['fact_atoms']+a.get('supporting_fact_atoms',[])
    factrows.append(dict(id=r['id'],bank=r['bank'],tier=r['tier'],fact_ids=';'.join(x['id'] for x in atoms),propositions=json.dumps(atoms,ensure_ascii=False),event_ids=';'.join(a.get('event_ids',[])),source_url=r['source_url'],source_locator=r['source_locator'],source_key_verifier=r['evidence_reviewer'],fact_auditor='/root/p2c_fact_audit',finding='No residual fact/event overlap found in recorded audit; adjacent concepts and source reuse remain'))
writecsv(OUT/'Authority Swap - v1.3 Fact Disjointness Ledger.csv',factrows,list(factrows[0]))

new_ids={r['id'] for p in ['replacement','diversify'] for r in readcsv(HERE/f'p2c-{p}-questions.csv')}|{'C037','C038'}
disputes={'C013':'NPS construction-start discrepancy (1875/1876); comparative ordering unaffected, corrected citation rechecked',
          'C024':'Previous pedestal-height question ambiguous; replaced with a different knowledge question',
          'E041':'Previous includes wording allowed a true subset; revised full-range question independently rechecked',
          'C016':'Earlier stem supplied the year tested by C004; removed that date and rechecked',
          'S022':'NASA mean-temperature metric is at one bar; does not claim minimum atmospheric temperature',
          'E019':'Held rainfall, slope and vegetation comparable; soil-runoff relationship remains general, not universal',
          'E040':'Plausibility concern remains: evaporation-creates-salts distractor may be easy; provisional tier and pilot/correction baselines must reveal this'}
queue=[]
for r in rows:
    if r['changed_in_2c']=='True' or r['id'] in disputes:
        queue.append({**{k:r[k] for k in ['id','bank','tier','stem','option_a','option_b','source_url','source_locator']},'change_type':'NEW_FACT_REPLACEMENT' if r['id'] in new_ids else 'WORDING_OR_CITATION_REVISION' if r['changed_in_2c']=='True' else 'RETAINED_WITH_QUALITY_NOTE','review_note':disputes.get(r['id'],'Fresh source verification recorded; independent second review still useful'),'second_reviewer_choice':'','second_reviewer_concern':''})
writecsv(OUT/'Authority Swap - v1.3 Second Reviewer Queue.csv',queue,list(queue[0]))

sample=readcsv(OUT/'Authority Swap - v1.3 Human Check Sample.csv')
concentration=readcsv(OUT/'Authority Swap - v1.3 Source Concentration.csv')
new=[r['id'] for r in rows if r['id'] in new_ids]
revised=[r['id'] for r in rows if r['changed_in_2c']=='True' and r['id'] not in new_ids]
before=summary['cue_audit']['before_active119'];after=summary['cue_audit']['after']
def table(headers,data):return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|']+['| '+' | '.join(str(x).replace('|','/') for x in rr)+' |' for rr in data])
lines=['# Authority Swap — Part 2c review and freeze','',
'Review files: '+ ' · '.join(f'[{label}](<{(OUT/name).as_posix()}>)' for label,name in [('Key-free questions','Authority Swap - Dataset v1.3 Key-free.csv'),('Source and key ledger — open after blind review','Authority Swap - Dataset v1.3 Source and Key Ledger.csv'),('Human-check worksheet','Authority Swap - v1.3 Human Check Sample.csv'),('Second-reviewer queue','Authority Swap - v1.3 Second Reviewer Queue.csv'),('Fact disjointness ledger','Authority Swap - v1.3 Fact Disjointness Ledger.csv'),('Source concentration CSV','Authority Swap - v1.3 Source Concentration.csv')]),'',
'**Part 2c only. Main experiment and submission HELD. Part 3 has not begun.** Dataset v1.3 is a source-verified candidate bank, not a collection of model results. All difficulty labels remain provisional; each model must later answer correctly under both A/B orders to qualify a main item. Human and different-family review have not been completed.','',
'## Frozen counts and presentation balance','',table(['Bank','Tier','Items','A keys','B keys'],[(x['bank'],x['tier'],x['n'],x['A'],x['B']) for x in summary['balance']]),'',
f"Total {len(rows)} items. Main retains 30 easy, 29 medium and 26 hard candidates: 85 overall. The five retired slots are C027, C028, S017, S025 and S027. No weak items were added merely to make every tier 30. Consequently the achievable main balances are 15/15, 15/14 and 13/13. Pilot acceptance hard is now 2/2. All answer text is preserved by deterministic option swaps, with mapped final keys checked against the independently derived answer text.",'',
f"Random seed: **{summary['seed']}**. Presentation randomization shuffles IDs inside each bank × tier and assigns the recorded near-half A/B target. Option-order changes alone are presentation permutations, not changes in the verified factual claim. Both orientations are still required at baseline.",'',
'## Source verification and changes','',
f"{len(new)} items use new facts; {len(revised)} additional items have wording or citation revisions. Every accepted content revision has a fresh key-file-blind primary-source derivation. Unchanged questions inherit their Part 2b blind verification. Reviewers were fresh Astra agents authorized by the user, with only their own key-free input packet and source links. The coordinator had seen prior keys and is not called blind. This is same-family AI review, not independent human or different-family validation.",'',
'New facts: '+', '.join(new)+'.','',
'Wording/citation revisions: '+', '.join(revised)+'.','',
'All new/revised items and retained disputed items are listed in **Authority Swap - v1.3 Second Reviewer Queue.csv**. The raw reviewer records preserve earlier flags, including E041 and C013; their later decisions are separate records rather than overwritten history. No draft-key file was opened for this Part 2c assembly. Review input/output hashes are frozen in the evidence manifest.','',
'E021–E030, E033 and E037 now require factual knowledge or conceptual discrimination rather than arithmetic on facts provided in the stem. C024 is re-topicked. S010, S028 and S030 no longer use the silver/iodine comparisons; S029 retains its atomic-number relation with the unnecessary atomic-weight clause removed. S022 uses the requested wording. E034 has a sedimentary-rock distractor. E035 uses Yes/No; E041 asks for the full size range and has no “Only” cue. C038 now concerns a space-probe landing, and C037 concerns a cell organelle. C016 no longer supplies C004’s answer year.','',
'C013: the independently opened NPS construction account supplies both comparison dates. NPS pages differ between 1875 and 1876 for the statue start; either is earlier than the pedestal start in 1884. The report must not assert a uniquely resolved French start year. E011 retains the accessible USGS DYFI citation verified in Part 2b. The NPS Grand Canyon age table remains identified as the adaptation of the 2020 Update, page updated March 12, 2024; its retained comparison is approximate rather than an immutable numerical age.','',
'Access/provenance limits: the British Museum guide and the 2022 Nobel press PDF initially returned 403 but were recovered through indexed official-source opens. S028 now uses a verified section locator instead of the erroneous draft page number; its printed page number is not asserted. The original Nobel 1911 pages could not be opened; C021 is supported by the accessible NIST reproduction of the primary award citation, and that source-chain limitation remains in its ledger. C024 museum-project provenance and direct British Museum corroboration are recorded. E041 uses an opened USGS HVO source after the original FAQ timed out. Full supplementary sources and reviewer notes are preserved in verification_record_json in the source/key ledger.','',
'## Option cues','',
table(['Metric','Before: 119 active v1.2','After: v1.3'],[(label,before.get(key,0),after.get(key,0)) for label,key in [('Correct option shorter (words)','correct_words_shorter'),('Equal word length','correct_words_equal'),('Correct option longer (words)','correct_words_longer'),('Correct options with absolute words','correct_options_with_absolute'),('Wrong options with absolute words','wrong_options_with_absolute'),('Correct option shorter (characters)','correct_characters_shorter'),('Equal character length','correct_characters_equal'),('Correct option longer (characters)','correct_characters_longer')]]),'',
'Words are Unicode word sequences; internal decimals, apostrophes and hyphens stay joined. Absolute-word scan: all, only, always, never, must, none, every, solely, entirely, exclusively, alone, completely. Yes/No response labels are not treated as giveaway universal quantifiers. Counts compare different bank sizes after replacements; matched-ID before/after counts are also saved in p2c-summary.json. Length equality is not proof that all stylistic cues are absent, and natural names are not padded merely to equalize characters.','',
'## Source concentration — main cap of five','',
'The previous 17 NASA-table and 13 IUPAC-list items were totals across the 119 retained records. Their previous main counts were 12 and 9. The cap applies to main items per source page. The complete table below separates all banks; source-query identifiers are preserved and tracking/section parameters removed for page counting.','',
table(['Primary source page','Main','Dev pilot','Acceptance pilot','Correction','Main IDs'],[(f"[{r['source_page']}]({r['source_page']})",r['main_count'],r['pilot_dev_count'],r['pilot_accept_count'],r['correction_count'],r['main_ids']) for r in concentration]),'',
'Source concentration CSV records the same table. Main-source maximum is checked programmatically at five; a different URL for the same underlying page is not used to evade the cap. Source pages may contain related facts even when questions do not test the same fact.','',
'## Fact and event disjointness','',
'The independent quality audit maps every candidate to canonical fact propositions and event IDs. The exported **Fact Disjointness Ledger** joins those IDs to the final questions and verified source citations. No residual cross-bank fact/event overlap or within-main fact duplicate was found in this recorded audit. This is an audit finding, not a mathematical proof that semantically related facts are statistically independent. Shared entities, domains and pages remain and must be acknowledged in the paper.','',
'Documented boundaries: calcite cleavage versus the mineral deposited in travertine; Rosetta Stone ruler versus script (both main); replacement-torch installation versus original-torch relocation (different events); RNA codon count versus the identity of a particular stop codon. C038 removes the shared transcontinental-call event entirely. The five retired IDs and all replaced original facts remain preserved in older version files.','',
'The prior project, *Counting Evidence by Origin*, was inspected read-only through its generator and saved trial prompts: it uses fictional sensor, cabinet, gallery and drawer reports with synthetic A/B observations. No external factual question or trial record from it is reused here. Planned llama.cpp/runner infrastructure reuse, any later code reuse and hosted-credit use must still be disclosed. The earlier project’s exact creation date and submission receipt are not newly established by this audit.','',
'## Your twelve source checks','',
f"Please complete these **before any Part 4 pilot**; they can be checked now. The sample was drawn with seed {summary['seed']}, one item from every bank × provisional-tier stratum, using rejection sampling until at least three content-revised/new items were included. Accepted draw: {summary['human_sample_rejection_attempt']}; {summary['human_sample_changed_count']} changed items. Do not look at the source/key ledger until you have recorded your own choices. This prevents the answer key from steering your check.",'',
'For each row: open the primary source, find the named section/table, write A/B/uncertain and the source passage or table cells that justify it, and record any ambiguity or failure to open the source. The sample CSV provides blank columns for these answers. Do not guess a key for a disputed item.','',
table(['ID','Bank / tier','Question and options','Exact source location'],[(r['id'],r['bank']+' / '+r['tier'],r['stem']+' A: '+r['option_a']+'; B: '+r['option_b'],f"[{r['source_locator']}]({r['source_url']})") for r in sample]),'',
'A different-family reviewer should receive only **Dataset v1.3 Key-free.csv**, derive and save dated source-based keys first, then receive the separate Source and Key Ledger for comparison. Neither that review nor your twelve checks has been claimed complete.','',
'## Verification-time estimate and cut-down fallback','',
'Planning estimate for one careful sequential reviewer: 2 minutes/easy, 3/medium, 4/hard, plus 20% for access failures and adjudication. This is a workload estimate, not a measured per-item benchmark. Main: 251 minutes; development pilot: 21; acceptance pilot: 49; correction: 71. Total: 392 minutes (about 6½ hours), or about 7 hours 50 minutes with the contingency. Twelve human spot checks should take roughly 40–60 minutes, longer if a source fails. AI source review has already covered all accepted rows; the user is only committed to the twelve-item check.','',
'Default: retain the verified 85 main +24 pilot +24 correction candidates and finish the twelve human checks. If a fresh exhaustive human audit must fit a five-hour block, freeze a pre-result subset of 40 main (14 easy/13 medium/13 hard), all 24 pilot and 20 correction (5 easy/15 medium), chosen by seeded sampling with near-balanced keys and source cap preserved. Estimated 244 minutes +20% =293 minutes. This is a conservative exploratory fallback, not equivalent evidence. A less severe runtime fallback is one focal model and up to 60 eligible main items, preserving the full 2×2 plus neutral-control design. Neither fallback is activated automatically; record its selection before viewing treatment effects.','',
'## Power implication','',
'There are at most 85 main pairs per model, and fewer after the both-order eligibility screen. The pilot variance has not been measured; no variance of 0.20 is assumed. For per-question D = mean(expert switches over two tones) − mean(ordinary switches over two tones), D lies in [−1,1]. Approximate 95% interval half-width is 1.96 s_D/√n; two-sided 5%/80%-power detectable difference is approximately 2.80 s_D/√n. Use the actual pilot estimate and paired question-level intervals later; small-sample/non-normal behavior needs checked analysis, not this planning approximation.','',
table(['Eligible n','Conservative s_D=1 CI half-width','Conservative s_D=1 detectable difference'],[(n,f'{1.96/math.sqrt(n)*100:.1f} percentage points',f'{2.80/math.sqrt(n)*100:.1f} percentage points') for n in [85,60,40]]),'',
'These bounds are not predictions of variance. Reducing 90 to 85 increases standard errors by about 2.9% at fixed variance; 85 to 60 increases them by about 19.0%. The bank cannot currently support a claim of adequate power for 5–10 percentage-point effects. Report confidence intervals and which effect sizes they rule out, especially under a cut-down sample; do not interpret non-significance as no authority effect.','',
'## Files, integrity and holds','',
f"Key-free CSV SHA-256: `{summary['keyfree_sha256']}`.",'',f"Source/key ledger SHA-256: `{summary['ledger_sha256']}`.",'',
'The JSON manifest includes file hashes, evidence-manifest hash and sampling seed. Protocol is draft v3.4; no model or analysis results have been generated. Runtime/model access is Part 3 only. User-reported Adaption balance: 2,750, unverified. Project cap: 150 credits unless explicitly raised. **0 experimental inference calls, 0 Adaption credits and no API key access in Part 2c.** Chat-agent work is not a claim of zero chat usage; that allowance is not measured here.','',
'**STOP. Await “Proceed to Part 3.” Main experiment and submission remain held.**','']
(OUT/'Authority Swap - Part 2c Review.md').write_text('\n'.join(lines),encoding='utf-8')
# Extend the artifact manifest without changing dataset bytes.
manifest_path=OUT/'Authority Swap - Dataset v1.3 Manifest.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
for name in ['Authority Swap - v1.3 Fact Disjointness Ledger.csv','Authority Swap - v1.3 Second Reviewer Queue.csv','Authority Swap - Part 2c Review.md']:
    manifest['files']=[r for r in manifest['files'] if r['file']!=name]
    manifest['files'].append(dict(file=name,sha256=sha(OUT/name)))
manifest['fact_audit_sha256']=sha(HERE/'p2c-final-fact-audit.json')
manifest_path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(dict(review_items=len(queue),new=len(new),revised=len(revised),sample_ids=summary['human_sample_ids'],fact_ledger_rows=len(factrows)),indent=2))
