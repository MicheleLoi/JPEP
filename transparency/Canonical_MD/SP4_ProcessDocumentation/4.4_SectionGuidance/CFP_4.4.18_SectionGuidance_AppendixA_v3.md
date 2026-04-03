---
project: JPEP
document_type: Type 6 - Section Guidance
label: CFP_4.4.18_SectionGuidance_AppendixA_v3
title: "Appendix A v3 — Section Guidance for CFP Adaptation"
date_created: 2026-04-01
status: ready_to_implement
session_id: SID-20260401-111336
branch: cfp-ai-ethics-inquiry
feeds_into:
  - "Appendix A v3 draft (CFP adaptation)"
  - "SP-2: Reproduction Package (rewrite)"
  - "SP-3: Reproduction Guide (rewrite)"
derived_from:
  - "Paper/MDversion/appendix.md (v2 baseline)"
  - "II_5.3.3_A4_rewritten.md (v2 diff for A.4)"
  - "CFP_5.3.7_SelectedGraphCandidates.md (verified graph candidates)"
  - "CFP_4.7.8_EpistemicTrace_SelfReferentialDocumentation.md"
  - "CFP_4.7.9_EpistemicTrace_SelectedGraphsVsMegagraph.md"
  - "CFP_5.3.4_Note_SkeletonAndConnectionsStatus.md"
related:
  - "CFP_5.3.1_WorkPlan_CFP_Adaptation.md (master work plan)"
  - "4.4.12_From_Draft_1_Appendix_to_Appendix_A.md (original appendix guidance)"
---

# Appendix A v3 — Section Guidance for CFP Adaptation

**Design session:** 2026-04-01 (SID-20260401-111336)
**Designed by:** Opus | **To implement:** drafting agent (Sonnet or Opus)
**Baseline:** `Paper/MDversion/appendix.md` (v2, current canonical Appendix)
**Output file:** new Appendix A v3 draft (location TBD by implementer; suggested: `CFP_5.4.10_AppendixA_v3.md` in `5.4_SectionDrafts/`)

---

## 0. Purpose of this document

This is a design document for drafting Appendix A v3. It is not the appendix itself. The person or agent reading this guidance should use it as a structured plan for what to verify, what to rewrite, what to add, and how to structure the output so that it feeds directly into SP-2 (Reproduction Package) and SP-3 (Reproduction Guide).

---

## 1. What v2 says and what has changed since

### 1.1 The v2 story (summary)

Appendix A v2 tells this story:

- **A.1** describes a reproduction procedure centred on Reviewer B loading SP-1 into an LLM, using SP-2 for section guidance, generating comparable work, and comparing via trajectory matching. Time estimate: 5-9 hours.
- **A.2** narrates the writing process across six phases, emphasising three patterns: tangential conversations becoming foundational, self-recursion in documentation development, and branching when different work types require different approaches. Includes a flow diagram (Figure 2).
- **A.3** defines the eleven document types (Types 1-11) with a summary table.
- **A.4** lists all supplementary materials in the five SP packages with file-by-file inventories.
- **A.5** provides navigation guidance for three audiences: Reviewer B, editorial assessment, researchers.

### 1.2 What the CFP adaptation changed in the paper

The CFP adaptation made structural changes that v2's Appendix does not reflect:

1. **The reproduction test is dropped.** Section 7 (CFP) replaces the reproduction test with documentation-adequacy assessment. The three criteria are attribution, intellectual trajectory, and understanding-and-endorsement. A.1's reproduction procedure (load SP-1, generate comparable work, compare) is therefore obsolete as described. SP-2 and SP-3 must be reconceived around documentation assessment, not reproduction.

2. **The dual-reviewer architecture is reframed.** Reviewer B no longer "reproduces" — Reviewer B assesses whether the documentation record is adequate to trace the intellectual contribution. The time estimates, pass thresholds, and "comparison criteria" in A.1 and A.5 assume the reproduction model.

3. **New sections and version chains exist.** The CFP phase produced six new section drafts (Introduction, Section 2, 3, 5, 6, 7), each with its own modlog, some with version chains (Section 6: v1/v2/v3), PDLs, and epistemic traces. None of these appear in v2's file inventories (A.4).

