---
project: JPEP
document_type: Type 9 - Epistemic Trace
title: "Epistemic Trace: Selected Graphs vs Megagraph — What Visualization Serves the Argument"
date_created: 2026-04-01
session_id: SID-20260401
inputs:
  - CFP_5.3.7_SelectedGraphCandidates.md
status: complete
author: Michele Loi (direction) + Claude Sonnet 4.6 (transcription)
feeds_into:
  - "CFP_4.4.17_Guidance_SelectedGraphSpecifications.md"
  - "CFP Phase 4: Conclusion and Abstract"
relevance_for:
  - Appendix A (figures and visualization)
  - Section 7 (what makes documentation assessable)
  - Supplementary materials architecture
---

# Epistemic Trace: Selected Graphs vs Megagraph

## Question posed

The project has been building a megagraph (currently 189 nodes, 213 edges) of the full JPEP documentation network. The question arose: for a seminal paper on AI-assisted scholarship transparency, which is more valuable — the megagraph or selected graphs of specific revision processes?

## Reasoning

**The megagraph is the transparency apparatus, not an argument about it.** At 189 nodes it is unreadable in print and requires prior knowledge of the system to interpret. The claim it makes is quantitative ("we documented a lot"), not philosophical. It belongs in the supplementary materials on GitHub — an interactive artifact a motivated reader can explore.

**Selected graphs can make specific philosophical claims.** The paper argues transparency requires three criteria: attribution, intellectual trajectory, understanding-and-endorsement. A well-chosen graph can show what each criterion looks like when met — and what its absence looks like. That is argumentative work. A figure in a philosophy paper should move the argument forward, not display infrastructure.

**Types identified:**

- *Production chain graph*: one well-documented section showing all three criteria simultaneously — guidance in, session hub, outputs. Section 9 is the cleanest candidate.
- *Version chain graph*: a CFP section through v1→v2→v3, or the 4.2.1 case. Shows intellectual trajectory as a directed sequence. Makes the self-referential structure visible and explicable.
- *Contrast graph*: v1/v2 phase vs CFP phase for the same section. Sparse connections left (retrospective reconstruction, ghost nodes, lost IDs), dense right (contemporaneous documentation, full chains). Maps onto the paper's argument about what mandates cannot produce vs what a specified framework enables.
- *Consolidation graph*: three old sections merging into one (4.2.5). Shows documentation must track structural transformation, not just linear development. Relevant to the trajectory criterion.

**The relationship between the two:**

The selected graphs are subgraphs of the megagraph, each isolating a pattern the paper needs to argue about. The megagraph records; the selected graphs make the record assessable. This distinction maps directly onto Section 7's argument: transparency is not just recording everything — it is producing a record that is assessable.

## Decision

Selected graphs (2–3) in the paper or appendix, each captioned as an argument. Megagraph in the GitHub repository linked from Appendix A. A canonical example graph (probably Section 9 production chain) appears in both.
