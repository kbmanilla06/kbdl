# KBDL Responsive Behavior

> **KBDL Design Language v1 — active guidance.** Per-requirement
> lifecycle and approval labels below are historical provenance annotations
> from the retired specification programme; they are not pending decisions and
> they do not gate v1. Concrete values are consolidated in
> [tokens](tokens/README.md). Values a project may legitimately vary are
> labelled *Project-controlled*, not unresolved. See [STATUS](STATUS.md).

Lifecycle status: mixed. `Approved` for the requirements below that
directly restate an already-`Approved` KBDL principle, foundation rule,
or WCAG 2.2 Level A/AA success criterion — see
[§33](#33-normative-requirements) for exact per-requirement status.
`Recommended`/`Unresolved` for genuinely new KBDL-006 defaults (exact
breakpoint thresholds, grid columns, gutters, container widths) —
pending project-owner approval via [§35](#35-responsive-decision-packet).
No `Recommended` or `Unresolved` value in this document authorizes
implementation on its own — see
[conventions.md §1.1](conventions.md#11-lifecycle--approval-status).

Return to the [specification index](README.md).

## 1. Purpose and Scope

This document defines KBDL's framework-neutral responsive-behavior
specification: how layouts, navigation, content density, media, and
interaction adapt across viewport sizes, orientations, zoom levels, and
input methods, while preserving one system's hierarchy and meaning. It
resolves items KBDL-003 (visual foundations) and KBDL-005 (motion)
explicitly deferred to this module — exact breakpoint pixel values, grid
column counts, gutter values, and detailed responsive/motion interaction
rules — and adds new `KBDL-RSP-###` requirements. It does not define
component anatomy, application code, CSS, JavaScript, or any framework
choice; those remain later roadmap steps (see
[README.md § Document Hierarchy](README.md#document-hierarchy)).

## 2. Relationship to KBDL Principles

This module operationalizes, at responsive-behavior granularity:
Adaptability Without Fragmentation and Consistent System Behavior
(`KBDL-PRN-003`, `KBDL-PRN-007` — see
[principles.md §6.7, §9.4](principles.md#67-adaptability-without-fragmentation));
the locked **responsive content priority** rule
([principles.md §5.1](principles.md#51-locked-identity-rules)): "the
same content must retain the same relative priority across
breakpoints; smaller viewports reorganize, they do not silently drop
what matters"; and the content-driven breakpoint philosophy already
established in
[foundations/spacing-layout.md §3.1](foundations/spacing-layout.md#31-required-principle-approved)
(a breakpoint is introduced only where content, navigation, or
interaction genuinely needs to reorganize — never to match a device
name).

## 3. Responsive Terminology

- **Breakpoint** — a named viewport-width threshold at which layout,
  navigation, or interaction structure changes to serve content or
  interaction needs, not a specific device.
- **Reflow** — the process by which content rearranges to fit the
  available viewport without requiring two-dimensional scrolling for
  reading, per [WCAG 2.2 SC 1.4.10](https://www.w3.org/TR/WCAG22/#reflow).
- **Content priority** — the relative importance of a piece of content
  or a control, which must remain the same across breakpoints even as
  its position or visual treatment changes.
- **Source order** — the order elements appear in the underlying
  document structure, which determines default reading and
  keyboard-navigation order independent of visual position.
- **Reading order** — the order content is intended to be consumed in,
  which must match source order unless an explicit, accessible
  mechanism establishes a different but equally understandable order.
- **Container width** — the maximum width a content region is allowed
  to occupy at a given breakpoint.
- **Reading measure** — the number of characters per line recommended
  for comfortable reading, independent of container width.
- **Gutter** — the fixed space between columns in a grid.
- **Safe area** — the region of a viewport guaranteed not to be
  obscured by a device's physical cutouts, rounded corners, or
  system UI overlays.
- **Virtual keyboard** — an on-screen keyboard that temporarily reduces
  the visible viewport height on touch devices.
- **Hybrid input** — a device or session capable of touch, pointer, and
  keyboard input interchangeably (e.g., a touchscreen laptop).
- **Coarse pointer** — a pointer input (typically touch) with lower
  precision than a mouse, per media-query terminology; used here only
  as a concept, not a CSS feature name.

These terms are distinct: a **breakpoint** triggers a layout change; a
**reflow** is what happens to content within that change; **content
priority** is what must be preserved regardless of either.

## 4. Responsive-Content Priority

Status: `Approved` (`KBDL-RSP-001`, directly restates the locked
responsive-content-priority rule, [principles.md §5.1](principles.md#51-locked-identity-rules)).

**Requirements:**

- The same content and controls **must** remain available at every
  breakpoint; reorganization is permitted, removal of meaning is not.
- The single most important element or action on a screen (per
  [principles.md §6.4](principles.md#64-visual-hierarchy)) **must**
  remain the most prominent at every breakpoint, even if its visual
  treatment changes.
- Secondary content **may** collapse behind progressive disclosure
  (an expandable section, a "more" affordance) but **must** remain
  reachable, never silently dropped.
- Re-ranking content order between breakpoints **must** preserve task
  comprehension — a re-ranked element must still make sense in its new
  position relative to its neighbors.

## 5. Content-Driven Breakpoint Model

Status: `Approved` for the philosophy (directly restates
[foundations/spacing-layout.md §3.1](foundations/spacing-layout.md#31-required-principle-approved)).

A breakpoint is introduced only where: the content's layout genuinely
needs to reorganize (e.g., a multi-column layout no longer fits); the
navigation model needs to change structure (e.g., a persistent sidebar
becomes a menu); or the interaction model changes (e.g., hover-dependent
affordances become unavailable on touch). Breakpoints are **never**
introduced or named to match a specific device or screen size.

## 6. Named Breakpoint Roles

Status: `Approved` (the four named roles and their purposes were
approved via the foundation decision packet,
[KBDL-DEC-012](decision-register.md#kbdl-dec-012--foundation-decision-packet-approved)).

| Name | Role |
| --- | --- |
| `compact` | Single-column, touch-first layouts |
| `standard` | Introduces secondary columns / expanded navigation |
| `expanded` | Introduces dashboard-density multi-column layouts |
| `wide` | Introduces maximum content width and full editorial composition |

Exact pixel thresholds for these four roles were explicitly deferred to
this module and are proposed in [§7](#7-proposed-exact-breakpoint-thresholds).

## 7. Proposed Exact Breakpoint Thresholds

Status: `Recommended` (`KBDL-RSP-002`), `Assumed` provenance,
`Not verified` — pending project-owner approval via
[§35](#35-responsive-decision-packet).

| Named role | Recommended minimum width | Purpose | Trigger | Why not device-based |
| --- | --- | --- | --- | --- |
| `compact` | 0px (baseline) | Single-column, touch-first | Below the width where a second content column remains comfortably readable | No device name is stable across manufacturers or years; width alone reflects available reading space |
| `standard` | 600px | Secondary columns / expanded navigation become viable | A second column reaches a comfortable minimum reading measure alongside a primary column | Matches the point where two reading columns fit, not any specific phone/tablet boundary |
| `expanded` | 905px | Dashboard-density multi-column layouts | Enough width for three content regions or a persistent side navigation plus two content columns | Reflects layout capacity, not a "tablet vs. laptop" assumption |
| `wide` | 1240px | Maximum content width, full editorial composition | Content would otherwise stretch reading measure beyond comfortable line length without a max-width constraint | Reflects when a max-width constraint becomes necessary, not a specific monitor class |

**Alternatives considered:** device-class-based breakpoints (rejected —
violates the already-approved content-driven philosophy and becomes
stale as device sizes change); a five-tier system (rejected — the
four approved named roles already cover the content-reorganization
points identified; a fifth tier was not justified by a genuine content
need). **Trade-offs:** exact values may need revision once real content
is authored against them; revision requires a new decision, not silent
adjustment. **Accessibility impact:** thresholds must remain compatible
with 320px reflow ([§21](#21-zoom-and-enlarged-text)) regardless of
final value. **Performance impact:** none — these are layout thresholds,
not runtime costs. **Profile impact:** Showcase may introduce additional
compositional breakpoints within a profile's own pages, but the four
named roles remain shared. **Dependencies:** `KBDL-FND-011` (named
breakpoint set, approved architecture).

## 8. Grid and Column Behavior

Status: `Recommended` (`KBDL-RSP-003`), pending approval.

| Named role | Recommended columns | Purpose |
| --- | --- | --- |
| `compact` | 4 | Single-column content with minor internal alignment |
| `standard` | 8 | Two content regions or one content region plus a secondary panel |
| `expanded` | 12 | Multi-column dashboards, three-region layouts |
| `wide` | 12 (wider gutters/margins) | Editorial composition, larger compositional gestures |

**Requirements (Approved, restates locked hierarchy/proportion
principles):** column count **must not** be treated as a rigid grid
that forces content into artificial divisions — it is a proportion
reference, not a mandate that every element span whole columns.

## 9. Container Widths and Reading Measures

Status: `Recommended` (`KBDL-RSP-004`), pending approval.

| Named role | Recommended max container width | Recommended reading measure |
| --- | --- | --- |
| `compact` | 100% of viewport | 45–75 characters per line |
| `standard` | 100% of viewport | 45–75 characters per line |
| `expanded` | 1200px | 45–75 characters per line (per column) |
| `wide` | 1440px | 45–75 characters per line (per column) |

The reading-measure range restates
[foundations/typography.md §7](foundations/typography.md#7-paragraph-width-alignment-and-truncation-approved-principle)
(`Approved`); the exact container-width pixel values are new and
`Recommended`.

## 10. Gutters and Responsive Spacing

Status: `Recommended` (`KBDL-RSP-005`), pending approval.

| Named role | Recommended gutter | Recommended page-edge margin |
| --- | --- | --- |
| `compact` | `space-4` | `space-4` |
| `standard` | `space-6` | `space-6` |
| `expanded` | `space-8` | `space-8` |
| `wide` | `space-8` | `space-12` |

Gutter and margin values are expressed using the already-`Approved`
spacing scale
([foundations/spacing-layout.md §1.3](foundations/spacing-layout.md#13-default-modular-spacing-system)) —
no new spacing unit is introduced. **Responsive spacing compression**
(reducing a spacing step at smaller breakpoints) **may** occur but
**must not** compress below the next-smaller named step in the
approved scale, and **must not** be applied to spacing that separates
distinguishable interactive targets (see
[accessibility.md §25](accessibility.md#25-target-sizing-and-spacing)).

## 11. Layout Reflow

Status: `Approved` (`KBDL-RSP-006`, directly restates
[WCAG 2.2 SC 1.4.10 Reflow](https://www.w3.org/TR/WCAG22/#reflow), Level
AA).

**Requirements:**

- Content **must** reflow to be usable at a viewport width equivalent to
  320 CSS pixels without requiring horizontal scrolling for reading, and
  at a height equivalent to 256 CSS pixels for content that scrolls
  horizontally by nature (a data table row, for example).
- Exceptions permitted by WCAG 2.2 (content that requires
  two-dimensional layout for usage or meaning — maps, data tables,
  images requiring zoom to identify detail) remain valid exceptions here
  and **must** be explicitly documented per use, not assumed broadly.
- Reflow **must not** cause content or functionality to be lost, only
  rearranged.

## 12. Source Order and Reading Order

Status: `Approved` (`KBDL-RSP-007`, directly restates
[WCAG 2.2 SC 1.3.2 Meaningful Sequence](https://www.w3.org/TR/WCAG22/#meaningful-sequence),
Level A, and the locked responsive-content-priority rule).

**Requirements:**

- Reading order **must** match source order by default.
- Visual reordering (e.g., via layout techniques that change visual
  position without changing source order) **must not** create a
  reading or keyboard-navigation order that contradicts visual
  presentation, per WCAG 2.2 SC 1.3.2 and SC 2.4.3 (Focus Order).
- Where a breakpoint changes visual arrangement, source order **should**
  be re-authored to match, rather than relying on visual-only
  reordering that diverges from keyboard/screen-reader order.

## 13. Navigation Adaptation

Status: `Recommended` (`KBDL-RSP-008`), pending approval for exact
collapse thresholds; the underlying requirement that navigation meaning
stay constant is `Approved` (restates `KBDL-PRN-006`, Consistent System
Behavior).

Conceptual guidance: persistent navigation (visible at `expanded`/`wide`)
**may** collapse to a triggered menu at `compact`/`standard`; collapsing
**must not** change the navigation's interaction meaning (the same items
lead to the same destinations); a collapsed navigation trigger **must**
remain keyboard- and screen-reader-operable per
[accessibility.md §21](accessibility.md#21-keyboard-operability).

## 14. Content-Density Adaptation

Status: `Approved` (`KBDL-RSP-009`, restates
[principles.md §6.1](principles.md#61-clarity-before-spectacle) and
Technical Utility's density-without-prioritization exclusion).

Density (amount of visible content per screen) **must** be reduced, not
merely shrunk, at smaller breakpoints — reducing density means
reorganizing or deferring secondary content via progressive disclosure,
not proportionally scaling down text and controls until they become
illegible or hard to target. Precision Profile dashboards **must** apply
this most rigorously, given their inherently higher baseline density.

## 15. Media and Image Adaptation

Status: `Approved` (`KBDL-RSP-010`, restates
[foundations/iconography-media.md §2.3](foundations/iconography-media.md#23-aspect-relationships-cropping-and-focal-point-preservation),
"media reflows aspect at breakpoints... to preserve focal point rather
than uniform scaling").

Media **must** preserve its documented focal point when its aspect
changes across breakpoints — cropping toward the edges of an image
before its center is prohibited. Media **must not** cause layout shift
after load (per
[foundations/iconography-media.md §2.5](foundations/iconography-media.md#25-loading-behavior-and-performance-considerations)).

## 16. Data-Dense and Tabular Content

Status: `Recommended` (`KBDL-RSP-011`), pending approval.

Conceptual guidance for tables and dense data grids at `compact`/
`standard`: **permitted** approaches — horizontal scroll scoped to the
table region only (never the whole page); a card-per-row transformation
that preserves every column as a labeled field; column priority
collapse (hiding lowest-priority columns behind a "show more" control,
never silently dropping data). **Prohibited:** shrinking text below
the accessible minimum to fit more columns; removing a column's data
without a way to access it. Exact per-project column-priority rules are
implementation-specific and out of scope here.

## 17. Full-Bleed and Asymmetric Layouts

Status: `Approved` (`KBDL-RSP-012`, restates Showcase's documented
compositional emphasis, [principles.md §9.1](principles.md#91-showcase-profile)).

Full-bleed (edge-to-edge) and asymmetric compositions **are** permitted,
primarily in Showcase, provided: text content within them still respects
the reading-measure guidance in [§9](#9-container-widths-and-reading-measures);
the composition reflows without losing content at 320px
([§11](#11-layout-reflow)); and the composition does not become the
default treatment for Precision or Flow's task-focused content.

## 18. Sticky and Fixed Regions

Status: `Approved` (`KBDL-RSP-013`, restates WCAG 2.2 SC 2.4.11 Focus Not
Obscured (Minimum), Level AA, and
[themes/adaptation.md §2.2](themes/adaptation.md#22-rules)'s local
contrast context bounding rule).

**Requirements:**

- A sticky or fixed region **must not** entirely obscure the element
  that currently has keyboard focus.
- A sticky or fixed region's height **must** be accounted for by any
  scroll-to-anchor or in-page navigation, so the target content is not
  hidden beneath it.
- Sticky/fixed regions **must** remain usable at 320px reflow — they
  must not consume so much vertical space at small viewports that
  remaining content becomes unusable.

## 19. Safe Areas and Viewport Edges

Status: `Approved` (`KBDL-RSP-014`, restates Technical Utility's
predictable-behavior quality applied to device physical constraints).

Interactive controls and readable content **must not** be placed where a
device's physical safe-area insets (notches, rounded corners, home
indicators) would obscure or make them hard to activate. This is a
framework-neutral requirement; the specific implementation mechanism
(e.g., environment-variable insets) is out of scope.

## 20. Orientation Changes

Status: `Approved` (`KBDL-RSP-015`, directly restates
[WCAG 2.2 SC 1.3.4 Orientation](https://www.w3.org/TR/WCAG22/#orientation),
Level AA).

Content and functionality **must not** be restricted to a single display
orientation (portrait or landscape) unless a specific orientation is
essential to the content (e.g., a piano-keyboard simulation). Orientation
changes **must not** trigger a decorative motion replay
([motion/accessibility-performance.md §4](motion/accessibility-performance.md#4-mobile-and-input-method-considerations),
already `Approved`).

## 21. Zoom and Enlarged Text

Status: `Approved` (`KBDL-RSP-016`, directly restates
[WCAG 2.2 SC 1.4.4 Resize Text](https://www.w3.org/TR/WCAG22/#resize-text)
and [SC 1.4.10 Reflow](https://www.w3.org/TR/WCAG22/#reflow), both Level
AA).

**Requirements:**

- Text **must** be resizable up to 200% without loss of content or
  functionality, and without requiring assistive technology.
- Layouts **must** remain usable when text is enlarged this way,
  including at the 320px-equivalent reflow width.
- This resolves the "high-zoom and enlarged-text review" that
  [themes/validation.md §1](themes/validation.md#1-theme-validation-specification)
  explicitly deferred to this module — contrast ratios remain valid
  under zoom (zoom does not change relative luminance), but layout
  reflow at enlarged sizes is a distinct requirement, satisfied here.

## 22. Virtual-Keyboard Behavior

Status: `Approved` (`KBDL-RSP-017`, restates
[motion/accessibility-performance.md §4](motion/accessibility-performance.md#4-mobile-and-input-method-considerations)'s
existing virtual-keyboard requirement, extended with layout detail).

**Requirements:**

- When a virtual keyboard reduces visible viewport height, the focused
  field **must** remain visible and not be obscured by the keyboard.
- Layout **must not** trigger decorative reflow animation solely because
  a virtual keyboard appeared or dismissed.
- Content below the fold that becomes newly reachable when the keyboard
  dismisses **must** retain its scroll position rather than jumping
  unexpectedly.

## 23. Touch, Pointer, Keyboard, and Hybrid Input

Status: `Approved` (`KBDL-RSP-018`, restates
[WCAG 2.2 SC 2.5.1 Pointer Gestures](https://www.w3.org/TR/WCAG22/#pointer-gestures)
and [SC 2.5.2 Pointer Cancellation](https://www.w3.org/TR/WCAG22/#pointer-cancellation),
both Level A, and Technical Utility's interaction-predictability quality).

Full requirement text and target-size specifics live in
[accessibility.md §25–§27](accessibility.md#25-target-sizing-and-spacing)
to avoid duplication; this section covers the responsive-layout
consequence: **layouts must not assume any single input method** — a
control usable only via hover or only via a multi-finger gesture
**must** have an equally capable alternative reachable by keyboard,
single-pointer tap, or click.

## 24. Hover-Independent Discoverability

Status: `Approved` (`KBDL-RSP-019`, restates
[WCAG 2.2 SC 1.4.13 Content on Hover or Focus](https://www.w3.org/TR/WCAG22/#content-on-hover-or-focus),
Level AA, and [principles.md §11](principles.md#11-non-conforming-design-directions)
item 5's discoverability exclusion).

Controls **must not** be discoverable only via hover — touch and
keyboard users must have a persistent or equally reachable affordance.
Content revealed on hover or focus **must** be dismissible, hoverable
(remains visible while the pointer moves onto it), and persistent
(remains visible until dismissed or no longer relevant).

## 25. Responsive Focus Management

Status: `Approved` (`KBDL-RSP-020`, restates
[WCAG 2.2 SC 2.4.3 Focus Order](https://www.w3.org/TR/WCAG22/#focus-order),
Level A).

When a breakpoint change alters visible structure (e.g., collapsing
navigation into a menu), focus **must** remain on a sensible, existing
element rather than being lost to the document body. Full focus-order,
focus-visibility, and focus-restoration requirements live in
[accessibility.md §21–§24](accessibility.md#21-keyboard-operability).

### 25.1 Target Sizing Cross-Reference

Exact target-size requirements (WCAG 2.2 SC 2.5.8, Level AA, plus any
KBDL-preferred enhancement) are defined in
[accessibility.md §25](accessibility.md#25-target-sizing-and-spacing) to
avoid duplicating a single normative source; this document's spacing
guidance ([§10](#10-gutters-and-responsive-spacing)) must remain
compatible with whatever target-size minimum is approved there.

## 26. Responsive Motion Behavior

Status: `Approved` (`KBDL-RSP-021`, restates
[motion/accessibility-performance.md §4](motion/accessibility-performance.md#4-mobile-and-input-method-considerations),
already `Approved`, extended with the layout-specific detail below).

Motion amplitude and distance **should** reduce at smaller breakpoints
(per [motion/foundations.md §4](motion/foundations.md#4-motion-intensity),
already `Approved`, "reduce distance, scale, and screen coverage on
small viewports"). This document does not reopen or restate KBDL-005's
timing, easing, or reduced-motion substitution rules — see
[motion/README.md](motion/README.md) for those.

## 27. Performance and Low-Capability Contexts

Status: `Approved` (`KBDL-RSP-022`, restates
[principles.md §6.9](principles.md#69-performance-aware-enhancement)).

Layouts **must** degrade gracefully on constrained devices and
connections: images and media use low-cost placeholders during load
(already established,
[foundations/iconography-media.md §2.5](foundations/iconography-media.md#25-loading-behavior-and-performance-considerations));
layout **must not** shift unexpectedly as deferred content arrives;
dense layouts (`expanded`/`wide`) **should** offer a simplified path on
detected low-capability contexts, though the detection mechanism itself
is implementation-layer and out of scope.

## 28. Showcase Profile Interpretation

May emphasize: full-bleed and asymmetric compositions ([§17](#17-full-bleed-and-asymmetric-layouts));
larger compositional gestures at `wide`; stronger media hierarchy at
every breakpoint. Must preserve: reading comfort, reflow at 320px,
content priority, and hover-independent discoverability identically to
the other profiles.

## 29. Precision Profile Interpretation

May emphasize: higher information density at `expanded`/`wide` (within
the content-density rule, [§14](#14-content-density-adaptation));
persistent, stable navigation across breakpoints; column-priority
collapse for dense tables ([§16](#16-data-dense-and-tabular-content)).
Must preserve: identical accessibility and reflow requirements; no
exception permitting denser-than-usable layouts.

## 30. Flow Profile Interpretation

May emphasize: simplified, guided layouts at `compact` that preserve a
single clear next action; balanced reading measure across breakpoints.
Must preserve: identical navigation-meaning consistency and content
priority as the other profiles.

## 31. Conforming Examples

1. **Compact, touch, Flow.** A guided checkout step at 360px width shows
   one column, one primary action, and a persistent progress indicator;
   the navigation menu collapses to a single trigger with the same
   destinations as the `expanded` sidebar. *Conforms:* content priority
   preserved, navigation meaning unchanged, reflow satisfied.
2. **Standard, keyboard, Precision.** A dashboard at 640px width shows
   two columns; tab order follows the same left-to-right, top-to-bottom
   source order as the visual layout. *Conforms:* source/reading order
   match ([§12](#12-source-order-and-reading-order)).
3. **Expanded, pointer, Showcase.** A portfolio grid at 1000px width
   uses a three-column asymmetric composition; images maintain their
   documented focal point when their aspect changes from `standard`.
   *Conforms:* [§15](#15-media-and-image-adaptation), [§17](#17-full-bleed-and-asymmetric-layouts).
4. **Wide, screen reader, all profiles.** A `wide`-breakpoint page's
   reading measure stays within 45–75 characters despite a 1440px
   container. *Conforms:* [§9](#9-container-widths-and-reading-measures).
5. **Zoom 200%, Flow.** A form reflows to single-column at 200% zoom
   without any field becoming unreachable or losing its label.
   *Conforms:* [§21](#21-zoom-and-enlarged-text).
6. **Orientation change, Precision.** Rotating a tablet from portrait to
   landscape reflows a data table without replaying its entrance
   animation. *Conforms:* [§20](#20-orientation-changes).
7. **Virtual keyboard, Flow.** Focusing a text field on a phone keeps the
   field visible above the virtual keyboard without a decorative scroll
   animation. *Conforms:* [§22](#22-virtual-keyboard-behavior).
8. **Sticky header, keyboard, all profiles.** A sticky header does not
   cover the currently focused form field when tabbing down a long page.
   *Conforms:* [§18](#18-sticky-and-fixed-regions).

## 32. Non-Conforming Examples

1. **Device-name breakpoint.** A layout adds a special rule "for
   iPhone SE" rather than a named, content-justified breakpoint.
   *Violates:* [§5](#5-content-driven-breakpoint-model).
2. **Dropped secondary data on collapse.** A dashboard hides a data
   column at `compact` with no way to reveal it. *Violates:*
   [§4](#4-responsive-content-priority), [§16](#16-data-dense-and-tabular-content).
3. **Reading order mismatch.** A two-column layout at `expanded` is
   visually reordered via layout technique so that screen-reader order
   no longer matches visual order. *Violates:* [§12](#12-source-order-and-reading-order).
4. **Full-page horizontal scroll at 320px.** A page requires horizontal
   scrolling to read body text at a 320px-equivalent width. *Violates:*
   [§11](#11-layout-reflow).
5. **Hover-only navigation.** A Precision dashboard's secondary menu is
   reachable only by mouse hover, with no touch or keyboard equivalent.
   *Violates:* [§24](#24-hover-independent-discoverability).
6. **Sticky region obscures focus.** A sticky footer covers the focused
   button when tabbing to the bottom of a form. *Violates:*
   [§18](#18-sticky-and-fixed-regions).
7. **Orientation lock.** A non-essential content page refuses to
   display in landscape orientation. *Violates:* [§20](#20-orientation-changes).
8. **Layout breaks at 200% zoom.** Enlarging text to 200% causes a
   button label to overflow its container illegibly. *Violates:*
   [§21](#21-zoom-and-enlarged-text).
9. **Virtual keyboard obscures field.** A mobile form's focused field is
   hidden behind the virtual keyboard with no scroll compensation.
   *Violates:* [§22](#22-virtual-keyboard-behavior).
10. **Safe-area violation.** A primary action button sits under a
    device's rounded corner, partially unreachable. *Violates:*
    [§19](#19-safe-areas-and-viewport-edges).
11. **Density via shrinking.** A Precision table fits more rows by
    shrinking row height below a legible/targetable minimum instead of
    reorganizing. *Violates:* [§14](#14-content-density-adaptation).
12. **Media crop toward edge.** A responsive image crop moves toward the
    frame edge instead of preserving its documented focal point.
    *Violates:* [§15](#15-media-and-image-adaptation).

## 33. Normative Requirements

Requirement IDs use `KBDL-RSP-###`
([conventions.md §2](conventions.md#2-requirement-identification)),
starting at `001` (no prior `RSP` requirement exists in the repository).

- **KBDL-RSP-001** — The same content and controls **must** remain
  available at every breakpoint; the most important element on a screen
  **must** remain most prominent at every breakpoint.
  - Lifecycle status: Approved (directly restates the locked
    responsive-content-priority rule, [principles.md §5.1](principles.md#51-locked-identity-rules)).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-PRN-004`, `KBDL-PRN-005`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§4](#4-responsive-content-priority).
  - Validation method: Manual review once implemented; comparing content
    inventory across breakpoints.

- **KBDL-RSP-002** — The four named breakpoint roles **must** use the
  exact minimum-width thresholds in [§7](#7-proposed-exact-breakpoint-thresholds)
  once approved.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation
    status: Not applicable (a numerical recommendation, not yet a
    testable implementation claim).
  - Related requirement: `KBDL-FND-011` (named breakpoint set, Approved).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§7](#7-proposed-exact-breakpoint-thresholds).
  - Validation method: Project-owner review (not yet performed); manual
    implementation review once an implementation exists.

- **KBDL-RSP-003** — Grid column counts **must** use the values in
  [§8](#8-grid-and-column-behavior) once approved.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation
    status: Not applicable.
  - Related requirement: `KBDL-RSP-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§8](#8-grid-and-column-behavior).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-RSP-004** — Container widths and reading measures **must** use
  the values in [§9](#9-container-widths-and-reading-measures) once
  approved.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation
    status: Not applicable.
  - Related requirement: `KBDL-RSP-002`; foundation typography reading
    measure (Approved).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§9](#9-container-widths-and-reading-measures).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-RSP-005** — Gutter and page-edge margin values **must** use
  the values in [§10](#10-gutters-and-responsive-spacing) once approved.
  - Lifecycle status: Recommended. Provenance: Assumed. Validation
    status: Not applicable.
  - Related requirement: `KBDL-RSP-002`; `KBDL-FND-011` (8-step spacing
    scale, Approved).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§10](#10-gutters-and-responsive-spacing).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-RSP-006** — Content **must** reflow to be usable at a 320
  CSS-pixel-equivalent viewport width without requiring horizontal
  scrolling for reading, except where a documented WCAG exception
  applies.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.4.10,
    Level AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-018` (see [accessibility.md](accessibility.md)).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11](#11-layout-reflow).
  - Validation method: Manual reflow testing once an implementation
    exists (documented as a distinct method in [§34](#34-responsive-validation-matrix)).

- **KBDL-RSP-007** — Reading order **must** match source order by
  default; visual reordering **must not** create a reading or
  keyboard-navigation order contradicting visual presentation.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.3.2 and
    SC 2.4.3, both cited). Provenance: Confirmed. Validation status: Not
    verified.
  - Related requirement: `KBDL-A11Y-010`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§12](#12-source-order-and-reading-order).
  - Validation method: Manual keyboard/screen-reader order review once
    implemented.

- **KBDL-RSP-008** — Navigation **may** collapse structurally at smaller
  breakpoints but **must not** change interaction meaning; exact
  collapse thresholds use the values approved under `KBDL-RSP-002`.
  - Lifecycle status: Recommended (the constant-meaning rule is Approved
    per `KBDL-PRN-006`; exact collapse thresholds are new). Provenance:
    Assumed. Validation status: Not verified.
  - Related requirement: `KBDL-RSP-002`, `KBDL-PRN-006`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§13](#13-navigation-adaptation).
  - Validation method: Manual review once implemented; project-owner
    review of thresholds (not yet performed).

- **KBDL-RSP-009** — Content density **must** reduce via reorganization
  or progressive disclosure at smaller breakpoints, never via
  proportional shrinking below legible/targetable minimums.
  - Lifecycle status: Approved (directly restates `KBDL-PRN-003`,
    Clarity Before Spectacle, and Technical Utility's density
    exclusion). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-025` (target sizing).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14](#14-content-density-adaptation).
  - Validation method: Manual review once implemented.

- **KBDL-RSP-010** — Media **must** preserve its documented focal point
  across aspect changes and **must not** cause layout shift after load.
  - Lifecycle status: Approved (directly restates
    [foundations/iconography-media.md §2.3, §2.5](foundations/iconography-media.md#23-aspect-relationships-cropping-and-focal-point-preservation)).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: Foundation media requirements (Approved for
    strategy; exact values Unresolved per foundations/iconography-media.md).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§15](#15-media-and-image-adaptation).
  - Validation method: Manual review once implemented.

- **KBDL-RSP-011** — Data-dense and tabular content **must** use scoped
  horizontal scroll, card transformation, or column-priority collapse
  at smaller breakpoints — never silent data loss.
  - Lifecycle status: Recommended (new KBDL-006 policy). Provenance:
    Assumed. Validation status: Not verified.
  - Related requirement: `KBDL-RSP-001`.
  - Applicable profiles: Precision primarily; Showcase, Flow as
    applicable.
  - Specification location: [§16](#16-data-dense-and-tabular-content).
  - Validation method: Manual review once implemented; project-owner
    review (not yet performed).

- **KBDL-RSP-012** — Full-bleed and asymmetric compositions **are**
  permitted provided reading measure, 320px reflow, and profile
  task-focus requirements remain satisfied.
  - Lifecycle status: Approved (restates Showcase's documented
    compositional emphasis, already `Approved` per
    [principles.md §9.1](principles.md#91-showcase-profile)). Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-RSP-004`, `KBDL-RSP-006`.
  - Applicable profiles: Showcase primarily.
  - Specification location: [§17](#17-full-bleed-and-asymmetric-layouts).
  - Validation method: Manual review once implemented.

- **KBDL-RSP-013** — A sticky or fixed region **must not** entirely
  obscure the currently focused element, and **must** be accounted for
  by in-page scroll targets.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.4.11,
    Level AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-023`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§18](#18-sticky-and-fixed-regions).
  - Validation method: Manual keyboard-focus review once implemented.

- **KBDL-RSP-014** — Interactive controls and readable content **must
  not** be placed where a device's safe-area insets would obscure or
  make them hard to activate.
  - Lifecycle status: Approved (restates Technical Utility's
    predictable-behavior quality). Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-A11Y-025`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§19](#19-safe-areas-and-viewport-edges).
  - Validation method: Manual review on representative devices once
    implemented.

- **KBDL-RSP-015** — Content and functionality **must not** be
  restricted to a single display orientation unless that orientation is
  essential.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.3.4,
    Level AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§20](#20-orientation-changes).
  - Validation method: Manual orientation testing once implemented.

- **KBDL-RSP-016** — Text **must** be resizable to 200% and layouts
  **must** remain usable at that size, including at 320px-equivalent
  reflow width.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.4.4 and
    SC 1.4.10, both Level AA). Provenance: Confirmed. Validation status:
    Not verified.
  - Related requirement: `KBDL-RSP-006`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§21](#21-zoom-and-enlarged-text).
  - Validation method: Manual zoom/reflow testing once implemented.

- **KBDL-RSP-017** — A virtual keyboard **must not** obscure the
  focused field, and its appearance/dismissal **must not** trigger
  decorative reflow animation or unexpected scroll-position loss.
  - Lifecycle status: Approved (restates
    [motion/accessibility-performance.md §4](motion/accessibility-performance.md#4-mobile-and-input-method-considerations),
    already Approved, extended with layout detail). Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-MOT-025`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22](#22-virtual-keyboard-behavior).
  - Validation method: Manual mobile testing once implemented.

- **KBDL-RSP-018** — Layouts **must not** assume a single input method;
  any hover-only or multi-finger-gesture-only control **must** have an
  equally capable keyboard or single-pointer alternative.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.5.1 and
    SC 2.5.2, both Level A). Provenance: Confirmed. Validation status:
    Not verified.
  - Related requirement: `KBDL-A11Y-026`, `KBDL-A11Y-027`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§23](#23-touch-pointer-keyboard-and-hybrid-input).
  - Validation method: Manual cross-input testing once implemented.

- **KBDL-RSP-019** — Controls **must not** be discoverable only via
  hover; hover/focus-revealed content **must** be dismissible,
  hoverable, and persistent.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.4.13,
    Level AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24](#24-hover-independent-discoverability).
  - Validation method: Manual review once implemented.

- **KBDL-RSP-020** — Focus **must** remain on a sensible element when a
  breakpoint change alters visible structure.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.4.3,
    Level A). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-021`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§25](#25-responsive-focus-management).
  - Validation method: Manual keyboard testing once implemented.

- **KBDL-RSP-021** — Motion amplitude and distance **should** reduce at
  smaller breakpoints, consistent with the already-Approved motion
  intensity model.
  - Lifecycle status: Approved (restates
    [motion/foundations.md §4](motion/foundations.md#4-motion-intensity),
    already Approved). Provenance: Confirmed. Validation status: Not
    verified.
  - Related requirement: `KBDL-MOT-006`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§26](#26-responsive-motion-behavior).
  - Validation method: Manual review once implemented.

- **KBDL-RSP-022** — Layouts **must** degrade gracefully on constrained
  devices/connections without unexpected layout shift as deferred
  content arrives.
  - Lifecycle status: Approved (restates
    [principles.md §6.9](principles.md#69-performance-aware-enhancement)).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§27](#27-performance-and-low-capability-contexts).
  - Validation method: Manual review; implementation-level performance
    measurement once an implementation exists.

## 34. Responsive Validation Matrix

| Requirement | Validation method | Status |
| --- | --- | --- |
| `KBDL-RSP-001` | Content-inventory comparison across breakpoints | Not verified |
| `KBDL-RSP-002`–`005` | Project-owner review (approval); implementation review (later) | Not verified; awaiting approval |
| `KBDL-RSP-006` | Manual reflow test at 320px-equivalent width | Not verified |
| `KBDL-RSP-007` | Manual keyboard/screen-reader order review | Not verified |
| `KBDL-RSP-008` | Manual review + threshold approval | Not verified |
| `KBDL-RSP-009` | Manual review | Not verified |
| `KBDL-RSP-010` | Manual review | Not verified |
| `KBDL-RSP-011` | Manual review + approval | Not verified |
| `KBDL-RSP-012` | Manual review | Not verified |
| `KBDL-RSP-013` | Manual keyboard-focus review | Not verified |
| `KBDL-RSP-014` | Manual device review | Not verified |
| `KBDL-RSP-015` | Manual orientation test | Not verified |
| `KBDL-RSP-016` | Manual zoom/reflow test | Not verified |
| `KBDL-RSP-017` | Manual mobile test | Not verified |
| `KBDL-RSP-018` | Manual cross-input test | Not verified |
| `KBDL-RSP-019` | Manual review | Not verified |
| `KBDL-RSP-020` | Manual keyboard test | Not verified |
| `KBDL-RSP-021` | Manual review | Not verified |
| `KBDL-RSP-022` | Manual review; performance measurement (later) | Not verified |

All rows are `Not verified` because no implementation exists to test —
this is a design-language specification step. Manual documentation
review (confirming purpose/method/status completeness) is distinct from
implementation-level `Verified` status and is recorded separately in
[§37](#37-traceability).

## 35. Responsive Decision Packet

### 35.1 Already-Approved Responsive Architecture (context only)

Not awaiting approval — provided as context. Directly supported by
prior approved decisions: the four named breakpoint roles and
content-driven philosophy (`KBDL-DEC-012`); responsive-content priority
(locked, `principles.md §5.1`); reflow, resize-text, source-order,
orientation, pointer-gesture, pointer-cancellation, content-on-hover,
focus-order, and focus-not-obscured requirements (`KBDL-RSP-006`,
`007`, `009`, `010`, `012`–`022`, all directly restating WCAG 2.2
Level A/AA or already-approved KBDL principles).

### 35.2 Recommended Decisions — Ready for Approval

| # | Decision | Recommendation | Rationale | Alternatives | Trade-offs | Accessibility impact | Performance impact | Profile impact | Dependencies |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Exact breakpoint thresholds | Adopt 0/600/905/1240px for compact/standard/expanded/wide ([§7](#7-proposed-exact-breakpoint-thresholds), `KBDL-RSP-002`) | Reflects genuine content-reorganization points at common reading-column widths | Device-based thresholds (rejected, violates approved philosophy) | May need revision once real content is authored | Must remain compatible with 320px reflow regardless of value | None at this level | Showcase may add profile-scoped breakpoints within these; shared roles unaffected | `KBDL-FND-011` |
| 2 | Grid column counts | Adopt 4/8/12/12 columns ([§8](#8-grid-and-column-behavior), `KBDL-RSP-003`) | Matches typical multi-region layout needs per role | A fixed 12-column grid at every size (rejected — forces unnecessary subdivision at compact) | Column count is a proportion reference, not a rigid mandate | Not applicable at this level | None | Precision benefits most from higher column counts at expanded/wide | `KBDL-RSP-002` |
| 3 | Container widths and reading measures | Adopt the values in [§9](#9-container-widths-and-reading-measures) (`KBDL-RSP-004`) | Keeps reading measure within the already-approved 45–75 character range at every breakpoint | Unconstrained full-width text at wide (rejected — breaks reading measure) | Requires per-column width tracking at multi-column breakpoints | Supports reading comprehension, an accessibility-adjacent benefit | None | Applies identically across profiles | `KBDL-RSP-002`, foundation typography |
| 4 | Gutters and margins | Adopt the values in [§10](#10-gutters-and-responsive-spacing) (`KBDL-RSP-005`) | Uses the existing approved spacing scale, no new unit | A separate gutter-specific scale (rejected — fragments the spacing system) | None significant | Spacing compression must not go below target-size-compatible minimums | None | Applies identically across profiles | `KBDL-RSP-002`, foundation spacing scale |
| 5 | Navigation collapse thresholds | Adopt collapse at `standard` for persistent-to-menu transition (`KBDL-RSP-008`) | Matches the point where a persistent sidebar plus content no longer fits comfortably | Collapsing only at `compact` (rejected — persistent nav at 600–904px crowds content) | Requires testing the exact collapse point against real navigation content | Collapsed trigger must remain keyboard/screen-reader operable, unaffected by this decision | None | Applies identically; profiles vary navigation style, not the threshold | `KBDL-RSP-002` |
| 6 | Data-dense/tabular responsive strategy | Adopt scoped horizontal scroll, card transformation, and column-priority collapse as the three permitted strategies (`KBDL-RSP-011`) | Covers the realistic range of dense-table responsive needs without prescribing one universal technique | A single mandatory technique (rejected — different data shapes need different strategies) | Requires per-table judgment about which strategy fits | Column-priority collapse must never silently drop data | None | Precision benefits most; Showcase/Flow rarely apply | `KBDL-RSP-001` |

### 35.3 Unresolved or Not Approval-Ready

- **Device-performance detection strategy** for [§27](#27-performance-and-low-capability-contexts) —
  implementation-layer, out of scope.
- **Exact safe-area implementation mechanism** ([§19](#19-safe-areas-and-viewport-edges)) —
  implementation-layer, out of scope.
- **Browser-support matrix** — not proposed; explicitly out of scope per
  this prompt.
- **Per-project column-priority rules** for dense tables — inherently
  project-specific.
- **Component-specific responsive variants** — deferred to the
  Components module (`CMP`).

**Exact scope of a future approval:** an `APPROVE` response to
[§35.2](#352-recommended-decisions--ready-for-approval) would authorize
exactly items 1–6 above — the four exact breakpoint thresholds, grid
column counts, container widths/reading measures, gutters/margins,
navigation collapse thresholds, and the data-dense/tabular strategy. It
would **not** approve any [§35.3](#353-unresolved-or-not-approval-ready)
item, any component-specific value, or any KBDL-007-or-later content. It
would not itself constitute validation of any item — see
[§34](#34-responsive-validation-matrix).

## 36. Deferred and Unresolved Responsive Items

- Exact breakpoint thresholds, grid columns, container widths, gutters,
  navigation collapse points, and data-dense strategy — `Recommended`,
  pending [§35.2](#352-recommended-decisions--ready-for-approval).
- Device-performance detection, safe-area implementation mechanism,
  browser-support matrix, per-project column priority — `Unresolved`/
  out of scope, per [§35.3](#353-unresolved-or-not-approval-ready).
- Component-specific responsive behavior — `Deferred` to the Components
  module (`CMP`, KBDL-007+).

## 37. Traceability

See [traceability-matrix.md](traceability-matrix.md) for how each
`KBDL-RSP-###` requirement traces to its blueprint origin, approval
status, validation status, and evidence, and
[decision-register.md](decision-register.md) for any decision recorded
as part of this module.
