#!/usr/bin/env python3
"""Capture reproducible R10 pre-commit commands and package hashes."""
from pathlib import Path
import csv
import hashlib
import subprocess

ROOT = Path(__file__).resolve().parents[5]
PKG = ROOT / "docs/kbdl/evidence/kbdl-011-r10"

commands = [
    ["python3", "docs/kbdl/evidence/kbdl-011-r5/scripts/build_effective_ledger.py"],
    ["python3", "docs/kbdl/evidence/kbdl-011-r6/scripts/resolve_per_id_ledger.py"],
    ["python3", "docs/kbdl/evidence/kbdl-011-r8/scripts/reconcile_evidence.py"],
    ["python3", "docs/kbdl/evidence/kbdl-011-r9/scripts/documentation_validator.py", "--root", str(ROOT)],
    ["python3", "docs/kbdl/evidence/kbdl-011-r10/scripts/semantic_audit.py"],
    ["git", "diff", "--check"],
    ["git", "status", "--short"],
]

records = []
for command in commands:
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    records.extend([
        "$ " + " ".join(command),
        "STDOUT:", result.stdout.rstrip() or "(empty)",
        "STDERR:", result.stderr.rstrip() or "(empty)",
        f"EXIT: {result.returncode}",
    ])
    if command[-1].endswith("semantic_audit.py"):
        records.append("EXPECTED: exit 2 because required authority/evidence is unresolved")
    records.append("")

(PKG / "precommit-transcript.txt").write_text("\n".join(records), encoding="utf-8")

excluded = {"checksums.sha256", "evidence-inventory.csv"}
files = sorted(p for p in PKG.rglob("*") if p.is_file() and p.name not in excluded)
with (PKG / "evidence-inventory.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle, lineterminator="\n")
    writer.writerow(["Path", "Bytes", "SHA-256"])
    for path in files:
        data = path.read_bytes()
        writer.writerow([path.relative_to(ROOT), len(data), hashlib.sha256(data).hexdigest()])

checksum_files = sorted(p for p in PKG.rglob("*") if p.is_file() and p.name != "checksums.sha256")
lines = []
for path in checksum_files:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    lines.append(f"{digest}  {path.relative_to(ROOT)}")
(PKG / "checksums.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")

print(f"Captured {len(commands)} commands; inventoried {len(files)} files; checksummed {len(checksum_files)} files")
