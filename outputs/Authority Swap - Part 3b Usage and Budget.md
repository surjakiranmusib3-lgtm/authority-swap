# Authority Swap Part 3b usage and budget

15 November 2026 IST. All calls below used synthetic or generic prompts. No study questions, pilot, main experiment, or browser actions were run in this continuation.

**Adaption reported 2.999828 in usage cost** across 22 accounted responses. The long-context meter portion totaled 2.998792. The price calculation matched the provider cost on 22/22 accounted responses within a billionth of a credit. The earlier unresolved attempt retains 0.087040 credits as an additional upper reservation. Account credit coverage awaits the user's dashboard comparison. The prior balance was 2,750.

## Gemma diagnostic and fix

The saved non-study response was a completed object with one `message` item. Its opaque response ID was a 545-character padded string containing `=`. The old validator reused the local task-ID pattern, which capped length at 96 and excluded `=`, causing `response_id_unverified`. The new response-ID validator accepts the returned opaque format and screens literal and decoded candidates for credentials. The saved response was reconciled locally without another request.

Top-level keys: `id`, `created_at`, `error`, `incomplete_details`, `instructions`, `metadata`, `model`, `object`, `output`, `parallel_tool_calls`, `temperature`, `tool_choice`, `tools`, `top_p`, `max_output_tokens`, `previous_response_id`, `reasoning`, `status`, `text`, `truncation`, `usage`, `user`, `store`, `background`, `max_tool_calls`, `prompt`, `service_tier`, `top_logprobs`, `presence_penalty`, `frequency_penalty`, `kv_transfer_params`, `ec_transfer_params`, `input_messages`, `output_messages`, `output_text`. Usage contained integer input, output and total token counts, input details including cached tokens, output details including reasoning tokens, and a numeric `cost` field.

## Per-call usage

The response-ID fingerprints below match the complete provider IDs in the [private per-call summary](<C:/Users/REDACTED/Documents/Codex/2026-11-13/referenced-chatgpt-conversation-this-is-an/work/authority-swap/runs/adaption/summary.json>). The raw bodies are local in the ignored run folder. The report does not include response text or request headers. A rate-limited attempt returned no response ID or usage and is listed separately.

| Task | Model | Status | Response ID SHA-256 prefix | Input | Cached | Output | Reasoning | API cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3b-1 | gemma-4-31b-it | reserved | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable |
| 3b-gemma-64 | gemma-4-31b-it | completed | 3fd5430bdd81 | 20 | 0 | 2 | 0 | 0.000002480 |
| 3b-qwen27 | qwen3.8-27b | incomplete | 9362e328281e | 59 | 0 | 16 | 16 | 0.000022301 |
| 3b-qwen397 | qwen3.5-397b | incomplete | de997e0f508f | 17 | 0 | 16 | 16 | 0.000065350 |
| cal-shape-gemma-base | gemma-4-31b-it | completed | f2bdb3baaacd | 72 | 0 | 2 | 0 | 0.000007160 |
| cal-shape-gemma-branch | gemma-4-31b-it | completed | ea94e4ceeb5f | 121 | 0 | 2 | 0 | 0.000011570 |
| cal-shape-q27-base | qwen3.8-27b | incomplete | fba0b845ba0b | 107 | 0 | 64 | 64 | 0.000084173 |
| cal-shape-q27-branch | qwen3.8-27b | incomplete | 7b8836b27d92 | 161 | 0 | 64 | 64 | 0.000086279 |
| cal-shape-q397-base | qwen3.5-397b | incomplete | 45a272b1b408 | 69 | 0 | 64 | 64 | 0.000261950 |
| cal-shape-q397-branch | qwen3.5-397b | incomplete | 4edb4704ae45 | 119 | 0 | 64 | 64 | 0.000289450 |
| cal-qwen-controls | qwen3.5-397b | completed | 20c7facef8f4 | 121 | 0 | 2 | 0 | 0.000073550 |
| cal-meter-1 | glm-5.2 | incomplete | 239d65735d65 | 280736 | 0 | 64 | 64 | 0.393312000 |
| cal-shape-off-q27-base | qwen3.8-27b | completed | 10cb24483fe4 | 71 | 0 | 2 | 0 | 0.000005269 |
| cal-shape-off-q27-branch | qwen3.8-27b | completed | ae16bfc81d88 | 125 | 0 | 2 | 0 | 0.000007375 |
| cal-shape-off-q397-base | qwen3.5-397b | completed | 472b046c0e37 | 71 | 0 | 2 | 0 | 0.000046050 |
| cal-shape-off-q397-branch | qwen3.5-397b | completed | 07bca9dac960 | 121 | 0 | 2 | 0 | 0.000073550 |
| cal-meter-2 | glm-5.2 | rate_limited | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable |
| cal-meter-3 | glm-5.2 | incomplete | 84f8eecaa84c | 280865 | 0 | 64 | 64 | 0.393492600 |
| cal-meter-4 | glm-5.2 | incomplete | 3347a3a4910f | 280968 | 0 | 64 | 64 | 0.393636800 |
| cal-meter-5 | glm-5.2 | incomplete | ec879b931ffe | 281044 | 0 | 64 | 64 | 0.393743200 |
| cal-meter-6 | glm-5.2 | incomplete | ead6c751fc14 | 280676 | 0 | 64 | 64 | 0.393228000 |
| cal-meter-7 | glm-5.2 | incomplete | 671234d3e6af | 280932 | 0 | 64 | 64 | 0.393586400 |
| cal-meter-8 | glm-5.2 | incomplete | fe6dbaf13c04 | 281077 | 0 | 64 | 64 | 0.393789400 |
| cal-meter-9 | glm-5.2 | incomplete | bccd6212bc37 | 174087 | 0 | 64 | 64 | 0.244003400 |

