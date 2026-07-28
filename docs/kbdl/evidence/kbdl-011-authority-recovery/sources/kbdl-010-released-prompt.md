# IMPLEMENTATION PROMPT KBDL-010

## Role

Act as a senior:

* Design-language governance architect
* Manual-customization policy architect
* Cross-project design-system strategist
* Requirements lifecycle and provenance analyst
* Accessibility governance reviewer
* Responsive-design reviewer
* Theme and visual-foundation reviewer
* Motion-system reviewer
* Component-system reviewer
* Project Profile reviewer
* Security, privacy, and correctness reviewer
* Change-management and exception-process specialist
* Technical writer
* Traceability and documentation QA engineer
* Git configuration-control reviewer

You are defining framework-neutral governance and documentation requirements for manually customizing a KBDL-based project.

You are not:

* Implementing a customized project
* Creating design tokens
* Writing CSS or application code
* Creating automated theming
* Creating configuration generators
* Creating profile variants
* Approving pending recommendations
* Performing final KBDL validation
* Beginning any later roadmap item

## Current Project Context

KBDL is a reusable, framework-neutral web design language.

Validated specification steps:

* KBDL-001 — Specification architecture and governance
* KBDL-002 — Identity, principles, and visual consistency
* KBDL-003 — Core visual foundations
* KBDL-004 — Adaptive theme system
* KBDL-005 — Expressive motion language
* KBDL-006 — Responsive behavior and accessibility
* KBDL-007 — Core action, form, and navigation components
* KBDL-008 — Surface, overlay, feedback, system-state, and complex-presentation components
* KBDL-009 — Project Profiles

KBDL-010 is the next unlocked roadmap item:

> Manual Customization

Its planned document location is:

```text
docs/kbdl/customization.md
```

Its requirement module code is:

```text
CUS
```

The approved high-level customization decision is:

> Customization is performed manually and must be documented, rather than automated or silent.

KBDL-010 must turn that decision into a complete, framework-neutral specification for project-level customization.

It must preserve:

* KBDL’s locked identity rules
* The design-decision hierarchy
* One shared semantic architecture
* One shared accessibility architecture
* Shared foundation, theme, motion, responsive, and component systems
* Project Profile invariants
* Every prior lifecycle status
* Every pending recommendation status
* Governance approval and exception requirements
* Validation status as a dimension separate from lifecycle approval

KBDL-010 must not turn project customization into a way to bypass KBDL.

## Current Repository State

Expected baseline, subject to inspection:

* Repository: `kbmanilla06/kbdl`
* Branch: `main`
* Last validated commit: `907708c9a9db8004a7f03a36c54fb1a265fe7a9a`
* Working tree: clean
* Remote branch: synchronized
* `docs/kbdl/customization.md`: absent
* Existing `KBDL-CUS-###` requirements: none known
* `docs/kbdl/validation.md`: absent
* KBDL-011 and later work: not started

The current repository may still contain text saying that KBDL-009 is under validation and that KBDL-010 is locked. The planning agent has now validated KBDL-009 and unlocked KBDL-010.

Inspect the repository rather than assuming this expected state.

If commits exist after `907708c`:

1. Fetch current remote references.
2. Inspect every newer commit.
3. Preserve authorized collaborator work.
4. Do not reset the repository to `907708c`.
5. Stop and report conflicting KBDL-010 work.
6. Stop and report any final-validation or later-roadmap implementation.
7. Do not overwrite, broadly reformat, discard, or silently replace newer work.

## Objective

Create KBDL’s complete Manual Customization specification.

The completed step must:

1. Create `docs/kbdl/customization.md`.
2. Define what manual customization means in KBDL.
3. Distinguish customization from Project Profiles, themes, user preferences, open brand expression, controlled variables, implementation configuration, and governance exceptions.
4. Define a complete manual customization workflow.
5. Define the required project-level customization record.
6. Classify customization requests by authority and risk.
7. Define permitted customization within Approved bounds.
8. Define prohibited or escalation-required customization.
9. Preserve all locked rules and shared architecture.
10. Preserve all three Project Profile invariants.
11. Protect accessibility, responsive behavior, security, privacy, correctness, and performance.
12. Define how controlled customization interacts with foundations, themes, motion, responsive behavior, components, profiles, and content.
13. Define when a request is merely a selection of an existing Approved option.
14. Define when a request becomes a new KBDL proposal.
15. Define when a request requires an approved exception.
16. Define documentation, ownership, review, evidence, rollback, and change-history requirements.
17. Add stable `KBDL-CUS-###` requirements.
18. Classify inherited, prompt-mandated, discretionary, contingent, unresolved, and deferred policy accurately.
19. Create a KBDL-010 decision packet.
20. Separate independently approval-ready items from contingent items.
21. Audit every pending earlier-module recommendation.
22. Add a complete decision-packet coverage audit.
23. Add complete traceability for every CUS requirement.
24. Update the specification index, glossary, conformance checklist, traceability matrix, and stale customization deferrals.
25. Keep final validation and all later roadmap work locked.

## Authorization Gate

This released prompt is not authorization to begin implementation.

Implementation may begin only after the project owner responds:

```text
APPROVE PROMPT
```

Approval of this implementation prompt will authorize only the prompt’s mandatory KBDL-010 scope.

It will not approve:

* Any KBDL-010 decision-packet recommendation
* Any pending KBDL-009 recommendation
* Any pending KBDL-008 recommendation
* Any pending KBDL-007 recommendation
* Any pending KBDL-006 recommendation
* Any pending theme, motion, foundation, or accessibility item
* Any project-specific customization request
* Any locked-rule exception
* Any implementation technology

## Preconditions

Before editing:

1. Run `git fetch origin`.
2. Inspect configured remotes.
3. Confirm the active repository.
4. Confirm the active branch.
5. Confirm the working tree and index are clean.
6. Record local HEAD.
7. Record `origin/main`.
8. Confirm whether local HEAD equals `origin/main`.
9. Inspect the latest ten commits.
10. Inspect every commit after `907708c`, if any.
11. Confirm `docs/kbdl/customization.md` does not already contain authorized work.
12. Search the repository for every `KBDL-CUS-###` reference.
13. Confirm the current highest CUS ID, if any.
14. Confirm `docs/kbdl/validation.md` has not been created.
15. Search for other KBDL-011-or-later content.
16. Stop and report unexpected, uncommitted, conflicting, or collaborator-owned work.

Do not:

* Reset
* Rebase
* Amend
* Force-push
* Discard changes
* Overwrite teammate work
* Stash another contributor’s work
* Restore the repository to an earlier commit
* Rewrite `907708c`

## Source-of-Truth Hierarchy

Use this order:

1. Explicit project-owner approvals
2. Approved KBDL blueprint and roadmap
3. Planning-agent validation and progression decisions
4. Current repository and Git history
5. KBDL decision register
6. Approved per-requirement lifecycle records
7. KBDL governance and conventions
8. Approved KBDL principles and design-decision hierarchy
9. Current Project Profiles specification
10. Current foundation, theme, motion, responsive, accessibility, and component specifications
11. Existing repository conventions
12. Established governance and design-system practices

When sources conflict:

1. Stop work on the affected item.
2. Record the exact conflicting sources.
3. Identify every affected requirement and file.
4. Do not choose a lower-priority source silently.
5. Do not invent a customization permission.
6. Do not promote an unapproved value.
7. Do not create an exception without explicit approval.
8. Return the conflict for project-owner resolution.

## Lifecycle-Authority Model

Use KBDL’s three independent status dimensions:

* Lifecycle status
* Provenance
* Validation status

Only lifecycle status `Approved` authorizes implementation.

After explicit approval of this prompt, a `KBDL-CUS-###` requirement may be `Approved` when its complete normative rule is authorized by:

* A prior Approved KBDL requirement
* An Approved KBDL decision
* An explicit mandatory clause in the project-owner-approved KBDL-010 prompt
* A documented combination of these sources

Prompt approval does not approve the KBDL-010 decision packet.

New discretionary choices must remain:

* `Recommended`
* `Unresolved`
* `Deferred`
* `Blocked`

Examples of discretionary KBDL-010 policy include:

* A customization-record identifier format
* Project-level approval roles
* Minor versus material customization thresholds
* Review cadence
* Expiration policy
* Maximum customization-layer count
* Inheritance and override ordering between multiple project records
* Risk tiers
* Required evidence by risk tier
* Reusable customization-package governance
* Promotion of a project customization into shared KBDL
* Default handling of stale customization records
* Exception-renewal policy
* Automatic tooling or machine-readable formats

Assigning a CUS ID does not grant approval.

A customization record documenting a project choice does not grant the choice authority that its source requirement lacks.

Documentation review does not make implementation behavior `Verified`.

## Required Inspection

Read these files in full before writing:

* `docs/kbdl/README.md`
* `docs/kbdl/principles.md`
* `docs/kbdl/conventions.md`
* `docs/kbdl/governance.md`
* `docs/kbdl/contributing.md`
* `docs/kbdl/glossary.md`
* `docs/kbdl/decision-register.md`
* `docs/kbdl/traceability-matrix.md`
* `docs/kbdl/conformance-checklist.md`
* Every file under `docs/kbdl/foundations/`
* Every file under `docs/kbdl/themes/`
* Every file under `docs/kbdl/motion/`
* `docs/kbdl/responsive.md`
* `docs/kbdl/accessibility.md`
* `docs/kbdl/components-core.md`
* `docs/kbdl/components-system.md`
* `docs/kbdl/profiles.md`

Inspect every current occurrence of:

* `customization`
* `manual customization`
* `controlled customization`
* `controlled variable`
* `controlled option`
* `project override`
* `project-controlled`
* `open brand expression`
* `locked rule`
* `approved exception`
* `profile invariant`
* `profile exception`
* `project-specific`
* `future customization`
* `CUS`
* `KBDL-010`
* `implementation-layer`
* `token format`
* `manual and documented`
* `must not weaken`
* `must not override`
* `documentation requirement`
* `selection precedence`
* `scope-change process`
* `exception process`

At minimum inspect and reconcile:

* `KBDL-DEC-004`
* `KBDL-PRN-005`
* `KBDL-PRN-006`
* `KBDL-PRN-007`
* `KBDL-GOV-002`
* `KBDL-GOV-003`
* Foundation controlled-option guidance
* Theme project-override boundaries
* Motion hierarchy and safety constraints
* Responsive content-priority requirements
* Accessibility locked requirements
* Component semantic and anatomy contracts
* Project Profile locked, controlled, and open classifications
* Project Profile conflict and exception rules
* Every earlier-module non-Approved item

## Core Customization Principle

The KBDL-010 specification must establish:

> A project may customize only what KBDL has explicitly left controlled or open, and only within the owning module’s Approved bounds. Every customization must be manually chosen, documented, attributable, reviewable, reversible, and subordinate to all higher-priority requirements.

Customization must never:

* Create implementation authority
* Change a requirement’s lifecycle status
* Turn `Recommended` into `Approved`
* Turn `Unresolved` into a permitted option
* Turn `Deferred` into active scope
* Bypass an approval gate
* Weaken accessibility
* Weaken safety or data integrity
* Change semantic meaning
* Change shared component behavior
* Fragment profile architecture
* Create a second theme, motion, responsive, or component system
* Hide an exception
* Falsely claim conformance

## Approval Boundaries

KBDL-010 must preserve every earlier-module non-Approved status.

### KBDL-006 pending requirements

The following remain `Recommended`:

```text
KBDL-RSP-002
KBDL-RSP-003
KBDL-RSP-004
KBDL-RSP-005
KBDL-RSP-008
KBDL-RSP-011
KBDL-A11Y-011
KBDL-A11Y-021
KBDL-A11Y-035
```

KBDL-010 must not use customization to authorize:

* Exact breakpoint values
* Exact grid-column counts
* Exact gutters
* Exact container widths
* Exact navigation-collapse thresholds
* The pending data-dense transformation strategy
* The pending forced-colors policy
* The pending enhanced target size
* The pending accessibility test matrix

### KBDL-007 pending requirements

The following remain `Recommended`:

```text
KBDL-CMP-015
KBDL-CMP-017
KBDL-CMP-020
KBDL-CMP-025
KBDL-CMP-029
KBDL-CMP-036
KBDL-CMP-041
KBDL-CMP-044
KBDL-CMP-046
KBDL-CMP-048
```

`KBDL-CMP-041` remains contingent and not independently approval-ready.

KBDL-010 must not use customization to authorize:

* A button hierarchy taxonomy
* An icon-only visible-label threshold
* A button-group composition model
* A search-field model
* A custom-combobox justification threshold
* A form-action-row ordering model
* A navigation-collapse threshold
* Breadcrumb truncation
* Tabs activation policy
* Pagination truncation

### KBDL-008 pending requirements

The following remain `Recommended`:

```text
KBDL-CMP-067
KBDL-CMP-069
KBDL-CMP-073
KBDL-CMP-074
KBDL-CMP-076
KBDL-CMP-080
KBDL-CMP-083
KBDL-CMP-085
KBDL-CMP-089
KBDL-CMP-091
KBDL-CMP-099
KBDL-CMP-102
KBDL-CMP-105
KBDL-CMP-106
KBDL-CMP-108
KBDL-CMP-110
KBDL-CMP-111
```

KBDL-010 must not use customization to authorize:

* Card variants
* Accordion open models
* Tooltip timing
* Popover taxonomy
* Menu interaction policy
* Modal sizing or nesting
* Drawer/sheet taxonomy
* Overlay nesting limits
* Feedback severity taxonomy
* Toast persistence or queueing
* Empty-state taxonomy
* Recovery hierarchy
* Carousel auto-rotation
* Responsive surface transformation
* Grid-versus-table thresholds
* Treegrid thresholds
* Data-visualization interaction or palette policy

### KBDL-009 pending requirements

The following remain `Recommended`:

```text
KBDL-PRO-009
KBDL-PRO-016
KBDL-PRO-017
KBDL-PRO-018
KBDL-PRO-027
KBDL-PRO-028
KBDL-PRO-029
```

Their existing packet state must remain:

```text
KBDL-PRO-009 -> independently approval-ready
KBDL-PRO-017 -> independently approval-ready
KBDL-PRO-027 -> independently approval-ready
KBDL-PRO-028 -> independently approval-ready
KBDL-PRO-029 -> independently approval-ready
KBDL-PRO-016 -> contingent on KBDL-CMP-067
KBDL-PRO-018 -> contingent on KBDL-CMP-015 and KBDL-CMP-036
```

KBDL-010 must not use customization to authorize:

* Primary, secondary, or hybrid-profile policy
* Showcase composition defaults
* Precision density defaults
* Flow action defaults
* Profile change or migration policy
* Profile-selection rubric
* Profile-review cadence

### Other pending earlier-module items

Inventory and preserve every `Recommended`, `Unresolved`, `Deferred`, `Blocked`, `Deprecated`, or `Superseded` item in:

* Foundations
* Themes
* Motion
* Governance
* Responsive behavior
* Accessibility
* Components
* Project Profiles

At minimum preserve as non-Approved:

* Unverified theme opacity values
* Translucent theme variants
* High-contrast/forced-colors policy
* Data-visualization palettes
* Project-specific media composites not already Approved
* Account-level theme synchronization
* Exact component-specific motion values
* Device-performance detection
* Animation-library and rendering-technology choices
* CSS, JSON, JavaScript, or framework token formats
* Browser-support policy
* Exact quantitative motion-hazard thresholds
* Exact project typeface choice where unresolved
* Any implementation-level validation claim

## Exact Scope

## 1. Create the customization document

Create:

```text
docs/kbdl/customization.md
```

If it already exists:

1. Inspect it.
2. Determine whether it contains authorized collaborator work.
3. Preserve valid authorized content.
4. Stop and report conflicting implementations.

Do not replace the planned file with a directory unless an approved higher-priority source has changed the hierarchy.

## 2. Required document structure

The document must contain at least:

