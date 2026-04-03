---
project: JPEP
document_type: Type 11 - Steering Note / Candidates List
label: CFP_5.3.7_SelectedGraphCandidates
title: "Selected Graph Candidates for Paper Figures"
date_created: 2026-04-01
session_id: SID-20260401-033111
status: draft - pending user validation
derived_from: "CFP_4.4.17_Guidance_SelectedGraphSpecifications.md"
---

# Selected Graph Candidates for Paper Figures

This file lists verified candidate subgraphs of the JPEP documentation megagraph that could serve as paper figures. Each candidate was identified by reading hub files, modification logs, section draft frontmatter, and epistemic traces, then cross-checked against the actual archive to confirm that every node exists and every stated edge appears in a real frontmatter field. Three candidates are presented in order of verification confidence; a fourth (consolidation) is noted but deferred for weaker grounding of its output node.

---

## Candidates

### Graph 1: Section 5 Production Chain

**Type:** production chain

**Claim:** A single well-documented session hub encodes attribution, trajectory, and endorsement simultaneously — establishing that these three transparency criteria can be satisfied contemporaneously with production, not only retrospectively.

**Criterion:** attribution + trajectory + understanding-and-endorsement

**Nodes:**
- `Paper/MDversion/05_signaling_discontinuity_from_prestige_system.md` — source/input (JPEP v1 draft)
- `CHAT_SID-20260317-191544` — session hub (Claude Code session, 2026-03-17)
- `CFP_5.4.7_Section5_v1.md` — output: section draft (Finalized)
- `CFP_4.2.17_ModificationLog_Section5.md` — output: modification log (9 entries, validation=approved_with_edits)

**Edges:**
- `Paper/MDversion/05_...` → `CHAT_SID-20260317-191544`: `inputs` (declared in CFP_4.2.17 frontmatter)
- `CHAT_SID-20260317-191544` → `CFP_5.4.7_Section5_v1.md`: `output_completed` (declared in CFP_4.2.17 frontmatter; also `feeds_into` in CFP_5.4.7 frontmatter)
- `CHAT_SID-20260317-191544` → `CFP_4.2.17_ModificationLog_Section5.md`: hub artifact list (CFP_4.2.17 is listed in CHAT_SID-20260317-191544.md)
- `CFP_5.4.7_Section5_v1.md` → `CFP_4.2.17_ModificationLog_Section5.md`: `feeds_into` (CFP_5.4.7 frontmatter)

**Status:** verified

**Notes:** The hub file `CHAT_SID-20260317-191544.md` lists exactly two artifacts: the modlog and the section draft. The source file `Paper/MDversion/05_signaling_discontinuity_from_prestige_system.md` exists but is excluded from the graph per the constraint on MDversion files — it can be shown as a ghost/boundary node labelled "source draft (v1)" if needed for context, or omitted entirely. Without it the graph is 3 nodes (hub + 2 outputs); with it, 4 nodes. The `inputs` edge to the source file is marked UNRESOLVED in the hub's auto-connections section, so the link is real but the resolver couldn't match it to a canonical archive path — present it as a boundary node with a dashed edge. No ghost nodes otherwise. This is the cleanest production-chain candidate in the archive.

---

### Graph 2: Section 6 Version Chain

**Type:** version chain

**Claim:** Three successive drafts of Section 6, each transforming specific philosophical problems identified in the prior round, show that intellectual trajectory in AI-assisted writing is documentable as a directed sequence — and that the record of what changed and why is as significant as the final output.

**Criterion:** trajectory

**Nodes:**
- `III_5.4.2_Section6_v3.md` — source (Stage III predecessor, pre-CFP)
- `CFP_5.4.8_Section6_v1.md` — first CFP draft (2026-03-23)
- `CFP_5.4.8_Section6_v2.md` — second CFP draft (2026-03-23)
- `CFP_5.4.8_Section6_v3.md` — third CFP draft, finalized (2026-03-23, session SID-20260323-190000)
- `CFP_4.2.18_ModificationLog_Section6.md` — modification log (13 entries, Finalized)
- `CHAT_SID-20260323-190000` — session hub (v3 and modlog produced here)