## Controls observed

- Temperature 0 and 0.7 were accepted and echoed. This does not establish sampling distribution or deterministic replay.
- Qwen defaults used all 16 or 64 output tokens for reasoning and returned `incomplete` with `max_output_tokens`. The capability probe requested a cap of 1, which appeared as 16 in its response. Use a documented and calibrated output cap.
- Both Qwen variants completed the matched baseline and follow-up with `reasoning.effort=none`, echoing that setting and returning zero reasoning tokens and a valid label each time. The same prompts at the default did not finish at 64. Gemma completed both prompts with zero reasoning tokens under its default.
- The combined Qwen capability probe returned no seed and no populated top or message log probabilities. Those controls remain unverified for hosted study scoring. Do not use hosted A/B log probabilities or claim seed determinism.

## Cost from measured study-shaped prompts

| Model | Baseline input / output | Branch input / output | Pilot credits, 24 items | Main credits, 85 items |
| --- | --- | --- | --- | --- |
| gemma-4-31b-it | 72 / 2 | 121 / 2 | 0.001732080 | 0.006134450 |
| qwen3.8-27b | 71 / 2 | 125 / 2 | 0.001137912 | 0.004030105 |
| qwen3.5-397b | 71 / 2 | 121 / 2 | 0.011036400 | 0.039087250 |
| Three hosted models |  |  | 0.013906392 | 0.049251805 |

Each item assumes two baseline calls and five follow-ups at one prespecified order, with all items eligible and no retries. The table uses one synthetic baseline and one synthetic follow-up per model as measurements, and published token rates. It is a planning estimate, not a bound for the real questions. The metering calls used deliberately long synthetic GLM prompts to create an account-visible debit and are excluded from the study forecast. Local calls cost no Adaption credits. [Pricing](https://docs.adaptionlabs.ai/inference-stacks/models).

Keep the 600-credit project cap and the 6 / 60 / 400 / 134 smoke, pilot, main, and reserve allocations. Independently bound every batch with context and published rates, include unresolved reservations at full bound, and reconcile each returned usage record. The 3b requests ran one at a time.

Propose all three hosted candidates plus two local candidates for the pilot. Account reconciliation records sponsor coverage separately. Use the approved 45% both-order and 30 projected eligibility gates plus the other prespecified gates. For the main, consider only passers and keep the earlier three-model maximum unless the user confirms five-model coverage in the Part 4 plan. Choose the focal model without using observed treatment effect. The primary remains the paired expertise contrast averaged across tones. Send identical saved histories to hosted branches and check exact labels with the same parser. Local grammar constrains labels, whereas the hosted output format is only prompted. Keep that distinction in cross-model comparisons. A predeclared temperature-above-zero check can resample five times on a balanced focal-model subset and average draws within question. The separate genuine-correction arm has 24 preselected candidates. Keep both secondary to the core. Additional models require a scientific rationale and separate main-plan approval. A provisional title if hosted models enter the main is “Does Claimed Expertise Change False Switching? An Expertise × Tone Test Across Local and Hosted Language Models.”
