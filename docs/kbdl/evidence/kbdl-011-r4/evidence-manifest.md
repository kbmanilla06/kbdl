# KBDL-011-R4 Evidence Manifest

This package records the source-of-truth traceability remediation. The ledger generator reads authoritative Markdown only. The independently implemented validator separately parses the same authoritative sources and approved decisions; it uses the R2 audit only to calculate the historical regression count after current values are derived.

## Evidence inventory

- `scripts/generate_authoritative_ledger.py` — direct Markdown ledger generator.
- `scripts/validate_authoritative_ledger.py` — independent parser, comparator, baseline audit, and result calculator.
- `scripts/capture_precommit.py` — exact command/stream/exit-code capture.
- `artifacts/authoritative-comparison.csv` — complete 317-row comparison.
- `artifacts/provenance-mismatches.csv` — complete mismatch artifact (header only when zero).
- `artifacts/mixed-validation-scopes.csv` — all validation classifications and scopes.
- `artifacts/authority-resolution.csv` — authority statements, targets, missing targets, and circularity.
- `artifacts/packet-dependency.csv` — exact packet/tracking destinations and dependencies.
- `artifacts/baseline-differences.csv` — computed baseline metadata differences.
- `artifacts/validation-output.txt` — complete independent-validator result.
- `precommit-transcript.txt` — commands, purposes, stdout, stderr, exit codes, and results.

Sizes and full SHA-256 checksums are recorded in `checksums.sha256` after the final evidence run. Parser independence is structural: neither script imports the other, and each defines its own record segmentation, field extraction, normalization, and comparison logic.

Candidate calculation: documentation candidate readiness is recommended only when the independent validator, documentation validator, and `git diff --check` all pass. This does not change implementation conformance (`NOT VERIFIED`) or project completion (`PENDING PLANNING-AGENT VALIDATION AND PROJECT-OWNER APPROVAL`). Accepted limitations: None.
