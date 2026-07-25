# KBDL Contribution and Review Guidance

Status: `Approved`

Return to the [specification index](README.md). This document implements the
process rules defined in [governance.md](governance.md).

## Contributor Workflow

Follow these steps in order for any change to the KBDL specification:

1. **Inspect current documentation and decisions.** Read the affected
   module(s), the [decision register](decision-register.md), and the
   [traceability matrix](traceability-matrix.md) before writing anything, so
   the change is consistent with what already exists.
2. **Identify the requirement being changed.** State the requirement ID if
   one exists, or note that a new one is being proposed (see
   [conventions.md](conventions.md#2-requirement-identification)).
3. **Check related modules and cross-references.** Search for other
   documents that reference the affected requirement, module, or term, using
   the [cross-reference conventions](conventions.md#3-cross-reference-conventions).
4. **Record assumptions and unresolved questions.** Anything not directly
   confirmed by the user or repository must be labeled `Assumed` or
   `Unresolved` per [conventions.md](conventions.md#1-status-labels), not
   written as fact.
5. **Make the narrowest necessary change.** Do not refactor unrelated
   sections, rename unrelated terms, or restructure documents beyond what the
   change requires.
6. **Update traceability.** Add or update the relevant row(s) in the
   [traceability matrix](traceability-matrix.md).
7. **Update the decision register when required.** Any change to scope,
   approved status, or a locked rule requires a decision record (see
   [governance.md](governance.md)).
8. **Run applicable validation.** Use whatever validation tooling exists in
   the repository (see [README.md](README.md#how-to-use-this-specification)),
   or perform the manual review described in [governance.md](governance.md#conformance-review-process).
9. **Report evidence.** State exactly what was run or reviewed and its
   actual result; do not report validation as passed without evidence.
10. **Request review.** Submit the change against the
    [conformance checklist](conformance-checklist.md) for approval.

## Preserving Unrelated Work

- Do not modify files, sections, or terminology outside the scope of the
  change being made.
- Do not perform broad, unapproved refactoring, reformatting, or renaming as
  part of an unrelated change.
- If unrelated issues are discovered while working, record them as
  `Unresolved` in the [traceability matrix](traceability-matrix.md) rather
  than fixing them inline.
- If uncommitted or unfamiliar work is found in the repository, investigate
  its origin before changing or removing it; do not assume it is safe to
  discard.

## What a Reviewer Checks

A reviewer verifies, using the [conformance checklist](conformance-checklist.md):

- The change uses correct KBDL terminology (per the [glossary](glossary.md)).
- Requirement IDs and status labels follow [conventions.md](conventions.md).
- Traceability and cross-references are updated and not broken.
- The change stays within the approved scope of the current roadmap step.
- Accessibility, motion, responsive, theme, profile, and component impacts
  are stated, even when the answer is `Not applicable`.
- The decision register is updated where required.
- Deferred and unresolved items are recorded, not silently dropped.
- Validation evidence is present and matches what was actually run.
