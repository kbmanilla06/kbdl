# KBDL Components — Core Action, Form, and Navigation

Lifecycle status: mixed. `Approved` for the requirements below that
directly restate an already-`Approved` WCAG 2.2 Level A/AA criterion,
WAI-ARIA role/state/property, or prior approved KBDL principle,
foundation, theme, motion, responsive, or accessibility rule — see
[§30](#30-normative-requirements) for exact per-requirement status.
`Recommended`/`Unresolved` for genuinely new component-level taxonomies,
variants, activation models, and dimensions — pending project-owner
approval via [§35](#35-kbdl-007-decision-packet). No `Recommended` or
`Unresolved` value in this document authorizes implementation on its
own — see [conventions.md §1.1](conventions.md#11-lifecycle--approval-status).
Assigning a `KBDL-CMP-###` ID does not grant approval or implementation
authority, per the amended convention
([conventions.md §2](conventions.md#2-requirement-identification),
[KBDL-DEC-015](decision-register.md#kbdl-dec-015--kbdl-006-remediation-and-id-governance-amendment)).

This document does not claim full WCAG conformance, screen-reader
compatibility, browser compatibility, real-device compatibility, or
forced-colors compatibility. No coded component exists yet to test
against.

Return to the [specification index](README.md).

## 1. Purpose and Scope

This document defines KBDL's framework-neutral specification for core
action, form, and navigation components: shared contract, anatomy,
states, interaction behavior, and accessibility/responsive/theme/motion
mapping. It translates approved KBDL-001 through KBDL-006 requirements
into component-level rules and adds new `KBDL-CMP-###` requirements for
genuinely new component decisions. It does not define application code,
a component library, a frontend framework, token implementation formats,
or KBDL-008 surfaces (cards, panels, overlays, dialogs, menus, toasts,
tooltips, and similar) — see [§11](#11-kbdl-008-scope-boundary).

## 2. Component Status Model

Uses KBDL's standard three-dimension model
([conventions.md §1](conventions.md#1-status-labels)). A component-level
requirement directly restating an already-adopted WCAG 2.2 criterion,
WAI-ARIA specification, or prior approved KBDL rule may be `Approved`
because that source was already adopted. A genuinely new component
taxonomy, variant set, activation model, or dimension (not dictated by
an existing approved source) remains `Recommended`, `Unresolved`, or
`Deferred` until the project owner reviews
[§35](#35-kbdl-007-decision-packet). Documentation review alone never
justifies `Verified` — that requires the stated validation method to
have actually been run against a real implementation, which does not
exist at this specification stage.

## 3. Relationship to Prior KBDL Modules

This module operationalizes: KBDL-002's design-decision hierarchy and
locked identity rules (component-state-clarity, accessibility
requirements); KBDL-003's typography, spacing, shape/depth, and
iconography foundations; KBDL-004's semantic theme roles; KBDL-005's
motion hierarchy and purpose model; KBDL-006's WCAG 2.2 AA baseline and
responsive-behavior requirements. It reopens none of these — every
foundation, theme, motion, responsive, and accessibility value already
approved remains unchanged; this module only maps them to component-level
anatomy and behavior.

## 4. Component Terminology

- **Component** — a reusable interface element with documented anatomy,
  states, and accessibility behavior (existing glossary term, extended
  here to core action/form/navigation components specifically).
- **Anatomy** — the documented structural parts making up a component.
- **Contract** — the shared set of properties (purpose, anatomy, states,
  interaction behavior, accessibility, responsive, theme, and motion
  mapping) every in-scope component must document, per
  [§6](#6-shared-component-contract).
- **Native semantics** — the accessibility semantics a host-language
  element (e.g., `button`, `a`, `input`, `select`) provides without
  additional ARIA.
- **Custom widget** — a component whose semantics are not fully provided
  by a native element and must instead follow the applicable WAI-ARIA
  role, state, property, and keyboard contract.
- **Trigger** — a control that opens, closes, or controls a separate
  surface (a disclosure, menu, or combobox popup), without itself being
  that surface.
- **Field** — a labeled input or control within a form, together with
  its supporting label, description, instructions, and validation
  message.

## 5. Native-Semantics-First Rule

Status: `Approved` (`KBDL-CMP-002`, directly restates the requirement
that native host-language semantics satisfy WCAG 2.2 SC 4.1.2 Name,
Role, Value without additional authoring effort, and the WAI-ARIA
"First Rule of ARIA Use": do not use ARIA if a native element or
attribute already has the semantics and behavior required).

**Requirements:**

- A native `button` element **must** be used for actions when native
  button semantics satisfy the need.
- A native `a` (anchor) element **must** be used for navigation.
- Native form controls (`input`, `select`, `textarea`, and their native
  attributes) **must** be used where they provide the required
  semantics and behavior.
- Native labels and field associations (e.g., a `label` associated with
  its control) **must** be used rather than a purely visual pairing.
- Native disabled and read-only behavior **must** be used where the
  host language supports it for the given control type.
- Native validation semantics **may** be used only when their behavior
  and messaging meet KBDL's error-identification and error-suggestion
  requirements ([§23](#23-form-validation-and-recovery)); native
  validation UI that does not meet those requirements must be
  supplemented or replaced.
- ARIA **must** be used only to supply semantics, states, or
  relationships a native element cannot express (e.g., `aria-expanded`
  on a disclosure trigger, `role="tablist"` for a custom tab widget).
- A custom widget **must** follow the applicable WAI-ARIA role, state,
  property, and keyboard contract in full, not a partial subset.

**Explicitly prohibited:**

- A link styled as a button when it performs an action without
  navigation.
- A button used as a link when it only navigates.
- A click handler on a non-interactive element (e.g., a `div`) without
  equivalent semantics (an appropriate role) and full keyboard behavior.
- An ARIA role that conflicts with the native semantics of the element
  it is applied to.
- Redundant or incorrect ARIA (e.g., `role="button"` on a native
  `button` element).
- A visible label that does not match or begin the component's
  accessible name, where WCAG 2.2 SC 2.5.3 Label in Name applies.

## 6. Shared Component Contract

Status: `Approved` (`KBDL-CMP-001`, a structural completeness
requirement restating [conventions.md §1](conventions.md#1-status-labels)'s
three-dimension model applied per component; the exact anatomy/variant
content documented under this contract for each component carries its
own, separately stated lifecycle status).

Every in-scope component's documentation ([§20](#20-action-components)–[§24](#24-navigation-components))
must state:

| Field | Required for |
| --- | --- |
| Purpose | All |
| Appropriate use | All |
| Inappropriate use | All |
| Semantic role or preferred native element | All |
| Required accessible name | All |
| Optional accessible description | Where applicable |
| Anatomy (required parts) | All |
| Anatomy (optional parts) | Where applicable |
| Supported variants | Where applicable |
| Supported sizes or density modes | Where applicable |
| Default state | All |
| Hover state | Pointer-capable components |
| Focus-visible state | All focusable components |
| Active/pressed state | Activatable components |
| Selected/current state | Where applicable |
| Disabled state | Where valid |
| Read-only state | Where valid |
| Loading state | Where valid |
| Invalid state | Where valid |
| Checked/unchecked/mixed state | Selection controls only |
| Expanded/collapsed state | Disclosure/trigger components only |
| Keyboard behavior | All operable components |
| Pointer and touch behavior | All operable components |
| Focus-entry behavior | All focusable components |
| Focus-exit behavior | All focusable components |
| Focus-restoration behavior | Trigger/disclosure components |
| Responsive behavior | All |
| Theme behavior | All |
| Reduced-motion behavior | Components with motion |
| No-motion behavior | Components with motion |
| Content guidance | All |
| Error behavior | Form components |
| Validation method | All |
| Lifecycle status | All |
| Provenance | All |
| Validation status | All |
| Related requirements | All |
| Known limitations | All |

A component must not document a state or field irrelevant to it (e.g.,
a link does not need a "checked" state).

## 7. Component Anatomy Model

Status: `Approved` (`KBDL-CMP-001`, part of the shared contract).

Anatomy is documented as **required parts** (the component cannot
conform without them — e.g., a button's accessible label) and
**optional parts** (may be present depending on variant — e.g., a
leading icon). Anatomy documentation states each part's semantic role,
not its visual treatment, which remains implementation-layer.

## 8. Component State Model

Status: `Approved` (`KBDL-CMP-004`, directly restates the locked
component-state-clarity rule,
[principles.md §5.1](principles.md#51-locked-identity-rules): every
component state must be distinguishable without relying on color
alone, and WCAG 2.2 SC 4.1.2/SC 1.4.1).

**State inventory:** Default, Hover, Focus-visible, Active/pressed,
Selected/current, Checked, Mixed/indeterminate, Expanded, Invalid,
Valid (where meaningful), Loading, Disabled, Read-only, Unavailable,
Required, Optional.

**Coexistence and precedence:**

- Multiple states **may** coexist (e.g., a control can be both
  `Selected` and `Focus-visible`); each coexisting state must remain
  independently perceivable.
- **Visual priority** when states compete for visual attention: Invalid
  and Loading take precedence over Hover; Focus-visible must always
  remain perceivable regardless of any other concurrent state (focus
  visibility is a locked accessibility requirement and is never
  suppressed by another state's styling).
- **Programmatically determinable:** every listed state must be
  exposed via native semantics or ARIA state/property — never conveyed
  only through visual styling.
- **Must not depend on color alone:** Invalid, Selected, Current,
  Checked, and Required must each pair with a non-color cue (icon,
  text, pattern, or position).
- **Removes from interaction:** Disabled removes an element from the
  tab order and from activation; Unavailable (e.g., a page that does
  not yet exist) is presented as non-interactive content, not a
  disabled control, where the two differ semantically.
- **Preserves focusability:** Read-only, Invalid, and Loading do **not**
  remove a control from the tab order — only Disabled does.
- **Requires status communication:** Loading and Invalid transitions
  must be communicated via a status message where the change is not
  already conveyed by moved focus (see
  [accessibility.md §35](accessibility.md#35-status-messages-and-live-communication)).
- **Must not be represented as each other:** `disabled` is not the same
  as `read-only` (read-only content may still be selected/copied and
  remains in the tab order); `loading` is not automatically `disabled`
  (a loading button typically remains focusable but not re-triggerable);
  `selected` is not the same as `pressed` (selected marks membership in
  a set; pressed marks a toggled binary state); `current` is not the
  same as `selected` (current marks location within navigation; selected
  marks a user choice); `invalid` is not the same as a system error (invalid
  is field-level and user-correctable; a system error is operation-level);
  a visually muted control is not automatically unavailable (muting is a
  visual choice and must not replace an explicit disabled/unavailable
  state).

## 9. Interaction-State Priority

Status: `Approved` (`KBDL-CMP-004`, part of the state model above).

When simultaneous interaction cues would compete, resolve in this
order: (1) safety/correctness — a destructive action's state must never
be visually ambiguous with a safe one; (2) accessibility — focus
visibility and programmatic state always win; (3) task comprehension —
Invalid/Loading communicate over decorative Hover; (4) profile emphasis
— the least priority, per
[principles.md §8](principles.md#8-design-decision-hierarchy).

## 10. Accessible Naming and Description

Status: `Approved` (`KBDL-CMP-003`, directly restates WCAG 2.2 SC 4.1.2
Name, Role, Value and SC 2.5.3 Label in Name, both already adopted in
[accessibility.md §8, §32](accessibility.md#8-semantic-structure-and-relationships)).

Every component **must** have a programmatically determinable accessible
name; where a visible label exists, the accessible name **must** include
that visible text (matching or beginning with it). An accessible
description **may** supplement the name with additional context (e.g.,
field hint text) but **must not** substitute for a missing name.

## 11. KBDL-008 Scope Boundary

Status: `Approved` (`KBDL-CMP-005`, a scope-control requirement).

This module defines **only** the trigger, field, action, or
navigation-side contract needed for future composition with
[KBDL-008](components-system.md) surfaces. It does **not** fully
specify: Card, Panel, Container surface, Accordion surface, Tooltip,
Popover, Menu surface, Dropdown surface, Listbox surface, Dialog,
Modal, Drawer, Sheet, Alert, Banner, Toast, Snackbar, Badge, Progress
indicator, Skeleton, Empty state, Error page, Offline state, System
status, Data visualization, Table component, Tree, Grid, or Carousel —
see [components-system.md](components-system.md) for the full
specification of each. Examples: this module defines a menu button's
trigger semantics, not the menu surface; a form field's error
relationship, not the alert component's visual design; a submit
button's loading contract, not a progress-indicator component; a
collapsed-navigation trigger, not the drawer surface; a select's or
combobox's relationship, not the popup surface styling.

## 12. Focus Behavior

Status: `Approved` (`KBDL-CMP-006`, directly restates WCAG 2.2 SC 2.4.7
Focus Visible, SC 2.4.11 Focus Not Obscured, and SC 2.4.3 Focus Order,
already adopted in
[accessibility.md §14, §15, §10](accessibility.md#14-focus-visibility)).

Every focusable component **must** show a visible focus indicator
(mapped to the **Focus indicator** semantic role,
[themes/semantic-roles.md §1.3](themes/semantic-roles.md#13-borders-and-focus));
focus order **must** follow logical source order
([responsive.md §12](responsive.md#12-source-order-and-reading-order));
a trigger component that reveals content **must** restore focus to a
sensible location (typically itself) when that content closes, unless
focus has moved meaningfully elsewhere within it.

## 13. Keyboard Interaction

Status: `Approved` (`KBDL-CMP-007`, directly restates WCAG 2.2 SC 2.1.1
Keyboard and SC 2.1.2 No Keyboard Trap, already adopted in
[accessibility.md §21, §22](accessibility.md#21-keyboard-operability)).

Every operable component **must** be fully operable via keyboard,
without a keyboard trap. Component-specific keyboard models are defined
per component in [§20](#20-action-components)–[§24](#24-navigation-components).

## 14. Pointer and Touch Interaction

Status: `Approved` (`KBDL-CMP-008`, directly restates WCAG 2.2 SC 2.5.2
Pointer Cancellation, SC 2.5.1 Pointer Gestures, and the target-size
requirements in
[accessibility.md §25, §26, §27](accessibility.md#25-target-sizing-and-spacing),
already adopted).

Every pointer-operable component **must** support pointer cancellation
where applicable and **must** meet the WCAG 2.2 24-by-24 CSS-pixel
target-size minimum or a documented valid exception
([§16](#16-target-size-handling)). A component using a gesture or
dragging interaction **must** provide a single-pointer, non-gesture
alternative, per the already-approved
[accessibility.md §27](accessibility.md#27-dragging-and-gesture-alternatives).

## 15. Responsive Behavior

Status: `Approved` (`KBDL-CMP-009`, directly restates the already-approved
responsive-content-priority, reflow, source-order, and focus-preservation
requirements in
[responsive.md §4, §11, §12, §25](responsive.md#4-responsive-content-priority)).

Every component **must** preserve content priority, meaning, source
order, and interaction purpose across breakpoints; reflow at
320-CSS-pixel-equivalent width; tolerate 200% text resizing and text-spacing
overrides; and preserve focus location when structural adaptation
occurs. This module uses only the four **approved named breakpoint
roles** (`compact`, `standard`, `expanded`, `wide`,
[responsive.md §6](responsive.md#6-named-breakpoint-roles)) and does
**not** require the unapproved exact breakpoint thresholds, grid
columns, gutters, or container widths proposed in
[responsive.md §7–§10](responsive.md#7-proposed-exact-breakpoint-thresholds)
(`KBDL-RSP-002`–`005`, `Recommended`).

## 16. Target-Size Handling

Status: `Approved` for the WCAG minimum (`KBDL-CMP-010`, directly
restates the already-approved
[accessibility.md §25](accessibility.md#25-target-sizing-and-spacing),
`KBDL-A11Y-020`). `Recommended` for any component-specific enhanced
sizing proposal (see [§35](#35-kbdl-007-decision-packet)).

Pointer targets **must** meet the 24-by-24 CSS-pixel minimum or a
documented valid exception (Spacing, Equivalent, Inline, User Agent
Control, or Essential — see
[accessibility.md §25](accessibility.md#25-target-sizing-and-spacing)
for the exact geometric separation test). The unapproved 44-by-44
CSS-pixel preferred size (`KBDL-A11Y-021`) is **not** a normative KBDL
minimum in this document; a component **may** propose it as an
enhancement in the decision packet, never as a requirement. Inline
links rely on the Inline exception; any use of the Spacing exception
must be checked against the actual 24-pixel-diameter, non-intersecting-circle
test, never assumed.

## 17. Theme and Contrast Behavior

Status: `Approved` (`KBDL-CMP-011`, directly restates the already-approved
theme semantic-role architecture,
[themes/semantic-roles.md](themes/semantic-roles.md), and text/non-text
contrast requirements,
[accessibility.md §12, §13](accessibility.md#12-text-contrast)).

Every component **must** map its visual roles to existing approved
semantic roles: default text/surfaces (Primary text, Base surface),
interactive text (Interactive text, Link text), primary action
(Primary action background/content), secondary action (Secondary action
background/content), destructive action (Critical status roles combined
with Primary or Secondary action roles, per
[themes/semantic-roles.md §2](themes/semantic-roles.md#2-semantic-parity)'s
parity rule — there is no separate "destructive action" role), focus
indicator (Focus indicator), borders (Default/Strong/Interactive
border), selected state (Selected border + Selected emphasis, paired
with a non-border cue), disabled state (Disabled surface/text/border/emphasis),
invalid state (Critical status roles), hover/active state (Hover
emphasis/Active emphasis). This document **does not** introduce a new
color value, opacity value, CSS variable, JSON token, or forced-colors
policy, and does not reopen any approved light or dark mapping.

## 18. Foundation Behavior

Status: `Approved` (`KBDL-CMP-012`, directly restates the already-approved
foundation architecture:
[foundations/typography.md §3.4, §3.8](foundations/typography.md#34-interface)
for control/label text (the Interface role, never a separate scale
step); [foundations/shape-depth.md §1.3, §1.5](foundations/shape-depth.md#13-default-corner-system)
for interactive-shape corner treatment (`corner-subtle`/`corner-pill`);
[foundations/shape-depth.md §3.2](foundations/shape-depth.md#32-default-semantic-elevation-scale)
for elevation (components at rest use Level 0/1; KBDL-008 surfaces use
Levels 2–4); [foundations/iconography-media.md §1.3](foundations/iconography-media.md#13-optical-sizing-strokefill-relationships-corner-treatment-alignment-bounding-boxes-visual-weight)
for icon sizing).

This document does **not** create a new font family, typography value,
spacing value, radius value, shadow value, icon-size scale, or token
format. Where a component-specific dimension is not determined by an
approved foundation rule, it is recorded as `Recommended`/`Unresolved`
in [§35](#35-kbdl-007-decision-packet)/[§36](#36-deferred-and-unresolved-items),
never invented as approved.

## 19. Motion Behavior

Status: `Approved` for the requirement that motion behavior be
documented per component (`KBDL-CMP-013`, restates
[motion/foundations.md §1](motion/foundations.md#1-motion-purposes)).
`Recommended` for every component-specific motion-category mapping,
since the underlying motion-pattern-matrix rows for Press
acknowledgment, Selection change, Expand/collapse, and Navigation
forward/back are themselves `Recommended`
([motion/patterns.md §12](motion/patterns.md#12-motion-pattern-matrix)).

Every applicable component **must** state: whether motion is necessary;
its motion purpose (from the approved purpose list,
[motion/foundations.md §1](motion/foundations.md#1-motion-purposes));
its motion hierarchy level (from the approved five-level hierarchy,
[motion/foundations.md §3](motion/foundations.md#3-motion-hierarchy) —
typically Functional for buttons/toggles, Supportive for
navigation/expand-collapse); full-motion, reduced-motion, and no-motion
behavior; and interruption behavior. This document does **not** invent
or approve exact component-specific durations, movement distances,
scale values, stagger values, easing curves, animation-library choices,
CSS/JavaScript implementation, device-performance detection, or
browser-support policy — any such mapping is `Recommended`, per
[§35](#35-kbdl-007-decision-packet).

## 20. Action Components

### 20.1 Button

Status: `Approved` core (`KBDL-CMP-014`, restates native-semantics-first,
keyboard, pointer, and focus requirements above). `Recommended` for the
hierarchy taxonomy (`KBDL-CMP-015`).

- **Purpose:** perform an immediate action within the current context.
- **Appropriate use:** submitting a form, triggering an operation,
  opening a KBDL-008 surface (as a trigger only).
- **Inappropriate use:** navigating to a new location (use Link,
  [§20.4](#204-link)).
- **Semantic role:** native `button` element.
- **Anatomy (required):** accessible label. **Anatomy (optional):**
  leading icon, trailing icon.
- **Supported variants (Recommended, `KBDL-CMP-015`):** Primary,
  Secondary, Tertiary, Destructive — a proposed hierarchy taxonomy, not
  yet approved; see [§35](#35-kbdl-007-decision-packet) item 1.
- **States:** Default, Hover, Focus-visible, Active/pressed, Loading,
  Disabled. (Selected/Checked/Expanded do not apply to an ordinary
  command button.)
- **Keyboard:** activates on `Enter` and `Space` (native button
  behavior).
- **Pointer/touch:** activates on click/tap; supports pointer
  cancellation (moving off before release cancels activation).
- **Submit/reset behavior:** a button with `type="submit"` triggers form
  submission; a button with `type="reset"` restores initial field
  values — reset buttons **should** be used sparingly given their
  potential for accidental data loss.
- **Loading behavior:** a loading button remains focusable, is not
  re-triggerable (prevents double submission, per
  [§23](#23-form-validation-and-recovery)), and communicates its loading
  state as a status message where the delay is meaningful.
- **Disabled behavior:** removed from tab order; must not be the only
  way to communicate why an action is unavailable — pair with
  explanatory text where the reason is not obvious.
- **Icon placement:** a leading icon reinforces meaning; an icon alone
  without a text label requires the Icon Button contract instead
  ([§20.2](#202-icon-button)).
- **Label length/responsive wrapping:** labels **should** stay short
  enough to avoid wrapping at `compact`; where wrapping is unavoidable,
  it must not truncate meaning.
- **Theme:** Primary action, Secondary action, or Critical+action-role
  combination roles, per [§17](#17-theme-and-contrast-behavior).
- **Motion:** Press acknowledgment, Functional level, per
  [§19](#19-motion-behavior) (`Recommended` mapping).
- **Reduced motion:** press feedback becomes an instant state change.
- **Related requirements:** `KBDL-CMP-002`, `004`, `006`, `007`, `008`,
  `010`, `011`, `013`.
- **Validation method:** manual review once implemented; project-owner
  review of the hierarchy taxonomy (not yet performed).

### 20.2 Icon Button

Status: `Approved` core (`KBDL-CMP-016`, restates accessible-name and
target-size requirements). `Recommended` for the visible-label
preference threshold (`KBDL-CMP-017`).

- **Purpose:** perform an action represented by an icon alone.
- **Requirement:** **must** have a programmatic accessible name (e.g.,
  via `aria-label` or equivalent) distinct from any decorative icon
  markup.
- **Decorative versus meaningful icons:** the icon itself is decorative
  (excluded from AT narration per
  [accessibility.md §6](accessibility.md#6-text-alternatives)); the
  button's accessible name carries the meaning.
- **Icon-only ambiguity:** an icon whose meaning is not universally
  understood **must** use a visible label instead of icon-only
  presentation (`Recommended` threshold, `KBDL-CMP-017` — "universally
  understood" is not yet enumerated as an approved list).
- **Focus-visible treatment:** per [§12](#12-focus-behavior).
- **Target size:** per [§16](#16-target-size-handling) — 24-by-24
  minimum or documented exception.
- **Loading/disabled states:** as [§20.1](#201-button).
- **Tooltip-dependency boundary:** an icon button's accessible name
  **must not** depend on a KBDL-008 tooltip surface being present or
  visible — the accessible name must exist independent of any tooltip.
  KBDL-007 defines only this accessible-name/trigger contract; the
  tooltip surface itself is KBDL-008 scope.
- **Related requirements:** `KBDL-CMP-003`, `010`, `014`.
- **Validation method:** manual + automated static accessibility check
  once implemented.

### 20.3 Toggle Button

Status: `Approved` (`KBDL-CMP-018`, restates WAI-ARIA `aria-pressed`
semantics and the locked component-state-clarity rule).

- **Purpose:** represent and toggle a persistent binary state tied to a
  stable action identity (e.g., "bold" formatting on/off).
- **Semantic role:** native `button` with `aria-pressed` (true/false),
  since no native pressed-button element exists.
- **Pressed/unpressed semantics:** state **must** be programmatically
  exposed via `aria-pressed`, never visual styling alone.
- **Label behavior:** the label typically describes the action, not the
  current state (e.g., "Bold," not "Bold: on").
- **Difference from checkbox:** a toggle button represents an
  in-context action toggle, not a form-field selection; it does not
  participate in form submission the way a checkbox does.
- **Difference from switch:** a switch ([§22.9](#229-switch)) represents
  an immediate system/preference setting; a toggle button represents a
  UI-local action toggle. Use switch for settings, toggle button for
  in-context formatting/view toggles.
- **Difference from ordinary command buttons:** an ordinary button
  performs a one-time action with no persistent pressed state.
- **Keyboard:** activates on `Enter`/`Space`, same as button.
- **Related requirements:** `KBDL-CMP-002`, `004`, `014`.
- **Validation method:** manual review once implemented.

### 20.4 Link

Status: `Approved` (`KBDL-CMP-019`, restates WCAG 2.2 SC 2.4.4 Link
Purpose (In Context), already adopted).

- **Purpose:** navigate to a different location, view, or resource.
- **Semantic role:** native `a` element with a valid `href`.
- **Link-purpose clarity:** link text **must** be determinable from its
  own text or from text plus programmatically-determinable context —
  never "click here" alone.
- **Visited-state consideration:** a visited-state treatment **may** be
  used; it must not be the sole way to communicate current location
  (use Current-page indication instead for that purpose).
- **Current-page indication:** the current page's link within
  navigation **must** be marked (e.g., `aria-current="page"`),
  distinct from visited state.
- **External destination/download indication:** where useful, indicate
  that a link leaves the site or triggers a download, communicated in
  text or accessible name, not icon alone.
- **Inline-link target-size exception:** an inline link within body text
  relies on the WCAG Inline exception ([§16](#16-target-size-handling)) —
  it is not required to meet 24×24 independently.
- **Focus-visible behavior:** per [§12](#12-focus-behavior).
- **Hover-independent recognition:** a link **must** be recognizable
  without relying on hover alone (e.g., underline or sufficient
  non-color distinction from surrounding text), per
  [§17](#17-theme-and-contrast-behavior)'s color-independence
  requirement.
- **Prohibition on false disabled links:** a link **must not** be
  presented as "disabled" via styling alone while remaining focusable
  and clickable, or vice versa — if a destination is genuinely
  unavailable, remove the link or use non-interactive text, not a
  disabled-looking but functional link.
- **Related requirements:** `KBDL-CMP-002`, `003`, `010`.
- **Validation method:** manual review once implemented.

### 20.5 Button Group

Status: `Recommended` (`KBDL-CMP-020`, new composition guidance).

- **Purpose:** present related actions together.
- **Group labeling:** a group **should** have an accessible group label
  when its purpose is not otherwise clear from context.
- **Tab order:** follows source order; grouping does not itself change
  tab order.
- **Wrapping/reflow:** at `compact`, a button group **may** wrap or
  stack; primary-action prominence must be preserved.
- **Primary-action clarity:** exactly one action in a group should read
  as primary where a clear primary exists; avoid multiple
  equally-weighted primary treatments (restates
  [principles.md §6.4](principles.md#64-visual-hierarchy), Approved).
- **Destructive-action separation:** a destructive action **should** be
  visually and positionally separated from routine actions to reduce
  accidental activation.
- **Avoiding action density:** avoid grouping more actions than a user
  can realistically evaluate at a glance; excess actions belong behind
  a disclosure/menu trigger.
- **Difference from segmented selection controls:** a button group
  performs independent actions; a segmented control (not defined in
  this module) represents mutually exclusive selection, closer to
  radio-group semantics.
- **Related requirements:** `KBDL-CMP-014`, `KBDL-PRN-004`.
- **Validation method:** manual review once implemented; project-owner
  review (not yet performed).

### 20.6 Disclosure and Menu Triggers

Status: `Approved` core (`KBDL-CMP-021`, restates WAI-ARIA disclosure
pattern and `aria-expanded`).

- **Purpose:** control the visibility of separate, related content or a
  menu surface (the surface itself is KBDL-008 scope).
- **Expanded/collapsed state:** exposed via `aria-expanded` on the
  trigger.
- **Controlled-content relationship:** the trigger **must** be
  programmatically associated with the content it controls (e.g.,
  `aria-controls` or equivalent DOM relationship).
- **Accessible name:** describes the action/content being
  revealed, not merely "toggle."
- **Focus behavior:** activating the trigger **may** move focus into
  the revealed content where appropriate (e.g., a menu) or leave focus
  on the trigger where the revealed content is supplementary (e.g., a
  simple disclosure).
- **Keyboard activation:** `Enter`/`Space` at minimum; a menu-button
  trigger additionally supports arrow-key entry into the menu per the
  APG menu-button pattern (menu surface itself out of scope).
- **Responsive preservation:** the trigger's accessible name and
  expanded state meaning remain identical across breakpoints.
- **Safe closing/focus restoration:** closing the revealed content
  (via `Escape`, outside activation, or re-triggering) **must** restore
  focus to the trigger unless the user has explicitly moved on.
- **Related requirements:** `KBDL-CMP-006`, `007`, `012`.
- **Validation method:** manual keyboard review once implemented.

## 21. Form Architecture

Status: `Approved` (`KBDL-CMP-022`, directly restates WCAG 2.2 SC 3.3.2
Labels or Instructions, SC 1.3.5 Identify Input Purpose, SC 3.3.7
Redundant Entry, all already adopted in
[accessibility.md §32](accessibility.md#32-forms-labels-instructions-and-autocomplete)).

Every field **must** document: field label; control; required/optional
indicator; supporting instructions; input-format guidance; prefix/suffix
(where used); character count (where applicable); validation message;
error-summary relationship; accessible name; accessible description;
programmatic validity; group label/description (for grouped fields);
form-level actions. Labels and instructions **must** be presented before
the user is expected to correct an error. Required/optional status
**must not** be communicated by color or symbol alone — pair with text.

## 22. Form Components

### 22.1 Text Input

Status: `Approved` (`KBDL-CMP-023`).

- **Purpose:** collect a single line of text.
- **Native input purposes:** text, email, telephone, URL, numeric, and
  other appropriate native `input` types/purposes, supporting
  autocomplete per WCAG 2.2 SC 1.3.5.
- **Labeling:** a programmatically associated label is required.
- **Placeholder limitations:** placeholder text **must not** substitute
  for a visible label; it may supplement with a format example only.
- **Prefix/suffix, clear-button behavior:** optional anatomy; a clear
  button requires its own accessible name.
- **Read-only vs. disabled:** read-only remains focusable and its value
  is presented for reference/copy; disabled is removed from
  interaction and tab order entirely.
- **Invalid state/error association:** per
  [§23](#23-form-validation-and-recovery).
- **Virtual-keyboard visibility:** per
  [responsive.md §22](responsive.md#22-virtual-keyboard-behavior),
  already approved.
- **Zoom/reflow:** per [§15](#15-responsive-behavior).
- **Sensitive-data considerations:** avoid echoing sensitive values in
  labels, placeholders, or error messages (see [Security Requirements](#37-security-and-privacy-in-components)).
- **Related requirements:** `KBDL-CMP-022`, `010`.
- **Validation method:** manual + automated static check once
  implemented.

### 22.2 Password Input

Status: `Approved` (`KBDL-CMP-024`, restates WCAG 2.2 SC 3.3.8
Accessible Authentication (Minimum), already adopted in
[accessibility.md §36](accessibility.md#36-authentication-accessibility)).

- **Password-manager compatibility:** paste **must** be supported; the
  field **must not** block password-manager autofill.
- **Show/hide-password action:** a toggle **may** reveal the entered
  value; the reveal control **must** have its own accessible name
  (e.g., "Show password") and its state (shown/hidden) must be
  programmatically communicated.
- **Caps-lock/format guidance:** where used, presented as instructions,
  not solely as an icon.
- **Error recovery:** per [§23](#23-form-validation-and-recovery);
  entered (partial) values are never silently cleared on error.
- **No forced cognitive-function test:** authentication **must not**
  require an unsupported cognitive-function test without an
  alternative, per the already-approved
  [accessibility.md §36](accessibility.md#36-authentication-accessibility).
- **Related requirements:** `KBDL-CMP-023`, `KBDL-A11Y-032`.
- **Validation method:** manual review once implemented.

### 22.3 Search Field

Status: `Recommended` (`KBDL-CMP-025`, new component taxonomy
distinguishing filtering from navigation search).

- **Purpose:** locate content via a query.
- **Search labeling:** an accessible name identifying it as search
  (e.g., "Search," or "Search products").
- **Search landmark relationship:** where a search field is the primary
  page-level search, a `search` landmark role **may** apply.
- **Submit behavior:** triggered by `Enter` or an adjacent submit
  control.
- **Clear behavior:** a clear control, where present, needs its own
  accessible name.
- **Empty query handling:** must not silently do nothing without
  feedback appropriate to context.
- **Loading/result-status boundary:** result presentation and
  loading-status surfaces are KBDL-008 scope; this field defines only
  the input/submit/clear contract.
- **Filtering versus navigation search distinction:** a filtering
  search (narrows visible content in place) behaves differently from a
  navigation search (goes to a results page) — which model applies is
  `Recommended`, not yet a single approved default.
- **Related requirements:** `KBDL-CMP-023`.
- **Validation method:** manual review once implemented; project-owner
  review (not yet performed).

### 22.4 Textarea

Status: `Approved` (`KBDL-CMP-026`).

- **Purpose:** collect multi-line text.
- **Labeling:** per [§21](#21-form-architecture).
- **Resizing:** user resizing, where offered, must not break layout or
  hide the label/instructions.
- **Minimum usable area:** must remain large enough for multi-line
  review; exact dimensions are foundation-dependent and not defined
  here (no new dimension is invented — see
  [§18](#18-foundation-behavior)).
- **Character count:** optional anatomy; must be programmatically
  associated, not only visually adjacent.
- **Maximum length:** where enforced, communicated before the limit is
  hit, not only as a hard block.
- **Error association:** per [§23](#23-form-validation-and-recovery).
- **Text-spacing/zoom resilience:** per
  [accessibility.md §19](accessibility.md#19-text-spacing-overrides),
  already approved.
- **Related requirements:** `KBDL-CMP-022`.
- **Validation method:** manual review once implemented.

### 22.5 Select

Status: `Approved` (`KBDL-CMP-027`, restates native-semantics-first).

- **Purpose:** choose one (or more) values from a bounded list.
- **Native select preference:** a native `select` element **must** be
  used unless its behavior is genuinely insufficient (see
  [§22.6](#226-combobox-boundary)).
- **Labeling:** per [§21](#21-form-architecture).
- **Single/multiple selection:** native `select`/`select multiple`
  semantics apply respectively.
- **Placeholder-like option limitations:** a non-selectable prompt
  option (e.g., "Select one") **must** be marked disabled/non-selectable
  if used, and is not a substitute for a visible label.
- **Required/invalid state:** per [§21](#21-form-architecture),
  [§23](#23-form-validation-and-recovery).
- **Difference from command menus:** a select changes a field's value;
  a menu (see [§20.6](#206-disclosure-and-menu-triggers)) triggers
  actions.
- **Difference from custom comboboxes:** see
  [§22.6](#226-combobox-boundary).
- **Related requirements:** `KBDL-CMP-002`, `022`.
- **Validation method:** manual review once implemented.

### 22.6 Combobox Boundary

Status: `Approved` for the requirement that any custom combobox follow
the applicable ARIA/keyboard contract (`KBDL-CMP-028`); `Recommended`
for when a custom combobox is justified over native select
(`KBDL-CMP-029`).

- A custom combobox **may** be documented only when native select
  behavior is genuinely insufficient (e.g., filterable large option
  sets); this threshold is `Recommended`, not yet an approved
  enumerated list of qualifying cases.
- **Input/popup relationship:** the visible input is programmatically
  associated with its popup listbox (`aria-controls`/`aria-owns`
  equivalent).
- **Expanded state:** `aria-expanded` on the input/combobox wrapper.
- **Active-option communication:** the currently active (highlighted)
  option is communicated via `aria-activedescendant` or equivalent,
  following the APG combobox pattern.
- **Selection behavior, keyboard contract, Escape behavior:** follow the
  APG combobox pattern's keyboard model (arrow keys move active option,
  `Enter` selects, `Escape` closes without changing value unless a
  value was already committed).
- **Focus ownership:** focus **should** remain on the visible input
  throughout, with the popup managed via `aria-activedescendant` rather
  than moving actual DOM focus into the popup (per APG guidance),
  unless a documented alternative pattern is used.
- **Value versus suggestion distinction:** a suggested (not yet
  committed) option must be clearly distinguished from the field's
  actual committed value.
- **Popup-surface visual treatment:** deferred to KBDL-008.
- **Related requirements:** `KBDL-CMP-027`, `002`, `007`.
- **Validation method:** manual keyboard/ARIA review once implemented;
  project-owner review of the justification threshold (not yet
  performed).

### 22.7 Checkbox

Status: `Approved` (`KBDL-CMP-030`, restates native-semantics-first and
WAI-ARIA checkbox states).

- **Purpose:** binary selection, independently of other checkboxes.
- **Semantic role:** native `input type="checkbox"`.
- **States:** checked, unchecked, and mixed/indeterminate (the latter
  representing a partial-selection summary of a group, set
  programmatically, never user-togglable directly into mixed).
- **Group labeling:** a set of related checkboxes **should** share a
  group label (e.g., `fieldset`/`legend` or equivalent).
- **Keyboard behavior:** `Space` toggles; `Tab` moves between
  checkboxes individually (checkboxes are not arrow-key grouped, unlike
  radio buttons).
- **Label activation:** clicking the associated label **must** toggle
  the checkbox (native label-association behavior).
- **Error association:** per [§23](#23-form-validation-and-recovery).
- **Disabled behavior:** per [§8](#8-component-state-model).
- **Related requirements:** `KBDL-CMP-022`, `004`.
- **Validation method:** manual review once implemented.

### 22.8 Radio Group

Status: `Approved` (`KBDL-CMP-031`, restates native-semantics-first and
WAI-ARIA radio-group keyboard model).

- **Purpose:** mutually exclusive selection among a bounded set.
- **Group label:** required (e.g., `fieldset`/`legend`).
- **Required selection:** where the group is required, this **must** be
  communicated per [§21](#21-form-architecture), not by pre-selecting an
  arbitrary option to force a value.
- **Arrow-key behavior:** arrow keys move selection among options
  within the group (native radio-group behavior).
- **Tab-entry behavior:** `Tab` moves into and out of the group as a
  single stop, landing on the selected (or first) option.
- **Initial selection:** should reflect a genuine default, not force a
  choice the user has not made, unless a default is truly meaningful.
- **Error association:** per [§23](#23-form-validation-and-recovery).
- **Disabled options:** an individual option may be disabled while
  others in the group remain selectable.
- **Related requirements:** `KBDL-CMP-022`, `004`.
- **Validation method:** manual review once implemented.

### 22.9 Switch

Status: `Approved` (`KBDL-CMP-032`, restates WAI-ARIA switch role).

- **Purpose:** represent and immediately change a binary setting (not a
  form-submission-pending value).
- **Semantic role:** `role="switch"` with `aria-checked`, or a native
  checkbox styled/announced as a switch where the host language lacks a
  dedicated switch element.
- **On/off semantics:** immediate effect is the defining characteristic
  — a switch changes the setting as soon as toggled, unlike a checkbox
  in an unsubmitted form.
- **Stable label:** the label describes the setting, not the current
  value (e.g., "Notifications," not "Notifications: on").
- **State communication:** on/off state programmatically exposed, never
  color alone.
- **Keyboard/pointer behavior:** `Space`/`Enter` toggles; click/tap
  toggles.
- **Difference from checkbox:** immediate effect vs. pending
  form-submission value.
- **Difference from toggle button:** a switch represents a persistent
  setting; a toggle button ([§20.3](#203-toggle-button)) represents an
  in-context UI action toggle.
- **Avoidance of ambiguous affirmative/negative labels:** avoid labels
  where "on" is unclear (e.g., a double-negative setting name);
  restate the setting so "on" reads unambiguously.
- **Related requirements:** `KBDL-CMP-018`, `022`.
- **Validation method:** manual review once implemented.

### 22.10 File Input

Status: `Approved` (`KBDL-CMP-033`).

- **Purpose:** select one or more local files for upload.
- **Native file-control preference:** a native `input type="file"`
  **must** be used unless genuinely insufficient.
- **Accessible label:** required, describing what is being uploaded.
- **Accepted-file guidance:** communicated in visible instructions, not
  only the native `accept` attribute (which is not reliably
  communicated to all assistive technology).
- **Multiple-file selection:** where supported, clearly indicated.
- **File-name communication:** selected file name(s) presented as
  text, not only an icon.
- **Removal action:** a remove control needs its own accessible name.
- **Error association:** per [§23](#23-form-validation-and-recovery).
- **Security/privacy language:** guidance must not encourage exposing
  file contents or metadata beyond what the user intends; see
  [§37](#37-security-and-privacy-in-components).
- **Upload-progress boundary:** upload progress, failure feedback, and
  system status are KBDL-008 scope; this component defines only the
  field's selection/labeling/error contract.
- **Related requirements:** `KBDL-CMP-022`.
- **Validation method:** manual review once implemented.

### 22.11 Field Group

Status: `Approved` (`KBDL-CMP-034`, restates WCAG grouping/labeling
requirements).

- **Purpose:** group related controls (e.g., an address's street/city/
  postal fields).
- **Group label/description:** required where the grouping's purpose
  is not otherwise obvious.
- **Required/optional state:** may apply at the group level in addition
  to individual fields.
- **Group-level error:** a group can carry an error not attributable to
  a single field (e.g., "at least one option required").
- **Nested-grouping limits:** avoid nesting groups more than one level
  deep, since excessive nesting harms comprehension and AT navigation.
- **Reading/focus order:** matches visual layout; grouped fields are
  not reordered relative to their visual position.
- **Related requirements:** `KBDL-CMP-022`.
- **Validation method:** manual review once implemented.

### 22.12 Form Action Row

Status: `Approved` core (`KBDL-CMP-035`, restates double-submission
prevention and destructive-action requirements). `Recommended` for
exact responsive reflow ordering (`KBDL-CMP-036`).

- **Submit action:** primary button, per [§20.1](#201-button).
- **Secondary/cancel/back action:** clearly subordinate to submit,
  never equally weighted.
- **Destructive action:** visually and positionally distinguished, per
  [§20.5](#205-button-group).
- **Loading behavior:** submit enters Loading state during processing;
  other actions in the row **should** be disabled or clearly
  subordinated during submission to prevent conflicting actions.
- **Double-submission prevention:** a behavioral requirement — the
  submit control **must** prevent duplicate submission while a prior
  submission is in flight (e.g., via its Loading state), regardless of
  implementation technique.
- **Responsive reflow:** action order at `compact` (e.g., stacking) is
  `Recommended`, not a single approved default — see
  [§35](#35-kbdl-007-decision-packet).
- **Logical source order:** submit and secondary actions maintain a
  consistent, predictable source order regardless of visual reflow.
- **Confirmation-dialog visuals:** out of scope — belongs to KBDL-008.
- **Related requirements:** `KBDL-CMP-014`, `020`, `026` (error
  prevention).
- **Validation method:** manual review once implemented; project-owner
  review of reflow ordering (not yet performed).

## 23. Form Validation and Recovery

Status: `Approved` (`KBDL-CMP-037`, directly restates WCAG 2.2 SC 3.3.1
Error Identification, SC 3.3.3 Error Suggestion, SC 3.3.4 Error
Prevention, SC 3.3.7 Redundant Entry, and SC 4.1.3 Status Messages, all
already adopted in
[accessibility.md §33, §34, §35](accessibility.md#33-error-identification-and-recovery)).

**Requirements:**

- **Validation timing:** errors are identified at a point that gives
  the user a fair opportunity to correct them (typically on submission
  or on field exit, not while actively typing the first character).
- **Field-level errors:** identified in text, programmatically
  associated with the field.
- **Form-level error summary:** where multiple errors exist, a summary
  **should** list them, each linked to its affected field.
- **Focus movement after failed submission:** focus **should** move to
  the error summary or first invalid field, so the user is not left
  without orientation.
- **Error identification/suggestion:** errors state what's wrong and,
  where safely known, how to fix it.
- **Preserving entered data:** a failed submission **must not** clear
  already-entered valid data.
- **Redundant-entry avoidance:** information already provided in the
  same process **must not** be required again unless essential,
  auto-populated, or selectable.
- **Consequential-action review:** legal/financial/data-modifying
  submissions support review, correction, or confirmation before
  finalizing (the confirmation surface itself may be KBDL-008 scope;
  this component defines the requirement, not the dialog's visuals).
- **Status-message communication:** validation outcomes are
  programmatically determinable without requiring focus to move,
  where appropriate.
- **Server-side/client-side distinction:** both are surfaced through
  the same error-association contract; client-side validation is never
  a substitute for server-side security validation
  ([§37](#37-security-and-privacy-in-components)).
- **Retry behavior:** a failed operation permits retry without forcing
  re-entry of already-valid data.
- **Required-field communication:** per [§21](#21-form-architecture) —
  never color/symbol alone.
- **Success-confirmation boundary:** success banners/toasts are KBDL-008
  scope; this component defines the form's relationship to them
  (e.g., that a status message occurs), not their surface design.

**Prohibited:** relying on color alone, icons alone, placeholder text
alone, or motion alone to communicate an error; automatic focus
movement without context; automatic form submission triggered merely by
focus or input, unless explicitly justified and accessible.

## 24. Navigation Components

### 24.1 Skip Link

Status: `Approved` (`KBDL-CMP-038`, directly restates WCAG 2.2 SC 2.4.1
Bypass Blocks, already adopted in
[accessibility.md §23](accessibility.md#23-bypass-mechanisms)).

- **Purpose:** bypass repeated navigation/header content.
- **First-focus behavior:** typically the first focusable element on
  the page.
- **Visible-on-focus presentation:** may be visually hidden until
  focused, but must become visible when it receives focus.
- **Destination focus behavior:** activating it moves focus to the main
  content landmark.
- **Sticky-header offset:** the destination scroll position accounts
  for any sticky header, per the already-approved
  [responsive.md §18](responsive.md#18-sticky-and-fixed-regions).
- **Multiple bypass destinations:** justified only where multiple
  genuinely distinct repeated blocks exist (e.g., skip to main content,
  skip to search).
- **Related requirements:** `KBDL-A11Y-018`, `KBDL-CMP-012`.
- **Validation method:** manual keyboard testing once implemented.

### 24.2 Navigation Link and List

Status: `Approved` (`KBDL-CMP-039`, restates Link and semantic-list
requirements).

- **Purpose:** present a set of navigation destinations.
- **List semantics:** navigation items **must** use list semantics
  (native `ul`/`ol`/`li` or equivalent) so assistive technology
  communicates set size and position.
- **Current location:** per [§20.4](#204-link).
- **Hierarchical grouping:** nested navigation uses nested list
  semantics, not visual indentation alone.
- **Consistent order:** navigation item order **must** remain
  consistent across pages, per the already-approved
  [accessibility.md §38](accessibility.md#38-consistent-navigation-identification-and-help).
- **Icon/label relationship:** an icon paired with a nav label is
  decorative; the label itself carries the accessible name.
- **Keyboard/pointer:** standard link behavior.
- **Related requirements:** `KBDL-CMP-019`, `KBDL-A11Y-034`.
- **Validation method:** manual review once implemented.

### 24.3 Primary or Global Navigation

Status: `Approved` core (`KBDL-CMP-040`, restates landmark, current-location,
and focus-preservation requirements). `Recommended` for the exact
collapse trigger threshold (`KBDL-CMP-041`, since `KBDL-RSP-002`/`008`
remain unapproved).

- **Navigation landmark labeling:** the primary navigation region is a
  labeled landmark (e.g., `nav` with an accessible name), distinct from
  any secondary/local navigation landmark.
- **Current destination:** per [§20.4](#204-link).
- **Responsive meaning preservation:** navigation items and their
  destinations remain identical regardless of breakpoint or collapse
  state, per the already-approved
  [responsive.md §13](responsive.md#13-navigation-adaptation).
- **Source order:** consistent regardless of visual position.
- **Focus preservation:** structural adaptation (e.g., collapsing)
  preserves focus location per
  [responsive.md §25](responsive.md#25-responsive-focus-management),
  already approved.
- **Trigger contract for collapsed navigation:** uses the Disclosure/
  Menu Trigger contract ([§20.6](#206-disclosure-and-menu-triggers));
  the **exact width at which collapse occurs** is `Recommended`
  (depends on `KBDL-RSP-002`/`008`, unapproved) — this document does
  **not** prescribe that exact threshold.
- **Touch/pointer/keyboard parity:** the collapsed trigger and expanded
  navigation provide equivalent functionality across input methods.
- **Navigation drawer/overlay surface:** KBDL-008 scope.
- **Related requirements:** `KBDL-RSP-008`, `KBDL-CMP-021`, `039`.
- **Validation method:** manual review once implemented; project-owner
  review of the collapse threshold (not yet performed).

### 24.4 Local or Section Navigation

Status: `Approved` (`KBDL-CMP-042`).

- **Relationship to global navigation:** a secondary, page- or
  section-scoped navigation region, separately landmarked when more
  than one navigation region exists on a page (per
  [accessibility.md §9](accessibility.md#9-landmark-and-heading-architecture)).
- **Current section:** indicated per [§20.4](#204-link).
- **Hierarchy depth:** should remain shallow enough to scan; excessive
  nesting harms comprehension (restates
  [principles.md §6.1](principles.md#61-clarity-before-spectacle)).
- **Persistent versus collapsible:** either is valid; whichever is
  used must preserve meaning across breakpoints.
- **Responsive reflow:** per [§15](#15-responsive-behavior).
- **Landmark naming:** where multiple navigation regions exist, each
  needs a distinct accessible name.
- **Related requirements:** `KBDL-CMP-039`, `040`.
- **Validation method:** manual review once implemented.

### 24.5 Breadcrumb

Status: `Approved` core (`KBDL-CMP-043`, restates ordered-list/current-item
semantics). `Recommended` for the truncation model (`KBDL-CMP-044`).

- **Purpose:** communicate hierarchical location.
- **Ordered relationship:** uses an ordered list (or equivalent) inside
  a labeled navigation landmark (e.g., `nav` labeled "Breadcrumb").
- **Current-page handling:** the final (current) item is not a link,
  and is marked current, not merely styled differently.
- **Truncation without losing meaning:** where space is constrained,
  truncation must preserve access to all levels (e.g., via an overflow
  affordance), never silently drop a level; the exact truncation
  presentation is `Recommended`.
- **Accessible name:** the breadcrumb region has an accessible name
  identifying it as breadcrumb navigation.
- **Separator treatment:** visual separators are decorative, excluded
  from AT narration (the list semantics already convey order).
- **Responsive behavior:** per [§15](#15-responsive-behavior).
- **Related requirements:** `KBDL-CMP-019`, `039`.
- **Validation method:** manual review once implemented; project-owner
  review of the truncation model (not yet performed).

### 24.6 Tabs

Status: `Approved` core (`KBDL-CMP-045`, directly restates the WAI-ARIA
tabs pattern's role/state/keyboard model). `Recommended` for the
activation-model choice (`KBDL-CMP-046`).

- **Appropriate use:** switching between related content panels within
  one page context.
- **Inappropriate use:** page-level navigation between unrelated
  destinations (use navigation links instead).
- **Roles/relationships:** `tablist` containing `tab` elements, each
  associated with a `tabpanel` via `aria-controls`/`aria-labelledby`.
- **Selected state:** the active tab is marked `aria-selected="true"`;
  others `false`.
- **Keyboard arrow behavior:** arrow keys move among tabs (per the APG
  tabs pattern); only the selected (or focused, under manual
  activation) tab is in the natural tab order — arrow keys move within
  the tablist.
- **Home/End behavior:** where adopted, moves to first/last tab —
  `Recommended`, part of the activation-model decision.
- **Automatic versus manual activation:** whether moving focus with
  arrow keys immediately activates the panel (automatic) or requires a
  separate confirming keypress (manual) is a **new component choice**,
  `Recommended`, not silently approved — see
  [§35](#35-kbdl-007-decision-packet) item 2.
- **Focus placement:** activating a tab **should** place focus
  logically (either remaining on the tab or moving into the panel,
  depending on the chosen activation model).
- **Panel accessibility:** each panel has an accessible name derived
  from its tab and is properly associated.
- **Overflow/reflow:** at `compact`, tabs **may** scroll horizontally
  within their own region rather than causing page-level horizontal
  scroll, per [§15](#15-responsive-behavior)/[responsive.md §11](responsive.md#11-layout-reflow).
- **Reduced-motion behavior:** panel switching becomes an instant state
  change.
- **Related requirements:** `KBDL-CMP-004`, `007`, `019`.
- **Validation method:** manual keyboard/ARIA review once implemented;
  project-owner review of the activation model (not yet performed).

### 24.7 Pagination

Status: `Approved` core (`KBDL-CMP-047`, restates landmark and
current-page requirements). `Recommended` for the truncation model
(`KBDL-CMP-048`).

- **Navigation landmark:** a labeled navigation region (e.g., `nav`
  labeled "Pagination").
- **Current page:** marked (e.g., `aria-current="page"`), not a link to
  itself.
- **Previous/next actions:** clearly labeled, not icon-only without an
  accessible name.
- **Page-number purpose:** each page-number control's accessible name
  identifies the page number, not merely "link."
- **Disabled/unavailable navigation:** a Previous control at the first
  page (or Next at the last) is disabled or omitted, never a
  non-functional but visually active control.
- **Truncation/ellipsis behavior:** where the page count is large,
  truncation (e.g., an ellipsis) is `Recommended`, not a single
  approved presentation; it must never hide that more pages exist.
- **Small-viewport behavior:** per [§15](#15-responsive-behavior) —
  content priority (current page, previous/next) is preserved.
- **Accessible names:** every control has a distinct, descriptive name.
- **Focus behavior after page change:** focus **should** move
  logically (e.g., to the results region or remain on the activated
  control) so context is not lost.
- **Related requirements:** `KBDL-CMP-019`, `039`.
- **Validation method:** manual review once implemented; project-owner
  review of the truncation model (not yet performed).

### 24.8 Back Link

Status: `Approved` (`KBDL-CMP-049`).

- **Destination clarity:** a "back" link's destination **must** be
  determinable (e.g., "Back to search results," not "Back" alone),
  restating Link Purpose ([§20.4](#204-link)).
- **Difference from browser Back:** a component-level back link is an
  explicit, page-defined destination; it does not assume or replace the
  browser's native back-navigation history behavior.
- **Preservation of user context:** where feasible, returns the user to
  their prior scroll position/state, not merely the top of a
  destination page.
- **Focus destination:** where applicable, focus lands on a sensible
  landmark in the destination.
- **Avoidance of ambiguous labels:** "Back" alone without context is
  discouraged; pair with the specific destination.
- **Related requirements:** `KBDL-CMP-019`.
- **Validation method:** manual review once implemented.

## 25. Cross-Component Composition Rules

Status: `Approved` (`KBDL-CMP-050`, restates the shared contract and
native-semantics-first rule applied across component boundaries).

A field's clear action, a combobox's input, a select's native control,
and a form's submit button each independently satisfy their own
contract; composing them (e.g., a labeled text input with a clear
icon-button inside a field group) does not change any individual
component's accessible-name, keyboard, or state requirements. A
disclosure trigger inside a navigation component still follows the
Disclosure/Menu Trigger contract; a button inside a form action row
still follows the Button contract.

## 26. Profile Compatibility

Status: `Approved` (`KBDL-CMP-051`, directly restates
[principles.md §9.4](principles.md#94-shared-constraints-across-profiles)
and the already-approved motion/responsive/accessibility profile-
consistency requirements).

All core components **must** share one semantic and accessibility
architecture across Showcase, Precision, and Flow. Compatibility
considerations: Showcase may allow more expressive composition (larger
button treatments, richer navigation); Precision may need greater
density and data-task efficiency (compact button groups, dense
pagination); Flow may emphasize progression and consumer task clarity
(clear single-action form rows). Profiles **must not**: define separate
component systems; change component semantics; introduce
profile-specific variants as approved requirements; use a profile to
justify weaker accessibility. Detailed profile component mapping is
deferred to the later Project Profiles module (`PRO`).

## 27. Conforming Examples

1. **Showcase, keyboard.** A portfolio's primary "View Project" button
   is a native `button`, reachable via Tab, activates on Enter, and
   shows a visible focus ring meeting non-text contrast. *Conforms:*
   [§20.1](#201-button), [§12](#12-focus-behavior).
2. **Precision, screen reader.** A dashboard's icon-only "Refresh"
   button exposes `aria-label="Refresh data"`, independent of any
   tooltip. *Conforms:* [§20.2](#202-icon-button).
3. **Flow, touch.** A checkout form's submit button enters a Loading
   state on tap, remains focusable, and cannot be re-triggered before
   the first request completes. *Conforms:* [§20.1](#201-button),
   [§23](#23-form-validation-and-recovery).
4. **All profiles, narrow width.** A primary/global navigation collapses
   to a trigger at a content-justified point, preserving identical
   destinations and labels as the expanded state. *Conforms:*
   [§24.3](#243-primary-or-global-navigation).
5. **All profiles, enlarged text.** A field label and its input remain
   associated and legible at 200% zoom, with the error message still
   linked to the field. *Conforms:* [§15](#15-responsive-behavior),
   [§23](#23-form-validation-and-recovery).
6. **Light and dark theme.** A destructive "Delete" button maps to the
   Critical status family combined with the Primary action role,
   remaining equally prominent in both themes. *Conforms:*
   [§17](#17-theme-and-contrast-behavior).
7. **Reduced motion.** A disclosure trigger's expand/collapse becomes
   an instant show/hide, with `aria-expanded` still updating correctly.
   *Conforms:* [§19](#19-motion-behavior), [§20.6](#206-disclosure-and-menu-triggers).
8. **Precision, pointer.** A radio group for a report's date-range
   preset uses arrow-key navigation among options with `Tab` treating
   the group as one stop. *Conforms:* [§22.8](#228-radio-group).

## 28. Non-Conforming Examples

1. **Link styled as a button performing an action.** A "Delete" control
   is an `a` element with `href="#"` and a click handler, never
   navigating. *Violates:* [§5](#5-native-semantics-first-rule).
2. **Icon button with no accessible name.** A trash-can icon button has
   no `aria-label`, relying only on a tooltip that appears on hover.
   *Violates:* [§20.2](#202-icon-button).
3. **Color-only invalid state.** An invalid text input turns its border
   red with no icon, text, or accessible-name change. *Violates:*
   [§8](#8-component-state-model), [§23](#23-form-validation-and-recovery).
4. **False disabled link.** A navigation item looks disabled (muted
   color) but remains clickable and functional. *Violates:*
   [§20.4](#204-link).
5. **Keyboard trap in a custom combobox.** Opening the popup traps focus
   inside it with no way to Escape back to the input. *Violates:*
   [§13](#13-keyboard-interaction), [§22.6](#226-combobox-boundary).
6. **Redundant re-entry.** A multi-step form re-asks for an email
   address already entered in step one. *Violates:*
   [§23](#23-form-validation-and-recovery).
7. **Ambiguous switch label.** A settings switch reads "Disable
   notifications" with "on" meaning notifications are silenced —
   confusing double-negative. *Violates:* [§22.9](#229-switch).
8. **Breadcrumb dropping levels.** A breadcrumb at `compact` shows only
   "Home ... Current Page" with the middle levels entirely inaccessible,
   not just visually truncated. *Violates:* [§24.5](#245-breadcrumb).
9. **Tabs using page navigation semantics.** A "tabs" component is
   actually a set of full-page links styled to look like tabs, breaking
   the ARIA tablist/tabpanel relationship. *Violates:*
   [§24.6](#246-tabs).
10. **Pagination without labeled current page.** Page-number links have
    no way to determine which page is active except a subtle color
    change. *Violates:* [§24.7](#247-pagination), [§8](#8-component-state-model).
11. **Automatic form submission on selection.** Choosing a radio option
    immediately submits the form with no visible submit action or
    warning. *Violates:* [§23](#23-form-validation-and-recovery).
12. **Undersized icon-only action with no exception.** A 16-by-16 CSS
    pixel icon button sits with no adjacent equivalent-sized control
    and no documented WCAG exception. *Violates:*
    [§16](#16-target-size-handling).

## 29. Component Coverage Matrix

| Component | Family | Preferred native semantic | Custom pattern | Required states | Keyboard model | Responsive model | Theme roles | Motion model | CMP requirements | Related A11Y | Related RSP | Lifecycle | KBDL-008 dependency |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Button | Action | `button` | — | Default/Hover/Focus/Active/Loading/Disabled | Enter/Space | §15 | Primary/Secondary/Critical action | Press (Functional) | 014, 015 | 020, 026 | 006 | Approved core; Recommended hierarchy | None |
| Icon button | Action | `button` | — | Default/Hover/Focus/Active/Loading/Disabled | Enter/Space | §15 | Primary/Secondary action | Press (Functional) | 016, 017 | 001, 020 | 006 | Approved core; Recommended threshold | Tooltip (§8) |
| Toggle button | Action | `button` + `aria-pressed` | ARIA pressed | Default/Focus/Pressed/Disabled | Enter/Space | §15 | Selected emphasis | Selection change (Functional) | 018 | 006 | — | Approved | None |
| Link | Action | `a` | — | Default/Hover/Focus/Visited/Current | Enter | §15 | Link text, Interactive text | — | 019 | 034 | — | Approved | None |
| Button group | Action | `button` × N | — | Per-button | Tab between | §15 | Per-button | — | 020 | — | 006 | Recommended | None |
| Disclosure/menu trigger | Action | `button` + `aria-expanded` | ARIA disclosure/menu-button | Default/Focus/Expanded/Disabled | Enter/Space, arrows (menu) | §15 | Focus indicator | Expand/collapse (Supportive) | 021 | 010 | — | Approved core | Menu/popover surface (§8) |
| Text input | Form | `input` | — | Default/Focus/Invalid/Disabled/Read-only | Native text entry | §15 | Border, Focus indicator | — | 023 | 028 | — | Approved | None |
| Password input | Form | `input type=password` | — | Default/Focus/Invalid/Disabled | Native text entry | §15 | Border, Focus indicator | — | 024 | 032 | — | Approved | None |
| Search field | Form | `input type=search` | — | Default/Focus/Loading | Native text entry | §15 | Border, Focus indicator | — | 025 | 028 | — | Recommended | Results surface (§8) |
| Textarea | Form | `textarea` | — | Default/Focus/Invalid/Disabled | Native text entry | §15 | Border, Focus indicator | — | 026 | 019 | — | Approved | None |
| Select | Form | `select` | — | Default/Focus/Invalid/Disabled | Native select | §15 | Border, Focus indicator | — | 027 | 028 | — | Approved | None |
| Combobox | Form | `input` + `role=combobox` | ARIA combobox/APG | Default/Focus/Expanded/Invalid | APG combobox model | §15 | Border, Focus indicator | Expand/collapse (Supportive) | 028, 029 | 005 | — | Approved core; Recommended threshold | Popup surface (§8) |
| Checkbox | Form | `input type=checkbox` | — | Checked/Unchecked/Mixed/Disabled | Space | §15 | Selected border/emphasis | Selection change (Functional) | 030 | 006 | — | Approved | None |
| Radio group | Form | `input type=radio` × N | — | Selected/Disabled per option | Arrows within group | §15 | Selected border/emphasis | Selection change (Functional) | 031 | 006 | — | Approved | None |
| Switch | Form | `role=switch` | ARIA switch | On/Off/Disabled | Space/Enter | §15 | Selected emphasis | Selection change (Functional) | 032 | 006 | — | Approved | None |
| File input | Form | `input type=file` | — | Default/Focus/Invalid/Disabled | Native file picker | §15 | Border, Focus indicator | — | 033 | 001 | — | Approved | Upload progress (§8) |
| Field group | Form | `fieldset`/`legend` | — | Default/Invalid | Tab through members | §15 | Border | — | 034 | 028 | — | Approved | None |
| Form action row | Form | `button` × N | — | Default/Loading/Disabled | Tab between | §15 | Primary/Secondary/Critical action | — | 035, 036 | 030 | — | Approved core; Recommended order | Confirmation dialog (§8) |
| Skip link | Navigation | `a` | — | Default/Focus | Enter | §15 | Focus indicator | — | 038 | 018 | — | Approved | None |
| Nav link/list | Navigation | `a` + `ul`/`li` | — | Default/Current/Focus | Enter | §15 | Link text | — | 039 | 034 | — | Approved | None |
| Primary/global nav | Navigation | `nav` | ARIA landmark | Default/Current/Expanded (collapsed) | Enter/Tab | §15 | Link text, Focus indicator | Expand/collapse (Supportive) | 040, 041 | 019, 020 | 008 | Approved core; Recommended threshold | Drawer surface (§8) |
| Local/section nav | Navigation | `nav` | ARIA landmark | Default/Current | Enter/Tab | §15 | Link text | — | 042 | 018, 019 | — | Approved | None |
| Breadcrumb | Navigation | `nav` + `ol`/`li` | — | Default/Current | Enter | §15 | Link text | — | 043, 044 | 034 | — | Approved core; Recommended truncation | None |
| Tabs | Navigation | `div` + ARIA tabs | ARIA tablist/APG | Selected/Focus/Disabled | Arrows, Home/End | §15 | Selected border/emphasis | Selection change (Functional) | 045, 046 | 005, 006 | — | Approved core; Recommended activation | Panel content varies |
| Pagination | Navigation | `nav` + `a`/`button` | — | Current/Disabled | Enter/Tab | §15 | Link text, Focus indicator | — | 047, 048 | 034 | — | Approved core; Recommended truncation | None |
| Back link | Navigation | `a` | — | Default/Focus | Enter | §15 | Link text | — | 049 | 034 | — | Approved | None |

## 30. Normative Requirements

Requirement IDs use `KBDL-CMP-###`
([conventions.md §2](conventions.md#2-requirement-identification)),
starting at `001` (no prior `CMP` requirement exists). Assigning an ID
does not grant approval or implementation authority
([KBDL-DEC-015](decision-register.md#kbdl-dec-015--kbdl-006-remediation-and-id-governance-amendment)).

**Authoritative status summary** (derived directly from the per-requirement
lifecycle field below, not a separately maintained count):

```text
Total:       51
Approved:    41
Recommended: 10
Unresolved:   0
Deferred:     0
```

The ten `Recommended` requirements are exactly: `KBDL-CMP-015`, `017`,
`020`, `025`, `029`, `036`, `041`, `044`, `046`, `048` — each mapped to
exactly one item in the
[KBDL-007 decision packet](#35-kbdl-007-decision-packet),
[§35.5](#355-decision-packet-coverage-audit).

- **KBDL-CMP-001** — Every in-scope component **must** document the
  full shared contract in [§6](#6-shared-component-contract) (purpose,
  anatomy, states, interaction, accessibility, responsive, theme,
  motion, content, validation, status).
  - Lifecycle status: Approved (structural completeness requirement).
    Provenance: User-provided. Validation status: Not verified.
  - Related requirement: `KBDL-PRN-004`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§6](#6-shared-component-contract), [§7](#7-component-anatomy-model).
  - Validation method: Manual completeness review per component.

- **KBDL-CMP-002** — Native host-language semantics **must** be used
  when they satisfy the required behavior; ARIA **must** supplement,
  not replace, correct native semantics.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 4.1.2 and
    the WAI-ARIA First Rule of ARIA Use). Provenance: Confirmed.
    Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-003`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§5](#5-native-semantics-first-rule).
  - Validation method: Manual + automated static accessibility check
    once implemented.

- **KBDL-CMP-003** — Every component **must** have a programmatically
  determinable accessible name including any visible label text.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 4.1.2 and
    SC 2.5.3). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-003`, `KBDL-A11Y-028`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§10](#10-accessible-naming-and-description).
  - Validation method: Manual + automated static accessibility check
    once implemented.

- **KBDL-CMP-004** — Component states **must** follow the precedence and
  distinction rules in [§8](#8-component-state-model)/[§9](#9-interaction-state-priority);
  no state may be represented as another, and no state may depend on
  color alone.
  - Lifecycle status: Approved (directly restates the locked
    component-state-clarity rule). Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-PRN-005`, `KBDL-A11Y-006`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§8](#8-component-state-model), [§9](#9-interaction-state-priority).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-005** — This module **must not** fully specify KBDL-008
  surfaces (Card, Panel, Tooltip, Popover, Menu surface, Dialog, Drawer,
  Alert, Toast, Progress indicator, Table, Tree, Grid, Carousel, and
  similar); it defines only the trigger, field, action, or navigation-side
  contract needed for future composition.
  - Lifecycle status: Approved (scope-control requirement). Provenance:
    Confirmed. Validation status: Not applicable.
  - Related requirement: Not applicable.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§11](#11-kbdl-008-scope-boundary).
  - Validation method: Manual scope-compliance review (performed, see
    implementation report).

- **KBDL-CMP-006** — Every focusable component **must** show a visible
  focus indicator, meeting non-text contrast against every surface it
  can appear on, and **must not** have that indicator entirely obscured.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.4.7 and
    SC 2.4.11). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-009`, `KBDL-A11Y-010`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§12](#12-focus-behavior).
  - Validation method: Manual keyboard-focus review once implemented.

- **KBDL-CMP-007** — Every operable component **must** be fully
  keyboard-operable without a keyboard trap.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.1.1 and
    SC 2.1.2). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-016`, `KBDL-A11Y-017`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§13](#13-keyboard-interaction).
  - Validation method: Manual keyboard testing once implemented.

- **KBDL-CMP-008** — Every pointer-operable component **must** support
  pointer cancellation where applicable and **must** meet the target-size
  minimum or a documented exception.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.5.2 and
    SC 2.5.8). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-020`, `KBDL-A11Y-022`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§14](#14-pointer-and-touch-interaction).
  - Validation method: Manual pointer/touch testing once implemented.

- **KBDL-CMP-009** — Every component **must** preserve content priority,
  reflow, source order, and focus location across breakpoints, using
  only the approved named breakpoint roles.
  - Lifecycle status: Approved (directly restates `KBDL-RSP-001`,
    `006`, `007`, `020`). Provenance: Confirmed. Validation status: Not
    verified.
  - Related requirement: `KBDL-RSP-001`, `006`, `007`, `020`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§15](#15-responsive-behavior).
  - Validation method: Manual reflow/zoom testing once implemented.

- **KBDL-CMP-010** — Pointer targets **must** meet the 24-by-24
  CSS-pixel minimum or a documented WCAG exception; the unapproved
  44-by-44 preference **must not** be treated as a KBDL minimum.
  - Lifecycle status: Approved (directly restates `KBDL-A11Y-020`).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-020`, `KBDL-A11Y-021`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§16](#16-target-size-handling).
  - Validation method: Manual measurement once implemented.

- **KBDL-CMP-011** — Every component **must** map its visual roles to
  existing approved semantic theme roles; no new color, opacity, token,
  or forced-colors policy may be introduced.
  - Lifecycle status: Approved (directly restates the approved theme
    architecture). Provenance: Confirmed. Validation status: Not
    verified.
  - Related requirement: `KBDL-THM-007`, `KBDL-THM-008`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§17](#17-theme-and-contrast-behavior).
  - Validation method: Manual theme-role mapping review once
    implemented.

- **KBDL-CMP-012** — Every component **must** use existing approved
  foundation values (typography, spacing, shape, elevation, icon
  sizing); no new foundation value may be introduced.
  - Lifecycle status: Approved (directly restates the approved
    foundation architecture). Provenance: Confirmed. Validation status:
    Not verified.
  - Related requirement: `KBDL-FND-003`, `009`, `010`, `011`, `012`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§18](#18-foundation-behavior).
  - Validation method: Manual foundation-mapping review once
    implemented.

- **KBDL-CMP-013** — Every applicable component **must** document
  motion necessity, purpose, hierarchy level, and full/reduced/no-motion
  behavior, using only the approved motion architecture.
  - Lifecycle status: Approved (structural requirement — the obligation
    to document motion necessity/purpose/hierarchy/parity per component
    is itself Approved; the *exact* component-specific duration,
    distance, scale, stagger, easing, choreography, or rendering-technology
    mapping for any individual component is **not** newly approved by
    this requirement where no prior approved KBDL rule already supplies
    it — such exact mappings remain governed by the existing motion
    unresolved/not-approval-ready items in
    [motion/README.md §10.3](motion/README.md#103-unresolved-or-not-approval-ready)
    and this module's own
    [§36](#36-deferred-and-unresolved-items)). Provenance: Confirmed.
    Validation status: Not verified.
  - Related requirement: `KBDL-MOT-001`, `KBDL-MOT-005`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§19](#19-motion-behavior).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-014** — Button anatomy, semantics, keyboard, pointer,
  focus, theme, and motion behavior **must** follow
  [§20.1](#201-button).
  - Lifecycle status: Approved (core restates native-semantics-first
    and state-model rules). Provenance: Confirmed. Validation status:
    Not verified.
  - Related requirement: `KBDL-CMP-002`, `004`, `006`, `007`, `008`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§20.1](#201-button).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-015** — A button hierarchy taxonomy (Primary, Secondary,
  Tertiary, Destructive) is proposed for [§20.1](#201-button).
  - Lifecycle status: Recommended (new component taxonomy). Provenance:
    Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-014`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§20.1](#201-button), [§35](#35-kbdl-007-decision-packet).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-CMP-016** — Icon buttons **must** have a programmatic
  accessible name independent of any tooltip surface.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 4.1.2).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-003`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§20.2](#202-icon-button).
  - Validation method: Manual + automated static accessibility check
    once implemented.

- **KBDL-CMP-017** — Icon-only actions whose meaning is not universally
  understood **should** use a visible label instead.
  - Lifecycle status: Recommended (new threshold guidance). Provenance:
    Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-016`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§20.2](#202-icon-button).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-CMP-018** — Toggle buttons **must** expose pressed/unpressed
  state via `aria-pressed`, distinct from checkbox and switch semantics.
  - Lifecycle status: Approved (directly restates WAI-ARIA). Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-004`, `030`, `032`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§20.3](#203-toggle-button).
  - Validation method: Manual ARIA review once implemented.

- **KBDL-CMP-019** — Links **must** have determinable purpose, correct
  current-location marking, and correct focus behavior.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.4.4).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-034`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§20.4](#204-link).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-020** — Button-group composition guidance (labeling, tab
  order, primary-action clarity, destructive separation) is proposed for
  [§20.5](#205-button-group).
  - Lifecycle status: Recommended (new composition guidance).
    Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-014`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§20.5](#205-button-group),
    [§35](#35-kbdl-007-decision-packet) item 9.
  - Validation method: Project-owner review (not yet performed).

- **KBDL-CMP-021** — Disclosure and menu triggers **must** expose
  expanded/collapsed state, an accessible name, and safe closing/focus
  restoration.
  - Lifecycle status: Approved (directly restates the WAI-ARIA
    disclosure pattern). Provenance: Confirmed. Validation status: Not
    verified.
  - Related requirement: `KBDL-CMP-006`, `007`, `012`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§20.6](#206-disclosure-and-menu-triggers).
  - Validation method: Manual keyboard review once implemented.

- **KBDL-CMP-022** — Every form field **must** document the shared
  field model (label, description, instructions, validity, errors,
  grouping).
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 3.3.2, SC
    1.3.5, SC 3.3.7). Provenance: Confirmed. Validation status: Not
    verified.
  - Related requirement: `KBDL-A11Y-028`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§21](#21-form-architecture).
  - Validation method: Manual + automated static check once
    implemented.

- **KBDL-CMP-023** — Text-input semantics, labeling, and error
  association **must** follow [§22.1](#221-text-input).
  - Lifecycle status: Approved. Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-022`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.1](#221-text-input).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-024** — Password inputs **must** support password managers,
  paste, and must not force an unsupported cognitive-function test.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 3.3.8).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-032`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.2](#222-password-input).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-025** — A search-field contract (labeling, submit, clear,
  filtering-vs-navigation distinction) is proposed for
  [§22.3](#223-search-field).
  - Lifecycle status: Recommended (new component taxonomy). Provenance:
    Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-023`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.3](#223-search-field).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-CMP-026** — Textarea semantics, labeling, and error association
  **must** follow [§22.4](#224-textarea).
  - Lifecycle status: Approved. Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-022`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.4](#224-textarea).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-027** — Native select **must** be preferred over a custom
  combobox where it satisfies the requirement.
  - Lifecycle status: Approved (directly restates native-semantics-first).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-002`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.5](#225-select).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-028** — A custom combobox **must** follow the applicable
  WAI-ARIA combobox role, state, property, and keyboard contract in
  full.
  - Lifecycle status: Approved (directly restates WAI-ARIA/APG).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-002`, `027`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.6](#226-combobox-boundary).
  - Validation method: Manual ARIA/keyboard review once implemented.

- **KBDL-CMP-029** — The threshold for when a custom combobox is
  justified over native select is proposed in
  [§22.6](#226-combobox-boundary).
  - Lifecycle status: Recommended (new threshold guidance). Provenance:
    Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-028`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.6](#226-combobox-boundary).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-CMP-030** — Checkbox semantics (checked/unchecked/mixed,
  keyboard, label activation) **must** follow
  [§22.7](#227-checkbox).
  - Lifecycle status: Approved. Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-022`, `004`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.7](#227-checkbox).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-031** — Radio-group semantics (mutual exclusivity, group
  label, arrow-key behavior) **must** follow
  [§22.8](#228-radio-group).
  - Lifecycle status: Approved. Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-022`, `004`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.8](#228-radio-group).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-032** — Switch semantics (immediate effect, on/off,
  distinct from checkbox/toggle button) **must** follow
  [§22.9](#229-switch).
  - Lifecycle status: Approved (directly restates WAI-ARIA switch
    role). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-018`, `030`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.9](#229-switch).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-033** — File-input semantics, labeling, and privacy
  guidance **must** follow [§22.10](#2210-file-input).
  - Lifecycle status: Approved. Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-022`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.10](#2210-file-input).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-034** — Field-group semantics (labeling, grouping, error)
  **must** follow [§22.11](#2211-field-group).
  - Lifecycle status: Approved. Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-022`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.11](#2211-field-group).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-035** — Form action rows **must** prevent double
  submission and clearly distinguish primary, secondary, and destructive
  actions.
  - Lifecycle status: Approved (behavioral requirement). Provenance:
    Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-014`, `020`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.12](#2212-form-action-row).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-036** — Exact responsive reflow ordering for form action
  rows is proposed in [§22.12](#2212-form-action-row).
  - Lifecycle status: Recommended (new component-level guidance).
    Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-035`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§22.12](#2212-form-action-row).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-CMP-037** — Form errors **must** be identified, described,
  associated with fields, recoverable, and never communicated by color
  alone.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 3.3.1, SC
    3.3.3, SC 3.3.4, SC 3.3.7, SC 4.1.3). Provenance: Confirmed.
    Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-029`, `030`, `031`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§23](#23-form-validation-and-recovery).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-038** — A skip link **must** provide first-focus bypass
  behavior to the main content landmark.
  - Lifecycle status: Approved (directly restates WCAG 2.2 SC 2.4.1).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-A11Y-018`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24.1](#241-skip-link).
  - Validation method: Manual keyboard testing once implemented.

- **KBDL-CMP-039** — Navigation links and lists **must** use list
  semantics, consistent order, and correct current-location marking.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-019`, `KBDL-A11Y-034`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24.2](#242-navigation-link-and-list).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-040** — Primary/global navigation **must** use a labeled
  landmark, preserve meaning and focus across responsive adaptation.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-RSP-008`, `KBDL-CMP-021`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24.3](#243-primary-or-global-navigation).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-041** — The exact collapse-trigger width for primary
  navigation depends on the unapproved `KBDL-RSP-002`/`008` and remains
  proposed only.
  - Lifecycle status: Recommended (depends on unapproved responsive
    values). Provenance: Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-RSP-002`, `KBDL-RSP-008`, `KBDL-CMP-040`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24.3](#243-primary-or-global-navigation).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-CMP-042** — Local/section navigation **must** use a distinctly
  labeled landmark where more than one navigation region exists.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-039`, `040`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24.4](#244-local-or-section-navigation).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-043** — Breadcrumb **must** use ordered-list semantics and
  correctly mark the current (non-link) item.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-019`, `039`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24.5](#245-breadcrumb).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-044** — A breadcrumb truncation model that preserves access
  to every hierarchy level is proposed in
  [§24.5](#245-breadcrumb).
  - Lifecycle status: Recommended. Provenance: Assumed. Validation
    status: Not applicable.
  - Related requirement: `KBDL-CMP-043`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24.5](#245-breadcrumb).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-CMP-045** — Tabs **must** use the tablist/tab/tabpanel role
  relationship with correct selected-state exposure and arrow-key
  navigation.
  - Lifecycle status: Approved (directly restates the WAI-ARIA tabs
    pattern). Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-CMP-004`, `007`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24.6](#246-tabs).
  - Validation method: Manual keyboard/ARIA review once implemented.

- **KBDL-CMP-046** — Whether tabs use automatic or manual activation is
  proposed in [§24.6](#246-tabs).
  - Lifecycle status: Recommended (new component choice). Provenance:
    Assumed. Validation status: Not applicable.
  - Related requirement: `KBDL-CMP-045`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24.6](#246-tabs).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-CMP-047** — Pagination **must** use a labeled landmark and
  correctly mark the current page.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-019`, `039`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24.7](#247-pagination).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-048** — A pagination truncation model that never hides the
  existence of additional pages is proposed in
  [§24.7](#247-pagination).
  - Lifecycle status: Recommended. Provenance: Assumed. Validation
    status: Not applicable.
  - Related requirement: `KBDL-CMP-047`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24.7](#247-pagination).
  - Validation method: Project-owner review (not yet performed).

- **KBDL-CMP-049** — A back link's destination **must** be
  determinable from its text, distinct from browser Back.
  - Lifecycle status: Approved. Provenance: Confirmed. Validation
    status: Not verified.
  - Related requirement: `KBDL-CMP-019`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§24.8](#248-back-link).
  - Validation method: Manual review once implemented.

- **KBDL-CMP-050** — Composing in-scope components **must not** alter
  any individual component's accessible-name, keyboard, or state
  requirements.
  - Lifecycle status: Approved (restates the shared contract applied
    compositionally). Provenance: Confirmed. Validation status: Not
    applicable.
  - Related requirement: `KBDL-CMP-001`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§25](#25-cross-component-composition-rules).
  - Validation method: Manual composition review once implemented.

- **KBDL-CMP-051** — Showcase, Precision, and Flow **must** share one
  semantic and accessibility architecture for all core components.
  - Lifecycle status: Approved (directly restates
    [principles.md §9.4](principles.md#94-shared-constraints-across-profiles)).
    Provenance: Confirmed. Validation status: Not verified.
  - Related requirement: `KBDL-PRN-007`.
  - Applicable profiles: Showcase, Precision, Flow.
  - Specification location: [§26](#26-profile-compatibility).
  - Validation method: Manual cross-profile review once the
    project-profiles module is approved.

## 31. Component Coverage Matrix (see §29)

Cross-reference only; the full matrix is in
[§29](#29-component-coverage-matrix).

## 32. Accessibility Validation Matrix

| Requirement group | Validation method | Status |
| --- | --- | --- |
| Native semantics / name/role/value (`KBDL-CMP-002`, `003`) | Automated static check + manual screen-reader review | Not verified — no implementation exists |
| Focus visibility/order/restoration (`KBDL-CMP-006`) | Manual keyboard-focus review | Not verified |
| Keyboard operability (`KBDL-CMP-007`) | Manual keyboard testing | Not verified |
| Pointer/target size (`KBDL-CMP-008`, `010`) | Manual measurement/testing | Not verified |
| Form errors/labels (`KBDL-CMP-022`, `037`) | Manual + automated static check | Not verified |
| ARIA widget patterns (combobox, tabs, disclosure) | Manual ARIA/keyboard review | Not verified |

No implementation exists to test against; this matrix records intended
validation methods only.

## 33. Responsive Validation Matrix

| Requirement | Validation method | Status |
| --- | --- | --- |
| `KBDL-CMP-009` (content priority/reflow/focus) | Manual reflow/zoom testing | Not verified |
| `KBDL-CMP-041` (navigation collapse threshold) | Project-owner review + manual testing | Not verified; pending approval |
| Component reflow at named breakpoints (all components) | Manual review across `compact`/`standard`/`expanded`/`wide` | Not verified |

## 34. Theme and Motion Validation Matrix

| Requirement | Validation method | Status |
| --- | --- | --- |
| `KBDL-CMP-011` — Approved theme-role documentation requirement | Manual mapping review against approved semantic roles | Not verified |
| `KBDL-CMP-013` — Approved motion-documentation and parity requirement | Manual review confirming purpose/level/parity documented | Not verified |
| Exact component-specific motion values or mappings not inherited from an already-approved KBDL requirement (durations, distances, scales, stagger, easing, choreography) | Manual review; remain unapproved and outside implementation authority per [motion/README.md §10.3](motion/README.md#103-unresolved-or-not-approval-ready) and [§36](#36-deferred-and-unresolved-items) | Not applicable — no such mapping is approved or proposed as approved by this document |

## 35. KBDL-007 Decision Packet

### 35.1 Already-Approved Component Architecture (context only)

Not awaiting approval — provided as context. Directly supported by
prior approved decisions: the shared component contract structure
(`KBDL-CMP-001`); native-semantics-first (`KBDL-CMP-002`); accessible
naming (`KBDL-CMP-003`); the state model (`KBDL-CMP-004`); the KBDL-008
scope boundary (`KBDL-CMP-005`); focus, keyboard, and pointer behavior
(`KBDL-CMP-006`–`008`); responsive/target-size/theme/foundation mapping
(`KBDL-CMP-009`–`012`); Button, Icon Button (core), Toggle Button, Link,
Disclosure/Menu Trigger (core), the form field model, Text Input,
Password Input, Textarea, Select, Combobox (ARIA contract only),
Checkbox, Radio Group, Switch, File Input, Field Group, Form Action Row
(core), form validation/recovery, Skip Link, Navigation Link/List,
Primary Navigation (core), Local Navigation, Breadcrumb (core), Tabs
(core), Pagination (core), Back Link, composition rules, and profile
consistency.

### 35.2 Recommended Decisions — Ready for Approval

| # | Decision | Recommendation | Rationale | Alternatives | Trade-offs | Accessibility impact | Responsive impact | Theme impact | Motion impact | Security impact | Profile impact | Dependencies | Exact affected requirements | Approval scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Button hierarchy taxonomy | Adopt Primary/Secondary/Tertiary/Destructive as the button-variant taxonomy (`KBDL-CMP-015`) | Gives a consistent, small vocabulary for action prominence across the system | An unbounded/ad hoc variant set (rejected — fragments consistency) | Requires per-project mapping to visual treatment once themes are implemented | Destructive variant must still map to Critical status + action role, unaffected either way | None | None | None | None | Showcase may use more variants visibly; Precision favors Primary/Secondary only | None | `KBDL-CMP-015` | Item 1 only |
| 2 | Tabs activation model | Adopt manual activation (arrow keys move focus; a separate key/click activates the panel) as the default, per APG guidance for asynchronous panel content (`KBDL-CMP-046`) | Reduces unintended panel loads while navigating with arrow keys, per APG recommendation for panels with non-trivial load cost | Automatic activation (rejected as the sole default — can trigger unwanted loads while arrow-key browsing, though valid for lightweight panels) | Requires clear instructions/affordance for users on how to activate a focused-but-not-yet-active tab | None beyond APG's own guidance, which this follows | None | None | None | None | Applies identically across profiles | `KBDL-CMP-045` | `KBDL-CMP-046` | Item 2 only |
| 3 | Icon-only visible-label threshold | Adopt a qualitative threshold: universally understood actions (e.g., close, search) may remain icon-only; anything else requires a visible label (`KBDL-CMP-017`) | Balances compact icon-only density against discoverability | Icon-only always requiring a label (rejected — overly verbose for extremely common actions); no threshold at all (rejected — risks ambiguous icon-only actions) | Requires an enumerated "universally understood" list eventually, not yet produced | Directly serves discoverability; the accessible-name requirement (`KBDL-CMP-016`) is unaffected either way | None | None | None | None | Precision/Flow lean toward more visible labels; Showcase may use more icon-only in controlled contexts | `KBDL-CMP-016` | `KBDL-CMP-017` | Item 3 only |
| 4 | Search-field model (filtering vs. navigation) | Adopt both models as valid, selected per use case, with the field contract in §22.3 (`KBDL-CMP-025`) | Reflects real product needs without forcing one universal search behavior | A single mandated model (rejected — too restrictive for different search contexts) | Requires clear per-instance documentation of which model applies | Result/loading-status boundary with KBDL-008 remains unaffected | None | None | None | None | Applies identically across profiles | None | `KBDL-CMP-025` | Item 4 only |
| 5 | Combobox-justification threshold | Adopt a threshold: a custom combobox is justified only when native select cannot support filtering/searching within a large option set (`KBDL-CMP-029`) | Keeps native select as the default, reserving the added ARIA complexity for genuine need | No threshold, leaving it to implementer judgment (rejected — invites unnecessary custom widgets) | Requires implementers to document why native select was insufficient | Reinforces native-semantics-first; the ARIA contract itself (`KBDL-CMP-028`) is unaffected | None | None | None | None | Applies identically across profiles | `KBDL-CMP-028` | `KBDL-CMP-029` | Item 5 only |
| 6 | Form action row reflow order | Adopt primary action first (top or leading) at every breakpoint, with secondary/cancel following, reversing to a stacked column at `compact` (`KBDL-CMP-036`) | Keeps the primary action most reachable and visually first regardless of viewport | Reversing order at `compact` (rejected — de-emphasizes the primary action exactly where thumb reach matters most) | None significant | None beyond what §23 already requires | Depends on eventual approved breakpoint values for exact stacking point | None | None | None | Applies identically across profiles | `KBDL-RSP-002` (eventual) | `KBDL-CMP-036` | Item 6 only |
| 7 | Breadcrumb truncation model | Adopt collapsing middle levels behind a single overflow control (e.g., an ellipsis trigger) that reveals all hidden levels, never removing them (`KBDL-CMP-044`) | Preserves full hierarchy access while managing space at `compact` | Silently dropping middle levels (rejected — loses navigable history); horizontal scroll (rejected — awkward for a short list) | Overflow trigger itself must follow the Disclosure Trigger contract | Overflow trigger inherits the already-Approved disclosure accessibility contract | Depends on approved breakpoint values for exact trigger point | None | None | None | Applies identically across profiles | `KBDL-CMP-021` | `KBDL-CMP-044` | Item 7 only |
| 8 | Pagination truncation model | Adopt an ellipsis-based truncation showing first, last, current, and immediate neighbors, with the ellipsis itself non-interactive text (`KBDL-CMP-048`) | Common, well-understood pattern that preserves orientation without excessive control count | Showing every page number always (rejected — unusable for very large sets); a "load more" model only (rejected — loses direct page access) | None significant | Ellipsis must not be the only way to reach hidden pages — a documented current-page/total-count text should remain available | None | None | None | None | Applies identically across profiles | `KBDL-CMP-047` | `KBDL-CMP-048` | Item 8 only |
| 9 | Button-group composition guidance | Adopt the labeling, tab-order, primary-action-clarity, and destructive-action-separation guidance in [§20.5](#205-button-group) (`KBDL-CMP-020`) | Gives related-action groups a consistent, predictable composition pattern | No composition guidance, left entirely to per-project judgment (rejected — risks inconsistent action-group density and unclear primary-action prominence across projects) | None significant | Primary-action clarity and destructive-action separation directly support comprehension and error prevention | None | None | None | None | Applies identically across profiles | `KBDL-CMP-014` | `KBDL-CMP-020` | Item 9 only |

### 35.3 Unresolved or Not Approval-Ready

- **Navigation collapse-trigger threshold (contingent, not
  independently approval-ready)** — maps to `KBDL-CMP-041`, which
  remains `Recommended`. It reuses `KBDL-RSP-008`'s proposed
  navigation-collapse guidance for the primary-navigation trigger and
  therefore **depends directly on unapproved `KBDL-RSP-002` and
  `KBDL-RSP-008`**. It **cannot be approved independently through the
  KBDL-007 packet** and may become approval-ready only after the
  relevant KBDL-006 responsive decisions (`KBDL-RSP-002`, `KBDL-RSP-008`)
  are themselves approved or replaced. It grants no implementation
  authority and does not approve any exact collapse width or breakpoint.
  Related: `KBDL-RSP-002`, `KBDL-RSP-008`.

- **Preferred enhanced target size for primary actions (contingent, not
  independently approval-ready)** — adopting the KBDL-006 `KBDL-A11Y-021`
  44-by-44 preference specifically for Button and Icon Button primary
  variants, once `KBDL-A11Y-021` itself is approved. This item is
  **contingent on an unapproved KBDL-006 recommendation** and therefore
  **cannot be approved independently through the KBDL-007 packet**. It
  does **not** map to an additional `Recommended` `KBDL-CMP-###`
  lifecycle record — `KBDL-CMP-010` (the WCAG 24×24 minimum) remains
  `Approved` and unaffected by this item either way, regardless of
  whether `KBDL-A11Y-021` is ever approved. It remains outside the exact
  scope of any KBDL-007 packet approval and grants no implementation
  authority. Related: `KBDL-A11Y-021`, `KBDL-CMP-010`, `014`, `016`.

- **Exact component dimensions not inherited from foundations** (e.g.,
  precise textarea minimum height) — depend on foundation values not
  yet finalized; out of scope here.
- **Exact component-specific motion durations/distances/curves** — the
  underlying motion-pattern-matrix rows themselves remain `Recommended`
  ([motion/patterns.md §12](motion/patterns.md#12-motion-pattern-matrix));
  not re-proposed here.
- **Implementation-layer token formats, CSS architecture, JavaScript
  behavior, package structure, framework APIs** — explicitly out of
  scope for a design-language specification.
- **Browser-support matrix** — not proposed.
- **Product-specific or profile-specific component variants** —
  deferred to the later Project Profiles module (`PRO`).
- **Actual screen-reader/browser test matrix** — depends on
  `KBDL-A11Y-035`, itself unapproved.
- **Implementation-level accessibility, real-device, and production
  conformance validation** — require an implementation that does not
  exist yet.
- **Use of any of the nine unapproved KBDL-006 recommendations**
  (`KBDL-RSP-002`–`005`, `008`, `011`; `KBDL-A11Y-011`, `021`, `035`) as
  implementation authority — explicitly excluded throughout this
  document; see [§35.4](#354-kbdl-006-approval-boundary-audit).

### 35.4 KBDL-006 Approval-Boundary Audit

| KBDL-006 requirement | Where referenced in this document | How handled |
| --- | --- | --- |
| `KBDL-RSP-002` (exact breakpoint thresholds) | [§15](#15-responsive-behavior), [§24.3](#243-primary-or-global-navigation), decision packet item 6, [§35.3](#353-unresolved-or-not-approval-ready) contingent item | Cited only as unapproved; not required; collapse trigger left as `Recommended` (`KBDL-CMP-041`), moved to the contingent, not-approval-ready section |
| `KBDL-RSP-003` (grid columns) | Not referenced | Not used |
| `KBDL-RSP-004` (container widths) | Not referenced | Not used |
| `KBDL-RSP-005` (gutters) | Not referenced | Not used |
| `KBDL-RSP-008` (navigation collapse thresholds) | [§24.3](#243-primary-or-global-navigation), [§35.3](#353-unresolved-or-not-approval-ready) contingent item | Cited only as unapproved; component's exact collapse point left `Recommended` (`KBDL-CMP-041`), not part of the nine approval-ready packet items |
| `KBDL-RSP-011` (data-dense strategy) | Not referenced (no data-table component in KBDL-007 scope) | Not used |
| `KBDL-A11Y-011` (forced-colors policy) | Not referenced | Not used |
| `KBDL-A11Y-021` (44×44 preferred target) | [§16](#16-target-size-handling), [§35.3](#353-unresolved-or-not-approval-ready) contingent item | Cited explicitly as unapproved; not required; only proposed as a contingent, not-independently-approvable future enhancement — not part of the nine approval-ready packet items |
| `KBDL-A11Y-035` (preferred testing matrix) | [§35.3](#353-unresolved-or-not-approval-ready) | Cited only as a dependency for future validation, not used normatively |

None of the nine is treated as implementation authority anywhere in
this document.

### 35.5 Decision-Packet Coverage Audit

```text
CMP requirements: 51
Approved: 41
Recommended: 10

Independently approval-ready Recommended requirements: 9
Contingent Recommended requirements: 1
```

Every `Recommended` `KBDL-CMP-###` requirement maps to exactly one
packet item — either an independently approval-ready item in
[§35.2](#352-recommended-decisions--ready-for-approval) or the single
contingent item in
[§35.3](#353-unresolved-or-not-approval-ready) — and every
approval-ready packet item maps to exactly one `Recommended`
requirement:

| Recommended requirement | Packet item | Independently approval-ready | Dependency |
| --- | --- | --- | --- |
| `KBDL-CMP-015` | 1 | Yes | None |
| `KBDL-CMP-046` | 2 | Yes | None |
| `KBDL-CMP-017` | 3 | Yes | None |
| `KBDL-CMP-025` | 4 | Yes | None |
| `KBDL-CMP-029` | 5 | Yes | None |
| `KBDL-CMP-036` | 6 | Yes | None (eventual `KBDL-RSP-002` value affects exact stacking point only, not the ordering rule itself) |
| `KBDL-CMP-044` | 7 | Yes | None |
| `KBDL-CMP-048` | 8 | Yes | None |
| `KBDL-CMP-020` | 9 | Yes | None |
| `KBDL-CMP-041` | Contingent item ([§35.3](#353-unresolved-or-not-approval-ready)) | No — depends on unapproved `KBDL-RSP-002` and `KBDL-RSP-008` for its own approval | `KBDL-RSP-002`, `KBDL-RSP-008` |

Nine `Recommended` requirements map one-to-one to the nine
approval-ready packet items; one `Recommended` requirement
(`KBDL-CMP-041`) maps once to the non-approval-ready contingent item.
No `Recommended` requirement is orphaned, no approval-ready packet item
is orphaned, no `Approved` `KBDL-CMP-###` requirement is presented as
awaiting approval, and no KBDL-006 recommendation is presented as
approved. The separate contingent enhanced-target item
([§35.3](#353-unresolved-or-not-approval-ready)) is **not** counted as
an eleventh `Recommended` requirement — `KBDL-CMP-010` (the WCAG
minimum it references) is `Approved`, not `Recommended`, and is
unaffected regardless of whether that contingent item is ever approved.

**Exact scope of a future approval:** an `APPROVE` response to
[§35.2](#352-recommended-decisions--ready-for-approval) would authorize
exactly items 1–9 above. It would **not** approve `KBDL-CMP-041`, the
contingent navigation-collapse item, the contingent enhanced-target
item, any other
[§35.3](#353-unresolved-or-not-approval-ready) item, any of the nine
KBDL-006 recommendations, any KBDL-008-or-later content, any
implementation validation, or any recommendation not explicitly listed
in [§35.2](#352-recommended-decisions--ready-for-approval). It would
not itself constitute validation of any item — see
[§32](#32-accessibility-validation-matrix)–[§34](#34-theme-and-motion-validation-matrix).

## 36. Deferred and Unresolved Items

- KBDL-008 surfaces and overlays (Card, Panel, Tooltip, Popover, Menu
  surface, Dialog, Drawer, Alert, Toast, Progress indicator, Table,
  Tree, Grid, Carousel, and similar) — now specified in
  [components-system.md](components-system.md); no longer `Deferred`.
- Feedback and system-state components — now specified in
  [components-system.md](components-system.md); no longer `Deferred`.
- Exact component-specific motion values — `Recommended`/`Unresolved`,
  depend on the underlying motion-pattern-matrix rows themselves being
  `Recommended`.
- Exact component dimensions not inherited from foundations —
  `Unresolved`.
- Implementation-layer token formats, framework APIs, CSS architecture,
  JavaScript behavior, package structure — out of scope.
- Browser-support matrix — not proposed.
- Product-specific and profile-specific component variants —
  `Deferred` to the Project Profiles module.
- Actual screen-reader/browser test matrix — depends on unapproved
  `KBDL-A11Y-035`.
- Implementation-level accessibility validation, real-device
  validation, production conformance — `Not verified`, no
  implementation exists.
- Any use of the nine unapproved KBDL-006 recommendations as
  implementation authority — explicitly excluded throughout.
- The preferred enhanced target size for primary actions
  ([§35.3](#353-unresolved-or-not-approval-ready)) — contingent on the
  unapproved `KBDL-A11Y-021`; not independently approval-ready and not a
  separate `Recommended` `KBDL-CMP-###` requirement.
- The navigation collapse-trigger threshold (`KBDL-CMP-041`,
  [§35.3](#353-unresolved-or-not-approval-ready)) — remains
  `Recommended`, but is contingent on the unapproved `KBDL-RSP-002` and
  `KBDL-RSP-008`; not independently approval-ready through the KBDL-007
  packet.

## 37. Security and Privacy in Components

Future component implementations **must**: avoid exposing credentials
or sensitive values in component state examples; support password
managers and paste in authentication controls
([§22.2](#222-password-input)); distinguish client-side validation
from security validation — client-side checks are a UX convenience,
never a substitute for server-side authorization; avoid presenting
disabled UI as an authorization boundary (a disabled button is not
access control); avoid assuming hidden UI is secure; preserve
server-side authorization requirements; avoid leaking sensitive form
values through labels, error messages, or status messages; treat
destructive actions clearly and require review/confirmation/reversal
for consequential actions where applicable
([§23](#23-form-validation-and-recovery)); preserve user-entered data
after recoverable errors; avoid automatic submission caused merely by
focus; avoid unexpected context changes caused by selection. This
document does not define authentication architecture, authorization
architecture, data storage, or backend security.

## 38. Traceability

See [traceability-matrix.md](traceability-matrix.md) for how each
`KBDL-CMP-###` requirement traces to its blueprint origin, approval
status, validation status, and evidence, and
[decision-register.md](decision-register.md) for any decision recorded
as part of this module.
