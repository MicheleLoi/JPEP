# Documentation Structure, Provenance, and Metadata

This directory contains the **process documentation materials** associated with the JPEP paper.
The conceptual role and justification of these artifacts are explained in the paper itself, in §6 ("Community Assessment of Documentation Adequacy") and in the closing **AI Usage and Documentation Archive** note that follows the conclusion.

The archive is also accompanied by three documents that exist *inside* this directory and that an external reader should consult before, or alongside, the underlying materials:

- **SP-1 (`SP1_AIUsageDeclaration/`)** — concise declaration of how AI was used and orientation for navigating the archive.
- **SP-2 (`SP2_NavigationAndArchitecture/`)** — document-type ontology, metadata infrastructure, and structured index to SP-3, SP-4, SP-5.
- **SP-3 (`SP3_DocumentationAdequacy/`)** — the author's documentation-adequacy account: the argument that the record satisfies the §6 criteria, with a worked example.

What follows documents **how the materials are organized**, **how provenance is recorded**, and **how metadata should be read**.

---

## Structural grouping (SPs)

The materials are grouped into **SPs (Structural Partitions)**.
Each SP groups artifacts according to their **function within the documented process**, not according to section order or file chronology.

### SP4 — Process Documentation

SP4 contains the **formal process record**.
Artifacts in SP4 document decisions, constraints, and transformations applied to the manuscript.

This includes, for example:
- section-level guidance,
- modification logs,
- pattern summaries,
- epistemic traces and coordination documents.

SP4 is the primary space used to reconstruct **what decisions were made**, **in which context**, and **with which inputs**.

---

### SP5 — Prompt Development Logs and Notes

SP5 contains **prompt development logs (PDLs)** and **notes** that support the interpretation and reconstruction of the process.

Artifacts in SP5 typically:
- document how prompts, instructions, or evaluative criteria were developed,
- preserve intermediate material needed to reconstruct later documentation,
- serve as reference material for SP4 artifacts.

SP5 does **not** represent a different epistemic status.
It groups artifacts by **role in the documentation system**, not by importance or authority.

---

## Provenance

Each artifact records its provenance explicitly using metadata.

Provenance refers to:
- the **source chat(s)** from which the artifact derives,
- the **date(s)** of the underlying work,
- the relationship between the artifact and other documented materials.

The same chat material may give rise to **multiple artifacts** serving different documentary roles (e.g. guidance, modification log, note).
Metadata make these relationships explicit, preventing ambiguity about origin or reuse.

---

## Metadata as the organizing layer

Metadata headers are the **authoritative organizing layer** of this repository.

They are used to:
- locate artifacts within the SP structure,
- record provenance and relationships,
- distinguish writing activity from documentation activity,
- enable reconstruction of causal chains across artifacts.

Readers should rely on metadata — rather than filenames, folder placement, or textual similarity — to understand how artifacts relate to one another.

---

## Documentation timing

Not all documentation was created at the same time as writing.

In some cases:
- artifacts were documented contemporaneously,
- in others, documentation was reconstructed retrospectively from preserved chat material.

Metadata always distinguish:
- when the underlying work occurred, and
- when the artifact was documented or formalized.

Retrospective documentation is explicitly marked and treated as part of the documented process.

---

## Relationship to the paper

This repository is intended to be read **in conjunction with the paper**, not as a standalone explanation.

The paper explains:
- why these artifacts exist (§3: agent-integrity grounding),
- what epistemic role they play (§5: documentation as tracking, not reproducibility),
- what assessment of the apparatus must enable (§6: the three criteria),
- how the five-element framework instantiates those criteria (§6.4 onward),
- and how the present archive instantiates the framework (closing AI Usage and Documentation Archive note).

This directory provides the **structured material** that makes those explanations inspectable.
