"""Assemble Part 2a candidates without exposing draft keys to blind reviewers."""

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCES = [
    HERE / "p2a_space_standards.jsonl",
    HERE / "p2a_earth_ocean.jsonl",
    HERE / "p2a_culture_bio.jsonl",
]
QUESTION_FILE = ROOT / "outputs" / "Authority Swap - Part 2a Draft Questions.csv"
KEY_FILE = HERE / "draft-keys-v1.csv"
QUESTION_FIELDS = [
    "id", "bank", "tier", "domain_group", "domain", "stem", "option_a", "option_b",
    "source_url", "source_locator", "draft_status",
]
KEY_FIELDS = ["id", "draft_key", "draft_rationale"]
REQUIRED = set(QUESTION_FIELDS[:-1] + KEY_FIELDS[1:]) - {"domain_group"}
BANK_ORDER = {"main": 0, "pilot_dev": 1, "pilot_accept": 2, "correction": 3}
TIER_ORDER = {"easy": 0, "medium": 1, "hard": 2}
DOMAIN_GROUPS = {
    "astronomy": "astronomy",
    "measurement": "physical standards",
    "chemistry": "physical standards",
    "volcanology": "earth science",
    "seismology": "earth science",
    "geology": "earth science",
    "park_geology": "earth science",
    "park_geography": "earth science",
    "limnology": "earth science",
    "hydrology": "earth science",
    "oceanography": "ocean science",
    "ocean_acoustics": "ocean science",
    "coastal_ecology": "life science",
    "genomics": "life science",
    "zoology": "life science",
    "park_history": "history and culture",
    "monument_history": "history and culture",
    "printing_history": "history and culture",
    "invention_history": "history and culture",
    "monument_design": "history and culture",
    "exploration_history": "history and culture",
}


def normalized(text):
    return re.sub(r"[^a-z0-9]+", " ", text.casefold()).strip()


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


rows = []
for source in SOURCES:
    if not source.exists():
        raise SystemExit(f"Missing draft fragment: {source}")
    for line_no, raw in enumerate(source.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{source.name}:{line_no}: {exc}") from exc
        missing = [field for field in REQUIRED if not str(row.get(field, "")).strip()]
        if missing:
            raise SystemExit(f"{source.name}:{line_no}: missing {missing}")
        if row["bank"] not in BANK_ORDER or row["tier"] not in TIER_ORDER:
            raise SystemExit(f"{row['id']}: invalid bank or tier")
        if row["draft_key"] not in ("A", "B"):
            raise SystemExit(f"{row['id']}: invalid draft key")
        if normalized(row["option_a"]) == normalized(row["option_b"]):
            raise SystemExit(f"{row['id']}: options identical")
        url = urlparse(row["source_url"])
        if url.scheme != "https" or not url.netloc:
            raise SystemExit(f"{row['id']}: source URL not HTTPS")
        if row["domain"] not in DOMAIN_GROUPS:
            raise SystemExit(f"{row['id']}: unmapped domain {row['domain']}")
        row["domain_group"] = DOMAIN_GROUPS[row["domain"]]
        row["draft_status"] = "UNVERIFIED_DRAFT"
        rows.append(row)

ids = [row["id"] for row in rows]
if len(ids) != len(set(ids)):
    raise SystemExit("Duplicate IDs")
stems = [normalized(row["stem"]) for row in rows]
if len(stems) != len(set(stems)):
    duplicated = [stem for stem, count in Counter(stems).items() if count > 1]
    raise SystemExit(f"Duplicate stems: {duplicated[:5]}")
if any("origin o" in stem for stem in stems):
    raise SystemExit("Possible overlap with the prior synthetic source-origin project")

counts = Counter(row["bank"] for row in rows)
main_tiers = Counter(row["tier"] for row in rows if row["bank"] == "main")
expected_banks = {"main": 90, "pilot_dev": 8, "pilot_accept": 16, "correction": 24}
expected_tiers = {"easy": 30, "medium": 30, "hard": 30}
if counts != expected_banks or main_tiers != expected_tiers:
    raise SystemExit(f"Wrong allocation: banks={dict(counts)}, main tiers={dict(main_tiers)}")

rows.sort(key=lambda row: (BANK_ORDER[row["bank"]], TIER_ORDER[row["tier"]], row["id"]))
QUESTION_FILE.parent.mkdir(parents=True, exist_ok=True)
with QUESTION_FILE.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=QUESTION_FIELDS, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
with KEY_FILE.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=KEY_FIELDS, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)

domains = Counter(row["domain"] for row in rows)
domain_groups = Counter(row["domain_group"] for row in rows)
hosts = Counter(urlparse(row["source_url"]).netloc.lower() for row in rows)
key_balance = Counter(row["draft_key"] for row in rows)
print(f"items={len(rows)} banks={dict(counts)} main_tiers={dict(main_tiers)}")
print(f"domains={dict(domains)}")
print(f"domain_groups={dict(domain_groups)}")
print(f"source_hosts={dict(hosts)}")
print(f"draft_keys={dict(key_balance)}")
print(f"questions_sha256={sha256(QUESTION_FILE)}")
print(f"keys_sha256={sha256(KEY_FILE)}")
