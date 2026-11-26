# Authority Swap Part 3a checkpoint

15 November 2026 IST. **Part 3a complete. Part 3b preflight prepared. Hosted tests are pending a key visible to Codex and the user's current pre-call dashboard balance. Part 4, main, and submission remain held.**

## Verified local artifacts

The publisher revisions, download sources, and publisher checksums are in `work/authority-swap/part3a/model-sources.json`. Both files were downloaded to `work/authority-swap/models`, independently SHA-256 hashed on disk, matched to the publisher checksums, and loaded one at a time.

| File | Bytes | Local SHA-256 |
|---|---:|---|
| qwen2.5-1.5b-instruct-q4_k_m.gguf | 1,117,320,736 | `6a1a2eb6d15622bf3c96857206351ba97e1af16c30d7a74ee38970e434e9407e` |
| smollm2-1.7b-instruct-q4_k_m.gguf | 1,055,609,536 | `decd2598bc2c8ed08c19adc3c8fdd461ee19ed5708679d1c54ef54a5a30d4f33` |

- Qwen publisher revision [dd26da440ef0330c47919d1ecae0966d24022222](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/commit/dd26da440ef0330c47919d1ecae0966d24022222).
- HuggingFaceTB publisher revision [6a7e79393ef2957e087f11fce1e50476799e313c](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct-GGUF/commit/6a7e79393ef2957e087f11fce1e50476799e313c).
- Reused the earlier project's existing upstream `work/llama/llama-server.exe` and its runtime DLLs in the same directory. Version 0.9.0-dev, build **12243**, commit **8766c0273**, Clang 20.1.8 Windows x86-64. Server executable SHA-256 `6f363d75fbac112e049662c4ff653d8beb9af5bdcaefec5695c1fe8e9af0319a`. Restricted execution could start the model but could not reach the loopback endpoint. The approved local check ran with loopback access. [Pinned llama.cpp server documentation](https://raw.githubusercontent.com/ggml-org/llama.cpp/8766c0273/tools/server/README.md).
- The new Python code uses the same upstream native llama.cpp HTTP API and generic ChatML delimiters as the prior project. No functions, prompts, stimuli, or data were copied or imported from the prior project's `work/experiment.py`. That file was inspected read-only (SHA-256 `c58699c6f30b7d048be2609a72b54fe8b32695737a02a9bd6f468651453aac9d`). The old 0.5B weights were not used.

## Runner and verification

`work/authority-swap/part3a/runner.py` (SHA-256 `31f5a9de7b88b08b503322a90bd9442676839a6d5ac509b33d9b9d26d4304adc`) is the local runner. It commits raw responses atomically under stable SHA-256 request IDs, maintains a run lock, verifies the loaded model hash and manifest identity, and rebuilds a separate score CSV. It stores the request body, exact rendered text, saved baseline link and history hash. The same baseline transcript is replayed across each of the five branches for that answer order. The Part 3a entry point uses only the three embedded fictional test items. Study scheduling, eligibility gating, and study prompts remain later-stage work. The dummy harness follows up under both orders to exercise replay even when a dummy baseline is wrong. This is 12 completions per question per model and does not set the final study's scored orientation rule.

Greedy temperature 0, seed 2026111402, output cap 8 tokens, grammar `root ::= "A" | "B" | "ABSTAIN"`. The two independently pinned plain ChatML renderings matched their GGUF server templates for baseline and follow-up examples. The tokenizer receives the rendered delimiters with explicit special-token parsing and no extra automatic BOS. Hardware was the Part 0 i7-11700F, with eight CPU threads, one slot, context 2048, and zero GPU layers.

| Model | Dummy calls | Identical replay groups | Median prompt tok/s | Median generation tok/s | Median HTTP completion |
|---|---:|---:|---:|---:|---:|
| Qwen2.5-1.5B | 36 | 6 | 398.1 | 30.7 | 0.392 s |
| SmolLM2-1.7B | 36 | 6 | 346.6 | 29.2 | 0.426 s |

