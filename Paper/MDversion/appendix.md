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

These insights about stakeholder expectations became Epistemic Trace 2 (SP4.7.2). What began as presentation strategy generated understanding about documentation design.

This pattern—conversations beginning with one purpose generating insights valuable for another—occurred twice. First, the journal strategy conversation becoming article foundation (SP4.7.1). Second, the LinkedIn discussion becoming stakeholder analysis (SP4.7.2).

#### Pattern 2: Self-Recursion in Documentation Development

A recurring pattern involved using conversations as subject matter when developing the documentation system itself.

When establishing the artifact ontology—what document types should exist, how they should relate—conversations about documentation became material for analyzing documentation. The conversation from October 14 (documented in 4.7.5) was later used (October 18-19) as subject matter for analyzing whether the artifact ontology adequately covered all interaction types. The conversation functioned as both generative source and analytical object.

This self-referential pattern appeared throughout documentation development. Testing proposed ontologies required examining actual conversations, which revealed gaps or ambiguities, which led to ontology refinements, which then required testing against conversations. The documentation system developed through examining its own materials.

#### Pattern 3: Branching When Different Work Types Require Different Approaches

Conversation SP4.7.3 (Methodological Conversation, October 12-13) synthesized the Complete Prompt, both epistemic traces, accumulated pattern summaries and modification logs, while addressing a new question: what documentation material types should exist and how should they be organized?

This conversation created two parallel development paths.

Path A continued artifact ontology work directly. Conversation 4.7.4 (Artifact Consolidation) refined the four-tier document structure, established naming conventions, and clarified required versus optional materials. This produced Section VIII guidance (4.4.4) focused on structural framework and Review Mechanism design.

Path B proceeded through Section VII's development. Section VII required guidance about discontinuity and design principles. Developing that guidance (SP5.2.2) identified three design principles: ecological validity, good faith orientation, and cost structure as costly signaling. Section VII was written using that guidance.

Writing Section VII produced the complete section plus provisional thoughts about Section VIII. These became inputs for conversation 4.7.5, which developed philosophical grounding for transparency requirements: traditional values in philosophical writing, what opacity destroys, why attribution matters. This produced Section VIII guidance (4.4.6) about philosophical values and disclosure components.

Section VIII received two separate guidance artifacts from two independent development paths: structural framework from Path A, philosophical grounding from Path B.

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
[fig 3]
<figure>
<img src="media/image3.svg" style="width:6.27014in;height:9.01111in" />
<figcaption><p>. Writing Flow and Input-Output Relations.</p></figcaption>
</figure>

### How to Navigate the Diagram

The diagram organizes content by writing phases (major horizontal sections). Navigation focuses on key paths rather than every connection:

**Phase 1 - Foundation and Setup** Establishes foundational methods through original conversations (SP4.7.1) and complete prompt development (SP5.1), leading to 4.1. These primary artifacts set the conceptual framework and methodological approach for the entire writing process.

**Phase 2 - Main Writing Sequence (Sections I-VI)** Systematic development of core sections using feed-forward methodology. Each section builds on previous work through three mechanisms: pattern summaries extracting insights from completed sections, modification logs tracking evolving understanding, and section-specific guidance documents incorporating accumulated knowledge. Creates cumulative understanding through methodical progression.

**Phase 3 - Further Brainstorming and Parallel Development** SP4.7.3 serves as critical branching point, spawning two independent development streams: artifact consolidation path developing structural frameworks and review mechanisms (SP4.7.4 → SP4.4.4), and philosophical development path proceeding through Section VII toward values and theoretical grounding (SP4.7.5 → SP4.4.6). Prompt Development Logs emerge as documentary practice becomes more sophisticated. Both paths advance simultaneously, developing complementary dimensions.

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

### Section Numbering Reference Table

To navigate between supplementary materials (which use old numbering) and the final article:

| Process Artifacts (old) | Final Article (new)                   |
|-------------------------|---------------------------------------|
| § I                     | § 1: Introduction                     |
| §§ II + III + IV        | § 2: Systemic Barriers (consolidated) |
| § V                     | § 3: Why Engage                       |
| § VI                    | § 4: Dilemma Reconsidered             |
| § VII                   | § 5: Discontinuity                    |
| § VIII                  | § 6: Mandatory Transparency           |
| § IX                    | § 7: Review Mechanism                 |

