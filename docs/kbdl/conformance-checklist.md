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

## KBDL-009 Project Profiles Checklist Items

Applies in addition to the generic checklist above whenever a change
touches [profiles.md](profiles.md) or any `KBDL-PRO-###` requirement.
Uses the same four-column result convention.

| # | Item | Passed | Failed | Not verified | Not applicable |
| --- | --- | --- | --- | --- | --- |
| 18 | Profile declaration is present where applicable ([profiles.md §8](profiles.md#8-profile-selection-and-declaration)) | | | | |
| 19 | Profile selection rationale is documented, not based on visual preference alone | | | | |
| 20 | Project Profile is not confused with theme mode, viewport, device, role, persona, or manual customization | | | | |
| 21 | One shared semantic architecture is preserved across Showcase, Precision, and Flow | | | | |
| 22 | One shared accessibility architecture is preserved across all profiles | | | | |
| 23 | Cross-profile invariants ([profiles.md §9](profiles.md#9-cross-profile-invariants)) are preserved | | | | |
| 24 | Foundation roles and Approved values remain shared, not profile-specific | | | | |
| 25 | Theme semantic roles and mode behavior remain shared, not profile-specific | | | | |
| 26 | Motion timing/easing architecture remains shared, not profile-specific | | | | |
| 27 | Responsive and reflow outcomes remain shared, not profile-specific | | | | |
| 28 | Component semantics and anatomy (KBDL-007 and KBDL-008) remain unchanged across profiles | | | | |
| 29 | Security, privacy, correctness, and state-accuracy requirements remain shared across profiles | | | | |
| 30 | Pending KBDL-006 dependencies are identified and not promoted | | | | |
| 31 | Pending KBDL-007 dependencies are identified and not promoted | | | | |
| 32 | Pending KBDL-008 dependencies are identified and not promoted | | | | |
| 33 | Approval-ready and contingent KBDL-009 decisions are separated correctly ([profiles.md §34](profiles.md#34-approval-ready-versus-contingent-decisions)) | | | | |
| 34 | Every non-Approved `KBDL-PRO-###` requirement has a packet or tracking destination ([profiles.md §38](profiles.md#38-decision-packet-coverage-audit)) | | | | |
| 35 | KBDL-011 final validation and later roadmap work remain unstarted | | | | |
| 36 | Implementation-level profile conformance is not claimed without recorded evidence | | | | |

No row above is marked `Passed` in this repository; no project-level
implementation exists to generate evidence against.

## KBDL-010 Manual Customization Checklist Items

Applies in addition to the generic checklist whenever a change touches
[customization.md](customization.md), a customization record, or any
`KBDL-CUS-###` requirement. No row is pre-marked.

| # | Item | Passed | Failed | Not verified | Not applicable |
| --- | --- | --- | --- | --- | --- |
| 37 | Customization is manual and documented | | | | |
| 38 | Project and declared Profile are identified | | | | |
| 39 | Every affected module and requirement is identified | | | | |
| 40 | Source lifecycle statuses are recorded accurately | | | | |
| 41 | Request has exactly one correct primary class | | | | |
| 42 | Locked rules remain unchanged | | | | |
| 43 | Approved requirements remain unchanged unless an Approved exception exists | | | | |
| 44 | Controlled options remain inside Approved owning-module bounds | | | | |
| 45 | Open expression remains subordinate to locked and Approved rules | | | | |
| 46 | Pending recommendations are not promoted | | | | |
| 47 | Accessibility impact is reviewed | | | | |
| 48 | Responsive impact is reviewed | | | | |
| 49 | Theme and foundation impacts are reviewed | | | | |
| 50 | Motion impact is reviewed | | | | |
| 51 | Component semantics and anatomy are preserved | | | | |
| 52 | Profile invariants are preserved | | | | |
| 53 | Security, privacy, correctness, and data integrity are preserved | | | | |
| 54 | Required approval and its exact authority are recorded | | | | |
| 55 | Decision-register impact is handled correctly | | | | |
| 56 | Validation method and required evidence are defined | | | | |
| 57 | Implementation-level validation is not claimed prematurely | | | | |
| 58 | Rollback is documented | | | | |
| 59 | Duration and review conditions are documented | | | | |
| 60 | Reusable customization is escalated appropriately | | | | |
| 61 | Every non-Approved CUS requirement has one packet or tracking destination | | | | |
| 62 | Final validation and later-roadmap content remain unstarted | | | | |

## Result Summary

State the overall result as `Passed`, `Failed`, `Not verified`, or a mix with
per-item detail. A change with any `Failed` item is not ready for approval
until remediated or the failure is explicitly `Deferred` per
[governance.md](governance.md).