1. Purpose and scope
2. Lifecycle and validation status
3. Relationship to prior KBDL modules
4. Customization terminology
5. Customization authority model
6. Locked, controlled, open, proposed, and exception classifications
7. Manual customization workflow
8. Customization request intake
9. Source and lifecycle inspection
10. Impact assessment
11. Customization record
12. Approval and escalation paths
13. Implementation handoff boundary
14. Validation and evidence planning
15. Review, expiry, change, and rollback
16. Foundations customization
17. Theme customization
18. Motion customization
19. Responsive customization
20. Accessibility customization boundary
21. Core-component customization
22. System-component customization
23. Project Profile customization
24. Content and open brand expression
25. Security, privacy, correctness, and data integrity
26. Reusable versus project-local customization
27. Conflict handling and exceptions
28. Conforming examples
29. Non-conforming examples
30. Normative `KBDL-CUS-###` requirements
31. Requirement Coverage Matrix
32. Customization-classification matrix
33. Cross-module customization matrix
34. Customization-record completeness matrix
35. Approval-path matrix
36. Validation and evidence matrix
37. KBDL-010 decision packet
38. Approval-ready versus contingent decisions
39. Earlier-module lifecycle-boundary audits
40. Decision-packet coverage audit
41. Deferred and unresolved items
42. Traceability

Additional sections may be added when necessary.

## 3. Customization terminology

Define at minimum:

* Manual customization
* Customization request
* Customization record
* Customization owner
* Customization reviewer
* Source requirement
* Locked rule
* Controlled variable
* Controlled option
* Open brand expression
* Approved option selection
* Project-local customization
* Reusable customization
* Proposed KBDL extension
* Customization conflict
* Customization exception
* Customization dependency
* Customization evidence
* Customization rollback
* Stale customization
* Superseded customization
* Customization conformance

Do not define a discretionary governance choice as established fact.

Where an exact role, identifier, risk tier, or cadence is not already approved, mark it `Recommended` or `Unresolved`.

## 4. Distinguish customization from adjacent concepts

Explicitly distinguish manual customization from:

* Project Profile selection
* Light or dark mode
* User accessibility preference
* Responsive adaptation
* Component state
* Component variant
* Brand identity
* Open brand expression
* Theme override
* Implementation configuration
* Design-token format
* Feature flag
* Product tier
* User role
* Runtime setting
* Forking KBDL
* Changing a KBDL requirement
* Approving a recommendation
* Granting an exception
* Final validation

A Project Profile defines project-level emphasis.

A customization record documents a project-specific choice within, or a request beyond, the Approved system.

A customization must not silently change the selected Project Profile.

## 5. Customization classification model

Every customization request must be classified as exactly one primary class.

### Class A — Approved option selection

A project selects an option that is already:

* Explicitly permitted
* Inside documented Approved bounds
* Compatible with the project’s Profile
* Independent of any pending recommendation

The selection must still be documented.

It does not change KBDL lifecycle status.

### Class B — Open brand expression

A project selects project-owned expression such as:

* Logo
* Photography
* Illustration
* Campaign graphics
* Content voice
* Brand motifs
* Marketing composition
* Project-specific media

Open expression must remain subordinate to all locked and Approved rules.

### Class C — Proposed controlled customization

The project requests a new choice inside an existing KBDL role or architecture, but the exact option is not yet Approved.

It must be recorded as `Recommended` or `Unresolved`.

It grants no implementation authority until approved through the applicable process.

### Class D — Proposed KBDL extension

The request creates:

* A new reusable role
* A new semantic meaning
* A new component variant intended for reuse
* A new theme, foundation, motion, responsive, or profile option
* A new policy other KBDL projects are expected to share

It is not merely a project customization.

It requires a KBDL change proposal, impact assessment, lifecycle classification, traceability, and project-owner approval.

### Class E — Locked-rule or Approved-requirement exception

The request would modify or bypass a locked rule or an Approved requirement.

It must stop.

It requires an Approved exception decision containing:

* Affected rule
* Reason
* Scope
* Duration
* Approving decision
* Risks
* Mitigations
* Validation requirements
* Rollback plan

### Class F — Prohibited request

The request would:

* Weaken safety
* Weaken accessibility
* Misrepresent system state
* Create unauthorized access
* Hide material errors
* Break semantic meaning
* Create uncontrolled fragmentation
* Depend on unapproved scope without escalation
* Remove required documentation

It must not proceed.

## 6. Manual customization workflow

Define this required workflow:

1. Receive the customization request.
2. Identify the project and declared Project Profile.
3. Identify the requested outcome.
4. Identify affected KBDL modules.
5. Identify affected requirements.
6. Inspect lifecycle, provenance, and validation status.
7. Identify pending dependencies.
8. Classify the request.
9. Apply the design-decision hierarchy.
10. Assess accessibility impact.
11. Assess responsive impact.
12. Assess theme and foundation impact.
13. Assess motion impact.
14. Assess component impact.
15. Assess security, privacy, correctness, and data-integrity impact.
16. Assess performance impact.
17. Determine whether the request is within Approved bounds.
18. Determine the required approval path.
19. Create or update the customization record.
20. Define implementation constraints.
21. Define validation and evidence requirements.
22. Define rollback.
23. Obtain required approval.
24. Implement only after authority is confirmed.
25. Validate implementation separately.
26. Record evidence and remaining limitations.
27. Review or retire the customization when its source changes.

The workflow must not allow an implementation agent to infer approval from:

* A request
* A design mockup
* A validated prototype
* A stakeholder preference
* A Profile choice
* A CUS ID
* A customization record
* Similarity to another project
* A technically successful implementation

## 7. Customization request intake

Define required intake information:

* Project name
* Project Profile declaration
* Request title
* Requested outcome
* Business or user rationale
* Requestor
* Responsible owner
* Affected product areas
* Affected users
* Affected modules
* Known requirement IDs
* Target environments
* Accessibility impact
* Responsive impact
* Theme and foundation impact
* Motion impact
* Component impact
* Security/privacy/correctness impact
* Performance impact
* Dependencies
* Urgency
* Intended duration
* Reuse intention
* Proposed rollback
* Known uncertainty

Do not require information that is genuinely inapplicable.

## 8. Customization record

Define one framework-neutral manual customization record.

Every record must include:

* Record title
* Project
* Profile
* Record identifier or visible placeholder pending identifier-policy approval
* Requestor
* Owner
* Reviewer
* Date proposed
* Current status
* Customization class
* Requested outcome
* Rationale
* Affected modules
* Affected requirements
* Source requirement lifecycle statuses
* Approved authority
* Pending dependencies
* Exact permitted scope
* Explicit exclusions
* Values or choices selected
* Accessibility impact
* Responsive impact
* Theme impact
* Foundation impact
* Motion impact
* Component impact
* Profile impact
* Content impact
* Security impact
* Privacy impact
* Correctness and data-integrity impact
* Performance impact
* Implementation constraints
* Validation method
* Required evidence
* Validation status
* Known limitations
* Rollback plan
* Effective scope
* Duration
* Review or expiration date
* Superseded record
* Related KBDL decision
* Change history
* Final disposition

Do not mandate a machine-readable format.

Do not define a JSON schema, database table, or framework API.

## 9. Status and authority in customization records

A customization record must separately state:

### Source lifecycle status

The lifecycle status of every requirement or option being used.

### Record workflow status

Examples may include:

* Draft
* Awaiting information
* Awaiting approval
* Approved for project implementation
* Rejected
* Implemented
* Under validation
* Validated
* Expired
* Superseded
* Rolled back

These are project-record workflow states, not KBDL lifecycle labels.

Do not reuse `Approved` ambiguously.

Where the word “Approved” is used in a project workflow status, the record must identify:

* Who approved it
* What authority they exercised
* Whether this was a local project selection or a KBDL lifecycle decision
* Exact scope
* Explicit exclusions

### Validation status

Use KBDL’s `Verified` / `Not verified` validation dimension for the defined validation method.

A record may be:

* Authorized but not validated
* Validated technically but not authorized
* Both authorized and validated
* Neither

Only authorized and validated implementation should be represented as conforming.

## 10. Approval-path architecture

Define distinct paths for:

### Existing Approved option selection

Document the selection and local responsible approval.

Do not change any KBDL lifecycle status.

### Open brand expression

Document material or reusable choices.

Confirm locked-rule compliance.

### New project-local controlled option

Record it as non-Approved until the applicable authority reviews it.

Do not imply that local approval changes KBDL lifecycle status.

### Reusable KBDL extension

Use KBDL governance:

* Proposal
* Requirement ID where appropriate
* `Recommended` or `Unresolved` lifecycle
* Impact assessment
* Traceability
* Decision packet
* Project-owner approval

### Locked-rule exception

Use the governance exception process and decision register.

No exception is created by KBDL-010 itself.

### Pending dependency

Keep the request contingent.

State the blocker and what approval is required.

