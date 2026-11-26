# Reproducing the saved results

## Offline verification

Use Python 3.11+; there are no third-party package requirements:

```sh
python scripts/reproduce.py
```

The script verifies `SHA256SUMS`, extracts only explicitly manifested regular files into `_reproduction/workspace/`, reconstructs a minimal accounting database from the public CSV, and imports the preserved analysis code. It never loads an API key, launches a model, or makes a network request.

It checks:

1. Release and archive-member SHA-256 hashes.
2. Frozen v3.7 protocol, schedule, dataset, and source-ledger hashes.
3. Every saved main request's prompt, parent, and history hashes against the schedule.
4. Dual-order eligibility and the absence of unscheduled records.
5. All eight saved result tables: core branches, paired contrasts, escalation, escalation contrasts, correction, unusable diagnostics, timing, and hosted accounting.
6. The original main-record and item manifests.

Results are written to `_reproduction/verification.json` and `_reproduction/tables/`. A successful run prints `"status": "PASS"`, 5 models, and 5,354 audited logical records. This checks the saved data's internal consistency and calculation reproducibility; it does not independently establish the source facts or model identities.

## Data formats

- `data/research-records.tar.gz` preserves relative paths under `work/authority-swap/runs/`. Main records contain IDs, model and arm, item/orientation/branch, final assistant text, strict parsed labels, parent and prompt/history hashes, timing, and available usage metadata. Pilot and dummy schemas differ because the runner evolved.
- Full study API response bodies and request headers were not archived. The normalized records are the reproducibility artifact; they must not be described as complete raw provider responses.
- Main records and item summaries are byte-identical to their original files. Some dummy/setup metadata contains redacted local paths, with before/after hashes in the publication provenance.
- `data/hosted-accounting.csv` contains all 4,909 logged attempts across smoke, pilot, and main stages. Empty fields represent unavailable values. `provider_cost`, `estimated_credits`, and reservations have different meanings. Reservations are not confirmed charges.
- Baseline A/B order, scored orientation, wording set, branch order, correction excerpts, and model settings are in the frozen v3.7 schedule. Correction excerpts and scripted assistant answers can therefore be reconstructed.

## Historical collection code

The original collection scripts are included for inspection, not presented as a one-click fresh experiment. They contain the original time cutoff and budget safeguards. A new collection requires a separately versioned protocol, fresh authorization, and current provider documentation. Do not modify the frozen records to accommodate a rerun.

Local collection used llama.cpp build 12243 (`8766c0273`), CPU-first tests, fixed chat templates, greedy decoding, fixed seed, and grammar-constrained labels. Exact local model revisions and SHA-256 values are in `work/authority-swap/part3a/model-sources.json`. Weights, executable binaries, and DLLs are not included.

Hosted collection used the Adaption Responses API and the recorded provider IDs `gemma-4-31b-it`, `qwen3.8-27b`, and `qwen3.5-397b`. Parameters and supported/unsupported controls are documented in the final protocol and calibration records. Exact hosted reruns are not guaranteed: provider implementation, weights, and service availability may change, and hosted seed/log-probability support was limited.

The secret file path in the historical runner is a configuration reference only. No secret file or API key is distributed. The offline verification script does not need one.

## Limits of verification

All findings are descriptive. Model-specific eligibility selects different question populations. Curated questions, small eligible local samples, abstentions, strict output caps, source-review errors, and correlated AI verification errors limit interpretation. A degenerate bootstrap interval does not prove zero uncertainty; use the sparse bounds shown alongside it. Escalation and correction are exploratory post-pilot arms. Both orientations in correction are repeated observations of the same questions.
