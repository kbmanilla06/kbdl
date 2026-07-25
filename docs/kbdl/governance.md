# KBDL Governance and Change Control

Status: `Approved`

Return to the [specification index](README.md). Status labels are defined in
[conventions.md](conventions.md#1-status-labels); requirement IDs in
[conventions.md](conventions.md#2-requirement-identification).

## KBDL-GOV-001 — Specification architecture is established

The KBDL specification uses the documentation hierarchy, status labels,
requirement-ID scheme, and cross-reference conventions defined in
[README.md](README.md#document-hierarchy) and [conventions.md](conventions.md).
Later modules must be added into this hierarchy rather than reorganizing it.

## KBDL-GOV-002 — Accessibility requirements are protected

Accessibility requirements (module code `A11Y`) and motion-safety
requirements (module code `MOT`, safety-related subset) are locked rules.
They may not be silently removed, weakened, or bypassed. Any change requires
an approved exception recorded in the [decision register](decision-register.md)
and referenced from the affected requirement.

## KBDL-GOV-003 — Documentation governance process

The rules below govern how the KBDL specification changes over time.

### Ownership

- The project owner holds final approval authority over KBDL decisions,
  scope, and every change to a requirement's lifecycle status to
  `Approved`. Only the project owner may grant `Approved` status; no other
  lifecycle or dimension label substitutes for it (see
  [conventions.md](conventions.md#1-status-labels)).
- Any contributor may propose changes, record `Recommended` or `Assumed`
  content, and perform validation — including recording a `Verified`
  validation status with evidence attached — but may not unilaterally grant
  `Approved` lifecycle status. Recording `Verified` documents that
  validation happened; it never approves scope and never substitutes for
  the project owner's approval.

### Proposal process

1. A change is proposed by describing the requirement, module, and rationale.
2. The proposal is recorded with an appropriate status (`Recommended` or
   `Assumed`) until reviewed.
3. The proposal identifies affected requirement IDs, modules, and documents
   using the [cross-reference conventions](conventions.md#3-cross-reference-conventions).

### Review process

- A review checks: terminology consistency with the [glossary](glossary.md),
  correct requirement-ID usage, correct status labeling, updated
  [traceability](traceability-matrix.md), and scope compliance with the
  active roadmap step.
- Reviews record findings against the [conformance checklist](conformance-checklist.md).

### Approval requirements

- A requirement's lifecycle status becomes `Approved` only with explicit
  project-owner authorization, recorded in the
  [decision register](decision-register.md) when the decision is
  significant enough to warrant a decision record. This is the only
  condition under which implementation is authorized.
- A requirement's validation status becomes `Verified` only when its
  validation method has been run and evidence is recorded in the
  [traceability matrix](traceability-matrix.md). Recording `Verified` is a
  separate act from approval: it may be done by any contributor who
  performed the validation, and it neither requires nor grants `Approved`
  lifecycle status.
- A requirement intended for implementation must reach `Approved` lifecycle
  status before implementation begins, and `Verified` validation status
  after implementation is checked. Neither label substitutes for the other.

### Scope-change process

- Any change that would expand a roadmap step's scope (for example
  introducing design values during KBDL-001) requires an impact assessment
  describing what changes, which requirements and modules are affected, and
  explicit project-owner approval before proceeding.
- Scope changes are recorded in the [decision register](decision-register.md).

### Exception process

- An exception to a locked rule (see KBDL-GOV-002) must state: the rule
  affected, the reason, the scope and duration, and the approving decision.
- Exceptions are recorded as decision records with status `Approved` and
  referenced from the affected requirement.

### Deprecation process

- A requirement or guidance section is marked `Deprecated` when it is no
  longer recommended but not yet replaced.
- The original text is preserved with the `Deprecated` label rather than
  deleted, so historical context remains available.

### Versioning principles

- KBDL does not use numeric document versions in KBDL-001. Change history is
  carried by the [decision register](decision-register.md), status labels,
  and (where the repository is under version control) commit history.
- A future roadmap step may introduce a formal versioning scheme; until then,
  the decision register is the source of truth for what changed and why.

### Documentation-update requirements

- Any change to a requirement's status, wording, or ID must update every
  cross-referencing document, the [traceability matrix](traceability-matrix.md),
  and, where applicable, the [decision register](decision-register.md) in the
  same change.

### Accessibility review expectations

- Any change touching an `A11Y` requirement, or any other requirement with a
  stated accessibility impact, requires explicit confirmation that WCAG 2.2
  Level AA and KBDL's enhanced motion-safety requirements are still met,
  recorded in the affected decision record or traceability row.

### Motion review expectations

- Any change touching a `MOT` requirement requires explicit confirmation that
  reduced-motion behavior is preserved, following the same recording
  requirement as accessibility review.

### Responsive review expectations

- Any change touching an `RSP` requirement requires explicit confirmation
  that the change holds across the responsive breakpoints defined once the
  `RSP` module exists.

### Conformance-review process

- Conformance is assessed using the [conformance checklist](conformance-checklist.md).
  A requirement is `Passed` only with recorded evidence; absence of evidence
  is `Not verified`, never `Passed`.

### Conflict-resolution process

When two sources of truth conflict (see the source-of-truth hierarchy in
this prompt), the following steps apply:

1. Stop work on the conflicting portion.
2. Document the conflict: the sources involved, the exact disagreement, and
   the affected requirement IDs and files.
3. Do not silently default to the lower-priority source.
4. Escalate to the project owner for a decision, recorded in the
   [decision register](decision-register.md).
5. Resume work only once the conflict is resolved and recorded.

### Restoration from an approved snapshot

- If a document must be reverted, restore from the last commit (or file
  version) known to reflect an `Approved` state, as identified in the
  [decision register](decision-register.md) or version-control history.
- Restoration itself is recorded as a decision if it changes previously
  `Approved` or `Verified` content.

### Evidence required to declare a requirement `Verified`

- A stated validation method (see [traceability-matrix.md](traceability-matrix.md)).
- The actual result of running that method (command output, review notes, or
  link-check results).
- The date and, where available, who performed the validation.
- A `Verified` label must not be applied on the basis of the requirement
  merely existing or reading correctly; the validation method must have
  actually been executed.

## Additional Preserved Rules

- Only the lifecycle status `Approved` authorizes implementation (see
  [conventions.md](conventions.md#1-status-labels)). `Recommended`,
  `Unresolved`, `Deferred`, and `Blocked` items are never implementation
  authority. Provenance labels (`Confirmed`, `User-provided`, `Assumed`) and
  the validation label `Verified` describe origin, confidence, or checking
  outcome — none of them independently authorize implementation.
- A project profile (`PRO`) may adjust emphasis but must not replace or
  contradict KBDL foundations (`FND`) or locked rules.
- Unverified work cannot be labeled complete; use `Not verified` until
  evidence exists. A requirement being `Approved` does not by itself make it
  complete — completion requires the separate `Verified` validation status.
- A failed requirement must either be remediated or explicitly marked
  `Deferred` with a recorded approval; it cannot be left silently failing.
- Roadmap steps after the currently active one (see the
  [progression gate](README.md#specification-status)) must not begin early.