Do not approve the dependent customization independently.

The exact project-level approval-role model is a new KBDL-010 policy and must be represented accurately in the decision packet unless directly mandated by this prompt.

## 11. Foundations customization

Define customization boundaries for:

* Color
* Typography
* Spacing and layout
* Shape and corners
* Borders and dividers
* Elevation and depth
* Iconography
* Imagery and media

Require that projects:

* Preserve semantic roles
* Preserve shared scales and architecture
* Use only Approved values or Approved controlled alternatives
* Document selected controlled options
* Preserve accessible contrast
* Preserve hierarchy
* Preserve responsive content priority
* Preserve component-state clarity
* Preserve Profile invariants

Potentially permitted customization may include:

* Approved project accent selection
* Approved neutral-temperature choice
* Approved typeface selection inside the typeface model
* Approved imagery treatment
* Approved depth-intensity choice
* Open project imagery and media

The specification must inspect actual owning-module rules before describing any item as permitted.

Do not invent:

* New color values
* New type scales
* New spacing values
* New radii
* New elevation values
* New icon sizes
* New layout values

## 12. Theme customization

Use the Approved project-override list and documentation requirement already defined by the theme module.

Require that theme customization:

* Uses the shared semantic-role inventory
* Preserves light/dark parity
* Preserves user preference precedence
* Preserves focus and contrast
* Preserves status meaning
* Preserves local contrast-context rules
* Documents every project-controlled override
* Remains compatible with all three Profiles

Do not authorize:

* Pending opacity values
* Translucent variants
* Forced-colors policy
* Data-visualization palettes
* Account-level synchronization
* New semantic theme roles
* Framework token formats
* A project-specific theme architecture

A project-specific brand color must be mapped through an Approved role and validated; it must not replace the role architecture.

## 13. Motion customization

Define allowed and prohibited motion customization.

Require that projects preserve:

* Motion purpose
* Approved motion hierarchy
* Approved timing classes
* Approved easing architecture
* Approved safety rules
* Reduced-motion substitutions
* No-motion parity
* Interaction availability
* Performance constraints
* Profile-level shared architecture

A project may vary only what the motion module explicitly allows.

Do not authorize:

* New timing scales
* New easing curves
* Unapproved exact component durations
* Unapproved exact distances
* Unapproved exact scale values
* Unapproved stagger values
* Device-performance detection
* Animation-library choice as KBDL policy
* Rendering-technology choice
* Quantitative hazard thresholds not already Approved

Open brand animation remains subordinate to motion purpose and safety.

## 14. Responsive customization

Require that all customization preserve:

* Content priority
* Source order
* Focus order
* Reflow
* Text resizing
* Orientation flexibility
* Safe-area handling
* Virtual-keyboard visibility
* Input parity
* Semantic continuity
* Error and recovery access

Do not use customization to approve exact:

* Breakpoints
* Grid counts
* Gutters
* Container widths
* Navigation-collapse thresholds
* Table/grid transformations
* Overlay transformations

A project may document implementation choices, but a local implementation choice does not promote a pending KBDL recommendation.

## 15. Accessibility boundary

Accessibility is locked.

Customization must not:

* Lower WCAG 2.2 Level AA requirements
* Remove keyboard behavior
* Obscure focus
* Reduce target-size compliance
* Remove pointer alternatives
* Depend on color alone
* Depend on motion alone
* Remove text alternatives
* Remove status communication
* Weaken error identification or prevention
* Weaken accessible authentication
* Disable user preference support
* Create inaccessible local contrast
* Hide content from assistive technology incorrectly

Any requested exception must stop and use governance.

KBDL-010 must not create an “accessibility exception by customization” shortcut.

## 16. Core-component customization

Require that customization preserve:

* Semantic role
* Accessible name
* Accessible description
* Component anatomy
* State model
* Keyboard behavior
* Pointer behavior
* Focus behavior
* Error behavior
* Trigger/surface relationships
* Profile compatibility

A project may customize presentation only inside Approved foundation, theme, motion, responsive, and component boundaries.

Do not authorize profile-specific or project-specific semantic variants.

Do not silently adopt any pending KBDL-007 recommendation.

## 17. System-component customization

Require that customization preserve:

* Surface meaning
* Modality
* Focus containment
* Focus restoration
* Dismissal behavior
* Status urgency
* Live-region meaning
* Progress and meter semantics
* System-state correctness
* Offline and recovery honesty
* Data-presentation semantics
* Security and sensitive-data boundaries

Do not silently adopt any pending KBDL-008 taxonomy, timing, placement, sizing, queueing, transformation, or interaction recommendation.

## 18. Project Profile customization

A customization must begin from the project’s documented Profile declaration.

It must preserve:

* Shared architecture
* Profile invariants
* Locked decisions
* Approved profile emphasis
* Profile-independent accessibility and semantics
* Profile-independent security and correctness

Customization must not:

* Create a fourth Profile
* Create a hidden hybrid Profile
* Switch Profile by viewport
* Treat theme mode as Profile
* Apply pending profile defaults as Approved
* Change Profile migration policy
* Create profile-specific component semantics

Where a project request conflicts with its declared Profile:

1. Determine whether the request is permitted controlled customization.
2. Determine whether the Profile declaration should change.
3. Determine whether a pending KBDL-009 policy is involved.
4. Record the conflict.
5. Do not resolve it by silently overriding the Profile.

## 19. Content and open brand expression

Define open project-owned areas:

* Logo
* Photography
* Illustration
* Campaign graphics
* Content voice
* Brand motifs
* Marketing composition
* Domain-specific content
* Project-specific media

Require that open expression preserve:

* Accessible alternatives
* Reading order
* Comprehension
* Contrast
* Focus visibility
* Motion safety
* Responsive behavior
* Performance
* Privacy
* Intellectual-property and licensing review
* Security-safe content
* Honest system-state communication

Open expression is not permission to replace KBDL foundations or components.

## 20. Security, privacy, correctness, and data integrity

Every customization must preserve:

* Authentication boundaries
* Authorization
* Data ownership
* Input validation
* Sensitive-data protection
* Safe error disclosure
* Correct saved/synchronized/queued/completed states
* Consequential-action safeguards
* Permission and not-found privacy
* Auditability
* Recovery
* Rollback

Customization must not:

* Use visibility as authorization
* Hide restricted actions as the only control
* Expose credentials or personal data
* Expose stack traces
* Claim completion before confirmation
* Suppress security errors for aesthetic reasons
* Change destructive-action safeguards without approval
* Use branding to imitate trusted security indicators
* Hide stale or offline state
* Remove required audit information

Do not define backend security architecture.

## 21. Reusable versus project-local customization

Distinguish:

### Project-local

A choice intended for one project only.

It must be recorded and bounded.

### Reusable

A choice intended for use by more than one project.

A reusable choice may be evidence that KBDL needs a new Approved controlled option or extension.

It must not be copied across projects silently.

Define a promotion workflow:

1. Identify repeated use.
2. Confirm it is not already covered.
3. Assess cross-profile impact.
4. Assess accessibility, responsive, theme, motion, component, and security impact.
5. Create a KBDL proposal.
6. Assign an ID when stable.
7. Keep lifecycle non-Approved until reviewed.
8. Add traceability.
9. Obtain project-owner approval.
10. Update source modules rather than relying permanently on project-local records.

The exact reuse threshold is a decision-packet topic.

## 22. Conflict and exception handling

Apply the KBDL design-decision hierarchy.

When customization conflicts with:

1. Safety or data integrity
2. Accessibility
3. User task or comprehension
4. Approved KBDL requirements
5. Content hierarchy
6. Responsive constraints
7. Performance
8. Project Profile

the customization yields.

An exception record must state:

* Affected locked rule or Approved requirement
* Reason
* Alternatives considered
* Scope
* Duration
* Owner
* Approving decision
* Accessibility impact
* Security impact
* Responsive impact
* Theme/foundation impact
* Motion impact
* Component impact
* Validation
* Evidence
* Rollback
* Expiration and review

Do not create any actual project exception in this step.

## 23. Change, review, expiry, and rollback

Define requirements for:

* Updating a customization when source requirements change
* Reviewing records after Profile change
* Reviewing records after a KBDL lifecycle promotion
* Reviewing records after deprecation or supersession
* Expiring temporary customization
* Superseding a customization record
* Rolling back implementation
* Preserving change history
* Preventing orphaned records
* Preventing implementation from surviving after authority expires
* Recording failed rollback or incomplete migration

