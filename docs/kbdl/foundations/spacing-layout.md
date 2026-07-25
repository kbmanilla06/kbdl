# KBDL Foundations — Spacing, Layout, and Breakpoints

Lifecycle status of this document's **architecture and rules**: `Approved`,
derived from [principles.md](../principles.md). Lifecycle status of the
**recommended modular scale, grid model, and breakpoint values**:
`Recommended` — requires project-owner approval; see
[foundations/README.md § Foundation Status Model](README.md#3-foundation-status-model).

Return to the [foundations index](README.md) · [specification index](../README.md).

This document defines KBDL's spatial system (spacing and sizing) and its
layout and grid principles, including breakpoint philosophy. It proposes a
recommended modular scale and content-driven breakpoint approach. It does
not define exact pixel/rem values as final, and detailed responsive
interaction behavior is deferred to KBDL-006.

---

## 1. Spacing and Sizing Logic

This section defines KBDL's spatial architecture: required principles,
spatial categories, a recommended modular scale, and density/exception
rules.

### 1.1 Required principles (Approved)

- **Spacing follows a deliberate, repeated rhythm.** This is a locked rule
  per [principles.md §5.1](../principles.md#51-locked-identity-rules) and
  [principles.md §7](../principles.md#7-visual-consistency); arbitrary,
  one-off spacing values are prohibited (non-conforming pattern 10).
- **Density variation is a controlled variable**, not a separate spacing
  system per profile — see
  [principles.md §5.2](../principles.md#52-controlled-visual-variables)
  ("content density").
- **Touch usability must not be sacrificed for density.** Precision's
  denser layouts must still meet touch-target and tap-spacing minimums
  (see §5).
- **Optical adjustment is permitted only to correct a perceptual
  imbalance the rhythm itself creates** (for example, adjusting for a
  glyph's visual weight), never to justify an arbitrary one-off value.

### 1.2 Spatial categories (Approved architecture)

- **Atomic spacing** — the smallest deliberate gap, used between closely
  related elements (e.g., an icon and its label).
- **Component spacing** — internal padding and gaps within a single
  component.
- **Section spacing** — separation between logical groups of content
  within a page.
- **Page spacing** — outer margins between page content and the viewport
  edge.
- **Content grouping (inset spacing)** — padding inside a container that
  separates its edge from its content.
- **Stack spacing** — vertical rhythm between stacked elements.
- **Inline spacing** — horizontal rhythm between elements in a row.

### 1.3 Recommended modular spacing system

Status: `Recommended`, `Assumed` provenance, `Not verified` validation.

A single-base modular scale, expressed as multiples of one atomic unit
(the exact unit value in px/rem is deferred — see §7 Unresolved):

| Step | Multiple of base unit | Intended category |
| --- | --- | --- |
| space-1 | 1× | Atomic spacing (icon-to-label gap) |
| space-2 | 2× | Tight component-internal spacing |
| space-3 | 3× | Standard component-internal spacing |
| space-4 | 4× | Inline spacing between related controls |
| space-6 | 6× | Stack spacing between related content blocks |
| space-8 | 8× | Section spacing within a page |
| space-12 | 12× | Page spacing / major section separation |
| space-16 | 16× | Macro rhythm for large compositional breaks (Showcase) |

This is a **limited, named step set** by design — new intermediate steps
require an approved exception rather than ad hoc insertion, to preserve
the "deliberate repeated rhythm" locked rule.

### 1.4 Touch and pointer considerations

- Interactive elements must maintain a minimum touch-target size and
  minimum spacing between adjacent targets sufficient to avoid accidental
  activation, regardless of profile density.
- Precision's denser layouts achieve density through reduced *content*
  spacing (labels, rows), not through shrinking interactive targets below
  the accessible minimum.

### 1.5 Density variations (profile-level)

- **Showcase:** favors the upper end of the scale (space-8 through
  space-16) for generous, editorial rhythm.
- **Precision:** favors the lower-to-middle end (space-2 through space-6)
  for information density, never dropping below the touch-target rule in
  §1.4.
- **Flow:** favors the middle of the scale (space-3 through space-8) for
  comfortable, approachable rhythm.

### 1.6 Responsive compression

- Section and page spacing (space-8, space-12, space-16) may compress at
  smaller breakpoints; atomic and component spacing (space-1 through
  space-4) should remain stable, since they support in-component
  legibility rather than page-level composition.

### 1.7 Exception handling

- A one-off spacing value outside the named step set requires an approved
  exception recorded per
  [governance.md § Exception process](../governance.md#exception-process),
  with the specific optical or content justification stated.

## 2. Layout and Grid Principles (Approved architecture)

- **Page containers:** every page has a defined maximum content width
  appropriate to its profile; full-bleed regions are permitted only for
  media or background treatments, never for body text measure.
- **Content width / reading width:** see §4.
- **Full-bleed regions:** used for imagery, video, or decorative
  background; text content within a full-bleed region must still respect
  the reading-width rule.
- **Column behavior:** columns collapse by content priority (see §3), not
  by uniform proportional shrinking.
- **Alignment zones:** content aligns to a shared set of vertical guides
  consistent with the grid, not to ad hoc per-component alignment.
- **Gaps:** follow the spacing scale in §1.3, not an independent grid-gap
  value.
- **Nested grids:** a grid within a grid (e.g., a card grid inside a page
  grid) must align its own gutters to the outer grid's gap scale.
- **Vertical rhythm:** stack spacing (§1.2) governs vertical rhythm
  between sections, ensuring consistent "beats" down a page.
- **Dashboard density (Precision):** favors more columns and tighter
  gutters, within the touch and rhythm rules above.
- **Editorial composition (Showcase):** favors asymmetric, larger
  compositional blocks; see below.
- **Consumer-flow layouts (Flow):** favor a single, clear column for
  guided steps, widening only for supporting content.
- **Responsive rearrangement:** reflows by content priority (§3), not by
  uniform scaling.
- **Source-order preservation:** the semantic/reading order of content
  must not diverge from its visual order when the layout reflows, so
  assistive technology and sighted users experience the same sequence.
- **Asymmetric composition:** permitted, especially in Showcase, provided
  hierarchy and reading order remain clear.
- **Intentional overlap:** permitted for compositional effect (e.g., an
  image overlapping a text block) only where it does not obscure content
  or reduce contrast.
- **Safe areas:** layouts must respect device safe areas (notches, home
  indicators) so critical content and controls are never obscured.
- **Sticky and fixed regions:** used sparingly, only for content the user
  benefits from having persistently available (e.g., a primary action or
  navigation), and must never cover a focus target when navigating by
  keyboard.

## 3. Content-Driven Breakpoint Philosophy (Approved principle, Recommended values)

This section defines how KBDL decides when a breakpoint is justified and
proposes a recommended, content-named breakpoint set.

### 3.1 Required principle (Approved)

Breakpoints are justified by **content and interaction needs**, not by
matching specific device names or screen sizes. A breakpoint is introduced
only where:

- The content's layout genuinely needs to reorganize (e.g., a multi-column
  layout would otherwise become too narrow to read).
- Navigation needs to change structure (e.g., a horizontal nav becomes a
  collapsed menu).
- Interaction model changes matter (e.g., hover-dependent affordances need
  a touch-accessible equivalent).

### 3.2 What conditions justify a breakpoint

- Column count can no longer maintain the reading-width rule (§4).
- Navigation density exceeds comfortable horizontal space.
- Media aspect or size needs to change to preserve focal content (see
  [iconography-media.md](iconography-media.md)).
- Touch-target spacing (§1.4) can no longer be maintained at the current
  layout density.

### 3.3 How content priority changes

At each breakpoint, content is re-ranked by task relevance for that
context (e.g., a secondary metric may drop below the fold on a small
viewport before a primary metric does), never dropped outright, per the
locked responsive-content-priority rule
([principles.md §5.1](../principles.md#51-locked-identity-rules)).

### 3.4 How columns collapse, navigation adapts, density changes, media behaves

- Columns collapse from the least-prioritized column inward, not from
  edge to edge uniformly.
- Navigation adapts from a full horizontal presentation to a condensed or
  drawer-based presentation once it can no longer fit its full label set
  legibly.
- Density (§1.5) may reduce spacing before it reduces content, since
  removing spacing preserves comprehension longer than removing content.
- Media reflows its aspect and cropping (see
  [iconography-media.md § Aspect Relationships](iconography-media.md#23-aspect-relationships-cropping-and-focal-point-preservation))
  to preserve its focal point, rather than being uniformly scaled down.

### 3.5 Avoiding "shrunk desktop" layouts

A layout must be evaluated independently at each breakpoint against
content priority (§3.3); passing a check only at a "desktop" reference
size and applying uniform scaling below it is explicitly prohibited
(non-conforming pattern 8 in
[principles.md §11](../principles.md#11-non-conforming-design-directions)).

### 3.6 Recommended breakpoint set

Status: `Recommended`, `Assumed` provenance, `Not verified` validation.

A minimal, content-justified set (named by role, not device):

| Name | Approximate role |
| --- | --- |
| compact | Single-column, touch-first layouts |
| standard | Introduces secondary columns / expanded navigation |
| expanded | Introduces dashboard-density multi-column layouts |
| wide | Introduces maximum content width and full editorial composition |

Exact pixel values for these named breakpoints are deferred to KBDL-006
(Responsive Behavior); this document establishes only the philosophy and
named roles.

## 4. Reading Width (Approved principle)

Body text content is constrained to a comfortable reading measure
regardless of container width, so a wide viewport does not force
uncomfortably long lines; this rule underlies the typography paragraph-
width rule in [typography.md §7](typography.md#7-paragraph-width-alignment-and-truncation-approved-principle).

## 5. Touch and Pointer Considerations (cross-reference)

See §1.4 above; this rule applies identically across Layout and Spacing
and must not be relaxed for Precision's density goals.

## 6. Conceptual Conformance Examples

**Conforming:** A Precision dashboard reduces stack spacing from space-6 to
space-3 between data rows to increase density, while keeping row-action
touch targets at the accessible minimum size — density achieved without
violating touch usability.

**Non-conforming:** A layout applies a single "shrink factor" to an entire
desktop grid to produce a mobile layout, preserving relative column
proportions but making body text illegibly narrow — violates both the
reading-width rule and the "no shrunk-desktop layouts" rule (§3.5).

## 7. Unresolved Spacing/Layout Decisions

- Exact base spacing unit (px/rem) — `Unresolved`, deferred pending an
  implementation-unit convention.
- Exact breakpoint pixel values — `Unresolved`, deferred to KBDL-006.
- Exact grid column counts and gutter values per named breakpoint —
  `Unresolved`, deferred to KBDL-006.
