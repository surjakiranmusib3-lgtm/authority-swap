# Authority Swap protocol draft v3.4 — Part 2c amendments

14 November 2026. This records the completed dataset audit, not authorization to run a pilot or main experiment. The detailed model/credit and pilot-selection plan in `DRAFT_PROTOCOL_2A.md` remains in force where not superseded here. Part 1 literature and framing remain separate; no new novelty claim is made in this part.

## Candidate bank

Dataset v1.3 contains 85 main candidates (30 easy, 29 medium, 26 hard), 8 development-pilot, 16 acceptance-pilot, and 24 genuine-correction candidates. All tiers are provisional. No empirical baseline or reversal rate has been measured. Main eligibility is per model: correct under BOTH A/B answer orders. Different models may have different eligible populations; direct model comparisons require the common eligible intersection or an explicit population qualification.

The source-reviewed bank is frozen at 133 records. Twenty-nine questions use new facts and fourteen more have wording or citation changes; all 43 have fresh, key-file-blind source derivations. Ninety unchanged questions inherit Part 2b verification. The five permanently retired IDs are C027, C028, S017, S025 and S027. Full original versions and failed/superseded review records are preserved.

Main source pages are capped at five questions, including the NASA planet table and IUPAC list. Main/pilot/correction fact propositions and tested events are disjoint under the recorded audit. Shared entities, domains and source pages are still possible; fact disjointness is not a claim of statistical independence. C038 no longer shares the transcontinental-call event with main. C037 diversifies the torch section. C016 no longer exposes C004's answer year. The earlier project's synthetic question data are not reused.

Presentation balancing uses seed 2026111402 inside bank × provisional-tier strata. Main A/B counts are 15/15, 15/14 and 13/13; acceptance-pilot hard is 2/2; total A/B is 67/66. Every permutation preserves the independently verified answer text and maps it to the new key. At model runtime use ONLY the stem and answer options. Do not send sources, locators, keys, difficulty labels, verification notes or bank labels to the model.

The twelve human-check IDs are C008, E018, S028, C032, E032, E033, S035, E036, C035, C040, E041 and C044. Seed 2026111402, one item per bank × tier, first accepted random draw with at least three revised/new items; actual changed count is five. Human source checking is pending and must precede the Part 4 pilot. A different-family model review has not occurred; provide only the key-free CSV before disclosing the separate key ledger.

## Experimental design retained for later parts

Core false-rebuttal design: claimed expertise × tone, plus neutral control. Keep false factual content fixed across role/tone branches; use three paraphrases per condition, balanced and rotated across questions. Freeze prompts before outcomes. The primary contrast is each question's mean false-switch outcome under expert framing minus its mean under ordinary framing, averaged across two tones. Analyze paired questions, with intervals and pilot-estimated variance. Baseline correctness under both answer orders is an eligibility condition, not a result yet.

Retain floor and ceiling checks, parsing/completeness checks and gate-driven feasibility decisions. No pilot gate has been evaluated. Preserve all pilot candidate results, and never choose the focal model by the size of its expertise contrast. Use the previously proposed eligibility/feasibility rule with its documented selection limitations. If no model passes, stop and revise before main.

Correction-bank questions were selected before model errors or switches; their scripted wrong initial answers and true corrections remain to be frozen later. Do not retrospectively select correction items because a model happened to fail them. Any optional expert/ordinary true-correction crossing must be declared before outcomes. P(keyed wrong option) is a secondary continuous outcome only where supported and correctly normalized; missing log probabilities must not be treated as zero. Answer-format, abstention and unusable-response handling and local grammar support still require Part 3/4 implementation checks.

At most 85 main items can become eligible for a model. Pilot variance is UNMEASURED. Do not assume variance 0.20 or promise power for 5–10 percentage-point effects. Planning approximation: 95% paired interval half-width 1.96*s_D/sqrt(n), 80%-power two-sided 5% detectable difference about 2.80*s_D/sqrt(n). D lies in [-1,1]. Report ruled-out effect sizes from actual intervals; a null result is not evidence that authority has no effect. Any pre-result cut-down is described in the Part 2c Review and must be logged before treatment effects are inspected.

## Part 3 credit/model boundary

Adaption balance 2,750 is user-reported and unverified. Part 2c used zero Adaption credits and made zero experimental/API inference calls. User's chat-agent allowance is separate and unmeasured. Do not read, print or log the API key; the user sets ADAPTION_API_KEY themselves.

Part 3, after explicit authorization, covers local models, hosted credit smoke test and runner. Pilot candidates: two local models (Qwen2.5-1.5B-Instruct and SmolLM2-1.7B-Instruct) plus up to three hosted models whose exact availability, pricing and controls must be checked. At most three passing models may be used for the main experiment after separate authorization. User-named hosted IDs and credit-per-token prices remain unverified.

At most five hosted smoke-test inference calls total in Part 3. Record the user's dashboard balance before and after, list accessible models, test supported controls (temperature, seed, output cap, logprobs, reasoning mode), fix one reasoning setting per model and log token usage per call. Hard cap 150 credits for the entire project, including smoke/pilot/correction/main; do not call if verified pricing and bounded token use cannot conservatively keep within that cap. No payment authorization is inferred. Local models run sequentially; CPU throughput first, GPU offload only if needed.

## Holds and paper obligations

Main experiment HELD until explicit Part 5 authorization. Submission HELD throughout; Part 8 stops for the user's decision. Authority Swap is a separate second project, not a same-title replacement of *Counting Evidence by Origin*. Working title: “Does Claimed Expertise Change False Switching? A Controlled Expertise x Tone Test in Small Local Models.” User confirms the final title before Part 7; hosted main models may require changed scope wording.

Later paper: official template, 150–250-word abstract, authors/affiliations, at most 8 pages excluding references/appendices, required “Limitations and Dual-Use / Ethical Considerations” appendix, AI-use statement, prior-work/shared-infrastructure disclosure, hosted-credit disclosure and truthful source/access limits. No fabricated results/citations. The user remains responsible for the report. Deadline supplied/verified earlier: Monday 16 November 2026, 11:59 UTC / 17:29 IST. No submission or paid action is part of Part 2c.
