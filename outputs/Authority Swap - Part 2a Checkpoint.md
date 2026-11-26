# Authority Swap | Part 2a checkpoint

Updated: 2026-11-14 01:27 IST. **Part 2a complete; stopped. Part 2b has not begun.** Required next instruction: **“Proceed to Part 2b.”**

## What finished

- Drafted **138 distinct two-option candidate questions**: **90 main** (30 easy, 30 medium, 30 hard), **8 pilot development**, **16 pilot acceptance**, and **24 genuine-correction** candidates. Main items span six broad domains: astronomy (12), earth science (18), history/culture (17), life science (13), ocean science (12), physical standards (18). There are 48 distinct candidate source URLs from official NASA, BIPM, IUPAC, USGS, NOAA, NPS, Library of Congress, NHGRI and Smithsonian pages. This is a source-pointer inventory, not a verified source record.
- Ran structural checks: all 138 JSONL records parse; IDs and exact stems are unique; the three banks are separate; the main draft answer positions balance 45 A / 45 B and each tier 15 A / 15 B. Replaced one near-duplicate NASA eccentricity comparison before assembly. The earlier *Counting Evidence by Origin* project used fictional source-origin cases; none of its questions or response data was imported. Source-family correlations and subtler semantic overlap still require Part 2c audit.
- Split the public question review copy from provisional keys. The public CSV has no answer-key or draft-rationale fields. **No key, difficulty label, cited fact, source passage, or false alternative has yet passed blind verification.** Do not use this bank for inference.
- Wrote a planning-only Part 3 model/credit outline and a pilot-only focal-model selection rule, with its limitations. No Adaption account or key was accessed and no credit was spent.

## Files and versions

- Key-free review copy: `outputs/Authority Swap - Part 2a Draft Questions.csv`, **draft-v1**, SHA-256 `88A23677DC3115CEAC8EF502170319C1E74F80F8AB5C0C65354BB834B7A71636`.
- Provisional key/rationale file, **do not read before independent Part 2b key derivation**: `work/authority-swap/questions/draft-keys-v1.csv`, SHA-256 `338EEB9C3AC052E6008E03812253F593EAC8B8D62C881DAFC9641C036C48CA3F`.
- Original draft fragments with provisional keys: `work/authority-swap/questions/p2a_space_standards.jsonl` (SHA-256 `257DE7CA22CDF2BC48482987BD1141C1C6204C0F0768E972533F76EE16DC0A87`), `p2a_earth_ocean.jsonl` (`2ACF18AEC24F10DC9A54A7CF51EA17868DD2EBDE4D9BAF083607BDBDD9408038`), `p2a_culture_bio.jsonl` (`C49924FB6464DAEB05DE7AFF9793C54E6DF667860506BDBFDD116C5E6F6DD802`). Their keys must also be hidden from blind reviewers.
- Planning record: `outputs/Authority Swap - Part 2a Design Notes.md`; assembly script: `work/authority-swap/questions/build_draft_bank.py`. Part 1 literature: `outputs/Authority Swap - Part 1 Literature and Framing.md`. Part 0 hardware/tools: `work/authority-swap/checkpoints/part-0.md`.
- Protocol: **draft v3.2** (Part 1 v3.1 plus this bank/model plan), **not frozen**. Dataset: **draft-v1**, 138 unverified candidates; verified/eligible count **0**. Model runner, pilot outcomes, analysis and paper: not started.

## Model and credit plan carried forward

- Pilot at most **five candidates**: Qwen2.5-1.5B and SmolLM2-1.7B locally, plus up to three hosted candidates chosen before the pilot from the user's named Adaption models. Hosted IDs, availability, token prices and supported settings remain **unverified** until Part 3. Main may use at most **three gate-passing models** and remains held.
- Part 3: at most **five hosted smoke-test calls** total; user reports dashboard balance before and after. Never print/log `ADAPTION_API_KEY`. List models available to the key; check temperature, seed, max tokens, log probabilities and reasoning controls; pin a reasoning setting; log input/output tokens and credits per call. Hard project cap **150 Adaption credits**, including smoke, pilot, correction and any hosted main calls, unless the user explicitly approves more. Stop if the next call's worst-case cost cannot be bounded. Run local models one at a time, test CPU throughput first, and consider GPU offload only if needed.
- Proposed focal rule: among models passing the predetermined parse, pair-completion, both-order eligibility, floor/ceiling and feasibility gates, choose the one with most both-order eligible **pilot** items; tie-break by projected cost then fixed model ID. Never choose on the expertise contrast or main outcomes. **Critique:** 16 pilot acceptance items produce noisy eligibility and gate decisions, potentially favor large models; report all pilot gates and restrict claims to the selected model. Cross-model rates need a common eligible intersection or an explicit differing-item caveat.
- The user's current working title says “Small Local Models.” If a hosted model enters the main study, the title may misdescribe the work. The user confirms the final distinct second-project title before Part 7. Prior-project shared llama.cpp tooling or any code later reused must be disclosed.

## Usage so far

- Authority Swap inference calls: **0 local, 0 hosted**. Adaption credits used by Authority Swap: **0**; new charges: **0**. User-reported balance: **2,750 credits**, not independently checked. Whether that balance can fund hosted inference remains unverified.
- No model downloads, baselines, pilot, main experiment, submission form actions or submissions occurred in Part 2a. Part 2a elapsed wall time was about 20 minutes.

## Open issues and holds

- **Part 2b must derive each answer independently from the primary source before opening the draft-key file**. Record access date, exact source passage/table cell, derived key, and why the other option is false; only then compare the proposed key, resolve or exclude disagreements, and assign a verified version. Direct access to the canonical USGS earthquake FAQ used by draft item **E011** timed out; the source query URL requires checking or replacement. NPS Grand Canyon numerical ages were selected from a newer table because older NPS pamphlet values differ; check the exact version in Part 2b.
- The 90 main items are candidates, not 90 eligible items. After source checking and per-model correct baselines under **both A/B orders**, the usable number may shrink; replacements or a cut-down fallback are Part 2b/2c decisions. The user must receive **exactly 12 selected item IDs and source locations at the end of Part 2c** for their own check before the main bank freezes.
- Part 2c independently audits source/answer quality, semantic overlap and tier balance, estimates item-verification time and specifies the cut-down fallback. Do **not** perform that audit in Part 2b prematurely. The working title, final models, sponsor inference pricing and exact credit balance are open.
- Official deadline per user-verified sprint facts: **16 November 2026, 17:29 IST**. This is a **separate second project**, not a same-title replacement of *Counting Evidence by Origin*. **Main experiment: HELD. Submission: HELD.** Do not run Part 5 or submit without explicit later authorization.

## Next three actions

1. Wait for **“Proceed to Part 2b.”** Do no Part 2b work before it.
2. At Part 2b start, recommend Astra High and give blind reviewers only the key-free CSV and cited primary-source pointers; derive keys and source evidence before consulting draft keys.
3. Resolve source/key disagreements, write the verified-source ledger and versioned question bank, save the Part 2b checkpoint, report in at most 200 words, and stop for **“Proceed to Part 2c.”**
