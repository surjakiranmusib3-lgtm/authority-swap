# Authority Swap | Part 1 checkpoint

Updated: 2026-11-14 01:10 IST. **Part 1 complete; stopped. Part 2 has not begun.** The user's required continuation phrase is **“Proceed to Part 2.”**

## What finished

- Opened and reviewed the four added works: [PARROT](https://arxiv.org/html/2511.17220v2), [SWAY](https://arxiv.org/html/2604.02423v1), [*Wavering Oracles*](https://arxiv.org/html/2609.11428), and the author-hosted [*Stubborn or Sycophantic?* manuscript](https://ahmedtaha.io/documents/Stubborn-or-Sycophantic.pdf). The OpenReview page for the last work could not be opened. Its author page calls it a NeurIPS 2026 TAE **workshop poster**; main-track acceptance is unverified.
- Rechecked five earlier full texts. The exact earlier Yang study is *Beyond the Sycophancy Score*; [arXiv records its submission on **30 September 2026**](https://arxiv.org/abs/2610.08840), despite the `2610` identifier. [SycoBench-600](https://aclanthology.org/2026.findings-acl.1759.pdf) evaluated **seven** models on a **555-item common intersection**. Authority had the highest wrong-flip point estimate for **five**, but one margin was just 0.1 percentage point; no significance claim follows.
- Framed Authority Swap as a **replication with a controlled claimed expertise × tone extension**, holding the proposed false answer and rationale fixed, with valid correction reported separately. Do not claim authority testing or tone testing itself is novel. PARROT's Qwen2.5-1.5B result creates a pilot ceiling concern; Yang's anchored-fact result creates a floor concern. Full findings and source locations are in the literature file below.
- Identified from [official Adaption documentation](https://docs.adaptionlabs.ai/tools/mcp/) that credits can pay for dataset adaptation, augmentation, translation, localization, generation and AutoScientist training, and [document extraction](https://docs.adaptionlabs.ai/api/resources/datasets/methods/launch_preprocessing) can reserve them. Adaption also offers a [hosted Responses API](https://docs.adaptionlabs.ai/inference-stacks/quickstart/). **Whether the user's sprint credits apply to hosted inference, its price, and the actual balance remain unverified.**

## Files and locations

- Literature/contribution record: `outputs/Authority Swap - Part 1 Literature and Framing.md`; identical work copy: `work/authority-swap/literature/review-v1.md` (SHA-256 `68452AAD5A12B8A895897A6C0A95B60D9CDA7D160ABD7E18B26CDA0A6355CB3E`).
- Part 0 hardware/tool checkpoint: `work/authority-swap/checkpoints/part-0.md`. Current project-wide resume file will match this checkpoint at `work/authority-swap/RESUME.md`.
- Older two-page plan: `outputs/Authority Swap - Research Workflow.pdf` and Markdown source. It predates the user's newest amendments and this literature audit; apply this checkpoint and the Part 1 literature file when resuming. Companion submission checklist: `outputs/Authority Swap - Pilot and Submission.md`.

## Versions and frozen decisions

- Protocol: **draft v3.1** = earlier two-page plan plus approved 14 November amendments and this Part 1 literature frame. It is **not frozen**. The central paired contrast is expert minus ordinary false-switch probability, averaged over assertive and tentative branches, on questions initially correct under **both A/B answer orders**. Neutral reconsideration is separate. False answer and factual rationale must remain fixed across the four branches; use about three balanced paraphrases per condition. A small genuine-correction arm is should-have, with its items chosen before outcomes; crossing speaker role there is optional.
- Scope: about **80–100** main candidates, **2** proposed local models (Qwen2.5-1.5B-Instruct focal; SmolLM2-1.7B-Instruct comparison), **8** pilot development and **16** fresh pilot acceptance items, and **20–30** distinct correction items if feasible. These counts are planning targets, not collected data. Run one model at a time. In Part 3 measure **CPU throughput first** and consider GPU offload only if needed. Exact artifacts, hashes, settings and constrained A/B/ABSTAIN decoding are pending.
- Pilot decisions to preserve: check eligibility, parseability, pair completeness, runtime, **floor** (near-zero reversals) and **ceiling** (>90% false switching in every branch) before main work. Estimate variance from the pilot, not an assumed 0.20; decide N/call count before main outcomes. Record P(keyed wrong option) as a secondary continuous outcome if the runner can provide valid constrained scores. Use paired question-level intervals and state the detectable effect limits.
- Dataset: **v0, not created**. No main, pilot or correction question bank, source record, or 12-item user audit sample exists. Part 2 must log primary-source evidence for every key and a verification time estimate with a cut-down fallback. Give the user exact IDs and source locations for 12 preselected items at the end of Part 2. Their review is needed before the main bank is frozen.
- Analysis/paper: not run or drafted. Later paper requires the official template, 150–250-word abstract, authors/affiliations, at most eight pages excluding references/appendices, and an appendix titled **“Limitations and Dual-Use / Ethical Considerations”**. It must state AI use and prior-work overlap, and distinguish new work and external sources. Verify all citations/results and form fields in Parts 7–8.

## Entry and prior-work state

- The user designates Authority Swap as a **separate second project**, distinct from *Counting Evidence by Origin*; do **not** use the same-title replacement route. Working title: **“Does Claimed Expertise Change False Switching? A Controlled Expertise x Tone Test in Small Local Models”**. Final title requires the user's confirmation **before Part 7**. The earlier project's submission receipt was not independently checked here.
- Earlier project local files date from 13 November 2026. The presently identified shared resource is the local `llama.cpp` executable/computer and general local-testing approach. Its synthetic cases, Qwen2.5-0.5B response logs, analysis and reported results are not Authority Swap data. If Part 3 copies/adapts its `work/experiment.py` or other code, record the exact reuse for disclosure; no code has yet been copied.

## Usage so far

- Authority Swap inference calls: **0** across all models. Adaption credits used by this project: **0**. New financial charges initiated: **0**. The **2,750-credit balance is user-reported**, not independently checked. No account, API key, or payment method was accessed in Part 1.
- Part 1 used source reading, local file inspection and checkpoint writing only; approximately 10 minutes of wall time. No question bank, model download, pilot, main run, paper, form entry, or submission occurred.

## Open issues and holds

- Novelty search is targeted rather than exhaustive. The proposed contribution and title are provisional. PARROT's Qwen result may cause saturation; the local Q4_K_M behavior is unknown. The effects of role and tone may be near zero. The OpenReview copy of *Stubborn or Sycophantic?* was inaccessible, though its author-hosted manuscript was read.
- Sponsor credit applicability to hosted inference and account-specific limits remain unverified. The approved route uses local models, so no sponsor balance is budgeted for model calls.
- User's 12-item review, per-item verification time, and fallback bank size await Part 2. Model access and CPU speed await Part 3. Main experiment and submission retain separate holds.
- Official deadline per user-verified sprint facts: **16 November 2026, 17:29 IST**. Maximum two projects per person. **Submission state: HELD. Main experiment state: HELD.** Do not submit, replace, or run Part 5 without explicit later instruction.

## Next three actions

1. Wait for the user's exact message **“Proceed to Part 2.”** Do no Part 2 work before it.
2. At Part 2 start, recommend a model and effort level, then construct separately labeled main, pilot and correction question banks with primary-source records and both-order eligibility plans.
3. Estimate the human verification workload, create a cut-down fallback, select 12 auditable items and exact source locations for the user, save the Part 2 checkpoint, report in at most 200 words, and stop.
