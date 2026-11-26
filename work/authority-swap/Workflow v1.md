# Authority Swap — Research Workflow

Version 1 • Prepared Friday, 13 November 2026 • All calendar times are India Standard Time, UTC+05:30.

**Current status: planning only.** This document schedules future work. It does not establish that the literature review, dataset, pilot, experiments, or new report are complete. No new study inference was performed to prepare it. The previous submission remains on hold.

## Part 1. Define the project and the working agreement

### 1.1 The proposed question

When rebuttal content is held constant, how much does unverified claimed expertise change a model's probability of abandoning a correct factual answer? Can an evidence-focused response procedure reduce harmful reversals while preserving genuine correction?

The primary experiment measures an authority effect. Tone, evidence presentation, confidence changes, and correction behavior help interpret it. We will not assume an effect exists or describe all deference to expertise as irrational.

### 1.2 Intended contribution

The candidate contribution is a tightly controlled comparison of authority framing, paired with an explicit correction control and a reproducible set of stimuli. A small mitigation experiment is an extension if the core is sound. The novelty claim remains provisional until the closest-work review is complete.

### 1.3 What a strong finished project contains

- A precise question and comparison with the closest existing studies.
- Verified questions, answer keys, evidence records, and transparently constructed experimental rebuttals.
- Recorded model versions, settings, prompts, raw responses, usage, failures, and scoring decisions.
- Paired comparisons with uncertainty, baseline accuracy, genuine-correction outcomes, and appropriately limited claims.
- A readable report and a package from which its numbers and figures can be regenerated.
- A checked final submission, with confirmation recorded if submission is authorized and succeeds.

### 1.4 How the three-day process works

We will spread design, execution, and review over separate sessions through Monday. Plan for approximately 20–30 focused working hours, with blocks of roughly 3–5 hours when access permits. These are work allowances, not guaranteed uninterrupted agent runtimes or a requirement to consume a particular quantity of credits. Each block ends with saved progress and a concrete next action.

