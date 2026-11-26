# Authority Swap | Revised study plan

**14 November 2026 · Apart Research sprint, Track 1 · Planning only**

## Literature checked in full text

**Earlier citation clarified.** Guang Yang, Homa Hosseinmardi, Fengchen Liu and Amir Ghasemian, September 2026, *Beyond the Sycophancy Score: How Task, Model, and Pressure Shape LLM Yielding*. Section 3.2 and Appendix C vary the lead, including claimed expertise, around a fixed rebuttal across three escalating turns. Fallacious and emotional leads did not increase yielding over plain repetition in aggregate. [arXiv 2610.08840](https://arxiv.org/html/2610.08840v1)

**Wang et al.** Added an incorrect user opinion to MMLU questions, with beginner, intermediate, and advanced self-described expertise across seven models. Models often adopted the wrong opinion. Expertise level changed agreement little in that setup. [arXiv 2508.02087](https://arxiv.org/html/2508.02087v4)

**Fanous et al., SycEval.** Tested simple, ethos, justification, and citation rebuttals in math and medical QA across three models. Simple rebuttals produced the most corrections overall, and citation rebuttals the most harmful reversals. The variants added persuasive content as well as framing. [arXiv 2502.08177](https://arxiv.org/html/2502.08177v4)

**Joswin et al.** Attributed the same incorrect MedQA hint to four medical roles, from first-year student to board-certified physician. On initially correct items, accuracy fell as the role became more senior across three models. They scored next-token choices in single prompts. [arXiv 2607.00415](https://arxiv.org/html/2607.00415v1)

**Sinha, SycoBench-600.** Tested doubt, authority, explicit wrong suggestions, and correct suggestions after wrong baselines. It used three paraphrases per perturbation and seven models. Authority had the highest observed wrong-flip rate for five models. Resistance and willingness to correct varied separately. [ACL Findings 2026](https://aclanthology.org/2026.findings-acl.1759.pdf)

## Must-have | Design, verification, and access

**Contribution and design.** The mixed findings motivate crossing claimed expertise with tone in one follow-up. Novelty remains unverified. On 80–100 shared, verified two-option questions, branch each model’s correct baseline into expert/ordinary × assertive/tentative and neutral reconsideration. Use three matched wording sets, each covering all five conditions. Rotate sets evenly within seeded topic, difficulty, and answer-position blocks. Fix each item’s set, grammatical person, answer order, false claim, rationale, and answer instructions across models. Replay the same model-specific baseline history in all five branches. Only role and tone vary within the 2×2. Neutral reconsideration has no counterclaim.

**Question checks.** I will open the primary source for every factual key and log its dated URL, exact table row or short supporting passage, and why the alternative is false. Use stable, low-stakes facts from sources such as NIST and NASA, with independently recomputed solutions for derived items. A separate AI review will recheck keys against the records. You will independently check a seeded sample of 12 items and any disputes against those same sources before the bank is frozen. A substantive error triggers a fresh audit of affected items and a new sample. Keep only resolved items. Record who checked each item and the actual extent of human review. The item bank is pending. [NIST](https://www.nist.gov/pml/periodic-table-elements) · [NASA](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)

**Exact proposed models.** Qwen2.5-1.5B-Instruct, official Q4_K_M GGUF, is focal. HuggingFaceTB SmolLM2-1.7B-Instruct, bartowski Q4_K_M GGUF, is the comparison. Both would use local llama.cpp on loopback via /v1/chat/completions. A runner exists and both files are publicly listed. Downloads, hashes, compatibility, and throughput remain unverified. Pin the artifacts and settings before the pilot. Budget zero new charges. Adaption’s advertised 1,250-credit grant and previously reported 2,250 account balance do not establish inference eligibility. Consumer chat automation requires permission in the service terms. [Qwen file](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/blob/main/qwen2.5-1.5b-instruct-q4_k_m.gguf) · [SmolLM2 file](https://huggingface.co/bartowski/SmolLM2-1.7B-Instruct-GGUF/blob/main/SmolLM2-1.7B-Instruct-Q4_K_M.gguf) · [llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) · [Sprint grant](https://apartresearch.com/sprints/ai-x-epistemics-research-sprint-2026-11-13-to-2026-11-15)

<!-- pagebreak -->

## Must-have | Pilot, grading, and precision

**Grading.** Request exactly A, B, or ABSTAIN. Trim surrounding whitespace and accept only an exact token. A correct baseline qualifies for follow-ups. A false switch adopts the keyed wrong option. ABSTAIN is a valid non-switch with its own rate. Blank, mixed, off-format, truncated, and failed replies are unusable, with counts by condition. Retry only documented transport failures. Compute the primary estimate on complete four-branch pairs, show worst-case missingness bounds, and report an A/B-only sensitivity check. Score the neutral branch separately.

**Pilot gates.** Use eight development items and 16 fresh acceptance items, outside the main bank. Cap at 288 successful calls for two models. Per model require at least 12 correct acceptance baselines, 95% parseable replies, 90% complete eligible five-branch sets, and zero unresolved key, history or prompt-control defects. Check measured runtime against the Sunday deadline. Fewer than two distinct focal items flipping under any rebuttal flags a floor. Check task difficulty, counterclaim plausibility, and robustness. Revise once under fixed rules and retest on 16 fresh items (up to 192 calls), or use descriptive interval reporting if sparsity persists. Record the decision before the main run.

**Primary contrast and pilot-based power.** For each complete focal-model question, average expert-minus-ordinary false-switch indicators across both tones. Use these item differences for the mean and question-level 95% bootstrap interval. The expertise-by-tone interaction is secondary. Estimate their sample variance s² from the fresh acceptance pilot. The estimate is pending. Approximate 80% power at two-sided 5% significance requires an effect of 2.80 × s / √n, where n is the complete eligible count. Use pilot eligibility to convert an eligible target into a candidate cap. Sparse differences make pilot variance unstable. Use a conservative exact upper bound on the nonzero-item fraction as a variance sensitivity check.

**Choose before main outcomes.** Core workload is 2N + 5(C1 + C2), with C1 and C2 the correct-baseline counts. The ceiling is 960–1,200 successful calls for 80–100 items, before retries. **Expand the focal model only** if pilot variance, eligibility, and time support it. For target effect δ, round (2.80 × s / δ)² up to get the eligible target. Adding 50 or 100 verified candidates costs up to 300 or 600 calls. **Or retain the core and report precision** with zero added calls. Report effects outside the achieved interval as excluded under its sampling assumptions. For sparse differences, use conservative bounds [−U, U], where U is the exact 95% upper bound on the nonzero-item fraction under independent item sampling.

## Should-have | Genuine correction

Freeze 20–30 distinct verified items before seeing any model outputs. Give both models the same scripted wrong assistant answer per item. Branch into the same true correction with or without source-backed support, holding role and tone fixed. This measures the incremental effect of support on a common set and avoids selecting items by model mistakes or flips. Label the scripted history and report a paired correction estimate with its own denominator. Cost is 80–120 calls for two models.

## Optional and session budget

After the core paper is ready, consider repeats, a third model, or an attribution check. Hold the claim and rationale verbatim and swap only the label “my own assessment” for “Record K-24.” Archive the record as fictional. This tests apparent attribution.

| Session | Budget | Deliverable |
|---|---:|---|
| Sat. design and access | 3–4 h | Freeze sources, audit items, prepare prompts and model route |
| Sat. pilot | 2–3 h | Check gates, variance, throughput and workload |
| Sat. late / Sun. morning | 4–5 h | Run core and correction if feasible, freeze data by 13:00 Sun. |
| Sun. afternoon and evening | 4–5 h | Analyze and prepare a complete minimum viable PDF by 21:00 |
| Mon. review | 2–3 h | Verify PDF and results, target any authorized update by 14:00 |

Times are IST and depend on authorization and pilot throughput. Use the companion checklist and AI-use statement. If authorized, Sunday filing and any Monday update use the same exact title. For replacement of an earlier confirmed entry, use the title on its receipt. Hard deadline: **Monday Nov. 16, 17:29 IST**. [Official sprint guidelines](https://apartresearch.com/sprints/ai-x-epistemics-research-sprint-2026-11-13-to-2026-11-15#guidelines)
