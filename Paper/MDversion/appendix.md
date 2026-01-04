---
source_chat_name: "JPEP Appendix writing draft 1"
source_chat_id: "89db4632-4f5b-4729-8838-d526d166c44d"
---
# Appendix: Documentation Structure and Reproduction Procedure

Numbering convention used throughout:

*Old/process numbering = Roman numerals (I, II, III, …).*

*New/final article numbering = Arabic numerals (1, 2, 3, …).*

## Table of Contents

- [A.1 Overview of Reproduction Procedure](#_A.1_Overview_of)

- [A.2 Document Creation Flow and Relationships](#a.2-document-creation-flow-and-relationships)

- [A.3 The Eleven Document Types](#a.3-the-eleven-document-types)

- [A.4 This Article's Supplementary Materials](#a.4-this-articles-supplementary-materials)

- [A.5 Guide to Using Supplementary Materials](#a.5-guide-to-using-supplementary-materials)<span id="_A.1_Overview_of" class="anchor"></span>

## A.1 Overview of Reproduction Procedure

Reviewer B receives three core documents enabling reproduction assessment:

**• SP-1: Complete Prompt (~20 pages) —** synthesized instruction document containing full argument architecture, section specifications, tone requirements, and reference guidance. This served as the constant primary input throughout old §§ I–VI and VIII.

**• SP-2: Reproduction Package (~15–20 pages) —** processed compilation generated from all process documentation (Types 1–8), organized into six sections: Architectural Overview, Guidance Patterns Across Sections, Refinement Patterns, Source Integration Approach, Development Flow, and Key Insights Checklist.

**• SP-3: Reproduction Guide (~5 pages) —** instructions for combining SP-1 and SP-2, comparison criteria, and pass threshold.

**Basic workflow.** Begin with SP-3 to understand the procedure, then load SP-1 (Complete Prompt) as primary input to the LLM. Use SP-2 for section-by-section guidance (patterns and insights), generate comparable work following the procedure, and finally compare reproduction to the submitted article using trajectory-matching criteria.

**Indicative time envelope.** 2–3 hours reviewing materials, 2–4 hours conducting reproduction, and 1–2 hours for comparison and assessment (≈5–9 hours total). Additional time may be warranted if results suggest deeper investigation of SP-4 (process documentation) or SP-5 (development records).

SP-3 specifies how to combine SP-1 and SP-2, explains comparison criteria (trajectory matching rather than output matching), and sets the pass threshold: documented inputs must be sufficient to generate work of this character, with gaps attributable to expected editorial refinement rather than missing documentation.

## A.2 Document Creation Flow and Relationships

Figure 2 (below) maps the complete document creation flow across six developmental phases. The diagram's complexity reflects the actual non-linear writing process, including parallel development paths, branching decision points, and emergent documentation practices. The following analysis explains the article's developmental origins, identifies key patterns in the process, and provides navigation guidance for interpreting the diagram.

### How This Article Began

The article originated from a conversation documented in Epistemic Trace 1 (SP4.7.1) about creating a journal for AI-assisted scholarship as an operational project—potential board members, strategic positioning, practical implementation details. These specifics required redaction from the published documentation.

The long discussion established sufficient material for a philosophical article. The conversation about creating a journal became the foundation for arguing why such a journal should exist. Epistemic traces document conversations where contribution framing gets determined. The redacted conversation established what the article needed to argue and how, which explains its presence in the documentation—not as raw process display, but as generative source for subsequent work.

### Documentation at Multiple Levels

The writing process involved two documentation types emerging at different developmental stages.

Modification logs tracked section evolution during writing. These began with the initial sections in Phase II (Sections I-VI) and continued throughout the process.

Prompt development logs appeared in Phase III when the writing process became more complex. Some section prompts were brief; others incorporated substantial material and were produced following section completion. The logs tracked how writing instructions themselves were constructed.

As AI-assisted writing becomes multi-stage—using AI systems to generate prompts, with conversations informing guidance development—documentation at multiple levels becomes necessary. Section development documentation shows what changed during writing. Prompt development documentation shows how writing instructions were constructed.

A complication arose: the documentation system itself could not be fully planned in advance. The ontology emerged through writing experience. After conversation 4.7.3, formal terminology crystallized (epistemic traces, modification logs, pattern summaries, section guidance, prompt development logs). However, ongoing adjustments occurred regarding how to track conversations that influenced section guidance or were incorporated into writing prompts. Once the system became clear, earlier materials required reorganization for reader accessibility.

This meta-level aspect—documenting the documentation system's emergence—proves difficult to represent without complexity. The diagram shows the result rather than all developmental oscillations.

### Three Patterns in the Development Process

#### Pattern 1: Tangential Conversations Becoming Foundational

Following Section VI, a conversation with ChatGPT addressed presenting the article on LinkedIn: anticipated stakeholder reactions in the author's network, who would find the approach problematic, who would express interest.

The conversation shifted to what different reader types would need from methodology documentation. What makes transparency credible to skeptics versus accessible to supporters? How to balance completeness with usability?

These insights about stakeholder expectations became Epistemic Trace SP4.7.2. What began as presentation strategy generated understanding about documentation design.

This pattern—conversations beginning with one purpose generating insights valuable for another—occurred twice. First, the journal strategy conversation becoming article foundation (SP4.7.1). Second, the LinkedIn discussion becoming stakeholder analysis (SP4.7.2).

#### Pattern 2: Self-Recursion in Documentation Development

A recurring pattern involved using conversations as subject matter when developing the documentation system itself.

When establishing the artifact ontology—what document types should exist, how they should relate—conversations about documentation became material for analyzing documentation. The conversation from October 15 (documented in 4.7.5) was later used (October 18-19) as subject matter for analyzing whether the artifact ontology adequately covered all interaction types. The conversation functioned as both generative source and analytical object.

This self-referential pattern appeared throughout documentation development. Testing proposed ontologies required examining actual conversations, which revealed gaps or ambiguities, which led to ontology refinements, which then required testing against conversations. The documentation system developed through examining its own materials.

#### Pattern 3: Branching When Different Work Types Require Different Approaches

Conversation SP4.7.3 (October 12-13) synthesized the Complete Prompt, both epistemic traces, accumulated pattern summaries and modification logs, while addressing a new question: what documentation material types should exist and how should they be organized?

This conversation created two parallel development paths.

Path A continued artifact ontology work directly. The conversation documented in 4.7.4 refined the four-tier document structure, established naming conventions, and clarified required versus optional materials. This produced Section VIII guidance (4.4.4) focused on structural framework and Review Mechanism design.

Path B proceeded through Section VII's development. Section VII required guidance about discontinuity and design principles. Developing that guidance (SP5.2.2) identified three design principles: ecological validity, good faith orientation, and cost structure as costly signaling. Section VII was written using that guidance.

Writing Section VII produced the complete section plus the initial ideas of section to be later moved in Section VIII. These became inputs for conversation 4.7.5, which developed philosophical grounding for transparency requirements: traditional values in philosophical writing, what opacity destroys, why attribution matters. This produced Section VIII guidance (4.4.5) about philosophical values and disclosure components.

Thus, section VIII received two separate guidance artifacts from two independent development paths: structural framework for documentation from Path A, philosophical grounding from Path B.

The branching occurred because structural thinking (artifact ontology) and philosophical thinking (traditional values) developed along different trajectories. Forcing sequential development would have constrained both approaches. The two paths converged in Section VIII because that section required both types of grounding.

### Documentation Approach Rationale

A linear reconstruction—"first X, then Y, then Z"—would have been easier to follow. However, AI-assisted writing involves multiple stages: prompts generating prompts, conversations informing guidance development, documentation systems emerging through use rather than advance planning. Recording what actually occurred requires capturing these multiple levels.

The branching at 4.7.3 demonstrates that different work types (structural framework versus philosophical grounding) developed in parallel because sequential development would have imposed artificial constraints. The tangential conversations (journal strategy becoming article foundation, LinkedIn discussion generating stakeholder insights) demonstrate that generative thinking does not follow predetermined paths. The self-recursion (using conversations as subject matter for documentation development) demonstrates that the documentation system itself evolved through examining its own materials.

This documentation approach does not assume linearity or complete advance planning. This enables capturing what actually occurred, including the documentation system's own emergence.

## Important: The Eventual Renumbering

All process artifacts (Modification Logs, Pattern Summaries, Section Guidance records) use the old section numbers from the writing process. The final article underwent radical renumbering after consolidation:

### Writing Process (old) → Final Article (new)

| Old | New |
|----|----|
| Introduction (I) | 1 (unchanged) |
| Incentives Analysis (II) + Why Contiguous Approaches Fail (III) + The Problem of Unfair Reviews (IV) | 2 (consolidated) |
| Why Engage (V) | 3 |
| Dilemma Reconsidered (VI) | 4 |
| Discontinuity (VII) | 5 |
| Mandatory Transparency (VIII) | 6 |
| Review Mechanism (IX) | 7 |

Throughout this Appendix, both numbers appear where needed: e.g., "Section V (new 3)" helps readers navigate between process artifacts (old) and the final article (new).
[fig 2]
<figure>
<img src="media/image3.svg" style="width:6.27014in;height:9.01111in" />
<figcaption><p>. Writing Flow and Input-Output Relations.</p></figcaption>
</figure>

### How to Navigate the Diagram

The diagram organizes content by writing phases (major horizontal sections). Navigation focuses on key paths rather than every connection:

**Phase 1 - Foundation and Setup** Establishes foundational methods through original conversations (SP4.7.1) and complete prompt development (SP5.1), leading to 4.1. These primary artifacts set the conceptual framework and methodological approach for the entire writing process.

**Phase 2 - Main Writing Sequence (Sections I-VI)** Systematic development of core sections using feed-forward methodology. Each section builds on previous work through three mechanisms: pattern summaries extracting insights from completed sections, modification logs tracking evolving understanding, and section-specific guidance documents incorporating accumulated knowledge. Creates cumulative understanding through methodical progression.

**Phase 3 - Further Brainstorming and Parallel Development** SP4.7.3 serves as critical branching point, spawning two independent development streams: artifact consolidation path developing structural frameworks and review mechanisms (SP4.7.4 → SP4.4.4), and philosophical development path proceeding through Section VII toward values and theoretical grounding (SP4.7.5 → SP4.4.5). Prompt Development Logs emerge as documentary practice becomes more sophisticated. Both paths advance simultaneously, developing complementary dimensions.

**Phase 4 - Later Writing (Sections VII-IX)** Section VII develops with guidance from brainstorming phase. Section VIII becomes convergence point, integrating structural framework from artifact consolidation path and philosophical grounding from values development path. Section IX provides conclusion based on accumulated development. Represents synthesis of parallel streams into unified narrative.

**Phase 5 - Editorial Revision and Appendix Development** Post-writing discoveries generate new distinctions and frameworks. Appendices capture supplementary materials including trajectory claims and ontological frameworks, coherence tests and verification processes, and late-emerging insights that enhance without restructuring the main argument. Final editorial work ensures document coherence and completeness. The final text of this section of the Appendix (A2) is compared with the graph of Fig.2 to assess coherence and produce a last rewriting.

**Phase 6 - Final Touches** A few final reads are sufficient to detect and eliminate redundant paragraphs, typical of AI slop. A tone discrepancy between section A2 of the Appendix (this very section) and the rest of the paper is detected and addressed. A few sentences are manually inserted; a few other sentences are added.

## A.3 The Eleven Document Types

(Records appear inside the consolidated Word documents. Labels below are record labels, not standalone files.)

### Writing Phase Types (Foundation & Execution)

#### Type 1: Complete Prompt

Created before writing begins (result of Type 8). Foundational instructions for generating the article; ~20 pages (problem framing, incentive analysis, solution architecture, dual-reviewer mechanism, tone, references, structure).

Played a constant primary role in forward writing throughout old §§ I–VI and VIII; temporarily absent for old § VII (new 5).

*Record label:* **CompletePrompt**

#### Type 2: Epistemic Trace

Asynchronous, one-to-many influence documents (verbatim/near-verbatim exploratory dialogues). Supply frameworks, voice calibration, and cross-section strategy.

*Record label pattern:* **EpistemicTrace_TopicDescriptor** or **PreliminaryChat_SectionX\_**

#### Type 3: Section Guidance

Created before each section (after a preliminary chat or end-of-previous-section request). Section-specific instructions (structure deviations, continuity, links, methods, length, tone).

*Record label pattern:* **SectionGuidance_SectionX**

#### Type 4: Pattern Summary

Post-section distillation from Modification Logs. Only generalizable modifications become patterns (e.g., attribution precision, redundancy control, epistemic humility).

*Record label pattern:* **PatternSummary_SectionX**

#### Type 5: Section Summary

Post-section synopsis (argument, structure, key concepts, connections) used for continuity.

*Record label pattern:* **SectionSummary_SectionX**

#### Type 6: Reference Log

Post-section citation tracking when new sources are added (usage, relation to earlier sources, quality).

*Record label pattern:* **ReferenceLog_SectionX**

#### Type 7: Modification Log

Recorded during writing; documents changes and rationales (from formatting fixes to conceptual restructures to direct user corrections). Numbering restarts at MOD-001 per section. Not forward input (except via Type 4). Can be forwarded to later conversations as material for (self-)observation.

*Record label pattern:* **ModificationLog_SectionX**

### Pre-Writing Phase Type

#### Type 8: Prompt Development Log

Structured decision tracking (PDL-XXX) showing how Epistemic Traces (Type 2) become guidance (Type 1 or Type 3).

• 8a: Complete Prompt development (project-level).

*Record label:* **PromptDevelopmentLog**

• 8b: Section Guidance development (section-level).

*Record label pattern:* **PromptDevelopmentLog_SectionX**

**Key rule.** If it tracks decisions that culminate in guidance (PDL-XXX), it's Type 8. If it's exploratory dialogue, it's Type 2.

### Post-Writing Phase Types

#### Type 9: Reproduction Package

Processed, curated compilation enabling reproduction (becomes SP-2). Six sections: Architectural Overview; Guidance Patterns Across Sections; Refinement Patterns; Source Integration Approach; Development Flow; Key Insights Checklist.

#### Type 10: Reproduction Guide

Instructions for combining SP-1 and SP-2, comparison criteria, pass threshold, time estimates, and when to consult deeper documentation (becomes SP-3).

### Utility Type

#### Type 11: Notes

Working documents (citation checks, renaming, organizational decisions). Not methodologically central; not forward inputs (but can be used as summaries when efficient).

### Summary Table

| Type | Name | Forward Writing | Documentation | Phase |
|----|----|----|----|----|
| 1 | Complete Prompt | Yes (constant) | Yes | Writing (foundation) |
| 2 | Epistemic Trace | Yes (voice) | Yes | Asynchronous |
| 3 | Section Guidance | Yes (per-section) | Yes | Writing |
| 4 | Pattern Summary | Yes (accum.) | Yes | Writing |
| 5 | Section Summary | Yes (accum.) | Yes | Writing |
| 6 | Reference Log | Yes (accum.) | Yes | Writing |
| 7 | Modification Log | No (retro) | Yes | Writing |
| 8 | Prompt Development Log | No | Yes | Pre-/Between sections |
| 9 | Reproduction Package | No | Yes | Post-Writing |
| 10 | Reproduction Guide | No | Yes | Post-Writing |
| 11 | Notes | No | No | Throughout |

## A.4 This Article's Supplementary Materials

All supplementary materials are available at: `https://github.com/MicheleLoi/JPEP/tree/main/transparency`

### Section Numbering Reference Table

To navigate between supplementary materials (which use old numbering from the writing process) and the final article:

| Process Artifacts (old) | Final Article (new)                   |
|-------------------------|---------------------------------------|
| § I                     | § 1: Introduction                     |
| §§ II + III + IV        | § 2: Systemic Barriers (consolidated) |
| § V                     | § 3: Why Engage                       |
| § VI                    | § 4: Dilemma Reconsidered             |
| § VII                   | § 5: Discontinuity                    |
| § VIII                  | § 6: Mandatory Transparency           |
| § IX                    | § 7: Review Mechanism                 |

All process documentation preserves original section numbers. This reflects the ecological validity principle—documentation shows actual process rather than retrospective reconstruction. Use this table when connecting process artifacts to final sections.

### The Five Supplementary Packages

#### SP-1: Complete Prompt (Type 1)

**Location:** `SP1_CompletePrompt/`

~20 pages containing the final synthesized prompt. Contents include: full argument structure (eleven original sections), the "laundering" barrier analysis, incentive gradient examination, the dual solution (discontinuity + mandatory transparency), dual-reviewer mechanism design, tone requirements (dry philosophical prose), and annotated references with relevance assessments.

Used as constant input throughout old §§ I–VI and VIII; temporarily absent for old § VII (new 5). Reviewer B loads this as the primary input when reproducing.

#### SP-2: Reproduction Package (Type 9)

~15–20 pages synthesized from SP-4 materials via preprocessing. Six sections: Architectural Overview, Guidance Patterns Across Sections, Refinement Patterns, Source Integration Approach, Development Flow, and Key Insights Checklist.

[Note: Optimal preprocessing recipe documented in development records; preliminary tests logged as SP5.2.6, with artifacts SP5.3.3–5.]

#### SP-3: Reproduction Guide (Type 10)

~5 pages explaining: how to combine SP-1 and SP-2 for reproduction, trajectory matching criteria (not output matching), pass threshold specification (sufficiency with expected refinement gap), time estimates (≈5–9 hours total), and guidance on when to consult deeper documentation.

#### SP-4: Process Documentation

**Location:** `SP4_ProcessDocumentation/`

All Type 1–7 materials, organized into seven parts (~35–55 pages consolidated):

**Part 1: Complete Prompt (Type 1)**

- `4.1_Complete_Prompt.md` — same content as SP-1 (see `SP1_CompletePrompt/`), included here for completeness of process record.

**Part 2: Modification Logs (Type 7)**

Located in `4.2_ModificationLogs/`

- `4.2.1_ModificationLog_I_Introduction__S01.md` — Introduction (unchanged in renumbering)
- `4.2.2_ModificationLog_Section_II__S02.md` — Incentives Analysis (now part of § 2)
- `4.2.3_ModificationLog_Section_III__S02.md` — Contiguous Approaches (now part of § 2)
- `4.2.4_ModificationLog_Section_IV__S02.md` — Unfair Reviews (now part of § 2)
- `4.2.5_ModificationLog_Section_II-III-IV_Consolidation__S02.md` — documents the three-section merger
- `4.2.6_ModificationLog_Section_V_3__S03.md` — Why Engage (now § 3); contains 13 modification entries
- `4.2.7_ModificationLog_Section_VI_4__S04.md` — Dilemma Reconsidered (now § 4)
- `4.2.8_ModificationLog_Section_VII_5__S05.md` — Discontinuity (now § 5)
- `4.2.9_ModificationLog_Section_VIII_6__S06.md` — Mandatory Transparency (now § 6)
- `4.2.10_ModificationLog_Section_IX_7__S07.md` — Review Mechanism (now § 7)
- `4.2.11_ModificationLog_Appendix.md`
- `4.2.12_ModificationLog_Title_and_Abstract.md`

Documentation only—not used in forward writing but essential for showing iterative development and user corrections.

**Part 3: Pattern Summaries (Type 4)**

Located in `4.3_PatternSummaries/`

- `4.3.1_Section_II_2__S02.md`
- `4.3.2_Sections_II-III_later_consolidated_into_2__S02.md`
- `4.3.3_Section_IV_later_consolidated_into_2__S02.md`
- `4.3.4_Section_V_now_3__S03.md`
- `4.3.5_Section_VIII_now_6__S06.md`

Used in forward writing as accumulating resource. Extracted from Modification Logs to identify generalizable lessons (epistemic humility for a priori claims, anti-redundancy approaches, attribution precision).

**Part 4: Section Guidance (Type 3)**

Located in `4.4_SectionGuidance/`

- `4.4.1_For_Section_IV_S02.md`
- `4.4.2_For_Section_VI_S03.md` — guidance for old § V (now § 3) and old § VI (now § 4)
- `4.4.3_For_Section_VII_now_5_from_SP5.2.2__S05.md`
- `4.4.4_For_Section_VIII-A_now_6_from_5.2.1__S06.md` — structural framework from artifact consolidation path
- `4.4.5_For_Section_VIII-B_from_Sideway_chat.md` — philosophical grounding from values development path
- `4.4.6_For_Section_IX_now_7_S7.md`
- `4.4.7_For_Conclusion.md`
- `4.4.8_Section_6_Revision_Guidance__S06.md`
- `4.4.9_Section_Guidance_Consolidate_Section_2_Systemic_Barriers__S02.md`
- `4.4.10_Section_Guidance_Introduction_tone_changes_and_Section_IV__S01-02.md`
- `4.4.11_Trajectory_Claims_Check_full_paper_analysis.md`
- `4.4.12_From_Draft_1_Appendix_to_Appendix_A.md`
- `4.4.13_From_Full_Draft_Appendix_to_Section_6__S06.md`

Created either via preliminary chat sessions or at end of previous section. Used in forward writing and documentation of section connections.

**Part 5: Section Summaries (Type 5)**

Located in `4.5_SectionSummaries/`

- `4.5.1_SectionSummary_Introduction__S01.md`
- `4.5.2_SectionSummary_Section_II__S02.md`
- `4.5.3_SectionSummary_Section_III__S02.md`
- `4.5.4_SectionSummary_Section_IV__S02.md`
- `4.5.5_SectionSummary_Section_V__S03.md`
- `4.5.6_SectionSummary_Section_VI__S04.md`
- `4.5.7_SectionSummary_Section_VIII__S06.md`
- `4.5.8_SectionSummary_Section_IX__S07.md`
- `4.5.9_SectionSummary_Conclusion__S10.md`

Used in forward writing to maintain continuity and document argument flow.

**Part 6: Reference Logs (Type 6)**

Located in `4.6_ReferenceLogs/`

- `citations-complete.md`
- `paper_bibliography.md`
- `references_doc.md`
- `references-master-list.md`
- `section5_refs.md`

Used in forward writing to avoid redundancy and track source engagement.

**Part 7: Epistemic Traces (Type 2)**

Located in `4.7_EpistemicTraces/`

Foundational documents characterized by one-to-many influence—created asynchronously to linear section writing and shaping multiple downstream outputs.

- `4.7.1_OriginalTextConversationExtract_Redacted.md` — article's generative origin (redacted for privacy)
- `4.7.2_OriginalTextConversation_VisibilityAndStakeholders.md` — stakeholder expectations analysis
- `4.7.3_PreliminaryChat_1.md` — critical branching point spawning parallel development paths
- `4.7.4_PreliminaryChat_2.md` — artifact consolidation path development
- `4.7.5_PreliminaryChat_3.md` — philosophical grounding development
- `4.7.6.1_primitive_artifacts_description.md` — artifact ontology expansion
- `4.7.6.2_EpistemicTrace_Testing_CanonicalTypeDescriptionProduction.md` — Type 8 distinction crystallization
- `4.7.7_ChatGPT_EvaluationsOfFullPaper.md` — external AI evaluation (index file)
- `4.7.7.1_IsThisAISlop_1.md`
- `4.7.7.2_IsThisAISlop_2.md`
- `4.7.7.3_IsThisAISlop_3.md`
- `4.7.7.4_Integrating_Technological_Observations_into_JPEP.md`

#### SP-5: Development Records

**Location:** `SP5_DevelopmentRecords/`

Contains Type 8 (Prompt Development Logs) + Type 11 (Notes)—the meta-level documentation of how instructions evolved (~10–15 pages).

**Part 1: Paper Prompt Development Log (Type 8a)**

Located in `5.1_PaperPromptDevelopmentLog_Type8a/`

- `5.1_paper_prompt_development_log.md` — Complete Prompt development showing how Epistemic Traces evolved into Type 1. Structured decision tracking with PDL-XXX format (≈17 entries).

**Part 2: Section Prompt Development Logs (Type 8b)**

Located in `5.2_SectionPromptDevelopmentLogs_Type8b/`

Shows how Epistemic Traces (Type 2 preliminary chats) became Section Guidance (Type 3). Structured logs documenting refinement process.

- `5.2.1_pdl_section_viii_now_6_A.md` — Section VIII (now 6) guidance development, structural path
- `5.2.2_pdl_section_vii_now_5.md` — Section VII (now 5) guidance; tracks defensive→constructive reframing
- `5.2.3_pdl_section_viii_now_6_B_transparency.md` — Section VIII (now 6) guidance, philosophical path
- `5.2.4_pdl_Appendix_a_initial_steps.md`
- `5.2.5_pdl_section_6_after_review.md` — post-review revision guidance
- `5.2.6_first_development_sp2.md` — SP-2 methodology design
- `5.2.7_pdl_appendix_1.md`
- `5.2.8_pdl-appendix-2.md`
- `5.2.9_pdl_appendix_overall.md`

**Part 3: Notes (Type 11)**

Located in `5.3_Notes_Type11/`

Working documents supporting organization and integrity—not methodologically central but available for inspection.

- `5.3.1_Artifact_ontology_expansion.md`
- `5.3.2_canonical_description.md` — final document type ontology
- `5.3.3_proto_generative_prompt_x.md` — functionally equivalent to SP-2 generation prompt
- `5.3.4_experimental_reproduction_prompt.md` — test reproduction (Sections 1–3)
- `5.3.5_first_proto_reviewer_prompt.md`
- `5.3.6_Artifact_1_Appendix_A_Documentation_Structure_and_Reproduction_Procedure.md`
- `5.3.7_Artifact_2_Figure_Prompts_for_Appendix_A.md`
- `5.3.8_epistemic_trace_emergence_crystallization.md`
- `5.3.9_architectural_guidance.md`
- `5.3.10_section8_guidance.md`
- `5.3.11_reproduction_pack_demonstration.md`
- `5.3.12_section_guidance_1_and_6.md`
- `5.3.13_appendix_guidance_rewritten.md`
- `5.3.14_AppendixA_Writing_Reconstruction.md`
- `5.3.15_section5_synthesis.md`
- `5.3.16_abstract_revision_log.md`
- `5.3.17_nov3_complete_revision_summary.md`
- `5.3.18_ModificationLog_Appendix_A2.md`
- `II_5.3.1_necessary_corrections_to_appendix_in_draft_II.md`
- `II_5.3.2_Complete_Appendix_Writing_Process.md`
- `II.5.3.3_A4_rewritten.md`

### Total Volume and Organizational Logic

Approximately 80–110 pages across the five supplementary packages. For basic reproduction, Reviewer B typically needs ~25–45 pages (SP-1, SP-2, SP-3).

SP-4 contains the writing process itself: what guided the work (Complete Prompt, Section Guidance), what changed (Modification Logs), what was learned (Pattern Summaries), what ensured continuity (Section Summaries, Reference Logs), and the foundational traces (Epistemic Traces).

SP-5 documents how guidance evolved: how exploratory material (Type 2) became actionable instructions (Type 1 and Type 3) via structured refinement (Type 8), plus integrity-supporting notes (Type 11).

This separation keeps artifacts used in the writing process (SP-4) distinct from documentation of the evolution of instructions (SP-5).

## A.5 Guide to Using Supplementary Materials

### For Reviewer B (Reproduction Task)

1.  Begin with SP-3 (Reproduction Guide) — human-directed instructions explaining the overall workflow, comparison criteria (trajectory matching), pass threshold, and the old/new mapping (see A.4).

2.  Provide the LLM with three inputs:

    - SP-1 (Complete Prompt)

    - SP-2.1 (Reproduction Package) — processed extracts with Architectural Overview, Guidance & Refinement Patterns, Source Integration, Development Flow, Key Insights

    - SP-2.2 (Reproduction Procedure) — LLM-directed instructions for how to use SP-1 + SP-2.1 together to generate the reproduction

3.  Compare generated work to submitted paper following criteria in SP-3: intellectual architecture match, presence of key insights, reproducibility of major moves, and gap analysis (expected editorial refinement vs. undocumented work).

4.  If needed, consult SP-4 for deeper investigation. Use the mapping table (A.4) to translate old Roman labels to new Arabic section numbers.

### For Editorial Assessment

• SP-1 shows disclosed inputs (foundational instructions).

• SP-2 provides a processed overview of scope and depth.

• SP-3 offers a clear verification procedure.

• SP-4 demonstrates maximal transparency (iterative refinement, user corrections, methodological learning).

• SP-5 shows systematic instruction development from exploratory traces to actionable guidance.

### For Researchers

• SP-4 Part 7 (Epistemic Traces) — intellectual origins and cross-section influences (e.g., methodology branch).

• SP-4 Part 2 (Modification Logs) — iterative refinement with candid corrections; old § V → new 3 includes 13 modifications; consolidation log documents the old §§ II–IV → new 2 merge.

• SP-4 Part 3 (Pattern Summaries) — methodological learning (epistemic humility for a priori claims, anti-redundancy approaches, attribution precision).

• SP-5 Part 1 (Complete Prompt PDLs) — ≈17 entries showing consolidation of scattered thinking into coherent instructions.

• SP-5 Part 2 (Section-level PDLs) — e.g., old § VII reframing tracked across seven entries.

[^1]: When measures become targets, they cease to be good measures (Strathern, 1997).
