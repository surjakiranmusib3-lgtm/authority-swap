# Authority Swap v3.7 main results

Five descriptive-only candidates with no focal model. The study extended v3.6 after observing a pilot floor. Times and credits are in the run and accounting tables. The collection cutoff was Monday 11:29 IST. Source checks used AI. The reported Claude blind pass checked key agreement from background knowledge. No human spot-check was performed.

Completed models out of five were core 5, escalation 5 and correction 5. The tables retain any missing replies.

## Confirmatory-structure core

Each cell is keyed wrong / usable, followed by the exact 95% Clopper–Pearson interval. Usable includes ABSTAIN. Eligibility requires a correct response in both baseline orders. Branch estimates condition on each model's eligible questions. Intervals describe binomial precision for the observed design, with a curated bank.

| Model | Eligible / 85 | Neutral | Expert assertive | Expert tentative | Ordinary assertive | Ordinary tentative | Bare |
| --- | ---: | --- | --- | --- | --- | --- | --- |
| gemma-4-31b-it | 80/85 | 1/80 [0.0, 6.8] pp | 1/78 [0.0, 6.9] pp | 0/80 [0.0, 4.5] pp | 0/79 [0.0, 4.6] pp | 0/79 [0.0, 4.6] pp | 0/80 [0.0, 4.5] pp |
| qwen2.5-1.5b-instruct | 26/85 | 0/26 [0.0, 13.2] pp | 0/26 [0.0, 13.2] pp | 0/26 [0.0, 13.2] pp | 0/26 [0.0, 13.2] pp | 0/26 [0.0, 13.2] pp | 0/26 [0.0, 13.2] pp |
| qwen3.5-397b | 79/85 | 0/79 [0.0, 4.6] pp | 2/79 [0.3, 8.8] pp | 2/79 [0.3, 8.8] pp | 3/79 [0.8, 10.7] pp | 2/79 [0.3, 8.8] pp | 3/79 [0.8, 10.7] pp |
| qwen3.8-27b | 77/85 | 1/77 [0.0, 7.0] pp | 0/77 [0.0, 4.7] pp | 0/77 [0.0, 4.7] pp | 0/77 [0.0, 4.7] pp | 0/77 [0.0, 4.7] pp | 1/77 [0.0, 7.0] pp |
| smollm2-1.7b-instruct | 26/85 | 11/26 [23.4, 63.1] pp | 12/26 [26.6, 66.6] pp | 13/26 [29.9, 70.1] pp | 12/26 [26.6, 66.6] pp | 12/26 [26.6, 66.6] pp | 16/26 [40.6, 79.8] pp |

### Paired expertise difference

Expert minus ordinary averaged over tone, paired by question. Complete cases require the original five branches. A bootstrap interval of [0, 0] reflects a degenerate empirical distribution. The overlap in eligible question populations varies by model.

| Model | Complete / eligible | Nonzero | Difference | Bootstrap 95% | Sparse 95% bound |
| --- | ---: | ---: | ---: | ---: | ---: |
| gemma-4-31b-it | 78/80 | 1 | +0.6 pp | [0.0, 1.9] pp | [-6.9, 6.9] pp |
| qwen2.5-1.5b-instruct | 26/26 | 0 | +0.0 pp | [0.0, 0.0] pp | [-13.2, 13.2] pp |
| qwen3.5-397b | 79/79 | 1 | -0.6 pp | [-1.9, 0.0] pp | [-6.9, 6.9] pp |
| qwen3.8-27b | 77/77 | 0 | +0.0 pp | [0.0, 0.0] pp | [-4.7, 4.7] pp |
| smollm2-1.7b-instruct | 26/26 | 1 | +1.9 pp | [0.0, 5.8] pp | [-19.6, 19.6] pp |

### Abstentions and unusable replies

| Model | Baseline abstentions | Baseline unusable | Follow-up abstentions | Follow-up unusable | Follow-up missing |
| --- | ---: | ---: | ---: | ---: | ---: |
| gemma-4-31b-it | 0 | 4 | 0 | 4 | 0 |
| qwen2.5-1.5b-instruct | 84 | 0 | 156 | 0 | 0 |
| qwen3.5-397b | 0 | 0 | 0 | 0 | 0 |
| qwen3.8-27b | 1 | 0 | 3 | 0 | 0 |
| smollm2-1.7b-instruct | 8 | 0 | 12 | 0 | 0 |

Gemma core unusable reply categories were truncated output cap (8). Each truncated reply used 64 output tokens. Diagnostics track message shape and output-token ranges. Grading stayed strict.

## Exploratory escalation

Each cell gives wrong / usable at this turn followed by ever switched / known through this turn. Pooled factor rows contain two replies per item per turn when both branches are available. A known cumulative negative requires a usable label at every preceding turn. Turn 1 reuses core observations.

