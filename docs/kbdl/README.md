# KBDL — Design Language Specification

## KBDL Overview

KBDL is a reusable web design language combining digital luxury, technical
utility, controlled expressive motion, cross-project visual consistency,
responsive and mobile-friendly behavior, adaptive light and dark
presentation, and WCAG 2.2 Level AA accessibility with enhanced
reduced-motion safeguards. KBDL initially supports three project profiles:
Showcase (portfolios and creative showcases), Precision (SaaS dashboards),
and Flow (consumer-facing web applications). See the
[glossary](glossary.md) for precise definitions of these terms.

## Specification Status

**KBDL-001: Specification Architecture and Governance Foundation**,
**KBDL-002: Identity, Principles, and Visual Consistency Rules**,
**KBDL-003: Core Visual Foundations**,
**KBDL-004: Adaptive Theme System**,
**KBDL-005: Expressive Motion Language**,
**KBDL-006: Responsive Behavior and Accessibility**, and
**KBDL-007: Core Action, Form, and Navigation Components** deliverables
are present in the repository, the first seven steps of a ten-step
approved roadmap. Their
lifecycle status is `Approved` for architecture, rules, and (as of the
project owner's foundation-defaults approval, see
[KBDL-DEC-012](decision-register.md#kbdl-dec-012--foundation-decision-packet-approved))
the KBDL-003 default values (color, typography, spacing, shape, elevation,
iconography); requirement-level validation statuses are recorded
independently in the [traceability matrix](traceability-matrix.md) and are
not all `Verified`. As of the project owner's theme-decisions approval
(see [KBDL-DEC-013](decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)),
the ten items in the KBDL-004 theme decision packet — persistence
baseline, the opaque light/dark theme mappings, status-family colors,
the opaque gradient caption-band strategy, the color-value expression
convention, conceptual transition guidance, theme-selection precedence,
project-override boundaries, and local contrast contexts — are
`Approved`. Excluded from this approval and still `Recommended`/`Not
verified`: Accent-surface, Scrim, and Selection-background opacity;
translucent variants of the caption band; project-specific media
composites; account-level theme sync; high-contrast/forced-colors mode;
data-visualization palettes; and any implementation-layer format (CSS
custom properties, JSON tokens, component-level theme tokens, framework
APIs) — see
[themes/README.md § Theme Decision Packet](themes/README.md#10-theme-decision-packet-approved-under-kbdl-004-a1).
KBDL-005 established KBDL's motion terminology, identity translation,
purpose model, and category-completeness structure, `Approved` where
directly supported by prior approved principles, theme rules, or the
motion-safety baseline (see [motion/README.md](motion/README.md)). As of
the project owner's motion-decisions approval (see
[KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved)),
the fifteen items in the KBDL-005 motion decision packet — the
five-level motion hierarchy, the timing architecture and duration
classes/values, easing categories/curves, movement-distance and scale
ranges, stagger/overlap guidance, the entrance-versus-exit relationship,
attention-repetition limits, ambient- and scroll-linked-motion
boundaries, theme-transition duration/easing, the reduced-motion
substitution matrix, the motion-token naming architecture,
profile-level intensity adjustments, the multi-factor intensity model,
and the navigation-motion architecture — are `Approved`. Excluded from
this approval and still `Recommended`/`Not verified`/`Deferred`: exact
component-specific movement/scale/stagger values, device-performance
detection, animation-library/rendering-technology selection, CSS/JSON/
JavaScript token formats, browser-support policy, exact scroll
thresholds, and exact quantitative motion-hazard thresholds — see
[motion/README.md § Motion Decision Packet](motion/README.md#10-motion-decision-packet).
KBDL-006 established KBDL's responsive-behavior and accessibility
specification: WCAG 2.2 Level AA is the adopted conformance baseline
(see [KBDL-DEC-010](decision-register.md#kbdl-dec-010--wcag-22-aa-baseline-with-enhanced-motion-safety)),
and every `KBDL-RSP-###`/`KBDL-A11Y-###` requirement that directly
restates an already-approved WCAG 2.2 criterion or prior KBDL rule is
`Approved` (see [responsive.md](responsive.md) and
[accessibility.md](accessibility.md)). Genuinely new KBDL-006 defaults —
exact breakpoint thresholds, grid columns, gutters, container widths, a
preferred enhanced target size, a forced-colors/high-contrast policy,
and a preferred accessibility testing matrix — remain `Recommended`,
pending project-owner approval via the
[responsive decision packet](responsive.md#35-responsive-decision-packet)
and the
[accessibility decision packet](accessibility.md#49-accessibility-decision-packet).
Validation status remains separate throughout: implementation-dependent
items (keyboard, screen-reader, zoom, forced-colors, flash, and
real-device testing) remain `Not verified`, since no implementation
exists; this module does not claim full WCAG conformance. KBDL-007
established KBDL's core action, form, and navigation component
specification: 51 `KBDL-CMP-###` requirements translating approved
KBDL-002 through KBDL-006 rules, WCAG 2.2, and WAI-ARIA into
component-level contracts (see [components-core.md](components-core.md)).
Requirements directly restating an already-approved source are
`Approved`; genuinely new component-level taxonomies (a button
hierarchy, a tabs activation model, truncation models for breadcrumbs
and pagination, and similar) remain `Recommended`, pending project-owner
approval via the
[KBDL-007 decision packet](components-core.md#35-kbdl-007-decision-packet).
None of the nine unapproved KBDL-006 recommendations is treated as
implementation authority anywhere in KBDL-007. KBDL-008 (Surface,
Overlay, Feedback, and System-State Components) remains locked until
KBDL-007 passes the planning agent's validation review; it has not been
started. This is not a claim that the overall KBDL project is complete —
three roadmap steps remain. Progression to later roadmap steps depends on
the
planning agent's validation review, not on this index. KBDL-001
established the documentation architecture, terminology, requirement
and status conventions, and governance for the entire KBDL
specification. KBDL-002 established KBDL's identity statement, Digital
Luxury and Technical Utility definitions, core principles,
visual-consistency relationships, the locked/controlled/open identity
model, and the design-decision hierarchy (see
[principles.md](principles.md)). KBDL-003 established KBDL's color,
typography, spacing/layout, shape/depth, and iconography/media
architecture (see [foundations/README.md](foundations/README.md)). KBDL-004
established KBDL's adaptive theme architecture, semantic-role inventory,
recommended light and dark theme mappings, selection precedence,
persistence guidance, project-controlled adaptation, and local contrast
contexts (see [themes/README.md](themes/README.md)). KBDL-005
established KBDL's framework-independent motion language (see
[motion/README.md](motion/README.md)). KBDL-006 established KBDL's
responsive-behavior and accessibility specification, mapping WCAG 2.2
Level AA to KBDL topics and resolving items previously deferred to it
(see [responsive.md](responsive.md) and
[accessibility.md](accessibility.md)). KBDL-007 established KBDL's
core action, form, and navigation component specification, translating
approved principles, foundations, themes, motion, responsive, and
accessibility rules into component-level contracts (see
[components-core.md](components-core.md)). None of these steps define
implementation code, KBDL-008 surfaces, or later-roadmap work — those
remain later roadmap steps and must not be started early (see
[governance.md](governance.md)).

## Intended Audience

This specification serves anyone who defines, implements, reviews, or governs
KBDL: design-system architects, engineers implementing KBDL in a project,
accessibility reviewers, and contributors proposing changes to the
specification itself.

## How to Use This Specification

1. Start with this index to understand the document hierarchy and
   conventions.
2. Consult the [glossary](glossary.md) for any unfamiliar term.
3. When looking for a specific requirement, use its requirement ID (see
   [Requirement Identification](#requirement-identification)) and check the
   [traceability matrix](traceability-matrix.md) for its current location and
   status.
4. Before implementing anything, confirm its lifecycle status (see
   [status labels](#status-labels)) is `Approved`. No other label —
   including `Confirmed`, `User-provided`, or `Verified` — authorizes
   implementation on its own.
5. Before proposing a change, read [contributing.md](contributing.md).
6. Before approving a change, use the [conformance checklist](conformance-checklist.md).

## Document Hierarchy

KBDL-001, KBDL-002, KBDL-003, KBDL-004, KBDL-005, KBDL-006, and
KBDL-007 deliver the documents below with real content. Rows still
marked `Deferred` show the **planned location only** for future
modules; those files do not exist yet and must not be created until
their roadmap step is reached.

| # | Module | Status | Location |
| --- | --- | --- | --- |
| 1 | Introduction | Deferred | `docs/kbdl/introduction.md` (planned) |
| 2 | Principles | Approved | [principles.md](principles.md) |
| 3 | Visual foundations | Approved (architecture and default values)* | [foundations/README.md](foundations/README.md) |
| 4 | Adaptive themes | Approved (architecture and the ten-item theme decision packet)** | [themes/README.md](themes/README.md) |
| 5 | Motion | Approved (architecture and the fifteen-item motion decision packet)† | [motion/README.md](motion/README.md) |
| 6 | Responsive behavior | Approved (architecture)‡; Recommended (exact breakpoint/grid/gutter/container values) | [responsive.md](responsive.md) |
| 7 | Accessibility | Approved (WCAG 2.2 AA mapping)‡; Recommended (KBDL-specific enhancements) | [accessibility.md](accessibility.md) |
| 8 | Core action, form, and navigation components | Approved (architecture)§; Recommended (component-level taxonomies) | [components-core.md](components-core.md) |
| 9 | Surface, overlay, feedback, and system-state components | Deferred (locked until KBDL-007 passes validation) | `docs/kbdl/components-system.md` (planned) |
| 10 | Project profiles (Showcase, Precision, Flow) | Deferred | `docs/kbdl/profiles.md` (planned) |
| 11 | Manual customization | Deferred | `docs/kbdl/customization.md` (planned) |
| 12 | Validation | Deferred | `docs/kbdl/validation.md` (planned) |
| 13 | Governance | Approved | [governance.md](governance.md) |
| 14 | Future expansion | Deferred | Location to be determined when needed |

\* See
[foundations/README.md § Foundation Status Model](foundations/README.md#3-foundation-status-model)
for how the module's architecture and default values are distinguished,
and [KBDL-DEC-012](decision-register.md#kbdl-dec-012--foundation-decision-packet-approved)
for the project owner's approval of the default values.

\*\* See
[themes/README.md](themes/README.md) for the full theme architecture and
semantic-role inventory, and
[KBDL-DEC-013](decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)
for the project owner's approval of the ten-item
[theme decision packet](themes/README.md#10-theme-decision-packet-approved-under-kbdl-004-a1)
(opaque light/dark mappings, status-family colors, opaque gradient
caption-band strategy, color-value expression convention, conceptual
transition guidance, selection precedence, project-override boundaries,
and local contrast contexts). Opacity values, translucent variants, and
all implementation-layer formats remain `Recommended`/`Not verified` and
outside this approval.

† See [motion/README.md](motion/README.md) for the full motion
architecture and
[KBDL-DEC-014](decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved)
for the project owner's approval of the fifteen-item
[motion decision packet](motion/README.md#10-motion-decision-packet)
(the five-level motion hierarchy, timing architecture and duration
classes/values, easing categories/curves, movement-distance and scale
ranges, stagger/overlap guidance, the entrance-versus-exit relationship,
attention-repetition limits, ambient- and scroll-linked-motion
boundaries, theme-transition duration/easing, the reduced-motion
substitution matrix, the motion-token naming architecture,
profile-level intensity adjustments, the multi-factor intensity model,
and the navigation-motion architecture). Exact component-specific
values, implementation technology, and all KBDL-006-or-later content
remain `Recommended`/`Not verified`/`Deferred` and outside this
approval.

‡ See [responsive.md](responsive.md) and [accessibility.md](accessibility.md)
for the full specifications. Requirements directly restating an
already-adopted WCAG 2.2 Level A/AA criterion (adopted under
[KBDL-DEC-010](decision-register.md#kbdl-dec-010--wcag-22-aa-baseline-with-enhanced-motion-safety))
or a prior approved KBDL rule are `Approved`. Genuinely new KBDL-006
defaults — exact breakpoint thresholds, grid columns, gutters,
container widths, a preferred enhanced target size, a forced-colors/
high-contrast policy, and a preferred accessibility testing matrix —
remain `Recommended`, pending project-owner approval via the
[responsive decision packet](responsive.md#35-responsive-decision-packet)
and the
[accessibility decision packet](accessibility.md#49-accessibility-decision-packet).
No implementation-dependent validation (keyboard, screen-reader, zoom,
forced-colors, flash, or real-device testing) is claimed `Verified` —
no implementation exists yet.

§ See [components-core.md](components-core.md) for the full
specification. Requirements directly restating an already-approved
WCAG 2.2 criterion, WAI-ARIA role/state/property, or prior approved
KBDL rule are `Approved`. Genuinely new KBDL-007 component-level
decisions — a button hierarchy taxonomy, a tabs activation model,
breadcrumb/pagination truncation models, a navigation collapse
threshold, and similar — remain `Recommended`, pending project-owner
approval via the
[KBDL-007 decision packet](components-core.md#35-kbdl-007-decision-packet).
None of the nine unapproved KBDL-006 recommendations is treated as
implementation authority anywhere in this module. No implementation-dependent
validation is claimed `Verified` — no coded component exists yet.

Supporting documents (not numbered modules, but required by KBDL-001 and
referenced by KBDL-002 and KBDL-003):

- [glossary.md](glossary.md) — terminology
- [conventions.md](conventions.md) — status labels, requirement IDs, cross-references
- [governance.md](governance.md) — governance and change control
- [contributing.md](contributing.md) — contribution and review workflow
- [decision-register.md](decision-register.md) — approved decisions
- [traceability-matrix.md](traceability-matrix.md) — requirement traceability
- [conformance-checklist.md](conformance-checklist.md) — conformance review

This hierarchy is designed so each remaining future module (rows 1, 5–12,
14) can be added as its own file without reorganizing this index or
renumbering existing requirement IDs, exactly as row 2 (Principles),
row 3 (Visual foundations), and row 4 (Adaptive themes) were added in
KBDL-002, KBDL-003, and KBDL-004 without disturbing any other row.

## Status Labels

Every requirement, decision, or claim is described along three independent
dimensions:

- **Lifecycle / approval status** — `Recommended`, `Unresolved`, `Approved`,
  `Deferred`, `Blocked`, `Deprecated`, `Superseded`. Only `Approved`
  authorizes implementation.
- **Provenance** — `User-provided`, `Confirmed`, `Assumed`. Describes where a
  statement came from or how much confidence it carries; never by itself an
  authorization to implement.
- **Validation status** — `Not verified`, `Verified`. Records whether a
  defined validation method has actually been run; never by itself an
  authorization to implement.

A requirement carries one label from each dimension at once. Full
definitions, who may assign each label, and how they change are documented
in [conventions.md](conventions.md#1-status-labels).

## Requirement Identification

Requirements use the format `KBDL-<MODULE>-<###>` (for example
`KBDL-GOV-001`), where `<MODULE>` is a stable three-to-four letter module
code and `<###>` is a zero-padded sequential number, unique and never reused
within its module. The full scheme, including module codes and the
create/retire/supersede lifecycle, is documented in
[conventions.md](conventions.md#2-requirement-identification).

## Governance, Glossary, Decisions, Traceability, and Conformance

- **Principles:** [principles.md](principles.md) — KBDL identity, Digital
  Luxury, Technical Utility, core principles, visual consistency, and the
  design-decision hierarchy.
- **Visual foundations:** [foundations/README.md](foundations/README.md) —
  color, typography, spacing/layout, shape/depth, and iconography/media
  architecture, plus the foundation decision packet approved via
  [KBDL-DEC-012](decision-register.md#kbdl-dec-012--foundation-decision-packet-approved).
- **Adaptive themes:** [themes/README.md](themes/README.md) — theme
  architecture, semantic-role inventory, recommended light/dark theme
  mappings, selection precedence, persistence, and project-controlled
  adaptation.
- **Governance:** [governance.md](governance.md) — ownership, change
  control, approval, exceptions, and review expectations.
- **Glossary:** [glossary.md](glossary.md) — definitions for all KBDL terms
  used across the specification.
- **Decision register:** [decision-register.md](decision-register.md) — the
  record of approved KBDL decisions.
- **Traceability matrix:** [traceability-matrix.md](traceability-matrix.md) —
  connects blueprint concepts, requirement IDs, specification locations,
  status, and validation.
- **Conformance checklist:** [conformance-checklist.md](conformance-checklist.md) —
  used to review any change before approval.
