# KBDL Conformance Checklist

Status: `Approved`

Return to the [specification index](README.md).

## How to Use This Checklist

Every KBDL change or module is assessed against the items below. Each item is
marked with exactly one of:

- **Passed** — the item was checked and met the requirement, with evidence.
- **Failed** — the item was checked and did not meet the requirement.
- **Not verified** — the item has not yet been checked, or evidence is
  missing. This is the default state; it is never used interchangeably with
  `Passed`.
- **Not applicable** — the item does not apply to the change being reviewed,
  with a stated reason.

An unfinished requirement must never be marked `Passed`.

## Checklist Items

| # | Item | Passed | Failed | Not verified | Not applicable |
| --- | --- | --- | --- | --- | --- |
| 1 | Correct KBDL terminology used, consistent with the [glossary](glossary.md) | | | | |
| 2 | Requirement IDs follow the format in [conventions.md](conventions.md#2-requirement-identification) | | | | |
| 3 | Status labels used correctly per [conventions.md](conventions.md#1-status-labels) | | | | |
| 4 | Traceability updated in the [traceability matrix](traceability-matrix.md) | | | | |
| 5 | Cross-references follow [conventions.md](conventions.md#3-cross-reference-conventions) and resolve correctly | | | | |
| 6 | Change stays within the approved scope of the active roadmap step | | | | |
| 7 | Accessibility impact stated (or `Not applicable` with reason) | | | | |
| 8 | Motion impact stated (or `Not applicable` with reason) | | | | |
| 9 | Responsive impact stated (or `Not applicable` with reason) | | | | |
| 10 | Theme impact stated (or `Not applicable` with reason) | | | | |
| 11 | Project-profile impact stated (or `Not applicable` with reason) | | | | |
| 12 | Component impact stated (or `Not applicable` with reason) | | | | |
| 13 | [Decision register](decision-register.md) updated where required | | | | |
| 14 | Deferred and unresolved items recorded, not dropped | | | | |
| 15 | Validation evidence recorded and matches what was actually run | | | | |
| 16 | Unresolved risks documented | | | | |
| 17 | Reviewer approval recorded | | | | |

## Result Summary

State the overall result as `Passed`, `Failed`, `Not verified`, or a mix with
per-item detail. A change with any `Failed` item is not ready for approval
until remediated or the failure is explicitly `Deferred` per
[governance.md](governance.md).
