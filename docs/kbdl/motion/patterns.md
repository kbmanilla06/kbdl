# KBDL Motion — Patterns, Profiles, and Conformance

**Updated under KBDL-005-A1.** Lifecycle status: `Approved` throughout —
see each section's own status line and
[motion/README.md §9](README.md#9-normative-requirements) for exact
`KBDL-MOT-###` wording. Sections restating an already-`Approved`
principle or KBDL-004 rule were `Approved` from the start; sections
introducing new KBDL-005 policy (exact durations, distances, repetition
counts) are now `Approved` per the project owner's approval of
[KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved)
via [motion/README.md §10](README.md#10-motion-decision-packet). No
implementation behavior is thereby `Verified` — see
[validation.md](validation.md).

Return to the [motion index](README.md) · [specification index](../README.md).

## 1. Navigation and Spatial Continuity

Status: `Approved` (`KBDL-MOT-013`, per
[KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved),
decision packet item 15), `User-provided` provenance, `Not verified`.

Conceptual guidance for route changes, step-based flows, drill-down and
back, side panels, tabs/views, master-detail layouts, modal transitions,
full-screen transitions, shared visual elements, scroll-position
continuity, and focus continuity.

**Requirements:**

- Navigation motion must reinforce information structure (e.g., forward
  moves one direction, back moves the other).
- Back navigation should not feel directionally unrelated to forward
  navigation.
- Motion must not obscure the destination — the user must be able to
  identify where they landed before the transition fully completes.
- A transition must not delay access to required content beyond the
  Standard timing class (see [timing-easing.md §1](timing-easing.md#1-timing-architecture)).
- Browser navigation (back/forward) must remain predictable and must not
  be hijacked by custom transition logic.
- Focus location must remain understandable after navigation — either
  preserved contextually or deliberately reset to a sensible landmark.
- Reduced motion may replace movement with instant change or a short
  crossfade.
- Full-page cinematic transitions must be exceptional (Level 4, see
  [foundations.md §3](foundations.md#3-motion-hierarchy)), never a
  default navigation pattern.

Detailed navigation component behavior is now defined in
[components-core.md §24](../components-core.md#24-navigation-components)
(KBDL-007); this section is not restated or reopened there.

## 2. Loading and Progress

Status: `Approved` (`KBDL-MOT-014`, directly restating Technical
Utility's visible-progress and error-prevention qualities), `Confirmed`
provenance, `Not verified`.

Covers indeterminate loading, determinate progress, skeleton/placeholder
behavior, content refresh, background synchronization, optimistic
update, delayed operation, failure and retry, and completion transition.

**Requirements:**

- Loading motion must not imply progress that is not occurring.
- Determinate operations should show real progress where available,
  never a fabricated estimate presented as exact.
- Indeterminate motion must not run indefinitely without context (pair
  with a label or timeout-driven fallback state for long operations).
- Repeated loading animation must remain low intensity (Functional
  level).
- Motion must stop the moment loading ends — no lingering animation
  after the underlying operation completes.
- Skeleton/placeholder treatments must not create excessive shimmer or
  motion; a low-contrast, low-frequency treatment is sufficient.
- Reduced-motion mode must support static or minimally-changing
  alternatives (e.g., a static placeholder shape instead of a shimmering
  one).
- Progress must remain understandable without motion (a percentage or
  step count, not only a moving bar).
- Failure must replace loading motion rather than animate indefinitely —
  a failed operation shows a static failure state, not a stalled loading
  animation.

Skeleton component anatomy is deferred to the Components module.

## 3. Direct Manipulation and Gesture Response

Status: `Approved` (`KBDL-MOT-015`, directly restating the accessibility
requirement for a non-gesture equivalent), `Confirmed` provenance, `Not
verified`.

Covers drag, swipe, resize, reorder, scrub, pull, pinch/zoom (where
applicable), press-and-hold, and pointer tracking.

**Requirements:**

- Motion should track input directly — position/size follows the
  pointer or touch point without perceptible lag.
- Release should settle predictably (see the Spring-like easing
  category, [timing-easing.md §3](timing-easing.md#3-easing-architecture)).
- Cancel and reversal must be supported where the interaction permits
  (e.g., dragging back to the origin cancels a reorder or dismiss).
- Target position must remain understandable throughout the
  manipulation, not only at the end.
- Overshoot must be controlled — small and damped, never large enough to
  make a target feel unstable.
- Gesture-only behavior must have a keyboard or control alternative
  (e.g., a reorder achievable via keyboard shortcuts or a menu action,
  not only by dragging).
- Reduced motion must not remove required direct feedback — direct
  tracking during manipulation is functional, not decorative, and is
  preserved even under reduced motion; only the release "settle"
  flourish simplifies.
- Touch and pointer behavior should preserve equivalent meaning even
  where the exact gesture differs.
- System gestures and browser gestures (e.g., browser back-swipe) must
  not be unnecessarily overridden.

Component-specific gesture implementation is deferred to the Components
module.

## 4. Attention Motion

Status: `Approved` (`KBDL-MOT-016`, directly restating the locked
component-state-clarity rule and Accessibility by Default), `Confirmed`
provenance, `Not verified`. The exact repetition limit below is a
separate requirement, `KBDL-MOT-029`, `Approved` per
[KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved).

Covers new notification, changed value, validation error, success
acknowledgment, warning, critical alert, background update, incoming
content, and unread state.

**Requirements:**

- Motion must not be the only indicator of an attention-worthy state —
  pair with color, icon, label, or badge.
- Attention motion must stop, never repeat indefinitely.
- Repetition must be bounded — **limit: 2–3 repetitions**, then hold a
  static emphasized state (`Approved` per
  [motion/README.md §10.2](README.md#102-approved-decisions-kbdl-005-a1)
  item 7).
- Critical alerts must use stable, visible static information as the
  primary cue, with motion as a secondary reinforcement only.
- Error motion must not shame, startle, or repeatedly shake the
  interface.
- Large screen flashes are prohibited (see
  [accessibility-performance.md §2](accessibility-performance.md#2-motion-safety)).
- Attention motion must not steal keyboard focus.
- Reduced-motion alternatives must use static emphasis (color, icon,
  contrast, or text) instead of motion.
- Multiple simultaneous attention cues must be prioritized — the most
  urgent plays its motion; lower-priority cues use static emphasis only,
  to avoid competing signals.

## 5. Ambient and Continuous Motion

Status: `Approved` (`KBDL-MOT-017`, directly restating the locked Motion
Purpose rule and the already-`Approved` reduced-motion requirement
`KBDL-THM-012a`), `Confirmed` provenance, `Not verified`. The detailed
boundaries below are a separate requirement, `KBDL-MOT-030`, `Approved`
per [KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved).

Covers decorative background movement, floating elements, slowly
changing gradients, animated illustrations, live data indicators, loops,
and video-like decorative media.

**Requirements:**

- Ambient motion must never be required for comprehension.
- Continuous motion must be rare and bounded — reserved for genuinely
  decorative, non-essential contexts.
- The user must be able to pause or avoid significant non-essential
  continuous motion (a documented pause mechanism, not necessarily a
  visible on/off control for every instance, but never impossible to
  avoid).
- Continuous movement near reading content must be avoided — ambient
  motion pauses or stops while the user is reading nearby text.
- Ambient motion must stop or simplify to a static frame under
  reduced-motion preference.
- Background motion must not compete with interaction — it must never
  overlay or visually interfere with active controls.
- Lower-performance devices must support a static fallback.
- Precision should use ambient motion exceptionally, if at all.
- Showcase may use more ambient motion but never during sustained
  reading.
- Flow should use ambient motion conservatively.

Animated-gradient implementation remains deferred to a later,
implementation-facing step.

## 6. Scroll-Linked Motion

Status: `Approved` (`KBDL-MOT-018`, directly restating the accessibility
requirement that content remain accessible without script/animation, and
the reduced-motion requirement), `Confirmed` provenance, `Not verified`.
The detailed boundaries below (bounded parallax, no replay on small
scroll changes) are a separate requirement, `KBDL-MOT-031`, `Approved`
per [KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved).

Covers reveal-on-entry, progress indicators, sticky transformations,
parallax, scrollytelling, section transitions, and media progression.

**Requirements:**

- Essential content must not depend on scroll-triggered animation to
  become visible or usable.
- Content must remain accessible when scripting or animation is
  unavailable.
- Motion must not repeatedly replay during small scroll changes (e.g.,
  scrolling a few pixels back and forth must not re-trigger a reveal
  animation each time).
- Large parallax movement must be avoided; bounded, subtle parallax is
  the ceiling, not the default.
- Scroll-linked motion must not trap or override normal scrolling
  behavior.
- Reading order must remain intact regardless of scroll-triggered
  visual effects.
- Reduced motion must disable or significantly simplify parallax and
  other scroll-linked transforms.
- Progress indicators tied to scroll must reflect real scroll position,
  not an approximation.
- Sticky transformations must preserve focus and content visibility —
  a sticky element must not obscure the content a keyboard or
  screen-reader user is currently interacting with.
- Scroll-triggered global theme switching remains prohibited unless
  separately approved (no such approval exists in this module).

Review criteria (rather than fixed implementation thresholds, since
evidence is insufficient to set exact numbers): does the reveal
trigger reliably once per relevant scroll direction change, not on
every pixel of movement; does the parallax offset stay small relative
to the element's own size; does disabling JavaScript/animation still
leave all essential content reachable.

## 7. Media Motion

Status: `Approved` (`KBDL-MOT-019`, directly restating WCAG 2.2 AA's
autoplay-with-sound prohibition and pause/stop requirement, already
adopted under `KBDL-DEC-010`), `Confirmed` provenance, `Not verified`.

Covers autoplay video, background video, animated illustrations,
GIF-like media, product demonstrations, portfolio reels, data playback,
media controls, and captions/transcripts.

**Requirements:**

- Essential information conveyed by media must have a static or textual
  equivalent.
- Autoplay with sound is prohibited.
- Significant autoplay motion must support pause or stop.
- Reduced-motion preference should prevent non-essential autoplay where
  feasible.
- Media must not obscure navigation or focus.
- Portfolio media (Showcase) may be prominent but must remain
  user-controlled.
- Dashboard media (Precision) must remain subordinate to tasks.
- Flow media must support comprehension and trust, never distract from
  the guided path.
- Performance fallbacks (a static poster frame) must be documented for
  constrained devices.
- Captions, transcripts, and accessible names remain required where
  applicable, per existing WCAG 2.2 AA baseline.

Detailed media-component implementation remains out of scope.

## 8. Theme-Transition Motion

Status: `Approved` (`KBDL-MOT-020`, per
[KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved))
for the exact duration/easing recommendation below; the underlying
non-blocking, readable, focus-preserving requirements were already
`Approved` (`KBDL-THM-012`, `KBDL-THM-012a`) and are unaffected by this
section's status either way.

Builds on the approved conceptual rules in
[themes/adaptation.md §7](../themes/adaptation.md#7-theme-transition-guidance).

**Recommended concrete values:**

- **Duration class:** Standard, 150–250ms (see
  [timing-easing.md §2](timing-easing.md#2-duration-recommendations)).
- **Easing category:** Standard (balanced ease-in-out; see
  [timing-easing.md §3](timing-easing.md#3-easing-architecture)) — chosen
  over Enter/Exit curves because a theme switch has no directional
  arrival/departure to communicate.
- **Properties that may transition:** surface background colors, border
  colors, and text colors (a simultaneous crossfade, not sequenced).
- **Properties that change immediately:** the Focus indicator's presence
  and position (its color may transition; visibility never lapses).
- **Properties that must not animate:** anything already respecting a
  reduced-motion preference — for those users, every change is instant,
  per the already-`Approved` `KBDL-THM-012a`.
- **Images and media:** update immediately alongside the color
  transition — a theme-dependent image swap (if any) is not animated
  separately.
- **Charts (conceptual):** all chart elements update together within the
  same transition window, never piecemeal, consistent with
  `themes/adaptation.md §7.1`'s coherent-update requirement.
- **Focus and selection:** remain visible throughout, unaffected by the
  crossfade.
- **Rapid repeated toggling:** resolves to the most recently requested
  theme; in-progress transitions are cancelled and restarted toward the
  new target, never queued.
- **Interruption:** always interruptible; a new theme request cancels
  the current transition immediately.
- **Reduced-motion behavior:** instant switch (already `Approved`,
  `KBDL-THM-012a`), unaffected by this section's status.
- **Initial-render fallback:** if the persisted theme preference is not
  yet known at first paint, the initial render must not intentionally
  show a known-incorrect theme; render deferred or use the
  system-preference fallback per
  [themes/README.md §5](../themes/README.md#5-theme-selection-precedence),
  never animate into the correct theme after a visible incorrect flash.

**Requirements:**

- Theme change must not block interaction.
- Theme change must not create a large flash — the Standard crossfade
  duration and simultaneous (not sequenced) property transition are
  chosen specifically to avoid this.
- Text must remain readable throughout — no intermediate frame drops
  below the applicable contrast threshold (conceptually verified against
  the worked example below; not implementation-tested).
- Semantic states (status colors, selection) must not disappear during
  the transition.
- Focus indicators must remain visible throughout.
- Reduced motion may use an instant switch.
- Initial rendering must not intentionally show a known-incorrect theme.

This does not reopen any approved KBDL-004 theme mapping — it only
supplies the timing and easing that KBDL-004 explicitly deferred.

## 9. Interruption, Reversal, and Recovery

Status: `Approved` (`KBDL-MOT-021`, directly restating safety/
correctness and state-comprehension priorities), `Confirmed` provenance,
`Not verified`.

Covers user interruption, system interruption, rapid repeated input,
reversal, cancellation, replacement by a newer state, navigation away,
error during motion, and reduced-performance fallback.

**Requirements:**

- Motion must resolve to a valid state, never an intermediate, broken,
  or ambiguous one.
- Input must not be ignored merely because motion is in progress —
  new input either interrupts, cancels, or queues predictably; it is
  never silently dropped.
- Rapid repeated input must not queue excessive animation — later input
  supersedes earlier, incomplete requests rather than stacking them.
- Reversal should begin from the current visual state where practical,
  not restart from the original starting point.
- Interrupted exits must not leave inaccessible or focusable remnants —
  a partially-exited element is either fully removed or fully restored,
  never left in between as a dead, unreachable artifact.
- Interrupted loading must not continue visually after the underlying
  operation is cancelled.
- System state is authoritative over an unfinished animation — if the
  real state and the animated state disagree (e.g., due to a race), the
  real state wins and the visual is corrected immediately.
- Recovery from an error must not require animation completion — a user
  can act on the real state immediately, regardless of whether a
  recovery animation has finished playing.

## 10. Profile-Level Motion Interpretation

Status: `Approved` (`KBDL-MOT-026`, directly restating `KBDL-PRN-007` —
profiles must share one motion architecture, adjusting only emphasis).
The specific per-profile "may emphasize"/"must preserve" adjustments
below are a separate requirement, `KBDL-MOT-034`, `Approved` per
[KBDL-DEC-014](../decision-register.md#kbdl-dec-014--kbdl-005-motion-decisions-approved).

### 10.1 Showcase

May emphasize: more expressive reveals; editorial sequencing; richer
media motion; selective shared-element continuity; controlled ambient
moments; stronger branded choreography.

Must preserve: reading stability; user control; reduced-motion parity;
fast navigation access; bounded continuous motion; stable focus.

### 10.2 Precision

May emphasize: immediate feedback; short state transitions; efficient
data updates; predictable navigation; minimal ambient motion; compact
choreography.

Must preserve: scanning speed; repeated-workflow efficiency; data
stability; state clarity; low visual noise; performance.

### 10.3 Flow

May emphasize: approachable transitions; reassuring feedback; clear
progress; gentle spatial continuity; balanced expressive moments.

Must preserve: predictable progression; trust; error recovery; mobile
clarity; immediate action acknowledgment; motion safety.

### 10.4 Shared constraint

Profiles must not define separate timing or easing architectures unless
an approved exception exists (none exists at this time); all three share
the [timing-easing.md](timing-easing.md) architecture, varying only
which named class or category is used and how often.

## 11. Motion Conformance Rules

For every motion category (see [foundations.md §2](foundations.md#2-motion-categories)):
required purpose, permitted transformations, recommended intensity,
timing class, easing category, interruption behavior, reduced-motion
behavior, no-motion fallback, profile considerations, performance
considerations, validation questions, and prohibited behavior are
defined in that section and cross-referenced from
[§12](#12-motion-pattern-matrix) below.

### 11.1 Conforming examples

1. **Showcase, press feedback.** A portfolio project card scales down
   2% and its shadow softens over 100ms (Immediate/Responsive) on press,
   returning on release. *Conforms:* Functional intensity, serves
   Acknowledge Input, reduced motion reduces to an instant color-state
   change.
2. **Precision, data-table row selection.** A dashboard table row
   changes background color instantly with a 120ms fade
   (Immediate/Standard easing) on selection, no movement. *Conforms:*
   Low intensity appropriate to Precision, communicates state change
   without competing with data density.
3. **Flow, guided-checkout step transition.** A checkout flow crossfades
   between steps over 250ms (Standard/Standard easing), preserving the
   progress indicator unanimated. *Conforms:* Preserves spatial
   continuity and orientation; exit (departing step) and entrance
   (arriving step) overlap slightly per choreography guidance.
4. **Mobile, bottom-sheet entrance.** A mobile filter sheet slides up
   over 280ms (Standard/Standard-Enter), decelerating to a stop; back
   gesture reverses it from its current position. *Conforms:* Direction
   matches structural meaning (from off-screen below, to on-screen);
   reversal is supported from any point.
5. **Keyboard interaction, focus-visible transition.** Tabbing to a
   button shows the focus ring with no transition delay (Instant).
   *Conforms:* Focus visibility must never be delayed by decorative
   easing.
6. **Reduced motion, modal entrance.** With reduced motion enabled, a
   modal appears instantly with no scale or slide, and its focus moves
   to the modal's heading immediately. *Conforms:* Full functional parity
   preserved with zero motion.
7. **Loading, determinate progress.** A file-upload progress bar fills
   in exact proportion to bytes transferred, using Linear easing, with
   no artificial minimum-display duration. *Conforms:* Truthful,
   understandable without relying on motion character.
8. **Theme transition, light to dark.** Toggling dark mode crossfades
   surface, border, and text colors together over 200ms (Standard/
   Standard easing); focus ring remains visible throughout; a second
   toggle mid-transition cancels and reverses cleanly. *Conforms:*
   Matches [§8](#8-theme-transition-motion) exactly.

### 11.2 Non-conforming examples

1. **Showcase, ambient motion during reading.** A background gradient
   continues animating at full amplitude while the user reads a long
   article. *Violates:* [§5](#5-ambient-and-continuous-motion) — ambient
   motion must pause near sustained reading content.
2. **Precision, animated row reorder for 200 rows.** Every row
   individually animates position on a large sort operation. *Violates:*
   [foundations.md §5](foundations.md#5-choreography-and-sequencing) —
   large lists must not animate every item individually by default.
3. **Flow, blocking entrance before required action.** A guided flow's
   "Continue" button is not clickable until a 600ms entrance animation
   finishes. *Violates:* [timing-easing.md §1](timing-easing.md#1-timing-architecture)
   — required interaction must not wait for decorative motion.
4. **Mobile, large off-screen parallax hero.** A landing hero's
   background image moves 40% of viewport height during scroll on a
   mobile device. *Violates:* [§6](#6-scroll-linked-motion) — large
   parallax must be avoided, especially on constrained viewports.
5. **Keyboard interaction, focus stolen by attention motion.** A
   notification badge's pulse animation moves keyboard focus to itself
   while the user is filling a form elsewhere. *Violates:*
   [§4](#4-attention-motion) — attention motion must not steal keyboard
   focus.
6. **Reduced motion, parallax not disabled.** A user enables reduced
   motion, but the scroll-linked parallax hero still moves at full
   amplitude. *Violates:* [§6](#6-scroll-linked-motion) and
   `KBDL-MOT-018` — reduced motion must disable or simplify parallax.
7. **Loading, indeterminate spinner after completion.** A loading
   spinner continues animating for 500ms after the underlying data has
   already arrived and rendered. *Violates:* [§2](#2-loading-and-progress)
   — motion must stop the moment loading ends.
8. **Navigation, disorienting direction.** Forward navigation slides
   content in from the right; pressing back also slides new content in
   from the right instead of the left. *Violates:* [§1](#1-navigation-and-spatial-continuity)
   — back navigation must not feel directionally unrelated to forward.
9. **Direct manipulation, no keyboard alternative.** A reorderable list
   can only be reordered by dragging, with no keyboard-accessible
   alternative. *Violates:* [§3](#3-direct-manipulation-and-gesture-response)
   — gesture-only behavior must have a keyboard or control alternative.
10. **Attention motion, indefinite repetition.** An unread-message badge
    pulses continuously every second until the user manually dismisses
    it, with no bound. *Violates:* [§4](#4-attention-motion) — repetition
    must be bounded, then hold a static state.
11. **Theme transition, sequenced property animation.** Surface color
    transitions over 200ms, but text color does not begin transitioning
    until the surface finishes, creating a visible low-contrast gap.
    *Violates:* [§8](#8-theme-transition-motion) — properties must
    transition simultaneously, and no intermediate frame may drop below
    the applicable contrast threshold.
12. **Ambient motion, media autoplay with sound.** A portfolio reel
    autoplays a video with audio on page load. *Violates:*
    [§7](#7-media-motion) and `KBDL-MOT-019` — autoplay with sound is
    prohibited.

## 12. Motion Pattern Matrix

| Pattern | Purpose | Default level | Duration class | Easing class | Permitted transformations | Interruption behavior | Reduced-motion equivalent | No-motion fallback | Profile adjustments | Future component dependency | Lifecycle | Validation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Press acknowledgment | Acknowledge input | Functional | Immediate | Responsive | Small scale/opacity | Always interruptible | Instant | Instant | Minimal variation | Components (action) | Recommended | Not applicable |
| Selection change | Communicate state change | Functional | Immediate–Fast | Standard | Color/opacity change | Re-triggerable | Instant | Instant | Minimal variation | Components (form/data) | Recommended | Not applicable |
| Expand and collapse | Reveal or conceal content | Functional–Supportive | Fast–Standard | Standard-Enter/Exit | Height/clip, opacity | Interruptible, reversible mid-animation | Instant show/hide | Instant | Precision favors Fast; Showcase may use Standard | Components (surfaces) | Recommended | Not applicable |
| Surface entrance | Reveal content, establish relationship | Supportive | Standard | Standard-Enter | Opacity, small translate/scale | Interruptible | Instant or short crossfade | Instant | Consistent | Components | Recommended | Not applicable |
| Surface exit | Communicate removal | Functional–Supportive | Fast–Standard (≤ entrance) | Standard-Exit | Opacity, small translate/scale | Interruptible, resolves to fully removed | Instant | Instant | Consistent | Components | Recommended | Not applicable |
| Modal entrance and exit | Reveal/conceal, establish relationship | Supportive | Standard | Standard-Enter/Exit | Opacity, scale, backdrop | Interruptible; exit ≤ entrance duration | Instant | Instant | Consistent | Components (overlay) | Recommended | Not applicable |
| Navigation forward and back | Preserve spatial continuity | Supportive | Standard | Standard-Enter/Exit (directional) | Directional translate, crossfade | New navigation cancels prior | Instant or short crossfade | Instant | Precision favors instant/crossfade | Components (navigation), RSP | Recommended | Not applicable |
| Content insertion | Communicate content change | Functional–Supportive | Fast–Standard | Enter | Opacity, height | Superseding update resolves first | Instant | Instant | Precision restrained; Showcase moderate | Components (data display) | Recommended | Not applicable |
| Content removal | Communicate content change | Functional–Supportive | Fast (≤ insertion) | Exit | Opacity, height | Superseding update resolves first | Instant | Instant | Same as insertion | Components | Recommended | Not applicable |
| Reorder | Communicate content change, preserve identity | Supportive | Standard | Standard | Position interpolation (bounded count) | Cancellable mid-reorder | Instant | Instant | Precision limits count; Showcase may allow more | Components | Recommended | Not applicable |
| Loading | Communicate progress | Functional | Continuous (bounded) | Linear | Low-intensity indeterminate motion | Stops immediately on completion/cancel | Static/textual | Static | Consistent | Components (feedback) | Approved | Not verified |
| Determinate progress | Communicate progress | Functional | Matches operation | Linear | Fill proportional to real progress | Reflects real state | Static percentage/text | Static | Consistent | Components | Approved | Not verified |
| Success | Confirm completion | Functional–Supportive | Fast–Standard | Standard | Icon/color reveal | Not interrupted once shown | Static icon/label | Static | Consistent | Components | Approved | Not verified |
| Error | Communicate error/recovery | Functional–Supportive | Fast–Standard | Standard | Static emphasis, no shake | Re-triggerable on retry | Static emphasis | Static | Consistent | Components | Approved | Not verified |
| Warning | Communicate error/recovery | Functional | Fast | Standard | Static emphasis | Re-triggerable | Static emphasis | Static | Consistent | Components | Approved | Not verified |
| Drag and drop | Acknowledge input, communicate state change | Functional (track)–Supportive (settle) | Direct/Responsive settle | Direct manipulation / Spring-like | Position tracking, bounded settle | Cancellable mid-drag | Tracking preserved; settle simplified | Instant drop | Consistent | Components, RSP | Approved | Not verified |
| Theme transition | Communicate state change (theme) | Functional | Standard | Standard | Simultaneous color crossfade | Rapid toggles resolve to latest | Instant (Approved, `KBDL-THM-012a`) | Instant | Consistent (`KBDL-THM-006`) | None (this module) | Recommended | Not applicable |
| Notification attention | Direct attention | Functional–Supportive | Attention cue (400–600ms × bounded reps) | Standard | Bounded-repetition emphasis | Stops on interaction | Static emphasis | Static | Consistent | Components (feedback) | Approved | Not verified |
| Ambient loop | Express brand character, delight | Functional–Supportive (never higher) | Continuous (4–8s cycle) | Linear or gentle ease | Slow, low-contrast movement | Pauses near reading content, always under reduced motion | Static frame | Static | Showcase primary; Precision/Flow rare-to-none | None | Approved (architecture); Recommended (exact cycle length) | Not applicable |
| Scroll reveal | Reveal content, establish relationship | Supportive | Standard | Standard-Enter | Opacity, small translate | Does not replay on small scroll changes | Instant reveal | Static (already visible) | Showcase primary | Components, RSP | Approved (architecture); Recommended (exact thresholds) | Not applicable |
| Media autoplay | Express brand character (Showcase), support comprehension (Flow) | Functional–Supportive | Continuous (user/context-bound) | Not applicable (media playback, not UI easing) | Muted playback only, pause/stop control | Pauses on navigation away | Suppressed where feasible | Static poster frame | Showcase primary; Precision minimal; Flow supportive only | Foundations (media strategy), Components | Approved | Not verified |

## 13. Traceability

See [motion/README.md §9](README.md#9-normative-requirements) for the
full `KBDL-MOT-###` list and [traceability-matrix.md](../traceability-matrix.md)
for status and evidence.
