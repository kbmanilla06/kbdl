# KBDL Specification Conventions

Status: `Approved` (governance framework for KBDL-001 and all later modules)

This document defines three foundational conventions used across the entire KBDL
specification: status labels, requirement identifiers, and cross-reference rules.
Every later KBDL module must use these conventions without modification unless a
change is proposed and approved through [governance](governance.md).

Return to the [specification index](README.md).

## 1. Status Labels

Every requirement, decision, or claim in KBDL is described along three
**independent dimensions**: lifecycle/approval status, provenance, and
validation status. A statement can carry one label from each dimension at
once (for example: `Approved`, `User-provided`, `Not verified`, all at the
same time, for the same requirement). No dimension substitutes for another,
and a label from one dimension never implies a label from a different
dimension.

### 1.1 Lifecycle / approval status

This dimension is the **only** source of implementation authority in KBDL.
A requirement may be implemented if, and only if, its lifecycle status is
`Approved`.

| Label | Meaning | Who may assign it |
| --- | --- | --- |
| `Recommended` | An editorial or technical suggestion awaiting approval. Does not authorize implementation. | Any contributor. |
| `Unresolved` | An open question with no current answer. Does not authorize implementation. | Any contributor. |
| `Approved` | The project owner has explicitly authorized this requirement or decision for implementation, through the project's approval process. This is the only label that authorizes implementation. | Project owner only. |
| `Deferred` | Known, intentionally postponed to a later roadmap step, with an approval reference. Does not authorize implementation now. | Project owner. |
| `Blocked` | Work that cannot proceed until a dependency, decision, or conflict is resolved. Does not authorize implementation. | Any contributor; must name the blocker. |
| `Deprecated` | Guidance that is no longer recommended but has not yet been formally replaced. No longer authorizes new implementation. | Project owner, via governance. |
| `Superseded` | Guidance formally replaced by a newer decision or requirement, with a reference to the replacement. No longer authorizes implementation; the replacement's own lifecycle status governs. | Project owner, via governance. |

### 1.2 Provenance

This dimension records **where a statement came from** or how much
confidence it carries. It describes the statement's origin, not whether it
may be implemented. A fact can be `Confirmed` or `User-provided` and still
have a lifecycle status of `Recommended` or `Unresolved` — provenance never
by itself grants approval.

| Label | Meaning | Who may assign it |
| --- | --- | --- |
| `User-provided` | Information stated directly by the project owner and not independently derived. Describes origin, not approval; content only gains implementation authority once it is separately given `Approved` lifecycle status. | Recorded verbatim by whoever received it. |
| `Confirmed` | A fact verified directly against the repository, tooling, or a user statement. Describes factual confidence, not approval; a confirmed fact may inform implementation of an already-approved requirement but cannot expand or alter approved scope on its own. | Any contributor, with evidence. |
| `Assumed` | A working assumption used to make progress in the absence of a decision. Must be flagged for review and never treated as approved. | Any contributor, must be logged in the [decision register](decision-register.md) or [traceability matrix](traceability-matrix.md). |

### 1.3 Validation status

This dimension records **whether a defined validation method has been run**
and its outcome. It is independent of approval: a requirement can be
`Approved` and `Not verified` (approved, but not yet checked), or, in the
unusual case of exploratory validation work, `Verified` while its lifecycle
status is still short of `Approved`. Validation never grants or substitutes
for approval.

| Label | Meaning | Who may assign it |
| --- | --- | --- |
| `Not verified` | The requirement's validation method has not been performed, or evidence could not be confirmed. Default state until evidence exists. | Default; no action needed to hold this state. |
| `Verified` | The requirement's defined validation method has been completed and recorded evidence exists. Recording `Verified` documents that validation happened; it does not authorize implementation and does not grant `Approved` lifecycle status. | Any contributor who performed the validation, with evidence attached. The project owner's approval authority (see [governance.md](governance.md)) is unaffected by who verifies. |

### Combining the dimensions

A requirement intended for implementation must reach `Approved` lifecycle
status. After implementation, it is separately checked and marked
`Verified` once its validation method has actually been run. Examples:

- **`User-provided`, lifecycle `Recommended`, `Not verified`** — the project
  owner stated something directly, but it has not yet been approved as a
  requirement or checked against anything. It is context, not an
  implementable requirement.
- **`Approved`, `Not verified`** — the project owner has authorized
  implementation, but no validation method has been run yet. Implementation
  may proceed; completion cannot yet be claimed.
- **`Approved`, `Verified`** — the project owner has authorized
  implementation and its validation method has been completed with recorded
  evidence. This is the only combination that represents a fully
  implemented and checked requirement.
- **`Confirmed` repository fact, lifecycle `Unresolved`** — a fact observed
  directly in the repository (for example, "no `package.json` exists") is
  `Confirmed`, but that fact alone does not authorize any new scope; it only
  informs decisions that still require their own `Approved` status.

