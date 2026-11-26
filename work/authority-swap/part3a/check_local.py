"""Run Part 3a dummy and decoder checks on the pinned CPU build."""

import csv
import json
from pathlib import Path
import socket
import statistics
import subprocess
import sys
import time
import urllib.error

from runner import (
    DECODING, LocalServer, TEMPLATES, chatml, message, save_json, sha256,
    sha256_file,
)

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
SERVER = PROJECT.parent / "llama" / "llama-server.exe"
BUILD = "12243-8766c0273"
SERVER_SHA = "6f363d75fbac112e049662c4ff653d8beb9af5bdcaefec5695c1fe8e9af0319a"
THREADS = 8


def json_post(server, route, payload):
    return json.loads(server.post(route, payload))


def decoder_checks(server, model, output):
    token_ids = {}
    for label in ("A", "B", "ABSTAIN"):
        token_ids[label] = json_post(server, "/tokenize", {
            "content": label, "add_special": False, "parse_special": False,
        })["tokens"]
    assert all(len(token_ids[label]) == 1 for label in ("A", "B")), token_ids
    assert token_ids["A"] != token_ids["B"], token_ids
    probes = []
    for requested in ("A", "B", "ABSTAIN", "NOT_ALLOWED"):
        messages = [
            message("system", "Repeat the requested label exactly, without surrounding text."),
            message("user", f"Print exactly this label: {requested}"),
        ]
        request, raw, elapsed = server.completion(chatml(messages, generation=True))
        save_json(output / f"decoder-{requested}.json", {
            "requested": requested, "request": request, "raw_http_body": raw,
            "wall_seconds": elapsed,
        })
        body = json.loads(raw)
        probabilities = body.get("completion_probabilities") or []
        top = probabilities[0].get("top_logprobs", []) if probabilities else []
        by_id = {entry["id"]: entry["logprob"] for entry in top}
        probes.append({
            "requested": requested, "output": body["content"], "tokens": body.get("tokens"),
            "first_token_logprobs": {
                label: by_id.get(token_ids[label][0]) for label in ("A", "B")
            },
        })
    for label in ("A", "B", "ABSTAIN"):
        assert next(p["output"] for p in probes if p["requested"] == label) == label, probes
    assert probes[-1]["output"] in {"A", "B", "ABSTAIN"}, probes
    template_checks = []
    for messages in (
        [message("system", "Answer briefly."), message("user", "A or B?")],
        [message("system", "Answer briefly."), message("user", "A or B?"),
         message("assistant", "A"), message("user", "Please reconsider.")],
    ):
        ours = chatml(messages, generation=True)
        theirs = json_post(server, "/apply-template", {"messages": messages})["prompt"]
        template_checks.append({"matches": ours == theirs, "runner": ours, "server": theirs})
    save_json(output / "template-checks.json", template_checks)
    return {"model": model, "tokens": token_ids, "probes": probes,
            "server_template_matches": all(check["matches"] for check in template_checks)}


def audit_dummy(output, tokens):
    records = [json.loads(p.read_text(encoding="utf-8")) for p in (output / "raw").glob("*.json")]
    assert len(records) == len({r["request_id"] for r in records}) == 36
    assert {r["item_id"] for r in records} == {"dummy-01", "dummy-02", "dummy-03"}
    parents = {r["request_id"]: r for r in records if r["branch"] == "baseline"}
    assert len(parents) == 6
    for parent_id, parent in parents.items():
        children = [r for r in records if r["baseline_request_id"] == parent_id]
        assert len(children) == len({r["branch"] for r in children}) == 5
        baseline_output = json.loads(parent["raw_http_body"])["content"]
        expected = parent["messages"] + [message("assistant", baseline_output)]
        expected_history = chatml(expected, generation=False)
        expected_hash = sha256(expected_history.encode("utf-8"))
        assert all(r["messages"][:-1] == expected and
                   r["history_sha256"] == expected_hash and
                   r["rendered_prompt"].startswith(expected_history) for r in children)
    with (output / "scores.csv").open(encoding="utf-8", newline="") as stream:
        assert {r["request_id"] for r in csv.DictReader(stream)} == {r["request_id"] for r in records}
    per_call_timings = []
    both_logprobs = 0
    for record in records:
        raw = json.loads(record["raw_http_body"])
        assert raw["content"] in {"A", "B", "ABSTAIN"} and not raw.get("truncated")
        probs = raw.get("completion_probabilities") or []
        top = probs[0].get("top_logprobs", []) if probs else []
        first_ids = {candidate["id"] for candidate in top}
        both_logprobs += all(tokens[key][0] in first_ids for key in ("A", "B"))
        per_call_timings.append(raw["timings"])
    return {
        "completions": len(records), "identical_history_groups": len(parents),
        "A_and_B_present_in_first_token_top_32": both_logprobs,
        "median_prompt_tokens_per_second": statistics.median(t["prompt_per_second"] for t in per_call_timings),
        "median_generation_tokens_per_second": statistics.median(t["predicted_per_second"] for t in per_call_timings),
        "median_completion_wall_seconds": statistics.median(r["wall_seconds"] for r in records),
        "total_completion_wall_seconds": sum(r["wall_seconds"] for r in records),
    }