4. **New metadata infrastructure exists.** Session IDs (SIDs), hub files (`_HUBS/`), `derived_from` / `feeds_into` / `output_completed` fields, version chains, and the hub-generation script are all CFP-phase innovations. The eleven document types in A.3 do not mention session hubs, metadata fields, or the graph infrastructure. The skeleton covers 88/128 artifacts (68%); 48 hub nodes exist.

5. **The section numbering changed.** v2 maps old Roman numerals to new Arabic. The CFP adaptation uses Arabic throughout (Section 2, 3, 5, 6, 7) with CFP_ prefixes. The renumbering table in A.4 is still correct but incomplete — it does not show CFP-phase artifacts.

6. **Self-referential documentation acknowledged.** CFP_4.7.8 documents three layers of self-reference. v2 hints at self-recursion (Pattern 2 in A.2) but does not address the deeper issue: the documentation system was built under exactly the conditions the paper analyses.

### 1.3 Verification checklist — what the drafter must check

Before writing, the drafter should verify these specific claims against current SP4 state:

| v2 claim | Where in v2 | Verification needed |
|---|---|---|
| "Reviewer B receives three core documents" (SP-1, SP-2, SP-3) | A.1, para 1 | SP-2 and SP-3 do not yet exist in CFP form. The claim must be reframed: what does Reviewer B receive under the documentation-adequacy model? |
| "Basic workflow: load SP-1, use SP-2, generate, compare" | A.1, para 3 | Obsolete. The workflow under documentation-adequacy assessment is different: examine SP-4, assess against the three criteria. |
| "5-9 hours total" | A.1, para 4 | Not meaningful without a reproduction procedure. Replace with a realistic estimate for documentation assessment, or drop. |
| "trajectory matching rather than output matching" | A.1, A.5 | The concept survives but the operationalisation changes. Trajectory matching in v2 means comparing generated output to submitted paper. In the CFP framework it means reading the modlog chain and assessing whether the documented trajectory is plausible and sufficient. |
| Figure 2 (six-phase flow diagram) | A.2 | Figure 2 covers only the v1/v2 writing process. The CFP phase is entirely absent. Either: (a) retain Figure 2 as a historical record and add selected graphs for the CFP phase, or (b) replace Figure 2 with the selected graphs and describe the v1/v2 flow in prose. Option (a) is recommended. |
| Eleven document types | A.3 | The eleven types still hold but new infrastructure layers sit on top of them: session hubs, metadata fields, hub scripts. A.3 should either acknowledge these as infrastructure supporting the type system or add them as a twelfth+ type. |
| File inventories in A.4 | A.4 | Incomplete. CFP-phase modlogs (CFP_4.2.14 through CFP_4.2.19), section drafts (CFP_5.4.3 through CFP_5.4.9), PDLs (CFP_5.2.1), epistemic traces (CFP_4.7.5 through CFP_4.7.9), guidance files (CFP_4.4.14 through CFP_4.4.17), and notes (CFP_5.3.1 through CFP_5.3.7) are all missing. The III_ prefix files are also absent. |
| "80-110 pages across five packages" | A.4, total volume | Outdated. The archive has grown significantly. Recount or provide a credible estimate. |
| Navigation guidance in A.5 | A.5 | Assumes reproduction workflow. Must be rewritten for documentation-adequacy assessment. |

---

## 2. New stories the metadata enables

v2 told three patterns (tangential conversations, self-recursion, branching). These remain valid for the v1/v2 phase. The CFP phase enables additional stories that are both more specific and more directly tied to the paper's argument.

### 2.1 Selected graphs as argumentative figures

Three verified graph candidates exist (CFP_5.3.7). Each makes a specific philosophical claim:

**Graph 1 — Section 5 production chain (attribution + trajectory + understanding-and-endorsement):** Shows a single session hub encoding all three transparency criteria simultaneously. Nodes: source draft, session hub (CHAT_SID-20260317-191544), section draft (CFP_5.4.7), modlog (CFP_4.2.17). Claim: the three criteria can be satisfied contemporaneously with production, not only retrospectively.

