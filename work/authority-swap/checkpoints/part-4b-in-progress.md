# Authority Swap Part 4b in progress

15 November 2026 IST. v3.6 was frozen before study outcomes. The binding hash list is `outputs/Authority Swap - Protocol v3.6 SHA-256.txt`. v3.5 was retained. The Claude background-knowledge result is documented as supplied by the user, with the promised CSV still pending.

Offline validation passed on both local models with 16 dummy calls and zero hosted calls. Replay, strict parsing, and the 22-word bare template were checked. See `work/authority-swap/runs/part4b-v3.6/validation-summary.json`.

Chrome displayed 2,747 credits. The 3-credit drop matched the 2.999828-credit Part 3b log, and the old 3b-1 reservation was released. The private ledger preserves the unknown original charge.

Part 4b is running in the authorized background session 28811. Runner source SHA-256 `acc726e958be302cc2cad322d6e9a62959f40096d884909fdb2703a3dc90c2bf`. It finishes all five development blocks before opening acceptance, checks each hosted reservation, and saves summaries in `work/authority-swap/runs/part4b-v3.6/`. There is one hosted dispatch at a time. Do not launch a second process while this one is active. Check `pilot_dev-summary.json`, `pilot_accept-summary.json`, `stop-summary.json`, or `run-summary.json` only.

Next actions: monitor to completion, read only aggregate summaries, produce each gate and ranking, and reconcile the post-pilot display. Then save the completed checkpoint and stop. Main, optional reasoning and submission remain held. The user must explicitly say “Proceed to Part 5.”
