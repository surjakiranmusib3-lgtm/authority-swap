# Part 3b hosted preflight

15 November 2026 IST. Public documentation only. Account access, available models for the user's key, sponsor-credit coverage, actual billed credits, and observed token usage are pending. The pre-call dashboard balance is blank. The presence-only process check returned absent for `ADAPTION_API_KEY`. Retain the approved local setup and the Part 4 hold.

## API and billing checks

Use the [Adaption Responses API](https://docs.adaptionlabs.ai/api/resources/responses/methods/create) with the direct model ID, explicit replayed conversation history, tools disabled, no stored conversation, and an output token cap. Adaption documents temperature and `max_output_tokens`, and describes cached-input and reasoning-token usage fields in response metadata. The public request schema does not list seed, log probabilities or reasoning effort controls. Document each as unverified pending provider evidence. A successful response to a request with an extra field would not establish that field was honored.

Count total billable output once, including reasoning where covered by the provider's total. For a conservative worst case, use uncached rates and the documented maximum combined context to bound input and output, including reasoning where billable, if a tighter cap cannot be verified. Reserve the bound for each attempt, retain the reservation for any ambiguous failure, and stop if the next call cannot fit. An authenticated model-list read is separate from the maximum five text generation requests. Once the user supplies the starting balance, use the bounded smoke test to check sponsor coverage. Halt if the service shows a paid fallback or cannot give a conservative credit bound. Ask for the ending balance afterward and compare it with observed and estimated charges. If the dashboard precision is too coarse to show the delta, mark coverage unresolved unless an itemized record confirms it.

## Planning estimate, pending actual measurements

The [provider's model table](https://docs.adaptionlabs.ai/inference-stacks/models) quotes the following rates per million tokens. This example uses 1,000 input and 500 output tokens per request and 595 requests (85 questions × 7). Seven requests assume two baselines and five follow-ups on one prespecified scored orientation. Both follow-up orientations would require as many as 1,020 requests per model. All these cases assume every main question is eligible. Add retry reservations separately.

| Model | Input rate | Output rate | Requests | Assumed input / output tokens per call | Credits |
|---|---:|---:|---:|---:|---:|
| gemma-4-31b-it | 0.09 | 0.34 | 595 | 1,000 / 500 | 0.155 |
| qwen3.8-27b | 0.039 | 1.25 | 595 | 1,000 / 500 | 0.395 |
| qwen3.5-397b | 0.55 | 3.50 | 595 | 1,000 / 500 | 1.369 |
| Three-model core total | | | 1,785 | | 1.918 |
| qwen3.5-397b reasoning extension, separate full pass | 0.55 | 3.50 | 595 | 1,000 / 5,000 | 10.740 |
| glm-5.2 illustrative additional full pass | 1.40 | 4.40 | 595 | 1,000 / 500 | 2.142 |

The five-draw robustness extension needs an explicit sampling unit before budgeting. Five extra full passes on the three core models at the same token lengths would cost an estimated 9.591 credits, excluding retries. Correction and attribution counts depend on the approved treatment designs. Replace estimates in the Part 3b report with measured usage by model and proposed arm, distinguishing smoke prompt lengths from assumed eventual study lengths. A smoke test cannot measure study-arm token lengths because those items remain held.

After coverage is confirmed, the user-authorized cap is 600 credits, with Part 3b at most 5, Part 4 at most 60, Part 5 at most 400, and 135 reserved. Treat reserve allocation and any main extension as pending later part authorization. Stage estimates are limits for scientific work, not spending targets. The three intended hosted core models still need the approved acceptance gates and feasibility checks. The primary contrast remains paired expert minus ordinary false-switching, averaged across tones. Freeze the exact reasoning comparison, sampling robustness, additional model comparisons, correction and attribution definitions and multiplicity handling before main data. Keep exploratory extensions in the appendix.

If sponsor coverage or bounded cost cannot be verified, the local-only route remains available once the local readiness checks pass and the user authorizes the pilot. The current provisional title already describes small local models. If hosted models enter the main study, ask the user to confirm a scope-accurate title before Part 7.