| Model | Group | Turn 1 | Turn 2 | Turn 3 |
| --- | --- | --- | --- | --- |
| gemma-4-31b-it | expert | 1/158 · 1/158 | 1/158 · 1/158 | 1/158 · 1/158 |
| gemma-4-31b-it | ordinary | 0/158 · 0/158 | 0/158 · 0/158 | 0/158 · 0/158 |
| gemma-4-31b-it | assertive | 1/157 · 1/157 | 1/157 · 1/157 | 1/157 · 1/157 |
| gemma-4-31b-it | tentative | 0/159 · 0/159 | 0/159 · 0/159 | 0/159 · 0/159 |
| qwen2.5-1.5b-instruct | expert | 0/52 · 0/52 | 0/52 · 0/52 | 2/52 · 2/52 |
| qwen2.5-1.5b-instruct | ordinary | 0/52 · 0/52 | 2/52 · 2/52 | 6/52 · 6/52 |
| qwen2.5-1.5b-instruct | assertive | 0/52 · 0/52 | 2/52 · 2/52 | 7/52 · 7/52 |
| qwen2.5-1.5b-instruct | tentative | 0/52 · 0/52 | 0/52 · 0/52 | 1/52 · 1/52 |
| qwen3.5-397b | expert | 4/158 · 4/158 | 4/158 · 4/158 | 4/158 · 4/158 |
| qwen3.5-397b | ordinary | 5/158 · 5/158 | 5/158 · 5/158 | 5/158 · 5/158 |
| qwen3.5-397b | assertive | 5/158 · 5/158 | 5/158 · 5/158 | 5/158 · 5/158 |
| qwen3.5-397b | tentative | 4/158 · 4/158 | 4/158 · 4/158 | 4/158 · 4/158 |
| qwen3.8-27b | expert | 0/154 · 0/154 | 0/154 · 0/154 | 0/154 · 0/154 |
| qwen3.8-27b | ordinary | 0/154 · 0/154 | 0/154 · 0/154 | 0/154 · 0/154 |
| qwen3.8-27b | assertive | 0/154 · 0/154 | 0/154 · 0/154 | 0/154 · 0/154 |
| qwen3.8-27b | tentative | 0/154 · 0/154 | 0/154 · 0/154 | 0/154 · 0/154 |
| smollm2-1.7b-instruct | expert | 25/52 · 25/52 | 25/52 · 25/52 | 25/52 · 25/52 |
| smollm2-1.7b-instruct | ordinary | 24/52 · 24/52 | 24/52 · 24/52 | 24/52 · 24/52 |
| smollm2-1.7b-instruct | assertive | 24/52 · 24/52 | 24/52 · 24/52 | 24/52 · 24/52 |
| smollm2-1.7b-instruct | tentative | 25/52 · 25/52 | 25/52 · 25/52 | 25/52 · 25/52 |

## Exploratory correction

Uptake is keyed correct / usable after a scripted wrong label. Each of the 24 items contributes both orientations to each condition. The two orientations are repeated observations of one question. Evidence excerpts differ in format.

| Model | Bare | Evidence | Evidence minus bare |
| --- | --- | --- | ---: |
| gemma-4-31b-it | 44/47 | 48/48 | +6.4 pp |
| qwen2.5-1.5b-instruct | 0/48 | 3/48 | +6.2 pp |
| qwen3.5-397b | 46/48 | 48/48 | +4.2 pp |
| qwen3.8-27b | 44/48 | 48/48 | +8.3 pp |
| smollm2-1.7b-instruct | 31/48 | 23/48 | -16.7 pp |

## Claim ledger

| Claim supported by these data | Evidence | Scope |
| --- | --- | --- |
| How often models chose the keyed wrong label after each prompt | Core branches and exact intervals | Model-specific eligible questions. |
| How claimed expertise changed wrong-label choices in this setup | Paired contrasts and sparse bounds | Original five usable branches on the same question. |
| Switching during repeated rebuttals | Escalation counts and factor differences | Exploratory continuation from the model's own reply. Denominators reflect missing history. |
| Uptake of a correction with and without an excerpt | Correction counts | Exploratory comparison after a scripted wrong answer, with both orientations per item. |

## Run and provenance

Hosted ledger cost for this stage was 0.173298167 credits. Unresolved reservations held 0.08704 credits. The conservative whole-project accounting exposure at close was 3.280434 credits. Accounting separates the provider’s cost fields from estimate-only entries, when present.

The runner last wrote a response record at 2026-11-15T21:25:40+05:30. It committed 5354 logical requests across all arms. The independent aggregate pass reconstructed every saved request's prompt and history hashes against the frozen schedule. Unavailable replies remain missing.

Queue state reports escalation `complete` and correction `complete`.

- [Authority Swap - v3.7 Core Branches](Authority%20Swap%20-%20v3.7%20Core%20Branches.csv)
- [Authority Swap - v3.7 Paired Contrasts](Authority%20Swap%20-%20v3.7%20Paired%20Contrasts.csv)
- [Authority Swap - v3.7 Escalation](Authority%20Swap%20-%20v3.7%20Escalation.csv)
- [Authority Swap - v3.7 Escalation Contrasts](Authority%20Swap%20-%20v3.7%20Escalation%20Contrasts.csv)
- [Authority Swap - v3.7 Correction](Authority%20Swap%20-%20v3.7%20Correction.csv)
- [Authority Swap - v3.7 Unusable Diagnostics](Authority%20Swap%20-%20v3.7%20Unusable%20Diagnostics.csv)
- [Authority Swap - v3.7 Run Timing](Authority%20Swap%20-%20v3.7%20Run%20Timing.csv)
- [Authority Swap - v3.7 Hosted Accounting](Authority%20Swap%20-%20v3.7%20Hosted%20Accounting.csv)
- [Authority Swap - v3.7 Data Hashes](Authority%20Swap%20-%20v3.7%20Data%20Hashes.txt)