All process documentation uses old Roman numbering. This preserves ecological validity by reflecting the actual process. Use the table above to connect artifacts to final sections.

### The Five Supplementary Files

#### SP-1: Complete Prompt (Type 1)

~20 pages containing the final synthesized prompt from the prompt development process (documented as records described in SP-5 Part 1). Contents include the full structure (eleven sections), the "laundering" barrier, incentive gradient analysis, the dual solution (discontinuity + mandatory transparency), the dual-reviewer mechanism, tone requirements, and annotated references.

Used as constant input throughout old §§ I–VI and VIII; temporarily absent for old § VII (new 5). Reviewer B loads this as the primary input when reproducing.

#### SP-2: Reproduction Package (Type 9)

~15–20 pages synthesized from SP-4 records via preprocessing. Six sections:

- \[optimal pre-processing recipe still being researched, preliminary tests logged as 5.2.6.1, with artifacts 5.3.3-5\]

#### SP-3: Reproduction Guide (Type 10)

~5 pages explaining how to combine SP-1 and SP-2, how to evaluate by trajectory matching (not output matching), the pass threshold (sufficiency with expected refinement gap), time estimates, and when to consult SP-4/SP-5.

#### SP-4: Process Documentation (~35–55 pages consolidated)

All Type 1–7 materials, organized into seven record parts inside the consolidated Word document(s):

**Part 1: Complete Prompt (Type 1)**

Record label: CompletePrompt (also represented in SP-1).

**Part 2: Modification Logs (Type 7)**

4.2.1 ModificationLog_I (Introduction)

4.2.2 ModificationLog_Section_II

4.2.3 ModificationLog_Section_III

4.2.4 ModificationLog_Section_IV

4.2.5 ModificationLog_Section II-III-IV_Consolidation

4.2.6 ModificationLog_Section_V (3)

4.2.7 ModificationLog_Section_VI (4)

4.2.8 ModificationLog_Section_VII (5)

4.2.9 ModificationLog_Section_VIII (6)

4.2.10 ModificationLog_Section_IX (7)

4.2.11 ModificationLog_Appendix

4.2.12 ModificationLog_Title_and_Abstract

**Part 3: Pattern Summaries (Type 4)**

PatternSummary_Section1.md through PatternSummary_Section9.md (old numbering):

4.3.1 Section II (2)

4.3.2 Sections II-III (later consolidated into 2)

4.3.3 Section IV (later consolidated into 2)

4.3.4 Section V (now 3)

4.3.5 Section VIII (now 6)

**Part 4: Section Guidance (Type 3)**

SectionGuidance_Section1.md through SectionGuidance_Section9.md (old numbering), plus SectionGuidance_Appendix.md:

4.4.1 Part 1: before the first full draft

4.4.2 For Section IV (both consolidated into 2 later)

4.4.3 For Section V (now 3) for Section VI (now section 4)

4.4.4 For Section VIII-A (now 6) from 5.2.1

4.4.5 For Section VII \[now 5\] (from SP5.2.2)

4.4.6 For Section VIII-B and Section IX guidance

4.4.6.i For Section VIII-B \[now 6\] (from 5.2.3)

4.4.6.ii From Section VIII \[now 6\] to Section IX \[now 7\]

4.4.7 From section IX \[7\] to Conclusion

4.4.8 Section Guidance: Introduction (tone changes) and Section IV

4.4.9 Section 6 Revision Guidance

4.4.10 Section Guidance: Consolidate Section 2 (Systemic Barriers)

4.4.11 Trajectory Claims Check (full paper analysis)

4.4.12 From Draft 1 (−Appendix) to Appendix A

4.4.13 From Full Draft (+Appendix) to Section 6

**Part 5: Section Summaries (Type 5)**

SectionSummary_Section1.md through SectionSummary_Section9.md (old numbering):

4.5.1 Introduction

4.5.2 Section II (later 2)

