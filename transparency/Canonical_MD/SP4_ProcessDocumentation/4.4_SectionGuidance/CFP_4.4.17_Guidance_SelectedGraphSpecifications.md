---
project: JPEP
document_type: Type 6 - Section Guidance
title: "Guidance: Selected Graph Specifications for Paper Figures"
date_created: 2026-04-01
session_id: SID-20260401
status: active
derived_from: "CFP_4.7.9_EpistemicTrace_SelectedGraphsVsMegagraph.md"
feeds_into:
  - CFP_5.3.7_SelectedGraphCandidates.md
  - paper_figures_selected
relevance_for: [figures, appendix-a, selected-graphs, visualization]
---

# Guidance: Selected Graph Specifications

## Purpose

Identify 2–4 subgraphs of the megagraph that can serve as paper figures. Each must make a specific philosophical argument, be readable in print (static, no interaction), and map onto at least one of the three adequacy criteria from Section 7 (attribution, trajectory, understanding-and-endorsement).

## Criteria for a good selected graph

1. **Makes a claim** — the caption should be arguable, not just descriptive. A graph that illustrates what adequate documentation looks like for the trajectory criterion is an argument; a graph that shows all artifacts from October 2025 is not.
2. **Readable at print scale** — maximum ~15 nodes, directed edges, clean layout. Labels must be legible without zooming.
3. **Grounded in actual archive data** — every node and edge must correspond to a real artifact or verified connection in the archive. No illustrative fabrications.
4. **Contrastive where possible** — showing presence and absence of documentation (v1/v2 vs CFP, archived vs ghost nodes) is more powerful than showing presence alone.

## Types to search for

| Type | What it shows | Criterion illustrated |
|---|---|---|
| Production chain | Inputs → session hub → outputs for one section | All three: hub=attribution, chain=trajectory, modlog=endorsement |
| Version chain | v1→v2→v3 sequence for one section draft, showing what changed each step | Trajectory |
| Contrast | Same section: v1/v2 sparse vs CFP dense documentation | Trajectory + attribution gap |
| Consolidation | Multiple sections merging into one | Trajectory (structural transformation, not just linear) |
| Feed-forward | How outputs of one section became inputs of the next | Trajectory across sections |
| Self-referential | A case where documentation and artifact collapse (4.2.1) | Limits of the framework |

## Output format (for each candidate)

```
### [Graph name]
**Type:** production chain / version chain / contrast / consolidation / feed-forward / self-referential
**Claim:** [One sentence: what this graph argues]
**Criterion:** attribution / trajectory / understanding-and-endorsement
**Nodes:** [list of artifact IDs]
**Edges:** [list of source → target with field name]
**Status:** verified / needs checking / speculative
**Notes:** [any caveats, ghost nodes, limitations]
```

## Constraints

- Do not include Paper/MDversion/ files as nodes unless essential
- Ghost nodes (unarchived in-chat states) are acceptable and should be marked as such — they make absences visible
- Prefer CFP-phase artifacts where possible; contrast graphs specifically need v1/v2 nodes