Exact review cadence and default expiry are new policy and belong in the decision packet.

## 24. Conforming examples

Include examples across:

* Approved accent selection
* Typeface selection within an Approved model
* Project photography and illustration
* Theme override inside Approved boundaries
* Motion emphasis inside Approved architecture
* Precision density request that avoids pending exact values
* Flow content-tone customization
* Component styling without semantic changes
* Project-local customization record
* Reusable customization escalated as a KBDL proposal
* Temporary exception with explicit scope and rollback
* Customization invalidated by a later source change

Each example must state:

* Project and Profile
* Request
* Classification
* Source requirements
* Lifecycle authority
* Documentation required
* Approval path
* Validation method
* Rollback
* Why it conforms

Do not claim implementation testing.

## 25. Non-conforming examples

Include examples such as:

* Treating a pending breakpoint as a local Approved value
* Defining a project-only semantic color role
* Removing focus styling for branding
* Creating a new Button meaning
* Using a tooltip as an accessible name
* Creating a hidden hybrid Profile
* Treating dark mode as customization of Profile
* Reducing target size
* Using a pending Card variant
* Creating a custom toast queue policy
* Hiding an error to reduce visual noise
* Copying a project-local pattern into multiple projects without governance
* Recording a customization after implementation to retroactively justify it
* Marking a technically validated choice as Approved
* Omitting rollback
* Allowing an expired exception to remain active
* Using automation that silently mutates KBDL values

Each example must identify:

* Violated requirement
* Risk
* Correct classification
* Required correction or escalation

## 26. Requirement architecture

Create requirements using:

```text
KBDL-CUS-###
```

Before assigning IDs:

1. Search the complete repository for existing CUS IDs.
2. Begin at the next unused sequential number.
3. Use three-digit zero padding.
4. Never reuse an ID.
5. Never renumber another module.
6. Assign one primary ID to every independently testable rule.
7. Preserve one authoritative normative location per requirement.
8. Cross-reference related prior requirements.
9. State applicable Profiles.
10. State lifecycle status.
11. State provenance.
12. State validation status.
13. State authority.
14. State classification.
15. State validation method.
16. State known limitations.
17. State specification location.
18. State packet destination.
19. State pending dependencies.
20. State affected customization classes.

Do not target an arbitrary requirement count.

## 27. Required metadata for every CUS requirement

Every CUS record must explicitly contain:

* Requirement ID and normative rule
* Lifecycle status
* Provenance
* Validation status
* Authority
* Related requirements
* Applicable Profiles
* Customization class
* Specification location
* Decision-packet destination
* Pending dependencies
* Validation method
* Known limitation

For Approved requirements, authority must support the complete rule.

For Recommended requirements, state:

```text
Authority: Not applicable — pending explicit project-owner approval; assignment of a CUS ID does not grant implementation authority.
```

## 28. Requirement Coverage Matrix

Create a matrix covering every CUS requirement.

Include:

* ID
* Title
* Category
* Customization class
* Lifecycle
* Provenance
* Validation status
* Authority
* Applicable Profiles
* Related modules
* Related requirements
* Specification location
* Packet destination
* Pending dependency
* Validation method
* Known limitation

Every CUS ID must appear exactly once.

## 29. Customization-classification matrix

For each class record:

* Definition
* Typical request
* Allowed authority
* Required documentation
* Required approval
* Implementation permission
* Validation
* Traceability
* Decision-register impact
* Rollback
* Prohibited misuse

## 30. Cross-module customization matrix

Map customization across:

* Governance
* Principles
* Foundations
* Themes
* Motion
* Responsive behavior
* Accessibility
* Core components
* System components
* Project Profiles
* Content and open expression
* Security/privacy/correctness
* Future validation

For each module state:

* Locked rules
* Approved controlled areas
* Open areas
* Pending items
* Prohibited changes
* Approval path
* Validation method
* Known limitation

## 31. Customization-record completeness matrix

Make the record template programmatically auditable.

Map every required record field to:

* Purpose
* Required or conditional
* Responsible source
* Validation method
* Example
* Common failure

## 32. Approval-path matrix

Map each customization class to:

* Local documentation
* Local review
* KBDL project-owner approval
* Decision-register entry
* Requirement lifecycle change
* Contingent blocker
* Implementation eligibility
* Validation eligibility

Do not invent authority where current governance is silent.

Mark discretionary role and approval details accurately.

## 33. Validation and evidence matrix

Define evidence expectations for:

* Documentation-only selection
* Theme or foundation implementation
* Motion implementation
* Responsive implementation
* Component implementation
* Accessibility-impacting implementation
* Security-impacting implementation
* Temporary exception
* Reusable customization
* Rollback

Do not perform final KBDL validation in this module.

## 34. KBDL-010 decision packet

Create an approval-ready decision packet for genuinely new customization policy.

Potential categories include:

* Project customization-record identifier format
* Which customizations require a record
* Local approval-role model
* Required independent reviewer
* Minor/material customization threshold
* Customization risk tiers
* Evidence required by risk tier
* Review cadence
* Default expiry
* Exception-renewal rules
* Multiple-record inheritance
* Override precedence between project records
* Reusable-customization threshold
* Promotion-to-KBDL workflow details
* Stale-record handling
* Default rollback-evidence requirement
* Customization archive policy
* Project Profile re-review triggers
* Required licensing review for project assets
* Whether a machine-readable format may be introduced later

For every packet item include:

* Packet number
* Decision
* Recommendation
* Lifecycle status
* Provenance
* Validation status
* Rationale
* Alternatives
* Trade-offs
* Accessibility impact
* Responsive impact
* Theme/foundation impact
* Motion impact
* Component impact
* Profile impact
* Security/privacy/correctness impact
* Performance impact
* Dependencies
* Exact affected CUS requirements
* Approval scope
* Explicit exclusions

Do not predetermine the number of packet items.

Do not create a decision-register entry because no KBDL-010 recommendation has been approved.

## 35. Approval-ready versus contingent separation

Create separate subsections.

### Independently approval-ready

An item belongs here only if it does not require approval of:

* A pending foundation item
* A pending theme item
* A pending motion item
* A pending KBDL-006 requirement
* A pending KBDL-007 requirement
* A pending KBDL-008 requirement
* A pending KBDL-009 requirement
* A later validation policy
* An implementation-specific assumption

### Contingent or not approval-ready

A contingent item must state:

* Blocker
* Affected CUS requirement
* Earlier pending requirement
* Why KBDL-010 cannot approve it independently
* What approval would be needed
* That it grants no implementation authority

Do not place contingent items in the approval-ready table.

## 36. Earlier-module lifecycle-boundary audits

Create separate audits for:

### Foundations and themes

Inventory every non-Approved value or policy.

State whether each is:

* Not referenced
* Context only
* Contingent dependency
* Explicitly excluded

### Motion

Inventory every non-Approved or Deferred implementation-level item.

### KBDL-006

List all nine pending requirements.

### KBDL-007

List all ten pending requirements.

### KBDL-008

List all seventeen pending requirements.

### KBDL-009

List all seven pending requirements and preserve their exact approval-ready/contingent status.

For each item record:

* Reference status
* Customization impact
* Normative use: yes or no
* Lifecycle status
* Packet destination where applicable
* Exact exclusion

## 37. Decision-packet coverage audit

Create an auditable coverage section showing:

* Total CUS requirements
* Approved count
* Recommended count
* Unresolved count
* Deferred count
* Blocked count
* Independently approval-ready count
* Contingent count
* Unresolved tracking count

Map every non-Approved CUS requirement exactly once to:

* One approval-ready packet item
* One contingent packet item
* One unresolved item
* One deferred item
* One blocked item

Prove:

* No non-Approved CUS requirement is orphaned.
* No packet item is orphaned.
* No Approved requirement awaits approval.
* No earlier-module dependency is hidden.
* No project record itself grants KBDL approval.
* No contingent item is included implicitly in approval scope.
* Exact future approval scope is explicit.
* No pending earlier recommendation is promoted.

## 38. Deferred and unresolved items

Explicitly record:

