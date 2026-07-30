# KBDL Design Language Completion Checklist

The lean checklist for KBDL Design Language v1. It verifies that the design
language is documented and internally consistent — not that every historical
requirement ID has been re-verified, and not that any product built with KBDL
is conformant.

Run [`scripts/validate_design_language.py`](scripts/validate_design_language.py)
to check the mechanical items automatically.

## Documentation completeness

- [x] **Principles documented** — [principles](principles.md), summarised in the
      [README](README.md)
- [x] **Tokens documented** — [tokens](tokens/README.md) with a single active
      source at [`kbdl.tokens.json`](tokens/kbdl.tokens.json)
- [x] **Light and dark themes documented** — [themes](themes/README.md),
      including semantic mappings and selection behaviour
- [x] **Motion documented** — [motion](motion/README.md): durations, easings,
      relationships, and reduced-motion substitutions
- [x] **Responsive behaviour documented** — [responsive](responsive.md):
      breakpoints, containers, navigation, targets, reflow
- [x] **Accessibility guidance documented** — [accessibility](accessibility.md)
- [x] **Core component specifications documented** — 24 components in
      [components](components/README.md), each with the required sections
- [x] **Common patterns documented** — [patterns](patterns.md)
- [x] **Three profiles documented** — Showcase, Precision, and Flow in
      [profiles](profiles.md)
- [x] **Adoption guide documented** — [adoption](adoption.md), with designer and
      developer checklists

## Mechanical validation

- [x] **Token JSON valid** — parses, no duplicate keys, required groups present
- [x] **Token names follow the convention** — lowercase, dot-separated,
      hierarchical
- [x] **Internal links valid** — every relative Markdown link in the active
      documentation resolves
- [x] **Component sections present** — every component has purpose, anatomy,
      variants, states, interaction, responsive, keyboard, focus, accessibility,
      content, and token guidance
- [x] **Disclaimers present** — the accessibility conformance disclaimer and the
      historical-archive notice
- [x] **No active legacy gates** — active documentation does not present the
      retired owner-decision queue, field-source resolution, or the PA1
      remediation chain as blocking v1

## Preservation

- [x] **Historical evidence preserved** — `docs/kbdl/evidence/**` is unchanged
      and labelled as historical reference
- [x] **Historical governance records retained** — `validation.md`,
      `traceability-matrix.md`, `traceability-metadata.csv`, and
      `decision-register.md` are unchanged and explicitly classified as
      historical in [STATUS](STATUS.md)

## Honest claims

- [x] **No implementation-level conformance claimed** — KBDL provides
      accessibility design requirements and implementation guidance;
      conformance must be verified in each product implementation
- [x] **No application, framework library, backend, API, or deployment
      created** — KBDL ships documentation and tokens only

## Not required for v1

Explicitly out of scope, by the approved scope change in [STATUS](STATUS.md):
resolving the remaining historical owner decisions, reducing the historical
field-source registry to zero failures, continuing the PA1 remediation chain,
completing every earlier roadmap prompt, generating new evidence packages,
producing audit-grade checksums for routine documentation work, proving
implementation-level WCAG conformance without an implementation, or writing
production component code.
