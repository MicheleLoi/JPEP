---
project: JPEP
document_type: Type 11 - Note
label: CFP_5.3.19_Note_SP3_FigureDataSpecs
title: "SP-3 Figure Data Specifications (consolidated)"
date: 2026-04-07
session_id: SID-20260407-181422
source_conversation: SID-20260407-181422
status: Draft
related:
  - "CFP_4.4.20_SectionGuidance_SP3.md (v7)"
  - "CFP_4.7.20_EpistemicTrace_Section6History.md"
  - "CFP_5.2.4_pdl_SP1_SP2_SP3.md (PDL-024)"
  - "CFP_5.3.7_SelectedGraphCandidates.md"
feeds_into:
  - "SP-3 figure rendering (refine pass after first SP-3 draft)"
purpose: "Consolidated layout / label / data-source specifications for the six SP-3 figures called out by CFP_4.4.20 v7. Authoritative source the AI reads when drafting figures in the refine pass. Keeping figure detail here (not in section guidance) is the PDL-024 separation: guidance owns the story, this note owns the rendering."
---

# SP-3 Figure Data Specifications

This note collects layout, labels, node lists, and data sources for the six figures called out in CFP_4.4.20 v7. The guidance document specifies *what each figure must show*; this note specifies *how to render it*. Section 6 data is sourced from CFP_4.7.20 (full Section 6 history trace).

Convention: figures are referenced by the short names used in CFP_4.4.20 v7.

---

## Figure 1 — Section 6 across six months (timeline)

**Purpose (from guidance):** Give the reader a single visual anchor for the Section 6 throughline. Five stages, two platforms, four model identities, ~5.5 months.

**Type:** Horizontal timeline with stage bands.

**X-axis:** Time, 2025-10-01 → 2026-04-07.

**Tracks (top to bottom):**
1. *Platform band* — two colors. Claude.ai web (2025-10-15 → 2025-11-06). Claude Code (2026-01-26 → 2026-04-01).
2. *Model band* — four colors keyed to identity: Sonnet 4.5, Opus 4.5, Sonnet 4.6, Opus 4.6.
3. *Stage markers* — five labeled markers (Stage 1 … Stage 5).
4. *Renumbering event* — single vertical tick during Nov 2025 labelled "Section VIII → Section 6".
5. *Lost-content marker* — single hollow circle on 2026-01-28 labelled "Jan 28 draft (no commit, no export)". Visually understated, NOT featured.

**Stage marker data (from CFP_4.7.20):**

| # | Date | Label | Platform | Model |
|---|---|---|---|---|
| 1 | 2025-10-15 | First writing as Section VIII | Claude.ai web | Sonnet 4.5 |
| 2 | 2025-11-05/06 | Appendix → §6.2 feedback loop | Claude.ai web | Sonnet 4.5 |
| 3 | 2026-01-26 → 2026-03-02 | meaningful human control integration | Claude Code | Opus 4.5 → Sonnet 4.6 |
| 4 | 2026-03-23 | Three-draft session (v1→v2→v3) | Claude Code | Sonnet 4.6 |
| 5 | 2026-04-01 | Redundancy pass (v4.1) | Claude Code | Opus 4.6 |

**Color suggestion:** Platforms = neutral grays (light/dark). Models = qualitative palette (4 hues). Lost-content marker = same hue as its model band but unfilled.

**Required labels in caption:** total span 5.5 months; 2 platforms; 4 model identities; 1 renumbering; 1 ghost.

---

## Figure 2 — The feedback loop

**Purpose (from guidance):** Make the §6.2 ↔ Appendix A.2 recursion legible. The strongest single piece of evidence that the documentation framework is recursive. Three artifacts must be visible as nodes the reader can resolve: 4.4.13, 4.2.11, 4.2.9 MOD-009.

**Type:** Small directed graph, ~6 nodes.

**Nodes:**
1. *Section VIII (writing in progress)* — chat `aac1629a-ffa5-42c9-b313-859d849097c9` "JPEP epistemic trace temporal logging", 2025-11-05
2. *Appendix A.2 drafting* — same chat
3. *Infrastructure constraint observed* — discovery event during appendix work
4. *4.4.13 bridging guidance* — `4.4.13_From_Full_Draft_(+Appendix)_to_Section_6__S06.md`
5. *Revision chat* — `65a571f1-5ce8-4d28-be15-a5ad85e64d8a` "JPEP AI transparency framework infrastructure constraints", 2025-11-06
6. *§6.2 modified + 4.2.9 MOD-009* — `phase2_insertion_mode: manual_copy_paste`

