# KBDL Governance

Lightweight change control for KBDL Design Language v1. Proportionate to the
change: most documentation work needs a clear rationale and a review, not an
audit trail.

## Change process

1. **Propose** the change in writing — one paragraph is often enough.
2. **Explain the problem** it solves, for users or for implementers. A change
   with no stated problem does not proceed.
3. **Identify what it touches** — which tokens, components, patterns, or
   profiles.
4. **Review accessibility and cross-profile impact.** Does it weaken contrast,
   focus, keyboard operation, or target size? Does it work in Showcase,
   Precision, and Flow?
5. **Approve** — a maintainer for ordinary changes; see below for changes
   needing stronger review.
6. **Update** the affected active documentation and
   [`tokens/kbdl.tokens.json`](tokens/kbdl.tokens.json) together, in one change,
   so they never disagree.
7. **Version** — increment when appropriate (see versioning).

Run [`scripts/validate_design_language.py`](scripts/validate_design_language.py)
before publishing.

## What routine changes do *not* require

Clarifying wording, adding an example, fixing a link, adding a component
variant, or documenting an existing behaviour more clearly does **not** require:

* a field-source-registry update
* an owner-decision record per field
* a separate implementation prompt per metadata correction
* a new evidence package
* per-field validation checks
* planning-agent remediation for harmless wording

## Changes needing stronger review

Two reviewers, and an explicit migration note:

* **Breaking token changes** — renaming or removing a token, or changing a
  value in a way that alters existing layouts
* **Accessibility regressions** — anything that reduces contrast, focus
  visibility, keyboard operability, or target size
* **Removed component behaviour** — dropping a state, variant, or interaction
  implementers may depend on
* **Major profile changes** — altering what a profile means or how far it may
  diverge
* **Backward-incompatible naming** — changes that break token or component
  references

For these, record: what changed, why, who approved it, and how adopters
migrate.

## Versioning

* **Patch** — clarifications, typos, examples, non-breaking additions to prose
* **Minor** — new components, patterns, tokens, or guidance that is additive
* **Major** — breaking token or component changes, or a change in what a
  profile means

## Deciding conflicts

When two documents disagree:

1. Prefer the value presented as the current approved design default.
2. Record the chosen value in [tokens](tokens/README.md) — the single active
   source.
3. Note the superseded value briefly, as a migration note.
4. Do not reopen the retired owner-decision workflow.

## Contributing

See [contributing](contributing.md) and the extension rules in
[adoption](adoption.md). Extensions that prove generally useful are the best
candidates for promotion into KBDL itself.

## Historical governance

> Historical governance and validation artifacts are preserved under
> `docs/kbdl/evidence/`. They document earlier project decisions but are not
> active completion gates for KBDL Design Language v1.

The earlier programme used per-requirement traceability, durable
owner-decision records, a field-source registry, and evidence packages with
checksummed transcripts. That machinery is retained for provenance and is no
longer part of routine change control. `validation.md`,
`traceability-matrix.md`, `traceability-metadata.csv`, and
`decision-register.md` are historical records in the same sense.

See [STATUS](STATUS.md) for the scope change that retired it.
