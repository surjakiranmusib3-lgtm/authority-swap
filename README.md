# Authority Swap

**Claimed Expertise and False Switching in Five Language Models**  
Surja Kiran Musib · Apart Research AI × Epistemics Research Sprint, November 2026

This repository contains the submitted report, question bank, source-verification records, protocol history, experiment code, saved model responses, accounting records, and offline analysis for a controlled **claimed expertise × tone** study.

**Status:** submitted on 16 November 2026; public reproducibility package prepared on 27 November 2026. All findings are descriptive. The escalation and correction arms were added after the pilot and are exploratory. No focal model was selected.

## Start here

- [Submitted report (PDF)](outputs/Authority%20Swap%20-%20Final%20Report.pdf) — 6 main-text pages, 10 pages including references and appendices.
- [Results and claim ledger](outputs/Authority%20Swap%20-%20Parts%205%20and%206%20Results.md).
- [Process timeline](docs/PROCESS.md) — what changed, why it changed, and which records document each stage.
- [Offline reproduction](docs/REPRODUCIBILITY.md) — verify records and regenerate all eight analysis tables without calling any model.
- [Final protocol amendment v3.7](outputs/Authority%20Swap%20-%20Protocol%20v3.7.md), building on [v3.6](outputs/Authority%20Swap%20-%20Protocol%20v3.6.md) and its frozen templates.
- [Key-free question bank](outputs/Authority%20Swap%20-%20Dataset%20v1.3%20Key-free.csv) and [source-and-key ledger](outputs/Authority%20Swap%20-%20Dataset%20v1.3%20Source%20and%20Key%20Ledger.csv).
- [Provenance, publication exclusions, and limitations](docs/PROVENANCE.md).

## What was tested?

Models first answered factual A/B questions in both answer orders. Only questions answered correctly in both orders were eligible for follow-ups. Four branches crossed claimed expertise (expert/ordinary) with tone (assertive/tentative), holding the false counterclaim fixed. Neutral reconsideration and a shorter bare counterclaim provided controls. Three wording sets were balanced across questions.

The final bank has **133 questions**: 85 main, 8 development, 16 pilot acceptance, and 24 correction. The run contains **5,354 logical response records**: 2,578 core, 2,296 additional escalation turns, and 480 correction responses. Hosted model names are the exact provider identifiers recorded at collection, not independently verified weight identities.

| Model | Eligible main questions | Paired expertise difference | Conservative sparse 95% bound |
|---|---:|---:|---:|
| gemma-4-31b-it | 80/85 | +0.6 percentage points | ±6.9 pp |
| qwen3.5-397b | 79/85 | −0.6 pp | ±6.9 pp |
| qwen3.8-27b | 77/85 | 0.0 pp | ±4.7 pp |
| Qwen2.5-1.5B-Instruct, Q4_K_M | 26/85 | 0.0 pp | ±13.2 pp |
| SmolLM2-1.7B-Instruct, Q4_K_M | 26/85 | +1.9 pp | ±19.6 pp |

The paired comparison averages expert minus ordinary false switching over both tones. Gemma has 78 complete paired cases; other paired counts equal their eligible counts. See the CSVs for exact denominators and intervals.

The study **does not establish a general absence of authority effects**. Hosted switches were sparse. Local Qwen abstained on all 156 first-turn follow-ups; SmolLM2 switched frequently even under neutral reconsideration. These behaviors limit a simple interpretation of wrong-answer switching as deference to authority. In the exploratory correction arm, all three hosted models accepted the correct answer in 48/48 evidence-present responses, after a **scripted** wrong answer; this is not a test of correcting their naturally occurring errors.

## Reproduce the analysis

With Python 3.11 or newer, from the repository root:

```sh
python scripts/reproduce.py
```

This uses the standard library only, makes **zero network or inference calls**, spends no credits, and writes into `_reproduction/`. It verifies the archive, reconstructs prompt/history hashes for all main records, and compares regenerated tables with the saved results. No API key, model download, GPU, or llama.cpp installation is needed for this check.

## Repository map

| Location | Contents |
|---|---|
| `outputs/` | Submitted PDF; final data, results, protocols, and historical checkpoint reports |
| `work/authority-swap/` | Original study scripts, literature notes, question-building and verification records |
| `data/research-records.tar.gz` | Normalized main/pilot records and dummy-run records, with original relative paths |
| `data/hosted-accounting.csv` | Allowlisted per-attempt accounting, token usage, response IDs, and credit fields |
| `data/archive-manifest.json` | SHA-256 and original SHA-256 for every archived member |
| `data/publication-provenance.json` | Copied-file hashes, disclosed redactions, and exclusions |
| `docs/` | Process, reproduction, and provenance guides |
| `scripts/reproduce.py` | Offline verification entry point |
| `SHA256SUMS` | Public-package checksums |

Older plans, tentative claims, excluded questions, and superseded budgets are retained as **historical records**, not as the final method. Read the final report, v3.7 schedule, and final results first. References in early notes may have been unverified or later removed; their inclusion here does not promote them to verified citations.

## Verification and disclosure

Answer keys were verified by LLM-based source-review agents plus a background-knowledge pass. A Claude (Anthropic) blind pass answered all 133 items from background knowledge, without opening the sources, before seeing the keys, with 133/133 agreement. **This is not a source check. No human spot-check was performed.** Cross-model agreement does not establish that source interpretations are correct or rule out correlated errors.

AI tools were used for coding, source verification, analysis and drafting. The author takes responsibility for the content.

Hosted inference used Adaption sponsor credits. The earlier project, *Counting Evidence by Origin*, shares only the llama.cpp executable and machine. Its data and report are not part of this repository. Provider usage fields, estimates, and unresolved reservations are kept separate; a reservation is not a confirmed charge.

## Rights and citation

No repository-wide reuse license has been selected. Public visibility alone does not grant a software or data license. Third-party source excerpts, cited publications, models, and llama.cpp retain their respective rights and licenses. Model weights and executable binaries are not redistributed here. Use `CITATION.cff` or cite the report title, author, and 2026 sprint.