**Graph 2 — Section 6 version chain (trajectory):** Three successive drafts (v1/v2/v3) with `derived_from` links and a 13-entry modlog. Claim: intellectual trajectory in AI-assisted writing is documentable as a directed sequence; the record of what changed and why is as significant as the final output.

**Graph 3 — Introduction contrast (v1/v2 phase vs CFP phase):** Two panels showing the same section with radically different documentation records. Left: ghost nodes, null source_chat_id, self-referential output. Right: session hub, named inputs, related_documents list. Claim: what mandates cannot produce, a specified framework enables.

**How to use them in v3:** Each graph should appear as a captioned figure in a new A.2 or A.3 subsection (see structure below). The caption should state the claim, not just describe the graph. The surrounding prose should connect the graph to the paper's argument (Section 7 criteria for Graphs 1-2; Section 2 mechanisms for Graph 3).

### 2.2 The self-referential documentation story

CFP_4.7.8 documents three layers:

1. The documentation reproduces the mechanisms Section 2 describes (definitional flexibility, temporal discounting).
2. The Section 7 criteria (attribution, trajectory, understanding-and-endorsement) are applied to the documentation itself — and tested against it during the v1/v2 consolidation.
3. The 4.2.1 case: version-chain self-reference where the modlog's output points to itself at a different state.

v2 mentioned self-recursion as a pattern but did not connect it to the paper's argument. v3 should make this explicit: the documentation record is an instance of the problem the paper analyses, not a solved example of it. The v1/v2 phase was documented retrospectively and partially; the CFP phase is documented prospectively and more fully. This difference demonstrates the paper's claim about what infrastructure enables.

### 2.3 Self-philology and the conditions for retrospective recovery

CFP_4.7.8 also introduces the concept of self-philology: applying philological method to one's own production process. Four conditions for successful retrospective reconstruction were identified:

1. Session identifiers must survive (UUIDs preserved in frontmatter).
2. Conversations must remain accessible (vendor data retention).
3. Enough internal structure must exist to generate testable hypotheses.
4. A human judgment layer is required.

