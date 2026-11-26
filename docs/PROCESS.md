# Research process and decision history

This guide was written when preparing the public repository on 27 November 2026. It summarizes contemporaneous files; it is not a claim that the entire final design was fixed before the pilot. Earlier documents are preserved, including superseded decisions and failed checks.

## 0. Setup

Hardware, tools, folders, checkpoints, and resumability were established. Local models were run sequentially. See [Part 0 checkpoint](../outputs/Authority%20Swap%20-%20Part%200%20Checkpoint.md), `work/authority-swap/CHECKPOINT_TEMPLATE.md`, and the early workflow files.

## 1. Literature and contribution

The contribution was narrowed to a replication with a controlled expertise × tone extension. The research notes distinguish opened papers from unavailable or unverified material. See [literature and framing](../outputs/Authority%20Swap%20-%20Part%201%20Literature%20and%20Framing.md) and `work/authority-swap/literature/`. Early notes are not substitutes for the final report's reference list.

## 2a–2c. Build, verify, revise, and audit the question bank

Drafting covered graded difficulty and multiple low-stakes factual domains. Fresh blind reviewers derived keys from cited primary sources before comparing draft keys. Audits addressed self-answering arithmetic, logical tautologies, repeated facts, weak distractors, option cues, answer-position balance, and source-page concentration. Replacements underwent additional review.

The final version is dataset **v1.3**, with 85 main items and disjoint development, acceptance, and correction banks. Difficulty labels remain provisional. The final files are in `outputs/Authority Swap - Dataset v1.3*`; the fact-disjointness, source-concentration, second-reviewer queue, and human-check sample files sit alongside them. Detailed preparation code, key-free reviewer inputs, draft keys, and review evidence are in `work/authority-swap/questions/`.

The 12-item human check was ultimately waived. Its sampling list is retained as a planned check, **not evidence that it was performed**. The later Claude CSV records background-knowledge agreement, not source opening or human review.

## 3a. Local models and runner

Qwen2.5-1.5B-Instruct and SmolLM2-1.7B-Instruct Q4_K_M weights were downloaded and hashed. CPU throughput, dummy questions, grammar-constrained labels, parsing, and history replay were checked. The reusable runner stores unique request IDs and responses separately from derived scores.

See [Part 3a checkpoint](../outputs/Authority%20Swap%20-%20Part%203a%20Checkpoint.md), `work/authority-swap/part3a/`, and the archived dummy runs. llama.cpp build 12243, commit `8766c0273`, was used. The only overlap with *Counting Evidence by Origin* was that executable and the machine.

## 3b. Hosted access and accounting

Non-study smoke and calibration calls tested the hosted Responses API, model identifiers, response shapes, parsing, token usage, and sponsor-credit accounting. The response validator was corrected before study collection. Credit budgets were caps, not spending targets. The earlier planning estimates and unresolved reservations are retained rather than rewritten as actual charges.

See [Part 3b checkpoint](../outputs/Authority%20Swap%20-%20Part%203b%20Checkpoint.md), [usage and budget](../outputs/Authority%20Swap%20-%20Part%203b%20Usage%20and%20Budget.md), `hosted_runner.py`, and `data/hosted-accounting.csv`. The public export omits secrets, request headers, and private account configuration.

## 4a–4b. Freeze and pilot

Protocol v3.5 fixed templates, parsing, eligibility, scheduling, pacing, and gates. Amendment v3.6 added the bare counterclaim and descriptive-only handling for floor/ceiling failures, while correcting the provenance description. Dummy checks preceded study items; 8 development items and 16 acceptance items were run on five candidates.

See v3.5/v3.6 protocols, their SHA-256 files, frozen templates/assignments, and [pilot results](../outputs/Authority%20Swap%20-%20Part%204b%20Results.md). These are the records of pre-main decisions and observed pilot gates.

## 5. Post-pilot amendment and main collection

After observing a pilot floor, v3.7 explicitly made all five candidates descriptive-only, with no focal model. It increased hosted concurrency, retained the core structure, and added exploratory repeated rebuttals and correction of scripted wrong answers. Both correction orientations were collected. The final schedule and evidence excerpts were frozen before main outcomes.

The saved run contains 5,354 logical records. Rate-limited attempts and an unresolved reservation appear in the accounting ledger, so attempt counts differ from logical-response counts. Collection finished before the writing cutoff. Original main response and item bytes are preserved in the public archive.

## 6. Analysis

Analysis reconstructed prompt and history hashes against the frozen schedule. Outputs include branch counts and Clopper–Pearson intervals, question-paired expertise contrasts, bootstrap intervals and conservative sparse bounds, abstentions, unusable replies, escalation, correction, timing, and accounting. Strict parsing was retained after diagnostic inspection.

See [Parts 5 and 6 results](../outputs/Authority%20Swap%20-%20Parts%205%20and%206%20Results.md), `analyze_v37.py`, and the eight `v3.7` CSV tables. The public `scripts/reproduce.py` reruns aggregation offline without changing the submitted artifacts.

## 7–8. Report, checks, and submission

The report was assembled using the official template. The saved final validation records a 199-word abstract, 6 main-text pages, 10 total pages, 174 checked table cells, and a PDF hash matching the confirmed attachment. It records submission on 16 November 2026 at 05:43:57 IST. The publication package does not include private confirmation email contents or browser/account screenshots.

The submitted PDF is preserved unchanged. Its historical statement that no public repository accompanied submission reflects the state on 16 November. This repository was prepared later, on 27 November.

## Public release

The package uses an explicit file allowlist. Selected process notes replace personal machine paths, private document/submission links, and email addresses with markers; original and public hashes are recorded. Main study records, the frozen schedule, final data ledger, result tables, and submitted PDF remain unchanged. A fresh offline pass checks the record archive and regenerates all eight result tables. See [provenance](PROVENANCE.md).
