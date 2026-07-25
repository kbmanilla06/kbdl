# KBDL Traceability Matrix

Status: `Approved` framework; rows below reflect only KBDL-001 scope.

Return to the [specification index](README.md).

## Purpose

This matrix connects each approved blueprint concept or KBDL-001 requirement to
its roadmap origin, its requirement ID (where assigned), its location in the
specification, its status, and how it will be or was validated. It is updated
whenever a requirement is created, changes status, or is validated.

## Fields

| Field | Meaning |
| --- | --- |
| Blueprint section | The approved KBDL blueprint concept this row traces to. |
| Roadmap prompt | The roadmap step (e.g. KBDL-001) that owns this row. |
| Requirement ID | The requirement ID, if one has been assigned yet. |
| Specification location | The file (and heading, where applicable) this concept lives in. |
| Status | One of the labels in [conventions.md](conventions.md#1-status-labels). |
| Validation method | How this requirement is or will be checked (for example manual review, link check, Markdown lint). |
| Validation evidence | A pointer to where evidence is recorded, or `Not verified` if none exists yet. |
| Known limitation | Any known gap or caveat, or `None identified`. |
| Related decision | Decision ID from the [decision register](decision-register.md), if applicable. |
| Notes | Free text. |

## KBDL-001 Rows

| Blueprint section | Roadmap prompt | Requirement ID | Specification location | Status | Validation method | Validation evidence | Known limitation | Related decision | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Project naming | KBDL-001 | Not applicable | [decision-register.md](decision-register.md#kbdl-dec-001--project-name-is-kbdl) | Approved | Manual review | This document | None identified | KBDL-DEC-001 | Naming decision, not a technical requirement. |
| Specification architecture | KBDL-001 | KBDL-GOV-001 | [governance.md](governance.md#kbdl-gov-001--specification-architecture-is-established) | Approved | Manual review | This document, [README.md](README.md) | None identified | Not applicable | Demonstrates the requirement-ID convention. |
| Accessibility baseline protection | KBDL-001 | KBDL-GOV-002 | [governance.md](governance.md#kbdl-gov-002--accessibility-requirements-are-protected) | Approved | Manual review | [governance.md](governance.md) | Not verified against a real accessibility requirement, since none exist yet | KBDL-DEC-010 | Rule takes effect once `A11Y` requirements exist in a later module. |
| Documentation governance process | KBDL-001 | KBDL-GOV-003 | [governance.md](governance.md) | Approved | Manual review | [governance.md](governance.md) | None identified | Not applicable | Establishes change control before design content exists. |
| Visual consistency strategy | KBDL-001 | Not applicable | [decision-register.md](decision-register.md#kbdl-dec-003--visual-consistency-is-the-cross-project-strategy) | Approved | Manual review | This document | Will require `FND`, `THM`, `PRO` requirements in later steps | KBDL-DEC-003 | No visual foundation requirements exist yet; out of scope for KBDL-001. |
| Manual customization strategy | KBDL-001 | Not applicable | [decision-register.md](decision-register.md#kbdl-dec-004--customization-is-manual-and-documented) | Approved | Manual review | This document | Will require `CUS` requirements in a later step | KBDL-DEC-004 | Out of scope for KBDL-001. |
| Progressive delivery / roadmap gating | KBDL-001 | Not applicable | [governance.md](governance.md) | Approved | Manual review | This document | None identified | KBDL-DEC-005 | Enforced by the progression gate in this prompt and in governance.md. |
| Project profiles (Showcase, Precision, Flow) | KBDL-001 | Not applicable | [README.md](README.md#document-hierarchy) | Approved (naming only) | Manual review | This document | No `PRO` requirements exist yet | KBDL-DEC-006 | Only the profile names and future module location are recorded. |
| Responsive web platform context | KBDL-001 | Not applicable | [decision-register.md](decision-register.md#kbdl-dec-007--responsive-web-is-the-platform-context) | Approved | Manual review | This document | No `RSP` requirements exist yet | KBDL-DEC-007 | Out of scope for KBDL-001. |
| Adaptive theme behavior | KBDL-001 | Not applicable | [decision-register.md](decision-register.md#kbdl-dec-008--adaptive-light-and-dark-theme-behavior) | Approved | Manual review | This document | No `THM` requirements exist yet | KBDL-DEC-008 | Out of scope for KBDL-001. |
| Controlled expressive motion | KBDL-001 | Not applicable | [decision-register.md](decision-register.md#kbdl-dec-009--expressive-but-controlled-motion) | Approved | Manual review | This document | No `MOT` requirements exist yet | KBDL-DEC-009 | Out of scope for KBDL-001. |
| WCAG 2.2 AA baseline with enhanced motion safety | KBDL-001 | Not applicable | [decision-register.md](decision-register.md#kbdl-dec-010--wcag-22-aa-baseline-with-enhanced-motion-safety) | Approved | Manual review | This document | No `A11Y` requirements exist yet | KBDL-DEC-010 | Protected as a locked-rule category by KBDL-GOV-002. |
| Later modules (visual foundations, themes, motion, responsive, accessibility, components, profiles, customization, validation) | KBDL-002 through KBDL-010 | Not assigned | Planned locations only, see [README.md](README.md#document-hierarchy) | Deferred | Not applicable | Not applicable | Not designed; intentionally out of scope for KBDL-001 | Not applicable | Do not treat as implemented or verified. |

## Notes on Scope

No requirement in this matrix outside `GOV` has been implemented, designed, or
validated. Rows for later roadmap modules exist only to show where their
future requirements will be traced once their roadmap step is reached.
