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
  [adaptation.md §4.3](adaptation.md#43-worked-example--worst-case-contrast-corrected-kbdl-004-r1).
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
  breakpoints; exact breakpoint values are now proposed as `Recommended`
  in [responsive.md §7](../responsive.md#7-proposed-exact-breakpoint-thresholds)
  and target-size requirements are defined in
  [accessibility.md §25](../accessibility.md#25-target-sizing-and-spacing)
  (both KBDL-006); the review itself remains implementation-dependent
  and `Not verified`.
- **Reduced-motion behavior** — per
  [adaptation.md §7](adaptation.md#7-theme-transition-guidance).
- **High-zoom and enlarged-text review** — text roles must remain within
  contrast thresholds when the user has enlarged text or zoomed the
  page, since relative contrast ratios are zoom-independent but layout
  reflow is not; the requirement to reflow at 200% zoom and 320px width
  is now defined in
  [responsive.md §21](../responsive.md#21-zoom-and-enlarged-text) (KBDL-006);
  the implementation-level review itself remains `Not verified`, since
  no implementation exists.

## 2. Parity Check (Revalidated under KBDL-004-R1)

**Method:** every role listed in
[semantic-roles.md §1](semantic-roles.md#1-semantic-role-inventory) was
checked directly against the actual rows in
[light-theme.md](light-theme.md) and [dark-theme.md](dark-theme.md) — a
re-run against the real tables, not a re-assertion of the prior report.
This re-run found and fixed one real defect: a paragraph inserted
between rows of the Status Families table in
[light-theme.md §5](light-theme.md#5-status-families) had silently
broken the table, orphaning its "Neutral status" row outside the table
structure. That row has been restored to the table; the parity result
below reflects the corrected table.

**Counting model:** 4 colored status families × 6 sub-roles = 24
distinct roles; Neutral status contributes 0 additional distinct roles
(implemented via role-level alias only). See
[semantic-roles.md § Parity Matrix](semantic-roles.md#parity-matrix-corrected-under-kbdl-004-r1)
for the full corrected table.

**Result (corrected under KBDL-004-R3):**

- Total unique semantic roles: **72**
- Total light-mode mappings (direct values or the 1 named alias): **72**
- Total dark-mode mappings (direct values or the 1 named alias): **72**
- Role-level aliases (not counted as separate roles): **1** — Neutral
  status → existing Primary/Secondary text, Default/Strong border, and
  Subtle surface roles (both modes). This is the same model, with the
  same count, used in
  [semantic-roles.md § Parity Matrix](semantic-roles.md#parity-matrix-corrected-under-kbdl-004-r1);
  **Keyboard focus and Text-link states are not aliases** under this
  model (see below) — a KBDL-004-R2 version of this document had
  incorrectly counted Keyboard focus as an alias while
  `semantic-roles.md` simultaneously counted it among the Actions
  category's 10 distinct roles; KBDL-004-R3 resolves that contradiction
  by classifying Keyboard focus as a distinct role, consistent with its
  own inventory entry and its mapping in both theme files.
- Unresolved or missing mappings: **none**.

No role is marked "not applicable" in either mode.

**Note on "Selection text/background," "Text-link states," and
"Keyboard focus":** none of the three is an alias. All are distinct
inventory roles (counted in the 72) whose *values* happen to reuse (or,
for Keyboard focus, are required to equal) another role's color — the
same ordinary value-reuse pattern as Muted metadata (reuses Secondary
text) — rather than being a pointer with no separate definition of its
own, which is what distinguishes the one true alias (Neutral status)
under this document's model. "Selection text/background" is presented
as two table rows in [light-theme.md §2](light-theme.md#2-text-and-content) for
readability, the same way Primary text and Secondary text each get a
Base-surface row and a Canvas-surface row. This is a presentation
choice, not a double-counted or aliased role.

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
| Informational text on Base (light) — **revised value `#164499`, KBDL-004-R1** | 9.05:1 | 4.5:1 | Passes, large margin |
| Positive text on Base (light) | 6.57:1 | 4.5:1 | Passes |
| Caution text on Base (light) | 5.93:1 | 4.5:1 | Passes |
| Critical text on Base (light) | 6.54:1 | 4.5:1 | Passes |
| Informational text on Subtle surface (light) — **revised value** | 7.51:1 | 4.5:1 | Passes, large margin — corrected from the original `#2F6FED` value's 3.78:1 failure |
| Positive text on Subtle surface (light) | 5.46:1 | 4.5:1 | Passes |
| Caution text on Subtle surface (light) | 4.92:1 | 4.5:1 | Passes |
| Critical text on Subtle surface (light) | 5.43:1 | 4.5:1 | Passes |
| Informational on-strong-surface content (light) — **revised value** | 8.37:1 | 4.5:1 | Passes, large margin — corrected from the original `#2F6FED` value's 4.21:1 failure |
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
| Gradient caption-band text (`neutral-10` on a **fully opaque** `neutral-100` caption band, placed over the gradient) | 17.17:1 (directly correct — the band is opaque, so the gradient underneath has no compositing effect on it; not "inherited" from an unrelated claim) | 4.5:1 | Passes — see [adaptation.md §4.3](adaptation.md#43-worked-example--worst-case-contrast-corrected-kbdl-004-r1); direct text on the raw gradient (`neutral-10`/`neutral-90` against either endpoint) is prohibited, not verified, since neither passes across both endpoints (1.94:1–7.32:1 range) |

**In plain terms (corrected under KBDL-004-R1):** every text and
essential-border pair in both themes now meets its required threshold,
with four documented, intentional decorative exemptions — the
decorative-only Default/Subtle borders and data-display gridlines in
both modes, which never carry information alone. The two prior
Informational failures (3.78:1 and 4.21:1) are resolved by the revised
`#164499` value (see the Informational rows above), not carried forward
as restrictions. The gradient's raw endpoints remain unsuitable for
direct text (see [adaptation.md §4.3](adaptation.md#43-worked-example--worst-case-contrast-corrected-kbdl-004-r1))
and are addressed by prohibiting direct text on the gradient rather than
accepting a failing pair. No pair is silently allowed to fail; every
remaining exemption is an accepted decorative case, and every
previously-restricted status case has been resolved with a passing
value instead.

**This is not a claim of complete WCAG conformance.** Only the pairs
listed were tested, in isolation. Real usage must be re-verified once
component-level implementation and exact translucency opacity values
are finalized (see §5); the gradient's direct-text failure is not
"pending re-verification" — it is a permanent constraint addressed by
the no-direct-text-on-gradient rule, not something a future calculation
could pass.

## 4. Status vs. Accent Distinguishability Check

- Light mode: Critical (`#B3261E`, red) vs. accent (`#4A4EE0`,
  indigo-violet) — different hue families, not confusable.
- Dark mode: Critical (`#FF8A80`, coral) vs. accent (`#A9ACFF`,
  lavender) — different hue families, not confusable.
- Light mode: Informational (`#164499`, revised under KBDL-004-R1, a
  pure/cyan-leaning blue) vs. accent (`#4A4EE0`, indigo-violet) —
  distinguishable hue families, more clearly separated than the
  original `#2F6FED` value since `#164499` sits further from violet on
  the hue wheel; projects substituting a different accent hue (per
  [adaptation.md §1.1](adaptation.md#1-project-controlled-adaptation))
  should still re-check this pair.
- Dark mode: Informational-dark (`#7CC4FF`, sky blue) vs. accent-30
  (`#A9ACFF`, lavender) — deliberately shifted toward cyan specifically
  to increase separation from the accent hue (see
  [dark-theme.md §6](dark-theme.md#6-status-families)).

## 5. Items Not Verified

The following are explicitly `Not verified` and must not be treated as
passing until calculated. [KBDL-DEC-013](../decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)
(the project owner's approval of the ten-item theme decision packet)
does not change this — approval is a lifecycle/authority decision,
separate from validation, and explicitly excludes every item below from
its scope:

- Accent-surface and Scrim opacity values (both modes) — no specific
  opacity has been approved, so no worst-case contrast calculation has
  been run. **Excluded from the approval-ready decision-packet items**
  (see [themes/README.md §10.2](README.md#10-theme-decision-packet-approved-under-kbdl-004-a1)).
- Selection-background opacity (both modes) — same reason. **Excluded
  from the approval-ready decision-packet items.**
- Any **translucent** variant of the gradient caption band or media
  caption band (e.g., at reduced opacity) — the *opaque* caption-band
  pair used in the approval-ready recommendation is `Verified` (17.17:1,
  §3), but a translucent version of that same band is a different pair:
  its effective color would be an alpha composite of the band color and
  whatever is behind it (the gradient's stops, or the actual media
  content), and no such composite has been calculated. **Excluded from
  the approval-ready decision-packet items** until an exact opacity is
  chosen and its worst-case composite is calculated against every
  permitted underlying background.
- The gradient's *direct-text* pairs are **not** listed here as
  "pending" — they were calculated (§3, §4 below) and found to fail
  across the full endpoint range; this is resolved by prohibiting direct
  text on the gradient (§4.3), not by further calculation.
- Media-overlay contrast against actual (as opposed to placeholder)
  images — inherently project-specific and cannot be verified in the
  abstract. **Excluded from the approval-ready decision-packet items.**
- Full data-display categorical palette — deferred, not yet designed.
- Mobile/compact-breakpoint layout review and high-zoom/enlarged-text
  layout review — the requirement to perform these is established in
  §1, and the applicable breakpoint/zoom/reflow requirements are now
  defined in [responsive.md](../responsive.md) (KBDL-006), but the
  review itself remains implementation-dependent and `Not verified`,
  since no implementation exists.

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