This is new argumentative material. v3 should present self-philology as the fallback (confirming the framework's coherence) whose difficulty confirms the framework's necessity. This connects directly to Section 7's argument that the criteria must be satisfied contemporaneously.

### 2.4 The architectural decision about section drafts

CFP_5.3.4 records a non-obvious design choice: section drafts intentionally lack session IDs because they are multi-session artifacts. The correct locus of session-to-revision tracing is the modlog, not the draft. This is worth explaining in v3 because it anticipates a reader objection ("why don't the drafts have session IDs?") and turns it into an argument about what adequate documentation architecture looks like.

### 2.5 The megagraph as supplementary, selected graphs as argumentative

CFP_4.7.9 records the decision: the megagraph (189 nodes, 213 edges) belongs in the GitHub supplementary materials; selected graphs belong in the paper. The relationship: selected graphs are subgraphs of the megagraph, each isolating a pattern the paper needs to argue about. The megagraph records; the selected graphs make the record assessable. This distinction maps onto Section 7's argument.

---

## 3. How v3 should be structured to feed SP-2 and SP-3

### 3.1 The key shift

v2's Appendix was designed to feed a reproduction procedure. v3 must feed a documentation-adequacy assessment. The difference:

- **Reproduction model (v2):** Reviewer B needs to *do* something — load prompts, generate text, compare. The Appendix provides the recipe and the materials list.
- **Documentation-adequacy model (v3):** Reviewer B needs to *read* something — the documentation record — and assess whether it satisfies three criteria. The Appendix provides the map and the assessment framework.

SP-2 under the new model is not a "reproduction package" but a **navigation document** — it tells Reviewer B where to find the evidence for each criterion, section by section. SP-3 is not a "reproduction guide" but a **documentation adequacy account** — it argues that the record satisfies the three criteria and points to the evidence.

### 3.2 What v3 must provide that SP-2 and SP-3 will draw on

1. **A clear map of the documentation record.** Which artifacts exist, what they cover, how they link. The file inventories (A.4) serve this function but must be updated and restructured around the three criteria rather than around the five SP packages.

2. **Worked examples.** The selected graphs are worked examples of what the documentation record looks like when it meets the criteria. SP-3 will reference these when arguing adequacy.

3. **Honest acknowledgment of gaps.** The v1/v2 phase has weaker documentation (40 orphaned artifacts, 5 modlogs without SIDs, ghost nodes). SP-3 cannot claim full adequacy for the v1/v2 phase — it must distinguish between the prospective CFP record and the partly reconstructed v1/v2 record. v3 should provide the factual basis for this distinction.

4. **The architectural rationale.** Why session IDs live on modlogs not drafts, why the hub system was built, why `derived_from` and `feeds_into` fields were added. SP-2 needs this to explain the navigation logic; SP-3 needs this to argue the design was principled rather than ad hoc.

### 3.3 Proposed v3 structure

| Section | Content | Relation to v2 | SP-2/SP-3 function |
|---|---|---|---|
| **A.1 Overview** | What the documentation record is and how to assess it. Replace the reproduction procedure with a documentation-adequacy assessment overview. State the three criteria. Point to SP-3. | Replaces v2 A.1 entirely | SP-3 draws its assessment framework from here |
| **A.2 The Documentation Record** | Two-phase narrative: v1/v2 phase (retrospective, partial) and CFP phase (prospective, structured). Retain v2 A.2's three patterns as historical context for the v1/v2 phase. Add the self-referential documentation story and the self-philology argument for the CFP phase. | Major rewrite of v2 A.2 | SP-3 draws its honest-acknowledgment-of-gaps argument from here |
| **A.3 Selected Documentation Graphs** | NEW section. Present the 2-3 selected graphs as captioned argumentative figures. Each graph: nodes, edges, claim, connection to Section 7 criteria. | New (replaces or supplements Figure 2) | SP-2 uses these as navigation examples; SP-3 uses them as adequacy evidence |
| **A.4 Document Types and Infrastructure** | Retain the eleven types from v2 A.3. Add a subsection on infrastructure layers: session hubs, metadata fields, hub scripts, the skeleton. Explain the architectural decision about section drafts. | Expansion of v2 A.3 | SP-2 uses this as its structural reference |
| **A.5 Supplementary Materials Inventory** | Updated file inventories covering both v1/v2 and CFP artifacts. Organized by SP package but with CFP-phase additions clearly marked. Updated volume estimate. | Update of v2 A.4 | SP-2 draws its materials list from here |
| **A.6 Guide to Using Supplementary Materials** | Rewritten for documentation-adequacy assessment. Three audiences: documentation assessor (replaces Reviewer B), editorial assessment, researchers. For assessor: "examine modlog chains for trajectory evidence; check hub files for attribution; look at review records for understanding-and-endorsement." | Rewrite of v2 A.5 | SP-3's practical instructions derive from here |

---

## 4. Drafting instructions

### 4.1 What to keep from v2

- **A.2 patterns 1-3** (tangential conversations, self-recursion, branching): retain as historical description of the v1/v2 phase. They are accurate and well-written. Shorten slightly if needed for space.
- **A.3 eleven document types** (Type 1-11 table and descriptions): retain with minor updates. The type system is stable.
- **Section numbering reference table**: retain verbatim.
- **The ecological validity principle** stated in A.4: "documentation shows actual process rather than retrospective reconstruction." Keep this — it is even more important in v3 given the self-referential context.

### 4.2 What to rewrite

- **A.1 entirely.** The reproduction procedure is obsolete. Replace with documentation-adequacy assessment overview. Do not try to preserve the reproduction language — it contradicts what Section 7 now says.
- **A.5 navigation guidance.** Reframe for documentation-adequacy assessment, not reproduction. The three audiences remain but their tasks change.
- **File inventories (A.4).** Add all CFP-phase and III-phase artifacts. Use the current archive state, not the v1 baseline.

### 4.3 What to add

- **Selected graphs section (new A.3).** Use the candidates from CFP_5.3.7. Provide textual descriptions sufficient for a figure designer to produce the graphs. Each graph needs: node list, edge list, claim statement (1-2 sentences), connection to Section 7 criteria.
- **Self-referential documentation discussion.** Draw from CFP_4.7.8. Keep it concise (300-400 words). The point is not to narrate the consolidation work but to make the argumentative point: this paper's documentation record is an instance of the problem it analyses.
- **Self-philology paragraph.** 150-200 words explaining the concept and connecting it to the framework's claim about contemporaneous documentation.
- **Infrastructure subsection in A.4.** Session hubs, metadata fields, hub scripts, skeleton coverage. 200-300 words. Explain what these are and why they exist, not how to use the script.
- **Architectural decision note.** Why section drafts lack session IDs. 100-150 words. Can be a boxed note or a subsection.

### 4.4 Word targets

| Section | Target |
|---|---|
| A.1 (overview) | 300-400 words |
| A.2 (documentation record) | 800-1,000 words |
| A.3 (selected graphs) | 600-800 words |
| A.4 (document types + infrastructure) | 500-700 words |
| A.5 (materials inventory) | 600-800 words (mostly lists) |
| A.6 (navigation guide) | 400-500 words |
| **Total** | **3,200-4,200 words** |

v2 is approximately 3,500 words. v3 should be in the same range, possibly slightly longer given the additional material. Do not exceed 4,500 words.

### 4.5 Tone

- Match the paper's tone: dry philosophical prose, no hedging, no enthusiasm.
- The appendix is expository, not argumentative — but the selected graphs section is argumentative (each graph makes a claim). Keep the claims precise and understated.
- Be honest about gaps. The v1/v2 documentation is partly reconstructed. Say so plainly. Do not apologise for it or minimise it.
- Avoid meta-commentary about the documentation process being "impressive" or "thorough." Let the record speak.

### 4.6 Files the drafter must read

Before drafting, the implementing agent must read:

1. `Paper/MDversion/appendix.md` — the v2 baseline (what to revise)
2. `CFP_5.3.7_SelectedGraphCandidates.md` — the three verified graph candidates
3. `CFP_4.7.8_EpistemicTrace_SelfReferentialDocumentation.md` — the self-referential documentation story
4. `CFP_4.7.9_EpistemicTrace_SelectedGraphsVsMegagraph.md` — the megagraph vs selected graphs decision
5. `CFP_5.3.4_Note_SkeletonAndConnectionsStatus.md` — current metadata coverage and the section-draft architectural decision
6. `CFP_5.4.9_Section7_v1.md` — the three criteria (attribution, trajectory, understanding-and-endorsement) as specified in the paper
7. `CFP_4.2.19_ModificationLog_Section7.md` — example of a well-documented modlog for format reference
8. One CFP-phase hub file (e.g., `_HUBS/CHAT_SID-20260317-191544.md`) — to understand the hub structure

Additionally, the drafter should scan:
- `transparency/Canonical_MD/SP4_ProcessDocumentation/4.2_ModificationLogs/` — to verify the current list of modlogs
- `transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/` — to verify the current list of section drafts
- `transparency/Canonical_MD/SP4_ProcessDocumentation/4.7_EpistemicTraces/` — to verify the current list of epistemic traces

### 4.7 Key constraint

v3 must not claim that the documentation record is complete or fully adequate. It must distinguish between:
- The CFP phase (prospective documentation, structured metadata, session hubs) — where the record is strong
- The v1/v2 phase (retrospective reconstruction, missing SIDs, ghost nodes) — where the record is honest about its limitations

This distinction is the paper's argument in miniature. Getting it wrong would undermine the paper's credibility.

### 4.8 Relationship to the paper body

v3 should be self-contained enough that a reader encountering only the Appendix can understand the documentation architecture. But it should not re-argue the philosophical points made in Sections 5, 6, and 7. Where the Appendix makes a claim that the paper argues at length (e.g., "the three criteria for adequate transparency"), cite the section and move on. The Appendix shows; the paper argues.

---

## 5. Post-drafting steps

After v3 is drafted:

1. **Create modlog** for the Appendix revision (CFP_4.2.21 or similar).
2. **Update the work plan** (CFP_5.3.1) to reflect Appendix v3 completion.
3. **Flag for SP-2/SP-3 drafting.** The Appendix v3 is a prerequisite for rewriting SP-2 and SP-3. Those rewrites are a separate task, not part of this guidance.
4. **Update `Paper/MDversion/appendix.md`** with the v3 content once approved, or create a new canonical location for the CFP appendix draft.
