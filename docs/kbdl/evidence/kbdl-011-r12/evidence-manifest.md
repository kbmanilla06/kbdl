# KBDL-011-R12 Evidence Manifest

R12 replaces R11 baseline comparison and requirement-level evidence inheritance
with direct normative-block parsing and clause-specific evidence decisions.

Primary artifacts:

- `artifacts/authoritative-requirement-blocks.csv` — 317 directly located blocks.
- `artifacts/complete-effective-field-audit.csv` — source/group/ledger precedence.
- `artifacts/approved-authority-chain-audit.csv` — all 266 Approved IDs.
- `artifacts/verified-clause-inventory.csv` — retained Verified clauses.
- `artifacts/not-verified-clause-inventory.csv` — excluded/unexecuted clauses.
- `artifacts/clause-level-evidence-audit.csv` — clause-specific evidence.
- `artifacts/manual-review-governance.md` — executed GOV-001/GOV-003 review.
- `artifacts/contrast-execution.txt` — reproduced calculation output.
- `artifacts/val-003-audit.txt`, `val-004-audit.txt`, `val-006-audit.txt`, and
  `val-007-audit.txt` — corrected gate results.
- `negative-tests/` — twelve isolated source-independence controls.
- `precommit-transcript.txt`, `evidence-inventory.csv`, and
  `checksums.sha256` — reproducibility and integrity evidence.

The result is intentionally conservative: `VAL-003`, `VAL-004`, and `VAL-006`
remain Not verified, and candidate readiness is `NOT READY`. No limitation,
readiness, implementation-conformance, or completion approval is created.
