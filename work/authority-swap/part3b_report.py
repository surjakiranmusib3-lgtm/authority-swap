"""Build a public-safe Part 3b report from the private hosted usage summary."""

import argparse
from decimal import Decimal
import hashlib
import json
from pathlib import Path

from hosted_runner import ROOT, RATES, MILLION


PROJECT = Path(__file__).resolve().parent
OUTPUTS = PROJECT.parents[1] / "outputs"


def response_fingerprint(value):
    return hashlib.sha256(value.encode()).hexdigest()[:12] if value else "Unavailable"


def money(value, digits=9):
    return f"{Decimal(value):.{digits}f}" if value is not None else "Unavailable"


def rate_cost(row):
    _, input_price, cached_price, output_price = RATES[row["model"]]
    n_in, cached, n_out = (row["input_tokens"], row["cached_tokens"], row["output_tokens"])
    if any(value is None for value in (n_in, cached, n_out)):
        raise ValueError("Shape metering is unavailable.")
    return ((n_in - cached) * input_price + cached * cached_price + n_out * output_price) / MILLION


def table(headers, rows):
    return "\n".join(["| " + " | ".join(headers) + " |",
                      "| " + " | ".join("---" for _ in headers) + " |",
                      *["| " + " | ".join(str(value) if value is not None else "Unavailable"
                                         for value in row) + " |" for row in rows]])


