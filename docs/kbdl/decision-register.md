# KBDL Decision Register

Status: `Approved` framework; individual decisions below carry their own status.

Return to the [specification index](README.md). Status labels are defined in
[conventions.md](conventions.md#1-status-labels).

## Fields

Every decision record uses these fields:

| Field | Meaning |
| --- | --- |
| Decision ID | Stable identifier, format `KBDL-DEC-###`, never reused. |
| Title | Short descriptive title. |
| Date | Date the decision was made. `Not verified` if no date is available. |
| Status | One of the labels in [conventions.md](conventions.md#1-status-labels). |
| Decision owner | Person or role with authority for this decision. `Not verified` if unknown. |
| Context | The situation that made the decision necessary. |
| Decision | The decision itself, stated plainly. |
| Rationale | Why this option was chosen. |
| Alternatives considered | Other options that were weighed, if known. |
| Trade-offs | Known costs or limitations accepted by making this decision. |
| Affected requirements | Requirement IDs affected, if any exist yet. |
| Affected modules | Module codes affected (see [conventions.md](conventions.md#2-requirement-identification)). |
| Accessibility impact | How the decision affects accessibility, or `Not applicable`. |
| Motion impact | How the decision affects motion, or `Not applicable`. |
| Responsive impact | How the decision affects responsive behavior, or `Not applicable`. |
| Implementation impact | How the decision affects implementation, or `Not applicable`. |
| Superseded decision | Decision ID this replaces, if any. |
| Review date | A future date to revisit the decision, if applicable, otherwise `Not applicable`. |

## Approved High-Level Decisions

The decisions below are recorded as `Approved` because the project owner
stated them directly in the KBDL blueprint and roadmap approval. Dates,
owners, and meeting records were not supplied and are marked `Not verified`
rather than invented, per the source-of-truth rules in this prompt.

### KBDL-DEC-001 — Project name is KBDL

- **Date:** Not verified
- **Status:** Approved
- **Decision owner:** Not verified (project owner, per user-provided context)
- **Context:** The project needed a stable name to anchor the specification, requirement IDs, and file structure.
- **Decision:** The project is named KBDL.
- **Rationale:** User-provided as part of the approved blueprint.
- **Alternatives considered:** Not verified.
- **Trade-offs:** Not applicable.
- **Affected requirements:** None yet (naming decision, not a technical requirement).
- **Affected modules:** All.
- **Accessibility impact:** Not applicable.
- **Motion impact:** Not applicable.
- **Responsive impact:** Not applicable.
- **Implementation impact:** All KBDL requirement IDs, file paths, and terminology use the `KBDL` prefix.
- **Superseded decision:** None.
- **Review date:** Not applicable.

### KBDL-DEC-002 — First deliverable is a written specification

- **Date:** Not verified
- **Status:** Approved
- **Decision owner:** Not verified (project owner)
- **Context:** KBDL requires a documented foundation before any visual or component design work begins.
- **Decision:** The first approved deliverable is a written design-language specification, delivered across a ten-step roadmap.
- **Rationale:** User-provided; ensures governance and terminology exist before design values are chosen.
- **Alternatives considered:** Not verified.
- **Trade-offs:** Delays visual and component work until the specification foundation (this prompt, KBDL-001) is in place.
- **Affected requirements:** Governs the scope of KBDL-001 through KBDL-010.
- **Affected modules:** GOV.
- **Accessibility impact:** Not applicable.
- **Motion impact:** Not applicable.
- **Responsive impact:** Not applicable.
- **Implementation impact:** No implementation code is produced until later roadmap steps.
- **Superseded decision:** None.
- **Review date:** Not applicable.

### KBDL-DEC-003 — Visual consistency is the cross-project strategy

- **Date:** Not verified
- **Status:** Approved
- **Decision owner:** Not verified (project owner)
- **Context:** KBDL must be reused across multiple, differently purposed projects.
- **Decision:** Visual consistency across projects is the primary cross-project strategy.
- **Rationale:** User-provided.
- **Alternatives considered:** Not verified.
- **Trade-offs:** Constrains how much individual projects can diverge visually; addressed through profiles and documented customization.
- **Affected requirements:** Will govern future `FND`, `THM`, and `PRO` requirements.
- **Affected modules:** FND, THM, PRO.
- **Accessibility impact:** Not applicable at this stage.
- **Motion impact:** Not applicable at this stage.
- **Responsive impact:** Not applicable at this stage.
- **Implementation impact:** Future foundation and theme requirements must not be duplicated or diverged per project without going through profiles or customization rules.
- **Superseded decision:** None.
- **Review date:** Not applicable.

### KBDL-DEC-004 — Customization is manual and documented

- **Date:** Not verified
- **Status:** Approved
- **Decision owner:** Not verified (project owner)
- **Context:** Projects will need to diverge from KBDL defaults in some cases.
- **Decision:** Customization is performed manually and must be documented, rather than automated or silent.
- **Rationale:** User-provided; keeps customization auditable and consistent with governance.
- **Alternatives considered:** Not verified.
- **Trade-offs:** Slower than automated theming; requires discipline from implementers.
- **Affected requirements:** Will govern future `CUS` requirements.
- **Affected modules:** CUS.
- **Accessibility impact:** Undocumented customization could bypass accessibility rules; documentation requirement mitigates this.
- **Motion impact:** Not applicable at this stage.
- **Responsive impact:** Not applicable at this stage.
- **Implementation impact:** Future customization guidance must include a documentation step.
- **Superseded decision:** None.
- **Review date:** Not applicable.

### KBDL-DEC-005 — Progressive-system delivery

- **Date:** Not verified
- **Status:** Approved
- **Decision owner:** Not verified (project owner)
- **Context:** The full KBDL specification is large and spans ten roadmap steps.
- **Decision:** KBDL is delivered progressively, one roadmap step at a time, without skipping ahead.
- **Rationale:** User-provided; keeps each step reviewable and prevents unapproved scope creep.
- **Alternatives considered:** Not verified.
- **Trade-offs:** Later modules remain unspecified until their step is reached.
- **Affected requirements:** Governs sequencing of all future requirements.
- **Affected modules:** GOV.
- **Accessibility impact:** Not applicable.
- **Motion impact:** Not applicable.
- **Responsive impact:** Not applicable.
- **Implementation impact:** This prompt (KBDL-001) must not populate later modules with substantive content.
- **Superseded decision:** None.
- **Review date:** Not applicable.

### KBDL-DEC-006 — Initial profiles are Showcase, Precision, and Flow

- **Date:** Not verified
- **Status:** Approved
- **Decision owner:** Not verified (project owner)
- **Context:** KBDL needs to serve multiple categories of project without fragmenting the design language.
- **Decision:** KBDL initially supports three project profiles: Showcase (portfolios/creative showcases), Precision (SaaS dashboards), and Flow (consumer-facing web applications).
- **Rationale:** User-provided.
- **Alternatives considered:** Not verified.
- **Trade-offs:** Other project categories are not yet served and would require a future profile.
- **Affected requirements:** Will govern future `PRO` requirements.
- **Affected modules:** PRO.
- **Accessibility impact:** Not applicable at this stage.
- **Motion impact:** Not applicable at this stage.
- **Responsive impact:** Not applicable at this stage.
- **Implementation impact:** Future profile requirements are scoped to these three profiles only.
- **Superseded decision:** None.
- **Review date:** Not applicable.

### KBDL-DEC-007 — Responsive web is the platform context

- **Date:** Not verified
- **Status:** Approved
- **Decision owner:** Not verified (project owner)
- **Context:** KBDL must work across device sizes without a separate native design language.
- **Decision:** KBDL targets responsive, mobile-friendly web presentation as its platform context.
- **Rationale:** User-provided.
- **Alternatives considered:** Not verified.
- **Trade-offs:** Not applicable at this stage.
- **Affected requirements:** Will govern future `RSP` requirements.
- **Affected modules:** RSP.
- **Accessibility impact:** Not applicable at this stage.
- **Motion impact:** Not applicable at this stage.
- **Responsive impact:** Defines the module's scope.
- **Implementation impact:** Not applicable at this stage.
- **Superseded decision:** None.
- **Review date:** Not applicable.

### KBDL-DEC-008 — Adaptive light and dark theme behavior

- **Date:** Not verified
- **Status:** Approved
- **Decision owner:** Not verified (project owner)
- **Context:** KBDL must present consistently regardless of the user's light/dark preference.
- **Decision:** KBDL supports adaptive light and dark presentation as a core behavior.
- **Rationale:** User-provided.
- **Alternatives considered:** Not verified.
- **Trade-offs:** Not applicable at this stage.
- **Affected requirements:** Will govern future `THM` requirements.
- **Affected modules:** THM.
- **Accessibility impact:** Adaptive themes must each independently meet accessibility requirements.
- **Motion impact:** Not applicable at this stage.
- **Responsive impact:** Not applicable at this stage.
- **Implementation impact:** Not applicable at this stage.
- **Superseded decision:** None.
- **Review date:** Not applicable.

### KBDL-DEC-009 — Expressive but controlled motion

- **Date:** Not verified
- **Status:** Approved
- **Decision owner:** Not verified (project owner)
- **Context:** KBDL combines a luxury feel with technical restraint.
- **Decision:** KBDL motion is expressive but controlled, rather than either purely functional or unconstrained.
- **Rationale:** User-provided.
- **Alternatives considered:** Not verified.
- **Trade-offs:** Requires explicit motion tiers and safeguards rather than ad hoc animation.
- **Affected requirements:** Will govern future `MOT` requirements.
- **Affected modules:** MOT.
- **Accessibility impact:** Must be paired with enhanced reduced-motion safeguards (see KBDL-DEC-010).
- **Motion impact:** Defines the module's guiding principle.
- **Responsive impact:** Not applicable at this stage.
- **Implementation impact:** Not applicable at this stage.
- **Superseded decision:** None.
- **Review date:** Not applicable.

### KBDL-DEC-010 — WCAG 2.2 AA baseline with enhanced motion safety

- **Date:** Not verified
- **Status:** Approved
- **Decision owner:** Not verified (project owner)
- **Context:** KBDL must be broadly accessible and safe for users sensitive to motion.
- **Decision:** KBDL targets WCAG 2.2 Level AA as its accessibility baseline, with enhanced reduced-motion safeguards beyond the WCAG minimum.
- **Rationale:** User-provided.
- **Alternatives considered:** Not verified.
- **Trade-offs:** May constrain motion and visual design choices in later modules.
- **Affected requirements:** Will govern future `A11Y` and `MOT` requirements; establishes `KBDL-GOV-002` as a locked-rule protection (see [governance.md](governance.md)).
- **Affected modules:** A11Y, MOT.
- **Accessibility impact:** Defines the module's baseline.
- **Motion impact:** Constrains all future motion requirements.
- **Responsive impact:** Not applicable at this stage.
- **Implementation impact:** Not applicable at this stage.
- **Superseded decision:** None.
- **Review date:** Not applicable.

### KBDL-DEC-011 — Status model correction: approval vs. provenance vs. validation

- **Date:** Not verified
- **Status:** Approved
- **Decision owner:** Not verified (project owner, via remediation prompt KBDL-001-R1)
- **Context:** KBDL-001 validation identified contradictory rules: some sections implied `Confirmed`, `User-provided`, and `Verified` each independently authorized implementation, while others reserved `Verified` status changes for the project owner only. The traceability matrix also used "This document" as its own validation evidence in several rows.
- **Decision:** The status model is corrected to three independent dimensions — lifecycle/approval status (`Recommended`, `Unresolved`, `Approved`, `Deferred`, `Blocked`, `Deprecated`, `Superseded`), provenance (`User-provided`, `Confirmed`, `Assumed`), and validation status (`Not verified`, `Verified`). Only the lifecycle label `Approved` authorizes implementation. Any contributor may record `Verified` validation status with evidence, but this never grants `Approved` lifecycle status.
- **Rationale:** Separating these dimensions removes the contradiction between "who may assign `Verified`" and "what authorizes implementation," and stops circular evidence (a document citing itself as proof of its own validity).
- **Alternatives considered:** Keeping a single combined status list was considered and rejected because it could not express "approved but not yet checked" or "checked but not yet approved" without contradiction.
- **Trade-offs:** Slightly more terminology for contributors to track (three dimensions instead of one list), in exchange for removing ambiguity about implementation authority.
- **Affected requirements:** KBDL-GOV-001, KBDL-GOV-003.
- **Affected modules:** GOV.
- **Accessibility impact:** None directly; KBDL-GOV-002's locked-rule protection for accessibility is unchanged by this correction.
- **Motion impact:** Not applicable.
- **Responsive impact:** Not applicable.
- **Implementation impact:** `conventions.md`, `governance.md`, `README.md`, `glossary.md`, and `traceability-matrix.md` were updated to remove every statement that treated `Confirmed`, `User-provided`, or `Verified` as independent implementation authority.
- **Superseded decision:** None (this decision corrects wording in KBDL-GOV-001/003; it does not replace KBDL-DEC-001 through KBDL-DEC-010, which remain approved as recorded).
- **Review date:** Not applicable.

### KBDL-DEC-012 — Foundation decision packet approved

- **Date:** 2026-07-25
- **Status:** Approved
- **Decision owner:** Project owner (approved directly, in response to the KBDL-003-R1 validation review and foundation-defaults approval gate)
- **Context:** KBDL-003 (as corrected by KBDL-003-R1) proposed eleven `Recommended` foundation defaults — neutral and accent color direction, typeface strategy, type-scale relationships, spacing scale, named breakpoint set, geometric character, corner classification, elevation scale, icon strategy, and media strategy — none of which carried implementation authority until approved, per [conventions.md §1.1](conventions.md#11-lifecycle--approval-status).
- **Decision:** The project owner approved all eleven recommended defaults in full, with no changes, exactly as documented in [foundations/README.md §6.2](foundations/README.md#62-recommended-defaults--approved).
- **Rationale:** The project owner accepted the planning agent's assessment that the eleven defaults provide a coherent technological-luxury direction while preserving project-level flexibility, and that the outstanding typeface-licensing risk applies to the eventual specific font family, not to the approved humanist-sans strategy itself.
- **Alternatives considered:** "Approve with changes" (rejected — no specific item was flagged for change) and "Revise" (rejected — no item required rework before approval).
- **Trade-offs:** None beyond those already documented per item in [foundations/README.md §6.2](foundations/README.md#62-recommended-defaults--approved).
- **Affected requirements:** `KBDL-FND-009`, `KBDL-FND-010`, `KBDL-FND-011`, `KBDL-FND-012` (lifecycle status changed from `Recommended` to `Approved`).
- **Affected modules:** FND.
- **Accessibility impact:** None beyond what was already evaluated in KBDL-003/KBDL-003-R1 (the `neutral-50`/`neutral-60` contrast correction); no accessibility rule was changed by this approval.
- **Motion impact:** Not applicable.
- **Responsive impact:** Named breakpoint roles are now approved; exact pixel values remain deferred to KBDL-006.
- **Implementation impact:** `foundations/README.md`, `foundations/color.md`, `foundations/typography.md`, `foundations/spacing-layout.md`, `foundations/shape-depth.md`, `foundations/iconography-media.md`, `README.md`, and `traceability-matrix.md` were updated to reflect the `Approved` lifecycle status of these defaults. KBDL-004 (Adaptive Themes) may now build on these approved values.
- **Superseded decision:** None.
- **Review date:** Not applicable.

## Unresolved Metadata

The following metadata could not be verified from available sources and is
intentionally left as `Not verified` rather than fabricated: exact decision
dates, named decision owners, meeting or approval records, and participant
lists, **except** where a decision (such as KBDL-DEC-012) records a date
and owner directly confirmed within the conversation that produced it.