**Edges:**
- `III_5.4.2_Section6_v3.md` → `CFP_5.4.8_Section6_v1.md`: `source_file` (declared in CFP_5.4.8_Section6_v1.md frontmatter)
- `CFP_5.4.8_Section6_v1.md` → `CFP_5.4.8_Section6_v2.md`: `derived_from` (declared in CFP_5.4.8_Section6_v2.md frontmatter)
- `CFP_5.4.8_Section6_v2.md` → `CFP_5.4.8_Section6_v3.md`: `derived_from` (declared in CFP_5.4.8_Section6_v3.md frontmatter)
- `CFP_5.4.8_Section6_v3.md` → `CFP_4.2.18_ModificationLog_Section6.md`: `feeds_into` (declared in CFP_5.4.8_Section6_v3.md frontmatter; also in v1 and v2 frontmatter)
- `CHAT_SID-20260323-190000` → `CFP_5.4.8_Section6_v3.md`: hub artifact list
- `CHAT_SID-20260323-190000` → `CFP_4.2.18_ModificationLog_Section6.md`: hub artifact list

**Status:** verified

**Notes:** All six nodes exist as confirmed files. The `derived_from` chain is present in frontmatter for v2 and v3; v1 uses `source_file` rather than `derived_from` (its source is the Stage III predecessor, not a prior CFP draft). The session hub (SID-20260323-190000) is registered only to v3 and the modlog — v1 and v2 were produced in the same session but lack explicit `session_id` fields; their place in the chain is established through `derived_from` links. The modlog records 13 modification entries spanning all three versions, with reviewer comments from both Reviewer A (user) and Reviewer B (Opus). If the graph becomes crowded, `III_5.4.2_Section6_v3.md` can be shown as a boundary node, reducing to a 5-node graph.

---

### Graph 3: Contrast — Introduction Documentation Density (v1/v2 phase vs CFP phase)

**Type:** contrast

**Claim:** The same section (Introduction) has two radically different documentation records: the v1/v2 modlog is sparse (null source_chat_id, inputs as in-chat ghosts, self-referential output), while the CFP modlog is dense (session_id, named inputs, related_documents list) — illustrating that what mandates cannot produce, a specified framework enables.

**Criterion:** trajectory + attribution

**Nodes (left — v1/v2 phase):**
- `GHOST: original draft chat` — ghost node (source_chat_id: null, original chat not preserved)
- `GHOST: MOD-001 to MOD-003 state of 4.2.1` — ghost node (in-chat input to revision chat ae493f0b, not separately archived)
- `CHAT_ae493f0b` — revision chat (revision_chat_id: ae493f0b-cc8a-43b0-b32f-0fc597b297a2, 2025-10-18); no hub file exists
- `4.2.1_ModificationLog_I_Introduction__S01.md` — output (self-referential: also its own input at prior state)

**Nodes (right — CFP phase):**
- `CFP_5.4.3_Introduction_v1.md` — input and output (section draft)
- `CHAT_SID-20260303-102634` — session hub (2026-03-03)
- `CFP_4.2.14_ModificationLog_Introduction.md` — modification log (session_id, related_documents, validated)
- `CFP_4.7.5_EpistemicTrace_IntroductionArgumentativeDevelopment.md` — epistemic trace (listed in CFP_4.2.14 related_documents)

**Edges (left):**
- `GHOST: original draft chat` → `GHOST: MOD-001–003 state`: production (ghost, unarchived)
- `GHOST: MOD-001–003 state` → `CHAT_ae493f0b`: `inputs` (declared in 4.2.1 frontmatter as "pasted into revision chat")
- `CHAT_ae493f0b` → `4.2.1_ModificationLog_I_Introduction__S01.md`: `output_completed` (self-referential: output IS the input document at a later state)

**Edges (right):**
- `CFP_5.4.3_Introduction_v1.md` → `CHAT_SID-20260303-102634`: implied by session_id in CFP_5.4.3 frontmatter
- `CHAT_SID-20260303-102634` → `CFP_4.2.14_ModificationLog_Introduction.md`: hub artifact list
- `CFP_4.2.14_ModificationLog_Introduction.md` → `CFP_4.7.5_EpistemicTrace_...`: `related_documents` (declared in CFP_4.2.14 frontmatter)

