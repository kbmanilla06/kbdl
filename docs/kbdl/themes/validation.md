# KBDL Themes — Validation and Conformance

Lifecycle status: `Approved` for the validation methodology and
conformance criteria (architecture). Validation status of the results
recorded below: `Verified` for every contrast pair and the parity check;
`Not verified` items are listed explicitly in §5.

Return to the [themes index](README.md) · [specification index](../README.md).

This document defines how KBDL themes are validated and records the
consolidated contrast and parity evidence for
[light-theme.md](light-theme.md) and [dark-theme.md](dark-theme.md). A
passing light-theme value is never assumed to pass in dark mode — every
pair below was calculated independently per mode.

---

## 1. Theme Validation Specification

A theme (or a project theme extending it) is validated against every
item below before any pair may be marked `Verified`:

- **Semantic-role completeness** — every role in
  [semantic-roles.md §1](semantic-roles.md#1-semantic-role-inventory) has
  a mapping (see §2 Parity Check).
- **Light/dark parity** — per
  [semantic-roles.md §2](semantic-roles.md#2-semantic-parity).
- **Text contrast** — every text role meets 4.5:1 normal / 3:1 large
  against its documented surface, or carries an explicit restriction
  (see §3).
- **Essential non-text contrast** — every border/focus/status-border role
  meets 3:1 where it is the sole boundary cue, or carries an explicit
  pairing requirement.
- **Focus visibility** — the Focus indicator meets 3:1 against every
  surface it can appear on, in both modes.
- **Selected and disabled states** — perceivable through more than color,
  per [semantic-roles.md §1.3–§1.4](semantic-roles.md#13-borders-and-focus).
- **Status differentiation** — per
  [adaptation.md §5.1](adaptation.md#5-status-family-theme-behavior).
- **Surface separation** — per
  [adaptation.md § Surface and Elevation Requirements](adaptation.md#surface-and-elevation-requirements-cross-reference).
- **Translucency fallback** — per
  [adaptation.md §3.3](adaptation.md#33-validation-checklist-for-translucent-surfaces).
- **Gradient worst-case contrast** — per
  [adaptation.md §4.3](adaptation.md#43-worked-example--worst-case-contrast).
- **Media-overlay readability** — per
  [semantic-roles.md §1.6](semantic-roles.md#16-media-and-decorative-context).
- **Theme-control behavior** — per
  [themes/README.md §6](README.md#6-user-theme-controls).
- **Precedence behavior** — per
  [themes/README.md §5](README.md#5-theme-selection-precedence).
- **Persistence failure** — per
  [themes/README.md §7](README.md#7-persistence-guidance).
- **Initial-render mismatch** — per
  [adaptation.md §7.1](adaptation.md#71-requirements).
- **Profile consistency** — per
  [themes/README.md §8](README.md#8-project-profile-theme-interpretation).
- **Mobile review** — surfaces and touch targets re-checked at compact
  breakpoints (deferred to KBDL-006 for exact breakpoint values; the
  requirement to review is established here).
- **Reduced-motion behavior** — per
  [adaptation.md §7](adaptation.md#7-theme-transition-guidance).
- **High-zoom and enlarged-text review** — text roles must remain within
  contrast thresholds when the user has enlarged text or zoomed the
  page, since relative contrast ratios are zoom-independent but layout
  reflow is not; a full review is deferred to KBDL-006 but the
  requirement is established here.

## 2. Parity Check

**Method:** every role listed in
[semantic-roles.md §1](semantic-roles.md#1-semantic-role-inventory) (72
distinct roles across 6 categories) was checked against the
corresponding row in [light-theme.md](light-theme.md) and
[dark-theme.md](dark-theme.md). A role "passes" the parity check if it
appears with an assigned value (or an explicit, named alias to another
mapped role) in both files.

**Result:** all 72 roles are mapped in both modes. No role is marked
"not applicable" in either mode. See
[semantic-roles.md § Parity Matrix](semantic-roles.md#parity-matrix) for
the category-level count.

**Aliases used** (permitted per
[themes/README.md §4](README.md#4-theme-architecture)): Keyboard focus →
Focus indicator; Neutral status → existing Primary/Secondary text,
Default/Strong border, and Subtle surface roles (both modes); Selection
text → Primary text value (both modes).

## 3. Consolidated Contrast Evidence

All ratios below were computed with the WCAG 2.x relative-luminance
formula (`L = 0.2126R + 0.7152G + 0.0722B` on linearized sRGB channels;
contrast ratio `(L1 + 0.05) / (L2 + 0.05)`), using a local, dependency-
free Python script (no package was installed or added for this check).
Each pair was tested against its actually-documented surface — light-
mode pairs against light surfaces, dark-mode pairs against dark
surfaces, independently.

| Pair | Ratio | Threshold | Result |
| --- | --- | --- | --- |
| Primary text on Base (light) | 15.32:1 | 4.5:1 | Passes |
| Primary text on Canvas (light) | 14.17:1 | 4.5:1 | Passes |
| Secondary text on Base (light) | 5.59:1 | 4.5:1 | Passes |
| Secondary text on Canvas (light) | 5.17:1 | 4.5:1 | Passes |
| Tertiary/metadata on Base (light, large-text only) | 3.25:1 | 3:1 | Passes (restricted to large text/UI) |
| Inverse text on Inverse surface (light) | 17.17:1 | 4.5:1 | Passes |
| Accent/Interactive/Link/Quiet-action text on Base (light) | 6.07:1 | 4.5:1 | Passes |
| Muted metadata / Placeholder on Base (light) | 5.59:1 | 4.5:1 | Passes |
| Strong/Interactive border on Base (light) | 7.36:1 | 3:1 | Passes |
| Default border on Base (light) | 1.46:1 | 3:1 | **Fails** — restricted to decorative use paired with another boundary cue, per [semantic-roles.md §1.3](semantic-roles.md#13-borders-and-focus) |
| Selected border / Focus indicator on Base (light) | 6.07:1 | 3:1 | Passes |
| Primary action content on Primary action background | 5.62:1 | 4.5:1 | Passes (mode-independent pairing) |
| Informational text on Base (light) | 4.55:1 | 4.5:1 | Passes, narrow margin |
| Positive text on Base (light) | 6.57:1 | 4.5:1 | Passes |
| Caution text on Base (light) | 5.93:1 | 4.5:1 | Passes |
| Critical text on Base (light) | 6.54:1 | 4.5:1 | Passes |
| Informational text on Subtle surface (light) | 3.78:1 | 4.5:1 | **Fails** — restricted to large text/icon, per [adaptation.md §5.2](adaptation.md#52-two-documented-restrictions) |
| Positive text on Subtle surface (light) | 5.46:1 | 4.5:1 | Passes |
| Caution text on Subtle surface (light) | 4.92:1 | 4.5:1 | Passes |
| Critical text on Subtle surface (light) | 5.43:1 | 4.5:1 | Passes |
| Informational on-strong-surface content (light) | 4.21:1 | 4.5:1 | **Fails** normal-text; passes 3:1 large-text/icon — restricted, per [adaptation.md §5.2](adaptation.md#52-two-documented-restrictions) |
| Positive on-strong-surface content (light) | 6.08:1 | 4.5:1 | Passes |
| Caution on-strong-surface content (light) | 5.48:1 | 4.5:1 | Passes |
| Critical on-strong-surface content (light) | 6.04:1 | 4.5:1 | Passes |
| Data-display grid on Base (light) | 1.20:1 | 3:1 | **Fails** — decorative/structural only, never the sole way to read a value |
| Primary text on Canvas/Base (dark) | 17.17:1 | 4.5:1 | Passes |
| Primary text on Raised (dark) | 14.17:1 | 4.5:1 | Passes |
| Secondary text on Canvas/Base (dark) | 5.72:1 | 4.5:1 | Passes |
| Tertiary/metadata on Canvas/Base (dark, large-text only) | 3.32:1 | 3:1 | Passes (restricted to large text/UI) |
| Inverse text on Inverse surface (dark) | 15.32:1 | 4.5:1 | Passes |
| Accent/Interactive/Link/Quiet-action text on Canvas/Base (dark) | 8.87:1 | 4.5:1 | Passes |
| Muted metadata / Placeholder on Canvas/Base (dark) | 5.72:1 | 4.5:1 | Passes |
| Strong/Interactive border on Raised (dark) | 4.72:1 | 3:1 | Passes |
| Interactive border on Canvas/Base (dark) | 5.72:1 | 3:1 | Passes |
| Default/Subtle border on Raised (dark) | 2.08:1 | 3:1 | **Fails** — restricted to decorative use paired with another boundary cue |
| Selected border / Focus indicator on Canvas/Base (dark) | 8.87:1 | 3:1 | Passes |
| Focus indicator on Raised (dark) | 7.32:1 | 3:1 | Passes |
| Secondary action content on background (dark) | 14.17:1 | 4.5:1 | Passes |
| Informational-dark text on Canvas/Base | 9.90:1 | 4.5:1 | Passes |
| Positive-dark text on Canvas/Base | 9.96:1 | 4.5:1 | Passes |
| Caution-dark text on Canvas/Base | 8.70:1 | 4.5:1 | Passes |
| Critical-dark text on Canvas/Base | 8.13:1 | 4.5:1 | Passes |
| Informational-dark on Subtle surface | 8.17:1 | 4.5:1 | Passes |
| Positive-dark on Subtle surface | 8.22:1 | 4.5:1 | Passes |
| Caution-dark on Subtle surface | 7.18:1 | 4.5:1 | Passes |
| Critical-dark on Subtle surface | 6.71:1 | 4.5:1 | Passes |
| Informational-dark on-strong-surface content | 8.17:1 | 4.5:1 | Passes |
| Positive-dark on-strong-surface content | 8.22:1 | 4.5:1 | Passes |
| Caution-dark on-strong-surface content | 7.18:1 | 4.5:1 | Passes |
| Critical-dark on-strong-surface content | 6.71:1 | 4.5:1 | Passes |
| Data-display grid on Canvas (dark) | 1.21:1 | 3:1 | **Fails** — decorative/structural only, same restriction as light mode |

**In plain terms:** every text and essential-border pair in both themes
meets its required threshold, with four documented, intentional
exceptions — the decorative-only Default/Subtle borders and data-display
gridlines in both modes (which never carry information alone), and
Informational's two normal-text restrictions in light mode (restricted
to large text/icon use). No pair was silently allowed to fail; every
failure above is either an accepted decorative exemption or an explicit
usage restriction stated in the relevant document.

**This is not a claim of complete WCAG conformance.** Only the pairs
listed were tested, in isolation. Real usage must be re-verified once
component-level implementation, exact translucency opacity, and gradient
overlay text are finalized (see §5).

## 4. Status vs. Accent Distinguishability Check

- Light mode: Critical (`#B3261E`, red) vs. accent (`#4A4EE0`,
  indigo-violet) — different hue families, not confusable.
- Dark mode: Critical (`#FF8A80`, coral) vs. accent (`#A9ACFF`,
  lavender) — different hue families, not confusable.
- Light mode: Informational (`#2F6FED`, blue) vs. accent (`#4A4EE0`,
  indigo-violet) — related but distinguishable hue families; both are
  in the blue-violet range, so projects substituting a different accent
  hue (per [adaptation.md §1.1](adaptation.md#1-project-controlled-adaptation))
  should re-check this pair specifically.
- Dark mode: Informational-dark (`#7CC4FF`, sky blue) vs. accent-30
  (`#A9ACFF`, lavender) — deliberately shifted toward cyan specifically
  to increase separation from the accent hue (see
  [dark-theme.md §6](dark-theme.md#6-status-families)).

## 5. Items Not Verified

The following are explicitly `Not verified` and must not be treated as
passing until calculated:

- Accent-surface and Scrim opacity values (both modes) — no specific
  opacity has been approved, so no worst-case contrast calculation has
  been run.
- Selection-background opacity (both modes) — same reason.
- The gradient worked example in
  [adaptation.md §4.3](adaptation.md#43-worked-example--worst-case-contrast)
  (`neutral-10` text over the `accent-30` gradient stop) — flagged
  explicitly rather than assumed to pass.
- Media-overlay contrast against actual (as opposed to placeholder)
  images — inherently project-specific and cannot be verified in the
  abstract.
- Full data-display categorical palette — deferred, not yet designed.
- Mobile/compact-breakpoint layout review and high-zoom/enlarged-text
  layout review — the requirement to perform these is established in
  §1, but the review itself depends on KBDL-006 (Responsive/
  Accessibility), not yet available.

## 6. Manual Documentation Reviews Performed

- **Heading-hierarchy review** — no skipped levels across all five theme
  documents.
- **Relative-link and anchor validation** — automated script, see the
  KBDL-004 final report for the command and result.
- **Empty-section scan** — no empty sections found.
- **Placeholder scan** — no `TBD`/`TODO`/lorem-ipsum content found.
- **Duplicate requirement-ID scan** — all `KBDL-THM-###` IDs confirmed
  unique.
- **Requirement-ID format review** — all IDs follow
  `KBDL-THM-###`, consistent with
  [conventions.md §2](../conventions.md#2-requirement-identification).
- **Lifecycle-status review** — every exact mapping and every newly
  proposed value confirmed `Recommended`, never `Approved`, except
  where a value is a direct, unmodified reuse of an already-`Approved`
  KBDL-003 foundation color used for its already-approved purpose.
- **Validation-status review** — `Verified` used only where a
  calculation was actually performed; `Not verified` used everywhere
  else (§5).
- **Semantic-role completeness review** — §2 above.
- **Light/dark parity review** — §2 above.
- **Contrast review** — §3 above.
- **Status-family review** — §4 above and
  [adaptation.md §5](adaptation.md#5-status-family-theme-behavior).
- **Precedence-flow review** — the decision flow in
  [themes/README.md §5](README.md#5-theme-selection-precedence) checked
  for a single deterministic path with no ambiguous branch.
- **Project-override review** — [adaptation.md §1](adaptation.md#1-project-controlled-adaptation)
  checked against the "must not" list for completeness.
- **Profile consistency review** — confirmed Showcase/Precision/Flow
  sections in every document reference the same underlying roles.
- **Scope-compliance review** — confirmed no motion timing, easing,
  component anatomy, or KBDL-005+ content appears anywhere in
  `docs/kbdl/themes/`.
- **Roadmap-reference review** — confirmed every "KBDL-00#" reference in
  `docs/kbdl/themes/` matches the approved roadmap mapping (004 Themes,
  005 Motion, 006 Responsive/Accessibility, 007/008 Components, 009
  Profiles/Customization, 010 Assembly/Validation).