4.5.3 Section III (later 2)

4.5.4 Section IV (later 2)

4.5.5 Section V (later 3)

4.5.6 Section VI (later 4)

4.5.7 Section VIII (later 6)

4.5.8 Section IX (later 7)

**Part 6: Reference Logs (Type 6)**

4.6.1 Complete citations by section

4.6.2 Complete References

**Part 7: Epistemic Traces (Type 2)**

4.7.1 Original Text Conversation Extract (Redacted)

4.7.2 Original text conversation on how to make the paper visible and useful for different stakeholders

4.7.3 Preliminary Chat

4.7.4 Preliminary Chat

4.7.5 Preliminary Chat

4.7.6 Epistemic Trace: Discovery of the Epistemic trace / (Session) prompt development log distinction / Crystallization of the Distinction

4.7.6.1 Step 1. Note: Artifact Ontology Expansion — Type 2b

4.7.6.2 Step 2. Introduces Type 8 Distinction and Section Prompt Development Logs

4.7.6.3 Step 3. Testing and "canonical type description" production

4.7.7 Chat GPT evaluations of the full paper

4.7.7.1 Is this AI slop? (Chat GPT)

4.7.7.2 Is this AI slop (2)? (Chat GPT)

4.7.7.3 Is this AI Slop (3)? (Chat GPT)

4.7.7.4 Infrastructure Limitations and Transparency Framework

#### SP-5: Development Records (~10–15 pages)

Contains ONLY Type 8 (Prompt Development Logs) + Type 11 (Notes) — the meta-level documentation of how instructions evolved.

**SP5.1: Paper Prompt Development Log (Type 8a)**

Complete Prompt development — shows how Epistemic Traces (SP-4 Part 7) evolved into Complete Prompt (Type 1). Structured decision tracking with PDL-XXX format.

**SP5.2: Section Prompt Development Logs (Type 8b)**

Shows how Epistemic Traces (Type 2 preliminary chats in SP-4 Part 7) became Section Guidance (Type 3). Structured logs documenting refinement process, NOT the exploratory dialogue itself.

1.  SP5.2.1 Prompt Development Log: Section VIII \[now 6\] Guidance (A-4.4.4)

2.  SP5.2.2 Prompt Development Log: Section VII \[now 5: "Signalling Discontinuity"\] Guidance

3.  SP5.2.3 Prompt Development Log: Section VIII \[now 6\] Guidance (B-4.4.6)

4.  SP5.2.4 Prompt Development Log: Appendix A

5.  SP5.2.5 Prompt Development Log: Section 6 (after full paper review)

6.  SP5.2.6 Reproduction Pack: Methodology Design Conversation

    - SP5.2.6.1 First attempt (during 4.7.3)

    - SP5.2.6.2 Second attempt (after paper completion)

    - SP5.2.6.3 Final attempt (delivering SP3 definitive items)

**SP5.3: Notes (Type 11)**

1.  SP5.3.1 Note: Artifact Ontology Expansion - Type 2b

2.  SP5.3.2 Canonical Description of the Final Document Type Ontology

3.  SP5.3.3 Proto-Generative Prompt for SP-2.1 (functionally equivalent to SP5.4)

4.  SP5.3.4 Experimental Proto-Reproduction Package (Sections 1-3)

5.  SP5.3.5 First Proto-Reviewer Prompt

### Total Volume and Organizational Logic

Approximately 80–110 pages across the five supplementary documents. For basic reproduction, Reviewer B typically needs ~25–45 pages (SP-1, SP-2, SP-3).

• SP-4 contains the writing process itself: what guided the work (Complete Prompt, Section Guidance), what changed (Modification Logs), what was learned (Pattern Summaries), what ensured continuity (Section Summaries, Reference Logs), and the foundational traces (Epistemic Traces).

• SP-5 documents how guidance evolved: how exploratory material (Type 2) became actionable instructions (Type 1 and Type 3) via structured refinement (Type 8), plus integrity-supporting notes (Type 11).

*This separation keeps Artifacts used in the writing progress (SP-4) distinct from the documentation of the evolution of instructions (SP-5).*

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