def build():
    calls = json.loads((ROOT / "summary.json").read_bytes())["calls"]
    by_id = {row["task_id"]: row for row in calls}
    known_cost = sum((Decimal(row["provider_cost"]) for row in calls
                      if row["provider_cost"] is not None), Decimal(0))
    meter_cost = sum((Decimal(row["provider_cost"]) for row in calls
                      if row["task_id"].startswith("cal-meter-") and row["provider_cost"] is not None),
                     Decimal(0))
    billed_rows = [row for row in calls if row["provider_cost"] is not None]
    reserved = sum((Decimal(row["reserved_microcredits"]) / MILLION for row in calls
                    if row["estimated_credits"] is None and row["status"] != "rate_limited"), Decimal(0))
    cost_checks = sum(abs(Decimal(row["provider_cost"]) - Decimal(row["estimated_credits"]))
                      <= Decimal(".000000001") for row in billed_rows if row["estimated_credits"])
    entries = [
        (row["task_id"], row["model"], row["status"], response_fingerprint(row["response_id"]),
         row["input_tokens"], row["cached_tokens"], row["output_tokens"],
         row["reasoning_tokens"], money(row["provider_cost"]))
        for row in calls
    ]

    budget = []
    for model, tag in (("gemma-4-31b-it", "shape-gemma"), ("qwen3.8-27b", "shape-off-q27"),
                       ("qwen3.5-397b", "shape-off-q397")):
        base, branch = by_id[f"cal-{tag}-base"], by_id[f"cal-{tag}-branch"]
        per_item = rate_cost(base) * 2 + rate_cost(branch) * 5
        budget.append((model, f"{base['input_tokens']} / {base['output_tokens']}",
                       f"{branch['input_tokens']} / {branch['output_tokens']}",
                       per_item * 24, per_item * 85))
    pilot_total = sum(row[3] for row in budget)
    main_total = sum(row[4] for row in budget)
    study_table = [(*row[:3], money(row[3]), money(row[4])) for row in budget]
    study_table.append(("Three hosted models", "", "", money(pilot_total), money(main_total)))

    report = [
        "# Authority Swap Part 3b usage and budget",
        "",
        "15 November 2026 IST. All calls below used synthetic or generic prompts. "
        "No study questions, pilot, main experiment, or browser actions were run in this continuation.",
        "",
        f"**Adaption reported {money(known_cost, 6)} in usage cost** across {len(billed_rows)} accounted "
        f"responses. The long-context meter portion totaled {money(meter_cost, 6)}. "
        f"The price calculation matched the provider cost on {cost_checks}/{len(billed_rows)} accounted "
        "responses within a billionth of a credit. The earlier unresolved attempt retains "
        f"{money(reserved, 6)} credits as an additional upper reservation. "
        "Account credit coverage awaits the user's dashboard comparison. The prior balance was 2,750.",
        "",
        "## Gemma diagnostic and fix",
        "",
        "The saved non-study response was a completed object with one `message` item. "
        "Its opaque response ID was a 545-character padded string containing `=`. "
        "The old validator reused the local task-ID pattern, which capped length at 96 and excluded "
        "`=`, causing `response_id_unverified`. The new response-ID validator accepts the returned "
        "opaque format and screens literal and decoded candidates for credentials. The saved response "
        "was reconciled locally without another request.",
        "",
        "Top-level keys: `id`, `created_at`, `error`, `incomplete_details`, `instructions`, "
        "`metadata`, `model`, `object`, `output`, `parallel_tool_calls`, `temperature`, "
        "`tool_choice`, `tools`, `top_p`, `max_output_tokens`, `previous_response_id`, "
        "`reasoning`, `status`, `text`, `truncation`, `usage`, `user`, `store`, "
        "`background`, `max_tool_calls`, `prompt`, `service_tier`, `top_logprobs`, "
        "`presence_penalty`, `frequency_penalty`, `kv_transfer_params`, `ec_transfer_params`, "
        "`input_messages`, `output_messages`, `output_text`. Usage contained integer input, "
        "output and total token counts, input details including cached tokens, output details "
        "including reasoning tokens, and a numeric `cost` field.",
        "",
        "## Per-call usage",
        "",
        "The response-ID fingerprints below match the complete provider IDs in the [private per-call "
        f"summary](<{(ROOT / 'summary.json').as_posix()}>). The raw bodies are local in the ignored "
        "run folder. The report does not include response text or request headers. "
        "A rate-limited attempt returned no response ID or usage and is listed separately.",
        "",
        table(("Task", "Model", "Status", "Response ID SHA-256 prefix", "Input", "Cached", "Output",
               "Reasoning", "API cost"), entries),
        "",
        "## Controls observed",
        "",
        "- Temperature 0 and 0.7 were accepted and echoed. This does not establish sampling "
        "distribution or deterministic replay.",
        "- Qwen defaults used all 16 or 64 output tokens for reasoning and returned "
        "`incomplete` with `max_output_tokens`. The capability probe requested a cap of 1, "
        "which appeared as 16 in its response. Use a documented and calibrated output cap.",
        "- Both Qwen variants completed the matched baseline and follow-up with "
        "`reasoning.effort=none`, echoing that setting and returning zero reasoning tokens and "
        "a valid label each time. The same prompts at the default did not finish at 64. "
        "Gemma completed both prompts with zero reasoning tokens under its default.",
        "- The combined Qwen capability probe returned no seed and no populated top or message "
        "log probabilities. Those controls remain unverified for hosted study scoring. "
        "Do not use hosted A/B log probabilities or claim seed determinism.",
        "",
        "## Cost from measured study-shaped prompts",
        "",
        table(("Model", "Baseline input / output", "Branch input / output", "Pilot credits, 24 items",
               "Main credits, 85 items"), study_table),
        "",
        "Each item assumes two baseline calls and five follow-ups at one prespecified order, with "
        "all items eligible and no retries. The table uses one synthetic baseline and one synthetic "
        "follow-up per model as measurements, and published token rates. It is a planning estimate, "
        "not a bound for the real questions. The metering calls used deliberately long synthetic "
        "GLM prompts to create an account-visible debit and are excluded from the study forecast. "
        "Local calls cost no Adaption credits. [Pricing](https://docs.adaptionlabs.ai/inference-stacks/models).",
        "",
        "Keep the 600-credit project cap and the 6 / 60 / 400 / 134 smoke, pilot, main, and "
        "reserve allocations. Independently bound every batch with context and published rates, "
        "include unresolved reservations at full bound, and reconcile each returned usage record. "
        "The 3b requests ran one at a time.",
        "",
        "Propose all three hosted candidates plus two local candidates for the pilot. "
        "Account reconciliation records sponsor coverage separately. Use the approved 45% "
        "both-order and 30 projected eligibility gates plus "
        "the other prespecified gates. For the main, consider only passers and keep the earlier "
        "three-model maximum unless the user confirms five-model coverage in the Part 4 plan. "
        "Choose the focal model without using observed treatment effect. The primary remains the "
        "paired expertise contrast averaged across tones. Send identical saved histories to hosted "
        "branches and check exact labels with the same parser. Local grammar constrains labels, "
        "whereas the hosted output format is only prompted. Keep that distinction in cross-model comparisons. "
        "A predeclared temperature-above-zero check can resample five times on a balanced focal-model "
        "subset and average draws within question. The separate genuine-correction arm has 24 "
        "preselected candidates. Keep both secondary to the core. "
        "Additional models require a scientific rationale and separate main-plan approval. "
        "A provisional title if hosted models enter the main is “Does Claimed Expertise Change "
        "False Switching? An Expertise × Tone Test Across Local and Hosted Language Models.”",
        "",
    ]
    OUTPUTS.mkdir(exist_ok=True)
    path = OUTPUTS / "Authority Swap - Part 3b Usage and Budget.md"
    path.write_text("\n".join(report), encoding="utf-8")
    return {"calls_with_cost": len(billed_rows), "api_cost": str(known_cost),
            "meter_cost": str(meter_cost), "unresolved_reserved_credits": str(reserved),
            "pilot_estimate": str(pilot_total), "main_estimate": str(main_total),
            "matching_rate_records": cost_checks}


