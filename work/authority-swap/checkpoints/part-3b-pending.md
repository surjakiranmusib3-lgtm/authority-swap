# Authority Swap Part 3b checkpoint

15 November 2026 IST. **Stopped after the first hosted smoke attempt because billing could not be verified.** Part 3a is complete. Part 4, the main experiment and submission remain held. No browser actions were repeated.

The authenticated read-only [hosted model catalog](https://docs.adaptionlabs.ai/api/resources/models/methods/list) returned all three exact IDs: `gemma-4-31b-it`, `qwen3.8-27b` and `qwen3.5-397b`. The pre-test displayed balance was **2,750 credits** in the prior browser check. A post-attempt dashboard balance was not measured in this continuation.

| Task | Model | Time (IST) | Response ID | Input / output / reasoning tokens | Credits |
|---|---|---|---|---|---|
| 3b-1 | gemma-4-31b-it | 15 Nov, 05:18:44 | Unavailable | Unavailable / unavailable / unavailable | **0.087040 reserved**; debit unknown |

The non-study request used `temperature=0` and `max_output_tokens=16`. The runner rejected the returned data during validation before it recorded response metadata. The specific validation failure and any actual debit are unknown. No second attempt was made. Whether a paid fallback occurred could not be determined. The per-call ledger keeps this reservation and prevents further dispatches while it is unresolved. A balance rounded to whole credits cannot resolve a small debit. Ask for an itemized inference event at the recorded time that identifies the model, usage and funding source.

The [Responses request schema](https://docs.adaptionlabs.ai/api/resources/responses/methods/create) documents temperature and max output tokens. Their operational behavior was not established by this attempt. No seed, log probabilities or reasoning toggle appears in that schema; do not assume any of those controls work. Exclude the hosted A/B probability analysis and reasoning on/off extension unless a supported control is verified.

| Model | Published input / output credits per million | Pilot (168 calls) | Main (595 calls) |
|---|---:|---:|---:|
| gemma-4-31b-it | 0.09 / 0.34 | 0.043680 | 0.154700 |
| qwen3.8-27b | 0.039 / 1.25 | 0.111552 | 0.395080 |
| qwen3.5-397b | 0.55 / 3.50 | 0.386400 | 1.368500 |
| Total estimated credits | | **0.541632** | **1.918280** |

Planning estimates only. Uses 1,000 uncached input and 500 output tokens per call, all 24 pilot and 85 main items eligible, two baselines plus five branches on one scored order, no retries. The main estimate is about 0.070% of 2,750 credits. There is no measured-token budget until usage is reconciled. Source: [Adaption pricing and context limits](https://docs.adaptionlabs.ai/inference-stacks/models). Stage limits remain smoke 5 (at most five attempts), pilot 60, main 400, reserve 135. The full-context reservation for all five planned smoke calls was 1.288192 credits; this is not a charge or a pilot budget approval.

The runner now loads the credential at call time from the private `secrets` folder. That folder is ignored and excluded from outputs and packaging. No secret, headers or raw response were written to the ledger. The output-free call summary is in `work/authority-swap/runs/adaption/summary.json`. The runner now records allowlisted response ID and token counters before validating them, and captures a safe failure code when reconciliation fails. An offline fixture verified this repair. It cannot recover the earlier missing metadata. Runner SHA-256 `8f97bb4497bb0d725c9feb2560d321007401f232ad5621d7f20082c2c49804b0`.

1. Await the user's itemized usage or account billing evidence. Keep the first attempt reserved until reconciled and make no further hosted attempts meanwhile.
2. If sponsor coverage is confirmed, reconcile the ledger before any separately continued smoke work and record the measured budget. Otherwise recommend the local-only plan and retain the existing title ending “Small Local Models.”
3. Keep dataset v1.3 and draft protocol v3.4 with the approved 45% / 30-item eligibility amendment. Await the twelve human checks and explicit “Proceed to Part 4” before any pilot.