def run_model(model, spec):
    output = PROJECT / "runs" / f"part3a-{model}-dummy"
    output.mkdir(parents=True, exist_ok=True)
    artifact = PROJECT / "models" / spec["file"]
    digest = sha256_file(artifact)
    if digest != spec["publisher_sha256"]:
        raise RuntimeError(f"{artifact.name} fails its publisher checksum")
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        port = listener.getsockname()[1]
    command = [
        str(SERVER), "-m", str(artifact), "--host", "127.0.0.1", "--port", str(port),
        "-c", "2048", "-t", str(THREADS), "-tb", str(THREADS), "-ngl", "0", "-np", "1",
        "--no-webui", "--jinja",
    ]
    server = LocalServer(port, 90)
    print(f"Starting {spec['name']} with {THREADS} CPU threads", flush=True)
    log = output / "llama-server.log"
    with log.open("ab") as logfile:
        process = subprocess.Popen(command, stdout=logfile, stderr=subprocess.STDOUT,
                                   creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        try:
            started = time.monotonic()
            while True:
                if process.poll() is not None:
                    raise RuntimeError(f"llama.cpp exited at startup. See {log}")
                if time.monotonic() - started > 90:
                    raise RuntimeError(f"llama.cpp did not become ready. See {log}")
                try:
                    if LocalServer(port, 2).get("/health").get("status") == "ok":
                        break
                except (urllib.error.URLError, TimeoutError):
                    time.sleep(0.35)
            props = server.get("/props")
            save_json(output / "server-props.json", props)
            model_args = [
                sys.executable, str(HERE / "runner.py"), "--model", model,
                "--model-sha256", digest, "--llama-build", BUILD, "--port", str(port),
                "--output", str(output),
            ]
            passes = []
            for extra in (["--limit", "7"], [], []):
                run = subprocess.run(model_args + extra, capture_output=True, text=True, check=False)
                if run.returncode:
                    raise RuntimeError(f"Runner exit {run.returncode}: {run.stderr} {run.stdout}")
                passes.append(json.loads(run.stdout))
            assert passes[-1]["new_completions"] == 0 and passes[-1]["reused_completions"] == 36, passes
            if passes[0]["new_completions"]:
                assert [p["new_completions"] for p in passes] == [7, 29, 0], passes
                assert [p["reused_completions"] for p in passes] == [0, 7, 36], passes
            check = decoder_checks(server, model, output)
            check.update(audit_dummy(output, check["tokens"]))
            check.update(model_file=artifact.name, bytes=artifact.stat().st_size, sha256=digest,
                         server_sha256=SERVER_SHA, server_version=BUILD, command=command,
                         decoder_settings=DECODING, benchmark_passes=passes, decoder_probe_calls=4,
                         port=port, cpu_threads=THREADS, gpu_layers=0)
            save_json(output / "local-check-summary.json", check)
            print(json.dumps(check), flush=True)
        finally:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=10)


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in {*TEMPLATES, "both"}:
        raise SystemExit("Usage: check_local.py qwen|smol|both")
    if sha256_file(SERVER) != SERVER_SHA:
        raise SystemExit("llama-server.exe fails the saved checksum")
    sources = json.loads((HERE / "model-sources.json").read_text(encoding="utf-8"))
    names = list(sources) if sys.argv[1] == "both" else [sys.argv[1]]
    for name in names:
        run_model(name, sources[name])
