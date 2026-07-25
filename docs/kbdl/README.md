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

This is **KBDL-001: Specification Architecture and Governance Foundation**,
the first of a ten-step approved roadmap. This step establishes the
documentation architecture, terminology, requirement and status conventions,
and governance for the entire KBDL specification. It does not define visual
foundations, themes, motion values, components, or profile-specific design
guidance — those are later roadmap steps and must not be started early (see
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

KBDL-001 delivers the documents below. Later rows show the **planned
location only** for future modules; those files do not exist yet and must
not be created until their roadmap step is reached.

| # | Module | Status | Location |
| --- | --- | --- | --- |
| 1 | Introduction | Deferred | `docs/kbdl/introduction.md` (planned) |
| 2 | Principles | Deferred | `docs/kbdl/principles.md` (planned) |
| 3 | Visual foundations | Deferred | `docs/kbdl/foundations.md` (planned) |
| 4 | Adaptive themes | Deferred | `docs/kbdl/themes.md` (planned) |
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

Supporting KBDL-001 documents (not numbered modules, but required by this
step):

- [glossary.md](glossary.md) — terminology
- [conventions.md](conventions.md) — status labels, requirement IDs, cross-references
- [governance.md](governance.md) — governance and change control
- [contributing.md](contributing.md) — contribution and review workflow
- [decision-register.md](decision-register.md) — approved decisions
- [traceability-matrix.md](traceability-matrix.md) — requirement traceability
- [conformance-checklist.md](conformance-checklist.md) — conformance review

This hierarchy is designed so each future module (rows 1–12, 14) can be added
as its own file without reorganizing this index or renumbering existing
requirement IDs.

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
