# KBDL Design Language

**Version 1.0** — a framework-independent design language for building
consistent, accessible, responsive web products.

KBDL gives you principles, foundations, tokens, themes, motion and responsive
guidance, accessibility requirements, component specifications, and patterns.
It does not ship runtime code, so you can implement it in any stack.

See [STATUS](STATUS.md) for scope and version state.

## Goals

* **Consistent** — one visual and interaction language across products
* **Accessible by design** — accessibility is a requirement of the
  specification, not a later audit
* **Adaptive** — light and dark, compact to wide, comfortable to dense
* **Framework-independent** — tokens and specifications, not a component library
* **Expressive within limits** — three profiles that flex character without
  fragmenting into separate systems

## Who it is for

Product designers, front-end engineers, and accessibility specialists building
or maintaining a product that should look and behave like the others in its
family.

## Core principles

1. **Clarity before decoration** — if an effect competes with comprehension, it
   goes.
2. **Accessibility is structural** — contrast, focus, keyboard operation, and
   target size are design inputs, not remediation.
3. **Consistency over novelty** — reuse an existing component before inventing
   one.
4. **Motion with purpose** — motion explains change; it never performs.
5. **Content sets the breakpoints** — layout adapts where content stops working,
   not at rumoured device widths.
6. **Honest states** — loading, empty, and error are designed, not afterthoughts.

Full detail: [principles](principles.md).

## Documentation map

| Area | Document |
| --- | --- |
| Scope and version | [STATUS](STATUS.md) |
| Principles | [principles](principles.md) |
| Foundations | [foundations](foundations/README.md) — [color](foundations/color.md), [typography](foundations/typography.md), [spacing & layout](foundations/spacing-layout.md), [shape & depth](foundations/shape-depth.md), [iconography & media](foundations/iconography-media.md) |
| Tokens | [tokens](tokens/README.md) · [`kbdl.tokens.json`](tokens/kbdl.tokens.json) |
| Themes | [themes](themes/README.md) — [light](themes/light-theme.md), [dark](themes/dark-theme.md), [semantic roles](themes/semantic-roles.md), [adaptation](themes/adaptation.md) |
| Motion | [motion](motion/README.md) — [foundations](motion/foundations.md), [timing & easing](motion/timing-easing.md), [patterns](motion/patterns.md), [accessibility & performance](motion/accessibility-performance.md) |
| Responsive | [responsive](responsive.md) |
| Accessibility | [accessibility](accessibility.md) |
| Components | [components](components/README.md) |
| Patterns | [patterns](patterns.md) |
| Profiles | [profiles](profiles.md) |
| Customization | [customization](customization.md) |
| Adoption | [adoption](adoption.md) |
| Governance | [governance](governance.md) |
| Conventions | [conventions](conventions.md) · [glossary](glossary.md) · [contributing](contributing.md) |
| Completion checklist | [conformance-checklist](conformance-checklist.md) |

## Foundations

Color, typography, spacing, layout grid, shape, elevation, iconography, and
imagery. Base unit 4px; body type 16px; named breakpoints `compact`,
`standard`, `expanded`, `wide`. → [foundations](foundations/README.md)

## Tokens

One framework-independent source of design values, grouped into color,
typography, space, size, breakpoint, container, radius, border, shadow,
opacity, motion, layer, and focus. Use semantic tokens in components; reference
primitives only when defining a new semantic role. → [tokens](tokens/README.md)

## Themes

Light and dark are peers, not a base and a variant. Semantic tokens carry both
values; theme selection follows system preference by default and persists an
explicit user choice. Contrast requirements hold in both. →
[themes](themes/README.md)

## Motion

Duration classes from instant to extended, named easings, and defined
enter/exit relationships. Motion communicates change. Every animation has a
reduced-motion alternative that preserves the information without the movement.
→ [motion](motion/README.md)

## Responsive behaviour

Mobile-first, content-driven breakpoints, fluid containers, adaptive
navigation, touch-target minimums, and reflow at 320px and 200% zoom without
loss of content or function. → [responsive](responsive.md)

## Accessibility

Contrast, non-color communication, keyboard operation, focus visibility, target
size, labelling, error identification, motion sensitivity, zoom and reflow, and
the semantics implementations must expose.

> KBDL provides accessibility design requirements and implementation guidance.
> Conformance must be verified in each product implementation.

→ [accessibility](accessibility.md)

## Components

24 core specifications — button, text link, icon button, text input, textarea,
select, checkbox, radio group, switch, form field, card, badge, alert, toast,
dialog, tooltip, tabs, primary navigation, breadcrumb, table, pagination,
loading indicator, skeleton, and empty state — each with purpose, anatomy,
variants, states, interaction, responsive and keyboard behaviour, accessibility
requirements, content guidance, and token dependencies. →
[components](components/README.md)

## Patterns

Page structure, navigation, forms and validation, loading, empty states,
confirmation, search and filtering, dense data, theme selection, progressive
disclosure, and reduced-motion behaviour. → [patterns](patterns.md)

## Profiles

| Profile | For | Character |
| --- | --- | --- |
| **Showcase** | Portfolios, brand and editorial experiences | Expressive, generous spacing, larger type, richer motion |
| **Precision** | Dashboards, tools, settings, data-heavy work | Dense, efficient, restrained motion, information-first |
| **Flow** | Consumer products, guided and transactional tasks | Approachable, comfortable spacing, clear progression |

Profiles adapt density, motion intensity, and surface treatment. They never
change semantics, keyboard behaviour, or accessibility requirements. →
[profiles](profiles.md)

## Adopting KBDL

Read the principles → choose a profile → map the tokens → apply foundations →
build components → apply responsive and accessibility rules → test the real
implementation → document extensions → contribute back. Includes designer and
developer checklists. → [adoption](adoption.md)

## Extending KBDL

* Compose existing components before creating new ones.
* Add semantic tokens; do not edit primitives in place.
* A new component needs a purpose no existing one serves.
* Extensions must satisfy the same accessibility requirements.
* Record every project deviation in one place.

Change process: [governance](governance.md).

## Version status

KBDL Design Language v1.0. Active documentation is the set listed in the map
above. Changes follow lightweight governance; breaking token changes,
accessibility regressions, removed component behaviour, and major profile
changes get stronger review.

## Historical governance archive

KBDL was previously developed as an audit-grade specification programme with
per-requirement traceability, evidence packages, and a formal owner-decision
workflow.

> Historical governance and validation artifacts are preserved under
> `docs/kbdl/evidence/`. They document earlier project decisions but are not
> active completion gates for KBDL Design Language v1.

The same applies to [validation.md](validation.md),
[traceability-matrix.md](traceability-matrix.md), `traceability-metadata.csv`,
and [decision-register.md](decision-register.md): they are retained as
historical records of how earlier decisions were reached. Where they describe a
release candidate as not ready, list pending owner decisions, or reference
source-model resolution, those statements are historical and describe the
retired programme — they do not gate v1. See [STATUS](STATUS.md) for the scope
change.
