"""Release exploratory queues in priority order while protecting the writing reserve."""

from datetime import datetime, timezone
from pathlib import Path
import subprocess
import sys
import time

from main_v37 import CUTOFF, ROOT, host, json_file, read_schedule, save_json, sha256_file


RUNNER = Path(__file__).with_name("main_v37.py")
SURFACES = ("hosted", "local")
LOCKS = (host.ROOT / "dispatch.lock", ROOT / "local.lock")
MEASURE = ROOT / "collection-summary.json"


def seconds_left():
    return (CUTOFF - datetime.now(timezone.utc)).total_seconds()


def summaries(arm, models):
    for model in models:
        path = ROOT / f"{model}-{arm}-summary.json"
        if path.exists():
            yield json_file(path)


def estimate(core, models, arm):
    by_route = dict.fromkeys(SURFACES, 0.0)
    for r in core:
        route = models[r["model"]]["route"]
        eligible = (r["logical_calls"] - 170)//6
        pending = 8*eligible if arm == "escalation" else 96
        # Double observed per-call time, include startup or ramp, retain shutdown buffer.
        per_call = r["elapsed_seconds"] / r["logical_calls"]
        by_route[route] += 2*per_call*pending + (20 if route == "hosted" else 45)
    return round(max(by_route.values()), 1)


def dispatch(arm):
    codes = {}
    active = {route: subprocess.Popen([sys.executable, str(RUNNER), arm, route])
              for route in SURFACES}
    try:
        for route, worker in active.items():
            codes[route] = worker.wait()
    finally:
        for worker in active.values():
            if worker.poll() is None:
                worker.wait()
    return codes


def main():
    cfg, _, _ = read_schedule()
    models = cfg["model_settings"]
    state = {"core": "waiting", "escalation": "pending", "correction": "pending",
             "runner_sha256": sha256_file(RUNNER), "updated_utc": host.utc()}
    save_json(MEASURE, state)
    while True:
        core = list(summaries("core", models))
        if len(core) == 5 and all(r["status"] == "complete" for r in core) and not any(p.exists() for p in LOCKS):
            break
        if seconds_left() <= 150 or list(ROOT.glob("*-core-stop-summary.json")):
            state.update(core="incomplete", escalation="omitted: core incomplete",
                         correction="omitted: core incomplete", updated_utc=host.utc())
            save_json(MEASURE, state)
            return
        time.sleep(5)
    state.update(core="complete", updated_utc=host.utc())
    state["escalation_estimate_s"] = estimate(core, models, "escalation")
    state["correction_estimate_s"] = estimate(core, models, "correction")
    if seconds_left() < 150 + state["escalation_estimate_s"] + state["correction_estimate_s"]:
        state["correction"] = "omitted: writing reserve, lower priority"
    if seconds_left() < 150 + state["escalation_estimate_s"]:
        state["escalation"] = "omitted: writing reserve"
    for arm in ("escalation", "correction"):
        if state[arm] != "pending":
            continue
        if seconds_left() < 150 + state[f"{arm}_estimate_s"]:
            state[arm] = "omitted: writing reserve"
            continue
        state.update({arm:"running", "updated_utc":host.utc()})
        save_json(MEASURE, state)
        print(f"{arm} | queues released", flush=True)
        codes = dispatch(arm)
        state[arm] = "complete" if all(code == 0 for code in codes.values()) else "partial"
        state[f"{arm}_return_codes"] = codes
        if state[arm] == "partial" and arm == "escalation":
            state["correction"] = "omitted: exploratory priority after interruption"
        state["updated_utc"] = host.utc()
        save_json(MEASURE, state)
    save_json(MEASURE, state)
    print(f"Collection | escalation {state['escalation']} | correction {state['correction']}", flush=True)


if __name__ == "__main__":
    main()