**Status changes:** A lifecycle status changes only when the project
owner's approval process (see [governance.md](governance.md)) justifies the
change; provenance and validation labels change when new evidence is
recorded. Contributors record the reason for any status change in the
affected document and, where applicable, the
[decision register](decision-register.md).

**Implementation authority:** Only the lifecycle label `Approved` authorizes
implementation. `Confirmed`, `User-provided`, `Verified`, and every other
label — regardless of dimension — never independently authorize
implementation. `Recommended`, `Unresolved`, `Deferred`, and `Blocked` items
must never be implemented as if they were approved requirements.

**Unresolved and deferred tracking:** Every `Unresolved` or `Deferred` item
must have a corresponding row in the [traceability matrix](traceability-matrix.md)
so it is not lost between roadmap steps.

**Superseded guidance:** When guidance is superseded, the original text is kept
in place with a `Superseded` label and a link to the replacing decision or
requirement, rather than deleted. This preserves the historical record required
by [governance](governance.md).

## 2. Requirement Identification

KBDL requirements use a stable, human-readable, module-scoped identifier:

```
KBDL-<MODULE>-<###>
```

- `KBDL` — fixed project prefix.
- `<MODULE>` — a short, stable code for the owning module (see table below).
- `<###>` — a three-digit, zero-padded, sequential number, unique within its
  module code. Numbers are never reused.

| Module code | Module |
| --- | --- |
| `GOV` | Governance |
| `PRN` | Principles |
| `FND` | Visual foundations |
| `THM` | Adaptive themes |
| `MOT` | Motion |
| `RSP` | Responsive behavior |
| `A11Y` | Accessibility |
| `CMP` | Components (core action, form, navigation, surface, overlay, feedback, system-state) |
| `PRO` | Project profiles |
| `CUS` | Manual customization |
| `VAL` | Validation |

**Properties:**

- **Stable** — an ID, once assigned, never changes meaning or moves to a
  different module code.
- **Unique** — no two requirements share an ID.
- **Searchable** — IDs are plain text and grep-able across the repository.
- **Independent of page numbering** — IDs do not encode document position, so
  reordering a document never invalidates an ID.
- **Extensible** — new module codes may be added by governance approval without
  renumbering any existing module's requirements.

**Lifecycle:**

- **Creation** — a new requirement is assigned the next unused number in its
  module code at the time it is `Approved`. Draft or `Recommended` text may
  exist without an ID until it is approved.
- **Retirement** — a requirement that is no longer applicable is marked
  `Deprecated` or `Superseded`; its ID is never reassigned to a different
  requirement.
- **Supersession** — a replacing requirement gets a new ID and references the
  superseded ID; the superseded requirement's entry records the new ID.
- **Referencing** — any document may reference a requirement by its ID alone
  (e.g. "see `KBDL-GOV-001`"); the [traceability matrix](traceability-matrix.md)
  resolves each ID to its current specification location.

This prompt (KBDL-001) introduces governance-scoped requirements under `GOV`
only, to demonstrate the convention. See the [decision register](decision-register.md)
and [traceability matrix](traceability-matrix.md).

## 3. Cross-Reference Conventions

KBDL documents link to each other using relative Markdown links so references
work both inside a rendered documentation site and when a file is opened
individually.

**Rules:**

1. **Sections** — link to another specification section using a relative path
   and, where the target module exists, a heading anchor:
   `[Motion](motion/README.md#9-normative-requirements)`.
2. **Requirement IDs** — always state the ID as literal text (`KBDL-A11Y-003`)
   even inside a link, so the reference is understandable without following the
   link.
3. **Decisions** — reference decisions by their Decision ID from the
   [decision register](decision-register.md), e.g. `KBDL-DEC-004`.
4. **Exceptions** — reference an exception by the requirement ID it applies to
   plus the approving decision ID, e.g. "exception to `KBDL-A11Y-002` approved
   under `KBDL-DEC-009`".
5. **Deferred work** — reference deferred items by their row in the
   [traceability matrix](traceability-matrix.md).
6. **Validation evidence** — reference validation evidence by requirement ID and
   the validation method recorded in the traceability matrix, not by pasting
   raw logs into specification text.
7. **Standalone readability** — every cross-reference must include enough plain
   text (the ID, a short title) that a reader viewing the source document alone
   — without following the link — still understands what is being referenced.
8. **No orphan links** — a document must not link to a section, module, or file
   that does not yet exist. Planned-but-unwritten modules are referenced by name
   and future path in the [module hierarchy](README.md#document-hierarchy)
   table, not as clickable links, until the target file exists.

Decision IDs use the format `KBDL-DEC-###`, defined in the
[decision register](decision-register.md).