* Automated customization tooling
* Machine-readable customization schema
* JSON, YAML, or database format
* Token-generation tools
* Framework APIs
* Design-tool plugins
* Figma libraries
* Storybook integration
* CI enforcement
* Customization dashboards
* Automated lifecycle checking
* Automated dependency resolution
* Automatic Profile recommendation
* Automatic contrast or motion remediation
* Exact project-level approval roles
* Exact risk thresholds
* Exact review cadence
* Exact expiry period
* Exact reuse threshold
* Exact inheritance depth
* Exact implementation token format
* Browser-support policy
* Final validation policy
* Production conformance
* Implementation packages

Do not lose deferred work through omission.

## 39. Cross-module updates

Update only where necessary:

* `docs/kbdl/README.md`
* `docs/kbdl/traceability-matrix.md`
* `docs/kbdl/glossary.md`
* `docs/kbdl/conformance-checklist.md`
* `docs/kbdl/principles.md`
* `docs/kbdl/profiles.md`
* Theme or foundation files containing stale customization deferrals
* Other files containing explicit KBDL-010 lock wording

### Main index

Update the index to state:

* KBDL-009 passed planning-agent validation.
* KBDL-010 deliverables are present.
* `customization.md` resolves.
* Manual customization is documented and auditable.
* Locked rules remain protected.
* Shared architecture and Profile invariants remain intact.
* Pending earlier-module recommendations remain unapproved.
* KBDL-010 recommendations remain distinct from mandatory inherited rules.
* No implementation-level customization validation exists.
* Final validation and later work remain locked pending KBDL-010 validation.
* The overall project is not complete.

### Earlier-module reconciliation

Update prior modules only where necessary to:

* Link deferred customization references to `customization.md`.
* State that KBDL-010 owns detailed manual-customization governance.
* Preserve all prior lifecycle, provenance, and validation statuses.
* Preserve every prior packet mapping.
* Preserve every Approved value.
* Preserve every Profile invariant.

Do not broadly rewrite prior modules.

## 40. Traceability

Add complete traceability for every CUS requirement.

Each entry must include:

* Blueprint section
* Roadmap prompt
* Requirement ID
* Per-ID specification location
* Lifecycle status
* Provenance
* Validation status
* Authority
* Customization class
* Validation method
* Validation evidence
* Known limitation
* Related decision
* Related prior requirements
* Packet destination
* Pending dependencies
* Profile impact
* Future validation dependency
* Notes

Requirements may be grouped only when:

* Every ID is listed explicitly.
* Per-ID locations are explicit.
* Mixed lifecycle and authority are separated.
* Packet destinations are individually auditable.
* Dependencies are individually auditable.
* Every ID appears exactly once.

Do not use the traceability matrix as its own validation evidence.

## 41. Glossary

Audit existing terms and add only genuinely new terms.

Potential additions:

* Manual customization
* Customization request
* Customization record
* Approved option selection
* Project-local customization
* Reusable customization
* Proposed KBDL extension
* Customization exception
* Stale customization
* Customization conformance

Do not redefine existing:

* Locked rule
* Controlled variable
* Open brand expression
* Project Profile
* Lifecycle status
* Validation status

## 42. Conformance checklist

Preserve every existing checklist item.

Add a clearly labeled KBDL-010 Manual Customization section covering at least:

1. Customization is manual and documented.
2. The project and Profile are identified.
3. Every affected module and requirement is identified.
4. Source lifecycle statuses are recorded accurately.
5. The request is classified correctly.
6. Locked rules remain unchanged.
7. Approved requirements remain unchanged unless an approved exception exists.
8. Controlled options stay inside Approved bounds.
9. Open expression remains subordinate to locked rules.
10. Pending recommendations are not promoted.
11. Accessibility impact is reviewed.
12. Responsive impact is reviewed.
13. Theme and foundation impact is reviewed.
14. Motion impact is reviewed.
15. Component semantics and anatomy are preserved.
16. Profile invariants are preserved.
17. Security, privacy, correctness, and data integrity are preserved.
18. Required approval is recorded.
19. Decision-register impact is handled correctly.
20. Validation method and required evidence are defined.
21. Implementation-level validation is not claimed prematurely.
22. Rollback is documented.
23. Duration and review conditions are documented.
24. Reusable customization is escalated appropriately.
25. Every non-Approved CUS requirement has a packet or tracking destination.
26. Final validation and later-roadmap content remain unstarted.

Do not mark checklist rows Passed in the repository.

## Out of Scope

Do not:

* Create application code
* Create production HTML
* Create CSS, Sass, JavaScript, TypeScript, JSON, YAML, JSX, TSX, Vue, Svelte, or Angular files
* Create design-token files
* Create a customization manifest
* Create a JSON schema
* Create database tables
* Create APIs
* Add dependencies
* Select a frontend framework
* Build a customization UI
* Build a theme editor
* Build automated tooling
* Create Figma assets
* Create Storybook stories
* Create a demo application
* Customize a real project
* Create an actual exception
* Approve a project customization
* Approve any KBDL-010 packet item
* Approve any KBDL-009 recommendation
* Approve any KBDL-008 recommendation
* Approve any KBDL-007 recommendation
* Approve any KBDL-006 recommendation
* Approve pending theme or motion items
* Change prior lifecycle statuses
* Change prior validation statuses
* Change Approved values
* Change Profile architecture
* Change component semantics
* Define final implementation formats
* Create `docs/kbdl/validation.md`
* Begin final validation
* Begin any later roadmap item
* Modify unrelated documentation
* Amend or rewrite `907708c`
* Reset or rebase validated history
* Force-push

## Security Requirements

The specification must require future customization implementations to:

* Preserve authentication and authorization.
* Preserve data ownership.
* Preserve server-side access controls.
* Avoid exposing credentials, tokens, personal data, or private media.
* Avoid exposing stack traces or sensitive diagnostic information.
* Avoid false saved, synchronized, queued, or completed claims.
* Preserve consequential-action safeguards.
* Preserve permission-denied and not-found privacy.
* Preserve error and recovery behavior.
* Preserve auditability.
* Document security impact.
* Define rollback.
* Stop when authority is unclear.

This documentation step must not define backend security architecture.

## UI and UX Requirements

The specification must ensure that customization preserves:

* KBDL identity
* Shared semantics
* Shared accessibility
* Shared component anatomy
* Light and dark parity
* Responsive reflow
* Keyboard support
* Pointer and touch parity
* Focus visibility
* Focus not obscured
* Reduced-motion parity
* No-motion parity
* Loading, empty, error, offline, and success meaning
* Honest system-state communication
* Clear content hierarchy
* Plain-language guidance
* Recoverable workflows
* Profile invariants
* Existing design-system consistency

Customization differences must remain expression or controlled variation, not semantic fragmentation.

## Implementation Requirements

Perform the work in this order:

1. Inspect repository and remote state.
2. Inspect recent commits.
3. Confirm KBDL-010 has not started.
4. Confirm no existing CUS IDs.
5. Read all required KBDL documents.
6. Inventory every customization reference.
7. Inventory every locked rule.
8. Inventory every Approved controlled option.
9. Inventory every open-expression category.
10. Inventory every pending earlier-module item.
11. Define terminology.
12. Define the authority and classification model.
13. Define the manual workflow.
14. Define request intake.
15. Define the customization record.
16. Define statuses and approval paths.
17. Define foundation customization.
18. Define theme customization.
19. Define motion customization.
20. Define responsive customization.
21. Define the accessibility boundary.
22. Define component customization.
23. Define Profile customization.
24. Define open brand expression.
25. Define security, privacy, correctness, and performance requirements.
26. Define reuse, promotion, conflict, exception, review, and rollback processes.
27. Add conforming and non-conforming examples.
28. Assign CUS requirement IDs.
29. Apply lifecycle, provenance, validation, and authority metadata.
30. Create all coverage and validation matrices.
31. Create the decision packet.
32. Separate approval-ready and contingent decisions.
33. Create every earlier-module boundary audit.
34. Create the decision-packet coverage audit.
35. Record deferred and unresolved items.
36. Add traceability.
37. Update the index, glossary, checklist, and stale deferrals.
38. Run complete documentation validation.
39. Run complete lifecycle and dependency audits.
40. Inspect the full diff.
41. Confirm no prior status changed.
42. Confirm no pending recommendation was promoted.
43. Confirm no implementation artifact was created.
44. Confirm final validation has not started.
45. Commit KBDL-010 separately.
46. Push only by normal fast-forward.
47. Return the complete implementation report.
48. Do not begin any later roadmap item.

