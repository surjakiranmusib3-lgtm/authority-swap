# Authority Swap Parts 5 and 6 in progress

Main authorized for five candidates, all descriptive-only, with no focal model. Protocol v3.7 froze at 2026-11-15 19:27:15 IST before the first main request. The protocol and schedule hashes are in `outputs/Authority Swap - Protocol v3.7 SHA-256.txt`. The v3.6 pilot and dataset v1.3 remain the inputs. Protocol changes are explicitly post-pilot.

Core ran first. Hosted background session 43718 and local session 95439 were launched with `work/authority-swap/main_v37.py`. The executable core runner SHA-256 at launch was `f0ea4e062988dcd043737c5fb78c2d45501ae059053bb7a3930ae42652e4a5a0`. All five core runs completed with 2,578 logical requests by 20:25 IST Sunday. Both queues exited successfully. A separate program validated the local stored prompt and history hashes. Read per-model progress summaries in `work/authority-swap/runs/main-v3.7` and only the totals of the private hosted ledger summary. Keep the 400-credit main and 600-credit project limits.

1. Background session 14543 runs `collect_v37_extensions.py`. Escalation was released at about 20:24 IST Sunday. Correction remains queued. Check `collection-summary.json`, endpoint drain, and the 11:29 IST Monday data cutoff. Do not start duplicate workers.
2. After escalation and correction exit, record observed cost and throughput for all three arms. Mark any stopped or omitted data as partial.
3. Background session 22472 runs `analyze_v37.py --wait`. It writes the Part 6 tables, results, and hash manifest after the collection controller reports a terminal state. Validate the published aggregates and then save the completed checkpoint. If the analysis process exits before writing a report, use the error and the collection summary to recover without sending inference requests.

Submission held. Optional reasoning and paper drafting are outside this part.