The user will resume the chat after interruptions. Actual account availability determines when another session can begin. OpenAI's documentation directs users to their usage dashboard for current limits and reset times; a five-hour replenishment assumption is not sufficient to schedule guaranteed access. The requested assistant remains GPT-6 Astra with the user's chosen Ultra setting; this plan does not change it. [Official usage documentation](https://learn.chatgpt.com/docs/pricing#where-can-i-see-my-current-usage-limits)

### 1.5 Scope and existing work

The old “Counting Evidence by Origin” report and its data remain preserved as earlier sprint work. Their results do not become evidence for this new study. Any reused utilities must be documented. The old uploaded title, abstract, and PDF must eventually be replaced together. A planning request does not lift the user's earlier hold on submission.

**Completion condition:** the question, deliverables, current authorization, and previous-work status are recorded without implying new experiments have occurred.

## Part 2. Set calendar milestones and dependencies

The official deadline is Monday, 16 November 2026, 11:59 UTC, or **17:29 India time**. Our target is to have a complete draft Sunday evening and, if the submission hold is lifted, submit by **14:00 Monday**, leaving 3 hours 29 minutes for problems. [Official sprint page](https://apartresearch.com/sprints/ai-x-epistemics-research-sprint-2026-11-13-to-2026-11-15)

| Session | Intended window | Focus | Required saved result |
|---|---|---|---|
| A | Friday evening, current turn | Detailed planning | This workflow and a resume checkpoint |
| B | Next Friday session, or early Saturday | Closest-work review and design | Literature comparison, proposed contribution, draft protocol |
| C | Saturday morning | Questions, evidence, model access | Audited candidate corpus, available model list, initial cost worksheet |
| D | Saturday afternoon | Experiment runner and separate pilot | Pilot report, repaired pipeline, frozen main protocol |
| E | Saturday evening through Sunday morning, in resumed blocks | Main data collection | Saved batches, progress table, usage ledger, missing-cell list |
| F | Sunday afternoon | Analysis and predeclared validation | Reproducible tables, figures, sensitivity checks, claim ledger |
| G | Sunday evening | Complete report and supporting package | Full draft, citations, appendix, reproducibility archive |
| H | Monday morning through 11:00 | Critical review and corrections | Checked claims, regenerated calculations, final content |
| I | Monday 11:00–14:00 | PDF inspection and submission preparation | Reviewable final PDF and correctly populated form |
| J | Monday 14:00–17:29 | Submission and contingency, if authorized | Observed confirmation or an exact account of the remaining blocker |

### 2.1 Dependency rules

Large runs require a passed pilot. A novelty claim requires the literature comparison. Main scoring requires a frozen answer key and scoring policy. The report's claims require a traceable analysis. Submission requires the final artifact, review, and the hold to be lifted.

### 2.2 Schedule protections

- By Saturday evening, the primary design should be frozen and main collection should be ready or underway.
- At Sunday noon, assess time remaining using measured throughput. Drop optional extensions before compromising the main comparison.
- Target Sunday 18:00 for the primary data freeze. Any later run needs a documented reason and separate label.
- Target Sunday night for a complete draft, including limitations.
- Freeze substantive content Monday at 11:00. Use remaining time for corrections, rendering, and submission.
- If access interruptions threaten the schedule, reduce scope transparently. Never fill missing cells with invented observations.

**Completion condition:** every resumed session has one achievable work package and a named artifact, even if calendar windows shift.

## Part 3. Review the nearest research before claiming novelty

### 3.1 Build a focused reading queue

Start with the organizer-linked SycEval and ELEPHANT work, answer-reversal and challenge studies, and the two recent studies already identified. Verify the actual paper and its methods before citing it. Search for authority cues, persuasion under rebuttal, valid versus invalid correction, evidence fabrication, and confidence changes. Read the closest methods and limitations in full rather than relying on abstracts.

Initial verified starting points are [the official reading list](https://apartresearch.com/sprints/ai-x-epistemics-research-sprint-2026-11-13-to-2026-11-15#resources), [Big-Big-SycoBench](https://arxiv.org/abs/2610.15634), and [Beyond the Sycophancy Score](https://arxiv.org/abs/2610.08840). These are leads for the review, not a completed novelty assessment.

### 3.2 Create a comparison table

For each relevant study, record its exact question, task type, dataset, model versions, number of turns, authority manipulation, evidence manipulation, controls, confidence measure, analysis unit, public artifacts, and limitations. Include the source passage that supports each characterization. Record overlaps as well as differences.

### 3.3 Decide the contribution before large runs

Write a short statement explaining what our study adds and who can use the result. Candidate additions include a cleaner authority comparison, source-grounded factual controls, or a demonstrably useful correction procedure. If the closest work already covers our exact question, revise the scope before spending on the main study. A careful replication is permissible, but must be presented as replication rather than a new discovery.

### 3.4 Maintain an evidence ledger

Every external claim receives a source, a location in that source, and a note distinguishing the authors' finding from our interpretation. Dataset licensing, modifications, and reused code receive their own entries. Unknowns remain unknowns until checked.

**Completion condition:** a reviewer can see the closest existing work, the exact proposed difference, and the limits of our originality claim.

## Part 4. Freeze a coherent experimental design

### 4.1 Define the main outcome

The primary outcome is a **harmful reversal**: the model initially gives the verified correct answer, receives a counterclaim, and then gives a wrong answer. Record whether it adopts the specific false answer advocated by the rebuttal; with two answer alternatives these outcomes coincide. A change from a correct answer to uncertainty is recorded separately. Refusals and malformed responses remain visible. Initial abstentions are not naturally incorrect answers and are analyzed separately.

The primary authority effect is the difference in harmful-reversal rates between expert-claim and ordinary-speaker framing, paired on the same question, original response, tone, and rebuttal content. Average the predeclared matched contrasts within each model. Report percentage-point differences and uncertainty.

### 4.2 Separate expertise from tone

Use two authority levels, ordinary speaker and self-claimed relevant expert, crossed with two tone levels, tentative and assertive. Each factual counterclaim is otherwise identical. Expertise is unverified within the conversation. Do not compare an assertive expert only against a tentative ordinary person and then attribute the whole difference to expertise.

Audit lengths, wording, politeness, role descriptions, and answer leakage. Use generic roles without impersonating a real person. If several paraphrases are used, assign them by a fixed, balanced rule and record their versions.

### 4.3 Proposed main condition matrix

| Arm | Eligible baseline | Follow-up conditions | Purpose |
|---|---|---|---|
| Harmful reversal | Initially correct | 2 authority levels × 2 tones × 2 evidence presentations | Estimate the authority effect under matched counterclaims |
| Reconsideration control | Initially correct | Neutral request to reconsider, no new evidence | Measure answer drift without targeted persuasion |
| Confirmation control | Initially correct | Genuine supporting material for the original answer | Check that sound confirmation does not induce mistakes |
| Genuine correction | Initially wrong | Valid correcting evidence in the 4 authority/tone frames | Measure willingness to accept warranted correction |
| Correction reference | Initially wrong | The same ordinary-speaker, tentative correction with its evidence omitted | Distinguish a supplied correct claim from a supported correction |

The proposed evidence presentations in the harmful-reversal arm are an unsupported false assertion and the same assertion with fabricated support. This comparison bundles the presence and presentation of supporting material. It does **not** isolate authenticity by itself. A real citation can also be irrelevant or misquoted, so authenticity and actual support must have separate labels.

### 4.4 Keep the correction logic valid

For a stable factual question, genuine valid evidence cannot prove the opposite of an already correct answer. Genuine correction therefore belongs in the initially wrong arm. A confirming source can accompany an initially correct answer, but should not be called a valid rebuttal proving it wrong.

If naturally wrong answers are rare, report that the correction estimate is imprecise. An additional diagnostic may supply a deliberately incorrect assistant history, but it must be labeled artificial and analyzed separately. Do not pool such cases with naturally occurring model mistakes.

### 4.5 Use independent conversation branches

Run a baseline once under the frozen procedure. Clone its exact visible history for every follow-up condition. Each branch receives only its assigned follow-up. No branch may inherit another condition's answer or conversational memory. The core study uses one pushback turn; repeated escalation is optional and must not silently replace the core question.

### 4.6 Treat confidence consistently

Prefer two clearly defined answer alternatives if the selected benchmark supports them. Record a numerical probability for a fixed alternative before and after pushback, with answer labels balanced and held constant across branches. This avoids comparing confidence in different propositions after a flip. Record the final answer separately. State that elicited confidence is a model output, not a direct measurement of an internal belief.

The exact response format, probability validation, and abstention handling must be settled in the pilot. Missing probabilities do not erase otherwise usable answer data.

### 4.7 Write and timestamp the protocol

Freeze hypotheses, primary outcome, planned comparisons, condition wording, sampling, exclusions, scoring, model settings, uncertainty method, missing-data treatment, optional extensions, and stopping rules. A local timestamped plan is a dated analysis plan; do not describe it as publicly preregistered unless an actual public registration is made. Record later changes and their reasons.

**Completion condition:** the design changes one intended factor at a time within each authority comparison and cannot mistake stubbornness for success.

## Part 5. Build and audit the question and evidence corpus

### 5.1 Proposed size and separation

Plan for 20 pilot questions and a fixed main pool of 200 questions, with a feasible fallback of 150. Pilot and main questions must not be near duplicates. Final size follows feasibility and precision checks before main results are inspected. Do not keep adding questions solely until a desired result becomes significant.

### 5.2 Select suitable material

Prefer an established, reusable factual benchmark with clear licensing and sources. Choose stable facts with unambiguous answers. Exclude open-ended advice, contested normative judgments, ambiguous time references, and questions whose answer depends on unstated assumptions. If a source format is adapted, document the transformation and its possible effects.

### 5.3 Record each item completely

Each item needs a stable ID, question, allowed answers, correct answer, topic, source URL and passage, evidence-support label, source-authenticity label, counterclaim, experimental rebuttal variants, and any exclusion reason. Add the source retrieval date. Keep the answer key inaccessible to the tested model except where evidence is deliberately supplied by the assigned condition.

### 5.4 Verify ground truth and stimuli

Check every retained answer against the designated evidence. Resolve source conflicts before testing. Inspect whether the counterclaim is truly false and whether a genuine correction actually supports the answer. Mark fabricated material clearly in the research archive, while retaining the exact stimulus shown to the model. Avoid passing synthetic passages off as actual research references.

### 5.5 Prevent selection bias

Select the main pool before seeing main model behavior. Balance domains and correct-option positions using declared rules. Report all baseline answers. For each model, harmful-reversal analysis uses its initially correct subset and correction analysis its initially wrong subset. Show each denominator. Different models may have different subsets; a secondary comparison uses their shared initially correct questions and reports how that restriction changes coverage.

### 5.6 Plan actual human review honestly

Offer the user a manageable packet, for example 15–20 questions and selected responses, with clear checking instructions. Record which examples the user actually checks and any disagreements. Assistant or agent review must be described as AI-assisted review. If no human review happens, use objective scoring where possible and state the limitation.

**Completion condition:** every retained question has defensible ground truth, and the dataset can be inspected without relying on an undocumented judgment.

## Part 6. Confirm models, access, and the credit budget

### 6.1 Keep assistant usage separate from experiment resources

The user's Astra allowance supports research assistance. Adaption credits support calls made through Adaption. The stated balance is 2,250 credits; verify the current balance and billing behavior when execution starts. Do not assume that a credit equals a dollar or that a displayed dollar-spend field directly measures consumed sponsor credits.

### 6.2 Verify the actual model inventory

The provisional shortlist is Qwen3.5-397B, GLM-5.2, and Gemma-4-31B-IT, drawn from the catalog checked during planning. Exact access and current identifiers remain unconfirmed for this study. Save the account-accessible inventory, prices, and settings before final selection. If necessary, choose another available family using capability, reproducibility, cost, and task suitability, without silently substituting models.

### 6.3 Record configuration fairly

For every model, save provider, requested and returned model identifier, date, API mode, system instructions, sampling settings, output limits, reasoning settings if exposed, tool availability, and memory behavior. Disable tools and persistent memory for the core experiment where supported. If settings cannot be matched, document that rather than claiming perfectly equal compute.

### 6.4 Estimate workload without inventing a price

With 200 main questions and 3 models there are 600 baseline calls. Initially correct cases have 10 proposed follow-ups; initially wrong cases have 5. If all baselines are eligible correct or wrong answers and c is the fraction initially correct, the successful-call estimate is 600 × (6 + 5c), at most 6,600 before pilot calls, retries, repetitions, or extensions. Initial abstentions and invalid baselines require their separately recorded policy. This is a planning calculation, not a run count.

The pilot must measure input/output usage, latency, errors, and provider-reported credit consumption. Use those observations and the actual rate card to estimate each phase. Include a conservative runtime estimate and a reserve for technical retries and necessary verification.

### 6.5 Allocate resources by scientific purpose

Create rows for pilot, core collection, correction controls, selected repetitions, optional mitigation, and reserve. Keep roughly 15–20% of the chosen experiment budget available for repair and verification initially. The total may use the existing credits generously if scientifically useful. Unspent credits are acceptable. Purchases, paid overages, additional payment methods, and new paid commitments remain outside this plan without clear consent.

**Completion condition:** model access is real, the estimated run fits both time and existing credits, and the spend guard is based on measured units.

## Part 7. Build a reliable, recoverable experiment process

### 7.1 Plan the records before running

Every attempted request gets a unique key containing question, model, condition, repetition, and protocol version. Save the exact request and raw response immediately. Keep the parsed answer and confidence separately so scoring can be repaired without another paid inference.

### 7.2 Capture enough context to reproduce results

Save timestamps, model/settings metadata, prompt hashes, baseline-history identifiers, response identifiers, completion status, token usage, observed credit usage where available, latency, finish reason, and errors. Keep credentials out of reports, screenshots, archives, and progress notes.

### 7.3 Handle interruptions and retries

Resume only missing requests. Keep a bounded retry policy for transport errors. Do not retry semantic refusals or unwanted answers to obtain a preferred response. Detect duplicates. If a timeout leaves a request's outcome uncertain, record that uncertainty and use the provider's retrieval or idempotency support when available before retrying.

### 7.4 Interleave conditions and models

Use a seeded randomized schedule so every condition is not run in a different time block. Preserve matched comparisons. Respect rate limits and use small recoverable batches. If a model alias changes or the service behavior changes, split the affected runs into separate versions rather than silently merging them.

### 7.5 Test meaningful invariants

Check that expert and ordinary prompts differ only as intended, every branch uses the correct baseline, no gold answer leaks into the baseline, all expected condition cells exist, and interrupted runs resume without duplicating completed calls. Verify the parser against known examples and malformed outputs. These checks protect scientific validity.

**Completion condition:** a small interrupted rehearsal can resume cleanly, and every reported value will be traceable to a saved response.

## Part 8. Run the pilot and freeze the main study

### 8.1 Use separate development and acceptance items

Use part of the pilot for repairing wording, parsing, and logging; use the remaining items to check the repaired procedure. Preserve all pilot attempts and label them exploratory. Exclude pilot items from confirmatory main estimates.

### 8.2 Inspect the right failures

Check ambiguity, evidence validity, response extraction, answer-position bias, uncontrolled memory, incompatible settings, excessively long outputs, model refusals, missing confidence, and runtime. Investigate any mismatch between recorded costs and provider usage. Do not select final prompts because they produce the largest authority effect.

### 8.3 Pilot acceptance gate

Require no unresolved ground-truth or condition-assignment error; exact preservation of baseline histories; a documented parser policy; no unexplained loss of responses; and a feasible runtime/budget projection. Any extraction error must be understood before scale-up. A percentage threshold cannot excuse a systematic error.

### 8.4 Assess precision and freeze decisions

Use pilot variability and paired disagreement rates to estimate what the proposed sample can distinguish. Label any simulated power calculation as simulation, separate from observed experiments. If small effects will remain uncertain, plan to report that. Freeze sample size and planned analyses without choosing a sample to guarantee significance.

**Completion condition:** a written pilot report explains what changed, why it changed, and why the main procedure is now ready.

## Part 9. Collect the main data in auditable batches

### 9.1 Establish baselines

Run the fixed main pool for each selected model. Score initial answers using the frozen key, retain raw outputs, and record baseline accuracy, uncertainty, abstentions, and invalid outputs. Assign follow-up arms by the predefined baseline rule.

### 9.2 Run matched branches

Execute the planned authority, tone, evidence, and control conditions from their saved baselines. Save each result as it arrives. Update progress by model and condition, not merely a total request counter.

### 9.3 Monitor technical quality without tuning conclusions

Inspect missing cells, duplicates, output truncation, service errors, and usage. Do not repeatedly examine significance to decide when to stop. If a substantive defect is discovered, record the affected scope, amend the protocol, and rerun or exclude the affected block transparently.

### 9.4 Save a batch summary

Each batch records expected, successful, failed, pending, and uncertain requests; current usage; next request range; and any technical concern. A run is complete only after its manifest and saved outputs reconcile.

### 9.5 Freeze the primary dataset

Record a dataset version and file hashes, the exact inclusion policy, missingness, and deviations. Preserve the original records. Do not overwrite observations when producing cleaned analysis tables.

**Completion condition:** the primary dataset is complete or explicitly bounded, with failures and exclusions accounted for.

## Part 10. Run only the extensions that answer a defined question

### 10.1 Repetition and stability

Preselect a balanced subset for repeated baseline and follow-up trials. Use repetitions to estimate stochastic variability and the stability of correct initial answers. Keep all observations, and treat repeated responses from the same item as related. Do not call thousands of responses thousands of independent questions.

### 10.2 Evidence-focused mitigation

Define one procedure during pilot development: distinguish the speaker's status claim from the evidence, assess the supplied material, and then answer. Request only a concise explanation, not private chain-of-thought. Compare against a matched reconsideration instruction where feasible so added attention or length is not mistaken for the whole mechanism.

Select its evaluation subset before inspecting main effects; for example, reserve 60 main-pool items from intervention development. Freeze the intervention before viewing its evaluation outcomes. Measure harmful reversals and genuine correction separately. A refusal to change every answer is not successful mitigation.

### 10.3 Keep verification claims proportionate

A model without source access cannot necessarily determine whether a plausible passage is fabricated. Describe a prompt-based procedure as assessment of supplied evidence, not independent source verification. Adding browsing or retrieval would be a separate experiment with its own controls and costs.

### 10.4 Expansion priority and stop rule

Prioritize resolving measurement errors, adequate distinct questions, stability checks, and correction coverage. Add an extra model or multi-turn escalation only if the core and report remain on schedule. No extension should be added merely because it makes a headline more dramatic. At Sunday noon, drop extensions that threaten the primary work.

**Completion condition:** each extension has a predeclared purpose and remains separate from the core comparison.

## Part 11. Analyze the data and challenge the interpretation

### 11.1 Start with the data audit

Reconcile all counts, inspect duplicates and missing cells, confirm prompt matching, and reproduce baseline scores from raw outputs. Show the number of distinct questions as well as responses. Explain all exclusions by model and arm.

### 11.2 Produce the core results

For each model, report baseline accuracy; harmful-reversal rates by condition; paired authority effects; genuine-correction rates; neutral reconsideration behavior; confirming-source behavior; and confidence changes. Display denominators beside rates. Correction and reversal are separate axes, not an arbitrary combined safety score.

### 11.3 Quantify uncertainty correctly

Use paired item-level comparisons. Resample entire questions, preserving their conditions and repetitions; if items share a source or template, assess clustering at that level too. Predefine a 95% interval method. If formal significance tests are used for the three primary model-specific effects, address that family of comparisons. Label interactions and additional subgroup results secondary or exploratory.

### 11.4 Check fair comparisons and missingness

Show both each model's own initially correct subset and the common-correct subset. Explain selection effects and changing coverage. A failed response is not a correct answer. Predefine missing/abstention categories and provide sensitivity bounds or alternative analyses when missingness could change conclusions. Do not hide cases by dropping them after seeing outcomes.

### 11.5 Examine confidence carefully

Compare changes for the same proposition. Describe calibration only with a defined score and suitable denominators; avoid fine-grained calibration plots supported by very few items. State when confidence extraction fails. A change in verbal certainty alone does not prove an internal belief change.

### 11.6 Inspect examples and alternative explanations

Check whether reversals reflect baseline guessing, confusing questions, unequal evidence, refusal behavior, source salience, formatting, answer-position bias, or model-version changes. Choose qualitative examples by a recorded rule including typical cases and counterexamples. Explain what a small or null authority effect would and would not establish.

### 11.7 Maintain a claim ledger

Every proposed result sentence links to its analysis output, raw data, uncertainty, and caveat. Mark whether it was planned or exploratory. Regenerate all tables and figures from the frozen data, and independently inspect a sample of calculations.

**Completion condition:** every main claim is supported by a reproducible calculation, and reasonable competing explanations have been considered.

## Part 12. Write the report and supporting materials

### 12.1 Apply the verified submission rule card

Use the current official template; keep the main report within eight pages, excluding references and appendices; include a 150–250-word abstract, accurate author/affiliation details, and the required “Limitations and Dual-Use / Ethical Considerations” appendix. Disclose reused work and distinguish sprint contributions. AI assistance is permitted; the team remains responsible for accurate results and references. A public repository and video are optional. [Official guidelines](https://apartresearch.com/sprints/ai-x-epistemics-research-sprint-2026-11-13-to-2026-11-15#guidelines)

### 12.2 Plan a compact paper

Aim for roughly six to eight main pages, adapting to the actual template. Allocate space to the question and contribution; closest work; conditions and source construction; model and scoring methods; primary results; correction and robustness results; and discussion. Keep complete prompts and detailed failure tables in supporting material where appropriate. Draft the abstract after results are stable.

### 12.3 Design a small set of useful figures

Prefer a condition diagram, paired authority-effect plot with intervals and sample counts, correction-versus-reversal plot, and a compact examples table. Each figure must be readable at final PDF size. Avoid decorative plots or rankings that conceal uncertainty.

### 12.4 Write naturally and precisely

Explain what was done, what happened, and what remains uncertain in ordinary language. Remove formulaic filler, repetitive transitions, and unsupported grand claims. Read the draft for flow and use concrete examples. Preserve accurate descriptions of AI assistance and actual human participation; natural prose must not create a false research history.

### 12.5 Cover limitations and ethics substantively

Discuss question selection, possible benchmark contamination, model access and versioning, elicited confidence, stochasticity, correction sample size, realism of prompts, absence of human-user outcomes, and any missing human review. Explain why deliberately misleading stimuli were used and how released materials label them. Describe personal-data handling and plausible misuse without presenting fabricated stimuli as factual sources.

### 12.6 Assemble the reproducibility package

Include the protocol, item/evidence records where licensing allows, full prompt templates, model/settings manifest, raw or appropriately redacted responses, scoring and analysis utilities, usage summary, figures, decision log, licenses, and instructions for regenerating results. Separate locally reproducible analysis from inference that requires provider access and credits. Exclude credentials and unrelated personal information.

**Completion condition:** a new reader can understand the contribution and trace the results without reading this conversation.

## Part 13. Conduct a fresh critical review on Monday

### 13.1 Review the scientific claim

Ask whether the contribution is supported, whether the claimed authority effect is actually a tone or evidence effect, and whether any reported improvement merely makes the model stubborn. Check that observations are not generalized to all models, all languages, or real users without evidence.

### 13.2 Review the numbers and sources

Recompute report tables from the archived data. Inspect a sample of raw responses against reported scores. Verify model names, sample sizes, denominators, uncertainty labels, and all references. A second AI reviewer is useful but must not be described as an independent human annotator.

### 13.3 Review against the rubric

| Dimension | Evidence we must be able to show |
|---|---|
| Innovation and impact | Closest-work comparison, precise added contribution, credible use of the result |
| Execution | Sound controls, source-grounded labels, paired comparisons, uncertainty, reproducible records |
| Clarity | One main question, readable figures, understandable methods, restrained conclusions |

Record weaknesses and repairs. Do not invent predicted judge scores or promise a prize.

### 13.4 Review the rendered PDF

Inspect every page for cropping, tiny labels, missing equations, broken links, inconsistent numbering, wrong author information, and awkward page breaks. Check abstract length and the main-page boundary. Open the final file after export and compare its title/version with the package.

### 13.5 Prepare a short explanation for the user

Provide the final question, actual models, main findings, strongest limitation, credit usage, and location of supporting evidence. Make the final PDF concrete and reviewable before the held submission decision.

**Completion condition:** unresolved issues are listed honestly, and the final artifact is ready for an informed submission decision.

## Part 14. Prepare, submit, and verify the correct project

### 14.1 Replace the earlier project draft carefully

Inspect the existing form state. Replace the previous project's title, abstract, attachment, track selection, and supporting links together. Verify that the new PDF is actually attached and the account/team details are accurate. Preserve the previous report locally for provenance.

### 14.2 Honor the outstanding submission hold

The user previously said to wait before submission. Do not treat this workflow as consent to click Submit. When the final report is ready, request only the remaining decision, with the actual file and relevant terms available for review. Do not ask repeatedly for previously settled routine details.

### 14.3 Verify completion

After authorized submission, inspect the success state and the organizer's confirmation email for the matching title and PDF. An uploaded file alone is not a completed submission. Record the time, version, and confirmation evidence. The organizer identifies the confirmation email as the way to verify receipt. [Submission FAQ](https://apartresearch.com/sprints/ai-x-epistemics-research-sprint-2026-11-13-to-2026-11-15#guidelines)

### 14.4 Handle blockers promptly

If login, CAPTCHA, OTP, unresolved consent, or an inaccessible form needs the user, identify the exact action promptly and continue unrelated packaging or verification. Do not silently wait until the deadline. A necessary message to organizers requires explicit authorization before sending.

**Completion condition:** confirmed submission of the intended report, or a precise statement that submission remains blocked and why.

## Part 15. Save enough state to resume after every interruption

### 15.1 The checkpoint contents

After each meaningful batch and before a planned pause, save:

1. Timestamp, phase, and current authorization.
2. What actually completed, with artifact locations.
3. The next three actions, in order, and their prerequisites.
4. Frozen protocol, dataset, prompt, model, and analysis versions.
5. Completed, missing, failed, and uncertain run counts by condition and model.
6. Actual provider usage, estimated pending usage, and budget remaining.
7. Active job identifiers and whether their continued operation was actually verified.
8. Decisions, deviations, and unresolved scientific questions.
9. User-dependent blockers and work that can proceed independently.
10. Submission state and the exact report version in the form.

Do not rely on reaching a usage limit gracefully. Save incrementally so a sudden interruption loses as little as possible. Never assume that an experiment or assistant continued running during a break without checking its logs.

### 15.2 Resume routine

Read the checkpoint and current artifact manifest; confirm the current date and deadline buffer; inspect any existing process before starting another; reconcile usage; and perform the next unfinished task. Avoid re-reading the entire conversation or rerunning completed paid calls when saved evidence is sufficient.

The user can resume with: “Continue the authority-swap study from the saved checkpoint. Keep using GPT-6 Astra. Report the next stage before starting it.” The current checkpoint still requires the user to begin execution because this turn is planning only.

### 15.3 Scope-reduction rules

| Problem | Planned response |
|---|---|
| Exact design duplicates recent work | Refine the contribution before the main run, or explicitly frame a replication |
| One model unavailable | Use a documented substitute or reduce the model comparison transparently |
| Too few initially wrong answers | Report correction uncertainty; keep artificial-history diagnostics separate |
| Ambiguous ground truth or biased prompts | Repair before scale-up; preserve versions and affected-run accounting |
| Low response extraction quality | Fix the parser or format on pilot material; do not hide invalid responses |
| Deadline pressure | Drop optional models, escalation, and mitigation before weakening core validation |
| No clear authority effect | Report the estimate and uncertainty; do not redesign post hoc to force an effect |
| Mitigation damages valid correction | Report the tradeoff; do not claim an unqualified improvement |
| Access or allowance interruption | Save state and resume from the last verified batch when the user returns |
| Submission cannot be confirmed | Report it as unconfirmed or blocked, with the precise missing step |

### 15.4 Definition of finished

The research is finished when its bounded question has been investigated, the results are traceable, the limitations are stated, and the final report has passed review. The submission is finished only when receipt of the correct report is confirmed. Time spent, credits consumed, an attractive PDF, or an uploaded attachment alone cannot establish either outcome.

## Current handoff

**Completed in this planning turn:** a detailed workflow, design-risk review, scheduling and interruption plan, and fresh checks of the public deadline/guidelines. Two AI planning reviews informed this workflow.

**Not completed for the new study:** full literature review, final novelty claim, question corpus, account/model access verification, experiment runner, pilot, main experiments, results, report, or submission.

**Next action when the user starts execution:** Part 3, the closest-work comparison, followed by the draft protocol in Part 4. No experiment should begin merely because this plan has been saved.
