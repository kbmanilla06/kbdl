# KBDL Accessibility

Lifecycle status: mixed. `Approved` for the requirements below that
directly restate an already-`Approved` KBDL principle, foundation/theme/
motion rule, or WCAG 2.2 Level A/AA success criterion — see
[§47](#47-normative-requirements) for exact per-requirement status.
`Recommended` for genuinely new KBDL-specific enhancements beyond the
WCAG 2.2 AA baseline (e.g., a preferred larger target size, an enhanced
focus-indicator geometry) — pending project-owner approval via
[§49](#49-accessibility-decision-packet). This document does not claim
full WCAG conformance, screen-reader compatibility, or real-device
support — those require an implementation to test against, which does
not yet exist; see [§48](#48-accessibility-validation-matrix).

Return to the [specification index](README.md).

## 1. Purpose and Conformance Target

This document defines KBDL's accessibility requirements, using
**WCAG 2.2 Level AA** as the minimum conformance target, combined with
KBDL's enhanced motion-safety protections already established under
[KBDL-DEC-010](decision-register.md#kbdl-dec-010--wcag-22-aa-baseline-with-enhanced-motion-safety).
It resolves items KBDL-003 through KBDL-005 explicitly deferred here
(exact flash-frequency thresholds, mobile/high-zoom theme review,
detailed responsive-accessibility interaction) and adds new
`KBDL-A11Y-###` requirements. This document does not claim that any
implementation is conformant, tested with real screen readers, or
verified on real devices — those claims require an implementation and
recorded test evidence, neither of which exists at this specification
stage.

## 2. Accessibility Status Model

Uses KBDL's standard three-dimension model
([conventions.md §1](conventions.md#1-status-labels)): lifecycle/
approval, provenance, validation — independently tracked for every
requirement in this document. A requirement directly restating an
adopted WCAG 2.2 Level A or AA success criterion may be marked
`Approved` because the criterion itself was already adopted under
`KBDL-DEC-010`; a KBDL-specific enhancement beyond that baseline remains
`Recommended` until the project owner separately approves it. No
requirement in this document is marked `Verified` merely because it was
documented — `Verified` requires the stated validation method to have
actually been run with recorded evidence.

## 3. WCAG 2.2 Level AA Mapping

This document maps the following WCAG 2.2 success criteria (Level A and
AA only; Level AAA criteria are never described as AA requirements
here) to KBDL topics. Full official criterion text and numbering is
defined by the W3C; this table records which KBDL section addresses
each:

| WCAG 2.2 criterion | Level | KBDL section |
| --- | --- | --- |
| 1.3.1 Info and Relationships | A | [§8](#8-semantic-structure-and-relationships) |
| 1.3.2 Meaningful Sequence | A | [§10](#10-reading-and-focus-order) |
| 1.3.4 Orientation | AA | [responsive.md §20](responsive.md#20-orientation-changes) |
| 1.3.5 Identify Input Purpose | AA | [§32](#32-forms-labels-instructions-and-autocomplete) |
| 1.4.1 Use of Color | A | [§11](#11-color-independent-communication) |
| 1.4.3 Contrast (Minimum) | AA | [§12](#12-text-contrast) |
| 1.4.4 Resize Text | AA | [responsive.md §21](responsive.md#21-zoom-and-enlarged-text) |
| 1.4.5 Images of Text | AA | [§6](#6-text-alternatives) |
| 1.4.10 Reflow | AA | [responsive.md §11](responsive.md#11-layout-reflow) |
| 1.4.11 Non-text Contrast | AA | [§13](#13-non-text-contrast) |
| 1.4.12 Text Spacing | AA | [§19](#19-text-spacing-overrides) |
| 1.4.13 Content on Hover or Focus | AA | [responsive.md §24](responsive.md#24-hover-independent-discoverability) |
| 2.1.1 Keyboard | A | [§21](#21-keyboard-operability) |
| 2.1.2 No Keyboard Trap | A | [§22](#22-keyboard-traps-and-escape-behavior) |
| 2.1.4 Character Key Shortcuts | A | [§21](#21-keyboard-operability) |
| 2.2.1 Timing Adjustable | A | [§31](#31-timing-automatic-movement-and-interruptions) |
| 2.2.2 Pause, Stop, Hide | A | [§31](#31-timing-automatic-movement-and-interruptions) |
| 2.3.1 Three Flashes or Below Threshold | A | [§30](#30-flashing-vestibular-and-motion-safety-limits) |
| 2.4.1 Bypass Blocks | A | [§23](#23-bypass-mechanisms) |
| 2.4.2 Page Titled | A | [§9](#9-landmark-and-heading-architecture) |
| 2.4.3 Focus Order | A | [§10](#10-reading-and-focus-order) |
| 2.4.4 Link Purpose (In Context) | A | [§38](#38-consistent-navigation-identification-and-help) |
| 2.4.6 Headings and Labels | AA | [§9](#9-landmark-and-heading-architecture) |
| 2.4.7 Focus Visible | AA | [§14](#14-focus-visibility) |
| 2.4.11 Focus Not Obscured (Minimum) | AA | [§15](#15-focus-not-obscured) |
| 2.5.1 Pointer Gestures | A | [§27](#27-dragging-and-gesture-alternatives) |
| 2.5.2 Pointer Cancellation | A | [§26](#26-pointer-cancellation) |
| 2.5.3 Label in Name | A | [§32](#32-forms-labels-instructions-and-autocomplete) |
| 2.5.4 Motion Actuation | A | [§28](#28-motion-actuation-alternatives) |
| 2.5.7 Dragging Movements | AA | [§27](#27-dragging-and-gesture-alternatives) |
| 2.5.8 Target Size (Minimum) | AA | [§25](#25-target-sizing-and-spacing) |
| 3.1.1 Language of Page | A | [§37](#37-plain-language-and-cognitive-accessibility) |
| 3.2.1 On Focus | A | [§21](#21-keyboard-operability) |
| 3.2.2 On Input | A | [§32](#32-forms-labels-instructions-and-autocomplete) |
| 3.2.6 Consistent Help | A | [§38](#38-consistent-navigation-identification-and-help) |
| 3.3.1 Error Identification | A | [§33](#33-error-identification-and-recovery) |
| 3.3.2 Labels or Instructions | A | [§32](#32-forms-labels-instructions-and-autocomplete) |
| 3.3.3 Error Suggestion | AA | [§33](#33-error-identification-and-recovery) |
| 3.3.4 Error Prevention (Legal, Financial, Data) | AA | [§34](#34-error-prevention-for-consequential-actions) |
| 3.3.7 Redundant Entry | A | [§32](#32-forms-labels-instructions-and-autocomplete) |
| 3.3.8 Accessible Authentication (Minimum) | AA | [§36](#36-authentication-accessibility) |
| 4.1.2 Name, Role, Value | A | [§8](#8-semantic-structure-and-relationships) |
| 4.1.3 Status Messages | AA | [§35](#35-status-messages-and-live-communication) |

## 4. Accessibility-Supported Technology Assumptions

This specification assumes conformance is evaluated against widely-used
current browsers and assistive technologies (screen readers, screen
magnifiers, switch access, voice control) in their default
configurations. It does not assume or require any specific browser,
operating system, or assistive-technology product by name; it does not
claim conformance has been tested against any specific product, since
no implementation exists yet (see [§48](#48-accessibility-validation-matrix)).

## 5. Perceivable Content

Umbrella principle: all content and controls **must** be presentable to
users in ways they can perceive, regardless of sensory ability. This
section introduces the topic; specific requirements are in
[§6](#6-text-alternatives)–[§13](#13-non-text-contrast).

## 6. Text Alternatives

Status: `Approved` (`KBDL-A11Y-001`, directly restates WCAG 2.2 SC 1.1.1
Non-text Content, Level A, and SC 1.4.5 Images of Text, Level AA).

**Requirements:** every non-decorative image, icon, or graphic **must**
have a text alternative conveying its purpose; decorative images
**must** be excluded from assistive-technology narration (already
anticipated in
[foundations/iconography-media.md §2.6](foundations/iconography-media.md#26-accessibility-expectations));
text **must not** be presented as an image except where the
presentation itself (a logotype, for example) is essential.

## 7. Captions, Transcripts, and Audio Description

Status: `Approved` (`KBDL-A11Y-002`, restates WCAG 2.2 SC 1.2.x caption/
audio-description criteria, Level A/AA, already anticipated in
[foundations/iconography-media.md §2.6](foundations/iconography-media.md#26-accessibility-expectations)).

Video with audio **must** provide captions; audio-only content **must**
provide a transcript; video conveying information visually that isn't in
the audio track **must** provide audio description or an equivalent
text alternative. Exact captioning workflow/vendor is implementation-layer
and out of scope.

## 8. Semantic Structure and Relationships

Status: `Approved` (`KBDL-A11Y-003`, directly restates WCAG 2.2 SC 1.3.1
Info and Relationships and SC 4.1.2 Name, Role, Value, both Level A).

Every component **must** expose its name, role, value, and state
programmatically, not only visually. Visual groupings, labels, and
hierarchy **must** be represented in the underlying semantic structure,
not conveyed by layout or styling alone.

## 9. Landmark and Heading Architecture

Status: `Approved` (`KBDL-A11Y-004`, directly restates WCAG 2.2 SC 2.4.2
Page Titled, Level A, and SC 2.4.6 Headings and Labels, Level AA).

Every page **must** have a descriptive title; heading levels **must**
reflect actual content hierarchy without skipping levels for visual
effect; landmark regions (navigation, main content, complementary
content) **must** be identifiable programmatically.

## 10. Reading and Focus Order

Status: `Approved` (`KBDL-A11Y-005`, directly restates WCAG 2.2 SC 1.3.2
Meaningful Sequence and SC 2.4.3 Focus Order, both Level A). Full detail
in [responsive.md §12](responsive.md#12-source-order-and-reading-order)
and [responsive.md §25](responsive.md#25-responsive-focus-management);
this entry exists to complete the WCAG mapping table in
[§3](#3-wcag-22-level-aa-mapping).

## 11. Color-Independent Communication

Status: `Approved` (`KBDL-A11Y-006`, directly restates WCAG 2.2 SC 1.4.1
Use of Color, Level A, and KBDL's own locked component-state-clarity
rule, [principles.md §5.1](principles.md#51-locked-identity-rules)).

Color **must never** be the only means of conveying information, an
action, a prompted response, or distinguishing a visual element — pair
with text, icon, pattern, or position.

## 12. Text Contrast

Status: `Approved` (`KBDL-A11Y-007`, directly restates WCAG 2.2 SC 1.4.3
Contrast (Minimum), Level AA, already adopted and applied throughout
[themes/light-theme.md](themes/light-theme.md) and
[themes/dark-theme.md](themes/dark-theme.md)).

Normal text **must** meet 4.5:1 contrast against its background; large
text **must** meet 3:1. This restates, and does not reopen, the exact
approved theme contrast evidence in
[themes/validation.md §3](themes/validation.md#3-consolidated-contrast-evidence).

## 13. Non-Text Contrast

Status: `Approved` (`KBDL-A11Y-008`, directly restates WCAG 2.2 SC 1.4.11
Non-text Contrast, Level AA, already applied to KBDL's border and focus
roles).

Borders, icons, and other non-text elements conveying information or
boundaries, and UI-component states, **must** meet 3:1 contrast against
adjacent colors, except where already documented as an accepted
decorative exemption (per
[themes/validation.md §3](themes/validation.md#3-consolidated-contrast-evidence)).

## 14. Focus Visibility

Status: `Approved` (`KBDL-A11Y-009`, directly restates WCAG 2.2 SC 2.4.7
Focus Visible, Level AA, and the already-Approved Focus indicator role
across [themes/light-theme.md](themes/light-theme.md)/
[themes/dark-theme.md](themes/dark-theme.md)).

Every interactive element **must** show a visible focus indicator when
it receives keyboard focus, meeting the non-text contrast requirement
in [§13](#13-non-text-contrast) against every surface it can appear on.

## 15. Focus Not Obscured

Status: `Approved` (`KBDL-A11Y-010`, directly restates WCAG 2.2 SC 2.4.11
Focus Not Obscured (Minimum), Level AA). Full detail in
[responsive.md §18](responsive.md#18-sticky-and-fixed-regions).

## 16. Light, Dark, Forced-Colors, and High-Contrast Behavior

Status: `Recommended` (`KBDL-A11Y-011`) for the forced-colors and
high-contrast policy proposed below — this ground is currently
unaddressed anywhere in the themes module and was explicitly excluded
from the KBDL-004 theme decision packet approval
([KBDL-DEC-013](decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved)).
Light/dark behavior itself remains governed by the already-`Approved`
theme module ([themes/README.md](themes/README.md)) and is not reopened
here.

**Proposed forced-colors requirements** (see
[§49](#49-accessibility-decision-packet) for approval status):

- Interfaces **must** remain usable when a user-agent forced-colors
  mode overrides authored colors with a user-selected system palette,
  per the W3C CSS Color Adjustment specification's treatment of
  forced-colors mode as an accessibility feature.
- Meaning conveyed by shadows, gradients, transparency, or background
  images **must** have a non-color-dependent fallback, since
  forced-colors mode may suppress these effects.
- Visible boundaries (borders, focus indicators) **must** remain
  distinguishable when forced-colors mode is active, using system-color
  keywords rather than authored colors where the two would conflict.
- KBDL **must not** override a user's forced-colors or contrast
  preference except where doing so would make content entirely
  illegible (an explicitly narrow, documented exception, never a
  default).
- Light theme, dark theme, and forced-colors mode **must** be tested
  as three separate presentations, not assumed to be covered by testing
  only two of the three.

No CSS implementation code is prescribed; this is framework-neutral
policy only.

## 17. Resize Text

Status: `Approved` (`KBDL-A11Y-012`, directly restates WCAG 2.2 SC 1.4.4,
Level AA). Full detail in
[responsive.md §21](responsive.md#21-zoom-and-enlarged-text).

## 18. Reflow

Status: `Approved` (`KBDL-A11Y-013`, directly restates WCAG 2.2 SC 1.4.10,
Level AA). Full detail in
[responsive.md §11](responsive.md#11-layout-reflow).

## 19. Text-Spacing Overrides

Status: `Approved` (`KBDL-A11Y-014`, directly restates WCAG 2.2 SC 1.4.12
Text Spacing, Level AA).

Content **must** remain usable and undamaged when a user applies the
WCAG-defined text-spacing overrides: line height to at least 1.5 times
font size; paragraph spacing to at least 2 times font size; letter
spacing to at least 0.12 times font size; word spacing to at least 0.16
times font size. No content or functionality may be lost when these
overrides are applied.

## 20. Orientation

Status: `Approved` (`KBDL-A11Y-015`, directly restates WCAG 2.2 SC 1.3.4,
Level AA). Full detail in
[responsive.md §20](responsive.md#20-orientation-changes).

## 21. Keyboard Operability

Status: `Approved` (`KBDL-A11Y-016`, directly restates WCAG 2.2 SC 2.1.1
Keyboard, SC 2.1.4 Character Key Shortcuts (both Level A), and SC 3.2.1
On Focus, Level A).

**Requirements:** all functionality **must** be operable through a
keyboard interface without requiring specific timings for individual
keystrokes; single-character key shortcuts, if any, **must** be
remappable, disableable, or active only on focus; moving keyboard focus
to an element **must not** by itself trigger a change of context (e.g.,
automatic form submission or navigation).

## 22. Keyboard Traps and Escape Behavior

Status: `Approved` (`KBDL-A11Y-017`, directly restates WCAG 2.2 SC 2.1.2
No Keyboard Trap, Level A).

If keyboard focus can be moved into a component using the keyboard, it
**must** be possible to move focus away using only the keyboard (a
standard exit method, or documented instructions where a non-standard
exit is unavoidable).

## 23. Bypass Mechanisms

Status: `Approved` (`KBDL-A11Y-018`, directly restates WCAG 2.2 SC 2.4.1
Bypass Blocks, Level A).

A mechanism **must** exist to bypass repeated blocks of content (e.g.,
a "skip to main content" link, or landmark-based navigation) so
keyboard and screen-reader users are not forced through the same
repeated navigation on every page.

## 24. Pointer and Touch Behavior

Status: `Approved` (`KBDL-A11Y-019`, restates WCAG 2.2 SC 2.5.1 and
2.5.2, both cited fully in [§26](#26-pointer-cancellation)–[§27](#27-dragging-and-gesture-alternatives)).

Umbrella section introducing pointer/touch topics; normative detail is
in [§25](#25-target-sizing-and-spacing)–[§28](#28-motion-actuation-alternatives).

## 25. Target Sizing and Spacing

Status: `Approved` for the WCAG minimum (`KBDL-A11Y-020`, directly
restates WCAG 2.2 SC 2.5.8 Target Size (Minimum), Level AA).
`Recommended` for the KBDL-preferred enhanced size (`KBDL-A11Y-021`).

**WCAG minimum (Approved):** pointer targets **must** be at least 24 by
24 CSS pixels, except where at least one of the following five
WCAG 2.2 SC 2.5.8 exceptions applies:

- **Spacing** — the target is smaller than 24 by 24 CSS pixels, but
  targets are positioned so that a 24-CSS-pixel-diameter circle centered
  on each undersized target's bounding box does not intersect either
  another target's bounding box or another undersized target's own
  24-pixel circle. This is a **geometric separation test**, not simply
  "leave some space" — it must be verified per pair of adjacent
  undersized targets, not assumed.
- **Equivalent** — the same function is available through a different,
  on-page control that itself meets the 24-by-24 minimum (or a valid
  exception).
- **Inline** — the target is in a sentence or block of text (e.g., a
  link within a paragraph), where the text flow determines size.
- **User Agent Control** — the target's size is determined by the user
  agent and not modified by the author (e.g., a native browser control
  the author does not restyle).
- **Essential** — a particular presentation of the target is essential,
  or is legally required, for the information being conveyed, and no
  larger equivalent would preserve that essential presentation.

This document does not simplify the Spacing exception into a generic
"add space around small targets" rule — the exact 24-pixel-diameter,
non-intersecting-circle test above is the actual WCAG mechanism, and
any implementation claiming this exception must be checked against it
specifically.

**KBDL-preferred enhancement (Recommended):** a 44-by-44 CSS-pixel
preferred target size for primary actions, exceeding the WCAG minimum
— proposed in [§49](#49-accessibility-decision-packet), not yet
approved. Until approved, only the 24-by-24 WCAG minimum carries
implementation authority.

## 26. Pointer Cancellation

Status: `Approved` (`KBDL-A11Y-022`, directly restates WCAG 2.2 SC 2.5.2
Pointer Cancellation, Level A).

For single-pointer activation, at least one of the following **must**
hold: no down-event triggers the function; the function triggers on the
up-event and can be aborted by moving the pointer away before release;
the up-event reverses any action triggered by the down-event; or
completing the function on down-event is essential (e.g., a piano-key
simulation).

## 27. Dragging and Gesture Alternatives

Status: `Approved` (`KBDL-A11Y-023`, directly restates WCAG 2.2 SC 2.5.1
Pointer Gestures, Level A, and SC 2.5.7 Dragging Movements, Level AA).

All functionality that uses a multipoint or path-based gesture **must**
be operable with a single pointer without a path-based gesture, unless
the multipoint/path gesture is essential. All functionality that uses a
dragging movement **must** be operable with a single pointer without
dragging (e.g., a reorder achievable via up/down controls), unless
dragging is essential — this extends the already-`Approved`
[motion/patterns.md §3](motion/patterns.md#3-direct-manipulation-and-gesture-response)
requirement for a non-gesture alternative.

## 28. Motion Actuation Alternatives

Status: `Approved` (`KBDL-A11Y-024`, directly restates WCAG 2.2 SC 2.5.4
Motion Actuation, Level A).

Functionality triggered by device motion or user motion (e.g., shaking
to undo) **must** also be operable via a conventional UI control, and
motion actuation **must** be disableable to prevent accidental
triggering, except where the motion is essential to the function.

## 29. Reduced-Motion and No-Motion Parity

Status: `Approved` (`KBDL-A11Y-025`, restates the already-`Approved`
[motion/accessibility-performance.md §1](motion/accessibility-performance.md#1-reduced-motion-and-no-motion-parity)
in full — not reopened or restated with new substance here).

Cross-reference only: every major motion pattern's full-motion,
reduced-motion, and no-motion behavior is defined in
[motion/accessibility-performance.md §1.4](motion/accessibility-performance.md#14-per-category-parity-matrix),
approved under `KBDL-DEC-014`. This document does not duplicate that
matrix; it incorporates it as the accessibility baseline for motion.

## 30. Flashing, Vestibular, and Motion-Safety Limits

Status: `Approved` (`KBDL-A11Y-026`, directly restates WCAG 2.2 SC 2.3.1
Three Flashes or Below Threshold, Level A, and the already-Approved
KBDL motion-safety prohibited list).

**WCAG flash rule (Approved, exact):** content **must not** flash more
than three times in any one-second period, unless the flash is below
the general flash and red flash thresholds defined by WCAG 2.2's
referenced flash-analysis methodology. This document does not invent an
alternative or additional numeric threshold, and does not assert any
medical claim beyond what WCAG itself states.

**KBDL qualitative motion-safety list (Approved, already established in
[motion/accessibility-performance.md §2](motion/accessibility-performance.md#2-motion-safety)
and restated here for completeness, not as new policy):** large rapid
viewport movement; repeated shaking; continuous zoom; simulated camera
movement; rapid alternating direction; unexpected automatic movement in
task-focused contexts; high-frequency flashing; full-screen brightness
changes; large reading-context parallax; uninterruptible long
sequences; repeated pulsing near text; essential information available
only during animation. These qualitative restrictions apply regardless
of whether a flash falls under the numeric WCAG threshold above — a
flash within the WCAG limit can still violate the broader KBDL
motion-safety list (e.g., repeated pulsing near text at a sub-threshold
rate is still prohibited).

## 31. Timing, Automatic Movement, and Interruptions

Status: `Approved` (`KBDL-A11Y-027`, directly restates WCAG 2.2 SC 2.2.1
Timing Adjustable and SC 2.2.2 Pause, Stop, Hide, both Level A).

Where a time limit is set by content, the user **must** be able to turn
it off, adjust it, or extend it (with documented exceptions for
real-time events or where the limit is essential). Moving, blinking,
scrolling, or auto-updating content that starts automatically, lasts
more than five seconds, and is presented in parallel with other content
**must** have a mechanism to pause, stop, or hide it.

## 32. Forms, Labels, Instructions, and Autocomplete

Status: `Approved` (`KBDL-A11Y-028`, directly restates WCAG 2.2 SC 1.3.5
Identify Input Purpose, SC 2.5.3 Label in Name, SC 3.2.2 On Input, SC
3.3.2 Labels or Instructions, and SC 3.3.7 Redundant Entry — Levels A/AA
as listed in [§3](#3-wcag-22-level-aa-mapping)).

Every form field **must** have a programmatically associated label;
labels **must** include the visible text used to identify the field
(supporting voice-control users who reference the visible label);
fields collecting common information types (name, address, etc.)
**must** support the appropriate autocomplete purpose where applicable;
changing a setting **must not** automatically cause a context change
unless the user was advised beforehand; information a user has already
provided in the same process **must not** be required again unless
essential (e.g., re-entering a password for security), auto-populated,
or available for the user to select.

## 33. Error Identification and Recovery

Status: `Approved` (`KBDL-A11Y-029`, directly restates WCAG 2.2 SC 3.3.1
Error Identification, Level A, and SC 3.3.3 Error Suggestion, Level AA).

Input errors **must** be identified and described to the user in text;
where a suggestion for correction is known and doesn't jeopardize
security or purpose, it **must** be provided.

## 34. Error Prevention for Consequential Actions

Status: `Approved` (`KBDL-A11Y-030`, directly restates WCAG 2.2 SC 3.3.4
Error Prevention (Legal, Financial, Data), Level AA).

For submissions that carry legal, financial, or data-modification
consequences, at least one of the following **must** hold: submissions
are reversible; data is checked for errors with an opportunity to
correct them; or a confirmation step is provided before finalizing.

## 35. Status Messages and Live Communication

Status: `Approved` (`KBDL-A11Y-031`, directly restates WCAG 2.2 SC 4.1.3
Status Messages, Level AA, and the locked component-state-clarity rule).

Status messages (loading, progress, success, error, and similar) that
are not given keyboard focus **must** still be programmatically
determinable so assistive technology can announce them without a
context change. This is the requirement that loading/progress/error
states must never depend only on visual animation, color, or layout
position — restating
[motion/patterns.md §2](motion/patterns.md#2-loading-and-progress) and
[§11](#11-color-independent-communication) at the status-communication
level.

## 36. Authentication Accessibility

Status: `Approved` (`KBDL-A11Y-032`, directly restates WCAG 2.2 SC 3.3.8
Accessible Authentication (Minimum), Level AA).

An authentication process **must not** require a cognitive-function
test (remembering a password, solving a puzzle, transcribing a code)
unless an alternative method not relying on such a test is also
available, or the test is providing an object identification or
personal-content identification exception permitted by WCAG. KBDL
authentication guidance **must** support password managers (no
restriction on paste-into-password-field) and copy/paste for
one-time codes.

## 37. Plain Language and Cognitive Accessibility

Status: `Approved` (`KBDL-A11Y-033`, directly restates WCAG 2.2 SC 3.1.1
Language of Page, Level A, and
[principles.md §6.3](principles.md#63-consumer-comprehension), Consumer
Comprehension).

The default human language of each page **must** be programmatically
determinable. Instructions and error messages **must** use plain
language appropriate for general consumers, consistent with the
already-Approved Consumer Comprehension principle.

## 38. Consistent Navigation, Identification, and Help

Status: `Approved` (`KBDL-A11Y-034`, directly restates WCAG 2.2 SC 2.4.4
Link Purpose (In Context), Level A, and SC 3.2.6 Consistent Help, Level
A).

A link's purpose **must** be determinable from its text alone or from
its text plus programmatically-determinable context. Where help
mechanisms (contact info, chat, FAQ) are provided across multiple
pages, they **must** appear in a consistent relative order.

## 39. Screen-Reader Behavior

Status: `Recommended` (`KBDL-A11Y-035`) for KBDL-specific screen-reader
testing-matrix guidance; the underlying requirement that all content be
programmatically determinable is `Approved` (restates [§8](#8-semantic-structure-and-relationships)).

No implementation exists to test with a real screen reader; this
document does not claim screen-reader compatibility. A preferred
testing matrix (which screen-reader/browser pairings to test once an
implementation exists) is proposed in
[§49](#49-accessibility-decision-packet) as a KBDL-specific enhancement,
not yet approved.

## 40. Media and Animation Controls

Status: `Approved` (`KBDL-A11Y-036`, restates [§7](#7-captions-transcripts-and-audio-description)
and the already-Approved
[motion/patterns.md §7](motion/patterns.md#7-media-motion) media-motion
requirements — not reopened here).

Cross-reference only: exact autoplay, pause/stop, and captioning
requirements for media are defined in [§7](#7-captions-transcripts-and-audio-description)
and `motion/patterns.md §7`.

## 41. Accessible Data Presentation

Status: `Approved` (`KBDL-A11Y-037`, restates [§8](#8-semantic-structure-and-relationships)
applied to tabular data).

Data tables **must** use programmatic row/column header association so
assistive technology can convey a cell's context; a responsive
transformation of a table (per
[responsive.md §16](responsive.md#16-data-dense-and-tabular-content))
**must** preserve this association, not just its visual appearance.

## 42. Mobile Accessibility

Status: `Approved` (`KBDL-A11Y-038`, restates
[responsive.md §22–§25](responsive.md#22-virtual-keyboard-behavior) and
[motion/accessibility-performance.md §4](motion/accessibility-performance.md#4-mobile-and-input-method-considerations)).

Cross-reference only, to avoid duplication: mobile-specific
requirements (virtual keyboard, touch targets, orientation, safe areas)
are fully defined in `responsive.md` and `motion/accessibility-performance.md`.

## 43. Virtual-Keyboard Accessibility

Status: `Approved` (`KBDL-A11Y-039`, restates
[responsive.md §22](responsive.md#22-virtual-keyboard-behavior)).

Cross-reference only — see `responsive.md §22` for the full requirement.

## 44. Profile Interpretation

Status: `Approved` (`KBDL-A11Y-040`, directly restates
[principles.md §9.4](principles.md#94-shared-constraints-across-profiles):
"Profiles may alter emphasis but cannot... Remove accessibility rules").

Showcase, Precision, and Flow **must** share this entire accessibility
specification without exception — no profile may weaken any requirement
in this document. Profiles differ only in visual/motion emphasis
(already governed by KBDL-002/004/005), never in accessibility floor.

## 45. Conforming Examples

1. **Showcase, screen reader.** A portfolio project card's decorative
   background pattern is excluded from AT narration; the project title
   and description remain the accessible name. *Conforms:* [§6](#6-text-alternatives).
2. **Precision, keyboard.** A dashboard's filter panel is fully operable
   via Tab/Enter/Escape with no keyboard trap and a visible focus ring
   meeting 3:1 contrast on every panel background. *Conforms:*
   [§21](#21-keyboard-operability), [§14](#14-focus-visibility).
3. **Flow, low vision.** A checkout form remains fully usable after the
   user applies WCAG text-spacing overrides and 200% zoom. *Conforms:*
   [§19](#19-text-spacing-overrides), [responsive.md §21](responsive.md#21-zoom-and-enlarged-text).
4. **All profiles, forced-colors.** A form's required-field indicator
   uses an icon plus text, remaining visible and meaningful under
   forced-colors mode. *Conforms:* [§16](#16-light-dark-forced-colors-and-high-contrast-behavior),
   [§11](#11-color-independent-communication).
5. **Precision, touch.** A data-table row-reorder control offers
   up/down buttons as a non-drag alternative to dragging. *Conforms:*
   [§27](#27-dragging-and-gesture-alternatives).
6. **All profiles, reduced motion.** A success confirmation uses a
   static checkmark icon and text instead of an animated celebration
   when reduced motion is active. *Conforms:* [§29](#29-reduced-motion-and-no-motion-parity).
7. **Flow, cognitive accessibility.** A password reset flow supports
   pasting a one-time code and does not require solving a puzzle.
   *Conforms:* [§36](#36-authentication-accessibility).
8. **All profiles, status.** A save-in-progress indicator announces
   "Saving…" and then "Saved" via a programmatically determinable
   status message, without requiring the user's visual attention.
   *Conforms:* [§35](#35-status-messages-and-live-communication).

## 46. Non-Conforming Examples

1. **Color-only error state.** A required field turns red with no icon,
   text, or accessible-name change. *Violates:* [§11](#11-color-independent-communication).
2. **Keyboard trap.** A modal dialog cannot be exited with Escape or Tab
   cycling, trapping keyboard focus. *Violates:* [§22](#22-keyboard-traps-and-escape-behavior).
3. **Missing focus indicator.** A custom control removes its focus
   outline with no visible replacement. *Violates:* [§14](#14-focus-visibility).
4. **Undersized target.** A close ("X") button is 16 by 16 CSS pixels
   with no adjacent equivalent-sized target and no listed exception.
   *Violates:* [§25](#25-target-sizing-and-spacing).
5. **Drag-only reorder.** A list can only be reordered by dragging, with
   no keyboard or single-pointer alternative. *Violates:* [§27](#27-dragging-and-gesture-alternatives).
6. **Cognitive-test authentication.** A login flow requires solving a
   memory puzzle with no alternative method. *Violates:* [§36](#36-authentication-accessibility).
7. **Silent status change.** A background sync fails without any
   programmatically determinable status message, only a color change
   on an icon. *Violates:* [§35](#35-status-messages-and-live-communication).
8. **Repeated shaking near text.** An unread-badge animation continues
   shaking indefinitely next to body copy. *Violates:* [§30](#30-flashing-vestibular-and-motion-safety-limits).
9. **Text-spacing override breaks layout.** Applying WCAG text-spacing
   overrides causes text to overlap and become unreadable. *Violates:*
   [§19](#19-text-spacing-overrides).
10. **Motion-only actuation.** A "shake to undo" gesture has no
    alternative button and cannot be disabled. *Violates:* [§28](#28-motion-actuation-alternatives).
11. **Redundant re-entry.** A multi-step checkout asks the user to
    re-enter their shipping address on a later step despite already
    having it. *Violates:* [§32](#32-forms-labels-instructions-and-autocomplete).
12. **No error suggestion.** An invalid-email error says only "Error"
    with no description of what's wrong or how to fix it. *Violates:*
    [§33](#33-error-identification-and-recovery).

## 47. Normative Requirements

Requirement IDs use `KBDL-A11Y-###`
([conventions.md §2](conventions.md#2-requirement-identification)),
starting at `001` (no prior `A11Y` requirement exists in the
repository).

- **KBDL-A11Y-001** — Non-decorative images/icons **must** have a text
  alternative; decorative images **must** be excluded from AT
  narration; text **must not** be presented as an image except where
  essential.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.1.1, Level A, and SC 1.4.5, Level AA). Provenance: Confirmed.
  - Validation status: Not verified.
  - Validation-classification authority record: `KBDL-SMR1-BA-VC-0001-OWNER-DECISION-2026-07-29` — current and non-retroactive project-owner decision authority for retaining this classification; decision authority only, not validation evidence.
  - Related requirement: `KBDL-FND-007` (media anticipates accessible-text
    requirements, Approved).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§6](#6-text-alternatives).
  - Validation method: Manual + automated static accessibility check
    once implemented.

- **KBDL-A11Y-002** — Video with audio **must** provide captions;
  audio-only content **must** provide a transcript; video conveying
  visual-only information **must** provide audio description or
  equivalent text.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.2.x,
    Level A/AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-001`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§7](#7-captions-transcripts-and-audio-description).
  - Validation method: Manual review once implemented.

- **KBDL-A11Y-003** — Every component **must** expose name, role,
  value, and state programmatically; groupings/labels/hierarchy
  **must** be represented in semantic structure, not layout alone.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.3.1 and
    SC 4.1.2, both Level A). Provenance: Confirmed. Validation status:
    Not verified.
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§8](#8-semantic-structure-and-relationships).
  - Validation method: Automated static accessibility check + manual
    screen-reader review once implemented.

- **KBDL-A11Y-004** — Every page **must** have a descriptive title;
  heading levels **must** reflect actual hierarchy; landmarks **must**
  be programmatically identifiable.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.4.2,
    Level A, and SC 2.4.6, Level AA). Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-A11Y-003`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§9](#9-landmark-and-heading-architecture).
  - Validation method: Automated static check + manual review once
    implemented.

- **KBDL-A11Y-005** — Reading order **must** match source order; focus
  order **must** be logical and consistent with visual presentation.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.3.2 and
    SC 2.4.3, both Level A). Provenance: Confirmed. Validation status:
    Not verified.
  - Related requirement: `KBDL-RSP-007`, `KBDL-RSP-020`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§10](#10-reading-and-focus-order),
    [responsive.md §12, §25](responsive.md#12-source-order-and-reading-order).
  - Validation method: Manual keyboard/screen-reader order review once
    implemented.

- **KBDL-A11Y-006** — Color **must never** be the sole means of
  conveying information, an action, or a distinction.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.4.1,
    Level A, and the locked component-state-clarity rule). Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11](#11-color-independent-communication).
  - Validation method: Manual review once implemented.

- **KBDL-A11Y-007** — Normal text **must** meet 4.5:1 contrast; large
  text **must** meet 3:1, per the already-verified theme evidence.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.4.3,
    Level AA). Provenance: Confirmed. Validation status: Verified (for
    the documented theme role pairs; see
    [themes/validation.md §3](themes/validation.md#3-consolidated-contrast-evidence)).
  - Related requirement: `KBDL-THM-007`, `KBDL-THM-008`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§12](#12-text-contrast).
  - Validation method: WCAG relative-luminance contrast calculation
    (completed for theme role pairs, see cited evidence).

- **KBDL-A11Y-008** — Borders, icons, and UI-component states **must**
  meet 3:1 non-text contrast, except accepted decorative exemptions.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.4.11,
    Level AA). Provenance: Confirmed. Validation status: Verified (for
    documented pairs, see cited evidence).
  - Related requirement: `KBDL-A11Y-007`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§13](#13-non-text-contrast).
  - Validation method: WCAG relative-luminance contrast calculation
    (completed for documented pairs).

- **KBDL-A11Y-009** — Every interactive element **must** show a visible
  focus indicator meeting non-text contrast on every surface it can
  appear on.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.4.7,
    Level AA). Provenance: Confirmed. Validation status: Verified (for
    the documented Focus indicator role; see theme validation evidence).
  - Related requirement: `KBDL-A11Y-008`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14](#14-focus-visibility).
  - Validation method: Contrast calculation (completed); manual
    keyboard review once implemented.

- **KBDL-A11Y-010** — A sticky/fixed region **must not** entirely
  obscure the currently focused element.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.4.11,
    Level AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-RSP-013`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§15](#15-focus-not-obscured),
    [responsive.md §18](responsive.md#18-sticky-and-fixed-regions).
  - Validation method: Manual keyboard-focus review once implemented.

- **KBDL-A11Y-011** — Interfaces **must** remain usable under
  user-agent forced-colors mode; meaning conveyed by shadow/gradient/
  transparency/background image **must** have a non-color-dependent
  fallback; light, dark, and forced-colors presentations **must** be
  tested as three separate cases.
  - Lifecycle status: Recommended (new KBDL policy — no prior theme
    decision addresses forced-colors mode; explicitly excluded from
    `KBDL-DEC-013`). Provenance: Assumed. Validation status: Not
    verified.
  - Related requirement: No direct prior requirement ID — forced-colors/
    high-contrast mode is explicitly listed as excluded from the KBDL-004
    theme decision packet approval; see
    [themes/README.md §10.3](themes/README.md#103-unresolved-or-not-approval-ready)
    and [KBDL-DEC-013](decision-register.md#kbdl-dec-013--kbdl-004-theme-decisions-approved).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§16](#16-light-dark-forced-colors-and-high-contrast-behavior).
  - Validation method: Manual forced-colors testing once implemented;
    project-owner review (not yet performed).

- **KBDL-A11Y-012** — Text **must** be resizable to 200% without loss of
  content or functionality.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.4.4,
    Level AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-RSP-016`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§17](#17-resize-text).
  - Validation method: Manual zoom testing once implemented.

- **KBDL-A11Y-013** — Content **must** reflow at 320px-equivalent width
  without requiring horizontal scrolling for reading.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.4.10,
    Level AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-RSP-006`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§18](#18-reflow).
  - Validation method: Manual reflow testing once implemented.

- **KBDL-A11Y-014** — Content **must** remain usable and undamaged when
  WCAG text-spacing overrides are applied.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.4.12,
    Level AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§19](#19-text-spacing-overrides).
  - Validation method: Manual text-spacing override testing once
    implemented.

- **KBDL-A11Y-015** — Content and functionality **must not** be
  restricted to a single orientation unless essential.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.3.4,
    Level AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-RSP-015`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§20](#20-orientation),
    [responsive.md §20](responsive.md#20-orientation-changes).
  - Validation method: Manual orientation testing once implemented.

- **KBDL-A11Y-016** — All functionality **must** be keyboard-operable
  without specific timing requirements; single-character shortcuts
  **must** be remappable/disableable; focus **must not** trigger an
  unannounced context change.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.1.1, SC
    2.1.4, and SC 3.2.1, all Level A). Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§21](#21-keyboard-operability).
  - Validation method: Manual keyboard testing once implemented.

- **KBDL-A11Y-017** — Keyboard focus **must** be movable away from any
  component using only the keyboard.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.1.2,
    Level A). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-016`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22](#22-keyboard-traps-and-escape-behavior).
  - Validation method: Manual keyboard testing once implemented.

- **KBDL-A11Y-018** — A mechanism **must** exist to bypass repeated
  content blocks.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.4.1,
    Level A). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-004`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§23](#23-bypass-mechanisms).
  - Validation method: Manual keyboard testing once implemented.

- **KBDL-A11Y-019** — (Umbrella; see `KBDL-A11Y-020`–`024` for the
  normative pointer/touch requirements.)
  - Lifecycle status: Approved. Provenance: Confirmed. Validation
    status: Not applicable.
  - Related requirement: `KBDL-A11Y-020` through `024`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24](#24-pointer-and-touch-behavior).
  - Validation method: Not applicable (umbrella section).

- **KBDL-A11Y-020** — Pointer targets **must** be at least 24 by 24 CSS
  pixels, except where a documented WCAG exception applies.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.5.8,
    Level AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-RSP-014`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§25](#25-target-sizing-and-spacing).
  - Validation method: Manual measurement once implemented.

- **KBDL-A11Y-021** — A preferred 44-by-44 CSS-pixel target size for
  primary actions is proposed, exceeding the WCAG minimum.
  - Lifecycle status: Recommended (new KBDL enhancement, not yet
    approved). Provenance: Assumed. Validation status: Not
    applicable.
  - Related requirement: `KBDL-A11Y-020`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§25](#25-target-sizing-and-spacing),
    [§49](#49-accessibility-decision-packet).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-A11Y-022** — For single-pointer activation, at least one
  WCAG-defined cancellation mechanism **must** hold.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.5.2,
    Level A). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§26](#26-pointer-cancellation).
  - Validation method: Manual testing once implemented.

- **KBDL-A11Y-023** — Path-based/multipoint gestures and dragging
  movements **must** have a single-pointer, non-gesture, non-dragging
  alternative unless essential.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.5.1,
    Level A, and SC 2.5.7, Level AA). Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-MOT-015`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§27](#27-dragging-and-gesture-alternatives).
  - Validation method: Manual testing once implemented.

- **KBDL-A11Y-024** — Device/user-motion-triggered functionality **must**
  have a conventional UI alternative and **must** be disableable, unless
  essential.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.5.4,
    Level A). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§28](#28-motion-actuation-alternatives).
  - Validation method: Manual testing once implemented.

- **KBDL-A11Y-025** — Every major motion pattern's reduced-motion and
  no-motion behavior, as defined in `motion/accessibility-performance.md
  §1`, applies as this document's motion-accessibility baseline.
  - Lifecycle status: Approved (restates `KBDL-MOT-022`, already
    Approved under `KBDL-DEC-014`; not reopened). Provenance: Confirmed.
    Validation status: Not verified.
  - Related requirement: `KBDL-MOT-022`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§29](#29-reduced-motion-and-no-motion-parity).
  - Validation method: Cross-reference only; see `KBDL-MOT-022`'s own
    validation method.

- **KBDL-A11Y-026** — Content **must not** flash more than three times
  per second above the WCAG general/red flash thresholds; KBDL's
  qualitative motion-safety prohibited list applies regardless of
  numeric flash threshold.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.3.1,
    Level A, and restates the already-Approved `KBDL-MOT-023`).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-MOT-023`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§30](#30-flashing-vestibular-and-motion-safety-limits).
  - Validation method: Flash-analysis testing once implemented (exact
    threshold measurement is implementation-dependent and deferred
    until an implementation exists).

- **KBDL-A11Y-027** — Adjustable time limits **must** be extendable/
  disableable where content-set; automatic moving/blinking/scrolling
  content lasting over five seconds **must** have pause/stop/hide.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.2.1 and
    SC 2.2.2, both Level A). Provenance: Confirmed. Validation status:
    Not verified.
  - Related requirement: `KBDL-MOT-017` (ambient motion).
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§31](#31-timing-automatic-movement-and-interruptions).
  - Validation method: Manual testing once implemented.

- **KBDL-A11Y-028** — Form fields **must** have programmatic labels
  including visible label text; common input types **must** support
  autocomplete purpose; settings changes **must not** cause an
  unannounced context change; already-provided information **must not**
  be required again unless essential/auto-populated/selectable.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 1.3.5, SC
    2.5.3, SC 3.2.2, SC 3.3.2, and SC 3.3.7, Levels A/AA as listed).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§32](#32-forms-labels-instructions-and-autocomplete).
  - Validation method: Manual + automated static check once implemented.

- **KBDL-A11Y-029** — Input errors **must** be identified and described
  in text; correction suggestions **must** be provided where known and
  safe to disclose.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 3.3.1,
    Level A, and SC 3.3.3, Level AA). Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-A11Y-028`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§33](#33-error-identification-and-recovery).
  - Validation method: Manual testing once implemented.

- **KBDL-A11Y-030** — Legal/financial/data-modifying submissions
  **must** be reversible, error-checked with correction opportunity, or
  confirmed before finalizing.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 3.3.4,
    Level AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-029`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§34](#34-error-prevention-for-consequential-actions).
  - Validation method: Manual testing once implemented.

- **KBDL-A11Y-031** — Status messages not receiving focus **must** be
  programmatically determinable for assistive-technology announcement.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 4.1.3,
    Level AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-MOT-014`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§35](#35-status-messages-and-live-communication).
  - Validation method: Manual screen-reader testing once implemented.

- **KBDL-A11Y-032** — Authentication **must not** require an
  unsupported cognitive-function test without an alternative; password
  managers and copy/paste one-time codes **must** be supported.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 3.3.8,
    Level AA). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§36](#36-authentication-accessibility).
  - Validation method: Manual testing once implemented.

- **KBDL-A11Y-033** — The page's default human language **must** be
  programmatically determinable; instructions/errors **must** use plain
  language.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 3.1.1,
    Level A, and `KBDL-PRN-003`, Consumer Comprehension). Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-PRN-003`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§37](#37-plain-language-and-cognitive-accessibility).
  - Validation method: Manual review once implemented.

- **KBDL-A11Y-034** — Link purpose **must** be determinable from text
  alone or text plus programmatic context; help mechanisms **must**
  appear in consistent relative order across pages.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.4.4,
    Level A, and SC 3.2.6, Level A). Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§38](#38-consistent-navigation-identification-and-help).
  - Validation method: Manual review once implemented.

- **KBDL-A11Y-035** — A preferred screen-reader/browser testing matrix
  is proposed for future validation once an implementation exists.
  - Lifecycle status: Recommended (new KBDL testing-process
    enhancement, not yet approved). Provenance: Assumed.
    Validation status: Not applicable.
  - Related requirement: `KBDL-A11Y-003`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§39](#39-screen-reader-behavior),
    [§49](#49-accessibility-decision-packet).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-A11Y-036** — Media/animation control requirements are defined
  in [§7](#7-captions-transcripts-and-audio-description) and
  `motion/patterns.md §7`; not restated here.
  - Lifecycle status: Approved (cross-reference to already-Approved
    requirements). Provenance: Confirmed. Validation status: Not
    applicable.
  - Related requirement: `KBDL-MOT-019`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§40](#40-media-and-animation-controls).
  - Validation method: Not applicable (cross-reference section).

- **KBDL-A11Y-037** — Data tables **must** use programmatic row/column
  header association, preserved through any responsive transformation.
  - Lifecycle status: Approved (restates `KBDL-A11Y-003` applied to
    tabular data). Provenance: Confirmed. Validation status: Not
    verified.
  - Related requirement: `KBDL-RSP-011`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§41](#41-accessible-data-presentation).
  - Validation method: Automated static check + manual review once
    implemented.

- **KBDL-A11Y-038** — Mobile-specific accessibility requirements are
  defined in `responsive.md §22`–`§25` and `motion/accessibility-
  performance.md §4`; not restated here.
  - Lifecycle status: Approved (cross-reference). Provenance: Confirmed.
    Validation status: Not applicable.
  - Related requirement: `KBDL-RSP-017`, `KBDL-RSP-018`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§42](#42-mobile-accessibility).
  - Validation method: Not applicable (cross-reference section).

- **KBDL-A11Y-039** — Virtual-keyboard accessibility requirements are
  defined in `responsive.md §22`; not restated here.
  - Lifecycle status: Approved (cross-reference). Provenance: Confirmed.
    Validation status: Not applicable.
  - Related requirement: `KBDL-RSP-017`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§43](#43-virtual-keyboard-accessibility).
  - Validation method: Not applicable (cross-reference section).

- **KBDL-A11Y-040** — Showcase, Precision, and Flow **must** share this
  entire accessibility specification without exception.
  - Lifecycle status: Approved (directly restates
    [principles.md §9.4](principles.md#94-shared-constraints-across-profiles)).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-PRN-007`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§44](#44-profile-interpretation).
  - Validation method: Manual cross-profile review once the
    project-profiles module is approved.

## 48. Accessibility Validation Matrix

| Validation type | Scope | Status |
| --- | --- | --- |
| Documentation validation | This document's completeness, cross-references, terminology | Performed (see [§50](#50-deferred-and-unresolved-accessibility-items) and the implementation report) |
| Conceptual/manual design review | Every requirement in [§47](#47-normative-requirements) | Performed for documentation completeness; implementation-level review not yet possible |
| Automated static accessibility checks | Semantic structure, labels, contrast (tooling) | Not verified — no implementation exists to scan |
| Keyboard testing | Operability, traps, focus order/visibility | Not verified — no implementation exists |
| Screen-reader testing | Name/role/value, status messages, landmarks | Not verified — no implementation exists |
| Zoom/reflow testing | 200% resize, 320px reflow, text-spacing overrides | Not verified — no implementation exists |
| Contrast calculation | Text and non-text contrast | Verified for documented theme role pairs (see `themes/validation.md §3`); not verified for any new implementation |
| Forced-colors testing | [§16](#16-light-dark-forced-colors-and-high-contrast-behavior) | Not verified — policy only, pending approval and implementation |
| Reduced-motion testing | Cross-reference to `motion/validation.md` | Performed conceptually there; not implementation-tested |
| Flash analysis | [§30](#30-flashing-vestibular-and-motion-safety-limits) | Not verified — requires an implementation to analyze |
| Mobile and orientation testing | [§20](#20-orientation), [§42](#42-mobile-accessibility) | Not verified — no implementation exists |
| Real-device testing | All device-dependent requirements | Not verified — no implementation exists |
| Component-level testing | Deferred to KBDL-007 (Components) and later | Deferred |
| Production conformance testing | Deferred until an implementation exists | Deferred |

This document does **not** claim full WCAG conformance, screen-reader
compatibility, or real-device support. It claims only that the
documented requirements accurately map to WCAG 2.2 Level A/AA criteria
and already-approved KBDL rules, subject to the manual-review evidence
recorded in the implementation report for this module.

## 49. Accessibility Decision Packet

### 49.1 Already-Approved Accessibility Architecture (context only)

Not awaiting approval — provided as context. Every WCAG 2.2 Level A/AA
criterion mapped in [§3](#3-wcag-22-level-aa-mapping) is `Approved`
because the WCAG 2.2 AA baseline itself was already adopted under
[KBDL-DEC-010](decision-register.md#kbdl-dec-010--wcag-22-aa-baseline-with-enhanced-motion-safety);
this packet does not re-request approval for any WCAG-derived
requirement.

### 49.2 Recommended Decisions — Ready for Approval

| # | Decision | Recommendation | Rationale | Alternatives | Trade-offs | Accessibility impact | Responsive impact | Motion impact | Theme impact | Performance impact | Dependencies | Exact affected requirements | Exact approval scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Preferred enhanced target size | Adopt a 44-by-44 CSS-pixel preferred target for primary actions, above the 24-by-24 WCAG minimum (`KBDL-A11Y-021`) | Improves touch usability beyond the floor, consistent with common platform guidance | Keep only the WCAG 24×24 minimum (rejected — KBDL-005/006 already prefer generous touch targets elsewhere) | Larger targets consume more layout space at `compact`; must be reconciled with [responsive.md §10](responsive.md#10-gutters-and-responsive-spacing) | Exceeds, never weakens, the WCAG floor | Interacts with spacing-compression limits | Not applicable | Not applicable | Negligible | `KBDL-A11Y-020` | `KBDL-A11Y-021` | Item 1 only — does not touch the WCAG-mandated minimum (`KBDL-A11Y-020`), which remains Approved and unaffected either way |
| 2 | Forced-colors and high-contrast policy | Adopt the requirements in [§16](#16-light-dark-forced-colors-and-high-contrast-behavior) (`KBDL-A11Y-011`) | Fills a genuine gap explicitly excluded from KBDL-004's theme approval; framework-neutral, does not prescribe CSS | No forced-colors policy at all (rejected — leaves users of this OS/browser feature unsupported) | Requires testing light/dark/forced-colors as three separate cases, an added QA cost | This is itself the accessibility deliverable | Not applicable | Not applicable | Does not reopen any approved theme mapping; adds a parallel, independent presentation mode | Negligible | None | `KBDL-A11Y-011` | Item 2 only — does not approve any specific palette or CSS mechanism, policy only |
| 3 | Preferred accessibility testing matrix | Adopt a defined set of screen-reader/browser pairings to test once an implementation exists (`KBDL-A11Y-035`) | Gives future implementation work a concrete, repeatable testing target | No defined matrix (rejected — ad hoc testing risks inconsistent coverage) | Matrix will need periodic revision as products update | Ensures testing actually covers real assistive-technology combinations | Not applicable | Not applicable | Not applicable | Not applicable | None | `KBDL-A11Y-035` | Item 3 only — testing-process guidance only, not a conformance claim |

### 49.3 Unresolved or Not Approval-Ready

- **Exact forced-colors CSS mechanism** — implementation-layer, out of
  scope.
- **Exact screen-reader/browser version pairings** for the preferred
  testing matrix (item 3 above proposes that a matrix should exist;
  the specific product/version list is not proposed here).
- **Any additional quantitative motion-safety limit beyond WCAG's flash
  threshold** — not proposed; KBDL-005's qualitative list plus WCAG's
  numeric threshold are considered sufficient at this stage.
- **Component-level accessibility variants** — deferred to the
  Components module (`CMP`).

**Exact scope of a future approval:** an `APPROVE` response to
[§49.2](#492-recommended-decisions--ready-for-approval) would authorize
exactly items 1–3 above — the preferred enhanced target size, the
forced-colors/high-contrast policy, and the preferred testing matrix. It
would **not** approve any [§49.3](#493-unresolved-or-not-approval-ready)
item, any component-specific value, or any KBDL-007-or-later content. It
would not itself constitute validation of any item — see
[§48](#48-accessibility-validation-matrix).

## 50. Deferred and Unresolved Accessibility Items

- Preferred enhanced target size, forced-colors/high-contrast policy,
  and preferred testing matrix — `Recommended`, pending
  [§49.2](#492-recommended-decisions--ready-for-approval).
- Exact forced-colors CSS mechanism, exact testing-matrix product/
  version list, additional motion-safety numeric limits beyond WCAG —
  `Unresolved`/out of scope, per [§49.3](#493-unresolved-or-not-approval-ready).
- Component-level accessibility variants — `Deferred` to the Components
  module (`CMP`, KBDL-007+).
- Implementation-level validation (automated checks, keyboard/
  screen-reader/zoom/forced-colors/flash/mobile/real-device testing) —
  `Not verified`, since no implementation exists yet.

## 51. Traceability

See [traceability-matrix.md](traceability-matrix.md) for how each
`KBDL-A11Y-###` requirement traces to its blueprint origin, approval
status, validation status, and evidence, and
[decision-register.md](decision-register.md) for any decision recorded
as part of this module.
