# KBDL Manual Customization Specification

Status: mixed — requirement-level lifecycle, provenance, and validation status are authoritative.

Return to the [specification index](README.md).

## 1. Purpose and Scope

This document defines framework-neutral governance for manually customizing a KBDL-based project. A project may customize only what KBDL explicitly leaves controlled or open, and only within the owning module's Approved bounds. Every customization is manually chosen, documented, attributable, reviewable, reversible, and subordinate to higher-priority requirements.

This module does not customize a project, create implementation formats or tooling, approve a recommendation or exception, or perform final validation.

## 2. Lifecycle and Validation Status

Lifecycle status, provenance, and validation status are independent. Only `Approved` lifecycle status authorizes implementation. A technically successful or `Verified` result does not grant authority; an authorized choice remains `Not verified` until its defined implementation evidence exists. Approval of the KBDL-010 prompt authorizes its mandatory scope, not the [decision packet](#37-kbdl-010-decision-packet).

## 3. Relationship to Prior KBDL Modules

This module applies [KBDL-DEC-004](decision-register.md#kbdl-dec-004--customization-is-manual-and-documented), the [design-decision hierarchy](principles.md#8-design-decision-hierarchy), the [governance exception process](governance.md#exception-process), and the owning requirements in foundations, themes, motion, responsive behavior, accessibility, components, and [Project Profiles](profiles.md). It creates no second semantic, accessibility, foundation, theme, motion, responsive, component, or Profile architecture.

## 4. Customization Terminology

- **Manual customization** — a human-chosen, documented project choice within Approved bounds or a governed request beyond them; never an automated or silent mutation.
- **Customization request** — the intake description of a desired project outcome before authority is established.
- **Customization record** — the auditable project record of classification, authority, scope, impacts, evidence, and rollback.
- **Customization owner / reviewer** — the accountable project role and the role reviewing the record; exact role names remain Recommended.
- **Source requirement** — the owning KBDL requirement or decision whose lifecycle bounds the request.
- **Approved option selection** — selection of an explicitly permitted option within Approved bounds.
- **Project-local customization** — a bounded choice intended for one project.
- **Reusable customization** — a choice intended for multiple projects and therefore a candidate KBDL proposal.
- **Proposed KBDL extension** — a proposed reusable role, meaning, variant, option, or policy that remains non-Approved until governed.
- **Customization conflict** — incompatibility between a request and a higher-priority requirement, Profile, dependency, or other record.
- **Customization exception** — an Approved, recorded deviation under governance; this document creates none.
- **Customization dependency** — an approval or source decision required before a request can proceed.
- **Customization evidence** — artifacts demonstrating the defined validation method without granting lifecycle authority.
- **Customization rollback** — the documented restoration path and evidence.
- **Stale customization** — a record requiring review because its source, Profile, scope, or authority changed.
- **Superseded customization** — a record replaced by an explicitly linked later record.
- **Customization conformance** — authorized and validated implementation of the applicable Approved requirements and record scope.

Existing meanings of locked rule, controlled variable, open brand expression, Project Profile, lifecycle status, and validation status remain defined by the [glossary](glossary.md).

## 5. Customization Authority Model

A request, mockup, prototype, stakeholder preference, Profile choice, CUS ID, record, similar project, or successful implementation never supplies authority. Authority comes only from Approved sources. A record documents authority; it does not create it. Pending, unresolved, deferred, blocked, deprecated, or superseded material cannot be used as an Approved option.

## 6. Locked, Controlled, Open, Proposed, and Exception Classifications

| Classification | Meaning | Implementation path |
| --- | --- | --- |
| Locked | Rule cannot be altered locally | Preserve, or stop for an Approved exception |
| Controlled | Variation explicitly bounded by an owning Approved requirement | Select and document within those bounds |
| Open | Project-owned expression subordinate to all locked and Approved rules | Document material choices and validate impacts |
| Proposed | Choice has no complete Approved authority | Keep non-Approved and route through governance |
| Exception | Requested deviation from a locked or Approved rule | Stop until an Approved decision record exists |

## 7. Manual Customization Workflow

1. Receive the request and identify project, declared Profile, outcome, users, environments, modules, and requirements.
2. Inspect lifecycle, provenance, validation status, dependencies, and decision history.
3. Classify the request under [§6](#6-locked-controlled-open-proposed-and-exception-classifications) and [§32](#32-customization-classification-matrix).
4. Apply the design-decision hierarchy and assess accessibility, responsive, foundations/theme, motion, components, Profile, content, security/privacy/correctness/data integrity, and performance.
5. Determine Approved bounds, approval path, and blockers.
6. Create or update the record, exact scope/exclusions, constraints, evidence plan, and rollback.
7. Obtain required authority before implementation.
8. Validate separately; record evidence, limitations, and disposition.
9. Review, supersede, retire, or roll back when a source or Profile changes.

## 8. Customization Request Intake

Intake records project name and Profile; title, outcome, rationale, requestor and owner; affected areas, users, modules, known IDs, and environments; accessibility, responsive, theme/foundation, motion, component, security/privacy/correctness, performance, and Profile impacts; dependencies, urgency, duration, reuse intention, rollback, and uncertainty. Genuinely inapplicable fields may say why.

## 9. Source and Lifecycle Inspection

Inspect every source's lifecycle, provenance, validation status, decision, packet state, dependencies, replacement status, and owning module. Conflicts follow the source-of-truth hierarchy and stop rather than being resolved from a lower-priority source.

## 10. Impact Assessment

Assessment covers affected people, tasks, semantics, accessibility, responsive behavior, foundation/theme, motion, component contracts, Profile invariants, content, security, privacy, correctness, data integrity, performance, interoperability, dependencies, evidence, reversibility, and source-change risk.

## 11. Customization Record

Every record contains: title; project; Profile; identifier or visible placeholder; requestor; owner; reviewer; proposed date; workflow status; class; outcome; rationale; affected modules; affected requirements; source lifecycle statuses; Approved authority; dependencies; exact scope and exclusions; selected choices and values; accessibility, responsive, theme, foundation, motion, component, Profile, content, security, privacy, correctness/data-integrity, and performance impacts; implementation constraints; validation method and evidence; validation status; limitations; rollback; effective scope; duration; review/expiry or expiration date; superseded record; related decision; change history; and final disposition.

Source lifecycle, record workflow, local approval authority, and validation status are separate fields. If a workflow state contains “Approved,” it identifies approver, exercised authority, local-versus-KBDL scope, and exclusions.

## 12. Approval and Escalation Paths

- **Existing Approved selection:** document the local selection; no KBDL lifecycle change.
- **Open expression:** document material/reusable choices and confirm locked-rule compliance.
- **New project-local controlled option:** keep non-Approved until applicable authority reviews it; local review does not change KBDL lifecycle.
- **Reusable extension:** proposal, impact assessment, non-Approved requirement where stable, traceability, packet, and project-owner approval.
- **Locked-rule exception:** stop and use governance plus the decision register; KBDL-010 creates none.
- **Pending dependency:** remain contingent and identify blocker and required approval.

## 13. Implementation Handoff Boundary

Handoff occurs only after authority, exact scope, exclusions, constraints, dependencies, evidence, and rollback are recorded. Implementation teams may choose technologies locally but may not represent those choices as KBDL policy or infer permission outside the record.

## 14. Validation and Evidence Planning

The record defines observable outcomes, environments, assistive technologies where applicable, responsible reviewer, evidence artifacts, pass/fail conditions, limitations, and rollback verification. Documentation review cannot mark implementation behavior `Verified`.

## 15. Review, Expiry, Change, and Rollback

Review follows a source change, Profile change, lifecycle promotion, deprecation/supersession, scope change, failed validation, or incident. Temporary authority must not survive expiry. Supersession preserves linked history; rollback records success, failure, or incomplete migration. Exact cadence and default expiry remain Recommended.

## 16. Foundations Customization

Preserve semantic roles, Approved scales/values, hierarchy, contrast, responsive priority, state clarity, and Profile invariants. Only owning-module Approved controlled alternatives may be selected for color, typography, spacing/layout, shape, borders, depth, iconography, imagery, or media. Open imagery remains permitted subject to all higher requirements. No new value or scale is authorized here.

## 17. Theme Customization

Use the Approved [project-controlled adaptation](themes/adaptation.md#1-project-controlled-adaptation): shared semantic roles, light/dark parity, preference precedence, focus, contrast, status meaning, local contrast contexts, documentation, and cross-Profile compatibility. A project brand color maps through an Approved role and is validated. Pending opacity, translucent variants, forced-colors policy, visualization palettes, account sync, new roles, token formats, and project-specific theme architectures remain unauthorized.

## 18. Motion Customization

Preserve purpose, hierarchy, Approved timing/easing architecture, safety, reduced/no-motion parity, interaction availability, performance, and shared Profile architecture. No new scale, curve, component-specific quantitative value, device detection, library/rendering choice, or quantitative hazard threshold is authorized.

## 19. Responsive Customization

Preserve content priority, source/focus order, reflow, text resizing, orientation, safe areas, virtual-keyboard access, input parity, semantic continuity, and recovery. Local implementation choices do not promote pending exact breakpoints, grid counts, gutters, containers, navigation thresholds, or data/surface transformations.

## 20. Accessibility Customization Boundary

Accessibility is locked. Customization cannot lower WCAG 2.2 AA, remove keyboard/pointer alternatives, obscure focus, weaken target size, depend on color/motion alone, remove alternatives/status/error/authentication support, disable preferences, create inaccessible contrast, or misuse assistive-technology visibility. A requested deviation stops for governance; there is no customization shortcut.

## 21. Core-Component Customization

Preserve role, name, description, anatomy, states, keyboard/pointer/focus/error behavior, trigger relationships, and Profile compatibility. Presentation varies only inside Approved owning boundaries; no project-specific semantic variant or pending KBDL-007 recommendation is authorized.

## 22. System-Component Customization

Preserve surface meaning, modality, focus containment/restoration, dismissal, urgency/live-region meaning, progress/meter semantics, system-state honesty, recovery, data semantics, and sensitive-data boundaries. No pending KBDL-008 taxonomy, timing, sizing, placement, queueing, transformation, or interaction policy is authorized.

## 23. Project Profile Customization

Begin with the documented Profile and preserve shared architecture, invariants, locked decisions, Approved emphasis, and Profile-independent accessibility, semantics, security, and correctness. Do not create a fourth/hidden hybrid, switch Profile by viewport, treat theme as Profile, adopt pending defaults, invent migration policy, or create Profile-specific semantics. Record conflicts and determine whether the request, declaration, or pending policy needs governance.

## 24. Content and Open Brand Expression

Logo, photography, illustration, campaign graphics, voice, motifs, marketing composition, domain content, and project media are open only while preserving alternatives, reading order, comprehension, contrast, focus, motion safety, responsive behavior, performance, privacy, licensing, secure content, and honest state. Open expression cannot replace foundations or components.

## 25. Security, Privacy, Correctness, and Data Integrity

Preserve authentication, authorization, ownership, input validation, sensitive-data protection, safe disclosure, truthful saved/synchronized/queued/completed state, consequential-action safeguards, permission/not-found privacy, auditability, recovery, and rollback. Visibility is not authorization. Never expose secrets or personal data, suppress material errors, imitate trusted security indicators, hide stale/offline state, or remove audit information. Backend architecture remains out of scope.

## 26. Reusable versus Project-Local Customization

Project-local choices remain bounded to one project. Repeated or intended multi-project use triggers a proposal: confirm the gap; assess cross-Profile and cross-module impact; create a non-Approved proposal and stable ID where appropriate; add traceability; seek project-owner approval; then update owning modules. Copying records silently is prohibited; the exact reuse threshold remains Recommended.

## 27. Conflict Handling and Exceptions

Customization yields, in order, to safety/data integrity, accessibility, user task/comprehension, Approved KBDL requirements, content hierarchy, responsive constraints, performance, and Profile. An exception request records affected rule, reason, alternatives, scope, duration, owner, approving decision, all impacts, validation/evidence, rollback, expiry, and review. No actual exception is created here.

## 28. Conforming Examples

Examples are documentation-only and `Not verified`.

| Project / Profile | Request and class | Source / lifecycle authority | Documentation / approval | Validation / rollback | Why conforming |
| --- | --- | --- | --- | --- | --- |
| Gallery / Showcase | Select an Approved accent, A | FND/THM Approved role and bound | Record mapping; local responsible review | Contrast/parity; restore prior accent | Existing Approved option, no lifecycle change |
| Analytics / Precision | Select a typeface already permitted by the Approved typeface model, A | Approved FND model | Record exact source and selection; local review | Legibility/hierarchy; restore prior typeface | Does not invent or resolve an unapproved typeface |
| Retail / Flow | Project photography and illustration, B | PRN open expression plus Approved accessibility rules | Asset, owner, licensing, alternatives; content/accessibility review | Alternatives, contrast, responsive media, performance; replace asset | Open expression remains subordinate |
| Gallery / Showcase | Map brand color through an Approved theme override, A | THM-014 Approved boundaries | Role mapping and exclusions; local review | Light/dark, contrast, focus/status; restore mapping | Preserves semantic-role architecture |
| Gallery / Showcase | Use upper permitted motion emphasis, A | Approved MOT hierarchy/bounds | Record purpose and reduced-motion constraint; local review | Purpose, reduced/no-motion, input/performance; restore prior emphasis | Stays inside Approved architecture |
| Analytics / Precision | Request denser presentation without adopting pending exact density values, C | Approved content-priority rules; no exact-value authority | Non-Approved request with pending status; applicable authority review | Plan reflow/zoom/order tests; abandon request | Correctly withholds implementation authority |
| Service / Flow | Adapt content tone, B | Open content expression plus PRO-022 | Voice guidance and affected content; content review | Comprehension, errors, privacy; restore prior copy | Meaning and state honesty remain intact |
| Analytics / Precision | Restyle a Button inside Approved roles, A | Approved CMP semantics plus FND/THM bounds | Record presentation-only scope; local review | Name, keyboard, focus, states; restore style | Anatomy and semantics do not change |
| Service / Flow | One-project media treatment, B project-local | Open expression and Approved media constraints | Complete local record; local compliance review | Accessibility/performance/privacy; remove treatment | Scope is bounded to one project |
| Two projects / all Profiles | Repeated local pattern proposed for reuse, D | No current authority | KBDL proposal, impact, traceability, packet; project-owner review | Evidence may inform review; remove local copies | Reuse is escalated, not copied silently |
| Hypothetical / declared Profile | Temporary deviation after a separately Approved exception, E | Exact governance decision only | Exception scope, duration, mitigations, decision; authorized review | Focused tests and expiry monitoring; tested restoration | Authority is explicit and temporary; this module creates no exception |
| Gallery / Showcase | Existing selection becomes stale after source supersession, A pending re-review | Former source no longer sufficient | Mark stale, stop expansion, review replacement | Revalidate replacement; restore Approved baseline | Source change invalidates silent continuation |

## 29. Non-Conforming Examples

| Request | Violated requirement / risk | Correct class | Required correction or escalation |
| --- | --- | --- | --- |
| Treat a pending breakpoint as locally Approved | CUS-002/016; false authority and reflow risk | C | Keep non-Approved and seek owning approval |
| Add a project semantic color role | CUS-013/014; semantic fragmentation | D | Propose a reusable KBDL extension |
| Remove focus styling for branding | CUS-017; keyboard access failure | F | Reject and preserve visible focus |
| Invent a project-only Button meaning | CUS-018; semantic inconsistency | D/E | Use existing semantics or govern a proposal/exception |
| Use Tooltip as accessible name | CUS-018; name unavailable before hover/focus | F | Provide persistent programmatic naming |
| Create a hidden hybrid Profile | CUS-020; Profile fragmentation | C/D | Preserve declaration; route any policy proposal through KBDL-009 governance |
| Treat dark mode as Profile customization | CUS-020; concept conflation | F | Keep theme mode independent of Profile |
| Reduce target size below the baseline | CUS-017; motor-access barrier | F | Preserve Approved accessibility requirement |
| Adopt a pending Card variant | CUS-019; promotes CMP-067 | C | Keep non-Approved pending owning decision |
| Create a custom toast queue policy | CUS-019; promotes pending policy | C/D | Escalate to owning component governance |
| Hide an error to reduce visual noise | CUS-021; false state and recovery loss | F | Preserve honest error and recovery communication |
| Copy a local pattern to multiple projects | CUS-006; uncontrolled divergence | D | Create a KBDL proposal before reuse |
| Write the record after implementation | CUS-001/008/022; retroactive authority | F | Stop, assess, record, and obtain authority before proceeding |
| Mark technical validation as Approved | CUS-002/010; lifecycle/validation conflation | F | Record validation separately; obtain lifecycle authority |
| Omit rollback | CUS-010/012; unrecoverable change | F | Define and review rollback before handoff |
| Keep an expired exception active | CUS-007/012; unauthorized deviation | E | Stop implementation and renew through governance or roll back |
| Use automation that silently mutates values | CUS-001/022; unauditable change | F | Reject; any future tooling requires separately authorized scope |

## 30. Normative KBDL-CUS Requirements

Each record below has one authoritative normative location identified by its Specification location. `Not verified` means implementation evidence does not exist.

- **`KBDL-CUS-001` — Manual, documented customization.** Every customization **must** be manually chosen, documented, attributable, reviewable, reversible, and subordinate to higher-priority requirements; silent or automated mutation **must not** grant authority.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: `KBDL-DEC-004` plus the mandatory KBDL-010 prompt.
  - Related requirements: `KBDL-PRN-005`, `KBDL-GOV-003`. Applicable Profiles: Showcase, Precision, Flow. Customization class: A–F.
  - Specification location: [§1](#1-purpose-and-scope). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Record and implementation audit. Known limitation: No project customization exists to test.

- **`KBDL-CUS-002` — Authority separation.** A request, record, CUS ID, local preference, prototype, or successful implementation **must not** create lifecycle authority or promote non-Approved material.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: KBDL lifecycle conventions and mandatory KBDL-010 prompt.
  - Related requirements: `KBDL-GOV-003`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§5](#5-customization-authority-model). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Authority-source audit. Known limitation: Project records are not available.

- **`KBDL-CUS-003` — Exact primary classification.** Every request **must** receive exactly one primary Class A–F classification before implementation.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Mandatory KBDL-010 classification model.
  - Related requirements: `KBDL-CUS-002`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§6](#6-locked-controlled-open-proposed-and-exception-classifications). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Classification review. Known limitation: Classification has not been applied to a real request.

- **`KBDL-CUS-004` — Approved selection integrity.** Class A **must** remain inside explicit Approved bounds, be Profile-compatible and dependency-independent, and **must not** alter KBDL lifecycle status.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Mandatory KBDL-010 Class A rule and owning-module lifecycle rules.
  - Related requirements: `KBDL-CUS-002`, `KBDL-PRO-004`. Applicable Profiles: all. Customization class: A.
  - Specification location: [§12](#12-approval-and-escalation-paths). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Source-bound comparison. Known limitation: Implementation choices are project-specific.

- **`KBDL-CUS-005` — Open-expression integrity.** Class B expression **must** remain subordinate to every locked and Approved rule and document material or reusable choices.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: `KBDL-PRN-005`, `KBDL-PRO-005`, and mandatory KBDL-010 prompt.
  - Related requirements: `KBDL-PRN-005`, `KBDL-PRO-005`. Applicable Profiles: all. Customization class: B.
  - Specification location: [§24](#24-content-and-open-brand-expression). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Content and locked-rule audit. Known limitation: Actual assets require project review.

- **`KBDL-CUS-006` — Proposal and extension integrity.** Class C choices **must** remain non-Approved; Class D reusable choices **must** use KBDL proposal, impact, traceability, and project-owner approval rather than silent copying.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: KBDL governance plus mandatory KBDL-010 Classes C and D.
  - Related requirements: `KBDL-GOV-003`. Applicable Profiles: all. Customization class: C, D.
  - Specification location: [§26](#26-reusable-versus-project-local-customization). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Proposal-history audit. Known limitation: Exact reuse threshold is Recommended.

- **`KBDL-CUS-007` — Exception and prohibition integrity.** Class E requests **must** stop until an Approved exception decision exists; Class F safety-, accessibility-, security-, correctness-, integrity-, or documentation-weakening requests **must not** proceed.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: `KBDL-GOV-002`, governance exception process, and mandatory KBDL-010 Classes E/F.
  - Related requirements: `KBDL-GOV-002`, `KBDL-GOV-003`. Applicable Profiles: all. Customization class: E, F.
  - Specification location: [§27](#27-conflict-handling-and-exceptions). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Exception/stop-path audit. Known limitation: No exception is created here.

- **`KBDL-CUS-008` — Workflow completeness.** A customization **must** follow the request-to-retirement workflow in §7 and confirm authority before implementation.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Mandatory KBDL-010 workflow.
  - Related requirements: `KBDL-CUS-002`, `003`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§7](#7-manual-customization-workflow). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Workflow-stage audit. Known limitation: No real workflow history exists.

- **`KBDL-CUS-009` — Intake completeness.** Intake **must** capture the applicable identity, outcome, ownership, scope, impact, dependency, duration, reuse, rollback, and uncertainty information in §8.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Mandatory KBDL-010 intake fields.
  - Related requirements: `KBDL-CUS-008`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§8](#8-customization-request-intake). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Intake-field audit. Known limitation: Inapplicable fields require project rationale.

- **`KBDL-CUS-010` — Record completeness and status separation.** Every record **must** contain the fields in §11 and keep source lifecycle, workflow state, approval authority, and validation status distinct.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: `KBDL-DEC-004`, conventions, and mandatory KBDL-010 record fields.
  - Related requirements: `KBDL-CUS-001`, `002`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§11](#11-customization-record). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Programmatic field audit plus manual status review. Known limitation: No machine-readable format is mandated.

- **`KBDL-CUS-011` — Impact and evidence planning.** Every request **must** assess all applicable impacts and define observable validation, evidence, limitations, and rollback without claiming implementation verification from documentation review.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Mandatory KBDL-010 impact and evidence clauses.
  - Related requirements: `KBDL-CUS-008`, `010`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§10](#10-impact-assessment), [§14](#14-validation-and-evidence-planning). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Impact/evidence plan audit. Known limitation: Final KBDL validation remains later scope.

- **`KBDL-CUS-012` — Review and rollback.** Records **must** be reviewed when source or Profile authority changes, preserve history, prevent expired authority from surviving, and record rollback outcomes.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Mandatory KBDL-010 change and rollback clauses.
  - Related requirements: `KBDL-CUS-010`. Applicable Profiles: all. Customization class: A–E.
  - Specification location: [§15](#15-review-expiry-change-and-rollback). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Record-history and rollback audit. Known limitation: Exact cadence/expiry are Recommended.

- **`KBDL-CUS-013` — Foundation preservation.** Foundation customization **must** preserve Approved roles, scales, values, hierarchy, contrast, responsive priority, state clarity, and Profile invariants; this module authorizes no new exact value.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Approved foundation requirements plus mandatory KBDL-010 boundary.
  - Related requirements: `KBDL-FND-001`–`012`, `KBDL-PRO-001`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§16](#16-foundations-customization). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Foundation-role/value audit. Known limitation: Project implementation absent.

- **`KBDL-CUS-014` — Theme preservation.** Theme customization **must** preserve semantic roles, parity, preference precedence, focus/contrast/status meaning, local contexts, documentation, and cross-Profile compatibility within Approved override boundaries.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Approved `KBDL-THM-003`, `005`, `006`, `013`, `014` plus mandatory KBDL-010 boundary.
  - Related requirements: `KBDL-THM-003`, `005`, `006`, `013`, `014`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§17](#17-theme-customization). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Theme-role and parity audit. Known limitation: Pending theme items remain excluded.

- **`KBDL-CUS-015` — Motion preservation.** Motion customization **must** preserve Approved purpose, hierarchy, timing/easing architecture, safety, reduced/no-motion parity, interaction, performance, and shared architecture.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Approved motion requirements plus mandatory KBDL-010 boundary.
  - Related requirements: `KBDL-MOT-001`–`034`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§18](#18-motion-customization). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Motion architecture/safety audit. Known limitation: Exact component values and technology remain excluded.

- **`KBDL-CUS-016` — Responsive preservation.** Customization **must** preserve content priority, source/focus order, reflow, resizing, orientation, safe-area/keyboard access, input parity, semantics, and recovery without promoting pending exact policies.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Approved responsive requirements plus mandatory KBDL-010 boundary.
  - Related requirements: `KBDL-RSP-001`, `006`, `007`, `009`, `010`, `012`–`022`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§19](#19-responsive-customization). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Responsive outcome audit. Known limitation: Pending exact values remain excluded.

- **`KBDL-CUS-017` — Accessibility floor.** Customization **must not** weaken the Approved accessibility baseline or create an accessibility-by-customization exception path.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: `KBDL-GOV-002`, Approved accessibility requirements, and mandatory KBDL-010 boundary.
  - Related requirements: `KBDL-GOV-002`, `KBDL-A11Y-001`–`040`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§20](#20-accessibility-customization-boundary). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: WCAG/requirement audit. Known limitation: Implementation testing is absent.

- **`KBDL-CUS-018` — Core-component preservation.** Customization **must** preserve core-component role, name, description, anatomy, states, input/focus/error behavior, relationships, and Profile compatibility.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Approved KBDL-007 requirements plus mandatory KBDL-010 boundary.
  - Related requirements: `KBDL-CMP-001`–`051`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§21](#21-core-component-customization). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Component-contract audit. Known limitation: Pending KBDL-007 items remain excluded.

- **`KBDL-CUS-019` — System-component preservation.** Customization **must** preserve surface, modality, focus, dismissal, status, state, recovery, data, and sensitive-information contracts.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Approved KBDL-008 requirements plus mandatory KBDL-010 boundary.
  - Related requirements: `KBDL-CMP-052`–`111`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§22](#22-system-component-customization). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: System-component contract audit. Known limitation: Pending KBDL-008 items remain excluded.

- **`KBDL-CUS-020` — Profile invariants.** Customization **must** begin from the declared Profile and preserve shared architecture, invariants, locked decisions, Approved emphasis, and Profile-independent accessibility, semantics, security, and correctness.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Approved `KBDL-PRO-001`–`008`, `010`–`015`, `019`–`026` plus mandatory KBDL-010 boundary.
  - Related requirements: `KBDL-PRO-001`–`029`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§23](#23-project-profile-customization). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Profile-invariant audit. Known limitation: Pending KBDL-009 policies remain excluded.

- **`KBDL-CUS-021` — Security and correctness preservation.** Customization **must** preserve authentication, authorization, ownership, validation, privacy, safe disclosure, truthful state, safeguards, auditability, recovery, and rollback.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Prior Approved security/correctness requirements plus mandatory KBDL-010 boundary.
  - Related requirements: `KBDL-PRO-023`, `KBDL-CMP-103`, `104`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§25](#25-security-privacy-correctness-and-data-integrity). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Security/privacy/correctness review. Known limitation: Backend architecture is out of scope.

- **`KBDL-CUS-022` — Scope and handoff control.** Implementation **must not** begin until authority, scope, exclusions, constraints, dependencies, evidence, and rollback are recorded, and local technology choices **must not** be represented as KBDL policy.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation status: Not verified.
  - Authority: Mandatory KBDL-010 handoff and scope clauses.
  - Related requirements: `KBDL-CUS-002`, `008`, `010`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§13](#13-implementation-handoff-boundary). Decision-packet destination: None — Approved. Pending dependencies: None.
  - Validation method: Handoff-record and artifact audit. Known limitation: No implementation handoff exists.

- **`KBDL-CUS-023` — Record identifier policy.** Adopt a stable project customization-record identifier format.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a CUS ID does not grant implementation authority.
  - Related requirements: `KBDL-CUS-010`. Applicable Profiles: all. Customization class: A–E.
  - Specification location: [§11](#11-customization-record). Decision-packet destination: Approval-ready item 1. Pending dependencies: None.
  - Validation method: Project-owner review. Known limitation: Records use a visible placeholder meanwhile.

- **`KBDL-CUS-024` — Local approval roles.** Adopt exact project-level owner, approver, and independent-reviewer responsibilities.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a CUS ID does not grant implementation authority.
  - Related requirements: `KBDL-CUS-010`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§12](#12-approval-and-escalation-paths). Decision-packet destination: Approval-ready item 2. Pending dependencies: None.
  - Validation method: Project-owner review. Known limitation: Current governance does not define exact local roles.

- **`KBDL-CUS-025` — Risk-tier evidence policy.** Adopt customization risk tiers, minor/material thresholds, evidence expectations by tier, and any independent-review trigger based on material classification.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a CUS ID does not grant implementation authority.
  - Related requirements: `KBDL-CUS-011`. Applicable Profiles: all. Customization class: A–F.
  - Specification location: [§14](#14-validation-and-evidence-planning). Decision-packet destination: Approval-ready item 3. Pending dependencies: None.
  - Validation method: Project-owner review. Known limitation: Final validation policy remains later scope.

- **`KBDL-CUS-026` — Review, expiry, and renewal policy.** Adopt default cadence, expiry, stale-record handling, and exception-renewal rules.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a CUS ID does not grant implementation authority.
  - Related requirements: `KBDL-CUS-012`. Applicable Profiles: all. Customization class: A–E.
  - Specification location: [§15](#15-review-expiry-change-and-rollback). Decision-packet destination: Approval-ready item 4. Pending dependencies: None.
  - Validation method: Project-owner review. Known limitation: No default time period is authorized.

- **`KBDL-CUS-027` — Multiple-record precedence.** Adopt inheritance depth and override precedence for multiple project records.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a CUS ID does not grant implementation authority.
  - Related requirements: `KBDL-CUS-010`, `012`. Applicable Profiles: all. Customization class: A–E.
  - Specification location: [§15](#15-review-expiry-change-and-rollback). Decision-packet destination: Approval-ready item 5. Pending dependencies: None.
  - Validation method: Project-owner review. Known limitation: Conflicts stop under current rules.

- **`KBDL-CUS-028` — Reuse and promotion threshold.** Adopt the threshold and detailed process for escalating repeated project-local customization into KBDL.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a CUS ID does not grant implementation authority.
  - Related requirements: `KBDL-CUS-006`. Applicable Profiles: all. Customization class: C, D.
  - Specification location: [§26](#26-reusable-versus-project-local-customization). Decision-packet destination: Approval-ready item 6. Pending dependencies: None.
  - Validation method: Project-owner review. Known limitation: Reuse always triggers review until a threshold is approved.

- **`KBDL-CUS-029` — Archive, licensing, and rollback evidence policy.** Adopt archive retention, required asset-licensing review, and default rollback-evidence rules.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — pending explicit project-owner approval; assignment of a CUS ID does not grant implementation authority.
  - Related requirements: `KBDL-CUS-005`, `010`, `012`. Applicable Profiles: all. Customization class: A–E.
  - Specification location: [§15](#15-review-expiry-change-and-rollback), [§24](#24-content-and-open-brand-expression). Decision-packet destination: Approval-ready item 7. Pending dependencies: None.
  - Validation method: Project-owner review. Known limitation: Exact retention and evidence rules are not authorized.

- **`KBDL-CUS-030` — Machine-readable customization format.** A future machine-readable record or tooling format may be proposed only in a later authorized scope.
  - Lifecycle status: Deferred. Provenance: Assumed. Validation status: Not applicable.
  - Authority: Not applicable — deliberately deferred; assignment of a CUS ID does not grant implementation authority.
  - Related requirements: `KBDL-CUS-010`, `022`. Applicable Profiles: all. Customization class: A–E.
  - Specification location: [§41](#41-deferred-and-unresolved-items). Decision-packet destination: Deferred tracking. Pending dependencies: Later implementation/tooling authorization.
  - Validation method: Not applicable until resumed. Known limitation: No JSON, YAML, schema, API, plugin, or automation is authorized.

## 31. Requirement Coverage Matrix

All Profiles means Showcase, Precision, and Flow. `Prompt` authority means an explicit mandatory clause of the approved KBDL-010 prompt; exact authority remains in each record above.

| ID | Title | Category | Class | Lifecycle | Provenance | Validation | Authority | Profiles | Modules | Related | Location | Packet | Dependency | Validation method | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CUS-001 | Manual/documented | Governance | A–F | Approved | Confirmed | Not verified | DEC-004 + Prompt | All | GOV/PRN | PRN-005/GOV-003 | §1 | None | None | Record audit | No project record |
| CUS-002 | Authority separation | Lifecycle | A–F | Approved | Confirmed | Not verified | Conventions + Prompt | All | GOV | GOV-003 | §5 | None | None | Authority audit | No project record |
| CUS-003 | Primary classification | Classification | A–F | Approved | Confirmed | Not verified | Prompt | All | CUS | CUS-002 | §6 | None | None | Class audit | No real request |
| CUS-004 | Approved selection | Authority | A | Approved | Confirmed | Not verified | Prompt + owners | All | All | CUS-002/PRO-004 | §12 | None | None | Bounds audit | Project-specific |
| CUS-005 | Open expression | Content | B | Approved | Confirmed | Not verified | PRN-005/PRO-005/Prompt | All | PRN/PRO | PRN-005/PRO-005 | §24 | None | None | Content audit | Assets absent |
| CUS-006 | Proposal/extension | Governance | C/D | Approved | Confirmed | Not verified | GOV + Prompt | All | GOV | GOV-003 | §26 | None | None | Proposal audit | Reuse threshold pending |
| CUS-007 | Exception/prohibition | Safety | E/F | Approved | Confirmed | Not verified | GOV-002 + Prompt | All | GOV | GOV-002/003 | §27 | None | None | Stop-path audit | No exception |
| CUS-008 | Workflow | Process | A–F | Approved | Confirmed | Not verified | Prompt | All | All | CUS-002/003 | §7 | None | None | Workflow audit | No history |
| CUS-009 | Intake | Process | A–F | Approved | Confirmed | Not verified | Prompt | All | All | CUS-008 | §8 | None | None | Field audit | Conditional fields |
| CUS-010 | Record/status | Documentation | A–F | Approved | Confirmed | Not verified | DEC-004 + Prompt | All | All | CUS-001/002 | §11 | None | None | Field/status audit | No format mandated |
| CUS-011 | Impact/evidence | Validation | A–F | Approved | Confirmed | Not verified | Prompt | All | All | CUS-008/010 | §10/§14 | None | None | Plan audit | Final VAL later |
| CUS-012 | Review/rollback | Change | A–E | Approved | Confirmed | Not verified | Prompt | All | GOV | CUS-010 | §15 | None | None | History audit | Cadence pending |
| CUS-013 | Foundations | Boundary | A–F | Approved | Confirmed | Not verified | FND + Prompt | All | FND | FND-001–012 | §16 | None | None | Value audit | No implementation |
| CUS-014 | Themes | Boundary | A–F | Approved | Confirmed | Not verified | THM + Prompt | All | THM | THM-003/005/006/013/014 | §17 | None | None | Theme audit | Pending items excluded |
| CUS-015 | Motion | Boundary | A–F | Approved | Confirmed | Not verified | MOT + Prompt | All | MOT | MOT-001–034 | §18 | None | None | Motion audit | Exact values excluded |
| CUS-016 | Responsive | Boundary | A–F | Approved | Confirmed | Not verified | RSP + Prompt | All | RSP | Approved RSP | §19 | None | None | Outcome audit | Exact policies excluded |
| CUS-017 | Accessibility | Boundary | A–F | Approved | Confirmed | Not verified | GOV/A11Y + Prompt | All | A11Y | GOV-002/A11Y-001–040 | §20 | None | None | WCAG audit | Testing absent |
| CUS-018 | Core components | Boundary | A–F | Approved | Confirmed | Not verified | CMP + Prompt | All | CMP | CMP-001–051 | §21 | None | None | Contract audit | Pending 007 excluded |
| CUS-019 | System components | Boundary | A–F | Approved | Confirmed | Not verified | CMP + Prompt | All | CMP | CMP-052–111 | §22 | None | None | Contract audit | Pending 008 excluded |
| CUS-020 | Profiles | Boundary | A–F | Approved | Confirmed | Not verified | PRO + Prompt | All | PRO | PRO-001–029 | §23 | None | None | Invariant audit | Pending 009 excluded |
| CUS-021 | Security/correctness | Safety | A–F | Approved | Confirmed | Not verified | Prior + Prompt | All | CMP/PRO | PRO-023/CMP-103/104 | §25 | None | None | Security audit | Backend out of scope |
| CUS-022 | Handoff/scope | Scope | A–F | Approved | Confirmed | Not verified | Prompt | All | CUS | CUS-002/008/010 | §13 | None | None | Handoff audit | No handoff |
| CUS-023 | Identifier policy | Policy | A–E | Recommended | Assumed | Not applicable | N/A | All | CUS | CUS-010 | §11 | Ready 1 | None | Owner review | Placeholder meanwhile |
| CUS-024 | Local roles | Policy | A–F | Recommended | Assumed | Not applicable | N/A | All | GOV/CUS | CUS-010 | §12 | Ready 2 | None | Owner review | Roles undefined |
| CUS-025 | Risk/evidence tiers | Policy | A–F | Recommended | Assumed | Not applicable | N/A | All | CUS/VAL | CUS-011 | §14 | Ready 3 | None | Owner review | Final VAL later |
| CUS-026 | Cadence/expiry | Policy | A–E | Recommended | Assumed | Not applicable | N/A | All | GOV/CUS | CUS-012 | §15 | Ready 4 | None | Owner review | No time value |
| CUS-027 | Record precedence | Policy | A–E | Recommended | Assumed | Not applicable | N/A | All | CUS | CUS-010/012 | §15 | Ready 5 | None | Owner review | Conflicts stop |
| CUS-028 | Reuse threshold | Policy | C/D | Recommended | Assumed | Not applicable | N/A | All | GOV/CUS | CUS-006 | §26 | Ready 6 | None | Owner review | Review always |
| CUS-029 | Archive/licensing/rollback | Policy | A–E | Recommended | Assumed | Not applicable | N/A | All | GOV/CUS | CUS-005/010/012 | §15/§24 | Ready 7 | None | Owner review | Exact rules absent |
| CUS-030 | Machine format | Tooling | A–E | Deferred | Assumed | Not applicable | N/A | All | Future | CUS-010/022 | §41 | Deferred | Later authorization | Not applicable | No tooling authorized |

## 32. Customization-Classification Matrix

| Class | Definition / typical request | Authority | Documentation / approval | Implementation / validation | Traceability / decision / rollback | Prohibited misuse |
| --- | --- | --- | --- | --- | --- | --- |
| A | Existing Approved option, such as an Approved accent | Owning Approved rule | Record; local responsible review | Eligible, then separately validate | Source IDs; no KBDL decision; rollback selection | Treating selection as lifecycle change |
| B | Open brand expression, such as photography | Open area plus locked rules | Material/reusable choice; compliance review | Eligible, then impact validation | Constraints and assets; proposal if reusable; rollback asset | Replacing KBDL architecture |
| C | New local controlled option | None until reviewed | Non-Approved record; applicable authority | Ineligible before authority | Proposal/dependency; decision if approved; rollback draft | Calling local approval KBDL approval |
| D | Reusable KBDL extension | None until KBDL approval | KBDL proposal, impact, traceability, packet | Ineligible before approval | Requirement and decision on approval; rollback local copies | Silent cross-project copying |
| E | Locked/Approved exception | Approved exception decision only | Governance exception record | Ineligible before decision; validate exact scope | Decision register; expiry and rollback | Hidden or perpetual deviation |
| F | Safety/accessibility/security/integrity violation | None | Stop and record rejection/correction | Prohibited | Trace affected rules; no approval path that weakens floor | Proceeding for aesthetics or urgency |

## 33. Cross-Module Customization Matrix

| Module | Locked / Approved controlled / open | Pending items | Prohibited | Path / validation / limitation |
| --- | --- | --- | --- | --- |
| Governance | hierarchy/exception process; documented selection | Local role details | Local lifecycle promotion | GOV process; decision audit; local roles pending |
| Principles | identity/locked rules; bounded variables; brand expression | None | Semantic/identity fragmentation | Hierarchy audit |
| Foundations | roles/scales/Approved options; imagery | No unapproved exact values | New scale/value | Owner bounds + value/contrast audit |
| Themes | semantic roles/parity/Approved overrides | Opacity, translucency, forced-colors, palettes, sync/formats | New theme architecture | THM bounds + parity audit |
| Motion | purpose/hierarchy/safety/Approved timing/easing | Exact component values, technology, detection, thresholds | New motion system/safety weakening | MOT bounds + reduced-motion audit |
| Responsive | Approved outcomes | Nine KBDL-006 items as applicable | Local promotion of exact policies | Outcome audit; implementation-specific choices not KBDL policy |
| Accessibility | WCAG 2.2 AA and Approved requirements | A11Y-011/021/035 | Any weakening | Stop/exception governance; implementation testing absent |
| Core components | semantics/anatomy/Approved behavior | Ten KBDL-007 items | Project semantic variants | Contract audit |
| System components | state/modality/recovery/Approved behavior | Seventeen KBDL-008 items | Project taxonomy/interaction policy | Contract audit |
| Project Profiles | shared architecture/invariants/Approved emphasis | Seven KBDL-009 items | Hidden/fourth/hybrid Profile | Declaration/invariant audit |
| Content/open expression | accessibility-safe project assets/voice | Licensing policy details | Misleading/inaccessible/unsafe content | Asset/content review |
| Security/privacy/correctness | Approved safeguards | Backend design out of scope | Access/state/privacy weakening | Security review; no backend prescription |
| Future validation | Evidence planning only | Final validation policy | Claiming production conformance | Later VAL module remains locked |

## 34. Customization-Record Completeness Matrix

| Fields | Purpose | Required / source | Validation | Example | Common failure |
| --- | --- | --- | --- | --- | --- |
| Title, project, Profile, identifier/placeholder | Identity | Required / intake | Nonempty and Profile resolves | “Acme accent” | Missing project/Profile |
| Requestor, owner, reviewer, proposed date | Accountability | Required / project | Named/date audit | Named roles | Self-approval ambiguity |
| Workflow status, class, outcome, rationale | State/intent | Required / request | Status/class audit | Awaiting approval, A | Lifecycle conflation |
| Affected modules/requirements, source lifecycle, authority, dependencies | Authority | Required / KBDL sources | ID/status/source audit | THM-014 Approved | Pending item omitted |
| Exact scope, exclusions, selected choices | Boundary | Required / approval | Bounds comparison | Accent role only | Broad implicit scope |
| Accessibility/responsive/theme/foundation/motion/component/Profile/content impacts | Design impact | Required or reason inapplicable / assessment | Per-impact review | Contrast test planned | “No impact” unsupported |
| Security/privacy/correctness/data-integrity/performance impacts | Risk impact | Required or reason inapplicable / assessment | Specialist review as needed | State honesty preserved | Privacy omitted |
| Implementation constraints | Handoff | Required / authority | Constraint trace | Preserve role mapping | Technology treated as policy |
| Validation method, evidence, validation status, limitations | Evidence honesty | Required / plan/results | Method-result audit | Not verified | Approval treated as verification |
| Rollback, scope, duration, review/expiry | Reversibility | Required; duration conditional / record | Rollback and date audit | Restore prior mapping | No rollback |
| Superseded record, related decision | History | Conditional / governance | Link resolution | CUS-local-previous | Orphan record |
| Change history, final disposition | Audit trail | Required / owner | Chronology audit | Rolled back | Silent mutation |

## 35. Approval-Path Matrix

| Class | Local documentation/review | Owner approval / decision register | Lifecycle change | Blocker | Implementation / validation eligibility |
| --- | --- | --- | --- | --- | --- |
| A | Required / exact local role pending | No KBDL approval; no decision | None | Source dependency | Eligible inside Approved bounds / then validate |
| B | Material/reusable / compliance review | No KBDL approval unless extension; decision if governed | None | Locked-rule conflict | Eligible if compliant / then validate |
| C | Required / role pending | Applicable authority; KBDL owner if KBDL lifecycle changes | Only through governance | Missing Approved option | Not eligible before authority / planning allowed |
| D | Proposal and traceability | Project owner; decision register upon approval | Recommended→Approved only by decision | Proposal approval | Not eligible before approval / evidence may inform review only |
| E | Exception record | Project owner/authorized governance; decision required | Underlying rule unchanged | Approved exception absent | Not eligible before decision / validate exact exception |
| F | Rejection/correction record | No weakening approval path | None | Prohibited nature | Never eligible as requested |

## 36. Validation and Evidence Matrix

| Change | Minimum evidence plan | Validation status boundary | Rollback evidence |
| --- | --- | --- | --- |
| Documentation-only selection | Source/bounds and record review | Selection may be authorized; implementation remains Not verified | Prior selection/restoration steps |
| Theme/foundation | Role mapping, light/dark, contrast, hierarchy | Real implementation required | Before/after role mapping |
| Motion | Purpose, timing/easing, reduced/no-motion, input/performance | Real interaction required | Disable/restore motion choice |
| Responsive | Reflow, zoom, orientation, inputs, order, real viewport/device | Real implementation required | Prior layout choice |
| Component | Semantics, name, keyboard/pointer/focus/state/error | Browser/assistive testing required | Prior component mapping |
| Accessibility-impacting | Applicable WCAG methods and assistive technology | Documentation alone insufficient | Accessible baseline restored |
| Security-impacting | Threat/authorization/privacy/state review without secrets | Specialist implementation evidence | Safe state and access restored |
| Temporary exception | Decision scope, mitigations, expiry, focused testing | Only exact Approved scope eligible | Tested automatic/manual restoration |
| Reusable customization | Cross-profile/module evidence and proposal | No authority before KBDL approval | Remove local copies |
| Rollback | Trigger, steps, owner, data/state impact, success criteria | Failed/incomplete rollback recorded honestly | Execution record and residual risk |

## 37. KBDL-010 Decision Packet

All seven items are `Recommended`, `Assumed`, `Not applicable` for validation, independently approval-ready, and grant no implementation authority. Common explicit exclusions: no earlier recommendation, exception, project customization, technology, machine-readable format, or final-validation policy is approved. Common impacts: accessibility and security benefit from accountability; responsive, theme/foundation, motion, component, and Profile architecture remain unchanged; performance impact is documentation overhead only.

### Item 1 — Record identifier format

- **Decision / recommendation:** Whether to adopt a stable human-readable project customization identifier; recommend project namespace plus monotonic local number, with exact syntax chosen on approval.
- **Rationale / alternatives / trade-offs:** Stable linkage and supersession; alternatives are free-text titles or global numbering; adds administration.
- **Accessibility / responsive / theme-foundation / motion / component / Profile impacts:** No behavior change; improves evidence association.
- **Security, privacy, correctness / performance:** Identifier must contain no personal or secret data; minor record overhead.
- **Dependencies / affected requirements:** None; `KBDL-CUS-023`.
- **Approval scope / exclusions:** Identifier policy only; excludes schemas, generators, registries, and retroactive approval.

### Item 2 — Local roles and independent review

- **Decision / recommendation:** Whether to define owner, approver, and independent reviewer responsibilities; recommend separation of owner/approver responsibilities and an independent reviewer for accessibility- or security-impacting customization. Any additional independent-review trigger based on material-risk classification belongs exclusively to item 3.
- **Rationale / alternatives / trade-offs:** Reduces self-approval; alternatives are one local owner or case-by-case governance; adds review cost.
- **Accessibility / responsive / theme-foundation / motion / component / Profile impacts:** Specialist review follows affected areas; no architecture changes.
- **Security, privacy, correctness / performance:** Independent review applies to security-impacting customization without requiring a risk-tier or materiality threshold; organizational overhead.
- **Dependencies / affected requirements:** None; `KBDL-CUS-024`.
- **Approval scope / exclusions:** Role responsibilities only; excludes naming specific people or granting KBDL lifecycle authority locally.

### Item 3 — Risk tiers and evidence

- **Decision / recommendation:** Whether to adopt risk tiers and minor/material thresholds; recommend impact-based tiers with evidence proportional to affected accessibility, security, semantics, and reversibility. Item 3 exclusively owns any independent-review trigger based on material classification.
- **Rationale / alternatives / trade-offs:** Consistent scrutiny; alternatives are uniform evidence or case-by-case judgment; classification overhead.
- **Accessibility / responsive / theme-foundation / motion / component / Profile impacts:** Higher-risk impacts require relevant evidence without changing requirements.
- **Security, privacy, correctness / performance:** Security/correctness impact raises scrutiny; evidence effort may increase.
- **Dependencies / affected requirements:** None for documentation policy; `KBDL-CUS-025`. Final validation remains later scope.
- **Approval scope / exclusions:** Tiering/evidence planning only; excludes production conformance and exact final-validation policy.

### Item 4 — Review, expiry, stale records, and renewal

- **Decision / recommendation:** Whether to define default cadence, expiry, stale handling, and exception renewal; recommend event-triggered review plus explicit dates for temporary authority.
- **Rationale / alternatives / trade-offs:** Prevents orphaned authority; alternatives are fixed-only or event-only review; maintenance cost.
- **Accessibility / responsive / theme-foundation / motion / component / Profile impacts:** Re-review when affected source/Profile changes; no policy promotion.
- **Security, privacy, correctness / performance:** Prevents stale safeguards; recurring administrative cost.
- **Dependencies / affected requirements:** None; `KBDL-CUS-026`.
- **Approval scope / exclusions:** Record governance only; excludes renewing any actual exception or choosing an exact period without approval.

### Item 5 — Multiple-record inheritance and precedence

- **Decision / recommendation:** Whether to define inheritance depth and precedence; recommend no implicit inheritance and explicit conflict resolution by higher authority then later explicitly superseding record.
- **Rationale / alternatives / trade-offs:** Avoids hidden overrides; alternatives are stacking order or unlimited inheritance; requires consolidation.
- **Accessibility / responsive / theme-foundation / motion / component / Profile impacts:** Higher-priority requirements always win; no architecture changes.
- **Security, privacy, correctness / performance:** Prevents stale/conflicting controls; may add review work.
- **Dependencies / affected requirements:** None; `KBDL-CUS-027`.
- **Approval scope / exclusions:** Record precedence only; excludes implementation token cascade or configuration layering.

### Item 6 — Reuse threshold and promotion details

- **Decision / recommendation:** Whether to define when repeated local work becomes a KBDL proposal; recommend escalation on intended second-project use or explicit reusable intent.
- **Rationale / alternatives / trade-offs:** Prevents silent fragmentation; alternatives are numeric thresholds or discretionary review; may escalate early.
- **Accessibility / responsive / theme-foundation / motion / component / Profile impacts:** Full cross-module/profile assessment required; no pending option becomes Approved.
- **Security, privacy, correctness / performance:** Shared risks reviewed; proposal overhead.
- **Dependencies / affected requirements:** None; `KBDL-CUS-028`.
- **Approval scope / exclusions:** Threshold/process details only; excludes approval of any proposed extension.

### Item 7 — Archive, licensing, and rollback evidence

- **Decision / recommendation:** Whether to define archive retention, asset-licensing review, and default rollback evidence; recommend durable linked history, licensing confirmation for external assets, and recorded rollback verification.
- **Rationale / alternatives / trade-offs:** Auditability and legal/recovery confidence; alternatives are local discretion or minimal history; storage/review cost.
- **Accessibility / responsive / theme-foundation / motion / component / Profile impacts:** Preserves evidence relevant to each impact; no architecture changes.
- **Security, privacy, correctness / performance:** Archives must minimize sensitive data; rollback evidence improves correctness; modest storage cost.
- **Dependencies / affected requirements:** None; `KBDL-CUS-029`.
- **Approval scope / exclusions:** Documentation policy only; excludes exact retention duration, legal advice, implementation backup architecture, and actual asset approval.

## 38. Approval-Ready versus Contingent Decisions

### Independently approval-ready

Items 1–7 are independently approval-ready because none requires an earlier pending requirement, later validation policy, or implementation assumption.

| Item | Affected CUS requirement | Earlier-module dependency | Other packet-item dependency | Later-validation dependency | Implementation assumption | Independence verdict | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `KBDL-CUS-023` | None | None | None | None | Independent | Identifier policy excludes schemas, generators, and implementation registries |
| 2 | `KBDL-CUS-024` | None | None | None | None | Independent | Accessibility/security triggers are direct impacts; material-risk triggers are expressly excluded and owned by item 3 |
| 3 | `KBDL-CUS-025` | None | None | None — final-validation policy expressly excluded | None | Independent | Owns risk tiers, minor/material thresholds, proportional evidence, and material-classification reviewer triggers |
| 4 | `KBDL-CUS-026` | None | None | None | None | Independent | Event-triggered record review does not require an exact earlier-module cadence |
| 5 | `KBDL-CUS-027` | None | None | None | None | Independent | Record precedence is governance-only and excludes implementation cascades |
| 6 | `KBDL-CUS-028` | None | None | None | None | Independent | Reuse threshold governs escalation only and approves no extension |
| 7 | `KBDL-CUS-029` | None | None | None | None | Independent | Archive/licensing/rollback-evidence policy excludes retention duration and implementation architecture |

```text
KBDL-010 approval-ready items: 7
Hidden cross-item dependencies: 0
Contingent KBDL-010 packet items: 0
```

### Contingent or not approval-ready

No KBDL-010 packet item is contingent. `KBDL-CUS-030` is Deferred, not a packet item: its blocker is later tooling authorization; no earlier recommendation can unblock it inside KBDL-010, and it grants no implementation authority.

## 39. Earlier-Module Lifecycle-Boundary Audits

### Foundations and themes

| Non-Approved item or policy | Reference status | Customization impact / normative use | Exact exclusion |
| --- | --- | --- | --- |
| Exact project typeface where unresolved | Context only | Choice cannot be inferred / No | No new typeface approved |
| Unverified theme opacity values | Explicitly excluded | Cannot be selected as Approved / No | Accent/scrim/selection opacity excluded |
| Translucent theme/media variants | Explicitly excluded | No local authorization / No | Opaque Approved mappings only |
| Forced-colors/high-contrast theme policy | Contingent context | Accessibility boundary / No | `KBDL-A11Y-011` remains Recommended |
| Data-visualization palettes | Explicitly excluded | No palette authority / No | Pending palette policy excluded |
| Project media composites | Context only | Class B assets still require validation / No | No composite policy approved |
| Account-level theme sync | Explicitly excluded | No synchronization policy / No | Implementation/account policy excluded |
| CSS/JSON/JS/framework token formats | Explicitly excluded | No format authority / No | Deferred implementation layer |

All Approved foundation values and theme packet decisions retain their existing lifecycle and packet history.

### Motion

| Non-Approved or Deferred item | Reference status | Customization impact / normative use | Exact exclusion |
| --- | --- | --- | --- |
| Exact component durations/distances/scales/staggers | Explicitly excluded | Cannot be locally promoted / No | Only Approved architecture applies |
| Device-performance detection | Explicitly excluded | No detection policy / No | Implementation-layer decision |
| Animation library/rendering technology | Explicitly excluded | No technology policy / No | Project technology is not KBDL authority |
| CSS/JSON/JavaScript token formats | Explicitly excluded | No format policy / No | Deferred implementation layer |
| Browser-support policy | Explicitly excluded | No support matrix / No | Later authorized scope |
| Exact scroll/hazard thresholds | Explicitly excluded | No quantitative authority / No | Safety floor remains; value unresolved |

### KBDL-006

All remain `Recommended`; normative use is **No** and each is explicitly excluded from local promotion:

- `KBDL-RSP-002` exact breakpoints; `KBDL-RSP-003` grid columns; `KBDL-RSP-004` gutters; `KBDL-RSP-005` containers; `KBDL-RSP-008` navigation collapse; `KBDL-RSP-011` data-dense transformation.
- `KBDL-A11Y-011` forced-colors policy; `KBDL-A11Y-021` enhanced target size; `KBDL-A11Y-035` accessibility test matrix.

### KBDL-007

All remain `Recommended`; normative use is **No**: `KBDL-CMP-015`, `KBDL-CMP-017`, `KBDL-CMP-020`, `KBDL-CMP-025`, `KBDL-CMP-029`, `KBDL-CMP-036`, `KBDL-CMP-041`, `KBDL-CMP-044`, `KBDL-CMP-046`, `KBDL-CMP-048`. Their button, label, group, search, combobox, action-row, navigation, breadcrumb, tabs, and pagination policies are excluded. `KBDL-CMP-041` remains contingent and not independently approval-ready.

### KBDL-008

All remain `Recommended`; normative use is **No**: `KBDL-CMP-067`, `KBDL-CMP-069`, `KBDL-CMP-073`, `KBDL-CMP-074`, `KBDL-CMP-076`, `KBDL-CMP-080`, `KBDL-CMP-083`, `KBDL-CMP-085`, `KBDL-CMP-089`, `KBDL-CMP-091`, `KBDL-CMP-099`, `KBDL-CMP-102`, `KBDL-CMP-105`, `KBDL-CMP-106`, `KBDL-CMP-108`, `KBDL-CMP-110`, `KBDL-CMP-111`. Card/accordion, tooltip/popover/menu, modal/drawer/overlay, feedback/toast, empty/recovery, carousel, responsive surface, grid/treegrid, and visualization policies are excluded.

### KBDL-009

All remain `Recommended`; normative use is **No**. Existing destinations are preserved:

| ID | Existing status | Customization impact / exact exclusion |
| --- | --- | --- |
| `KBDL-PRO-009` | Independently approval-ready | No primary/secondary/hybrid policy |
| `KBDL-PRO-017` | Independently approval-ready | No exact Precision density default |
| `KBDL-PRO-027` | Independently approval-ready | No migration policy |
| `KBDL-PRO-028` | Independently approval-ready | No selection rubric |
| `KBDL-PRO-029` | Independently approval-ready | No review cadence |
| `KBDL-PRO-016` | Contingent on `KBDL-CMP-067` | No Showcase composition default |
| `KBDL-PRO-018` | Contingent on `KBDL-CMP-015`, `036` | No Flow action default |

## 40. Decision-Packet Coverage Audit

```text
Total CUS requirements:             30
Approved:                           22
Recommended:                         7
Unresolved:                          0
Deferred:                            1
Blocked:                             0
Independently approval-ready:        7
Contingent:                          0
Unresolved tracking:                 0
Deferred tracking:                   1
```

| Non-Approved requirement | Single destination |
| --- | --- |
| `KBDL-CUS-023` | Approval-ready item 1 |
| `KBDL-CUS-024` | Approval-ready item 2 |
| `KBDL-CUS-025` | Approval-ready item 3 |
| `KBDL-CUS-026` | Approval-ready item 4 |
| `KBDL-CUS-027` | Approval-ready item 5 |
| `KBDL-CUS-028` | Approval-ready item 6 |
| `KBDL-CUS-029` | Approval-ready item 7 |
| `KBDL-CUS-030` | Deferred tracking |

No non-Approved requirement or packet item is orphaned; no Approved requirement awaits approval; no earlier dependency is hidden; no record grants approval; no contingent scope is implicit; future approval scope is explicit; and no earlier recommendation is promoted.

## 41. Deferred and Unresolved Items

Deferred and unauthorized: automated customization tooling; machine-readable schema; JSON/YAML/database formats; token generators; framework APIs; design-tool/Figma plugins; Storybook integration; CI enforcement; dashboards; automated lifecycle/dependency/Profile checking; automatic contrast/motion remediation; implementation token format; browser-support policy; final-validation policy; production conformance; and packages. Exact local roles, risk thresholds, cadence, expiry, reuse threshold, inheritance depth, archive/licensing, and rollback-evidence policies remain Recommended in items 1–7, not established fact.

## 42. Traceability

Complete per-ID traceability is maintained in [traceability-matrix.md § KBDL-010](traceability-matrix.md#kbdl-010--manual-customization). The Requirement Coverage Matrix in §31 is not treated as validation evidence. Future implementation-level validation (`VAL`) remains locked pending planning-agent validation of KBDL-010.
