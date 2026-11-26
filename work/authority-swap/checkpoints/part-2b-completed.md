# Authority Swap | Part 2b completed checkpoint

14 November 2026 IST. **Part 2b complete. STOPPED before Part 2c.** This supersedes the interrupted Part 2b checkpoint; the interrupted record is retained as provenance.

## Finished

Three fresh, user-authorized Astra High reviewers independently opened primary sources for the 138 working candidates. They received the key-free working CSV and no prior conversation, raw draft fragments or draft-key file. Each saved source-derived answers, dated URLs, exact supporting passages/table cells, explanations and false-alternative checks. The evidence files were frozen and hashed before the assembly script first opened `draft-keys-v1.csv` for comparison. The coordinator had prior exposure to some draft keys, so its work is not described as blind; the fresh reviewers' source derivations were blind to that file. This is AI verification, not a substitute for the user's later 12-item check.

Results: **137 source-supported keys; one unresolved wording/source interpretation (C024).** For unchanged items, **129 keys match** the draft, zero disagree, and C024 is unresolved. Eight revised questions were independently verified in their new form and are not compared to obsolete draft keys.

Source support does not clear quality exclusions: **119 candidates await the Part 2c audit**, **18 remain excluded pending replacement**, and **C024 remains flagged**. The 119 comprise 74 main, 21 pilot and 24 correction candidates. Main tier counts are 30 easy, 29 medium, 15 hard. The target of 30 usable main candidates per tier is therefore **not met**; Part 2c must address replacements and feasibility. No bank is frozen or model-eligible.

## External-audit findings and disposition

1. E021–E030, E033 and E037 remain excluded for supplied-number arithmetic and need factual/nontrivial replacements in 2c. Their underlying source facts were checked, but that does not repair the design defect.
2. C021 now compares separate initial civilian and Army administration periods without putting dates in the question. The independently checked NPS dates yield 14 versus 32 years. C005 now specifies a typical human somatic (body) cell.
3. S038, C027, C028, S017, S025 and S027 remain excluded for fact overlap or prefix concentration. E027/E028 are already among the twelve exclusions. Counterpart items are only provisionally retained. Broader underlying-fact overlap review is reserved for 2c.
4. E009, C041, E040, E041, E045 and E046 have revised questions/distractors with independently supported keys. C041 now tests Latin versus German. Distractor plausibility and tier placement still require the 2c audit.
5. **E011 resolved** using the accessible USGS [DYFI Scientific Background](https://earthquake.usgs.gov/data/dyfi/background.php), “What is Intensity? A Measure of Earthquake Effects.” The original FAQ access failure is retained in provenance; the ledger uses the accessible source. The NPS [numeric ages page](https://home.nps.gov/articles/000/grcatime-numeric-ages.htm) was independently verified as an adaptation of the **2020 Update**, last updated **March 12, 2024**. Its approximate, revisable table values are not universal immutable ages.

Additional finding: **C024 cannot be keyed unambiguously** because the cited 154-foot measure is labeled ground-to-pedestal while the question asks about the pedestal itself. It needs clarified endpoints or replacement in 2c. C013 was resolved with an alternative NPS [construction history](https://www.nps.gov/stli/learn/historyculture/places_creating_statue.htm); NPS pages differ on the statue's construction-start year (1875/1876), but both precede the cited 1884 pedestal start, leaving its comparative answer unchanged. Hydrology and tephra source alternatives are documented in the ledger.

## Files and versions

- Authoritative reviewed record: `outputs/Authority Swap - Part 2b Source and Key Ledger.csv`, **dataset v1.2 source-reviewed**, SHA-256 `B48550317011B1FF541CA525633ABCE2863097657C24B66B358396CFD34E3A7D`.
- Independent records: `work/authority-swap/questions/verified-c.jsonl`, `verified-e.jsonl`, `verified-s.jsonl` (46 records each). Evidence freeze: `work/authority-swap/questions/blind-derivations-manifest.json`, SHA-256 `734205DA9FE547AFB731F1D9CC9AB159762D477A01B98DB520E1FCC5D15F37C3`. Summary: `part2b-summary.json`; assembler: `assemble_2b.py` in that folder.
- Preserved earlier states: Part 2a Draft Questions CSV, Part 2b Working Questions CSV, Part 2b Audit Dispositions CSV. Their older “unverified” or “unresolved” notes are historical; the reviewed ledger and this checkpoint state the latest result. Do not regenerate the original bank from draft fragments and overwrite this review.
- Protocol **draft v3.3** incorporates the eight revisions and exclusions; not frozen. No experimental baseline, pilot, analysis or paper exists for Authority Swap.

## Usage, decisions and holds

**0 experimental model inference calls, 0 Adaption credits, 0 new financial charges.** No API key accessed. User-reported Adaption balance is 2,750, unverified. Part 3 alone covers hosted access/pricing/parameter checks and at most five smoke-test calls, with user-reported dashboard balances before/after. Hard project cap is 150 Adaption credits unless explicitly raised; include smoke, pilot, correction and main calls. Log tokens/credits and fix one reasoning setting per model. Local models run sequentially, CPU throughput first.

Pilot may consider the two local models and up to three hosted candidates; main uses at most three passing models, only after separate authorization. Eligibility requires correct baselines under both A/B orders. Preserve floor/ceiling, parse and completeness gates, pilot-estimated variance, per-question comparisons and cross-model item-population caveats. The proposed focal rule uses pilot eligibility and feasibility, never the observed expertise contrast or main results; its noise/selection limitations remain in Part 2a Design Notes.

Authority Swap is the separate second project from *Counting Evidence by Origin*. Provisional title: “Does Claimed Expertise Change False Switching? A Controlled Expertise x Tone Test in Small Local Models”. The user confirms the title before Part 7; hosted main models may require changed wording. Disclose shared llama.cpp and any later reused code, hosted-credit use, AI assistance and all external sources. The literature review remains in the Part 1 artifact.

**MAIN EXPERIMENT HELD. SUBMISSION HELD.** User-verified deadline: Monday November 16, 2026, 17:29 IST. Paper later needs the official template, 150–250-word abstract, authors/affiliations, at most eight pages excluding references/appendices, and “Limitations and Dual-Use / Ethical Considerations” appendix. No submission action is authorized now.

## Next three actions

1. Wait for **“Proceed to Part 2c.”** Do not begin the independent quality/overlap audit now.
2. At 2c start recommend Astra Extra High; audit underlying-fact overlap, wording, distractor plausibility, tier balance, the 18 excluded items and C024. Any replacement or substantive revision must get new source/key verification before acceptance.
3. Give the verification-time estimate and cut-down fallback, plus exactly 12 item IDs and precise sources for the user to check; save the 2c checkpoint, report in at most 200 words, and stop for **“Proceed to Part 3.”**
