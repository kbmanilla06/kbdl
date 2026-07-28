# KBDL-011-R8 Evidence Manifest

R8 implements the complete precedence-aware effective-record and Verified-evidence audit. All artifacts are committed with the remediation.

## Sources and reports

- `implementation-report.md` — complete R8 implementation and candidate audit.
- `precommit-transcript.txt` — commands, complete stdout/stderr, and exit codes.
- `evidence-inventory.csv` — paths, byte sizes, and SHA-256 values.
- `checksums.sha256` — independently checkable SHA-256 list.

## Scripts

- `scripts/validate_effective_traceability.py` — complete R8 validator.
- `scripts/reconcile_evidence.py` — exact evidence/limitation ledger reconciliation.
- `scripts/capture_precommit.py` — deterministic command capture.

## Complete artifacts

- `artifacts/effective-record-audit.csv` — 317 rows; final value and source for all 16 required fields.
- `artifacts/mapping-resolution-audit.csv` — every group field/ID resolution, syntax, status, and defect detail.
- `artifacts/exact-location-audit.csv` — 317 exact effective locations and anchor results.
- `artifacts/authority-source-registry.csv` — 266 independent authority-source records.
- `artifacts/verified-evidence-audit.csv` — one row for each of 20 Verified requirements.
- `artifacts/limitation-audit.csv` — 317 source/effective limitation comparisons.
- `artifacts/packet-dependency-audit.csv` — all 51 non-Approved mappings.
- `artifacts/validation-output.txt` — required computed output.
- `artifacts/defects.csv` — final defect register (`None`).

The containing Git commit and push facts are returned in the release handoff. A Git commit cannot include its own object ID in its content because that content determines the ID; this package therefore uses no false post-commit placeholder.
