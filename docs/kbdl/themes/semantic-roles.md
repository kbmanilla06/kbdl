# KBDL Themes — Semantic Role Inventory

Lifecycle status: `Approved` for the role inventory and parity rules
(architecture). Provenance: `Confirmed`, extending
[foundations/color.md §2](../foundations/color.md#2-color-role-architecture-approved).
Validation status: `Verified` for the parity matrix in §2 (every role
confirmed present in both modes); `Not verified` for exact per-role
mapping suitability beyond the tested pairs in
[light-theme.md](light-theme.md) and [dark-theme.md](dark-theme.md).

Return to the [themes index](README.md) · [specification index](../README.md).

This document defines every semantic role KBDL themes must map, and the
parity rules that keep light and dark modes equivalent in meaning. It
does not assign exact foundation-color values — those are in
[light-theme.md](light-theme.md) and [dark-theme.md](dark-theme.md).

---

## 1. Semantic Role Inventory

Each table below lists roles in one category. Shared, category-wide
rules are stated once above each table rather than repeated per row, to
keep the tables narrow and readable per the "avoid overly wide tables"
requirement. Exact values are in
[light-theme.md](light-theme.md)/[dark-theme.md](dark-theme.md); this
table states purpose and validation intent only.

### 1.1 Canvas and Surfaces

**Category-wide rules:** every surface role traces to the approved
five-level elevation scale
([foundations/shape-depth.md §3.2](../foundations/shape-depth.md#32-default-semantic-elevation-scale)).
Surfaces must remain understandable without shadow or blur (a border or
spacing cue must also be present). Profile considerations: Showcase may
use surfaces with greater visual drama (stronger shadow/border emphasis);
Precision favors flat, low-noise surfaces; Flow favors calm, consistent
surfaces. Validation method for all rows: contrast/legibility review
against the content each surface hosts, per [validation.md](validation.md).

| Role | Purpose | Related foundation role | Prohibited use |
| --- | --- | --- | --- |
| Canvas | The page/screen's outermost background. | Neutral scale | Never used for a component background directly above content. |
| Base surface | The default resting surface for primary content (Elevation 0–1 boundary). | Neutral scale | Must not be indistinguishable from Canvas without a border/spacing cue. |
| Subtle surface | A recessed or muted surface (e.g., a disabled well, a quiet grouping). | Neutral scale | Must not be used where content needs full emphasis. |
| Raised surface | Elevation 1 — cards, panels. | Elevation scale L1 | Must not stack more than one visually ambiguous raised layer without separation. |
| Floating surface | Elevation 2 — dropdowns, popovers, tooltips. | Elevation scale L2 | Must not persist as permanent page content. |
| Modal surface | Elevation 3 — dialogs, sheets. | Elevation scale L3 | Must always pair with a scrim (see Scrim role) and trap focus. |
| Temporary overlay | Elevation 4 — toasts, transient notifications. | Elevation scale L4 | Must not block the primary task longer than necessary. |
| Inverse surface | A surface using the opposite luminance direction of the active mode, for a bounded local context. | Neutral scale | Must not be applied to more than a bounded region (see [adaptation.md §2](adaptation.md#2-local-contrast-contexts)). |
| Accent surface | A surface tinted with the accent role, for brand emphasis (e.g., a selected nav item). | Accent family | Must not be used for large content regions in Precision (restrained-accent rule). |
| Scrim / backdrop | The dimming layer behind a modal or floating surface. | Neutral scale (translucent) | Must not be used without verifying the content behind it does not need to remain readable. |
| Disabled surface | A surface indicating an inactive component. | Neutral scale | Must not be the only indicator of disabled state (label/cursor must also indicate it). |

### 1.2 Text and Content

**Category-wide rules:** every text role that carries required
information must meet the applicable WCAG 2.2 AA text-contrast
threshold (4.5:1 normal text, 3:1 large text) against its stated
surface, except roles explicitly exempted below (disabled, placeholder
where paired with a label). Profile considerations: Precision relies
most heavily on Secondary/Tertiary and Data-display roles; Showcase uses
Primary/Accent text more expressively; Flow keeps text roles simple and
predictable. Validation method: WCAG relative-luminance contrast
calculation, per [validation.md](validation.md).

| Role | Purpose | Contrast requirement | Prohibited use |
| --- | --- | --- | --- |
| Primary text | Main reading and heading content. | 4.5:1 normal / 3:1 large | Must not be used at a contrast below threshold in any surface it appears on. |
| Secondary text | Supporting, less prominent content. | 4.5:1 normal | Must not be used for content the user must read to complete a required task, unless it independently meets threshold. |
| Tertiary / metadata text | Least prominent supporting text (timestamps, counts). | 3:1 large-text/UI only — **not for normal-sized body text** | Must not carry required information at normal size without pairing with a passing role. |
| Disabled text | Text on an inactive control. | Exempt (WCAG does not require contrast for disabled content) | Must not be used for active, actionable text. |
| Inverse text | Text on an Inverse surface. | 4.5:1 normal against the Inverse surface value | Must not be used on a non-inverse surface. |
| Interactive text | Text that is itself interactive (beyond links, e.g. a text button). | 4.5:1 normal + 3:1 non-text state boundary | Must always have a visible non-color state change on hover/focus. |
| Accent text | Text using the accent role for brand emphasis, not interaction. | 4.5:1 normal | Must not be the only way an interactive element is identified as interactive. |
| Link text | Text that navigates. | 4.5:1 normal + must be distinguishable from surrounding text by more than color (underline or weight) | Must not rely on color alone to indicate it is a link. |
| Muted metadata | Secondary metadata requiring normal-size legibility (e.g., a byline). | 4.5:1 normal | Must not use the Tertiary/metadata role's restricted value. |
| Placeholder text | Input-field placeholder content. | 4.5:1 normal recommended (exceeds the WCAG minimum expectation for placeholders as a safety margin) | Must not be the only labeling mechanism for a field — a real label must also exist. |
| Selection text / background | Text and background shown when content is selected (e.g., text highlight). | 4.5:1 between the pair | Must not obscure the selected content's meaning. |

### 1.3 Borders and Focus

**Category-wide rules:** a border that is the *sole* means of
identifying an essential interactive boundary must meet the WCAG 1.4.11
non-text threshold (3:1) against its adjacent surface; a purely
decorative/structural divider is exempt. Where a role's approved-value
mapping does not reach 3:1, it is restricted to decorative use paired
with another sufficient boundary cue (fill, spacing, label) — this
restriction is stated explicitly per mapping in
[light-theme.md](light-theme.md)/[dark-theme.md](dark-theme.md), never
silently assumed. Profile considerations: Precision relies most on
border-based separation (low decorative depth); Showcase may rely more
on spacing/surface separation than borders.

| Role | Purpose | Contrast requirement | Prohibited use |
| --- | --- | --- | --- |
| Subtle border | Decorative separation between related items. | Exempt (decorative) | Must not be relied on as the sole indicator of an essential boundary. |
| Default border | Structural, non-essential boundary (paired with other cues where needed). | 3:1 where used as the sole essential-boundary cue; otherwise exempt | Must state explicitly which case applies per mapping. |
| Strong border | Boundary between clearly distinct sections. | 3:1 | Must not be used at a contrast below 3:1. |
| Interactive border | Resting boundary of an interactive control (input, select). | 3:1 if sole cue; must pair with a non-border cue otherwise | Must not disappear on any interaction state. |
| Selected border | Indicates the selected state of a control or item. | 3:1 | Must always pair with a non-border selected cue (icon, background). |
| Disabled border | Boundary of an inactive control. | Exempt (disabled) | Must not be used for an active control. |
| Status border | Reinforces a status role (see §1.4). | 3:1 | Must always pair with a status icon or label. |
| Focus indicator | Shows current keyboard focus. | 3:1 against every adjacent approved surface | Must never be removed, hidden, or replaced by color alone. |
| Focus offset / separation | The gap or halo separating a focus indicator from adjacent content. | Not applicable (structural) | Must not let the focus indicator visually merge with an adjacent element's border. |

### 1.4 Actions and Interaction

**Category-wide rules:** these are semantic interaction roles, not
component specifications — exact anatomy (button shape, padding) is
deferred to later component modules. Every "content" sub-role must meet
4.5:1 against its paired background. State changes (hover/active/
selected/disabled) must always be perceivable through more than color.

| Role | Purpose | Contrast requirement | Prohibited use |
| --- | --- | --- | --- |
| Primary action background / content | The most prominent actionable surface and its text/icon. | 4.5:1 (background/content pair) | Must not appear more than once as the singular primary action within one view. |
| Secondary action background / content | A less prominent but still direct action. | 4.5:1 | Must not visually outweigh the Primary action. |
| Quiet action content | A minimal-emphasis action (e.g., a text-only "Cancel"). | 4.5:1 against its surface | Must not be used for a destructive or primary action. |
| Hover emphasis | Perceivable change on pointer hover. | Not applicable (state-existence requirement) | Must not be the only state cue relied on for touch (no hover) contexts. |
| Active emphasis | Perceivable change while a control is being activated (pressed). | Not applicable | Must not be indistinguishable from Hover emphasis. |
| Selected emphasis | Perceivable change indicating a selected item. | Not applicable | Must not rely on color alone (see Selected border). |
| Disabled emphasis | Perceivable reduction indicating an inactive control. | Exempt | Must not be confusable with a low-emphasis but still-active control. |
| Drag or drop target | Perceivable change indicating a valid drop target. | 3:1 non-text | Must not appear identical to a hover state a user could confuse with drop validity. |
| Keyboard focus | Synonym reference to Focus indicator (§1.3) for interactive elements specifically. | See Focus indicator | Must not diverge from the Focus indicator role. |
| Text-link states (visited/hover/active) | Perceivable changes across a link's lifecycle. | 4.5:1 for each state's text | Must not rely on color alone to distinguish states. |

### 1.5 Status

**Category-wide rules:** the four status roles (Informational, Positive,
Caution, Critical) plus Neutral status are semantically fixed per
[foundations/color.md §2.4](../foundations/color.md#24-status-roles);
their specific hue values remain `Recommended` (see
[adaptation.md §5](adaptation.md#5-status-family-theme-behavior)). Every
status role requires: Text, Icon, Border, Subtle surface, Strong surface
(emphasis fill), and On-strong-surface content. A status **must not** be
conveyed by color alone — an icon or label is always required. Caution
and Positive must remain distinguishable from each other in both hue and
luminance; Critical must remain distinguishable from the accent role.

| Sub-role | Purpose | Contrast requirement |
| --- | --- | --- |
| Text | Status-colored text (e.g., an inline error message). | 4.5:1 normal |
| Icon | Status-colored icon, always paired with text or an accessible label. | 3:1 (non-text) |
| Border | Status-colored border, always paired with icon/label. | 3:1 |
| Subtle surface | A tinted background indicating status without full emphasis. | Text/icon on it must still meet 4.5:1/3:1 |
| Strong surface (emphasis) | A solid status-colored fill (e.g., a badge). | See On-strong-surface content |
| On-strong-surface content | Text/icon placed on the Strong surface fill. | 4.5:1 normal (restricted to large-text/icon if this is not met — stated explicitly per status in the mapping) |

Neutral status (a fifth, non-alarm state — e.g., "not started") uses the
Neutral-family text/border/surface roles from §1.1–§1.3, not a new hue.

### 1.6 Media and Decorative Context

**Category-wide rules:** these roles support content; they are never
required to convey information alone. Chart/data-display palettes beyond
the general roles below remain deferred to a future module unless
already approved.

| Role | Purpose | Contrast requirement | Prohibited use |
| --- | --- | --- | --- |
| Media overlay | A scrim or gradient over media supporting text legibility. | Text on it must meet 4.5:1 at every point (worst-case) | Must not be relied on without verifying the darkest/lightest expected media content. |
| Media caption | Caption text for media. | 4.5:1 against its own background (not the raw media) | Must not be placed directly on unverified media without a caption background. |
| Decorative accent | Purely ornamental use of the accent role. | Exempt (decorative) | Must never resemble an interactive control. |
| Gradient start / end roles | The two anchor colors of an approved gradient (see [adaptation.md §4](adaptation.md#4-gradient-strategy)). | Worst-case text-over-gradient must meet 4.5:1 | Must not convey status meaning alone. |
| Data-display foreground | A data series' primary color. | 3:1 against its background; must be color-blind-safe in combination with other series | Must not reuse a Status role hue for a non-status series. |
| Data-display grid / guide | Axis lines, gridlines. | 3:1 non-text where essential to reading the chart | Must not be so prominent it competes with the data itself. |
| Data-display emphasis | A highlighted data point or series. | 4.5:1 if labeled with text | Must not be the only way a highlighted series is identified (a label or legend must also exist). |

## 2. Semantic Parity

Light and dark themes use the **same** semantic-role inventory from §1.
The following rules govern parity between the two modes:

- **Equivalent meaning:** a role means the same thing in both modes
  (e.g., "Critical text" always means a blocking error, in both light
  and dark).
- **Equivalent interaction hierarchy:** Primary action remains the most
  prominent actionable element in both modes.
- **Equivalent status meaning:** the four status roles keep the same
  relative severity ordering in both modes.
- **Equivalent focus visibility:** the Focus indicator meets its
  contrast requirement against every surface it can appear on, in both
  modes.
- **Equivalent content priority:** the same content is Primary/
  Secondary/Tertiary in both modes — a role never gets "promoted" or
  "demoted" between modes.
- **Equivalent destructive-action prominence:** a destructive action
  (mapped via Critical + Primary action roles) remains equally
  prominent in both modes.
- **Equivalent selected/disabled-state meaning:** these states are
  perceivable through the same combination of role types (never color
  alone) in both modes.
- **Equivalent surface and elevation relationships:** the five
  elevation levels retain their relative ordering and separation logic
  in both modes, even though the exact technique differs (see
  [dark-theme.md §1](dark-theme.md#1-elevation-strategy) for why dark
  mode lightens surfaces with elevation while light mode uses shadow/
  border).

A role **must not** disappear merely because one mode makes it harder to
style. Where a role is genuinely not applicable in one mode, the reason
is documented in the parity matrix below rather than the role being
silently omitted.

### Parity Matrix (Corrected under KBDL-004-R1)

Every role in §1 is confirmed present in both modes. "Mapped" means a
specific foundation-color value is assigned in
[light-theme.md](light-theme.md)/[dark-theme.md](dark-theme.md); no role
in this inventory is marked "not applicable" in either mode.

**Counting model** (this is the only model used — no double-counting):
4 colored status families (Informational, Positive, Caution, Critical),
each with 6 sub-roles (Text, Icon, Border, Subtle surface, Strong
surface, On-strong-surface content) = **4 × 6 = 24** distinct status
roles. Neutral status contributes **0** additional distinct roles — it
is implemented entirely through documented aliases to existing Primary/
Secondary text, Default/Strong border, and Subtle surface roles (see the
"Neutral status" row in
[light-theme.md §5](light-theme.md#5-status-families) and
[dark-theme.md §6](dark-theme.md#6-status-families)). The previous
version of this table incorrectly labeled this row "×5 sub-roles ×5
families" while its own total column already used the correct 4×6
figure — that label, not the total, was the error; it is corrected here.

**Alias model (KBDL-004-R2, the only model used):** a role counts as a
"distinct role" if it is separately listed in §1's inventory, regardless
of whether its assigned *value* happens to be reused from another role.
A role counts as an "alias" only when it is **not** separately
implemented at all — its inventory entry is purely a pointer to another
role's definition, contributing 0 to the distinct-role count. By this
test: **Keyboard focus** is an alias (its inventory entry, §1.4, is
literally "Synonym reference to Focus indicator"; it adds no new
definition). **Neutral status** is an alias (§1.5 states it "uses the
Neutral-family text/border/surface roles... not a new hue," and it has
no dedicated sub-role table of its own). **Text-link states** is *not*
an alias — it has its own purpose (distinct visited/hover/active
sub-states across a link's lifecycle) and its own inventory entry with
its own contrast requirement; that its light-mode *value* reuses
Interactive/Link text's color is ordinary value reuse, the same pattern
used by Muted metadata (reusing Secondary text's value) and Selection
text (reusing Primary text's value) — neither of which is called an
alias either. Total aliases under this model: **2**.

| Category | Distinct roles | Light-mapped | Dark-mapped | Aliases (not counted as new roles) |
| --- | --- | --- | --- | --- |
| Canvas and Surfaces | 11 | 11 | 11 | 0 |
| Text and Content | 11 | 11 | 11 | 0 |
| Borders and Focus | 9 | 9 | 9 | 0 |
| Actions and Interaction | 10 | 10 | 10 | 1 (Keyboard focus → Focus indicator; Text-link states remains a distinct role using value reuse, not an alias) |
| Status — 4 families × 6 sub-roles | 24 | 24 | 24 | 0 |
| Status — Neutral status | 0 | 0 (via alias) | 0 (via alias) | 1 (→ Primary/Secondary text, Default/Strong border, Subtle surface) |
| Media and Decorative | 7 | 7 | 7 | 0 |
| **Total unique semantic roles** | **72** | — | — | — |
| **Total light mappings (including aliases)** | — | **72** | — | — |
| **Total dark mappings (including aliases)** | — | — | **72** | — |
| **Total role-level aliases** | — | — | — | **2** |

**Unresolved or missing mappings:** none — every one of the 72 unique
roles has either a direct value or a named alias in both
[light-theme.md](light-theme.md) and [dark-theme.md](dark-theme.md).

This matrix was produced by a direct count of every row in §1.1–§1.6
against the actual mapping tables in
[light-theme.md](light-theme.md) and [dark-theme.md](dark-theme.md) —
not merely re-asserted from the prior report — including a corrected
count that found and fixed a table-formatting defect in
[light-theme.md §5](light-theme.md#5-status-families) (the "Neutral
status" row had been separated from its table by an inserted paragraph,
silently breaking Markdown table rendering; it is now restored as the
fifth row of that table). See
[validation.md § Parity Check](validation.md#2-parity-check-revalidated-under-kbdl-004-r1) for the
verification procedure and result.
