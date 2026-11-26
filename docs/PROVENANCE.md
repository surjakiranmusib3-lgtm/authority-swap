# Publication provenance and scope

## What is preserved

The submitted PDF has SHA-256:

`2834ef783c4f439130e04bf4f1a9380c0da04acb831fce62d56f5679178dc8cb`

The final dataset, source-and-key ledger, frozen protocol/schedule, main normalized records, item summaries, and result CSVs are preserved. This public release adds documentation, a portable offline verification wrapper, an allowlisted accounting export, and publication manifests. The new wrapper operates on a disposable copy; it does not rewrite original analysis artifacts.

The saved report and checkpoints were created during the sprint. The GitHub commit time is the publication time, not evidence that every file existed in its final form before collection. Protocol hashes, checkpoints, and post-pilot labels provide the internal provenance trail. No external preregistration is asserted.

## Redactions and exclusions

`data/publication-provenance.json` lists copied files with original/public hashes and every applied redaction. Selected process files replace personal Windows home paths, private Google-document links, submission-page links, and email addresses with markers. Redacted historical file references may therefore be nonfunctional. The already-submitted PDF is preserved verbatim, including its author correspondence details.

The public package excludes credentials and environment files, private email/browser records, account screenshots, Google-document readbacks, private SQLite storage, model weights, llama.cpp binaries/DLLs, caches, locks, and server logs. A field-allowlisted accounting CSV replaces the private database for reproducibility. The original database hash in historical outputs refers to the original private artifact and will not match the minimal reconstructed database.

One accounting response-ID value matched a credential-shaped pattern and was replaced with a redaction marker before publication. Its row/column location is recorded in the publication provenance without the value. It is not used to calculate the result tables. Token counts, usage costs, attempt statuses, and timestamps are unchanged.

Full study API bodies and headers were not saved in the original experiment. Available non-study response bodies and normalized study records are distinguished by location and purpose. Files from *Counting Evidence by Origin* are excluded; that project shares only the llama.cpp executable and machine with this one.

## Verification provenance

Answer keys were verified by LLM-based agents plus a background-knowledge pass. A Claude (Anthropic) blind pass answered all 133 items from background knowledge, without opening the sources, before seeing the keys, with 133/133 agreement. This is not a source check. No human spot-check was performed. Cross-model agreement does not establish that source interpretations are correct or rule out correlated errors.

The human-check sample and second-reviewer queue are retained as process artifacts. Their presence must not be mistaken for completed human checks. Early literature notes and plans may contain explicitly unverified or subsequently superseded material; only the final report represents the submitted claims.

AI tools were used for coding, source verification, analysis and drafting. The author takes responsibility for the content.

Hosted inference used Adaption sponsor credits. The saved main accounting records show approximately 0.173298167 credits in usage and 0.08704 credits in unresolved reservations. The conservative project exposure at close was 3.280434 credits; it is not a dashboard-confirmed final charge. No new inference or credit spend is part of publishing this repository.

## Interpretation and dual use

The work measures a constrained factual-choice interaction, not general trustworthiness, truthfulness, intelligence, or resistance to all persuasion. Small changes, floor effects, and abstentions must not be exaggerated. Repeated false counterclaims are research stimuli; they are not guidance for deceiving users. The report's required appendix, “Limitations and Dual-Use / Ethical Considerations,” is the primary statement of these limits.

## Rights

The repository has no blanket reuse license. Original work remains subject to the author's rights and the accepted sprint terms. Public visibility does not transfer ownership or automatically grant an open-source license. Source quotations and third-party material retain their original rights. The repository does not redistribute model weights or llama.cpp binaries. Any future license decision should distinguish original code, original questions/analysis, and third-party excerpts.
