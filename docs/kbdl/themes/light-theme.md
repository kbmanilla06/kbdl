# KBDL Themes — Light Theme

Lifecycle status: `Recommended` — this exact mapping requires project-
owner approval; see
[themes/README.md § Theme Decision Packet](README.md#10-theme-decision-packet).
Provenance: `Assumed`. Validation status: `Verified` for every contrast
pair shown below (see [validation.md](validation.md) for the calculation
method and full output); `Not verified` for suitability beyond the
tested pairs. All values used are already-`Approved` KBDL-003 foundation
colors except the status-family values, which remain `Recommended` (see
[adaptation.md §5](adaptation.md#5-status-family-theme-behavior)).

Return to the [themes index](README.md) · [specification index](../README.md).

This document maps every semantic role in
[semantic-roles.md](semantic-roles.md) to a specific foundation color for
light mode. The light theme is designed to feel calm and precise:
readable surface separation without excessive pure-white layering,
selective accent use, and depth that reads primarily through spacing and
border rather than heavy shadow.

---

## Design Strategy

- **Clear, calm canvas:** `neutral-10` (not pure white) as the page
  background, reserving `neutral-0` for content surfaces — this avoids a
  page that is one undifferentiated white field.
- **Elevation through border + shadow, not background tint:** Raised,
  Floating, Modal, and Temporary-overlay surfaces all use `neutral-0`;
  their elevation is communicated by the approved shadow/border logic in
  [foundations/shape-depth.md §3](../foundations/shape-depth.md#3-elevation-and-depth),
  not by a lighter/darker background per level. This avoids "a stack of
  indistinguishable white cards" by pairing every raised surface with a
  border or shadow cue — never background alone.
- **Selective accent:** the accent role appears only on Primary action,
  Accent text/surface, Focus, and Selected roles — never as a page-wide
  background.
- **Readable secondary text:** `neutral-60` (5.59:1) is used for
  Secondary text rather than a lighter, weaker gray.

## 1. Canvas and Surfaces

| Role | Light value | Contrast context | Lifecycle | Notes |
| --- | --- | --- | --- | --- |
| Canvas | `neutral-10` `#F5F6F8` | — | Approved value, Recommended mapping | Page background. |
| Base surface | `neutral-0` `#FFFFFF` | — | Approved value, Recommended mapping | Default content surface. |
| Subtle surface | `neutral-20` `#E8EAEE` | — | Approved value, Recommended mapping | Recessed/muted areas. |
| Raised surface | `neutral-0` `#FFFFFF` + Elevation L1 shadow/border | — | Approved value, Recommended mapping | Same background as Base; elevation via shape-depth L1. |
| Floating surface | `neutral-0` `#FFFFFF` + Elevation L2 shadow/border | — | Approved value, Recommended mapping | |
| Modal surface | `neutral-0` `#FFFFFF` + Elevation L3 shadow/border | — | Approved value, Recommended mapping | Always paired with Scrim. |
| Temporary overlay | `neutral-0` `#FFFFFF` + Elevation L4 shadow/border | — | Approved value, Recommended mapping | |
| Inverse surface | `neutral-100` `#121317` | Reuses the verified "neutral-10 on neutral-100" pair (17.17:1) for any Inverse text placed on it | Approved value, Recommended mapping | Bounded local context only, see [adaptation.md §2](adaptation.md#2-local-contrast-contexts). |
| Accent surface | `accent-50` `#4A4EE0` at reduced opacity (e.g., a subtle tint) over Base surface | Underlying content must remain verified per §2 below; full-opacity use follows Primary action rules | Recommended (new — opacity value not previously approved) | Restrained-accent rule applies most strongly in Precision. |
| Scrim / backdrop | `neutral-100` `#121317` at reduced opacity (translucent) | Non-translucent fallback: solid `neutral-90` `#23252B` | Recommended (new — opacity value) | See [adaptation.md §3](adaptation.md#3-transparency-and-glass-like-effects). |
| Disabled surface | `neutral-20` `#E8EAEE` | Exempt (disabled) | Approved value, Recommended mapping | Paired with Disabled text/border, never alone. |

## 2. Text and Content

Contrast pairs computed with the WCAG 2.x relative-luminance formula; see
[validation.md](validation.md) for the method and complete output.

| Role | Light value | Paired surface | Ratio | Threshold | Result |
| --- | --- | --- | --- | --- | --- |
| Primary text | `neutral-90` `#23252B` | Base (`neutral-0`) | 15.32:1 | 4.5:1 | Passes, large margin |
| Primary text (on Canvas) | `neutral-90` `#23252B` | Canvas (`neutral-10`) | 14.17:1 | 4.5:1 | Passes, large margin |
| Secondary text | `neutral-60` `#636872` | Base (`neutral-0`) | 5.59:1 | 4.5:1 | Passes |
| Secondary text (on Canvas) | `neutral-60` `#636872` | Canvas (`neutral-10`) | 5.17:1 | 4.5:1 | Passes |
| Tertiary / metadata text | `neutral-50` `#8A8F99` | Base (`neutral-0`) | 3.25:1 | 3:1 (large text/UI only) | Passes for large text only — **must not** be used for normal-sized body text |
| Disabled text | `neutral-50` `#8A8F99` | Disabled surface | Exempt | Exempt | Disabled content is exempt from WCAG contrast requirements |
| Inverse text | `neutral-10` `#F5F6F8` | Inverse surface (`neutral-100`) | 17.17:1 | 4.5:1 | Passes, large margin |
| Interactive text | `accent-50` `#4A4EE0` | Base (`neutral-0`) | 6.07:1 | 4.5:1 | Passes |
| Accent text | `accent-50` `#4A4EE0` | Base (`neutral-0`) | 6.07:1 | 4.5:1 | Passes (same value as Interactive text) |
| Link text | `accent-50` `#4A4EE0` + underline | Base (`neutral-0`) | 6.07:1 | 4.5:1 | Passes; underline required, color is not the sole cue |
| Muted metadata | `neutral-60` `#636872` | Base (`neutral-0`) | 5.59:1 | 4.5:1 | Passes (same value as Secondary text, used for normal-size metadata) |
| Placeholder text | `neutral-60` `#636872` | Base (`neutral-0`) | 5.59:1 | 4.5:1 | Passes; exceeds the WCAG minimum expectation as a safety margin |
| Selection text | `neutral-90` `#23252B` | Selection background | See Selection background row | — | Kept at Primary-text value since the selection tint is light |
| Selection background | `accent-50` `#4A4EE0` at ~15% opacity over Base | Selection text (`neutral-90`) | Not verified | 4.5:1 | **Not verified** — requires re-calculation once an exact opacity is approved (see [validation.md § Items Not Verified](validation.md#5-items-not-verified)) |

## 3. Borders and Focus

| Role | Light value | Paired surface | Ratio | Threshold | Result |
| --- | --- | --- | --- | --- | --- |
| Subtle border | `neutral-20` `#E8EAEE` | Base (`neutral-0`) | 1.20:1 | Exempt (decorative) | Decorative use only |
| Default border | `neutral-30` `#D3D6DC` | Base (`neutral-0`) | 1.46:1 | Exempt when paired with another boundary cue; 3:1 required if used alone | **Must** pair with a non-border cue (fill or label) — does not independently meet 3:1 |
| Strong border | `neutral-70` `#52565F` | Base (`neutral-0`) | 7.36:1 | 3:1 | Passes, may be used as a sole essential-boundary cue |
| Interactive border | `neutral-70` `#52565F` (resting) | Base (`neutral-0`) | 7.36:1 | 3:1 | Passes — used for essential control boundaries (e.g., unfilled inputs) |
| Selected border | `accent-50` `#4A4EE0` | Base (`neutral-0`) | 6.07:1 | 3:1 | Passes, large margin |
| Disabled border | `neutral-20` `#E8EAEE` | Disabled surface | Exempt | Exempt | Disabled content is exempt |
| Status border | Per status family, see [adaptation.md §5](adaptation.md#5-status-family-theme-behavior) | — | See status table | 3:1 | All four status hues pass 3:1 (they already pass the stricter 4.5:1 text threshold) |
| Focus indicator | `accent-50` `#4A4EE0` | Every approved surface (Base, Canvas, Subtle, Raised, etc.) | 6.07:1 (vs. Base); ≥4.5:1 against all lighter surfaces tested | 3:1 | Passes against every surface tested |
| Focus offset / separation | Base surface color (structural gap, no new value) | — | Not applicable | Not applicable | Prevents the focus ring merging with adjacent borders |

## 4. Actions and Interaction

| Role | Light value | Paired content | Ratio | Threshold | Result |
| --- | --- | --- | --- | --- | --- |
| Primary action background / content | Background `accent-50` `#4A4EE0`; content `neutral-10` `#F5F6F8` | — | 5.62:1 | 4.5:1 | Passes |
| Secondary action background / content | Background `neutral-0` `#FFFFFF` + `neutral-70` border; content `neutral-90` `#23252B` | — | 15.32:1 (content/background) | 4.5:1 | Passes |
| Quiet action content | `accent-50` `#4A4EE0` on Base, no fill | Base (`neutral-0`) | 6.07:1 | 4.5:1 | Passes (same value as Accent text) |
| Hover emphasis | Base surface + `neutral-20` overlay (or Subtle surface value) | — | Not applicable (state-existence) | — | Perceivable background shift; not the sole cue on touch |
| Active emphasis | Base surface + `neutral-30` overlay | — | Not applicable | — | Distinguishable from Hover by deeper shift |
| Selected emphasis | Accent surface tint + Selected border | — | Not applicable | — | Never color alone (border + tint together) |
| Disabled emphasis | Disabled surface + Disabled text/border | Exempt | Exempt | — | |
| Drag or drop target | `accent-50` dashed border at 3:1 | Base (`neutral-0`) | 6.07:1 | 3:1 | Passes |
| Keyboard focus | Alias of Focus indicator (§3) | — | 6.07:1 | 3:1 | Same role, restated per §1.4 of semantic-roles.md |
| Text-link states (visited/hover/active) | Visited: `accent-50` unchanged hue, reduced emphasis via reduced underline weight; Hover: `accent-50` + stronger underline; Active: `accent-50` + Active emphasis background | Base (`neutral-0`) | 6.07:1 for all states | 4.5:1 | Passes; state changes are non-color (underline weight / background) |

## 5. Status Families

Full status-family rationale, dark-mode variants, and all six sub-roles
per family are defined in
[adaptation.md §5](adaptation.md#5-status-family-theme-behavior). This
section states only the light-mode values used here, all `Recommended`
pending approval:

| Family | Text/Icon/Border | Subtle surface | Strong surface | On-strong-surface content |
| --- | --- | --- | --- | --- |
| Informational | `#2F6FED` (4.55:1 on Base) | `neutral-20` (3.78:1 — **fails 4.5:1; large text/icon only on this surface**, see [adaptation.md §5](adaptation.md#5-status-family-theme-behavior)) | `#2F6FED` | `neutral-10` (4.21:1 — **large text/icon only**, see [adaptation.md §5](adaptation.md#5-status-family-theme-behavior)) |
| Positive | `#146B3A` (6.57:1 on Base) | `neutral-20` (5.46:1) | `#146B3A` | `neutral-10` (6.08:1) |
| Caution | `#8A5A00` (5.93:1 on Base) | `neutral-20` (4.92:1) | `#8A5A00` | `neutral-10` (5.48:1) |
| Critical | `#B3261E` (6.54:1 on Base) | `neutral-20` (5.43:1) | `#B3261E` | `neutral-10` (6.04:1) |
| Neutral status | Aliases Primary/Secondary text, Default/Strong border, Subtle surface (§1–§3) | — | — | — |

## 6. Media and Decorative Context

| Role | Light value | Notes |
| --- | --- | --- |
| Media overlay | `neutral-100` at graduated opacity (darkest near text) | Worst-case contrast must be verified per actual image, see [adaptation.md §3](adaptation.md#3-transparency-and-glass-like-effects). |
| Media caption | `neutral-10` text on a `neutral-100` at ~70% opacity caption band | 17.17:1 base-pair reused; opacity re-verified per [validation.md](validation.md). |
| Decorative accent | `accent-30` or `accent-50` at reduced opacity | Exempt (decorative); never resembles a control. |
| Gradient start / end | `accent-50` → `accent-30` | See [adaptation.md §4](adaptation.md#4-gradient-strategy) for full rules; text-over-gradient must use worst-case (lightest) stop for contrast testing. |
| Data-display foreground | Reuses Accent + Status hues as a categorical set (deferred full palette) | Full chart-palette system deferred to a later module. |
| Data-display grid / guide | `neutral-20` `#E8EAEE` | 1.20:1 — decorative/structural only, never the sole way to read a value. |
| Data-display emphasis | `accent-50` `#4A4EE0` + direct label | 6.07:1 if labeled with text. |

## 7. Unresolved Light-Theme Mappings

- Exact Accent-surface and Scrim opacity values — `Recommended` but
  `Not verified`; final opacity must be re-tested once chosen (see
  [validation.md § Items Not Verified](validation.md#5-items-not-verified)).
- Selection background opacity — `Not verified`, same reason.
- Full data-display categorical palette — `Unresolved`, deferred.
