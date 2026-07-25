# KBDL Foundations — Typography

Lifecycle status of this document's **architecture and role model**:
`Approved`, derived from [principles.md](../principles.md). Lifecycle
status of the **recommended type scale and typeface strategy**:
`Recommended` — requires project-owner approval; see
[foundations/README.md § Foundation Status Model](README.md#3-foundation-status-model).

Return to the [foundations index](README.md) · [specification index](../README.md).

This document defines KBDL's typography architecture and role model, and
proposes a recommended type scale and typeface strategy. It does not
select a final commercial or proprietary typeface, and does not define
component-specific typography beyond general control-text roles.

---

## 1. Required Principles (Approved)

- **General-consumer readability takes priority over technological
  styling.** Per
  [principles.md §6.3 Consumer Comprehension](../principles.md#63-consumer-comprehension),
  no typographic choice may reduce readability for the sake of a
  "technological" look.
- **Monospaced typography must not become the default interface voice**,
  per [principles.md §3](../principles.md#3-technical-utility) and
  non-conforming pattern 9.
- **Typography must preserve clear hierarchy without relying only on
  size.** Weight, color (text role, not hue alone), spacing, and position
  must all participate in hierarchy, consistent with
  [principles.md §6.4 Visual Hierarchy](../principles.md#64-visual-hierarchy).
- **Display typography must not reduce comprehension.** Large, expressive
  type in Showcase contexts must remain legible and must not obscure
  meaning for impact alone.
- **Dense SaaS interfaces must remain readable.** Precision-profile
  typography must not sacrifice legibility to fit more content.
- **Portfolio typography may be more expressive but must preserve reading
  comfort**, per
  [principles.md §9.1 Showcase Profile](../principles.md#91-showcase-profile).
- **Consumer applications must favor approachable and predictable text
  hierarchy**, per
  [principles.md §9.3 Flow Profile](../principles.md#93-flow-profile).

## 2. Typeface-Role Architecture (Approved)

Typography roles are organized by **function**, not by a specific font
choice:

- **Display** — large-scale, high-impact type for hero or editorial
  moments (primarily Showcase).
- **Heading** — section and page-structure headings across all profiles.
- **Body** — primary reading content.
- **Interface** — control labels, navigation labels, and other UI chrome
  text.
- **Labels and metadata** — small supporting text identifying a field,
  status, or timestamp.
- **Numeric and tabular** — data and metrics, particularly in Precision
  contexts, where numeral alignment and consistent digit width matter.
- **Code or technical content** — reserved narrowly for genuinely
  technical or tabular-code content, never for general interface voice
  (see §1).

## 3. Type Scale and Text Roles

Status: `Approved` — architecture and the specific scale relationships
below were both approved by the project owner via the
[foundation decision packet](README.md#6-foundation-decision-packet); see
[KBDL-DEC-012](../decision-register.md#kbdl-dec-012--foundation-decision-packet-approved).
Provenance: `User-provided` (project-owner approval). Validation status:
`Not verified` — approval authorizes the ratios as KBDL's default; it does
not itself constitute rendering or usability validation.

For each role: purpose, hierarchical relationship, weight intent,
line-height intent, tracking intent, responsive behavior, profile
adjustments, accessibility considerations, and a recommended scale
relationship (expressed as a ratio to a base body size, not a final pixel
value, since exact sizing is deferred to project implementation once a
scale is approved).

### 3.1 Display

- **Purpose:** Large editorial or hero statements.
- **Hierarchy:** Highest visual weight; used sparingly, at most once per
  view.
- **Weight intent:** Bold to heavy.
- **Line-height intent:** Tight (below body line-height ratio) to preserve
  compositional impact without harming multi-line legibility.
- **Tracking intent:** Neutral to slightly tightened at large sizes.
- **Responsive behavior:** Scales down proportionally more aggressively
  than body text across breakpoints, since its impact depends on
  available composition space.
- **Profile adjustments:** Prominent in Showcase; rare-to-absent in
  Precision; used sparingly in Flow (e.g., a single onboarding headline).
- **Accessibility considerations:** Must still meet heading semantic
  structure; must not be the only cue that a section is a page's primary
  heading.
- **Recommended scale relationship:** Approximately 2.5–3× the body base
  size.

### 3.2 Heading (levels 1–3, conceptual)

- **Purpose:** Structural section hierarchy.
- **Hierarchy:** Three conceptual levels are sufficient for KBDL's
  purposes; additional visual levels should be achieved through spacing
  and weight rather than new sizes.
- **Weight intent:** Semibold to bold, decreasing slightly at lower
  levels.
- **Line-height intent:** Moderate; tighter than body, looser than
  display.
- **Tracking intent:** Neutral.
- **Responsive behavior:** Scales down moderately; must remain
  distinguishable from body at the smallest supported viewport.
- **Profile adjustments:** Precision may compress heading size more
  aggressively than Showcase to preserve density without losing hierarchy.
- **Accessibility considerations:** Must map to real semantic heading
  levels in markup; visual level and semantic level must not diverge.
- **Recommended scale relationship:** Approximately 1.9×, 1.5×, and 1.25×
  the body base size for levels 1–3.

### 3.3 Body

- **Purpose:** Primary reading content.
- **Hierarchy:** The reference point (1×) all other roles scale from.
- **Weight intent:** Regular.
- **Line-height intent:** Generous (roughly 1.4–1.6× the type size) to
  support sustained reading comfort.
- **Tracking intent:** Neutral (0).
- **Responsive behavior:** Minimal size change across breakpoints; line
  length adapts instead (see [spacing-layout.md](spacing-layout.md)).
- **Profile adjustments:** Flow may use a marginally larger body size for
  approachability; Precision keeps the reference size to preserve density.
- **Accessibility considerations:** Must remain resizable by the user
  (relative units, not fixed absolute sizing) and must never fall below
  commonly recommended minimum comfortable reading size.
- **Recommended scale relationship:** 1× (the base reference).

### 3.4 Interface

- **Purpose:** Control labels, navigation, and chrome.
- **Hierarchy:** Slightly below or equal to body, never above it, since
  interface chrome should not outweigh content.
- **Weight intent:** Medium, to remain legible at smaller sizes.
- **Line-height intent:** Tighter than body, since interface text is
  usually single-line.
- **Tracking intent:** Neutral to slightly opened at small sizes for
  legibility.
- **Responsive behavior:** Must remain legible and touch-target-compatible
  at the smallest supported viewport (see
  [spacing-layout.md § Touch and Pointer Considerations](spacing-layout.md#5-touch-and-pointer-considerations-cross-reference)).
- **Profile adjustments:** Precision favors a slightly smaller, denser
  interface role; Flow keeps it closer to body size for approachability.
- **Accessibility considerations:** Must maintain the contrast
  requirements from [color.md](color.md) at its actual rendered size.
- **Recommended scale relationship:** Approximately 0.875–1× the body
  base size.

### 3.5 Labels and metadata

- **Purpose:** Field labels, timestamps, secondary annotations.
- **Hierarchy:** Below interface text.
- **Weight intent:** Regular to medium.
- **Line-height intent:** Tight.
- **Tracking intent:** Slightly opened, especially for all-caps
  treatments (all-caps label text, if used, requires added tracking to
  remain legible).
- **Responsive behavior:** Rarely resizes; may increase touch spacing
  around it instead of the text itself.
- **Profile adjustments:** Precision uses this role heavily (dense data
  contexts); Showcase uses it sparingly.
- **Accessibility considerations:** Must still meet the applicable
  contrast threshold for its size (large-text or normal-text threshold
  depending on rendered size).
- **Recommended scale relationship:** Approximately 0.75–0.8125× the body
  base size.

### 3.6 Numeric and tabular

- **Purpose:** Data, metrics, tables.
- **Hierarchy:** Matches body or interface role in size, but uses
  tabular (fixed-width) figures so numbers align vertically in columns.
- **Weight intent:** Regular, with medium available for emphasis totals.
- **Line-height intent:** Matches the surrounding role (body or
  interface).
- **Tracking intent:** Neutral.
- **Responsive behavior:** Must degrade gracefully (e.g., truncate or wrap
  a label, not the numeral) when space is constrained.
- **Profile adjustments:** Central to Precision; used more sparingly in
  Showcase and Flow (e.g., pricing).
- **Accessibility considerations:** Tabular alignment itself is a
  readability aid for comparing values; it must not be dropped in dense
  tables.
- **Recommended scale relationship:** Matches body or interface, whichever
  role it appears alongside.

### 3.7 Code or technical content

- **Purpose:** Genuinely technical or code-like content only (see §1).
- **Hierarchy:** Distinct from body via a monospaced treatment, used only
  where content is actually technical.
- **Weight intent:** Regular.
- **Line-height intent:** Slightly looser than body to aid scanning of
  technical syntax.
- **Tracking intent:** Neutral.
- **Responsive behavior:** May require horizontal scroll for long technical
  lines rather than forcing a wrap that breaks meaning.
- **Profile adjustments:** Rare in all three profiles; most relevant to
  Precision if it exposes technical identifiers.
- **Accessibility considerations:** Must not be the default reading voice
  for any general-consumer content, per §1.
- **Recommended scale relationship:** Matches body or interface, whichever
  role it appears alongside.

### 3.8 Button and control text

- Uses the Interface role (§3.4) by definition; not a separate scale
  step, to avoid arbitrary role proliferation.

### 3.9 Captions

- **Purpose:** Media captions, footnote-style annotations.
- **Recommended scale relationship:** Same tier as Labels and metadata
  (§3.5); not a separate step.

### 3.10 Legal or auxiliary text

- **Purpose:** Legal disclaimers, fine print.
- **Recommended scale relationship:** Same tier as Labels and metadata
  (§3.5), with a requirement that it still meet the applicable contrast
  threshold — legal text is not exempt from accessibility requirements.

## 4. Weight, Width, and Optical-Size Considerations (Approved principle, Recommended specifics)

- **Weight hierarchy:** A working KBDL typeface family should offer at
  least regular, medium, semibold, and bold weights, so hierarchy can be
  expressed through weight without changing size at every step.
- **Width and optical size:** Where a variable or optical-size-aware
  typeface is available, Display and Heading roles should draw from a
  wider or display-optical cut, and Body/Interface roles from a text-
  optical cut, for legibility at their respective sizes. This is a
  `Recommended` preference, not a requirement, since it depends on the
  eventual typeface choice (§5).

## 5. Typeface Model

This section separates which typeface characteristics are locked,
controlled, and open, and defines selection, fallback, and licensing
criteria for a future project typeface.

### 5.1 Locked characteristics (Approved)

- The role architecture in §2 and the hierarchy relationships in §3.
- The principle that interface and body text prioritize readability over
  personality (§1).
- The requirement that any typeface support tabular figures for the
  Numeric role (§3.6).

### 5.2 Controlled characteristics

- Typeface **personality** (geometric, humanist, grotesque character) —
  see [principles.md §5.2](../principles.md#52-controlled-visual-variables)'s
  "typography personality" controlled variable.
- Exact weight availability, beyond the minimum set in §4.

### 5.3 Open brand choices

- The specific typeface family itself, provided it satisfies §5.1 and the
  selection criteria in §5.4.

### 5.4 Selection criteria for future project typefaces

A typeface considered for KBDL use should be evaluated against:

- Legibility at small interface sizes, not only at display sizes.
- Availability of at least regular, medium, semibold, and bold weights.
- Tabular figure support (or an acceptable numeric-only substitute).
- Broad script/language coverage appropriate to the project's audience.
- Reliable web-licensing terms (see §5.6).

### 5.5 Required fallback behavior

Every typeface role must degrade to a **system font stack** appropriate to
its role (a general sans-serif stack for Display/Heading/Body/Interface, a
monospace stack for Code) if the primary typeface fails to load, so
content never becomes unreadable or invisible while waiting on a web font.

### 5.6 Licensing and availability considerations

- Any recommended or selected typeface must have web-embedding rights
  verified before adoption; KBDL does not require an unverified commercial
  or proprietary typeface.
- Open-license (e.g., open-source, permissively licensed) typefaces are
  preferred as a starting recommendation specifically because their
  licensing can be verified without a separate commercial negotiation;
  this is a `Recommended` preference, not a mandate against commercial
  typefaces once licensing is confirmed.

## 6. Default Type Strategy

Status: `Approved` — this strategy (a humanist sans-serif with tabular
figures and verified open license, plus a monospace family for the Code
role) was approved by the project owner via the
[foundation decision packet](README.md#6-foundation-decision-packet); see
[KBDL-DEC-012](../decision-register.md#kbdl-dec-012--foundation-decision-packet-approved).
Provenance: `User-provided`. Validation status: `Not verified` — approving
the *strategy* does not select or verify a specific typeface family; the
final family remains `Unresolved` pending licensing verification (see §8).

A starting strategy consistent with §5: pair a humanist-leaning sans-serif
with genuine tabular-figure support and a verified open web-license for
Body/Interface/Heading/Display roles, and a well-supported monospace
family for the narrow Code role. No specific commercial family name is
selected here; selection is deferred to the
[foundation decision packet](README.md#6-foundation-decision-packet) for
project-owner review, pending licensing verification (§5.6).

## 7. Paragraph Width, Alignment, and Truncation (Approved principle)

- **Paragraph width:** Body text should be constrained to a comfortable
  reading measure; see
  [spacing-layout.md § Reading Width](spacing-layout.md#4-reading-width-approved-principle)
  for the layout-level rule this typography rule depends on.
- **Text alignment:** Left-aligned (in left-to-right contexts) by default
  for body and interface text; centered alignment is reserved for short,
  bounded Display or Showcase moments, never for multi-line body content.
- **Truncation:** Truncation (e.g., an ellipsis) is permitted only for
  Label/metadata and Numeric roles where the full value remains available
  on request (e.g., via a tooltip or detail view) — Body and Heading
  content must not be silently truncated without an alternative path to
  the full content.

## 8. Unresolved Typography Decisions

- Final typeface family selection — `Unresolved`/`Recommended` pending
  licensing verification (§5.6).
- Exact numeric scale values (in rem/px) — `Unresolved`, deferred until a
  scale is approved and an implementation unit convention is chosen.
- Variable-font adoption — `Unresolved`, depends on the eventual typeface
  choice.
