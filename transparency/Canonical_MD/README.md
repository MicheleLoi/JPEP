# Documentation Structure, Provenance, and Metadata

This directory contains the **process documentation materials** associated with the JPEP paper.  
The conceptual role and justification of these artifacts are explained in the paper itself, in **Appendix A** (see `appendix.md`).  

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

The paper (especially Appendix A) explains:
- why these artifacts exist,
- what epistemic role they play,
- and how they relate to claims about transparency and AI-assisted scholarship.

This directory provides the **structured material** that makes those explanations inspectable.
