# KBDL Components — Surface, Overlay, Feedback, and System-State

Lifecycle status: mixed. `Approved` for the requirements below whose
normative rule is authorized by at least one of: an adopted WCAG 2.2
Level A/AA requirement; an adopted WAI-ARIA 1.2 role, state, or
property definition; a prior approved KBDL principle, foundation,
theme, motion, responsive, accessibility, or KBDL-007 component-level
rule; an explicit mandatory requirement stated in the project-owner-
approved KBDL-008 implementation prompt; or a documented combination of
these — see [§27](#27-normative-requirements) for the exact authority
cited per requirement. The project owner's approval of the KBDL-008
implementation prompt authorizes the prompt's own mandatory scope and
required fields; it does **not** approve any of the 17 items in the
[KBDL-008 decision packet](#33-kbdl-008-decision-packet), any KBDL-006
recommendation, or any KBDL-007 recommendation. `Recommended` for
genuinely new, discretionary component-level taxonomies, timing,
placement, sizing, persistence, modality, queueing, stacking, or
transformation policy not mandated by the approved prompt — pending
project-owner approval via [§33](#33-kbdl-008-decision-packet). No
`Recommended` value in this document authorizes implementation on its
own — see [conventions.md §1.1](conventions.md#11-lifecycle--approval-status).
Assigning a `KBDL-CMP-###` ID does not grant approval or implementation
authority, per the amended convention
([conventions.md §2](conventions.md#2-requirement-identification),
[KBDL-DEC-015](decision-register.md#kbdl-dec-015--kbdl-006-remediation-and-id-governance-amendment)).
Documentation review does not make any requirement's implementation
behavior `Verified`.

This document does not claim full WCAG conformance, ARIA-pattern
compatibility, screen-reader compatibility, browser compatibility, or
real-device compatibility. No coded component exists yet to test
against. Documentation review does not justify `Verified` validation
status.

Return to the [specification index](README.md).

## 1. Purpose and Scope

This document defines KBDL's framework-neutral specification for
surface, overlay, feedback, complex-presentation, and system-state
components: Container Surface, Panel, Card, Accordion, Static Data
Table (surfaces); Tooltip, Popover, Menu, Listbox popup, Dialog, Modal
Dialog, Alert Dialog, Drawer/Sheet (overlays); Inline Feedback, Alert,
Banner, Toast/Snackbar, Status Region/Log, Badge, Progress Indicator,
Meter, Skeleton (feedback); Loading, Empty, No-Results, Error, Offline/
Reconnecting, Permission Denied, Not Found, Maintenance/Degraded, and
System Status states (system-state); and Interactive Grid, Tree/
Treegrid, Carousel, and Data Visualization (complex-presentation). It
extends — and does not duplicate or replace — the shared component
contract established in
[components-core.md §6](components-core.md#6-shared-component-contract).
It does not define application code, a component library, a frontend
framework, token implementation formats, `profiles.md`, manual
customization, or final validation.

## 2. Status Model

Uses KBDL's standard three-dimension model
([conventions.md §1](conventions.md#1-status-labels)), identical to
[components-core.md §2](components-core.md#2-component-status-model).
A requirement may be `Approved` when its normative rule is authorized
by an already-adopted WCAG 2.2 criterion, an adopted WAI-ARIA 1.2
role/state/property definition, a prior approved KBDL rule, an explicit
mandatory requirement in the project-owner-approved KBDL-008
implementation prompt, or a documented combination of these — see
[§27](#27-normative-requirements) for the exact authority cited per
requirement, split by clause where a requirement's authority is mixed.
Prompt approval authorizes only the prompt's own mandatory scope; it
does not approve the [KBDL-008 decision packet](#33-kbdl-008-decision-packet).
A genuinely new, discretionary taxonomy, timing, placement, sizing,
persistence, modality, queueing, stacking, or transformation policy not
mandated by the approved prompt remains `Recommended` until the project
owner reviews [§33](#33-kbdl-008-decision-packet). An APG
interaction-pattern recommendation is not automatically `Approved`
merely by being described in the APG — see
[§4](#4-standards-interpretation-for-this-module).

## 3. Relationship to Prior KBDL Modules

This module operationalizes: KBDL-002's design-decision hierarchy and
locked identity rules; KBDL-003's spacing, shape/depth, and
iconography foundations; KBDL-004's semantic theme roles (surface,
text, border, status, and media/decorative roles from
[themes/semantic-roles.md](themes/semantic-roles.md)); KBDL-005's
motion hierarchy and purpose model; KBDL-006's WCAG 2.2 AA baseline and
responsive-behavior requirements; and KBDL-007's shared component
contract, trigger semantics, and accessible-naming requirements. It
reopens none of these — every foundation, theme, motion, responsive,
accessibility, and KBDL-007 value already `Approved` remains `Approved`
here without change, and every value still `Recommended` in an earlier
module remains `Recommended` here (see [§35](#35-kbdl-006-approval-boundary-audit)
and [§36](#36-kbdl-007-approval-boundary-audit)).

## 4. Standards Interpretation for This Module

- WCAG 2.2 defines required accessibility outcomes; a requirement
  directly restating an adopted WCAG criterion may be `Approved`.
- WAI-ARIA 1.2 defines roles, states, properties, and semantic
  relationships; a requirement directly restating an adopted ARIA role
  or property definition may be `Approved`.
- The APG describes common interaction patterns and keyboard guidance
  but does not itself prove WCAG conformance, and an APG pattern
  recommendation is not automatically `Approved` — the exact keyboard,
  timing, dismissal, and placement choices an APG pattern permits
  remain `Recommended` unless independently dictated by an adopted WCAG
  or ARIA rule.
- The APG tooltip pattern is explicitly work in progress and lacks
  task-force consensus; this document does not mark a complete tooltip
  interaction policy `Approved` solely because it appears in that
  pattern (see [§11.1](#111-tooltip)).
- Native host-language semantics (`<table>`, `<details>`/`<summary>`,
  `<progress>`, `<meter>`, `<dialog>`) are preferred when they provide
  the required behavior; ARIA supplements missing semantics and must
  not replace correct native semantics unnecessarily.
- Documentation review is not implementation-level accessibility
  verification.

## 5. KBDL-007 Ownership Boundary

Status: `Approved` (`KBDL-CMP-052`, extends the scope-control rule
already established by `KBDL-CMP-005`).

This document owns the surface, overlay, feedback, presentation, and
system-state side of every composite pattern below. It does not
redefine, weaken, or replace any KBDL-007 trigger, field, action, or
navigation contract:

| Composite pattern | KBDL-007 owns | KBDL-008 owns |
| --- | --- | --- |
| Tooltip | Trigger's accessible name and action semantics | Tooltip surface, description relationship, persistence, dismissal, positioning behavior |
| Menu button | Button trigger, expanded state, controlled relationship | Menu surface, menu items, navigation within menu, closing and return-focus behavior |
| Combobox | Input, value, expanded state, active-option relationship | Listbox popup surface and option presentation |
| Disclosure/accordion | Disclosure trigger | Accordion panel surface and expanded content |
| Form validation | Field/error relationship and action behavior | Alert, banner, toast, summary surface, and system-feedback presentation |
| Submit loading | Submit action and duplicate-submission prevention | Progress indicator or loading-feedback surface |
| Confirmation | Consequential-action requirement | Dialog or alert-dialog surface |
| Collapsed navigation | Navigation trigger and semantic continuity | Drawer, sheet, or overlay surface |
| Icon button | Accessible name independent of tooltip | Optional tooltip description surface |

Rules: KBDL-008 must not weaken or replace a KBDL-007 trigger contract.
KBDL-008 surfaces must remain operable when composed with an approved
KBDL-007 trigger. A surface must not be used to repair a missing
trigger name, role, state, or keyboard contract. A tooltip must never
be the sole source of an icon button's accessible name
([§11.1](#111-tooltip), `KBDL-CMP-072`). A drawer must not define
or approve the exact responsive collapse threshold
([§11.8](#118-drawer-and-sheet)). A listbox popup must not silently
approve the KBDL-007 combobox-justification recommendation
(`KBDL-CMP-029`). A dialog action area must not silently approve the
KBDL-007 button hierarchy (`KBDL-CMP-015`) or form-action-row ordering
recommendation (`KBDL-CMP-036`).

- **`KBDL-CMP-052`** — This document **must not** weaken, redefine, or
  replace any KBDL-007 trigger, field, action, or navigation contract;
  it defines only the surface, overlay, feedback, presentation, and
  system-state side of the composite patterns in the ownership matrix
  above.
  - Lifecycle status: Approved (scope-control requirement, extends
    `KBDL-CMP-005`). Provenance: Confirmed. Validation status: Not
    applicable.
  - Related requirement: `KBDL-CMP-005` (KBDL-007 scope boundary).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§5](#5-kbdl-007-ownership-boundary).
  - Validation method: Manual scope-compliance review (performed, see
    implementation report).

## 6. System-Component Terminology

- **Surface** — a bounded visual region hosting content, which may or
  may not carry its own semantics.
- **Overlay** — a surface rendered above the normal document flow,
  anchored to a trigger or the viewport, that opens and closes.
- **Modal** — an overlay that requires user response before other
  content can be operated; background content is inert.
- **Non-modal** — an overlay that coexists with an operable background.
- **Inert** — content that cannot receive focus or be reached by
  sequential or assistive-technology navigation while a modal overlay
  is open.
- **Scrim** — a dimming layer behind a modal or floating surface,
  mapped to the existing approved Scrim/backdrop theme role
  ([themes/semantic-roles.md §1.1](themes/semantic-roles.md#11-canvas-and-surfaces)).
  This document does not assign an exact opacity value.
- **Live region** — a programmatically identified region whose updates
  are announced to assistive technology without requiring focus,
  already defined in
  [accessibility.md §35](accessibility.md#35-status-messages-and-live-communication).
- **System state** — a condition of a component, section, page, or
  application (loading, empty, error, offline, and similar) that must
  be communicated to the user independent of visual styling alone.

Additional terms are added to [glossary.md](glossary.md) — see
[§38](#38-cross-module-updates).

## 7. Extended System-Component Contract

Every KBDL-008 component is documented against the shared contract in
[components-core.md §6](components-core.md#6-shared-component-contract)
plus the following KBDL-008-specific fields, stated only where
applicable: trigger owner, surface owner, modal or non-modal behavior,
focus entry/containment/exit/restoration, opening/closing/dismissal/
persistence behavior, layering/nesting behavior, scroll behavior,
loading/empty/error/offline behavior, and security/privacy
considerations. A field genuinely inapplicable to a component (for
example "offline behavior" for a Tooltip) is omitted rather than filled
with placeholder text.

- **`KBDL-CMP-065`** — Every KBDL-008 component that conveys meaning
  **must** have a programmatically determinable accessible name.
  - Lifecycle status: Approved (extends the already-Approved KBDL-007
    accessible-naming requirement, `KBDL-CMP-003`, to this module).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-003` (KBDL-007), `KBDL-CMP-054`,
    `KBDL-CMP-072`, `KBDL-CMP-078`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§7](#7-extended-system-component-contract).
  - Validation method: Manual accessible-name review once implemented.

## 8. Surface Architecture

Status: `Approved` (`KBDL-CMP-053`, extends the native-semantics-first
rule already established by `KBDL-CMP-002`, and the ARIA 1.2 `region`
role definition).

Surfaces are distinguished as: structural (Container Surface),
interactive (Card with an action), grouping (Field Group's visual
container, already KBDL-007 scope), elevated (Panel, Card), expandable
(Accordion), data (Static Data Table, Interactive Grid), and overlay
(Tooltip, Popover, Menu, Dialog). A surface is semantically neutral
(no ARIA role) by default; it uses the `region` role, with a required
accessible name, only when its content is a significant, independently
navigable section — restating ARIA 1.2's own definition of `region`,
not a new KBDL policy. Nested surfaces preserve heading-level hierarchy
(a Panel inside a Card does not skip heading levels). Surface
boundaries must remain perceivable without color alone (a border,
spacing, or elevation cue must also be present) — restating the locked
component-state-clarity rule already established in
[principles.md §5.1](principles.md#51-locked-identity-rules). Surface
elevation maps to the existing approved five-level scale
([foundations/shape-depth.md §3.2](foundations/shape-depth.md#32-default-semantic-elevation-scale)):
Raised (Level 1) for Panel/Card, Floating (Level 2) for Tooltip/
Popover/Menu/Listbox popup, Modal (Level 3) for Dialog/Modal Dialog/
Drawer/Sheet, Temporary overlay (Level 4) for Toast — this document
introduces no new elevation, border, radius, spacing, or shadow value.
Scroll regions within a surface must remain keyboard-operable
(reachable by Tab, scrollable by arrow keys when focused) and must not
trap focus. Surfaces reflow at narrow widths and under enlarged text
per [§19](#19-responsive-transformation-policy); a card is never
automatically treated as an interactive landmark merely because it is
visually elevated.

- **`KBDL-CMP-053`** — A KBDL-008 surface **must** use native host-
  language structure or an ARIA role already dictated by an adopted
  specification when it provides the required semantics, before
  introducing a custom, non-native presentation.
  - Lifecycle status: Approved (extends the already-Approved native-
    semantics-first rule, `KBDL-CMP-002`, and the adopted ARIA 1.2
    `region` role definition, to this module's surfaces). Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-002` (KBDL-007), `KBDL-CMP-070`,
    `KBDL-CMP-094`, `KBDL-CMP-095`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§8](#8-surface-architecture).
  - Validation method: Manual native-structure review once implemented.

- **`KBDL-CMP-062`** — A KBDL-008 component **must not** apply an ARIA
  role or custom widget pattern where an already-approved native
  structure would supply the required behavior (for example, using
  `role="grid"` or a custom progress widget where a native `<table>`,
  `<progress>`, or `<meter>` element already meets the need).
  - Lifecycle status: Approved (restates `KBDL-CMP-053`/`002` as an
    explicit prohibition, distinguishing the general preference from
    the specific misuse it forbids). Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-053`, `KBDL-CMP-070`, `KBDL-CMP-105`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§8](#8-surface-architecture),
    [§17](#17-complex-presentation-architecture).
  - Validation method: Manual role-use review once implemented.

## 9. Required Surface Components

### 9.1 Container Surface

A neutral grouping surface with no semantics by default. May carry an
optional heading relationship (`aria-labelledby`) when it groups
labeled content. Content padding, overflow, and reflow follow existing
approved spacing foundations; no new dimension is introduced. Differs
from Panel by carrying no section-level identity (no default heading,
no `region` candidacy) and from Card by carrying no summary/preview
purpose.

- **`KBDL-CMP-054`** — Container Surface and Panel **must** remain
  semantically neutral unless their content qualifies for the `region`
  role per [§8](#8-surface-architecture); a `region` **must** carry an
  accessible name.
  - Lifecycle status: Approved (restates ARIA 1.2's `region` role
    definition). Provenance: Confirmed. Validation status: Not
    verified.
  - Related requirement: `KBDL-A11Y-002` (semantic structure).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§9.1](#91-container-surface),
    [§9.2](#92-panel).
  - Validation method: Manual semantic-structure review once
    implemented.

### 9.2 Panel

A section-level grouping surface with an optional heading and
description. Uses `region` semantics only when it is a significant,
independently navigable section (per `KBDL-CMP-054`); otherwise remains
neutral. Internal actions follow the KBDL-007 button/link contract
unchanged. Composes with loading/empty/error states
([§15](#15-system-state-architecture)). Differs from Container Surface
by optionally carrying section-level identity; differs from Dialog by
never requiring modality or focus containment; differs from Card by
never functioning as a summary/preview unit.

### 9.3 Card

A summary or preview surface with heading/content hierarchy, an
optional media relationship, and optional actions or a whole-card link.

- **`KBDL-CMP-055`** — A Card **must not** wrap a whole card in an
  interactive parent element while also placing interactive
  descendants inside it, and **must not** rely on hover alone to reveal
  an essential card action.
  - Lifecycle status: Approved (restates the native HTML prohibition on
    nested interactive elements and the already-Approved hover-
    independent-discoverability requirement,
    [responsive.md §24](responsive.md#24-hover-independent-discoverability)).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-RSP-019` (hover-independent
    discoverability), `KBDL-CMP-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§9.3](#93-card).
  - Validation method: Manual DOM-structure and keyboard review once
    implemented.

A card's selected or current state must not be communicated by color
alone, per `KBDL-CMP-004`'s already-Approved state-clarity rule,
applied here without change. The exact card-variant taxonomy (media-
forward, text-only, action-forward, and similar) is new KBDL-008
policy:

- **`KBDL-CMP-067`** — Adopt a defined card-variant taxonomy for
  media relationship, heading/content hierarchy, and action placement.
  - Lifecycle status: Recommended (new component-level taxonomy).
    Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-055`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§9.3](#93-card),
    [§33](#33-kbdl-008-decision-packet) item 1.
  - Validation method: Project-owner review (not yet performed).

### 9.4 Accordion Surface

Preserves the KBDL-007 disclosure-trigger contract
(`KBDL-CMP-021`-adjacent trigger semantics) unchanged. An accordion
item pairs one disclosure trigger with one panel, associated via
`aria-controls`/`aria-labelledby` per the adopted ARIA disclosure
pattern.

- **`KBDL-CMP-068`** — An accordion panel **must** remain programmatically
  associated with its disclosure trigger, expose its expanded/collapsed
  state on the trigger (not the panel), and **must not** move focus
  into a panel merely because it expands.
  - Lifecycle status: Approved (restates the adopted ARIA disclosure
    pattern's role/state definitions and the already-Approved KBDL-007
    disclosure-trigger contract). Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-021` (disclosure/menu trigger
    contract, KBDL-007).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§9.4](#94-accordion-surface).
  - Validation method: Manual ARIA-relationship review once
    implemented.

Whether an accordion permits multiple simultaneously open panels or
restricts to one is new policy:

- **`KBDL-CMP-069`** — Adopt a default accordion open-model (single-open
  or multiple-open) and state whether any item may be mandatorily open.
  - Lifecycle status: Recommended (new component-level policy).
    Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-068`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§9.4](#94-accordion-surface),
    [§33](#33-kbdl-008-decision-packet) item 2.
  - Validation method: Project-owner review (not yet performed).

### 9.5 Static Data Table

- **`KBDL-CMP-070`** — Static tabular data **must** use native `<table>`
  structure with a caption and correctly associated column/row headers;
  `grid`/`gridcell` ARIA roles **must not** be applied to non-interactive
  static data merely to gain keyboard styling or visual treatment.
  - Lifecycle status: Approved (restates the already-adopted WCAG 2.2
    SC 1.3.1 Info and Relationships and the native-semantics-first
    rule, `KBDL-CMP-002`). Provenance: Confirmed. Validation status:
    Not verified.
  - Related requirement: `KBDL-A11Y-###` (semantic structure,
    `accessibility.md §8`), `KBDL-CMP-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§9.5](#95-static-data-table),
    [§18.1](#181-interactive-grid) (distinction).
  - Validation method: Manual semantic-structure review once
    implemented.

Responsive behavior for wide tables (horizontal scroll, reflow, or an
alternate presentation such as a card transformation) is addressed in
[§33](#33-kbdl-008-decision-packet) item 17. This document does not
silently adopt the unapproved `KBDL-RSP-011` data-dense transformation
strategy as authority; `RSP-011` is cited only as related, unapproved
context (see [§35](#35-kbdl-006-approval-boundary-audit)).

## 10. Overlay Architecture

Status: `Approved` (`KBDL-CMP-056`, dictated outcome of the already-
approved focus, keyboard, and reading-order rules applied to layered
content).

Overlays are anchored (Tooltip, Popover, Menu, Listbox popup) or
viewport-level (Dialog, Modal Dialog, Alert Dialog, Drawer/Sheet);
modal or non-modal; transient (Tooltip, Toast) or persistent until
explicit dismissal (Dialog, Menu). Every overlay defines: trigger
ownership (KBDL-007, unchanged), surface ownership (this document),
opening, initial focus, focus containment (modal only), closing, focus
restoration, Escape behavior, outside-pointer behavior, backdrop
behavior, scroll locking (modal only), background inertness (modal
only), layering, nested-overlay behavior, responsive adaptation, safe-
area behavior, virtual-keyboard behavior, and full/reduced/no-motion
behavior. This document does not prescribe exact z-index values,
widths, heights, placement offsets, collision-detection algorithms,
scrim opacity, portal technology, top-layer implementation, or
JavaScript/framework behavior — any exact placement, sizing, nesting,
or stacking policy remains `Recommended` or `Unresolved`
([§33](#33-kbdl-008-decision-packet), [§40](#40-deferred-and-unresolved-items)).

- **`KBDL-CMP-056`** — Every overlay **must** define trigger ownership,
  surface ownership, opening, closing, and focus behavior appropriate
  to its modality, using only the anchored/viewport-level and modal/
  non-modal distinctions in this section.
  - Lifecycle status: Approved (dictated outcome of the already-adopted
    WCAG 2.2 focus, keyboard, and reading-order rules applied to
    layered content — a structural scope statement, not new policy).
    Provenance: Confirmed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-006`, `KBDL-CMP-007` (KBDL-007).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§10](#10-overlay-architecture).
  - Validation method: Manual scope-compliance review (performed, see
    implementation report).

- **`KBDL-CMP-057`** — Every non-modal overlay **must not** trap focus;
  Tab **must** move between the overlay and the rest of the page in
  logical order, and every operable element within any KBDL-008
  overlay **must** be reachable and operable by keyboard alone.
  - Lifecycle status: Approved (restates the already-adopted WCAG 2.2
    SC 2.1.1 Keyboard and SC 2.1.2 No Keyboard Trap, and the already-
    Approved KBDL-007 keyboard contract, `KBDL-CMP-007`, applied
    explicitly to non-modal overlays). Provenance: Confirmed.
    Validation status: Not verified.
  - Related requirement: `KBDL-CMP-007` (KBDL-007).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§10](#10-overlay-architecture),
    [§11.2](#112-popover-or-non-modal-dialog).
  - Validation method: Manual keyboard-trap review once implemented.

- **`KBDL-CMP-058`** — When an overlay's trigger element no longer
  exists at close time, focus **must** move to the nearest still-
  present ancestor or a documented fallback (e.g. the main content
  landmark), and **must never** be left unset.
  - Lifecycle status: Approved (dictated outcome of the already-adopted
    WCAG 2.2 SC 2.4.3 Focus Order — an unset focus target would violate
    the requirement that focus order remain determinable). Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-071`, `KBDL-CMP-079`, `KBDL-CMP-084`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§10](#10-overlay-architecture),
    [§20](#20-focus-and-modality).
  - Validation method: Manual focus-restoration review once
    implemented.

- **`KBDL-CMP-059`** — A critical error, destructive warning, or
  required instruction **must not** disappear (through timeout or
  automatic dismissal) without an accessible, persistent path to the
  same information remaining available.
  - Lifecycle status: Approved (restates the already-adopted WCAG 2.2
    SC 2.2.1 Timing Adjustable, extended to this module's dismissible
    surfaces generally, beyond the Toast-specific case in
    `KBDL-CMP-090`). Provenance: Confirmed. Validation status: Not
    verified.
  - Related requirement: `KBDL-CMP-090` (Toast-specific application).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§10](#10-overlay-architecture),
    [§21](#21-dismissal-and-persistence).
  - Validation method: Manual content-persistence review once
    implemented.

- **`KBDL-CMP-060`** — Full-motion, reduced-motion, and no-motion
  presentations of any KBDL-008 opening, closing, or transition
  behavior **must** preserve the same meaning and functionality.
  - Lifecycle status: Approved (restates the already-Approved motion-
    parity rule, [motion/accessibility-performance.md §1](motion/accessibility-performance.md#1-reduced-motion-and-no-motion-parity)).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: Motion parity rule (`motion/accessibility-performance.md §1`).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§10](#10-overlay-architecture),
    [§31](#31-theme-and-motion-validation-matrix).
  - Validation method: Manual reduced/no-motion parity review once
    implemented.

- **`KBDL-CMP-071`** — A modal overlay **must** render background
  content inert (unreachable by sequential navigation, screen-reader
  virtual cursor, or pointer) for as long as it is open, not merely
  visually dimmed.
  - Lifecycle status: Approved. Authority: the adopted WAI-ARIA 1.2
    `aria-modal` property definition, which specifies that assistive
    technology should restrict its reading and navigation to the modal
    element while it is active, directly requires background content
    to be excluded from that navigation — this is the primary source
    for "unreachable by ... screen-reader virtual cursor." The
    already-adopted WCAG 2.2 SC 2.4.3 Focus Order and SC 2.4.11 Focus
    Not Obscured support, but do not by themselves fully dictate, this
    outcome for pointer/sequential-navigation reachability. The
    approved KBDL-008 prompt's Overlay Architecture section explicitly
    requires "Background inertness" as a mandatory field for every
    modal overlay, which is the source for treating this as a complete,
    single normative rule rather than an inference from the standards
    alone. Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-006`, `KBDL-CMP-007` (KBDL-007
    focus/keyboard contracts).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§10](#10-overlay-architecture),
    [§11.5](#115-dialog), [§11.6](#116-modal-dialog).
  - Validation method: Manual focus-containment review once
    implemented.

## 11. Required Overlay Components

### 11.1 Tooltip

An informational, non-interactive surface describing its trigger.
Because the APG tooltip pattern is explicitly work-in-progress and
lacks task-force consensus, this document separates the accessibility
outcomes it inherits from already-adopted sources (`Approved`) from
KBDL's own timing, trigger, persistence, and placement policy
(`Recommended`), per [§4](#4-standards-interpretation-for-this-module).

- **`KBDL-CMP-072`** — A tooltip **must** contain only non-interactive
  text, **must** leave focus on its trigger, **must** be dismissible via
  Escape without moving focus, **must** remain visible while the
  trigger has either hover or focus, and **must never** be the sole
  source of its trigger's accessible name.
  - Lifecycle status: Approved. Authority, split by clause: "dismissible
    via Escape" and "remains visible while the trigger has hover or
    focus" restate the already-adopted WCAG 2.2 SC 1.4.13 Content on
    Hover or Focus, which dictates exactly these three properties
    (dismissible, hoverable, persistent). "Must never be the sole
    source of its trigger's accessible name" restates the already-
    Approved KBDL-007 accessible-naming requirement, `KBDL-CMP-003`,
    and the adopted WCAG 2.2 SC 4.1.2 Name, Role, Value — not SC
    1.4.13, which does not address naming. "Contains only non-
    interactive text" and "leaves focus on its trigger" are not
    dictated by SC 1.4.13 or the WAI-ARIA `tooltip` role definition
    alone (the ARIA 1.2 spec describes tooltip as advisory but does not
    itself prohibit interactive descendants); these two clauses are
    normative because the approved KBDL-008 prompt explicitly requires
    "Informational, non-interactive purpose" and "Interactive-content
    prohibition" as mandatory Tooltip fields. This requirement does not
    treat the APG tooltip pattern (explicitly non-consensus, see
    [§4](#4-standards-interpretation-for-this-module)) as a source for
    any clause. Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-003`, `KBDL-CMP-016`, `KBDL-CMP-017`
    (KBDL-007 icon-only naming).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11.1](#111-tooltip).
  - Validation method: Manual hover/focus and accessible-name review
    once implemented.

A tooltip containing controls must instead use Popover
([§11.2](#112-popover-or-non-modal-dialog)) or Menu
([§11.3](#113-menu-surface)) semantics, never a tooltip role.

- **`KBDL-CMP-073`** — Adopt a KBDL tooltip trigger, delay, persistence,
  and placement policy (when a tooltip appears/disappears on hover
  versus focus, and default placement behavior).
  - Lifecycle status: Recommended (new KBDL-specific timing/placement
    policy, not dictated by the non-consensus APG tooltip pattern).
    Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-072`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11.1](#111-tooltip),
    [§33](#33-kbdl-008-decision-packet) item 3.
  - Validation method: Project-owner review (not yet performed).

### 11.2 Popover or Non-Modal Dialog

Supplemental interactive content anchored to a trigger, non-modal:
focus is not contained, Tab moves normally between the popover and the
rest of the page, Escape closes it and returns focus to the trigger,
and an outside pointer interaction closes it by default. Differs from
Tooltip (interactive content permitted), Menu (arbitrary interactive
content rather than a fixed command/choice list), and Modal Dialog (no
focus containment).

- **`KBDL-CMP-074`** — Adopt a popover taxonomy (which supplemental-
  content cases use a popover versus a menu or modal dialog) and a
  default dismissal model (outside-pointer, Escape, and focus-loss
  behavior).
  - Lifecycle status: Recommended (new component-level taxonomy and
    dismissal policy). Provenance: Assumed. Validation status: Not
    applicable.
  - Related requirement: `KBDL-CMP-072`, `KBDL-CMP-078`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11.2](#112-popover-or-non-modal-dialog),
    [§33](#33-kbdl-008-decision-packet) item 4.
  - Validation method: Project-owner review (not yet performed).

### 11.3 Menu Surface

Preserves the KBDL-007 menu-button trigger contract
(`KBDL-CMP-021`-adjacent) unchanged.

- **`KBDL-CMP-075`** — A menu surface **must** expose `menu`/`menuitem`
  (or `menuitemcheckbox`/`menuitemradio`) roles and **must** maintain the
  trigger's `aria-expanded` and `aria-controls` relationship established
  by KBDL-007 without redefining it.
  - Lifecycle status: Approved (restates the adopted WAI-ARIA 1.2 menu
    role definitions and the already-Approved KBDL-007 trigger
    contract). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-021` (KBDL-007 disclosure/menu
    trigger).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11.3](#113-menu-surface).
  - Validation method: Manual ARIA-relationship review once
    implemented.

Menu semantics are used only for menu-like command or choice behavior,
never merely for visual dropdown navigation when ordinary links and
lists provide correct semantics. The exact interaction model (type-
ahead, submenu behavior, closing specifics) is new policy:

- **`KBDL-CMP-076`** — Adopt a menu-surface interaction and dismissal
  model: focus movement, type-ahead behavior, submenu opening/closing,
  and return-focus behavior on close.
  - Lifecycle status: Recommended (new component-level interaction
    policy; the underlying APG menu pattern is not automatically
    Approved). Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-075`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11.3](#113-menu-surface),
    [§33](#33-kbdl-008-decision-packet) item 5.
  - Validation method: Project-owner review (not yet performed).

### 11.4 Listbox Popup

Preserves the KBDL-007 combobox input, value, and active-option
relationship unchanged.

- **`KBDL-CMP-077`** — A listbox popup **must** expose `listbox`/`option`
  roles and **must** maintain the KBDL-007 combobox's active-descendant
  relationship without redefining it; using a listbox popup **must not**
  be treated as approving the KBDL-007 custom-combobox-justification
  recommendation (`KBDL-CMP-029`).
  - Lifecycle status: Approved (restates the adopted WAI-ARIA 1.2
    listbox role definitions and the already-Approved KBDL-007
    combobox contract). Provenance: Confirmed. Validation status: Not
    verified.
  - Related requirement: `KBDL-CMP-028` (combobox ARIA contract,
    KBDL-007). `KBDL-CMP-029` cited as unapproved context only.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11.4](#114-listbox-popup).
  - Validation method: Manual ARIA-relationship review once
    implemented.

### 11.5 Dialog

A viewport-level or anchored surface with an accessible name (via
`aria-labelledby`) and optional description (via `aria-describedby`).

- **`KBDL-CMP-078`** — A dialog **must** have a programmatically
  associated accessible name, **must** provide a visible and keyboard-
  operable close mechanism, and long content **must** remain scrollable
  without losing access to a sticky action area where one exists.
  - Lifecycle status: Approved (restates the already-adopted WCAG 2.2
    SC 4.1.2 Name, Role, Value and SC 2.1.1 Keyboard). Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-003`, `KBDL-CMP-007`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11.5](#115-dialog).
  - Validation method: Manual accessible-name and keyboard review once
    implemented.

### 11.6 Modal Dialog

- **`KBDL-CMP-079`** — A surface **must not** be labeled or presented as
  modal unless it satisfies, for all users including assistive-
  technology users: background inertness (`KBDL-CMP-071`), a defined
  initial focus, full focus containment, a defined return-focus target,
  and Escape-key closing (unless an explicit, documented exception
  applies, e.g. a destructive confirmation requiring explicit
  acknowledgement).
  - Lifecycle status: Approved (restates `KBDL-CMP-071` and the
    already-adopted WCAG 2.2 SC 2.1.2 No Keyboard Trap, applied to the
    definition of modality itself — this is the "modal integrity"
    rule). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-071`, `KBDL-CMP-078`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11.6](#116-modal-dialog).
  - Validation method: Manual modality-compliance review once
    implemented.

Exact modal sizing, placement, and nested-modal policy are new
decisions:

- **`KBDL-CMP-080`** — Adopt a modal sizing model (how a modal dialog's
  dimensions relate to viewport size and content) and a nested-modal
  policy (whether a second modal may open from within an open modal, or
  whether KBDL restricts to one modal at a time).
  - Lifecycle status: Recommended (new component-level sizing and
    nesting policy). Provenance: Assumed. Validation status: Not
    applicable.
  - Related requirement: `KBDL-CMP-079`, `KBDL-CMP-084`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11.6](#116-modal-dialog),
    [§33](#33-kbdl-008-decision-packet) item 6.
  - Validation method: Project-owner review (not yet performed).

### 11.7 Alert Dialog

- **`KBDL-CMP-081`** — An alert dialog **must** be reserved for urgent
  messages requiring an explicit user response, using the `alertdialog`
  role, and **must not** be used for routine or successful informational
  feedback (see Alert, [§14.2](#142-alert)).
  - Lifecycle status: Approved (restates the adopted WAI-ARIA 1.2
    `alertdialog` role definition). Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-079` (modal contract it inherits).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11.7](#117-alert-dialog).
  - Validation method: Manual role-use review once implemented.

An alert dialog for a destructive action favors presenting the least-
destructive action as the visually primary choice, consistent with
KBDL-007's existing consequential-action requirement
(`components-core.md §23`); this document does not silently approve
the KBDL-007 button-hierarchy recommendation (`KBDL-CMP-015`) or form-
action-row ordering (`KBDL-CMP-036`) as authority for the alert
dialog's action area.

### 11.8 Drawer and Sheet

- **`KBDL-CMP-082`** — A drawer or sheet used for collapsed navigation
  **must** preserve the KBDL-007 navigation-trigger and source-order
  rules unchanged, and **must not** define or approve an exact
  responsive collapse threshold.
  - Lifecycle status: Approved (scope-control requirement, restates
    `KBDL-CMP-005`/`KBDL-CMP-052`). Provenance: Confirmed. Validation
    status: Not applicable.
  - Related requirement: `KBDL-CMP-041` (KBDL-007 navigation collapse
    threshold — cited as unapproved context/contingent dependency
    only, not approved by this requirement).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11.8](#118-drawer-and-sheet).
  - Validation method: Manual scope-compliance review (performed, see
    implementation report).

The general drawer/sheet taxonomy and default modality (edge-attached
placement, modal versus non-modal variants) is new policy, independent
of any exact navigation-collapse threshold:

- **`KBDL-CMP-083`** — Adopt a drawer/sheet taxonomy and a default
  modality (modal or non-modal) for each conceptual variant.
  - Lifecycle status: Recommended (new component-level taxonomy).
    Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-082`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11.8](#118-drawer-and-sheet),
    [§33](#33-kbdl-008-decision-packet) item 7.
  - Validation method: Project-owner review (not yet performed). This
    item's approval would not approve any navigation-collapse
    threshold; a drawer used for collapsed navigation remains bound by
    `KBDL-CMP-041`'s existing contingent status (KBDL-007).

## 12. Overlay Layering and Nesting

- **`KBDL-CMP-084`** — At any moment, exactly one open overlay **must**
  own the Escape key and receive newly opened focus; closing an overlay
  **must** return focus and Escape ownership to its opener (the
  previously active overlay, or the original trigger if none).
  - Lifecycle status: Approved (dictated outcome of the already-adopted
    WCAG 2.2 SC 2.4.3 Focus Order and SC 2.1.2 No Keyboard Trap applied
    to nested layered content — not a new policy choice, since any
    other outcome would create an indeterminate or trapped focus
    state). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-071`, `KBDL-CMP-079`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§12](#12-overlay-layering-and-nesting).
  - Validation method: Manual nested-focus review once implemented.

The maximum number of simultaneously open overlays, and whether more
than one modal may ever be open at once beyond the one-at-a-time
default implied by `KBDL-CMP-080`, is new policy:

- **`KBDL-CMP-085`** — Adopt an overlay-nesting policy: the maximum
  practical stacking depth for non-modal overlays (menus inside
  dialogs, tooltips inside overlays) and confirmation that no more than
  one modal dialog is open at a time.
  - Lifecycle status: Recommended (new component-level policy).
    Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-080`, `KBDL-CMP-084`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§12](#12-overlay-layering-and-nesting),
    [§33](#33-kbdl-008-decision-packet) item 8.
  - Validation method: Project-owner review (not yet performed).

This document does not approve exact layer numbers, an exact z-index
scale, an unlimited nesting model, or a specific portal strategy (see
[§40](#40-deferred-and-unresolved-items)).

## 13. Feedback Architecture

Status: `Approved` (`KBDL-CMP-086`, extends `KBDL-A11Y-031`).

- **`KBDL-CMP-086`** — A feedback component's live-region role (`alert`,
  `status`, `log`, or no live role) **must** be chosen by the update's
  urgency and user impact, not by the component's visual name; routine
  or successful updates **must not** use the assertive `alert` role.
  - Lifecycle status: Approved (restates `KBDL-A11Y-031` and the
    adopted WAI-ARIA 1.2 live-region role definitions). Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-031` (accessibility.md §35).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§13](#13-feedback-architecture).
  - Validation method: Manual live-region role review once implemented.

- **`KBDL-CMP-061`** — Every meaningful component state introduced by
  this document (loading, empty, error, success, selected, disabled)
  **must** be distinguishable without depending on color alone.
  - Lifecycle status: Approved (restates the locked component-state-
    clarity rule, [principles.md §5.1](principles.md#51-locked-identity-rules),
    and `KBDL-CMP-004`, applied explicitly to the states this document
    introduces). Provenance: Confirmed. Validation status: Not
    verified.
  - Related requirement: `KBDL-CMP-004` (KBDL-007), `KBDL-CMP-097`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§13](#13-feedback-architecture),
    [§15](#15-system-state-architecture).
  - Validation method: Manual color-independence review once
    implemented.

Feedback components are further distinguished by persistence
(transient versus persistent), interruption level, and recovery-action
relationship, documented per component below.

## 14. Required Feedback Components

### 14.1 Inline Feedback

- **`KBDL-CMP-087`** — Inline feedback **must** carry a programmatic
  relationship to the content or control it describes (e.g.
  `aria-describedby`), and **must not** rely on icon or color alone to
  convey its meaning (information, success, warning, error).
  - Lifecycle status: Approved (restates `KBDL-CMP-004`'s already-
    Approved state-clarity rule and the adopted WCAG 2.2 SC 1.4.1 Use
    of Color). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-004`. Distinct from KBDL-007 field
    validation (`components-core.md §23`), which owns the field/error
    relationship itself; this requirement covers the feedback surface's
    own presentation.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14.1](#141-inline-feedback).
  - Validation method: Manual review once implemented.

### 14.2 Alert

- **`KBDL-CMP-088`** — An alert **must** be reserved for important,
  time-sensitive messages using the `alert` role, **must not** move
  focus by default, and **must not** be used for routine or successful
  updates.
  - Lifecycle status: Approved. Authority, split by clause: "important,
    time-sensitive messages" and "must not move focus by default"
    restate the adopted WAI-ARIA 1.2 `alert` role definition, which
    specifies an assertive live region for important, time-sensitive
    information without describing any inherent focus-moving behavior.
    "Must not be used for routine or successful updates" is not itself
    dictated by the ARIA `alert` role definition (which describes what
    the role announces, not which messages a component must avoid);
    this restriction is normative because the approved KBDL-008 prompt
    explicitly requires "Do not use alert for every successful or
    routine update" as a mandatory Alert constraint. Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-086`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14.2](#142-alert).
  - Validation method: Manual role-use review once implemented.

### 14.3 Banner

A page- or section-level message with a heading, severity meaning, and
actions. The exact severity taxonomy and visual variant set are new
policy:

- **`KBDL-CMP-089`** — Adopt a banner severity taxonomy (informational,
  success, warning, critical, or a subset) and its visual variant set,
  distinct from the site header/banner landmark.
  - Lifecycle status: Recommended (new component-level taxonomy).
    Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-088`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14.3](#143-banner),
    [§33](#33-kbdl-008-decision-packet) item 9.
  - Validation method: Project-owner review (not yet performed).

### 14.4 Toast or Snackbar

- **`KBDL-CMP-090`** — Critical information **must not** be presented
  only in a transient toast without an accessible, persistent path also
  being available; a toast **must not** move focus to itself by
  default; sensitive information **must not** be exposed in a toast.
  - Lifecycle status: Approved. Authority, split by clause: "sensitive
    information must not be exposed" extends the existing KBDL
    security-safe-disclosure principle,
    `components-core.md §37`. "Critical information must not be
    presented only in a transient toast without a persistent path" and
    "must not move focus to itself by default" are not directly
    dictated by WCAG 2.2 SC 2.2.1 Timing Adjustable (which governs
    user-adjustable time limits on content generally, not the specific
    toast/persistent-path pattern) or by `KBDL-A11Y-031` (which
    requires programmatic determinability, not a persistence
    guarantee); these two clauses are normative because the approved
    KBDL-008 prompt explicitly lists both as mandatory Toast/Snackbar
    "Do not" constraints. SC 2.2.1's adjustable-timing principle is
    cited as supporting rationale, not as the direct source of the
    persistent-path requirement. Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-086`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14.4](#144-toast-or-snackbar).
  - Validation method: Manual content-classification review once
    implemented.

Exact auto-dismiss timing, queue size, and stacking/placement are new
policy:

- **`KBDL-CMP-091`** — Adopt a toast lifecycle model: auto-dismiss
  timing (or persistence-until-dismissed default), pause-on-interaction
  behavior where timed, queue size, duplicate suppression, and stacking
  direction/placement.
  - Lifecycle status: Recommended (new component-level timing and
    queueing policy). Provenance: Assumed. Validation status: Not
    applicable.
  - Related requirement: `KBDL-CMP-090`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14.4](#144-toast-or-snackbar),
    [§33](#33-kbdl-008-decision-packet) item 10.
  - Validation method: Project-owner review (not yet performed).

### 14.5 Status Region and Log

- **`KBDL-CMP-092`** — A status region or log **must** use the correct
  live-region politeness and atomicity setting for its update pattern,
  and **must not** re-announce a visual message without a meaningful
  change (duplicate-announcement prevention).
  - Lifecycle status: Approved (restates `KBDL-A11Y-031` and the
    adopted WAI-ARIA 1.2 `status`/`log` role and `aria-live`/`aria-atomic`
    definitions). Provenance: Confirmed. Validation status: Not
    verified.
  - Related requirement: `KBDL-CMP-086`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14.5](#145-status-region-and-log).
  - Validation method: Manual live-region review once implemented.

### 14.6 Badge or Count Indicator

- **`KBDL-CMP-093`** — A badge conveying meaningful information (a
  count or status) **must** have an accessible text equivalent; a
  purely decorative badge carries no required semantics and **must not**
  be exposed to assistive technology as if it were meaningful.
  - Lifecycle status: Approved (restates the adopted WCAG 2.2 SC 1.1.1
    Non-text Content and SC 4.1.2 Name, Role, Value). Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-004`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14.6](#146-badge-or-count-indicator).
  - Validation method: Manual accessible-text review once implemented.

### 14.7 Progress Indicator

- **`KBDL-CMP-094`** — A progress indicator **must** expose an
  accessible name and, for determinate progress, its current value
  programmatically (native `<progress>` or the ARIA `progressbar` role);
  indeterminate progress **must** be identifiable as such, not
  presented as a stalled determinate value.
  - Lifecycle status: Approved (restates the adopted WAI-ARIA 1.2
    `progressbar` role definition and native `<progress>` semantics).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-086`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14.7](#147-progress-indicator).
  - Validation method: Manual role/value review once implemented.

### 14.8 Meter

- **`KBDL-CMP-095`** — A meter **must** expose its current value and
  minimum/maximum (and low/high/optimum where applicable)
  programmatically (native `<meter>` or the ARIA `meter` role), and
  **must not** be used interchangeably with Progress Indicator.
  - Lifecycle status: Approved (restates the adopted WAI-ARIA 1.2
    `meter` role definition and native `<meter>` semantics). Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-094` (distinction).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14.8](#148-meter).
  - Validation method: Manual role/value review once implemented.

### 14.9 Skeleton

- **`KBDL-CMP-096`** — A skeleton placeholder **must** be hidden from
  assistive technology as decorative, and an equivalent loading
  announcement **must** be available through a separate status
  mechanism (`KBDL-CMP-086`); a skeleton **must not** expose meaningless
  placeholder shapes as if they were content.
  - Lifecycle status: Approved. Authority, split by clause: "hidden from
    assistive technology as decorative" restates the adopted WAI-ARIA
    1.2 `aria-hidden` semantics for purely decorative content. "An
    equivalent loading announcement must be available through a
    separate status mechanism" restates `KBDL-A11Y-031`. "Must not
    expose meaningless placeholder shapes as if they were content" is
    not itself dictated by either of those sources; it is normative
    because the approved KBDL-008 prompt explicitly requires "Decorative
    accessibility treatment" and "Equivalent loading announcement" as
    mandatory Skeleton fields, which together imply placeholder shapes
    must not be presented as meaningful content. Provenance: Confirmed.
    Validation status: Not verified.
  - Related requirement: `KBDL-CMP-086`, `KBDL-CMP-098`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14.9](#149-skeleton).
  - Validation method: Manual accessibility-tree review once
    implemented.

Exact shimmer, pulse, timing, and density values remain unapproved (see
[§40](#40-deferred-and-unresolved-items)).

## 15. System-State Architecture

Status: `Approved` (`KBDL-CMP-097`, extends `KBDL-A11Y-031` and the
locked component-state-clarity rule).

- **`KBDL-CMP-097`** — Every system state (loading, empty, error,
  offline, and similar) **must** expose a programmatically determinable
  title and explanation, and **must not** rely on illustration or color
  alone to convey its meaning or user impact.
  - Lifecycle status: Approved (restates `KBDL-A11Y-031` and the locked
    component-state-clarity rule, [principles.md §5.1](principles.md#51-locked-identity-rules)).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-004`, `KBDL-A11Y-031`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§15](#15-system-state-architecture).
  - Validation method: Manual review once implemented.

System states are distinguished at component, section, page, and
application level; see [§16](#16-required-system-state-components) for
each required state's cause, recovery behavior, and difference from
adjacent states.

## 16. Required System-State Components

### 16.1 Loading State

- **`KBDL-CMP-098`** — During incremental loading, already-visible
  content **must** remain available, and a pending operation **must**
  prevent duplicate submission of the same action until it completes or
  fails.
  - Lifecycle status: Approved (extends the already-Approved KBDL-007
    submit-loading/duplicate-submission-prevention contract,
    `components-core.md §23`, to the surface-level loading indicator).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: KBDL-007 submit-action loading contract
    (`components-core.md §23`), `KBDL-CMP-094`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§16.1](#161-loading-state).
  - Validation method: Manual review once implemented.

### 16.2 Empty State

Genuine absence of content, distinct from a first-use state, a user-
cleared state, and a permission-limited state. The exact empty-state
taxonomy, illustration policy, and action hierarchy are new policy,
and this state is explicitly distinguished from No-Results below:

- **`KBDL-CMP-099`** — Adopt an empty-state taxonomy (first-use, user-
  cleared, permission-limited, and genuinely-empty cases), an
  illustration-use policy, and an action-hierarchy default.
  - Lifecycle status: Recommended (new component-level taxonomy).
    Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-097`, `KBDL-CMP-100` (distinction
    from No-Results).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§16.2](#162-empty-state),
    [§33](#33-kbdl-008-decision-packet) item 11.
  - Validation method: Project-owner review (not yet performed).

### 16.3 No-Results State

- **`KBDL-CMP-100`** — A no-results state **must** preserve the user's
  entered query or filter criteria, and **must** be distinguished from
  Empty State by relating to a current query/filter rather than a
  genuine absence of content.
  - Lifecycle status: Approved. Authority: this requirement is normative
    because the approved KBDL-008 prompt explicitly requires
    "Preservation of entered criteria" as a mandatory No-Results State
    field. WCAG 2.2 SC 3.3.7 Redundant Entry (which prohibits requiring
    re-entry of information already supplied earlier in the same
    process) is cited as supporting rationale by analogy, not as a
    direct restatement — SC 3.3.7 governs multi-step process re-entry
    generally and does not by itself mandate preserving search/filter
    state specifically on a no-results result. Provenance: Confirmed.
    Validation status: Not verified.
  - Related requirement: `KBDL-CMP-099`. This requirement does not
    approve the unapproved KBDL-007 search-field model (`KBDL-CMP-025`
    — cited as unapproved context only).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§16.3](#163-no-results-state).
  - Validation method: Manual data-preservation review once
    implemented.

### 16.4 Error State

- **`KBDL-CMP-101`** — An error state **must** state whether it is
  recoverable or blocking, and a recoverable error **must** provide a
  retry or alternative action; an error **must not** expose stack
  traces, internal exception details, credentials, or private data.
  - Lifecycle status: Approved. Authority, split by clause: that an
    error must be identified and described restates the already-adopted
    WCAG 2.2 SC 3.3.1 Error Identification, which requires errors be
    identified and described in text, but does not itself require
    classifying an error as "recoverable or blocking" or specifying a
    "retry or alternative action" — SC 3.3.1 governs identification,
    not remediation-path taxonomy. The recoverable/blocking
    classification and the retry/alternative-action requirement are
    normative because the approved KBDL-008 prompt explicitly requires
    "Recoverable versus blocking error," "Retry," and "Alternative
    action" as mandatory Error State fields, consistent with the
    already-Approved Technical Utility recovery-support principle,
    [principles.md §3](principles.md#3-technical-utility). The
    prohibition on exposing stack traces, internal exception details,
    credentials, or private data restates `KBDL-CMP-064`. Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-097`, `KBDL-CMP-064`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§16.4](#164-error-state).
  - Validation method: Manual review once implemented.

The exact severity taxonomy for error and broader system-state
recovery (a hierarchy distinguishing maintenance, temporary
unavailability, and degraded service) is new policy:

- **`KBDL-CMP-102`** — Adopt an error/system-state severity taxonomy and
  a recovery hierarchy distinguishing maintenance, unavailable, and
  degraded conditions, including expected escalation between them.
  - Lifecycle status: Recommended (new component-level taxonomy).
    Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-101`, `KBDL-CMP-103`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§16.4](#164-error-state),
    [§16.8](#168-maintenance-unavailable-and-degraded-state),
    [§33](#33-kbdl-008-decision-packet) item 12.
  - Validation method: Project-owner review (not yet performed).

### 16.5 Offline and Reconnecting State

- **`KBDL-CMP-103`** — An offline, reconnecting, or queued-action
  indicator **must not** claim a saved, synchronized, or completed
  status before the relevant system has confirmed that state.
  - Lifecycle status: Approved (extends the already-Approved KBDL
    correctness/safety principle, [principles.md §4](principles.md#4-relationship-between-luxury-and-utility)
    item 1, and the existing KBDL-007 form-recovery data-preservation
    pattern). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-097`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§16.5](#165-offline-and-reconnecting-state).
  - Validation method: Manual claim-accuracy review once implemented.

### 16.6 Permission Denied and Restricted State

- **`KBDL-CMP-104`** — A permission-denied or restricted state **must
  not** use disabled or hidden UI as an authorization boundary, and
  **must not** unnecessarily disclose whether a protected resource
  exists when doing so creates a privacy or security risk (see Not
  Found, [§16.7](#167-not-found-state)).
  - Lifecycle status: Approved (extends the existing KBDL security
    principle already established in `components-core.md §37`,
    "a disabled button is not access control"). Provenance: Confirmed.
    Validation status: Not verified.
  - Related requirement: `KBDL-CMP-097`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§16.6](#166-permission-denied-and-restricted-state).
  - Validation method: Manual security-review once implemented.

### 16.7 Not Found State

Distinguished from Permission Denied: a not-found state does not
require revealing whether a protected resource exists, per
`KBDL-CMP-104`, applied here without change.

### 16.8 Maintenance, Unavailable, and Degraded State

Uses the severity taxonomy and recovery hierarchy from `KBDL-CMP-102`
once approved; does not invent service-level commitments or recovery
time estimates.

### 16.9 System Status

Uses the Status Region/Log live-region model (`KBDL-CMP-092`) for its
update stream, distinct from a transient Alert or Toast
(`KBDL-CMP-088`, `KBDL-CMP-090`).

## 17. Complex-Presentation Architecture

Complex-presentation components apply a composite-widget interaction
model only when genuinely required; static content never receives an
interactive role merely for styling (`KBDL-CMP-070`, applied
consistently to Interactive Grid, Tree, and Data Visualization below).

## 18. Required Complex-Presentation Components

### 18.1 Interactive Grid

An interactive grid creates a composite-widget keyboard model (roving
tabindex, arrow-key cell navigation) distinct from Static Data Table.
Because the APG grid pattern is not automatically `Approved`
([§4](#4-standards-interpretation-for-this-module)), the threshold for
when grid semantics are justified, and the exact keyboard/selection/
editing model, are new policy:

- **`KBDL-CMP-105`** — Adopt a grid-versus-table threshold (when
  interactive selection, editing, or cell-level navigation justifies
  grid semantics over a static table) and the resulting composite-
  widget keyboard model (focus movement, selection, and header
  relationship).
  - Lifecycle status: Recommended (new component-level threshold and
    interaction model; the APG grid pattern is not automatically
    Approved). Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-070` (distinction from Static Data
    Table). `KBDL-RSP-011` (data-dense strategy, KBDL-006) is cited
    only as related unapproved context, not adopted as authority.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§18.1](#181-interactive-grid),
    [§33](#33-kbdl-008-decision-packet) item 13.
  - Validation method: Project-owner review (not yet performed).

Exact virtualization, column-resizing, column-reordering, and pinning
behavior remain later implementation decisions, out of scope here.

### 18.2 Tree and Treegrid

- **`KBDL-CMP-106`** — Adopt a tree/treegrid justification threshold
  (when hierarchical, tabular, or combined interaction is genuinely
  required) and the resulting expansion, focus-movement, and selection
  model.
  - Lifecycle status: Recommended (new component-level threshold and
    interaction model; the APG tree pattern is not automatically
    Approved). Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-105` (distinction), `KBDL-CMP-068`
    (distinction from Accordion).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§18.2](#182-tree-and-treegrid),
    [§33](#33-kbdl-008-decision-packet) item 14.
  - Validation method: Project-owner review (not yet performed).

### 18.3 Carousel

- **`KBDL-CMP-107`** — Where a carousel rotates automatically, it
  **must** provide a mechanism to pause, stop, or hide the rotation, per
  the already-adopted WCAG 2.2 SC 2.2.2 Pause, Stop, Hide.
  - Lifecycle status: Approved (restates the already-adopted WCAG 2.2
    SC 2.2.2). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-108`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§18.3](#183-carousel).
  - Validation method: Manual pause/stop/hide review once implemented.

Whether KBDL permits automatic rotation by default at all, and any
exact rotation interval, are new policy:

- **`KBDL-CMP-108`** — Adopt a default policy on whether carousels
  rotate automatically without user action, and, if so, the rotation
  interval and hover/focus-pause behavior.
  - Lifecycle status: Recommended (new component-level policy).
    Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-107`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§18.3](#183-carousel),
    [§33](#33-kbdl-008-decision-packet) item 15.
  - Validation method: Project-owner review (not yet performed).

### 18.4 Data Visualization

- **`KBDL-CMP-109`** — A data visualization **must** provide a non-
  color-dependent encoding (pattern, shape, or direct label) for every
  meaningful distinction, a text or data-table alternative, and
  keyboard-accessible access to any interactive data point, mapped to
  the already-approved Data-display theme roles
  ([themes/semantic-roles.md §1.6](themes/semantic-roles.md#16-media-and-decorative-context)).
  - Lifecycle status: Approved (restates the already-adopted WCAG 2.2
    SC 1.4.1 Use of Color, SC 1.3.1 Info and Relationships, and SC
    2.1.1 Keyboard, applied to chart content, using the existing
    approved Data-display roles rather than inventing new ones).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: Data-display foreground/grid/emphasis roles
    ([themes/semantic-roles.md §1.6](themes/semantic-roles.md#16-media-and-decorative-context)).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§18.4](#184-data-visualization).
  - Validation method: Manual review once implemented.

The exact chart taxonomy, tooltip behavior, and interaction model are
new policy; this document does not approve a data-visualization color
palette (the palette itself remains a separate, unapproved theme
matter, see [§40](#40-deferred-and-unresolved-items)):

- **`KBDL-CMP-110`** — Adopt a data-visualization chart taxonomy,
  tooltip-interaction behavior, and keyboard-navigation model for
  interactive charts, independent of the still-unapproved exact
  palette.
  - Lifecycle status: Recommended (new component-level taxonomy and
    interaction model). Provenance: Assumed. Validation status: Not
    applicable.
  - Related requirement: `KBDL-CMP-109`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§18.4](#184-data-visualization),
    [§33](#33-kbdl-008-decision-packet) item 16.
  - Validation method: Project-owner review (not yet performed).

## 19. Responsive Transformation Policy

Any transformation such as popover-to-sheet, dialog-to-full-screen,
table-to-cards, or multi-column overlay-to-single-column is new
component policy:

- **`KBDL-CMP-111`** — Adopt content-driven responsive transformation
  patterns for overlays and tabular data (e.g., a dialog becoming full-
  screen, a table becoming cards, a popover becoming a sheet) at
  narrow widths, independent of the exact unapproved breakpoint values
  that would trigger them.
  - Lifecycle status: Recommended (new component-level transformation
    policy; the exact trigger point depends on the eventual approved
    `KBDL-RSP-002` breakpoint values, cited here only as related
    context, not as authority). Provenance: Assumed. Validation
    status: Not applicable.
  - Related requirement: `KBDL-CMP-070`, `KBDL-CMP-080`,
    `KBDL-RSP-002` (eventual, unapproved).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§19](#19-responsive-transformation-policy),
    [§33](#33-kbdl-008-decision-packet) item 17.
  - Validation method: Project-owner review (not yet performed).

## 20. Focus and Modality

Every applicable component defines trigger focus before opening,
initial focus, focus order, focus containment (modal only), background
inertness (modal only), focus escape (non-modal), close-action focus,
Escape behavior, and a return-focus target, per
`KBDL-CMP-071`/`KBDL-CMP-079`/`KBDL-CMP-084` above. Focus must never be
trapped in non-modal content, must never enter inert background
content, and must never be returned to an element that no longer
exists (in which case focus moves to the nearest still-present
ancestor or a documented fallback, e.g. the main content landmark).

## 21. Dismissal and Persistence

Explicit close, Escape dismissal, outside-pointer dismissal, focus-loss
dismissal, action-completion dismissal, and timeout dismissal are
documented per component above. New defaults for outside-click
dismissal, automatic timeout, Escape-dismissal exceptions, persistent-
versus-transient behavior, undo duration, and queueing are recorded in
[§33](#33-kbdl-008-decision-packet) (`KBDL-CMP-074`, `KBDL-CMP-080`,
`KBDL-CMP-091`) rather than assumed. Critical errors, destructive
warnings, and required instructions must not disappear without an
accessible, persistent path remaining available (`KBDL-CMP-090`).

## 22. Status Communication and Live Regions

See [§13](#13-feedback-architecture) (`KBDL-CMP-086`) and
[§14.5](#145-status-region-and-log) (`KBDL-CMP-092`). Focus is never
moved merely to force an announcement; visual messages are not
announced repeatedly without meaningful change; an announcement does
not expose sensitive content unnecessarily (`KBDL-CMP-064`,
[§23](#23-security-and-privacy)).

## 23. Security and Privacy

Future KBDL-008 implementations **must**: avoid exposing credentials,
tokens, private keys, personal data, or sensitive values in feedback,
badges, previews, toasts, or notifications; avoid displaying stack
traces or internal exception details (`KBDL-CMP-101`); avoid using
disabled or hidden UI as authorization (`KBDL-CMP-104`); preserve
server-side authentication and authorization; avoid revealing whether
protected resources exist when doing so creates a privacy risk
(`KBDL-CMP-104`); avoid claiming queued, saved, synchronized, or
completed status before confirmation (`KBDL-CMP-103`); prevent repeated
destructive actions while an operation is pending (`KBDL-CMP-098`);
redact sensitive content from diagnostic references; avoid exposing
restricted data through data visualizations, tooltips, table exports,
or hidden series (`KBDL-CMP-109`); and preserve data-integrity warnings
during offline or stale-data states (`KBDL-CMP-103`). This document
does not define authentication architecture, authorization
architecture, database permissions, backend retry logic, storage
design, encryption architecture, or API design.

- **`KBDL-CMP-063`** — A KBDL-008 component **must not** claim a saved,
  synchronized, queued, or completed status before the relevant system
  has confirmed that state, for any feedback or system-state surface
  this document defines.
  - Lifecycle status: Approved (restates the already-Approved
    correctness/safety priority, [principles.md §4](principles.md#4-relationship-between-luxury-and-utility)
    item 1, as a general baseline; `KBDL-CMP-103` states its Offline/
    Reconnecting-specific application). Provenance: Confirmed.
    Validation status: Not verified.
  - Related requirement: `KBDL-CMP-103` (specific application).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§23](#23-security-and-privacy).
  - Validation method: Manual claim-accuracy review once implemented.

- **`KBDL-CMP-064`** — A KBDL-008 component **must not** expose
  credentials, tokens, private keys, personal data, stack traces, or
  internal diagnostic identifiers in any user-facing feedback surface.
  - Lifecycle status: Approved (extends the existing KBDL security
    principle already established in
    [components-core.md §37](components-core.md#37-security-and-privacy-in-components)
    as a general baseline; `KBDL-CMP-101` and `KBDL-CMP-104` state its
    Error-State- and Permission/Not-Found-specific applications).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-101`, `KBDL-CMP-104` (specific
    applications).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§23](#23-security-and-privacy).
  - Validation method: Manual content review once implemented.

## 24. Cross-Component Composition and Profile Compatibility

Composing KBDL-008 surfaces with each other and with KBDL-007 triggers
must not weaken any component's own contract: a Dialog opened from a
Menu item retains the Menu's closing/return-focus behavior for the
Menu and the Dialog's own focus-containment behavior for itself; a
Toast triggered by a form submission does not substitute for the
field-level error relationship KBDL-007 already owns
(`components-core.md §23`); a Tooltip must not be nested inside another
Tooltip; a Popover containing a Menu follows the Menu's own interaction
model for its contents while the Popover's own dismissal model governs
the outer surface. These composition rules extend, without altering,
the already-Approved KBDL-007 composition rule (`KBDL-CMP-050`).

Showcase, Precision, and Flow share one semantic and accessibility
architecture for every component in this document, consistent with the
already-Approved `KBDL-CMP-051`. Showcase may use more expressive
surfaces and media (e.g., larger Card media relationships); Precision
may emphasize dense information and complex data interaction (e.g.,
Interactive Grid, Data Visualization); Flow may emphasize task
completion, recovery, and consumer-legible feedback (e.g., simpler
Toast and Empty State treatments). No profile changes semantics, removes
accessibility behavior, or defines a final profile-specific variant;
detailed profile mappings are now specified in
[profiles.md](profiles.md).

- **`KBDL-CMP-066`** — Showcase, Precision, and Flow **must** share one
  semantic and accessibility architecture for every component this
  document defines; a profile **must not** change component semantics,
  remove accessibility behavior, or define a final profile-specific
  variant.
  - Lifecycle status: Approved (restates the already-Approved KBDL-007
    profile-consistency requirement, `KBDL-CMP-051`, applied to this
    module). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-051` (KBDL-007).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24](#24-cross-component-composition-and-profile-compatibility).
  - Validation method: Manual cross-profile consistency review once
    implemented.

## 25. Component Coverage Matrix

| Component | Family | Preferred structure/role | KBDL-007 trigger owner | KBDL-008 surface owner | Focus model | Dismissal model | Applicable CMP | Lifecycle | Provenance | Decision-packet item |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Container Surface | Surface | Neutral / optional `region` | N/A | This document | N/A | N/A | `KBDL-CMP-054` | Approved | Confirmed | None |
| Panel | Surface | Neutral / optional `region` | N/A | This document | N/A | N/A | `KBDL-CMP-054` | Approved | Confirmed | None |
| Card | Surface | Neutral or link/button | Icon/link trigger (KBDL-007) | This document | Standard tab order | N/A | `KBDL-CMP-055`, `067` | Mixed | Confirmed/Assumed | Item 1 (`067`) |
| Accordion Surface | Surface | Disclosure pattern | Disclosure trigger (KBDL-007) | This document | Trigger retains focus | N/A | `KBDL-CMP-068`, `069` | Mixed | Confirmed/Assumed | Item 2 (`069`) |
| Static Data Table | Surface | Native `table` | N/A | This document | N/A | N/A | `KBDL-CMP-070` | Approved | Confirmed | None |
| Tooltip | Overlay | `tooltip` role | Any trigger (KBDL-007) | This document | Focus remains on trigger | Escape / hover-focus-loss | `KBDL-CMP-072`, `073` | Mixed | Confirmed/Assumed | Item 3 (`073`) |
| Popover | Overlay | Non-modal dialog pattern | Button trigger (KBDL-007) | This document | Non-modal, Tab flows through | Outside-pointer / Escape | `KBDL-CMP-074` | Recommended | Assumed | Item 4 |
| Menu Surface | Overlay | `menu`/`menuitem` | Menu button (KBDL-007) | This document | Roving focus in menu | Escape / activation / outside | `KBDL-CMP-075`, `076` | Mixed | Confirmed/Assumed | Item 5 (`076`) |
| Listbox Popup | Overlay | `listbox`/`option` | Combobox input (KBDL-007) | This document | Active-descendant | Escape / selection / outside | `KBDL-CMP-077` | Approved | Confirmed | None |
| Dialog | Overlay | `dialog` | Opening action (KBDL-007) | This document | Contained if modal | Close / Escape | `KBDL-CMP-078` | Approved | Confirmed | None |
| Modal Dialog | Overlay | `dialog` (modal) | Opening action (KBDL-007) | This document | Fully contained | Close / Escape | `KBDL-CMP-079`, `080` | Mixed | Confirmed/Assumed | Item 6 (`080`) |
| Alert Dialog | Overlay | `alertdialog` | Opening action (KBDL-007) | This document | Fully contained | Explicit response only | `KBDL-CMP-081` | Approved | Confirmed | None |
| Drawer / Sheet | Overlay | `dialog` (modal or non-modal) | Nav/action trigger (KBDL-007) | This document | Per modality | Close / Escape / outside | `KBDL-CMP-082`, `083` | Mixed | Confirmed/Assumed | Item 7 (`083`) |
| Inline Feedback | Feedback | None / `aria-describedby` | Field (KBDL-007) | This document | N/A | Persistent until resolved | `KBDL-CMP-087` | Approved | Confirmed | None |
| Alert | Feedback | `alert` | N/A | This document | No focus move | Persistent/dismissible | `KBDL-CMP-088` | Approved | Confirmed | None |
| Banner | Feedback | `region` (labeled) | N/A | This document | N/A | Dismissible/persistent | `KBDL-CMP-089` | Recommended | Assumed | Item 9 |
| Toast / Snackbar | Feedback | `status`/`alert` (by urgency) | N/A | This document | No focus move | Timed or persistent | `KBDL-CMP-090`, `091` | Mixed | Confirmed/Assumed | Item 10 (`091`) |
| Status Region / Log | Feedback | `status`/`log` | N/A | This document | N/A | N/A | `KBDL-CMP-092` | Approved | Confirmed | None |
| Badge | Feedback | None / accessible text | N/A | This document | N/A | N/A | `KBDL-CMP-093` | Approved | Confirmed | None |
| Progress Indicator | Feedback | `progressbar` / native | Submit action (KBDL-007) | This document | N/A | N/A | `KBDL-CMP-094`, `098` | Approved | Confirmed | None |
| Meter | Feedback | `meter` / native | N/A | This document | N/A | N/A | `KBDL-CMP-095` | Approved | Confirmed | None |
| Skeleton | Feedback | Decorative (hidden) | N/A | This document | N/A | N/A | `KBDL-CMP-096` | Approved | Confirmed | None |
| Loading State | System-state | N/A | Submit action (KBDL-007) | This document | N/A | N/A | `KBDL-CMP-098` | Approved | Confirmed | None |
| Empty State | System-state | N/A | N/A | This document | N/A | N/A | `KBDL-CMP-099` | Recommended | Assumed | Item 11 |
| No-Results State | System-state | N/A | Search field (KBDL-007, unapproved context) | This document | N/A | N/A | `KBDL-CMP-100` | Approved | Confirmed | None |
| Error State | System-state | `alert` (if surfaced live) | N/A | This document | N/A | Retry / alternative action | `KBDL-CMP-101`, `102` | Mixed | Confirmed/Assumed | Item 12 (`102`) |
| Offline / Reconnecting | System-state | `status` | N/A | This document | N/A | N/A | `KBDL-CMP-103` | Approved | Confirmed | None |
| Permission Denied | System-state | N/A | N/A | This document | N/A | Navigation recovery | `KBDL-CMP-104` | Approved | Confirmed | None |
| Not Found | System-state | N/A | N/A | This document | N/A | Navigation recovery | `KBDL-CMP-104` | Approved | Confirmed | None |
| Maintenance / Degraded | System-state | `status` | N/A | This document | N/A | N/A | `KBDL-CMP-102` | Recommended | Assumed | Item 12 |
| System Status | System-state | `status`/`log` | N/A | This document | N/A | N/A | `KBDL-CMP-092` | Approved | Confirmed | None |
| Interactive Grid | Complex-presentation | `grid`/`gridcell` (justified) | N/A | This document | Roving tabindex | N/A | `KBDL-CMP-105` | Recommended | Assumed | Item 13 |
| Tree / Treegrid | Complex-presentation | `tree`/`treegrid` (justified) | N/A | This document | Roving tabindex | N/A | `KBDL-CMP-106` | Recommended | Assumed | Item 14 |
| Carousel | Complex-presentation | Grouped region + controls | N/A | This document | Standard + pause control | Pause/stop/hide | `KBDL-CMP-107`, `108` | Mixed | Confirmed/Assumed | Item 15 (`108`) |
| Data Visualization | Complex-presentation | Labeled graphic + data alt. | N/A | This document | Keyboard-accessible points | N/A | `KBDL-CMP-109`, `110` | Mixed | Confirmed/Assumed | Item 16 (`110`) |

## 26. Conforming and Non-Conforming Examples

Documentation examples only; none has been implementation-tested.

1. **Conforming — Modal Dialog, keyboard, light theme.** A confirmation
   modal opens from a destructive button, moves focus to its heading,
   traps Tab within the dialog, closes on Escape, and returns focus to
   the triggering button. *Requirements:* `KBDL-CMP-071`, `079`, `084`.
   *Conforms because:* background is inert, focus is contained, and
   focus returns to a still-present trigger. *Validation method:*
   Manual keyboard walkthrough once implemented. *Unapproved
   dependency:* None.
2. **Non-conforming — Modal Dialog, screen reader.** A "modal" panel
   dims the background visually but leaves it reachable via a screen
   reader's virtual cursor. *Fails:* `KBDL-CMP-071` (background not
   inert). *Correction:* Apply `inert` (or an equivalent technique) to
   background content, not only a visual scrim.
3. **Conforming — Tooltip, touch and keyboard.** An icon button has its
   own accessible name independent of its tooltip; the tooltip appears
   on focus and dismisses on Escape without moving focus.
   *Requirements:* `KBDL-CMP-072`. *Conforms because:* the accessible
   name does not depend on the tooltip. *Unapproved dependency:*
   `KBDL-CMP-073` (exact trigger/persistence timing) remains
   Recommended.
4. **Non-conforming — Tooltip as sole naming source.** An icon-only
   button relies on a tooltip's text as its only accessible name.
   *Fails:* `KBDL-CMP-072`, KBDL-007's `KBDL-CMP-003`/`017`.
   *Correction:* Give the button its own accessible name; the tooltip
   may supplement, never replace it.
5. **Conforming — Toast, reduced motion.** A non-critical save
   confirmation appears as a `status`-role toast, does not move focus,
   and a persistent activity log also records the same event.
   *Requirements:* `KBDL-CMP-086`, `090`. *Conforms because:* critical
   information (the save confirmation) also exists in a persistent
   path. *Unapproved dependency:* `KBDL-CMP-091` (exact auto-dismiss
   timing) remains Recommended.
6. **Non-conforming — Toast for critical-only information.** A payment-
   failure message appears only in an auto-dismissing toast with no
   other record. *Fails:* `KBDL-CMP-090`. *Correction:* Surface the
   failure in a persistent Alert or Error State in addition to any
   toast.
7. **Conforming — Static Data Table, enlarged text.** A pricing table
   uses native `<table>` with a caption and header scope, remaining
   readable at 200% text size via horizontal scroll within its own
   container. *Requirements:* `KBDL-CMP-070`. *Unapproved dependency:*
   `KBDL-CMP-111` (exact responsive transformation) remains
   Recommended.
8. **Non-conforming — Grid role for static content.** A read-only
   summary table is given `role="grid"` purely to enable custom arrow-
   key styling. *Fails:* `KBDL-CMP-070`, `105`. *Correction:* Use native
   `<table>` semantics; reserve `grid` for genuinely interactive,
   cell-level operations.
9. **Conforming — Carousel, Showcase profile, no motion.** An editorial
   carousel does not auto-rotate by default in this draft and exposes
   explicit previous/next controls with an accessible slide count.
   *Requirements:* `KBDL-CMP-107` (satisfied vacuously — no auto-
   rotation is present). *Unapproved dependency:* `KBDL-CMP-108`
   (auto-rotation default policy) remains Recommended.
10. **Non-conforming — Carousel, no pause control.** A homepage
    carousel rotates automatically every few seconds with no pause,
    stop, or hide control. *Fails:* `KBDL-CMP-107`. *Correction:* Add a
    pause/stop control or remove automatic rotation until
    `KBDL-CMP-108` is approved.

## 27. Normative Requirements

See each component section above ([§9](#9-required-surface-components)
through [§19](#19-responsive-transformation-policy)) for the full text
of every `KBDL-CMP-052` through `KBDL-CMP-111` requirement. This
section is intentionally a pointer, not a duplicate, to avoid
maintaining two divergent copies of the same normative text — consistent
with [conventions.md §3](conventions.md#3-cross-reference-conventions)'s
no-duplication intent for validation evidence; here it applies to
normative text itself, which must have one authoritative location.

**Authoritative status summary** (derived directly from the per-
requirement lifecycle field above, not a separately maintained count):

```text
New CMP requirements:  60 (KBDL-CMP-052 through KBDL-CMP-111)
Approved:              43
Recommended:           17
Unresolved:             0
Deferred:               0
Blocked:                0
```

The seventeen `Recommended` requirements are exactly: `KBDL-CMP-067`,
`069`, `073`, `074`, `076`, `080`, `083`, `085`, `089`, `091`, `099`,
`102`, `105`, `106`, `108`, `110`, `111` — see
[§34](#34-decision-packet-coverage-audit) for the exact, verified list
and its one-to-one packet mapping.

## 28. Component Coverage Matrix Cross-Check

See [§25](#25-component-coverage-matrix). Every component listed there
maps to at least one `KBDL-CMP-###` requirement in
[§27](#27-normative-requirements); no component is left without an
applicable requirement.

## 29. Accessibility Validation Matrix

| Requirement | Validation method | Status |
| --- | --- | --- |
| `KBDL-CMP-054` (surface neutrality/region use) | Manual semantic-structure review | Not verified |
| `KBDL-CMP-071` (modal background inertness) | Manual focus-containment review | Not verified |
| `KBDL-CMP-072` (tooltip naming independence) | Manual accessible-name review | Not verified |
| `KBDL-CMP-086` (live-region role selection) | Manual live-region review | Not verified |
| `KBDL-CMP-097` (system-state programmatic determinability) | Manual review | Not verified |
| `KBDL-CMP-109` (data-visualization non-color encoding) | Manual review | Not verified |
| Exact component-specific interaction/timing/taxonomy values not inherited from an already-approved KBDL requirement | Project-owner review, then manual review once implemented | Not applicable — none is approved or proposed as approved by this document |

## 30. Responsive Validation Matrix

| Requirement | Validation method | Status |
| --- | --- | --- |
| `KBDL-CMP-070` (table reflow) | Manual reflow/zoom testing | Not verified |
| `KBDL-CMP-111` (responsive transformation policy) | Project-owner review + manual testing | Not verified; pending approval |
| Component reflow at named breakpoints (all components) | Manual review across `compact`/`standard`/`expanded`/`wide` | Not verified |

## 31. Theme and Motion Validation Matrix

| Requirement | Validation method | Status |
| --- | --- | --- |
| Surface elevation mapping ([§8](#8-surface-architecture)) | Manual mapping review against the approved five-level elevation scale | Not verified |
| `KBDL-CMP-109` (Data-display role mapping) | Manual mapping review against approved semantic roles | Not verified |
| Reduced/no-motion parity for overlays, toasts, skeletons | Manual review confirming parity per `motion/accessibility-performance.md §1` | Not verified |
| Exact component-specific motion values or mappings not inherited from an already-approved KBDL requirement | Manual review; remain unapproved and outside implementation authority per [motion/README.md §10.3](motion/README.md#103-unresolved-or-not-approval-ready) | Not applicable — no such mapping is approved or proposed as approved by this document |

## 32. Security and Recovery Validation Matrix

| Requirement | Validation method | Status |
| --- | --- | --- |
| `KBDL-CMP-101` (no sensitive detail exposure) | Manual content review | Not verified |
| `KBDL-CMP-103` (no false synchronization claims) | Manual claim-accuracy review | Not verified |
| `KBDL-CMP-104` (no disabled-UI-as-authorization, no unnecessary disclosure) | Manual security review | Not verified |
| `KBDL-CMP-098` (duplicate-submission prevention) | Manual review | Not verified |

## 33. KBDL-008 Decision Packet

### 33.1 Already-Approved System-Component Architecture (context only)

Not awaiting approval — provided as context. Directly supported by
prior approved decisions: the KBDL-007 ownership boundary
(`KBDL-CMP-052`); surface architecture and elevation mapping
(`KBDL-CMP-053`); overlay architecture and focus/inertness rules
(`KBDL-CMP-056`, `071`, `079`, `084`); Container Surface/Panel
neutrality (`KBDL-CMP-054`); Card's nested-interaction/hover
prohibition (`KBDL-CMP-055`); Accordion's trigger/panel relationship
(`KBDL-CMP-068`); Static Data Table semantics (`KBDL-CMP-070`); Tooltip
naming independence (`KBDL-CMP-072`); Menu (`KBDL-CMP-075`) and Listbox
(`KBDL-CMP-077`) ARIA relationships; Dialog naming/keyboard
(`KBDL-CMP-078`); Modal integrity (`KBDL-CMP-079`); Alert Dialog role
use (`KBDL-CMP-081`); Drawer/Sheet KBDL-007 boundary preservation
(`KBDL-CMP-082`); feedback live-region selection (`KBDL-CMP-086`–`096`
Approved subset); system-state programmatic determinability
(`KBDL-CMP-097`–`104` Approved subset); Carousel pause/stop/hide
(`KBDL-CMP-107`); and Data Visualization non-color encoding
(`KBDL-CMP-109`).

### 33.2 Recommended Decisions — Ready for Approval

| # | Decision | Recommendation | Rationale | Alternatives | Trade-offs | Accessibility impact | Responsive impact | Theme impact | Motion impact | Security impact | Profile impact | Dependencies | Exact affected requirements | Approval scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Card-variant taxonomy | Adopt a defined set of card variants for media relationship and action placement (`KBDL-CMP-067`) | Gives summary/preview surfaces a consistent, predictable structure | An unbounded per-project card taxonomy (rejected — fragments consistency) | Requires per-project mapping to visual treatment once themes/foundations are implemented | Nested-interaction and hover-only prohibitions (`KBDL-CMP-055`) remain unaffected either way | None | None | None | None | Applies identically across profiles | `KBDL-CMP-055` | `KBDL-CMP-067` | Item 1 only |
| 2 | Accordion open model | Adopt a default single-open or multiple-open accordion behavior | Gives expandable-content lists a consistent default | Leaving the choice fully per-instance (rejected — inconsistent expectations) | Requires documenting any mandatory-open exception | Trigger/panel relationship (`KBDL-CMP-068`) unaffected either way | None | None | None | None | Applies identically across profiles | `KBDL-CMP-068` | `KBDL-CMP-069` | Item 2 only |
| 3 | Tooltip trigger/persistence/placement policy | Adopt KBDL-specific hover/focus timing and default placement behavior for tooltips (`KBDL-CMP-073`) | Provides a consistent tooltip feel without relying on the non-consensus APG timing guidance | Deferring entirely to implementation judgment (rejected — inconsistent behavior across projects) | Exact millisecond delay values remain a later implementation decision | Naming independence (`KBDL-CMP-072`) unaffected either way | None | None | None | None | Applies identically across profiles | `KBDL-CMP-072` | `KBDL-CMP-073` | Item 3 only |
| 4 | Popover taxonomy and dismissal model | Adopt a defined popover-versus-menu-versus-modal taxonomy and a default outside-pointer/Escape/focus-loss dismissal model (`KBDL-CMP-074`) | Prevents ad hoc, inconsistent choices between overlapping overlay types | No taxonomy, decided per instance (rejected — inconsistent dismissal expectations) | None significant | None beyond what non-modal focus rules already require | None | None | None | None | Applies identically across profiles | None | `KBDL-CMP-074` | Item 4 only |
| 5 | Menu interaction and dismissal model | Adopt a defined menu focus-movement, type-ahead, submenu, and return-focus model (`KBDL-CMP-076`) | Gives command/choice menus a consistent, predictable keyboard model | Relying on the APG menu pattern's exact behavior without KBDL adoption (rejected — the APG pattern is not automatically Approved) | None significant | ARIA role relationship (`KBDL-CMP-075`) unaffected either way | None | None | None | None | Applies identically across profiles | `KBDL-CMP-075` | `KBDL-CMP-076` | Item 5 only |
| 6 | Modal sizing and nested-modal policy | Adopt a modal sizing model and a one-modal-at-a-time (or defined exception) nesting policy (`KBDL-CMP-080`) | Prevents ambiguous or competing modal stacking | Unlimited nested modals (rejected — focus/Escape ownership becomes ambiguous) | None significant | Modal integrity (`KBDL-CMP-079`) unaffected either way | None | None | None | None | Applies identically across profiles | `KBDL-CMP-079`, `KBDL-CMP-084` | `KBDL-CMP-080` | Item 6 only |
| 7 | Drawer/Sheet taxonomy and default modality | Adopt a general drawer/sheet taxonomy and default modality for each conceptual variant (`KBDL-CMP-083`) | Gives edge-attached surfaces a consistent default behavior | Treating every drawer as identical to a modal dialog (rejected — collapses a useful distinction) | Navigation-collapse use remains separately contingent on `KBDL-CMP-041` regardless of this item's approval | KBDL-007 navigation-trigger boundary (`KBDL-CMP-082`) unaffected either way | None | None | None | None | Applies identically across profiles | `KBDL-CMP-082` | `KBDL-CMP-083` | Item 7 only |
| 8 | Overlay nesting/stacking policy | Adopt a maximum practical non-modal stacking depth and confirm the one-modal-at-a-time default (`KBDL-CMP-085`) | Keeps layering deterministic and testable | Unbounded nesting (rejected — same ambiguity risk as item 6) | None significant | Layering ownership (`KBDL-CMP-084`) unaffected either way | None | None | None | None | Applies identically across profiles | `KBDL-CMP-080`, `KBDL-CMP-084` | `KBDL-CMP-085` | Item 8 only |
| 9 | Banner severity taxonomy | Adopt a defined banner severity/variant set (`KBDL-CMP-089`) | Gives page-level messages a consistent, predictable set of meanings | An unbounded per-project banner variant set (rejected — fragments consistency) | None significant | Alert-role boundary (`KBDL-CMP-088`) unaffected either way | None | None | None | None | Applies identically across profiles | `KBDL-CMP-088` | `KBDL-CMP-089` | Item 9 only |
| 10 | Toast lifecycle model | Adopt auto-dismiss timing, queueing, duplicate suppression, and stacking/placement defaults for toasts (`KBDL-CMP-091`) | Gives transient feedback a consistent, testable lifecycle | Leaving timing fully to implementation judgment (rejected — inconsistent, risks WCAG 2.2.1 issues if timing is too short) | Exact millisecond/second values remain a later implementation decision | Critical-information boundary (`KBDL-CMP-090`) unaffected either way | None | None | None | None | Applies identically across profiles | `KBDL-CMP-090` | `KBDL-CMP-091` | Item 10 only |
| 11 | Empty-state taxonomy | Adopt an empty-state taxonomy (first-use, user-cleared, permission-limited, genuinely-empty), illustration policy, and action hierarchy (`KBDL-CMP-099`) | Gives absence-of-content states a consistent, predictable structure | A single undifferentiated "empty" treatment (rejected — conflates causes with different correct actions) | None significant | Programmatic-determinability requirement (`KBDL-CMP-097`) unaffected either way | None | None | None | None | Applies identically across profiles | `KBDL-CMP-097`, `KBDL-CMP-100` | `KBDL-CMP-099` | Item 11 only |
| 12 | Error/system-state severity taxonomy and recovery hierarchy | Adopt a severity taxonomy and recovery hierarchy distinguishing maintenance, unavailable, and degraded conditions (`KBDL-CMP-102`) | Gives system-wide disruption states a consistent, predictable escalation model | Treating all disruptions identically (rejected — obscures whether an action is possible) | None significant | Recovery/error-identification requirement (`KBDL-CMP-101`) unaffected either way | None | None | None | None | Applies identically across profiles | `KBDL-CMP-101`, `KBDL-CMP-103` | `KBDL-CMP-102` | Item 12 only |
| 13 | Grid-versus-table threshold and interactive-grid model | Adopt a threshold for when grid semantics are justified and the resulting composite-widget keyboard model (`KBDL-CMP-105`) | Prevents casual misuse of a composite keyboard model on effectively static data | Using grid semantics by default for any tabular data (rejected — unnecessary complexity and keyboard-model risk) | Exact virtualization/resizing/pinning behavior remains a later implementation decision | Static-table distinction (`KBDL-CMP-070`) unaffected either way | `KBDL-RSP-011` cited as unapproved context, not adopted as authority | None | None | None | Applies identically across profiles | `KBDL-CMP-070` | `KBDL-CMP-105` | Item 13 only |
| 14 | Tree/treegrid justification threshold | Adopt a threshold for when hierarchical, tabular, or combined interaction genuinely requires tree/treegrid semantics, and the resulting model (`KBDL-CMP-106`) | Prevents casual misuse of a composite hierarchical widget for simple nested lists | Using tree semantics for any nested list (rejected — unnecessary complexity) | None significant | Distinction from Accordion (`KBDL-CMP-068`) and Grid (`KBDL-CMP-105`) unaffected either way | None | None | None | None | Applies identically across profiles | `KBDL-CMP-068`, `KBDL-CMP-105` | `KBDL-CMP-106` | Item 14 only |
| 15 | Carousel auto-rotation default policy | Adopt a default policy on automatic rotation and, if permitted, an interval and hover/focus-pause behavior (`KBDL-CMP-108`) | Establishes whether auto-rotation is even a default before any interval is chosen | Always auto-rotating by default (rejected pending review — raises distraction/motion-safety concerns); never auto-rotating (a valid, conservative option this item may adopt) | None significant | Pause/stop/hide requirement (`KBDL-CMP-107`) applies regardless of this item's outcome | None | None | Any auto-rotation is itself a motion choice subject to the approved motion-safety baseline | None | Applies identically across profiles | `KBDL-CMP-107` | `KBDL-CMP-108` | Item 15 only |
| 16 | Data-visualization chart taxonomy and interaction model | Adopt a chart taxonomy, tooltip-interaction behavior, and keyboard-navigation model for interactive charts, independent of the still-unapproved exact palette (`KBDL-CMP-110`) | Gives data-heavy views a consistent, accessible interaction pattern without waiting on palette decisions | No defined taxonomy, chosen per project (rejected — inconsistent accessibility quality across charts) | None significant | Non-color-encoding requirement (`KBDL-CMP-109`) unaffected either way; palette itself remains unapproved and unaffected by this item | None | None | None | None | Applies identically across profiles | `KBDL-CMP-109` | `KBDL-CMP-110` | Item 16 only |
| 17 | Responsive transformation policy for overlays and tabular data | Adopt content-driven transformation patterns (dialog-to-full-screen, table-to-cards, popover-to-sheet) independent of the exact unapproved breakpoint values (`KBDL-CMP-111`) | Gives narrow-viewport adaptation a consistent, predictable pattern set | Ad hoc, per-project transformation choices (rejected — inconsistent responsive behavior) | Exact trigger breakpoint remains dependent on the eventual `KBDL-RSP-002` value | Static Data Table semantics (`KBDL-CMP-070`) unaffected either way | `KBDL-RSP-002` cited as eventual, unapproved context for the exact trigger point only, not adopted as authority | None | None | None | Applies identically across profiles | `KBDL-CMP-070`, `KBDL-CMP-080` | `KBDL-CMP-111` | Item 17 only |

### 33.3 Unresolved or Not Approval-Ready

- **Exact overlay z-index scale, placement offsets, and collision-
  detection algorithm** — implementation-layer, out of scope.
- **Exact scrim opacity** — depends on the still-unapproved theme
  opacity values (`themes/README.md`); not proposed here.
- **Exact modal, drawer, and popover dimensions** — depend on
  foundation values not yet finalized; out of scope here.
- **Exact toast auto-dismiss duration, queue limit, and carousel
  rotation interval** — numeric values remain a later implementation
  decision once the corresponding policy items (10, 15) are approved.
- **Exact skeleton shimmer/pulse timing** — component-specific motion
  value, remains `Recommended`/`Unresolved` per the existing motion-
  pattern-matrix pattern (`motion/patterns.md §12`); not re-proposed
  here.
- **Data-visualization color palette** — explicitly out of scope;
  remains unapproved regardless of whether item 16 is approved.
- **Forced-colors/high-contrast rendering of any KBDL-008 surface** —
  depends on the still-unapproved `KBDL-A11Y-011`; cited as unapproved
  context only.
- **Actual screen-reader/browser test matrix for KBDL-008 components**
  — depends on the still-unapproved `KBDL-A11Y-035`.
- **Implementation-layer token formats, CSS architecture, JavaScript
  behavior, package structure, portal/top-layer technology, charting
  library, virtualization implementation** — explicitly out of scope
  for a design-language specification.
- **Browser-support matrix** — not proposed.
- **Profile-specific component variants** — now specified in
  [profiles.md](profiles.md), where profile-specific defaults remain
  `Recommended` pending project-owner review.

## 34. Decision-Packet Coverage Audit

```text
New CMP requirements:                     60
Approved:                                 43
Recommended:                              17
Unresolved:                                 0
Deferred:                                   0
Blocked:                                    0

Independently approval-ready recommendations: 17
Contingent recommendations:                    0
Unresolved items:                              0
Deferred items:                                0
Blocked items:                                  0
```

Every `Recommended` `KBDL-CMP-###` requirement introduced by this
document maps to exactly one approval-ready packet item, and every
packet item maps to exactly one `Recommended` requirement:

| Recommended requirement | Packet item | Independently approval-ready | Dependency |
| --- | --- | --- | --- |
| `KBDL-CMP-067` | 1 | Yes | None |
| `KBDL-CMP-069` | 2 | Yes | None |
| `KBDL-CMP-073` | 3 | Yes | None |
| `KBDL-CMP-074` | 4 | Yes | None |
| `KBDL-CMP-076` | 5 | Yes | None |
| `KBDL-CMP-080` | 6 | Yes | None |
| `KBDL-CMP-083` | 7 | Yes | None (navigation-drawer use remains separately bound by `KBDL-CMP-041`, KBDL-007, not by this item) |
| `KBDL-CMP-085` | 8 | Yes | None |
| `KBDL-CMP-089` | 9 | Yes | None |
| `KBDL-CMP-091` | 10 | Yes | None |
| `KBDL-CMP-099` | 11 | Yes | None |
| `KBDL-CMP-102` | 12 | Yes | None |
| `KBDL-CMP-105` | 13 | Yes | None (`KBDL-RSP-011` cited as unapproved context only) |
| `KBDL-CMP-106` | 14 | Yes | None |
| `KBDL-CMP-108` | 15 | Yes | None |
| `KBDL-CMP-110` | 16 | Yes | None (data-viz palette remains separately unapproved, not required for this item) |
| `KBDL-CMP-111` | 17 | Yes (the pattern-adoption itself); exact trigger breakpoint depends on eventual `KBDL-RSP-002` | `KBDL-RSP-002` (eventual, unapproved) |

Exactly seventeen `Recommended` requirements (`067`, `069`, `073`,
`074`, `076`, `080`, `083`, `085`, `089`, `091`, `099`, `102`, `105`,
`106`, `108`, `110`, `111`) map one-to-one to the seventeen approval-
ready packet items tabulated above. `KBDL-CMP-102` serves both the
Error State ([§16.4](#164-error-state)) and Maintenance/Degraded
([§16.8](#168-maintenance-unavailable-and-degraded-state)) sections
under its single packet item (12), since both describe one severity/
recovery taxonomy rather than two independent decisions — this is one
requirement mapped once, not a duplicate mapping. No `Recommended`
requirement is orphaned, no approval-ready packet item is orphaned, no
`Approved` `KBDL-CMP-###` requirement is presented as awaiting
approval, no contingent dependency is hidden, and no KBDL-006
or KBDL-007 recommendation is represented as approved anywhere in this
document.

**Exact scope of a future approval:** an `APPROVE` response to
[§33.2](#332-recommended-decisions--ready-for-approval) would authorize
exactly items 1–17 above. It would **not** approve any
[§33.3](#333-unresolved-or-not-approval-ready) item, any of the nine
KBDL-006 recommendations, any of the ten KBDL-007 recommendations
(including `KBDL-CMP-041`), any data-visualization palette, any forced-
colors policy, any KBDL-009-or-later content, or any implementation
validation. It would not itself constitute validation of any item —
see [§29](#29-accessibility-validation-matrix)–[§32](#32-security-and-recovery-validation-matrix).

## 35. KBDL-006 Approval-Boundary Audit

| KBDL-006 requirement | Where referenced in this document | How handled |
| --- | --- | --- |
| `KBDL-RSP-002` (exact breakpoint thresholds) | [§19](#19-responsive-transformation-policy), decision packet item 17 | Cited only as unapproved, eventual context for the exact transformation trigger point; the transformation pattern itself remains independently approval-ready |
| `KBDL-RSP-003` (grid columns) | Not referenced | Not used |
| `KBDL-RSP-004` (container widths) | Not referenced | Not used |
| `KBDL-RSP-005` (gutters) | Not referenced | Not used |
| `KBDL-RSP-008` (navigation collapse thresholds) | [§11.8](#118-drawer-and-sheet) (navigation-drawer boundary note) | Cited only as unapproved context via the existing `KBDL-CMP-041` contingency; not adopted as authority |
| `KBDL-RSP-011` (data-dense strategy) | [§9.5](#95-static-data-table), [§18.1](#181-interactive-grid), decision packet item 13 | Referenced as unapproved context only; not adopted as authority for the grid-versus-table threshold |
| `KBDL-A11Y-011` (forced-colors policy) | [§33.3](#333-unresolved-or-not-approval-ready) | Cited only as unapproved context; explicitly excluded from any approval |
| `KBDL-A11Y-021` (44×44 preferred target) | Not referenced (KBDL-008 introduces no new target-size guidance beyond the existing KBDL-007 boundary) | Not used |
| `KBDL-A11Y-035` (preferred testing matrix) | [§33.3](#333-unresolved-or-not-approval-ready) | Cited only as a dependency for future validation, not used normatively |

None of the nine is treated as implementation authority anywhere in
this document.

## 36. KBDL-007 Approval-Boundary Audit

| KBDL-007 requirement | Where referenced in this document | How handled |
| --- | --- | --- |
| `KBDL-CMP-015` (button hierarchy taxonomy) | [§11.7](#117-alert-dialog) (alert-dialog action area note) | Cited explicitly as unapproved; not adopted as authority for the alert dialog's action area |
| `KBDL-CMP-017` (icon-only visible-label threshold) | [§11.1](#111-tooltip) (`KBDL-CMP-072` related-requirement note) | Referenced as unapproved context only; `KBDL-CMP-072`'s tooltip naming-independence rule does not depend on this threshold and does not approve it |
| `KBDL-CMP-020` (button-group composition) | Not referenced | Not used |
| `KBDL-CMP-025` (search-field model) | [§16.3](#163-no-results-state) | Cited explicitly as unapproved context; not adopted as authority for No-Results State |
| `KBDL-CMP-029` (combobox-justification threshold) | [§11.4](#114-listbox-popup) | Cited explicitly as unapproved; `KBDL-CMP-077` states the listbox popup does not approve it |
| `KBDL-CMP-036` (form-action-row reflow order) | [§11.7](#117-alert-dialog) (alert-dialog action area note) | Cited explicitly as unapproved; not adopted as authority |
| `KBDL-CMP-041` (navigation collapse threshold, itself contingent) | [§11.8](#118-drawer-and-sheet), decision packet item 7 | Referenced as a contingent dependency for navigation-drawer use only; `KBDL-CMP-083`'s general taxonomy remains independently approval-ready regardless |
| `KBDL-CMP-044` (breadcrumb truncation model) | Not referenced | Not used |
| `KBDL-CMP-046` (tabs activation model) | Not referenced (Tabs remain KBDL-007 scope; this document does not add an "overlay tabs" variant) | Not used |
| `KBDL-CMP-048` (pagination truncation model) | Not referenced | Not used |

None of the ten is treated as implementation authority anywhere in
this document.

## 37. Trigger/Surface Ownership Audit

See [§5](#5-kbdl-007-ownership-boundary) for the full ownership matrix.
Confirmed unchanged by this document: every KBDL-007 trigger, field,
action, and navigation contract (`KBDL-CMP-001`–`051`) — no lifecycle
status, provenance, validation status, or normative text in
`components-core.md` is modified by this document (see
[§38](#38-cross-module-updates) for the only permitted boundary-link
additions).

## 38. Cross-Module Updates

### README.md

Updated to state KBDL-007 passed planning-agent validation, KBDL-008
deliverables are present, the `docs/kbdl/components-system.md` path now
resolves, and KBDL-009 remains locked pending KBDL-008's own validation
review (see the diff in this remediation's evidence).

### traceability-matrix.md

New KBDL-008 traceability groups added for every `KBDL-CMP-052` through
`KBDL-CMP-111` requirement (see
[§41](#41-traceability)).

### glossary.md

New terms added: Surface, Container Surface, Panel, Card, Accordion,
Overlay, Modal, Non-modal, Tooltip, Popover, Menu, Listbox, Dialog,
Alert Dialog, Drawer, Sheet, Alert, Banner, Toast, Snackbar, Status,
Log, Badge, Progress Indicator, Meter, Skeleton, Empty State,
No-Results State, Error State, Offline State, System Status, Data
Table, Grid, Tree, Treegrid, Carousel, Data Visualization, Scrim,
Inert, Live Region — omitting any term already defined
([glossary.md](glossary.md) already defines Live region; not
duplicated).

### conformance-checklist.md

Unchanged — its existing generic items (terminology, requirement IDs,
status labels, traceability, cross-references, scope, accessibility/
motion/responsive/theme/profile/component impact, decision register,
deferred/unresolved items, validation evidence, unresolved risks,
reviewer approval) already cover KBDL-008 review without modification.

### components-core.md

Updated only to link its existing "deferred to KBDL-008" references to
this new file where a plain-text mention previously had no target (see
[§39](#39-components-core-boundary-reconciliation)); no KBDL-007
lifecycle status, provenance, or packet mapping is changed.

## 39. Components-Core Boundary Reconciliation

`components-core.md §11` (`KBDL-CMP-005`) and `§36` are updated only to
add a resolving link to `components-system.md` where they previously
named KBDL-008 by text alone, since the file now exists. No existing
`KBDL-CMP-001`–`051` lifecycle status, provenance, validation status, or
decision-packet mapping is changed by this addition.

## 40. Deferred and Unresolved Items

- Exact overlay z-index scale, placement offsets, collision-detection
  algorithm — out of scope, implementation-layer.
- Exact scrim opacity, modal/drawer/popover dimensions — depend on
  unapproved theme opacity and unfinalized foundation values.
- Exact toast timing, queue limit, carousel rotation interval, skeleton
  shimmer/pulse timing — component-specific values, remain
  `Recommended`/`Unresolved` pending the corresponding policy item's
  approval and, ultimately, the motion-pattern-matrix itself.
- Data-visualization color palette — explicitly out of scope.
- Forced-colors/high-contrast rendering of KBDL-008 surfaces — depends
  on unapproved `KBDL-A11Y-011`.
- Actual screen-reader/browser test matrix — depends on unapproved
  `KBDL-A11Y-035`.
- Implementation-layer token formats, CSS/JavaScript architecture,
  package structure, portal/top-layer technology, charting library,
  virtualization implementation — out of scope.
- Browser-support matrix — not proposed.
- Profile-specific component variants — deferred to the Project
  Profiles module (`PRO`).
- Manual customization of any KBDL-008 component — governed by
  [customization.md](customization.md), without changing this module's semantics
  or promoting any KBDL-008 recommendation.
- Implementation-level accessibility, real-device, and production
  conformance validation — `Not verified`, no implementation exists.
- Use of any of the nine unapproved KBDL-006 recommendations, or the
  ten unapproved KBDL-007 recommendations, as implementation authority
  — explicitly excluded throughout this document (see
  [§35](#35-kbdl-006-approval-boundary-audit),
  [§36](#36-kbdl-007-approval-boundary-audit)).

## 41. Traceability

### Surface components and module-wide baselines (KBDL-CMP-052, 053, 054, 055, 062, 065, 067, 068, 069, 070)

- **Blueprint section:** KBDL-007 ownership boundary; extended
  system-component contract; surface architecture; Container Surface,
  Panel, Card, Accordion, Static Data Table
- **Roadmap prompt:** KBDL-008
- **Requirement ID:** KBDL-CMP-052, 053, 054, 055, 062, 065, 067, 068,
  069, 070
- **Specification location:** [components-system.md §5, §7, §8, §9](#5-kbdl-007-ownership-boundary)
- **Approval status:** `KBDL-CMP-052`, `053`, `054`, `055`, `062`, `065`,
  `068`, `070` Approved (restate KBDL-007's scope-control and
  accessible-naming rules, native-semantics-first rule, WCAG
  1.3.1/1.4.1, and the adopted ARIA disclosure/region definitions);
  `KBDL-CMP-067` (card-variant taxonomy), `069` (accordion open model)
  Recommended (new component-level taxonomy)
- **Provenance:** Confirmed for `KBDL-CMP-052`, `053`, `054`, `055`,
  `062`, `065`, `068`, `070`; Assumed for `KBDL-CMP-067`, `069`.
- **Validation status:** Not verified
- **Validation method:** Manual semantic-structure and DOM-relationship
  review once implemented; project-owner review of `KBDL-CMP-067`/`069`
  (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Implementation-dependent.
- **Related decision:** Not applicable — pending a future decision-
  register entry once the project owner reviews the KBDL-008 decision
  packet.
- **Related requirements:** `KBDL-CMP-002`, `003`, `005`, `021`
  (KBDL-007).
- **KBDL-007 boundary:** Preserves the disclosure-trigger contract
  (`KBDL-CMP-021`) and the scope-control rule (`KBDL-CMP-005`)
  unchanged.
- **KBDL-006 dependency:** `KBDL-RSP-011` cited as unapproved context
  for Static Data Table only, not adopted as authority.
- **Later-roadmap dependency:** None.
- **Notes:** `KBDL-CMP-067`, `069` map to
  [KBDL-008 decision packet](components-system.md#33-kbdl-008-decision-packet)
  items 1 and 2 respectively.

### Overlay components (KBDL-CMP-056 through KBDL-CMP-060, 071 through 085)

- **Blueprint section:** Overlay architecture; Tooltip, Popover, Menu
  surface, Listbox popup, Dialog, Modal Dialog, Alert Dialog, Drawer/
  Sheet; overlay layering and nesting
- **Roadmap prompt:** KBDL-008
- **Requirement ID:** KBDL-CMP-056, 057, 058, 059, 060, 071, 072, 073,
  074, 075, 076, 077, 078, 079, 080, 081, 082, 083, 084, 085
- **Specification location:** [components-system.md §10–§12](#10-overlay-architecture)
- **Approval status:** `KBDL-CMP-056`, `057`, `058`, `059`, `060`, `071`,
  `072`, `075`, `077`, `078`, `079`, `081`, `082`, `084` Approved
  (restate WCAG 2.1.1/2.1.2/2.2.1/2.4.3/2.4.11/1.4.13/4.1.2, the
  already-Approved motion-parity rule, adopted ARIA menu/listbox/
  dialog/alertdialog role definitions, and the KBDL-007 scope-control
  rule); `KBDL-CMP-073` (tooltip timing), `074` (popover taxonomy),
  `076` (menu interaction model), `080` (modal sizing/nesting), `083`
  (drawer/sheet taxonomy), `085` (overlay nesting policy) Recommended
  (new component-level timing, taxonomy, or nesting policy)
- **Provenance:** Confirmed for `KBDL-CMP-056`, `057`, `058`, `059`,
  `060`, `071`, `072`, `075`, `077`, `078`, `079`, `081`, `082`, `084`;
  Assumed for `KBDL-CMP-073`, `074`, `076`, `080`, `083`, `085`.
- **Validation status:** Not verified
- **Validation method:** Manual focus-containment, keyboard, and ARIA-
  relationship review once implemented; project-owner review of the
  Recommended subset (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** `KBDL-CMP-083` additionally notes that
  navigation-drawer use remains bound by the unapproved `KBDL-CMP-041`
  (KBDL-007) regardless of this item's own approval.
- **Related decision:** Not applicable — pending a future decision-
  register entry once the project owner reviews the KBDL-008 decision
  packet.
- **Related requirements:** `KBDL-CMP-003`, `006`, `007`, `021`, `028`,
  `029`, `041` (KBDL-007).
- **KBDL-007 boundary:** Preserves the menu-button, combobox, and
  navigation-trigger contracts unchanged; does not approve
  `KBDL-CMP-029` or `KBDL-CMP-041`.
- **KBDL-006 dependency:** `KBDL-RSP-008` cited as unapproved context
  for the navigation-drawer boundary note only.
- **Later-roadmap dependency:** None.
- **Notes:** `KBDL-CMP-073`, `074`, `076`, `080`, `083`, `085` map to
  [KBDL-008 decision packet](components-system.md#33-kbdl-008-decision-packet)
  items 3, 4, 5, 6, 7, and 8 respectively.

### Feedback components (KBDL-CMP-086 through KBDL-CMP-098)

- **Blueprint section:** Feedback architecture; Inline Feedback, Alert,
  Banner, Toast/Snackbar, Status Region/Log, Badge, Progress Indicator,
  Meter, Skeleton
- **Roadmap prompt:** KBDL-008
- **Requirement ID:** KBDL-CMP-061, 086, 087, 088, 089, 090, 091, 092,
  093, 094, 095, 096, 098
- **Specification location:** [components-system.md §13–§14](#13-feedback-architecture)
- **Approval status:** `KBDL-CMP-061`, `086`, `087`, `088`, `090`, `092`,
  `093`, `094`, `095`, `096`, `098` Approved (restate the locked
  component-state-clarity rule, `KBDL-A11Y-031`, adopted WAI-ARIA
  live-region/alert/progressbar/meter role definitions, WCAG
  1.1.1/1.4.1/2.2.1, and the existing KBDL-007 submit-loading contract);
  `KBDL-CMP-089` (banner taxonomy), `091` (toast lifecycle model)
  Recommended (new component-level taxonomy/timing)
- **Provenance:** Confirmed for `KBDL-CMP-061`, `086`, `087`, `088`,
  `090`, `092`, `093`, `094`, `095`, `096`, `098`; Assumed for
  `KBDL-CMP-089`, `091`.
- **Validation status:** Not verified
- **Validation method:** Manual live-region, role, and content-
  classification review once implemented; project-owner review of
  `KBDL-CMP-089`/`091` (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** Implementation-dependent.
- **Related decision:** Not applicable — pending a future decision-
  register entry once the project owner reviews the KBDL-008 decision
  packet.
- **Related requirements:** `KBDL-A11Y-031`, KBDL-007 submit-loading
  contract (`components-core.md §23`).
- **KBDL-007 boundary:** Not applicable — feedback components have no
  KBDL-007 trigger counterpart beyond the submit action already owned
  by KBDL-007.
- **KBDL-006 dependency:** None.
- **Later-roadmap dependency:** None.
- **Notes:** `KBDL-CMP-089`, `091` map to
  [KBDL-008 decision packet](components-system.md#33-kbdl-008-decision-packet)
  items 9 and 10 respectively.

### System-state, complex-presentation, and profile/security baselines (KBDL-CMP-063, 064, 066, 097, 099–111)

- **Blueprint section:** System-state architecture; Loading, Empty,
  No-Results, Error, Offline/Reconnecting, Permission Denied, Not
  Found, Maintenance/Degraded, System Status; complex-presentation
  architecture; Interactive Grid, Tree/Treegrid, Carousel, Data
  Visualization; responsive transformation policy; security/privacy
  and profile-compatibility baselines
- **Roadmap prompt:** KBDL-008
- **Requirement ID:** KBDL-CMP-063, 064, 066, 097, 099, 100, 101, 102,
  103, 104, 105, 106, 107, 108, 109, 110, 111
- **Specification location:** [components-system.md §15–§19, §23, §24](#15-system-state-architecture)
- **Approval status:** `KBDL-CMP-063`, `064`, `066`, `097`, `100`, `101`,
  `103`, `104`, `107`, `109` Approved (restate `KBDL-A11Y-031`, the
  locked component-state-clarity rule, WCAG 3.3.1/3.3.7/2.2.2/1.4.1/
  1.3.1/2.1.1, the existing KBDL correctness/safety and security
  principles, the existing Data-display theme roles, and the
  already-Approved `KBDL-CMP-051` profile-consistency rule);
  `KBDL-CMP-099` (empty-state taxonomy), `102` (error/system-state
  severity taxonomy), `105` (grid-versus-table threshold), `106`
  (treegrid justification threshold), `108` (carousel auto-rotation
  policy), `110` (data-visualization interaction model), `111`
  (responsive transformation policy) Recommended (new component-level
  taxonomy, threshold, or policy)
- **Provenance:** Confirmed for `KBDL-CMP-063`, `064`, `066`, `097`,
  `100`, `101`, `103`, `104`, `107`, `109`; Assumed for `KBDL-CMP-099`,
  `102`, `105`, `106`, `108`, `110`, `111`.
- **Validation status:** Not verified
- **Validation method:** Manual review once implemented; project-owner
  review of the Recommended subset (not yet performed).
- **Validation evidence:** Not verified — no implementation exists yet.
- **Known limitation:** `KBDL-CMP-105` additionally cites the
  unapproved `KBDL-RSP-011` as related context; `KBDL-CMP-111`
  additionally depends on the eventual `KBDL-RSP-002` value for its
  exact trigger point.
- **Related decision:** Not applicable — pending a future decision-
  register entry once the project owner reviews the KBDL-008 decision
  packet.
- **Related requirements:** `KBDL-A11Y-031`, `KBDL-CMP-025` (KBDL-007,
  unapproved context only), `KBDL-RSP-002`, `KBDL-RSP-011` (KBDL-006,
  unapproved context only).
- **KBDL-007 boundary:** Does not approve `KBDL-CMP-025`.
- **KBDL-006 dependency:** `KBDL-RSP-002`, `KBDL-RSP-011` cited as
  unapproved context only, not adopted as authority.
- **Later-roadmap dependency:** None.
- **Notes:** `KBDL-CMP-099`, `102`, `105`, `106`, `108`, `110`, `111`
  map to
  [KBDL-008 decision packet](components-system.md#33-kbdl-008-decision-packet)
  items 11, 12, 13, 14, 15, 16, and 17 respectively.
