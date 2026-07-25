# KBDL Themes — Dark Theme

Lifecycle status: `Recommended` — this exact mapping requires project-
owner approval; see
[themes/README.md § Theme Decision Packet](README.md#10-theme-decision-packet).
Provenance: `Assumed`. Validation status: `Verified` for every contrast
pair shown below (see [validation.md](validation.md)); `Not verified`
for suitability beyond the tested pairs. All values used are already-
`Approved` KBDL-003 foundation colors except the status-family dark
variants, which are newly proposed and remain `Recommended` (see
[adaptation.md §5](adaptation.md#5-status-family-theme-behavior)).

Return to the [themes index](README.md) · [specification index](../README.md).

This document maps every semantic role in
[semantic-roles.md](semantic-roles.md) to a specific foundation color for
dark mode. **The dark theme is designed independently, not by inverting
the light theme.** Several roles intentionally use a *different* neutral
step than their light-mode counterpart, because contrast behaves
asymmetrically between light and dark backgrounds (a gray that reads
clearly on white does not necessarily read clearly on near-black, and
vice versa) — see §1 Design Strategy for the specific example this
produced.

---

## 1. Elevation Strategy

Dark mode uses a **two-step lightening strategy** for elevation,
combined with borders — not shadow alone (shadow is barely visible on a
dark background) and not lightening alone (a 1.21:1 step between
`neutral-100` and `neutral-90` is too subtle to read as separation by
itself):

- Canvas and Base surface: `neutral-100` `#121317` (darkest).
- Raised, Floating, Modal, and Temporary-overlay surfaces: `neutral-90`
  `#23252B` (one step lighter), **always paired with a border** (see §3)
  since the background-luminance step alone (1.21:1) is insufficient
  separation on its own.

This satisfies "dark-mode elevation must not depend only on lighter
backgrounds" — the border is mandatory, not optional, in dark mode.

## Design Strategy — Why Some Roles Use a Different Step Than Light Mode

The clearest example: light-mode Secondary text uses `neutral-60`
(5.59:1 against `neutral-0`), but `neutral-60` against `neutral-100`
computes to only **3.32:1** — it fails the 4.5:1 normal-text threshold in
dark mode. Dark-mode Secondary text instead uses `neutral-50`, which
computes to **5.72:1** against `neutral-100`. This is not an error or an
inconsistent choice: on a dark background, a *lighter* gray reads more
clearly, while on a light background a *darker* gray reads more clearly.
Mechanically inverting the light theme's exact values (rather than
independently re-selecting a per-mode value for each role, as done here)
would have shipped a Secondary-text failure in dark mode. All values
below were independently verified against their dark-mode surface, not
assumed from the light-mode result.

## 2. Canvas and Surfaces

| Role | Dark value | Contrast context | Lifecycle | Notes |
| --- | --- | --- | --- | --- |
| Canvas | `neutral-100` `#121317` | — | Approved value, Recommended mapping | Darkest reference. |
| Base surface | `neutral-100` `#121317` | — | Approved value, Recommended mapping | Same as Canvas; content surfaces are distinguished by border, not tint, at this level. |
| Subtle surface | `neutral-90` `#23252B` | — | Approved value, Recommended mapping | Recessed/muted areas — one step lighter than Canvas. |
| Raised surface | `neutral-90` `#23252B` + border (§3) | 1.21:1 background step (insufficient alone) | Approved value, Recommended mapping | Border is mandatory, not optional (see §1). |
| Floating surface | `neutral-90` `#23252B` + border + Elevation L2 shadow (subtle) | — | Approved value, Recommended mapping | |
| Modal surface | `neutral-90` `#23252B` + border + scrim | — | Approved value, Recommended mapping | Always paired with Scrim. |
| Temporary overlay | `neutral-90` `#23252B` + border | — | Approved value, Recommended mapping | |
| Inverse surface | `neutral-0` `#FFFFFF` | Reuses the verified "neutral-90 on neutral-0" family for Inverse text on it (15.32:1, via the already-verified neutral-90/neutral-0 text pair) | Approved value, Recommended mapping | Bounded local context only. |
| Accent surface | `accent-30` `#A9ACFF` at reduced opacity over Base | Underlying content re-verified per §3 below | Recommended (new — opacity value) | Restrained in Precision. |
| Scrim / backdrop | `neutral-0` `#FFFFFF` at reduced opacity is **not** used in dark mode (would create a jarring bright scrim); dark mode uses `neutral-100` at increased opacity instead, since the modal surface (`neutral-90`) is already lighter than the scrim | Non-translucent fallback: solid `neutral-100` | Recommended (new — opacity value) | See [adaptation.md §3](adaptation.md#3-transparency-and-glass-like-effects). |
| Disabled surface | `neutral-90` `#23252B` | Exempt (disabled) | Approved value, Recommended mapping | |

## 3. Text and Content

| Role | Dark value | Paired surface | Ratio | Threshold | Result |
| --- | --- | --- | --- | --- | --- |
| Primary text | `neutral-10` `#F5F6F8` | Canvas/Base (`neutral-100`) | 17.17:1 | 4.5:1 | Passes, large margin |
| Primary text (on raised surfaces) | `neutral-10` `#F5F6F8` | Raised (`neutral-90`) | 14.17:1 | 4.5:1 | Passes, large margin |
| Secondary text | `neutral-50` `#8A8F99` | Canvas/Base (`neutral-100`) | 5.72:1 | 4.5:1 | Passes — **note: different step than light mode's `neutral-60`; see Design Strategy above** |
| Tertiary / metadata text | `neutral-60` `#636872` | Canvas/Base (`neutral-100`) | 3.32:1 | 3:1 (large text/UI only) | Passes for large text only — **not for normal-sized body text**, mirroring the light-mode restriction on the analogous step |
| Disabled text | `neutral-60` `#636872` | Disabled surface | Exempt | Exempt | Disabled content is exempt |
| Inverse text | `neutral-90` `#23252B` | Inverse surface (`neutral-0`) | 15.32:1 | 4.5:1 | Passes, large margin |
| Interactive text | `accent-30` `#A9ACFF` | Canvas/Base (`neutral-100`) | 8.87:1 | 4.5:1 | Passes — **note: `accent-30`, not `accent-50` — `accent-50` on `neutral-100` computes to only 3.06:1 and fails 4.5:1** |
| Accent text | `accent-30` `#A9ACFF` | Canvas/Base (`neutral-100`) | 8.87:1 | 4.5:1 | Passes (same value as Interactive text) |
| Link text | `accent-30` `#A9ACFF` + underline | Canvas/Base (`neutral-100`) | 8.87:1 | 4.5:1 | Passes; underline required |
| Muted metadata | `neutral-50` `#8A8F99` | Canvas/Base (`neutral-100`) | 5.72:1 | 4.5:1 | Passes (same value as Secondary text) |
| Placeholder text | `neutral-50` `#8A8F99` | Canvas/Base (`neutral-100`) | 5.72:1 | 4.5:1 | Passes |
| Selection text | `neutral-10` `#F5F6F8` | Selection background | See row below | — | |
| Selection background | `accent-30` `#A9ACFF` at ~15% opacity over Canvas | Selection text (`neutral-10`) | Not verified | 4.5:1 | **Not verified** — same restriction as light mode |

## 4. Borders and Focus

| Role | Dark value | Paired surface | Ratio | Threshold | Result |
| --- | --- | --- | --- | --- | --- |
| Subtle border | `neutral-70` `#52565F` | Raised surface (`neutral-90`) | 2.08:1 | Exempt (decorative) | Decorative use only |
| Default border | `neutral-70` `#52565F` | Raised surface (`neutral-90`) | 2.08:1 | Exempt when paired with another cue; 3:1 if used alone | Must pair with a non-border cue, same restriction pattern as light mode |
| Strong border | `neutral-50` `#8A8F99` | Raised surface (`neutral-90`) | 4.72:1 | 3:1 | Passes, may be used as sole essential-boundary cue |
| Interactive border | `neutral-50` `#8A8F99` (resting) | Canvas/Base (`neutral-100`) | 5.72:1 | 3:1 | Passes |
| Selected border | `accent-30` `#A9ACFF` | Canvas/Base (`neutral-100`) | 8.87:1 | 3:1 | Passes, large margin |
| Disabled border | `neutral-90` `#23252B` | Disabled surface | Exempt | Exempt | |
| Status border | Per status family, see [adaptation.md §5](adaptation.md#5-status-family-theme-behavior) | — | See status table | 3:1 | All four dark status hues pass 3:1 (they pass the stricter 4.5:1 threshold) |
| Focus indicator | `accent-30` `#A9ACFF` | Every approved dark surface (Canvas, Base, Raised) | 8.87:1 (vs. Canvas/Base); 7.32:1 (vs. Raised) | 3:1 | Passes against every surface tested |
| Focus offset / separation | Base/Raised surface color (structural gap, no new value) | — | Not applicable | Not applicable | Same role as light mode, mode-appropriate background |

## 5. Actions and Interaction

| Role | Dark value | Paired content | Ratio | Threshold | Result |
| --- | --- | --- | --- | --- | --- |
| Primary action background / content | Background `accent-50` `#4A4EE0` (same hue as light mode — self-contained pair, not surface-dependent); content `neutral-10` `#F5F6F8` | — | 5.62:1 | 4.5:1 | Passes — kept identical to light mode intentionally, since this pairing does not depend on the page canvas and using one accent value for filled actions preserves one brand identity across modes |
| Secondary action background / content | Background `neutral-90` + `neutral-50` border; content `neutral-10` `#F5F6F8` | — | 14.17:1 (content/background) | 4.5:1 | Passes |
| Quiet action content | `accent-30` `#A9ACFF` on Canvas/Base, no fill | Canvas/Base (`neutral-100`) | 8.87:1 | 4.5:1 | Passes |
| Hover emphasis | Base/Raised surface + `neutral-70` overlay | — | Not applicable | — | Perceivable background shift |
| Active emphasis | Base/Raised surface + `neutral-50` overlay | — | Not applicable | — | Distinguishable from Hover |
| Selected emphasis | Accent surface tint + Selected border | — | Not applicable | — | Never color alone |
| Disabled emphasis | Disabled surface + Disabled text/border | Exempt | Exempt | — | |
| Drag or drop target | `accent-30` dashed border at 3:1 | Canvas/Base (`neutral-100`) | 8.87:1 | 3:1 | Passes |
| Keyboard focus | Alias of Focus indicator (§4) | — | 8.87:1 | 3:1 | Same role |
| Text-link states (visited/hover/active) | Visited: `accent-30` unchanged hue, reduced underline weight; Hover: `accent-30` + stronger underline; Active: `accent-30` + Active emphasis background | Canvas/Base (`neutral-100`) | 8.87:1 for all states | 4.5:1 | Passes; state changes are non-color |

## 6. Status Families

Full rationale and light-mode values in
[adaptation.md §5](adaptation.md#5-status-family-theme-behavior) and
[light-theme.md §5](light-theme.md#5-status-families). Dark-mode values,
all newly proposed and `Recommended`:

| Family | Text/Icon/Border | Subtle surface | Strong surface | On-strong-surface content |
| --- | --- | --- | --- | --- |
| Informational | `#7CC4FF` (9.90:1 on `neutral-100`) | `neutral-90` (8.17:1) | `#7CC4FF` | `neutral-90` (8.17:1) |
| Positive | `#6FD19A` (9.96:1 on `neutral-100`) | `neutral-90` (8.22:1) | `#6FD19A` | `neutral-90` (8.22:1) |
| Caution | `#E0A840` (8.70:1 on `neutral-100`) | `neutral-90` (7.18:1) | `#E0A840` | `neutral-90` (7.18:1) |
| Critical | `#FF8A80` (8.13:1 on `neutral-100`) | `neutral-90` (6.71:1) | `#FF8A80` | `neutral-90` (6.71:1) |
| Neutral status | Aliases Primary/Secondary text, Default/Strong border, Subtle surface (§2–§4) | — | — | — |

Dark-mode status hues are deliberately lighter tints distinct from the
light-mode hues (not a simple lightening of the same RGB values), chosen
so each remains clearly distinguishable from `accent-30` (the dark-mode
accent) — `#7CC4FF` (sky blue) versus `#A9ACFF` (indigo-violet accent)
keeps informational and brand accent from converging in hue.

## 7. Media and Decorative Context

| Role | Dark value | Notes |
| --- | --- | --- |
| Media overlay | `neutral-100` at graduated opacity | Same principle as light mode; worst-case verified per actual image. |
| Media caption | `neutral-10` text on a `neutral-100` at ~70% opacity caption band | Reuses the 17.17:1 base pair; opacity re-verified per [validation.md](validation.md). |
| Decorative accent | `accent-30` at reduced opacity | Exempt (decorative). |
| Gradient start / end | `accent-30` → `accent-50` | Reversed order from light mode's `accent-50 → accent-30`, since `accent-30` is the correctly-contrasting accent step for dark surfaces; see [adaptation.md §4](adaptation.md#4-gradient-strategy). |
| Data-display foreground | Reuses Accent + Status dark hues | Full chart-palette system deferred. |
| Data-display grid / guide | `neutral-90` `#23252B` | 1.21:1 on Canvas — decorative/structural only. |
| Data-display emphasis | `accent-30` `#A9ACFF` + direct label | 8.87:1 if labeled with text. |

## 8. Unresolved Dark-Theme Mappings

- Exact Accent-surface and Scrim opacity values — `Not verified`, same
  restriction as light mode.
- Selection background opacity — `Not verified`.
- Full data-display categorical palette — `Unresolved`, deferred.
