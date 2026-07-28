# KBDL-011-AR1 Evidence Manifest

This is a preparation-only evidence package. It grants no authority.

- `authority-recovery-packet.md` — eleven separately reviewable records and proposed non-effective confirmations.
- `authority-recovery-ledger.csv` — required 25-column, one-row-per-prompt ledger.
- `project-owner-review.md` — five unselected choices for each prompt.
- `authority-gaps.csv` — eleven original-approval gaps plus the KBDL-005 conflation risk.
- `sources/kbdl-010-released-prompt.md` and `sources/kbdl-011-released-prompt.md` — exact available released prompt texts.
- `artifacts/requirement-authority-mapping.csv` — 137 recomputed prompt-authority mappings with exact current clauses and sole/mixed classification.
- `artifacts/source-inventory.csv` — sources inspected and evidence classification.
- `artifacts/missing-evidence-report.txt` — recovered/unrecovered evidence summary.
- `artifacts/documentation-validation.txt` — link, anchor, heading, table, ID, packet, roadmap, and claim checks.
- `artifacts/validation-summary.txt` — required AR1 summary and normative-preservation counts.
- `scripts/build_packet.py` and `scripts/validate_packet.py` — reproducible generation and validation sources.
- `initial-clean-state.txt` — required baseline facts.
- `precommit-transcript.txt` — commands, purposes, stdout, stderr, and exits.
- `implementation-report.md` — full result and AC disposition.
- `evidence-inventory.csv` and `checksums.sha256` — sizes and full SHA-256 values.

Commit/push/final remote and clean-tree evidence are returned in the release
handoff because a Git commit cannot contain its own hash or post-push state.