Both runs saved 7 calls, resumed for 29, and then reused all 36 with zero new calls. Each run produced only the three allowed labels. Four additional decoder probes per model explicitly produced A, B and ABSTAIN and constrained an invalid label request. A/B are each one token (Qwen 32/33, Smol 49/50), and ABSTAIN occupies three and four tokens respectively, before end-of-generation tokens. Native completion returned both A/B first-token log probabilities on all 72 dummy requests with `n_probs=32` and pre-sampling probabilities. In deliberate label probes some candidates dropped out of the top 32. Any A/B conditional score can use `exp(lp_wrong) / (exp(lp_A) + exp(lp_B))` when both log probabilities are finite. Missing tokens stay missing. This is a first-token comparison conditional on A/B, not confidence in a complete response or probability across all three labels. Pilot coverage and interpretation are pending.

CPU throughput was adequate for these short checks, so GPU offload was unnecessary. Rerun/review command from workspace root:

```powershell
& 'work/authority-swap/.venv/Scripts/python.exe' 'work/authority-swap/part3a/check_local.py' both
```

Use existing run folders for resuming the dummy calls. The check wrapper also makes four decoder-probe calls per model each time it is invoked. Raw files and `scores.csv` are in `work/authority-swap/runs/part3a-qwen-dummy` and `part3a-smol-dummy`. Each has its own `local-check-summary.json`, server log, and template checks. Do not mix these runs with study data.

## Versions, usage, and gates

- Dataset v1.3, key-free SHA-256 `8d6e5377e1d92b31c6dcbe560b72120aa0f65c095b0bfade22717886d3c49232`. Main 85, development 8, acceptance 16, correction 24. Human review of the 12 sampled questions is pending. No study question was loaded, sent or scored.
- Protocol draft v3.4 from Part 2c with the user-approved Part 3a eligibility amendment in `work/authority-swap/part3a/pilot-gates-proposed.md`. At least **45%** of all acceptance items must be both-order eligible, which requires 8 of 16. At least **30** main items must be projected eligible using main-tier weights. The projection uses acceptance counts by tier and is noisy. It is a feasibility floor. The detailed floor/ceiling, parsing and completeness operational proposals remain for protocol freeze before Part 4 outcomes.
- Usage: **80 local completions** (72 dummy requests and eight decoder probes), **0 study inference calls**, **0 hosted calls**, **0 Adaption credits**. Both models were unloaded when the check finished. No GPU runs, payment or submission actions.
- Allowance and hosted support are unresolved. The console reported that `ADAPTION_API_KEY` was absent from its process. The user left their current pre-call balance as `[BALANCE]`. No key value was read into tool output. The [hosted preflight](<../work/authority-swap/part3a/hosted-preflight.md>) saves public prices, documented controls, conservative bounds, and planning estimates. Seed, logprobs and reasoning controls are not in the published request schema. A 600-credit project cap with stages 5/60/400 and reserve 135 becomes applicable after smoke confirmation, as instructed. The 3b smoke itself is limited to five calls and five credits. No research extension is authorized to run here.
- Authority Swap remains a separate project from *Counting Evidence by Origin*. Keep the working title for a local-only main run. Confirm a scope-accurate title before Part 7 if hosted models enter the main.
- Main experiment **held**. Submission **held**. Part 4 requires completion of the human checks and the user's explicit authorization. Sprint deadline recorded earlier is Monday 16 November, 17:29 IST.

## Next three actions

1. After the user sets `ADAPTION_API_KEY` in the environment Codex inherits and reports the starting dashboard balance, confirm presence without exposing the value and use the previously authorized Part 3b scope. Recommend Astra High for Part 3b. Do not repeat local downloads or completed dummy tests.
2. List models for the key, validate supported controls and pricing, and run the bounded non-study smoke test sequentially with at most five attempts. Log actual per-call token counts and any provider-reported credits separately from estimates. Compare with the user's ending dashboard balance. Stop if the next request cannot be bounded or coverage fails.
3. Save the Part 3b checkpoint and measured budget table, or mark what cannot be verified. Wait for “Proceed to Part 4” and the human checks.
