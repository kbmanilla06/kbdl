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
**KBDL-003: Core Visual Foundations**, and
**KBDL-004: Adaptive Theme System** deliverables are present in the
repository, the first four steps of a ten-step approved roadmap. Their
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
KBDL-005 (Motion) is the next eligible roadmap step and has not been
started. Progression to later roadmap steps depends on the planning
agent's validation review, not on this index. KBDL-001 established the
documentation architecture, terminology, requirement and status
conventions, and governance for the entire KBDL specification. KBDL-002
established KBDL's identity statement, Digital Luxury and Technical Utility
definitions, core principles, visual-consistency relationships, the
locked/controlled/open identity model, and the design-decision hierarchy
(see [principles.md](principles.md)). KBDL-003 established KBDL's color,
typography, spacing/layout, shape/depth, and iconography/media
architecture (see [foundations/README.md](foundations/README.md)). KBDL-004
established KBDL's adaptive theme architecture, semantic-role inventory,
recommended light and dark theme mappings, selection precedence,
persistence guidance, project-controlled adaptation, and local contrast
contexts (see [themes/README.md](themes/README.md)). None of these steps
define motion values, detailed responsive/accessibility rules, components,
or implementation code — those are later roadmap steps and must not be
started early (see [governance.md](governance.md)).

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

KBDL-001, KBDL-002, KBDL-003, and KBDL-004 deliver the documents below
with real content. Rows still marked `Deferred` show the **planned
location only** for future modules; those files do not exist yet and
must not be created until their roadmap step is reached.

| # | Module | Status | Location |
| --- | --- | --- | --- |
| 1 | Introduction | Deferred | `docs/kbdl/introduction.md` (planned) |
| 2 | Principles | Approved | [principles.md](principles.md) |
| 3 | Visual foundations | Approved (architecture and default values)* | [foundations/README.md](foundations/README.md) |
| 4 | Adaptive themes | Approved (architecture and the ten-item theme decision packet)** | [themes/README.md](themes/README.md) |
| 5 | Motion | Deferred | `docs/kbdl/motion.md` (planned) |
| 6 | Responsive behavior | Deferred | `docs/kbdl/responsive.md` (planned) |
| 7 | Accessibility | Deferred | `docs/kbdl/accessibility.md` (planned) |
| 8 | Core action, form, and navigation components | Deferred | `docs/kbdl/components-core.md` (planned) |
| 9 | Surface, overlay, feedback, and system-state components | Deferred | `docs/kbdl/components-system.md` (planned) |
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