**Edges:**
- 1 → 2 (writing produces appendix)
- 2 → 3 (appendix work surfaces constraint)
- 3 → 4 (constraint codified as bridging guidance 4.4.13)
- 4 → 5 (guidance feeds revision chat)
- 5 → 6 (revision modifies §6.2 — the loop closes)
- 6 → 1 (back-arrow, dashed, labelled "the section about transparency was modified by the act of documenting transparency")

**Required label:** the back-arrow is the figure's whole point — make it visually heavier than the forward arrows.

**Caption must reference:** 4.7.7.4 epistemic trace as the cross-reference for this loop.

---

## Figure 3 — Two architectures, one section (diptych)

**Purpose (from guidance):** Contrast the v1/v2 documentation system with the CFP-era system *on the same section*, so the reader sees what changed in *capability* between Stage 1 and Stage 4. The novelty being illustrated is the artifact-system maturation, not the AI capability.

**Type:** Side-by-side panels. Same Section 6, two regimes.

**Left panel — Stage 1 (2025-10-15, Claude.ai web, Sonnet 4.5):**
- Artifacts present (nodes): 4.1 Complete Prompt; 4.4.4 (Section VIII guidance); 4.4.5 (composite guidance with sideways-chat correction); 4.7.1, 4.7.2, 4.7.3 (preliminary chats); 4.2.9 (Phase 1 modlog); 4.3.5 (pattern summary)
- Artifact-system features visible: parallel prompt steering; mid-course correction injected from sideways chat e9d55db6 ("JPEP 4.7.5 value of transparency", 2025-10-18); manually authored modlog
- Notable absences: no session ID; no derived_from chain; no PDL; no automated frontmatter

**Right panel — Stage 4 (2026-03-23, Claude Code, Sonnet 4.6, SID-20260323-190000):**
- Artifacts present (nodes): CFP_5.3.1 work plan; III_5.4.2_v3 (input draft); CFP_5.4.8 v1; CFP_5.4.8 v2; CFP_5.4.8 v3; CFP_4.2.18 modlog (13 entries); both reviewers (A=user, B=Opus 4.6)
- Artifact-system features visible: SID; `derived_from` chain v1→v2→v3; per-version word count; reviewer attribution; finalized modlog
- Same custom artifact types operating: section_guidance, section_draft, pattern_summary

**Layout:** Two boxed columns. Same section header at top of both. Each artifact is a small labelled rectangle. Lines between artifacts show flow.

**Caption must say:** "Same section. Same author. Different documentation infrastructure." The diff is the artifact ontology, not the model.

---

## Figure 4 — The three-draft session (Stage 4 detail)

**Purpose (from guidance):** Make the cleanest documented version chain visible end-to-end inside a single session. Exercises Section 7 trajectory + understanding-and-endorsement criteria simultaneously.

**Type:** Vertical chain with side annotations.

**Nodes (top to bottom):**
1. *Inputs* — `III_5.4.2_Section6_v3.md` + `CFP_5.3.1_WorkPlan_CFP_Adaptation.md`
2. *CFP_5.4.8_Section6_v1.md* (~1550 words) — minor reframe: venue/journal → research practice/community; principles → conditions; virtue dimension §6.1; adverse-selection §6.3
3. *CFP_5.4.8_Section6_v2.md* (~1600 words) — `derived_from: v1`. §6.1 reorder; discovery/justification cut; "we do not" paragraphs removed; traditional-values reframed
4. *CFP_5.4.8_Section6_v3.md* (~1520 words) — `derived_from: v2`. §6.2 SP-3 paragraph rewritten; §6.4 architectural rewrite (raw transcript + SP-3 synthesis); timestamp claim removed
5. *CFP_4.2.18_ModificationLog_Section6.md* — 13 entries, finalized

**Side annotations (right of each transition):**
- v1→v2: "Reviewer A verdict: cut discovery/justification paragraph" + "Reviewer B REVISE instructions" + "multi-round philosophical revision"
- v2→v3: "§6.2 stated positively" + "§6.4 reframed as two-layer architecture"

**Side annotation (left of chain):** "All three drafts in one session: SID-20260323-190000. Sonnet 4.6. ~6 hours." (Whatever the session duration was — read from session_topology.yaml at draft time.)

