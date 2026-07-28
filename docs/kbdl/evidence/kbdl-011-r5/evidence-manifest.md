# KBDL-011-R5 Evidence Manifest

R5 validates the effective traceability model formed by each readable group and its per-ID ledger row. The builder and validator use separate parsing implementations and do not import one another.

## Evidence

- `scripts/build_effective_ledger.py` — builds the reconciled per-ID companion ledger.
- `scripts/reconcile_group_statuses.py` — mechanically aligns readable validation summaries with authoritative per-ID statuses.
- `scripts/validate_effective_records.py` — independent authoritative/group/ledger parser and comparator.
- `scripts/capture_precommit.py` — command, stream, exit-code, and result capture.
- `artifacts/effective-record-audit.csv` — complete 317-row effective audit.
- `artifacts/group-ledger-conflicts.csv` — complete conflict inventory.
- `artifacts/exact-location-audit.csv` — section and anchor audit.
- `artifacts/authority-resolution.csv` — complete authority audit.
- `artifacts/evidence-limitation-audit.csv` — method, evidence, and limitation audit.
- `artifacts/packet-dependency-audit.csv` — exact packet and dependency audit.
- `artifacts/validation-output.txt` — computed final results.
- `precommit-transcript.txt` — required command evidence.
- `checksums.sha256` — byte sizes and full SHA-256 checksums.

Candidate readiness requires the effective-record validator, documentation validator, and Git whitespace check to pass. Implementation conformance remains `NOT VERIFIED`; project completion remains `PENDING PLANNING-AGENT VALIDATION AND PROJECT-OWNER APPROVAL`; accepted limitations: None.
