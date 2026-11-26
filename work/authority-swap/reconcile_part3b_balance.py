"""Reconcile a user-supplied dashboard balance and release only reservation 3b-1."""

from contextlib import closing
from decimal import Decimal, ROUND_HALF_UP
import json
import sys

from hosted_runner import ROOT, open_ledger, update_summary, utc


BASELINE = Decimal("2750")
MATCH_TOLERANCE = Decimal("1")


def reconcile(balance, source="user-reported dashboard"):
    if not balance.is_finite() or balance < 0:
        raise ValueError("Expected a nonnegative dashboard balance.")
    path = ROOT / "part3b-dashboard-reconciliation.json"
    if path.exists():
        prior = json.loads(path.read_text(encoding="utf-8"))
        if Decimal(prior["displayed_balance"]) == balance:
            return prior
        if prior["released_3b_1_reservation"]:
            raise ValueError("A dashboard reconciliation already released this reservation.")
    lock = ROOT / "dispatch.lock"
    with lock.open("x", encoding="utf-8") as owner:
        owner.write("Offline dashboard reconciliation\n")
    try:
        with closing(open_ledger()) as db:
            db.execute("BEGIN IMMEDIATE")
            rows = db.execute("SELECT * FROM calls WHERE stage='smoke'").fetchall()
            logged = sum((Decimal(row["provider_cost"]) for row in rows
                          if row["provider_cost"] is not None), Decimal("0"))
            if len(rows) != 24 or logged.quantize(Decimal(".000001")) != Decimal("2.999828"):
                raise ValueError("Part 3b ledger differs from the frozen reconciliation record.")
            quant = Decimal(1).scaleb(balance.as_tuple().exponent)
            expected = (BASELINE - logged).quantize(quant, rounding=ROUND_HALF_UP)
            delta = BASELINE - balance
            match = abs(balance - expected) <= MATCH_TOLERANCE
            released = False
            if match:
                result = db.execute("""UPDATE calls SET status='reservation_released',
                    uncached_microcredits=0, detail='dashboard_reconciled_charge_unknown'
                    WHERE stage='smoke' AND task_id='3b-1' AND reserved_microcredits=87040
                    AND status='reserved' AND provider_cost IS NULL""")
                if result.rowcount != 1:
                    recovered = db.execute("""SELECT 1 FROM calls WHERE stage='smoke' AND task_id='3b-1'
                        AND status='reservation_released' AND detail='dashboard_reconciled_charge_unknown'
                        AND uncached_microcredits=0 AND provider_cost IS NULL""").fetchone()
                    if recovered is None:
                        raise ValueError("Expected the unresolved 3b-1 reservation.")
                released = True
            db.commit()
            update_summary(db)
        record = {
            "recorded_utc": utc(), "balance_source": source,
            "displayed_balance": str(balance), "previous_balance": str(BASELINE),
            "observed_drop": str(delta), "logged_cost": str(logged),
            "expected_at_display_precision": str(expected),
            "tolerance_credits": str(MATCH_TOLERANCE),
            "coverage_status": "credit coverage verified" if match else "credit coverage not reconciled",
            "released_3b_1_reservation": released,
            "original_3b_1_charge": "unknown",
        }
        path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        return record
    finally:
        lock.unlink()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: reconcile_part3b_balance.py <displayed dashboard balance>")
    print(json.dumps(reconcile(Decimal(sys.argv[1].replace(",", ""))), indent=2))
