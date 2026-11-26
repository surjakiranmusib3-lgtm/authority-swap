"""Summarize pilot v3.6 from its aggregate result files only."""

import argparse
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
import json
import math
from pathlib import Path

from freeze_part4a import OUTPUT, table, sha
from freeze_v36 import FILE, CFG, MANIFEST
from pilot_v36 import ROOT, FOUR, DEADLINE


def load(path):
    return json.loads(path.read_bytes())


def result_word(yes):
    return "pass" if yes else "FAIL"


def ratio(n, d):
    return f"{n}/{d} ({n/d:.1%})" if d else f"{n}/{d} (not evaluable)"


def number(value, places=4):
    return f"{value:.{places}f}" if value is not None else "not estimable"


def wilson(success, n=16):
    z = 1.95996398454
    rate = success / n
    scale = 1 + z*z/n
    center = (rate + z*z/(2*n))/scale
    width = z*math.sqrt(rate*(1-rate)/n + z*z/(4*n*n))/scale
    return f"{max(0, center-width):.1%}–{min(1, center+width):.1%}"


def select(acceptance, config, seconds):
    def rank(row):
        return (-row["eligible"], row["projected_main_credits_no_retries"], row["model"])

    def fallback(row):
        return (-row["eligible"], -row["parsed"]/row["logical_calls"],
                row["projected_main_credits_no_retries"], row["model"])

    def failure(row):
        return {gate for gate, passed in row["gates"].items() if not passed}

    def route(row):
        return config["model_settings"][row["model"]]["route"]

    ranked = sorted(acceptance, key=rank)
    passes = [r for r in ranked if not failure(r)]
    floor_ceiling = [r for r in ranked if failure(r) and failure(r) <= {"floor", "ceiling"}]
    selected = []

    def push(row, kind):
        choices = [row] + [r for r, _ in selected]
        cost = sum(r["projected_main_credits_no_retries"] for r in choices) * 2
        max_host_batch = max((float(config["model_settings"][r["model"]].get("request_reserve", 0))
                              for r in choices), default=0) * 16
        runtime = sum(r["projected_main_seconds_with_retry_allowance"] for r in choices)
        if len(selected) < 3 and all(row is not r for r, _ in selected) and (
                cost + max_host_batch <= 400 and runtime < seconds):
            selected.append((row, kind))
            return True
        return False

    focal = passes[0] if passes else None
    if focal:
        push(focal, "FOCAL")
        for row in passes[1:]:
            if route(row) != route(focal) and push(row, "PASS"):
                break
        for row in passes[1:]:
            push(row, "PASS")
        for row in floor_ceiling:
            push(row, "DESCRIPTIVE-ONLY")
    else:
        ranked = sorted(acceptance, key=fallback)
        for row in ranked:
            if row["gates"]["integrity"] and row["gates"]["feasibility"]:
                push(row, "DESCRIPTIVE-ONLY")
    return ranked, passes, focal, selected


