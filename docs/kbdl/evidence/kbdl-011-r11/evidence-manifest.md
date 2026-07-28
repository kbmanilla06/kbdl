# KBDL-011-R11 Evidence Manifest

This package records the current-authority and semantic-evidence validation for
KBDL-011-R11. It is documentation-only and creates no readiness or completion
approval.

## Primary evidence

- `initial-clean-state.txt` — synchronized baseline evidence.
- `precommit-transcript.txt` — commands, purposes, stdout, stderr, exit codes,
  and results.
- `artifacts/current-authority-audit.csv` — 137-row AR2 authority join.
- `artifacts/complete-effective-field-audit.csv` — 317-row effective audit.
- `artifacts/verified-requirement-inventory.csv` — 20 Verified requirements.
- `artifacts/clause-level-evidence-audit.csv` — 32 method clauses.
- `artifacts/val-003-audit.txt`, `val-004-audit.txt`, `val-006-audit.txt`, and
  `val-007-audit.txt` — dependency-ordered VAL results.
- `negative-tests/` — twenty isolated mutation artifacts and summary.
- `artifacts/candidate-readiness.txt` — documentation-only recommendation.
- `artifacts/normative-preservation-audit.txt` — protected-scope comparison.
- `evidence-inventory.csv` and `checksums.sha256` — availability, sizes, and
  SHA-256 values.

## Boundaries

Historical approval commands remain unrecovered. Current authority is effective
and non-retroactive. Implementation conformance remains `NOT VERIFIED`; project
completion remains pending. The only next action is planning-agent validation
of R11.
