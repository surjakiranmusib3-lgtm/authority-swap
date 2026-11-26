# Authority Swap — Part 2c in progress

Part 2c ONLY is authorized; Part 3, all experiment runs, and submission are held. User additionally authorized the C038 event replacement and C037 torch-section diversification. Do not stop at this interim checkpoint if the current turn can continue.

## Completed work

- Opened Part 2b checkpoint and source-reviewed ledger. Previous ledger SHA-256: B48550317011B1FF541CA525633ABCE2863097657C24B66B358396CFD34E3A7D.
- Independent audit: `questions/p2c-fact-audit.json`, 138 original items, 228 semantic fact atoms. Its allowed C026/C038 example is superseded by the user's stricter event-level request; C038 is being re-topicked.
- Draft replacements: `questions/p2c-replacement-questions.csv` (15) and `questions/p2c-diversify-questions.csv` (12), each with separate draft-key files. Root has not opened those draft-key files.
- Wording amendments and C037/C038 replacements: `questions/p2c-wording-questions.csv` (13), prepared from key-free input. Follow-up packets `p2c-adjudication-questions.csv` (4) and `p2c-citation-questions.csv` (2) supersede E041/C013/E019 and additionally revise E010/E015/C016. Total unique changed records expected: 43.
- Permanent exclusions expected: C027, C028, S017, S025, S027. Target final source-verified counts: main 85 (30 easy / 29 medium / 26 hard), pilot_dev 8, pilot_accept 16, correction 24. These remain provisional until all reviews pass.
- NASA main keep set: S002,S004,S013,S022,S024. IUPAC main keep set: S008,S009,S018,S020,S029. All other original main items from those pages are re-topicked.
- Read prior-project `work/experiment.py`, `model-trials.csv`, `swapped-trials.csv`: prior prompts use fictional sensor/cabinet/gallery/drawer evidence, not external factual questions. No execution or inference occurred. Shared runner infrastructure must still be disclosed.

## Fresh blind reviews in progress

Fresh agents received only their designated key-free CSV and primary-source instructions, with no parent conversation and no access authorized to draft keys or old ledgers:

1. `p2c_verify_diversify` -> `questions/p2c-verified-diversify.jsonl`.
2. `p2c_verify_replacements` -> `questions/p2c-verified-replacements.jsonl`.
3. `p2c_verify_wording` -> `questions/p2c-verified-wording.jsonl` (finished: 11 PASS and 2 FLAG; E041 includes-subset ambiguity, C013 incomplete original citation and immaterial 1875/1876 discrepancy).
4. `p2c_verify_final_fixes` owns `questions/p2c-verified-adjudication.jsonl` (4) and `questions/p2c-verified-citation.jsonl` (2). The two original source-review agents were explicitly told not to write these extra files, avoiding collisions.

Final structural/fact audit is saved in `questions/p2c-final-fact-audit.json`: 133 rows / 196 propositions, no residual overlaps found after C016's supplied year is removed. This is not source verification. All final source checks remain separately required. Assembly/report scripts are prepared but have not yet been run: `assemble_2c.py`, `report_2c.py`. They read actual independent results, never draft-key files. Do not treat drafted/future report wording as a completed result until outputs exist and checks pass.

All use requested Astra Extra High. This is same-family AI review, not human or different-family validation. No row can be accepted merely because drafted; only explicit source-supported PASS records may enter v1.3.

## Usage and timing

0 Authority Swap experimental inference calls; 0 Adaption credits; no API key access; no paid calls. Chat-agent assistance consumes the user's chat allowance, which is not measured here. User-reported sponsor balance 2,750, unverified; project cap remains 150 for later authorized parts.

Initial clock reading: 2026-11-14 01:24:13 UTC. After an intervening user continuation/context pause, tool clock reported 12:37:38 UTC. The former 02:54 UTC wall-clock target is stale. Budget is about 90 minutes of active work, excluding the long interruption; exact active minutes cannot be independently reconstructed. Keep the remaining verification and packaging bounded; freeze verified count rather than pad a tier.

## Next three actions

1. Finish the three source reviews, hash their evidence before any draft-key comparison, resolve or exclude flags. No further part begins.
2. Assemble v1.3 key-free CSV and source/key ledger; balance positions by bank/tier, audit length/absolute cues, source cap, fact and event overlap, prior-project separation. Draw seeded 12-item human sample and list all 40 changed/disputed items separately. Report cut-down and power implications using unknown pilot variance honestly.
3. Save complete Part 2c checkpoint and RESUME.md; final report at most 200 words including links and concentration table. STOP for “Proceed to Part 3.”