def build(after=None):
    run = load(ROOT / "run-summary.json")
    config = load(CFG)
    assert run["status"] == "complete" and run["config_sha256"] == sha(CFG)
    a = list(run["acceptance"].values())
    dev = list(run["development"].values())
    assert len(a) == len(dev) == 5 and all(r["items"] == 16 for r in a)
    assert all(r["items"] == 8 for r in dev)
    assert all(r["logical_calls"] == 32 + 6*r["eligible"] for r in a)
    assert all(r["core_scheduled"] == 32 + 5*r["eligible"] for r in a)
    assert all(r["complete"] <= r["eligible"] and r["bare_usable"] <= r["eligible"] for r in a)
    ranked, passes, focal, selected = select(a, config, (DEADLINE-datetime.now(timezone.utc)).total_seconds())
    paid = sum(r["credits_known"] for r in dev + a)
    hosted_acceptance = sum(r["credits_known"] for r in a)
    pilot_calls = sum(r["logical_calls"] for r in dev+a)
    before = "2,747 credits before the pilot, matching 2,750 minus the logged 2.999828 Part 3b credits at the dashboard's display precision. Credit coverage verified and the old 3b-1 reservation released."
    if after is None:
        after_line = "The post-pilot display has not been recorded. Use the detailed ledger for fractional pilot usage."
    else:
        drop = Decimal(2747) - after
        disagreement = abs(drop - Decimal(str(paid)))
        after_line = (f"The post-pilot display showed {after:,} credits. The displayed debit was "
                      f"{drop:.3f}, a difference of {disagreement:.6f} from the logged pilot cost. "
                      + ("This reconciles within one 0.001-credit display increment."
                         if disagreement <= Decimal(".001") else
                         "The display and logged cost differ by more than one 0.001-credit increment."))
    details = [
        "# Authority Swap v3.6 Part 4b pilot",
        "",
        "All five candidates completed the eight development items before any of the 16 acceptance items. "
        "Development checked transport, parsing and saved-history assembly only. Gate and ranking calculations use acceptance.",
        "",
        f"The pilot scheduled {pilot_calls} logical study requests. Hosted usage was **{paid:.9f} credits** "
        f"including development, of which {hosted_acceptance:.9f} was acceptance. "
        f"The highest reserved pilot-stage total observed at batch admission was "
        f"{run['max_pilot_reserved_credits']:.6f} credits against the 60-credit cap. {before} {after_line}",
        "",
        "## Development checks",
        "",
        table(("Candidate", "Items", "Baseline parsed", "All parsed", "Replay integrity", "Seconds", "Credits"),
              [(r["model"], r["items"], ratio(r["baseline_parsed"], 16),
                ratio(r["parsed"], r["logical_calls"]), result_word(r["history_integrity"]),
                number(r["runtime_seconds"], 2), number(r["credits_known"], 9)) for r in dev]),
        "",
        "## Acceptance gates",
        "",
        table(("Candidate", "Eligible", "Projected eligible", "Parsed", "Core complete", "Integrity",
               "Floor", "Ceiling", "Feasibility", "Gate failures"), [
            (r["model"], f"{ratio(r['eligible'], 16)} {result_word(r['gates']['eligibility'])}",
             f"{number(r['projection'], 2)} {result_word(r['gates']['projection'])}",
             f"{ratio(r['parsed'], r['logical_calls'])} {result_word(r['gates']['parse'])}",
             f"{ratio(r['complete'], r['eligible'])} {result_word(r['gates']['completeness'])}",
             result_word(r["gates"]["integrity"]),
             f"{r['floor_distinct_switchers']} distinct switchers; {result_word(r['gates']['floor'])}",
             f"{'/'.join(str(r['core_wrong_counts'][b]) for b in FOUR)} of {r['complete']}; "
             f"{result_word(r['gates']['ceiling'])}",
             result_word(r["gates"]["feasibility"]),
             ", ".join(g for g, passed in r["gates"].items() if not passed) or "none")
            for r in a]),
        "",
        "Ceiling numerators are expert assertive, expert tentative, ordinary assertive, ordinary tentative. "
        "The denominator is items complete across the original five branches. A zero denominator cannot pass. "
        "Parse counts include bare. The next table separately reports bare usability over the eligible set and "
        "false switching over its own usable responses. Variance is the sample variance of the complete "
        "question-level paired expert-minus-ordinary differences.",
        "",
        table(("Candidate", "Eligible easy/medium/hard", "Eligibility Wilson 95%", "Projected complete",
               "Core parsed", "Bare usable", "Bare wrong",
               "Bare abstain", "Neutral wrong", "Paired variance", "Complete N"),
              [(r["model"], "/".join(map(str, r["eligible_by_tier"])),
                wilson(r["eligible"]), number(r["projected_complete"], 2),
                ratio(r["core_parsed"], r["core_scheduled"]), ratio(r["bare_usable"], r["eligible"]),
                ratio(r["bare_wrong"], r["bare_usable"]), r["bare_abstain"],
                ratio(r["core_wrong_counts"]["neutral"], r["complete"]),
                number(r["pilot_pair_sample_variance"], 6), r["complete"]) for r in a]),
        "",
        "## Throughput and feasibility",
        "",
        "Acceptance throughput includes observed pacing and any wait within requests. Projections assume "
        "all 85 baseline pairs, six follow-ups on projected eligible items, and duplicate the measured "
        "request time for the one-retry allowance. Each planned hosted batch remains subject to the full "
        "reservation rule. The projected credits column is the no-retry planning estimate.",
        "",
        table(("Candidate", "Acceptance logical requests", "Attempts", "Requests/min", "Median seconds",
               "Measured credits", "Projected main credits", "Projected main minutes with retry allowance"),
              [(r["model"], r["logical_calls"], r["attempts"], number(r["requests_per_minute"], 2),
                number(r["median_request_seconds"], 3), number(r["credits_known"], 9),
                number(r["projected_main_credits_no_retries"], 9),
                number(r["projected_main_seconds_with_retry_allowance"]/60, 2)) for r in a]),
        "",
        "## Focal ranking and Part 5 recommendation",
        "",
        table((("Eligibility/cost order" if passes else "Eligibility/parse fallback order"),
               "Candidate", "Eligible", "Parse rate", "Class"),
              [(i, r["model"], f"{r['eligible']}/16", ratio(r["parsed"], r["logical_calls"]),
                "passed all gates" if r in passes else
                "descriptive-only eligible" if {g for g,p in r["gates"].items() if not p} <= {"floor", "ceiling"}
                else "failed other gates")
               for i, r in enumerate(ranked, 1)]),
        "",
        ("Focal model: **" + focal["model"] + "**." if focal else
         "**No focal model.** No candidate passed all gates. The fallback ranks feasibility- and "
         "integrity-compatible candidates by eligibility, parsing, cost, then ID. Any main results are descriptive."),
        "",
        "Recommended main configurations, pending explicit Part 5 authorization: "
        + (", ".join(f"{r['model']} ({kind})" for r, kind in selected) or "none within hard limits") + ".",
        "",
        "The current pilot gates use a small curated bank. A model selected on eligibility may have benefited "
        "from sampling variability. The paired variance is conditional on eligible complete items and "
        "is planning evidence with substantial uncertainty. Model populations can differ in the main. "
        "No main, optional reasoning or submission action ran. No human spot-check was performed.",
        "",
    ]
    report = OUTPUT / "Authority Swap - Part 4b Results.md"
    report.write_text("\n".join(details), encoding="utf-8")
    checkpoint = OUTPUT / "Authority Swap - Part 4b Checkpoint.md"
    content = f"""# Authority Swap Part 4b checkpoint

15 November 2026 IST. **Part 4b complete. Main and submission held.** No optional reasoning or main study requests were sent.

Protocol v3.6 SHA-256 `{sha(FILE)}`. Schedule SHA-256 `{sha(CFG)}`. The manifest is `outputs/{MANIFEST.name}`. Protocol v3.5 remains in history. Dataset v1.3 did not change.

Local non-study validation parsed 16 synthetic replies. All development and acceptance items were processed in the required order. The pilot scheduled {pilot_calls} logical study calls and used {paid:.9f} logged Adaption credits. {before} {after_line}

Five-model acceptance gates, throughput, bare-arm denominators and paired sample variances are in `outputs/{report.name}`. The output-free run summary is `work/authority-swap/runs/part4b-v3.6/run-summary.json`. Hosted per-attempt accounting is in the private ledger. The runner kept the 60-credit pilot stage cap and the 600-credit project cap.

Focal model: **{focal["model"] if focal else "none"}**. Passed all gates: {", ".join(r["model"] for r in passes) or "none"}. Part 5 plan: {", ".join(f"{r['model']} ({kind})" for r, kind in selected) or "no candidates within hard limits"}.

User human spot-check: not performed. The Claude pass is a key agreement exercise from background knowledge, not a source check. Preserve AI-only limitations and the status of the separate Claude artifact before the paper.

1. Wait for **“Proceed to Part 5.”**
2. On authorization, freeze the main model list, execution plan and statistical precision statement from the pilot. Label descriptive-only models and keep their results separate from the confirmatory focal contrast.
3. Keep the optional reasoning arm and submission held. Update the title with the user before Part 7 if hosted models are used in the main.
"""
    for path in (checkpoint, ROOT.parent.parent / "RESUME.md",
                 ROOT.parent.parent / "checkpoints" / "part-4b-completed.md"):
        path.write_text(content, encoding="utf-8")
    print(json.dumps({"passed_all": [r["model"] for r in passes],
          "focal": focal["model"] if focal else None,
          "main_plan": [(r["model"], kind) for r, kind in selected],
          "credits": paid, "logical_study_calls": pilot_calls,
          "variance": focal["pilot_pair_sample_variance"] if focal else None}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dashboard-after", type=Decimal)
    args = parser.parse_args()
    build(args.dashboard_after)