## Acceptance Criteria

### KBDL-010-AC-001 — Repository safety

Work begins from a clean, synchronized repository and preserves collaborator work.

### KBDL-010-AC-002 — Baseline preservation

Commit `907708c` remains unchanged.

### KBDL-010-AC-003 — Customization document

`docs/kbdl/customization.md` exists with substantive KBDL-010 content.

### KBDL-010-AC-004 — Module continuity

The planned path and `CUS` requirement code are used.

### KBDL-010-AC-005 — Manual and documented

Customization is explicitly manual, documented, attributable, reviewable, and reversible.

### KBDL-010-AC-006 — No silent customization

No customization may be implemented silently or used to infer authority.

### KBDL-010-AC-007 — Concept distinction

Customization is distinguished from Profile, theme mode, preference, runtime state, implementation configuration, and KBDL lifecycle approval.

### KBDL-010-AC-008 — Classification completeness

Every customization request can be classified through the defined model.

### KBDL-010-AC-009 — Approved-selection integrity

Selection of an existing Approved option does not change KBDL lifecycle status.

### KBDL-010-AC-010 — Open-expression integrity

Open brand expression remains subordinate to every locked and Approved rule.

### KBDL-010-AC-011 — Controlled-variable integrity

Controlled customization remains inside the owning module’s Approved bounds.

### KBDL-010-AC-012 — Proposal integrity

A new project-local or reusable option remains non-Approved until reviewed.

### KBDL-010-AC-013 — Extension integrity

A reusable new pattern is escalated as a KBDL proposal rather than copied silently.

### KBDL-010-AC-014 — Exception integrity

A locked-rule or Approved-requirement exception cannot proceed without an Approved decision record.

### KBDL-010-AC-015 — Prohibited-request handling

Safety-, accessibility-, security-, correctness-, or integrity-weakening requests are stopped.

### KBDL-010-AC-016 — Workflow completeness

The manual customization workflow covers request through review or retirement.

### KBDL-010-AC-017 — Intake completeness

Customization intake captures the information needed for classification and impact review.

### KBDL-010-AC-018 — Record completeness

The customization record includes every required field.

### KBDL-010-AC-019 — Status separation

KBDL lifecycle, project-record workflow, approval authority, and validation status are not conflated.

### KBDL-010-AC-020 — Approval-path clarity

Every customization class has a defined approval and implementation path.

### KBDL-010-AC-021 — Foundation preservation

Customization does not fragment or replace foundation architecture or Approved values.

### KBDL-010-AC-022 — Theme preservation

Customization preserves semantic roles, parity, precedence, focus, contrast, and Approved override boundaries.

### KBDL-010-AC-023 — Motion preservation

Customization preserves motion purpose, hierarchy, safety, reduced motion, and Approved timing/easing architecture.

### KBDL-010-AC-024 — Responsive preservation

Customization preserves content priority, reflow, source order, focus order, and input parity.

### KBDL-010-AC-025 — Accessibility protection

Customization cannot weaken KBDL’s accessibility baseline.

### KBDL-010-AC-026 — Core-component preservation

Core-component semantics, anatomy, states, keyboard, pointer, and focus behavior remain intact.

### KBDL-010-AC-027 — System-component preservation

Surface, overlay, feedback, system-state, modality, and recovery semantics remain intact.

### KBDL-010-AC-028 — Profile invariants

Customization preserves one shared semantic and accessibility architecture across Profiles.

### KBDL-010-AC-029 — No hidden Profile policy

Customization does not silently create a Profile, hybrid Profile, or Profile migration rule.

### KBDL-010-AC-030 — Content integrity

Open content and branding preserve accessibility, comprehension, privacy, and performance.

### KBDL-010-AC-031 — Security and correctness

Customization cannot weaken authentication, authorization, privacy, data ownership, state accuracy, or recovery.

### KBDL-010-AC-032 — Reuse governance

Reusable customization is escalated for KBDL review.

### KBDL-010-AC-033 — Change management

Customization records address source changes, expiry, supersession, review, and rollback.

### KBDL-010-AC-034 — CUS IDs

All CUS IDs are unique, sequential, stable, and correctly referenced.

### KBDL-010-AC-035 — Requirement metadata

Every CUS record contains complete lifecycle, authority, location, dependency, packet, validation, and limitation metadata.

### KBDL-010-AC-036 — Lifecycle integrity

Only inherited or prompt-mandated rules whose complete authority is supported are Approved.

### KBDL-010-AC-037 — Discretionary-policy integrity

New discretionary customization policies remain non-Approved.

### KBDL-010-AC-038 — Foundation/theme boundary audit

No pending foundation or theme value is promoted.

### KBDL-010-AC-039 — Motion boundary audit

No pending or Deferred motion item is promoted.

### KBDL-010-AC-040 — KBDL-006 boundary

None of the nine pending KBDL-006 requirements is treated as implementation authority.

### KBDL-010-AC-041 — KBDL-007 boundary

None of the ten pending KBDL-007 requirements is treated as implementation authority.

### KBDL-010-AC-042 — KBDL-008 boundary

None of the seventeen pending KBDL-008 requirements is treated as implementation authority.

### KBDL-010-AC-043 — KBDL-009 boundary

None of the seven pending KBDL-009 requirements is treated as implementation authority.

### KBDL-010-AC-044 — Decision packet

Every new customization policy requiring approval appears in the KBDL-010 decision packet.

### KBDL-010-AC-045 — Contingent separation

Every item dependent on an earlier pending requirement is outside the independently approval-ready packet.

### KBDL-010-AC-046 — Packet coverage

Every non-Approved CUS requirement maps exactly once to a packet or tracking destination.

### KBDL-010-AC-047 — No fabricated approval

No KBDL-010 packet item or project customization is represented as approved.

### KBDL-010-AC-048 — Requirement Coverage Matrix

Every CUS requirement appears exactly once with complete fields.

### KBDL-010-AC-049 — Cross-module matrix

Every relevant KBDL module has explicit customization boundaries.

### KBDL-010-AC-050 — Record matrix

Every required customization-record field is auditable.

### KBDL-010-AC-051 — Traceability

Every CUS requirement has complete, individually auditable traceability.

### KBDL-010-AC-052 — Cross-reference integrity

Every link, anchor, visible section label, ID, location, packet reference, and dependency resolves.

### KBDL-010-AC-053 — Documentation integrity

Counts, headings, matrices, classifications, lifecycle summaries, packet mappings, and audits are internally consistent.

### KBDL-010-AC-054 — Existing-work protection

No Approved KBDL-001 through KBDL-009 value, rule, decision, status, or packet mapping is unintentionally changed.

### KBDL-010-AC-055 — Scope control

No code, implementation schema, customization tool, final-validation module, or later-roadmap work is introduced.

### KBDL-010-AC-056 — Validation honesty

Implementation-level customization conformance remains `Not verified`.

### KBDL-010-AC-057 — Index accuracy

The index records KBDL-009 as passed, KBDL-010 as present and under validation, and final validation as locked.

### KBDL-010-AC-058 — Safe commit

KBDL-010 is committed separately without rewriting validated history.

### KBDL-010-AC-059 — Safe push

The KBDL-010 commit is pushed by normal fast-forward.

### KBDL-010-AC-060 — Progression gate

Final validation and every later roadmap item remain unstarted.

## Required Validation

Run every existing applicable repository validator.

Record exact command, complete stdout, complete stderr, exit code, and result for:

```bash
git fetch origin
git remote -v
git branch --show-current
git status --short
git rev-parse HEAD
git rev-parse origin/main
git log --oneline --decorate -10
git show --no-patch --format=fuller 907708c
git diff --check
```

Run dependency-free validation for:

