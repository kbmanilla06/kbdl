# KBDL Motion — Validation and Conformance

Lifecycle status: `Approved` for the validation methodology and
conformance criteria (architecture) below. Validation status of the
motion module's specific claims: `Not verified` for every exact
duration, curve, distance, and pattern default (no implementation
exists yet to check against); `Not applicable` for conceptual/manual
reviews already performed and recorded as such. See
[motion/README.md §9](README.md#9-normative-requirements) for
per-requirement status.

Return to the [motion index](README.md) · [specification index](../README.md).

## 1. Motion Validation Specification

A motion pattern (or a project's implementation of it) is validated
against every item below before any claim may be marked `Verified`:

- **Purpose completeness** — every documented pattern cites a purpose
  from [foundations.md §1](foundations.md#1-motion-purposes)
  (`KBDL-MOT-001`).
- **Category completeness** — every category in
  [foundations.md §2](foundations.md#2-motion-categories) documents
  purpose, intensity, transformations, interruption, reduced-motion,
  performance, and profile guidance (`KBDL-MOT-004`).
- **Hierarchy compliance** — no pattern exceeds its assigned hierarchy
  level without the required review (`KBDL-MOT-005`); Exceptional-level
  use has recorded project-owner approval.
- **Intensity assessment** — intensity is assessed using the full
  multi-factor model, not duration alone (`KBDL-MOT-006`).
- **Timing and duration compliance** — durations fall within their
  documented class range, once approved (`KBDL-MOT-007`, `KBDL-MOT-008`).
- **Easing compliance** — curves match their documented semantic
  category and have been reviewed for interruption/reversal
  (`KBDL-MOT-009`).
- **Spatial-movement compliance** — movement direction, distance, and
  scale stay within the documented constraints (`KBDL-MOT-010`).
- **Choreography compliance** — sequencing reflects hierarchy and
  cumulative delay stays bounded (`KBDL-MOT-011`).
- **Entrance/exit compliance** — exits are equal to or faster than
  entrances; destructive actions do not rely on exit animation as
  confirmation (`KBDL-MOT-012`).
- **Navigation continuity** — motion reinforces structure without
  delaying required content (`KBDL-MOT-013`).
- **Loading/progress truthfulness** — motion does not imply false
  progress and stops on completion (`KBDL-MOT-014`).
- **Direct-manipulation equivalence** — a non-gesture alternative exists
  for every gesture-only interaction (`KBDL-MOT-015`).
- **Attention boundedness** — attention motion stops, does not steal
  focus, and is not the sole indicator (`KBDL-MOT-016`).
- **Ambient boundedness** — ambient motion is pausable, avoidable, and
  reading-safe (`KBDL-MOT-017`).
- **Scroll-linked accessibility** — essential content does not depend on
  scroll-triggered animation (`KBDL-MOT-018`).
- **Media compliance** — no autoplay with sound; pause/stop available
  (`KBDL-MOT-019`).
- **Theme-transition compliance** — the transition does not block
  interaction, flash, or drop below contrast thresholds (`KBDL-MOT-020`).
- **Interruption/recovery validity** — motion resolves to a valid state
  after interruption, cancellation, or replacement (`KBDL-MOT-021`).
- **Reduced-motion/no-motion parity** — every major pattern has a
  documented and functionally equivalent reduced- and no-motion behavior
  (`KBDL-MOT-022`).
- **Motion-safety compliance** — no hazardous pattern from
  [accessibility-performance.md §2](accessibility-performance.md#2-motion-safety)
  is present (`KBDL-MOT-023`).
- **Performance compliance** — motion does not block input; performance
  claims are backed by measurement, not manual review alone
  (`KBDL-MOT-024`).
- **Input-method equivalence** — touch, pointer, keyboard, and
  screen-reader users receive equivalent meaning (`KBDL-MOT-025`).
- **Profile consistency** — Showcase, Precision, and Flow share one
  architecture, differing only in emphasis (`KBDL-MOT-026`).

## 2. Numerical Consistency Review (performed)

Manual review of every exact value proposed in this module confirms:

- Every duration and distance value has a stated semantic purpose (see
  [timing-easing.md §2](timing-easing.md#2-duration-recommendations)).
- Duration ranges do not overlap ambiguously without explanation —
  adjacent classes (e.g., Fast and Standard) have distinct, explained
  purposes even where their numeric ranges are close.
- Exit durations are documented as equal to or shorter than their
  paired entrance durations throughout [patterns.md](patterns.md) and
  [timing-easing.md](timing-easing.md).
- Stagger recommendations are qualitative and explicitly bounded (total
  cumulative delay), avoiding an unbounded per-item multiplier (see
  [foundations.md §5](foundations.md#5-choreography-and-sequencing)).
- Theme-transition values (150–250ms, Standard easing) are compatible
  with the already-`Approved` KBDL-004 requirement that no intermediate
  frame drop below the applicable contrast threshold — verified
  conceptually against the worked example in
  [patterns.md §8](patterns.md#8-theme-transition-motion), not against a
  live implementation.
- Reduced-motion replacements are explicitly defined for every pattern
  in the [parity matrix](accessibility-performance.md#14-per-category-parity-matrix)
  and the [motion pattern matrix](patterns.md#12-motion-pattern-matrix).
- No exact value in this module is marked `Approved` — every exact
  duration, curve, distance, scale, stagger, or repetition value is
  `Recommended`, pending
  [motion/README.md §10](README.md#10-motion-decision-packet).
- No implementation-level performance claim is marked `Verified` — this
  module contains no implementation to measure.

**Result:** Passed — no numerical inconsistency found; no value
incorrectly marked `Approved` or `Verified`.

## 3. Reduced-Motion Matrix Review (performed)

Verified against [accessibility-performance.md §1.4](accessibility-performance.md#14-per-category-parity-matrix):

- Every one of the ten motion categories has a documented reduced-motion
  and no-motion behavior.
- Functionality and state meaning remain present in every reduced/
  no-motion row (confirmed by the "Meaning preserved" column).
- Large spatial movement, parallax, and ambient motion are removed or
  simplified in every applicable row.
- Input acknowledgment remains visible in every row (as an instant state
  change where motion is removed).
- No reduced-motion variant introduces flashing or other unsafe
  behavior — every reduced/no-motion behavior is an instant or static
  substitute, never a faster or more abrupt animated one.

**Result:** Passed.

## 4. Pattern Coverage Review (performed)

Verified that the [motion pattern matrix](patterns.md#12-motion-pattern-matrix)
covers: immediate feedback, state transitions, navigation, content
insertion and removal, loading, progress, errors, success, attention,
direct manipulation, theme transition, ambient motion, scroll-linked
motion, and media motion. All fourteen are present as distinct rows or
directly-related rows (e.g., "content insertion"/"content removal" as
paired rows).

**Result:** Passed.

## 5. Items Not Verified

The following are explicitly `Not verified` and must not be treated as
passing until an implementation exists and is measured:

- Every exact duration, distance, scale, stagger interval, and
  repetition count in [timing-easing.md](timing-easing.md) and
  [foundations.md](foundations.md) — conceptually reviewed for internal
  consistency ([§2](#2-numerical-consistency-review-performed)), but not
  implementation-tested.
- Every exact easing curve in
  [timing-easing.md §3](timing-easing.md#3-easing-architecture) —
  conceptually reviewed for interruption/reversal behavior, not tested
  against a live animation implementation.
- The theme-transition worked example's contrast claim during motion —
  the underlying static contrast values are `Verified` (per
  [themes/validation.md §3](../themes/validation.md#3-consolidated-contrast-evidence)),
  but no mid-transition frame has been rendered and measured.
- All performance claims (frame rate, input latency, layout-shift
  avoidance) — no implementation exists to measure.
- All mobile/input-method equivalence claims — no implementation exists
  to test across touch, pointer, keyboard, and screen readers.
- The motion-safety prohibitions — reviewed conceptually against the
  qualitative list in
  [accessibility-performance.md §2](accessibility-performance.md#2-motion-safety);
  exact quantitative thresholds (e.g., flash frequency) are explicitly
  `Deferred` to KBDL-006.
- Cross-profile motion-architecture consistency — reviewable only once
  the project-profiles module (`PRO`) exists.

## 6. Manual Documentation Reviews Performed

- Heading-hierarchy review — passed.
- Relative-link and anchor validation — passed (see the implementation
  report's link/anchor checker results).
- Markdown-table validation — passed.
- Empty-section and placeholder scan — passed, none found.
- Duplicate requirement-ID and decision-ID scan — passed, none found.
- Requirement-ID format review — passed, all `KBDL-MOT-###` IDs follow
  [conventions.md §2](../conventions.md#2-requirement-identification).
- Lifecycle- and validation-status review — **initially failed, then
  corrected under KBDL-005-R1.** The original commit (`ea32ce3`) bundled
  several new `Recommended` policy defaults (the entrance-versus-exit
  duration relationship, the attention repetition default, detailed
  ambient- and scroll-linked-motion boundaries, the reduced-motion
  substitution matrix, the motion-token naming architecture, and
  profile-level intensity adjustments) inside `Approved` sections
  without an independent lifecycle record, and referenced the wrong
  requirement ID (`KBDL-MOT-009`, easing) for intensity defaults instead
  of `KBDL-MOT-006`. KBDL-005-R1 separated these into `KBDL-MOT-028`
  through `KBDL-MOT-034`, fixed the incorrect reference, and rechecked
  every section header and status line in this module; re-review now
  passes — every `Recommended` value is clearly distinguished from
  `Approved` architecture throughout this module.
- Motion-term consistency review — passed; terms from
  [motion/README.md §2](README.md#2-motion-terminology) are used
  consistently across all motion documents.
- Scope-compliance review — passed; no component anatomy, Figma assets,
  CSS/JSON tokens, animation libraries, or KBDL-006-plus content found
  (see the implementation report's scope-search results).
- Decision-packet coverage review — **initially failed, then corrected
  under KBDL-005-R2.** The thirteen-item packet committed under
  KBDL-005-R1 omitted two `Recommended` architecture requirements ready
  for approval — `KBDL-MOT-006` (multi-factor motion-intensity model)
  and `KBDL-MOT-013` (navigation-motion architecture) — neither of which
  had a decision row. KBDL-005-R2 added packet items 14 and 15 for these
  two requirements and added the
  [coverage table](README.md#1021-recommended-requirement-coverage) in
  [motion/README.md §10.2.1](README.md#1021-recommended-requirement-coverage).
  Re-review now confirms: all sixteen `Recommended`
  `KBDL-MOT-###` requirements (`005`–`011`, `013`, `020`, `028`–`034`)
  map to exactly one of the fifteen approval decisions; no lifecycle or
  validation status was changed; no motion policy (duration, curve,
  movement range, hierarchy level, safety behavior, reduced-motion
  behavior, or profile recommendation) was changed.

## 7. Traceability

See [traceability-matrix.md](../traceability-matrix.md) for how each
`KBDL-MOT-###` requirement traces to its blueprint origin, approval
status, validation status, and evidence, and
[decision-register.md](../decision-register.md) for any decision recorded
as part of this module.