**Status:** verified (ghost nodes marked as such)

**Notes:** The contrast graph has two panels side by side, sharing only the section label (Introduction) as a conceptual anchor — the documentation networks do not connect to each other as graph edges. Ghost nodes are: (1) the original draft chat (source_chat_id: null in 4.2.1 frontmatter — confirmed lost); (2) the pre-MOD-004 state of 4.2.1 (described explicitly in 4.2.1 frontmatter as "not separately archived"). The ae493f0b chat has no hub file in `_HUBS/` — it predates the hub convention. The self-referential loop on `4.2.1` should be shown as a dashed arrow from CHAT_ae493f0b back to the same node (with a label: "version-chain self-reference — output is input at prior state"). The `related_documents` edge on the right side is confirmed in CFP_4.2.14 frontmatter. The CFP_4.7.5 file exists (confirmed in the 4.7_EpistemicTraces directory). The node count is 4 per panel (8 total), within the 15-node print limit.

---

## Deferred candidate: Consolidation (Sections II–III–IV → Section 2)

**Type:** consolidation

**Why not included as primary candidate:** The input modlogs (4.2.2, 4.2.3, 4.2.4) and the pattern summary (4.3.1_Section_II_2__S02.md) all exist and are verified. The session hub (CHAT_ffea5b8a) does not have a hub file in `_HUBS/` — the source_chat_id `ffea5b8a-9c81-46c9-bb3c-8138d45c8eec` from 4.2.5 frontmatter has no corresponding `CHAT_ffea5b8a.md`. The output `Paper/MDversion/02_systemic_barriers_to_disclosure.md` exists but is a Paper/MDversion file (excluded per constraints). This makes the consolidation graph harder to draw cleanly within the constraint of no MDversion nodes and verified hub links.

**Recommendation:** Can be reconsidered if the paper needs a structural-transformation example. The graph would show: `4.2.2` + `4.2.3` + `4.2.4` → `4.2.5` (three modlogs feeding a consolidation modlog), with the output as a boundary node. The claim would be: "Transparency documentation must track structural transformation, not only linear revision — three section histories collapse into one."

---

## Search notes

**What was searched:**
- All 53 hub files in `_HUBS/` (Glob)
- All 6 CFP modlogs (`CFP_4.2.14` through `CFP_4.2.19`)
- All v1/v2 modlogs in scope (`4.2.1`, `4.2.2`, `4.2.3`, `4.2.5`)
- All CFP section drafts in `5.4_SectionDrafts/` (10 files)
- PDLs in `5.2_SectionPromptDevelopmentLogs_Type8b/` (11 files)
- Epistemic traces `CFP_4.7.8` and `CFP_4.7.9`
- Work plan `CFP_5.3.1`

**What was found:**
- Section 5 is the clearest single production-chain candidate: 1 hub, 2 outputs, 1 source, all fields present.
- Section 6 is the clearest version-chain candidate: 3 CFP drafts with `derived_from` links, 1 finalized hub, 1 modlog with 13 entries.
- The Introduction contrast pair is philosophically the richest candidate: it shows exactly what the paper argues about retrospective vs contemporaneous documentation, with real documented gaps (null source_chat_id, ghost intermediate states, AI hallucination of dates in body text).
- No CFP-phase PDL exists for Section 5 — the PDL for "Section VII" (5.2.2) is a v1/v2-phase artifact from October 2025. This means the Section 5 production chain does not have a PDL node, which is not a gap but a limit of the graph type.
- Hub files for v1/v2-phase chats are largely absent (predates the hub convention) — this is structurally significant for the contrast graph.

**Patterns worth flagging:**
- The CFP phase (Section 5, 6, Introduction) has substantially richer hub and modlog structure than the v1/v2 phase. This is not incidental — it reflects the availability of MHC-W infrastructure and SID conventions, which is precisely the paper's argument.
- The `feeds_into` / `derived_from` / `output_completed` field vocabulary is consistent across CFP-phase files but inconsistent across v1/v2-phase files. Graph construction will need to normalize edge labels.
- Ghost nodes are more common on the left side of any contrast graph than on the right side — this asymmetry is itself the argument.