**Required labels:** word counts on each draft node; `derived_from` arrows must be visually distinct from input arrows.

---

## Figure 5 — Failure and visible decision (Stage 3 detail)

**Purpose (from guidance):** Show one human-judgment moment with full provenance, including the *one ghost* in the entire Section 6 trace. The ghost is treated as a clean limit case, not the headline.

**Type:** Small horizontal flow, three nodes + one ghost.

**Nodes (left to right):**
1. *2026-01-26 — Initial guidance* — `III_4.4.5_SectionGuidance_Section6_MHC.md` v1 (target 1200–1500 words)
2. *2026-01-28 — Failed draft* — Claude Code, Opus 4.5. Rendered as a hollow / dashed-outline node. Annotation: "no git commit · no export · overwritten · irrecoverable. Known only from III_4.2.13 Entry 1 and the guidance revision timestamp."
3. *2026-01-28 — Guidance revised* — same `III_4.4.5`, hard constraints added: *"Existing Section 6 reading now MANDATORY"*
4. *2026-03-02 — Successful redraft* — `III_5.4.2_Section6_v3.md` (~1400 words), session SID-20260302-152952, Sonnet 4.6. Annotation on the arrow from node 3 → node 4: "**model switch: Opus 4.5 → Sonnet 4.6**"

**Below node 4, branching arrow:**
5. *Same session: III_4.7.3_MHC_Tracing_SP_Reconception.md — methodology of the entire paper reorganized inside this redraft session*

**Caption requirement:** Frame the ghost as "the one place the record falls short, scoped and acknowledged" — not as the figure's subject. The figure's subject is the *visible* decision (the model switch) and the *visible* consequence (the SP reconception).

---

## Figure 6 — Where Section 6 sits in the project (synthesis)

**Purpose (from guidance):** Closing figure. Place the Section 6 throughline back inside the whole paper so the reader sees that the illustrative example was not the only thing happening. Signal: "the other sections are not abandoned; we chose Section 6 because it exercises all three Section 7 criteria at once."

**Type:** Project-wide bird's-eye view with Section 6 highlighted.

**Layout option A (preferred):** Horizontal swimlanes — one lane per paper section (1 through 7). Each lane shows that section's drafting events as small markers across the same time axis as Figure 1. Section 6's lane is highlighted (color or thicker line); the others are present but desaturated.

**Layout option B (fallback):** Stacked bar of artifact counts per section, with Section 6 highlighted, plus a small inset replicating Figure 1's stage markers.

**Data source:** session_topology.yaml + CFP_4.2.* modlogs for the per-section event counts. Section 6 row data comes from CFP_4.7.20.

**Required labels in caption:**
- "Section 6 was chosen because it exercises all three Section 7 adequacy criteria simultaneously."
- "Other sections have their own histories; this paper traces one to keep the demonstration legible."
- The number of sections that have full modlog coverage, so the reader sees Section 6 is representative, not exceptional.

---

## Cross-figure conventions

- **Color discipline:** reuse the same model palette (Sonnet 4.5 / Opus 4.5 / Sonnet 4.6 / Opus 4.6) across Figures 1, 3, 4, 5. Reuse the same platform palette (Claude.ai web / Claude Code) wherever both appear.
- **Artifact label format:** when an artifact is a node, label it with its short ID (e.g. `4.2.9 MOD-009`, `CFP_5.4.8 v2`) so the reader can resolve it in SP-4/SP-5.
- **Citation in captions:** every figure caption ends with the artifact IDs that the reader can open to verify the figure (this is the "make the reader use the documentation" principle from PDL-024).
- **No abstract concept nodes.** Nodes are either artifacts (with IDs) or events (with dates). No "Documentation System" boxes, no "Transparency" clouds. This is the lesson from the deleted v1 visuals.
- **Ghost treatment:** the Jan 28 lost draft appears in exactly two places (Figure 1 marker, Figure 5 hollow node) and nowhere else. It is not the headline of any figure.

---

## What this note does NOT contain

- Story / argument structure → that lives in CFP_4.4.20 v7
- Why Section 6 was chosen → that lives in CFP_4.7.20 (and is summarized in v7)
- Reader background paragraph → drafted in SP-3 prose, not here
- Color hex codes / font sizes → deferred to figure-rendering session

---

*Companion note to CFP_4.4.20 v7. Read by the AI when drafting figures in the refine pass per PDL-024.*
