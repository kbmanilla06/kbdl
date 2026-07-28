# KBDL-011-R9 Evidence Manifest

R9 proves validator soundness with source-derived positive checks and 21 isolated negative controls.

- `implementation-report.md` — complete implementation and candidate audit.
- `initial-clean-state.txt` — baseline safety evidence captured before edits.
- `precommit-transcript.txt` — exact final commands, stdout, stderr, and exits.
- `approval-authority-registry.csv` — durable prompt approval sources and scopes.
- `verified-evidence-registry.csv` — distinct evidence sources, required results, and Verified scopes.
- `scripts/production_validator.py` — production group/evidence/authority/location/documentation validator.
- `scripts/documentation_validator.py` — complete fourteen-category documentation validator.
- `scripts/run_negative_controls.py` — isolated mutation harness.
- `scripts/run_full_validation.py` — complete positive/negative orchestration.
- `artifacts/production-validation.txt` — positive production output.
- `artifacts/production-effective-record.csv` — 317 production records.
- `artifacts/group-conflict-audit.csv` — explicit mapping comparison.
- `artifacts/approval-authority-audit.csv` and `authority-validation.txt` — approval registry verification.
- `artifacts/verified-evidence-audit.csv` and `evidence-source-validation.txt` — complete 20-claim evidence results.
- `artifacts/historical-location-audit.csv` — independently derived PRN locations.
- `artifacts/documentation-validation.txt` — fourteen-category positive documentation output.
- `artifacts/completion-scan.txt` — independent completion-decision scan.
- `negative-tests/*.txt` — one artifact per negative control and summary.
- `artifacts/final-validation-output.txt` — required combined result.
- `evidence-inventory.csv` and `checksums.sha256` — byte sizes and full SHA-256 values.

All mutations execute in temporary copies and are deleted. Release commit/push facts are returned in the handoff because a Git object cannot contain its own hash.
