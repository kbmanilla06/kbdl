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
- **Roadmap-evolution clarification (KBDL-011-R1):** The original decision
  above governs the written-specification scope KBDL-001 through KBDL-010.
  The subsequently approved roadmap adds KBDL-011 as a separate Final
  Validation and completion gate. This clarification preserves and does not
  supersede the original written-specification decision; it does not approve
  candidate readiness, accept any limitation, or approve project completion.

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
- **Decision owner:** Project owner. Approved via a direct, structured
  confirmation question posed in the implementing conversation ("How do
  you want to respond?" with four mutually exclusive options: approve
  all, approve with changes, revise, or pause); the project owner selected
  "Approve all eleven defaults." This is an explicit interactive user
  decision, not an inference from the planning agent's recommendation.
- **Context:** KBDL-003 (as corrected by KBDL-003-R1) proposed eleven `Recommended` foundation defaults — neutral and accent color direction, typeface strategy, type-scale relationships, spacing scale, named breakpoint set, geometric character, corner classification, elevation scale, icon strategy, and media strategy — none of which carried implementation authority until approved, per [conventions.md §1.1](conventions.md#11-lifecycle--approval-status).
- **Decision:** The project owner approved all eleven recommended defaults in full, with no changes, exactly as documented in [foundations/README.md §6.2](foundations/README.md#62-recommended-defaults--approved).
- **Rationale:** The project owner accepted the planning agent's assessment that the eleven defaults provide a coherent technological-luxury direction while preserving project-level flexibility, and that the outstanding typeface-licensing risk applies to the eventual specific font family, not to the approved humanist-sans strategy itself.
- **Alternatives considered:** "Approve with changes" (rejected — no specific item was flagged for change) and "Revise" (rejected — no item required rework before approval).
- **Confirmation:** A subsequent validation review disputed this decision's provenance, asserting no project-owner approval had occurred. The project owner was asked directly whether their prior selection stood; they confirmed on 2026-07-25 that "my approval stands," reconfirming this decision without any change to its scope or the eleven approved items.
- **Trade-offs:** None beyond those already documented per item in [foundations/README.md §6.2](foundations/README.md#62-recommended-defaults--approved).
- **Affected requirements:** `KBDL-FND-009`, `KBDL-FND-010`, `KBDL-FND-011`, `KBDL-FND-012` (lifecycle status changed from `Recommended` to `Approved`).
- **Affected modules:** FND.
- **Accessibility impact:** None beyond what was already evaluated in KBDL-003/KBDL-003-R1 (the `neutral-50`/`neutral-60` contrast correction); no accessibility rule was changed by this approval.
- **Motion impact:** Not applicable.
- **Responsive impact:** Named breakpoint roles are now approved; exact pixel values remain deferred to KBDL-006.
- **Implementation impact:** `foundations/README.md`, `foundations/color.md`, `foundations/typography.md`, `foundations/spacing-layout.md`, `foundations/shape-depth.md`, `foundations/iconography-media.md`, `README.md`, and `traceability-matrix.md` were updated to reflect the `Approved` lifecycle status of these defaults. KBDL-004 (Adaptive Themes) may now build on these approved values.
- **Superseded decision:** None.
- **Review date:** Not applicable.

### KBDL-DEC-013 — KBDL-004 theme decisions approved

- **Date:** 2026-07-26
- **Status:** Approved
- **Decision owner:** Project owner. A prompt introducing this decision
  (KBDL-004-A1) asserted that the project owner had already responded "
  APPROVE THEME DECISIONS," but no such message existed anywhere in the
  actual implementing conversation. This discrepancy was flagged directly
  to the project owner, who was then asked a direct, structured
  confirmation question ("Yes, APPROVE THEME DECISIONS" vs. alternatives);
  the project owner selected "Yes, APPROVE THEME DECISIONS." This
  in-conversation selection — not the prompt's original unverified claim
  — is the sole evidentiary basis for this decision, consistent with the
  standard already established and reconfirmed in
  [KBDL-DEC-012](#kbdl-dec-012--foundation-decision-packet-approved).
- **Context:** KBDL-004 (as corrected by KBDL-004-R1/R2/R3/R4) proposed
  ten `Recommended` theme decisions in
  [themes/README.md §10.2](themes/README.md#10-theme-decision-packet-approved-under-kbdl-004-a1) —
  persistence baseline, the opaque light-theme semantic mapping, the
  opaque dark-theme semantic mapping, status-family values, the opaque
  caption-band gradient strategy, the color-value expression convention,
  conceptual transition guidance beyond reduced-motion, the full
  six-level theme-selection precedence ordering, detailed
  project-override boundaries, and local contrast contexts — none of
  which carried implementation authority until approved, per
  [conventions.md §1.1](conventions.md#11-lifecycle--approval-status).
- **Decision:** The project owner approved exactly the ten items listed
  above, and only those ten items, as documented in
  [themes/README.md §10.2](themes/README.md#10-theme-decision-packet-approved-under-kbdl-004-a1).
  This approval is explicitly **scoped to the opaque/conceptual content
  of those ten items only** and does **not** extend to: Accent-surface
  opacity, Scrim opacity, or Selection-background opacity (all remain
  `Recommended`, `Not verified`); any translucent caption-band or
  media-overlay variant (remains `Recommended`, `Not verified`); any
  project-specific media composite; account-level theme-preference sync;
  high-contrast/forced-colors mode; data-visualization palettes;
  framework-specific theme APIs, CSS custom properties, JSON token
  formats, or component-level theme tokens (all implementation-layer,
  out of scope for this specification); any motion timing, easing, or
  duration value (belongs to KBDL-005, not started by this approval); and
  any KBDL-006 or later decision. This approval does **not** change any
  validation status — items marked `Not verified` before this decision
  remain `Not verified` after it; approval (lifecycle authority) and
  validation (evidence a claim was checked) are independent dimensions
  per [conventions.md §1](conventions.md#1-status-labels).
- **Rationale:** The project owner accepted that the ten items were
  fully specified, internally consistent, and — where a contrast claim
  was made — backed by verified opaque contrast evidence in
  [validation.md](themes/validation.md#3-consolidated-contrast-evidence),
  while the excluded opacity/translucency items still lack the
  alpha-composite evidence needed to responsibly approve them.
- **Alternatives considered:** "Approve with changes" (rejected — no
  specific item was flagged for change) and "Revise" (rejected — no item
  required rework before approval).
- **Trade-offs:** Two normative requirements (`KBDL-THM-007`,
  `KBDL-THM-008`) reference documents (`light-theme.md`, `dark-theme.md`)
  that mix approved opaque content with excluded opacity values; rather
  than approving those documents wholesale, the requirements' own
  normative text was narrowed to state the opaque-only scope explicitly,
  avoiding over-approval of unreviewed opacity claims.
- **Affected requirements:** `KBDL-THM-004`, `KBDL-THM-007` (narrowed to
  opaque mappings only), `KBDL-THM-008` (narrowed to opaque mappings
  only), `KBDL-THM-009`, `KBDL-THM-010` (narrowed to the opaque
  caption-band strategy only), `KBDL-THM-011`, `KBDL-THM-012`,
  `KBDL-THM-013`, `KBDL-THM-014`, `KBDL-THM-015` (lifecycle status
  changed from `Recommended` to `Approved`).
- **Affected modules:** THM.
- **Accessibility impact:** None beyond what was already evaluated in
  KBDL-004/R1-R4; no new accessibility rule or contrast claim was
  introduced by this approval, and the excluded opacity items remain
  unverified rather than being implicitly endorsed.
- **Motion impact:** None. `KBDL-THM-012`'s approval covers only
  conceptual, non-timing transition guidance; KBDL-005 (Motion) remains
  eligible for a future prompt and has not been started.
- **Responsive impact:** Not applicable.
- **Implementation impact:** `themes/README.md`, `themes/light-theme.md`,
  `themes/dark-theme.md`, `themes/adaptation.md`, `themes/validation.md`,
  `traceability-matrix.md`, and `README.md` were updated to reflect the
  `Approved` lifecycle status of these ten items, while preserving every
  `Recommended`/`Not verified` marking for the explicitly excluded items.
- **Superseded decision:** None.
- **Review date:** Not applicable.

### KBDL-DEC-014 — KBDL-005 motion decisions approved

- **Date:** 2026-07-26
- **Status:** Approved
- **Decision owner:** Project owner. A prompt introducing this decision
  (KBDL-005-A1) asserted that the project owner had already responded
  "approve motion decisions," but no such message existed anywhere in
  the actual implementing conversation. This discrepancy was flagged
  directly to the project owner, who was then asked a direct, structured
  confirmation question ("Yes, approve motion decisions" vs.
  alternatives); the project owner selected "Yes, approve motion
  decisions." This in-conversation selection — not the prompt's original
  unverified claim — is the sole evidentiary basis for this decision,
  consistent with the standard established in
  [KBDL-DEC-012](#kbdl-dec-012--foundation-decision-packet-approved) and
  [KBDL-DEC-013](#kbdl-dec-013--kbdl-004-theme-decisions-approved).
- **Context:** KBDL-005 (as corrected by KBDL-005-R1/R2) proposed fifteen
  `Recommended` motion decisions in
  [motion/README.md §10.2](motion/README.md#102-approved-decisions-kbdl-005-a1) —
  the five-level motion hierarchy, the timing architecture and duration
  classes/values, easing categories and exact curves, movement-distance
  and scale ranges, stagger and overlap guidance, the entrance-versus-exit
  duration relationship, attention repetition limits, ambient-motion
  boundaries, scroll-linked-motion boundaries, theme-transition duration
  and easing, the reduced-motion substitution matrix, the motion-token
  naming architecture, profile-level motion-intensity adjustments, the
  multi-factor motion-intensity model, and the navigation-motion
  architecture — none of which carried implementation authority until
  approved, per [conventions.md §1.1](conventions.md#11-lifecycle--approval-status).
- **Decision:** The project owner approved exactly the fifteen items
  listed above, and only those fifteen items, as documented in
  [motion/README.md §10.2](motion/README.md#102-approved-decisions-kbdl-005-a1)
  and its coverage table in
  [motion/README.md §10.2.1](motion/README.md#1021-approved-requirement-coverage).
  This approval promotes exactly the sixteen requirements mapped to
  those fifteen decisions —
  `KBDL-MOT-005`, `KBDL-MOT-006`, `KBDL-MOT-007`, `KBDL-MOT-008`,
  `KBDL-MOT-009`, `KBDL-MOT-010`, `KBDL-MOT-011`, `KBDL-MOT-013`,
  `KBDL-MOT-020`, `KBDL-MOT-028`, `KBDL-MOT-029`, `KBDL-MOT-030`,
  `KBDL-MOT-031`, `KBDL-MOT-032`, `KBDL-MOT-033`, `KBDL-MOT-034` — and
  does **not** extend to: exact component-specific movement, scale, or
  stagger values; exact concurrency limits; device-performance detection
  strategy; animation-library or rendering-technology selection; CSS,
  JSON, or JavaScript motion-token formats; component-specific animation
  specifications; browser-support policy; exact scroll thresholds; exact
  quantitative motion-hazard or flashing thresholds (all deferred to
  KBDL-006 or later, implementation-layer, or otherwise out of scope for
  this design-language specification); any unresolved KBDL-004 theme
  value; and any KBDL-006-or-later content. This approval does **not**
  change any validation status — items marked `Not verified` before this
  decision remain `Not verified` after it; approval (lifecycle authority)
  and validation (evidence a claim was checked) are independent
  dimensions per [conventions.md §1](conventions.md#1-status-labels).
- **Rationale:** The project owner accepted that the fifteen decisions
  were fully specified, internally consistent (per the numerical- and
  reduced-motion-parity reviews in
  [motion/validation.md](motion/validation.md)), and completely mapped to
  their sixteen underlying requirements, with no requirement left
  unaccounted for after KBDL-005-R2 corrected the packet's initial
  coverage gap.
- **Alternatives considered:** "Approve with changes" (rejected — no
  specific item was flagged for change) and "Revise" (rejected — no item
  required rework before approval).
- **Trade-offs:** None beyond those already documented per item in
  [motion/README.md §10.2](motion/README.md#102-approved-decisions-kbdl-005-a1).
- **Affected requirements:** `KBDL-MOT-005`, `KBDL-MOT-006`,
  `KBDL-MOT-007`, `KBDL-MOT-008`, `KBDL-MOT-009`, `KBDL-MOT-010`,
  `KBDL-MOT-011`, `KBDL-MOT-013`, `KBDL-MOT-020`, `KBDL-MOT-028`,
  `KBDL-MOT-029`, `KBDL-MOT-030`, `KBDL-MOT-031`, `KBDL-MOT-032`,
  `KBDL-MOT-033`, `KBDL-MOT-034` (lifecycle status changed from
  `Recommended` to `Approved`).
- **Affected modules:** MOT.
- **Accessibility impact:** None beyond what was already evaluated in
  KBDL-005/R1/R2; no new accessibility rule, safety threshold, or
  reduced-motion behavior was introduced by this approval, and the
  deferred quantitative safety thresholds remain unresolved rather than
  being implicitly endorsed.
- **Motion impact:** This decision is itself the motion-approval record;
  it authorizes the fifteen design-language decisions listed above and
  no others.
- **Responsive impact:** Not applicable. KBDL-006 remains locked until
  KBDL-005 passes validation, and is not started by this approval.
- **Implementation impact:** `motion/README.md`, `motion/foundations.md`,
  `motion/timing-easing.md`, `motion/patterns.md`,
  `motion/accessibility-performance.md`, `motion/validation.md`,
  `traceability-matrix.md`, and `README.md` were updated to reflect the
  `Approved` lifecycle status of these sixteen requirements, while
  preserving every `Recommended`/`Not verified`/`Deferred` marking for
  the explicitly excluded items.
- **Superseded decision:** None.
- **Review date:** Not applicable.

### KBDL-DEC-015 — KBDL-006 remediation and ID-governance amendment

- **Date:** 2026-07-27
- **Status:** Approved
- **Decision owner:** Project owner. A remediation prompt (KBDL-006-R1)
  asserted that the project owner had already approved this governance
  decision, but no such approval existed anywhere in the actual
  implementing conversation prior to this step. This discrepancy was
  flagged directly to the project owner, who was then asked a direct,
  structured confirmation question ("Yes, approve this governance
  change" vs. alternatives); the project owner selected "Yes, approve
  this governance change." This in-conversation selection — not the
  prompt's original unverified claim — is the sole evidentiary basis
  for this decision, consistent with the standard established in
  [KBDL-DEC-012](#kbdl-dec-012--foundation-decision-packet-approved),
  [KBDL-DEC-013](#kbdl-dec-013--kbdl-004-theme-decisions-approved), and
  [KBDL-DEC-014](#kbdl-dec-014--kbdl-005-motion-decisions-approved).
- **Context:** KBDL-006 (commit `14ef110`) assigned stable
  `KBDL-RSP-###`/`KBDL-A11Y-###` IDs to nine `Recommended` requirements
  before their approval, following the same practice already used for
  `KBDL-THM-013`–`015` and `KBDL-MOT-005`, `006`, etc. since KBDL-004-R1.
  This practice conflicted with the literal text of
  [conventions.md §2](conventions.md#2-requirement-identification),
  which stated an ID is assigned "at the time it is `Approved`." A
  remediation step (KBDL-006-R1) proposed correcting the written
  convention to match the practice actually in use, and separately
  proposed accepting commit `14ef110` as the KBDL-006 remediation
  baseline.
- **Decision:** The project owner approved exactly two things: (1)
  accepting commit `14ef110` as the KBDL-006 remediation baseline only
  — not as a statement that KBDL-006 has passed; and (2) amending
  [conventions.md §2](conventions.md#2-requirement-identification) so
  that a stable requirement ID may be assigned as soon as a requirement
  is documented, regardless of lifecycle status, provided that: an
  assigned ID never grants, implies, or shortcuts approval; an assigned
  ID never authorizes implementation; only the lifecycle-status
  dimension determines implementation authority; `Recommended`,
  `Unresolved`, `Deferred`, and `Blocked` requirements may retain stable
  IDs; retired or rejected IDs are never reused; and an approval
  transition updates lifecycle status only, never the ID itself. This
  decision does **not** approve any of the nine KBDL-006 decision-packet
  recommendations (`KBDL-RSP-002`, `003`, `004`, `005`, `008`, `011`,
  `KBDL-A11Y-011`, `021`, `035`), all of which remain `Recommended`. It
  does **not** declare KBDL-006 itself passed — KBDL-006 remains under
  remediation and validation. It does **not** unlock KBDL-007, which
  remains locked until KBDL-006 passes the planning agent's validation
  review.
- **Rationale:** The written convention had fallen out of sync with
  established practice across three prior modules; correcting the
  written rule (rather than retroactively stripping IDs from dozens of
  already-documented `Recommended` requirements) preserves stability and
  avoids ID churn, consistent with the convention's own "Stable" and
  "Independent of page numbering" properties.
- **Alternatives considered:** Retroactively removing IDs from every
  `Recommended` requirement until each is approved (rejected — would
  require renumbering or re-identifying dozens of existing, already
  cross-referenced requirements across `THM`, `MOT`, `RSP`, and `A11Y`,
  creating exactly the ID churn the convention's "Stable" property
  exists to prevent). Leaving the written convention uncorrected while
  continuing the conflicting practice (rejected — an unresolved,
  self-contradicting governance document is itself a defect).
- **Trade-offs:** None identified beyond the acknowledgment that the
  written convention was inaccurate for roughly two prior modules'
  worth of history; no existing ID, lifecycle status, provenance, or
  validation status changes as a result.
- **Affected requirements:** None — this decision changes governance
  text only ([conventions.md §2](conventions.md#2-requirement-identification));
  no requirement's ID, lifecycle status, provenance, or validation
  status is altered by this decision itself.
- **Affected modules:** GOV (governance/conventions only).
- **Accessibility impact:** Not applicable — a documentation-governance
  correction, not a substantive accessibility change.
- **Motion impact:** Not applicable.
- **Responsive impact:** Not applicable.
- **Implementation impact:** `conventions.md` was updated to state the
  amended ID-assignment rule. No file's substantive responsive or
  accessibility content changed as a result of this decision.
- **Superseded decision:** None — this decision corrects the written
  text of a convention established under KBDL-001; it does not replace
  any prior decision record.
- **Review date:** Not applicable.

### KBDL-DEC-016 — Current non-retroactive prompt-authority confirmations

- **Date:** 2026-07-28 (Asia/Manila)
- **Status:** Approved — current authority only; non-retroactive
- **Decision owner:** Project owner, by explicit selection in the conversation
  that produced KBDL-011-AR2.
- **Context:** The validated AR1 packet identified eleven unrecovered original
  implementation-prompt approval records and prepared eleven independent,
  bounded current-authority confirmations.
- **Decision:** The project owner selected `CONFIRM CURRENT AUTHORITY`
  independently for KBDL-001, KBDL-002, KBDL-003, KBDL-004, KBDL-005,
  KBDL-006, KBDL-007, KBDL-008, KBDL-009, KBDL-010, and KBDL-011. The exact
  record, scope, and exclusions are retained in the
  [durable owner-decision record](evidence/kbdl-011-authority-recovery/project-owner-authority-confirmations.md).
  Each confirmation applies only to the normative text and relying
  requirements enumerated by AR1 at baseline
  `33402250e3fdb27bd8e1cba53c722b7b765daf8a`, beginning 2026-07-28 in
  Asia/Manila.
- **Effect:** The current authority-decision blocker is resolved for all eleven
  prompt records. The effect is non-retroactive: no historical approval wording
  is proved or reconstructed, unavailable prompt wording is not incorporated,
  and historical implementation and validation history is not rewritten.
- **Exclusions:** No decision-packet item is approved; no `Recommended` or
  `Deferred` requirement is promoted; `KBDL-CUS-030` remains `Deferred`; no
  implementation conformance is established; no limitation is accepted; and
  documentation readiness and project completion are not approved.
- **KBDL-005 separation:** This confirmation is limited to the nine KBDL-005
  relying requirements enumerated by AR1. `KBDL-DEC-014` remains the separate,
  later approval of fifteen motion-decision packet items and is not treated as
  the original KBDL-005 prompt approval.
- **Affected requirements:** The 137 relying requirements enumerated in the AR1
  mapping, with 113 sole-prompt and 24 mixed-authority dependencies; no
  normative text, lifecycle, provenance, or validation-status change.
- **Implementation impact:** None. Implementation conformance remains `NOT
  VERIFIED`.
- **Completion impact:** The project owner's desired outcome is final
  completion, but this decision does not approve readiness or completion.
- **Superseded decision:** None.
- **Review date:** Not applicable.

## Unresolved Metadata

The following metadata could not be verified from available sources and is
intentionally left as `Not verified` rather than fabricated: exact decision
dates, named decision owners, meeting or approval records, and participant
lists, **except** where a decision (such as KBDL-DEC-012) records a date
and owner directly confirmed within the conversation that produced it.
