# KBDL-011-R10 Evidence Manifest

R10 records a blocked semantic reconciliation. It does not claim that missing
historical project-owner authority was recovered or that the candidate is ready.

- `initial-clean-state.txt` — branch, synchronization, clean-tree, and baseline evidence captured before editing.
- `prompt-authority-recovery.csv` — one record per KBDL prompt; all eleven exact historical commands/scopes are explicitly unrecovered.
- `authority-recovery-request.md` — separate project-owner action required to resolve prompt authority.
- `scripts/semantic_audit.py` — conservative audit that exits nonzero while authority and semantic evidence remain unresolved.
- `artifacts/complete-effective-field-audit.csv` — 317 per-ID records; blocked or not-completely-revalidated results are retained, not converted to PASS.
- `artifacts/verified-clause-audit.csv` — clause-level inventory of current Verified methods with blocked coverage results.
- `artifacts/documentation-output.txt` — documentation-validator output.
- `artifacts/validation-output.txt` — exact R10 summary showing `NOT READY` and exit-driving defects.
- `implementation-report.md` — acceptance-criterion disposition, affected original criteria, risks, gate, and rollback.
- `precommit-transcript.txt` — final commands, stdout/stderr, and exit codes.
- `evidence-inventory.csv` — evidence paths, byte sizes, and SHA-256 values.
- `checksums.sha256` — SHA-256 checksums for package files other than this self-referential checksum file.

The commit SHA, push output, final remote SHA, and final clean-tree result cannot
be embedded in their own commit. They are returned in the release handoff.