def save_checkpoint(stats):
    cost = Decimal(stats["api_cost"])
    meter = Decimal(stats["meter_cost"])
    projected_pilot = Decimal(stats["pilot_estimate"])
    projected_main = Decimal(stats["main_estimate"])
    unmatched = Decimal(stats["unresolved_reserved_credits"])
    start_balance = Decimal(2750)
    text = f"""# Authority Swap Part 3b checkpoint

15 November 2026 IST. **Hosted smoke and calibration finished. Dashboard reconciliation pending.** Part 3a remains complete. Part 4, main, and submission remain held. No browser or study-bank actions were taken.

The three authenticated candidates responded. The Gemma replay exposed the validator bug: the provider returned a 545-character padded opaque ID containing `=` and the runner's local task-ID pattern allowed 96 characters and no padding. The parser now accepts and screens provider response IDs separately. The saved Gemma response was recovered without another request. Its diagnostic structure and every call's usage are in `outputs/Authority Swap - Part 3b Usage and Budget.md`. Full provider IDs are in the private `work/authority-swap/runs/adaption/summary.json`. Only credential-screened non-study response bodies are saved.

Adaption's API reported **{cost:.6f} credits** across {stats['calls_with_cost']} accounted responses, including **{meter:.6f}** for long-context metering. The earlier unresolved attempt adds an upper reservation of **{unmatched:.6f}**, not a confirmed debit. One request was rate-limited and returned no usage. Subsequent metering was paced at least 62 seconds apart and used one request at a time. From the prior 2,750 balance, the logged debit predicts about **{start_balance-cost:.2f}** before unrelated activity or the earlier unresolved attempt. The user will compare their dashboard. Do not record “credit coverage verified” before that evidence arrives.

Observed settings: temperature was echoed at 0 and 0.7; a requested output cap of one was returned as 16; Qwen default reasoning exhausted caps of 16 or 64. Both Qwen models with `reasoning.effort=none` completed the matched tests with zero reasoning tokens, and Gemma completed them with zero under its default. Seed and log probabilities were not returned by the capability probe. Do not rely on either for hosted scoring or claim deterministic hosted replay.

One synthetic baseline/follow-up pair per model projects **{projected_pilot:.6f} pilot credits** for all 24 items and **{projected_main:.6f} main credits** for 85 items across all three hosted models. Assumes two baselines and five follow-ups at one order per item, all eligible, and no retries. Keep the 600-credit cap with 6 / 60 / 400 / 134 for smoke, pilot, main and reserve. Preserve batch reservations and per-call accounting. No Part 4 or main requests were sent.

Pilot candidates are Gemma 4 31B, Qwen 3.8 27B, Qwen 3.5 397B, local Qwen2.5-1.5B and local SmolLM2-1.7B. For the main, use eligible passers under the approved model limit and choose the primary focal model without looking at an expertise effect. Use hosted API only for hosted calls. Draft protocol v3.4, dataset v1.3 and the approved 45% / 30-item eligibility amendment are retained. One prespecified temperature robustness subset and the disjoint correction arm are optional secondary analyses. A hosted main model would require the user to confirm a wider title before Part 7. Local-only fallback keeps the current “Small Local Models” title.

1. Wait for the dashboard balance and reconcile it with the logged credit total. Retain the earlier unresolved reservation unless account evidence resolves it.
2. Confirm the 12 human source checks and await “Proceed to Part 4.” Do not start study calls from this checkpoint.
3. Once authorized, freeze the model, prompt, gating and cost settings before any pilot outcome. Keep main and submission held.
"""
    checkpoint = "Authority Swap - Part 3b Checkpoint.md"
    for path in (OUTPUTS / checkpoint, PROJECT / "RESUME.md",
                 PROJECT / "checkpoints" / "part-3b-completed.md"):
        path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", action="store_true")
    options = parser.parse_args()
    statistics = build()
    if options.checkpoint:
        save_checkpoint(statistics)
    print(json.dumps(statistics, indent=2))