1. Relative links
2. Heading anchors
3. Visible section-number labels
4. Markdown tables
5. Duplicate headings
6. Empty sections
7. Placeholder text
8. Placeholder requirement references
9. CUS-ID uniqueness
10. CUS-ID sequence continuity
11. Lifecycle totals
12. Provenance totals
13. Validation-status totals
14. Authority completeness
15. Classification completeness
16. Specification-location completeness
17. Packet-destination completeness
18. Dependency completeness
19. Requirement Coverage Matrix coverage
20. Requirement Coverage Matrix duplicates
21. Classification-matrix completeness
22. Cross-module-matrix completeness
23. Customization-record-field coverage
24. Approval-path coverage
25. Decision-packet item uniqueness
26. Packet-to-requirement mapping
27. Approval-ready independence
28. Contingent dependency completeness
29. Orphan non-Approved CUS requirements
30. Orphan packet items
31. Foundation/theme boundary audit
32. Motion boundary audit
33. KBDL-006 boundary audit
34. KBDL-007 boundary audit
35. KBDL-008 boundary audit
36. KBDL-009 boundary audit
37. Traceability coverage
38. Traceability duplicates
39. Traceability field completeness
40. Per-ID traceability locations
41. Existing requirement-status preservation
42. Existing decision-packet preservation
43. Existing Approved-value preservation
44. New exact-value scan
45. New color/opacity scan
46. New motion-value scan
47. New breakpoint/grid/gutter/container scan
48. Code/package/framework exclusion
49. JSON/YAML/schema/token-file exclusion
50. Automation/tooling exclusion
51. Final-validation leakage
52. README hierarchy consistency
53. Conformance-checklist preservation
54. KBDL-010 checklist coverage
55. Working-tree cleanliness
56. Safe-fast-forward eligibility

Required negative output:

```text
Pending foundation/theme promotions: 0
Pending motion promotions: 0
KBDL-006 recommendation promotions: 0
KBDL-007 recommendation promotions: 0
KBDL-008 recommendation promotions: 0
KBDL-009 recommendation promotions: 0
Locked-rule exceptions created: 0
Project-specific semantic architectures: 0
Project-specific accessibility exceptions: 0
Project-specific theme systems: 0
Project-specific motion systems: 0
Project-specific component semantic variants: 0
Implementation schemas or tooling files: 0
Final-validation implementation files: 0
```

Perform manual review for:

* Customization classification
* Approved option versus new proposal
* Open expression versus controlled customization
* Customization versus Profile
* Local versus reusable customization
* Locked-rule exception handling
* Lifecycle and authority separation
* Accessibility protection
* Security and correctness protection
* Foundation and theme boundaries
* Motion boundaries
* Responsive boundaries
* Component semantic preservation
* Approval-ready versus contingent separation
* Record completeness
* Rollback completeness

Do not mark implementation-dependent behavior `Verified` from documentation review alone.

## Required Evidence

Return:

* Initial repository state
* Initial HEAD
* Initial remote-main SHA
* Recent commits inspected
* Files inspected
* Existing customization-reference inventory
* Existing CUS-ID search
* Earlier-module non-Approved inventory
* Files created
* Files changed
* CUS ID range
* Exact CUS requirement count
* Lifecycle breakdown
* Provenance breakdown
* Validation-status breakdown
* Authority breakdown
* Customization-class breakdown
* Exact non-Approved IDs
* Approval-ready packet count
* Contingent packet count
* Unresolved, Deferred, and Blocked counts
* Complete packet mapping
* Complete customization classification audit
* Complete record-field audit
* Complete approval-path audit
* Foundation/theme boundary audit
* Motion boundary audit
* KBDL-006 boundary audit
* KBDL-007 boundary audit
* KBDL-008 boundary audit
* KBDL-009 boundary audit
* Traceability results
* Link and anchor results
* Visible section-label results
* Table results
* ID results
* Exact-value exclusion results
* Scope-control results
* Exact validation commands
* Complete stdout
* Complete stderr
* Exit codes
* Diff statistics
* Commit SHA
* Branch
* Push output
* Final remote-main SHA
* Final working-tree status
* Failed or skipped validation
* Remaining defects
* Remaining risks
* Items not verified
* Rollback command

Do not return only:

* Done
* Working
* Looks good
* All passed
* PASS without evidence

## Evidence Integrity Requirements

1. Use one complete record per command.
2. Include exact command, purpose, exit code, stdout, stderr, and result.
3. Supply complete source for every custom validation script.
4. Supply exact script invocation.
5. Do not truncate acceptance criteria.
6. Do not omit criteria.
7. Do not duplicate report sections.
8. Do not use malformed wide evidence tables.
9. Include complete 64-character SHA-256 checksums.
10. Attach external evidence files where supported.
11. Include critical raw evidence in the report.
12. A local path alone is insufficient.
13. Mark unavailable evidence honestly.

## Rollback Considerations

Keep all KBDL-010 work in one separate commit.

Do not amend `907708c`.

Record the initial SHA before editing.

Expected rollback:

```bash
git revert <KBDL-010-commit-sha>
```

The rollback must remove or reverse:

* `customization.md`
* New CUS requirements
* KBDL-010 traceability
* README updates
* Glossary additions
* Checklist additions
* Reconciled customization deferrals
* KBDL-010 cross-module links

Do not use reset, rebase, amend, or force-push.

## Required Final Report

Return exactly:

# Implementation Result

## Status

Choose exactly one:

* PASS
* PARTIAL PASS
* FAIL
* BLOCKED

## Summary

## Root Cause

Use:

```text
Not applicable — new implementation, not defect remediation.
```

## Repository Inspection

## Commits Inspected

## Files Inspected

## Existing Customization Guidance Inventory

## Changes Made

## Customization Authority Model

## Customization Classification Model

## Manual Customization Workflow

## Customization Request Intake

## Customization Record

## Approval and Escalation Paths

## Foundations Customization

## Theme Customization

## Motion Customization

## Responsive Customization

## Accessibility Boundary

## Core-Component Customization

## System-Component Customization

## Project Profile Customization

## Content and Open Brand Expression

## Security, Privacy, Correctness, and Data Integrity

## Reusable versus Project-Local Customization

## Change, Review, Expiry, and Rollback

## Requirements Added

Include:

* Starting CUS ID
* Ending CUS ID
* Total requirements
* Approved count
* Recommended count
* Unresolved count
* Deferred count
* Blocked count
* Exact non-Approved IDs
* Authority breakdown
* Customization-class breakdown

## Decision Packet

Include:

* Independently approval-ready items
* Contingent items
* Unresolved items
* Deferred items
* Blocked items

## Decision-Packet Coverage Audit

List every non-Approved CUS ID and its single destination.

## Foundation and Theme Approval-Boundary Audit

## Motion Approval-Boundary Audit

## KBDL-006 Approval-Boundary Audit

List all nine requirements.

## KBDL-007 Approval-Boundary Audit

List all ten requirements.

## KBDL-008 Approval-Boundary Audit

List all seventeen requirements.

## KBDL-009 Approval-Boundary Audit

List all seven requirements and preserve the existing five-ready/two-contingent structure.

## Files Changed

## Cross-Module Updates

## Validation Scripts

Provide complete source and exact invocation for every custom script.

## Validation Performed

For every command provide:

### [Command name]

**Command:**

```text
[exact command]
```

**Purpose:**
[Purpose]

**Exit code:**
[Exact exit code]

**Stdout:**

```text
[complete stdout]
```

**Stderr:**

```text
[complete stderr or "(empty)"]
```

**Result:**
Pass or Fail

## Acceptance Criteria Results

List `KBDL-010-AC-001` through `KBDL-010-AC-060` individually.

For each provide:

* Exact criterion
* Result: Passed, Failed, Not verified, or Not applicable
* Evidence
* Remaining uncertainty

## Evidence Files

For every evidence file provide:

* Path
* Purpose
* Size
* Full SHA-256
* Availability

## Evidence

## Failed or Skipped Validation

## Remaining Defects

Classify every defect:

* P0 Critical
* P1 High
* P2 Medium
* P3 Low

## Remaining Risks

## Items Not Verified

## Scope Compliance

## Repository Changes Outside Scope

## Rollback Plan

## Commit and Branch

## Push Status

## Deployment Status

Use:

```text
Not applicable
```

## Recommended Next Action

## Progression Gate

> Do not begin final validation or any later roadmap item. Complete only KBDL-010 and return the complete implementation evidence so the planning agent can determine whether progression is allowed.

## Progression Gate

Do not begin:

* Final KBDL validation
* Production-readiness audit
* Implementation packages
* Automated customization tooling
* Any later roadmap work

Do not approve:

* Any KBDL-010 decision-packet item
* Any KBDL-009 recommendation
* Any KBDL-008 recommendation
* Any KBDL-007 recommendation
* Any KBDL-006 recommendation
* Any pending foundation, theme, motion, or accessibility item
* Any project-specific exception

Complete only KBDL-010.
