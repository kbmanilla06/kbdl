# KBDL Status

| | |
| --- | --- |
| **Product name** | KBDL Design Language |
| **Version** | 1.0 |
| **Product type** | Framework-independent design language |
| **Status** | Ready for design and implementation adoption once this scope change passes planning-agent validation |

## Active scope

KBDL Design Language v1 covers:

* Design principles
* Visual foundations — color, typography, spacing, layout, shape, elevation, iconography, imagery
* A single active token reference
* Light and dark themes
* Motion guidance
* Responsive guidance
* Accessibility design requirements
* Core component specifications
* Common experience patterns
* The Showcase, Precision, and Flow profiles
* Adoption and extension documentation

KBDL is documentation and tokens. It is not an application, a component
library, a website, or a framework, and it does not ship runtime code.

## What this status does and does not claim

**Does:** KBDL v1 is coherent and complete enough for a team to design and
build against.

**Does not:** claim that any product built with KBDL is WCAG conformant.
KBDL provides accessibility design requirements and implementation guidance;
conformance must be verified in each product implementation, against a real
build, with real assistive technology. No such verification is claimed here.

**Does not:** authorize or represent any specific application implementation.

## Scope-change history

KBDL began as an audit-grade specification programme. Alongside the design
content, that earlier programme accumulated a governance system:
per-requirement traceability
metadata, a field-source registry, durable owner-decision records, evidence
packages with checksummed transcripts, and a chain of planning-agent
validation and remediation prompts.

That machinery did its job — the design foundations are unusually well
specified because of it — but it grew until routine documentation work
required an evidence package, and progress was gated on resolving hundreds of
per-field source-provenance questions that had no bearing on whether a
designer could use KBDL.

On 2026-07-30 the project owner deliberately simplified the project:

> KBDL is a design language only.

This approval retires the following as **completion gates** for v1: the
remaining owner-decision queue, per-requirement source-model resolution,
field-source-registry completion, the PA1 remediation chain, per-issue
metadata-recording prompts, and audit-grade evidence manifests for routine
changes.

Nothing is deleted or disparaged. The earlier work was rigorous and its
records remain intact.

## Historical records

Preserved, unchanged, and no longer active completion gates:

* `docs/kbdl/evidence/**` — historical evidence packages, validators,
  transcripts, owner-decision records, and the field-source registry
* `docs/kbdl/validation.md` — the historical validation-gate record
* `docs/kbdl/traceability-matrix.md` and `docs/kbdl/traceability-metadata.csv`
  — the historical per-requirement traceability records
* `docs/kbdl/decision-register.md` — historical decision records

These document how earlier decisions were reached. Read them for provenance,
not for the current state of the design language. Where they describe a
release candidate as `NOT READY`, or list pending owner decisions, those
statements are historical: they refer to the retired specification programme,
not to KBDL Design Language v1.

## Governance from here

Lightweight and proportionate — see [governance](governance.md). Stronger
review is retained only for breaking token changes, accessibility
regressions, removed component behaviour, major profile changes, and
backward-incompatible renames.
