---
project: JPEP
sp: SP-5
type: 8b
label: III_5.2.1_pdl_sections_3_and_6_MHC_integration
title: "III.5.2.1 Prompt Development Log: Sections 3 and 6 - Meaningful Human Control Integration"
section_focus: "Section 3 (Why Engage), Section 6 (Mandatory Transparency in Practice)"
date_created: 2026-01-26
date_last_updated: 2026-01-26
date_finalized: 2026-01-26
status: Complete (Phase 3 - All Guidance Documents Produced)
version: III (Post-arXiv v2 revision cycle)
related_documents: "III_4.7.1_Reasonable_Human_Control_in_AI.md, Full paper2511.08639v1.md"
input_source1_title: "Meaningful Human Control over Autonomous Systems: A Philosophical Account"
input_source1_authors: "Filippo Santoni de Sio, Jeroen van den Hoven"
input_source1_journal: "Frontiers in Robotics and AI"
input_source1_year: 2018
input_source1_doi: "10.3389/frobt.2018.00015"
input_source1_location: "transparency/TEMP/Santoni_de_sio_frobt-05-00015.xml"
input_source1_role: "Source of MHC framework (tracking/tracing conditions)"
input_source2_file: "transparency/Canonical_MD/SP4_ProcessDocumentation/4.7_EpistemicTraces/III_4.7.1_Reasonable_Human_Control_in_AI.md"
input_source2_role: "Already completed transfer of MHC to AI-assisted philosophical writing; provides operational checklist"
input_source3_file: "transparency/TEMP/Note on LLoyd.md"
input_source3_role: "Shows prior thinking connecting replicability to meaningful human control; objection to text demarcation"
input_source4_file: "Paper/MDversion/Full paper2511.08639v1.md"
input_source4_role: "Current paper structure; Sections 3 and 6 as revision targets"
input_source5_title: "Why Less Praise for Enhanced Performance?"
input_source5_authors: "Filippo Santoni de Sio, Nadira S. Faber, Julian Savulescu, Nicole A Vincent"
input_source5_book: "Handbook of Neuroethics (OUP)"
input_source5_year: 2016
input_source5_pages: "27-41"
input_source5_location: "transparency/TEMP/Santoni de Sio et al. (2016) Why less praise for enhanced performance - OUP.pdf"
input_source5_role: "Nature-of-activities framework; constitutive vs regulative rules; analogical basis for Section 3 rewrite"
input_source6_title: "Essentially Contested Concepts"
input_source6_authors: "W. B. Gallie"
input_source6_journal: "Proceedings of the Aristotelian Society"
input_source6_year: 1956
input_source6_doi: "10.1093/aristotelian/56.1.167"
input_source6_role: "Philosophy as essentially contested concept; meta-level framing for Section 3"
input_source7_title: "Epistemic responsibility: toward a community standard for human-AI collaborations"
input_source7_authors: "Dan Lloyd"
input_source7_journal: "Frontiers in Artificial Intelligence"
input_source7_year: 2025
input_source7_doi: "10.3389/frai.2025.1635691"
input_source7_location: "transparency/TEMP/Lloyd_frai-08-1635691.xml"
input_source7_role: "Epistemic responsibility standards; partial adoption (reject Standard 4 on text demarcation)"
output_completed1: "III_4.4.4_SectionGuidance_Section3_EssentiallyContested.md"
output_completed1_date: 2026-01-26
output_completed2: "III_4.4.5_SectionGuidance_Section6_MHC.md"
output_completed2_date: 2026-01-26
source_chat_name: "Claude Code (no chat ID)"
source_chat_date: 2026-01-26
---
# III.5.2.1 Prompt Development Log: Sections 3 and 6 - MHC Integration

Document Type: Type 8b - Prompt Development Log (Section-Level)
Sections: 3 (Why Engage) and 6 (Mandatory Transparency in Practice)
Date Created: January 26, 2026
Date Last Updated: January 26, 2026
Status: In Progress (Phase 1 Complete - MHC Framework; Phase 2 Complete - Nature-of-Activities + Essentially Contested; Phase 3 Pending - Guidance Development)
Production: Claude Code (no chat ID)

---

## Scope and Context

### What This Document Logs

This log documents the development of revised guidance for Sections 3 and 6, integrating the concept of **Meaningful Human Control (MHC)** from autonomous systems ethics into the paper's framework for AI-assisted scholarship.

### The Core Problem

User identified a structural issue:
- Section 3 ("Why Engage") currently has multiple reasons; user wants to **simplify to one**: "we need to understand how the practice of philosophy is evolving - on the human side (e.g., what human creativity becomes)"
- The question arose: where should discussion of **meaningful human control** go?
- User hypothesis: Section 6.1 (where the value of transparency is examined)

### Key Discovery

Prior work exists: **III_4.7.1_Reasonable_Human_Control_in_AI.md** already transfers the MHC framework (tracking/tracing conditions) to AI-assisted philosophical writing. What the paper lacks is:
1. **Justification for the transfer** (why moving MHC from weapons to scholarship is philosophically warranted)
2. **Connection to the paper's specific transparency apparatus** (SP-1 through SP-5, reproduction test)

---

## Development Process

### PDL-001: Initial Placement Analysis

**Trigger:** User question about where MHC discussion belongs

**Analysis of Section 6.1 as candidate location:**

Current Section 6.1 content:
- Discusses what transparency is FOR
- Addresses discovery/justification framework inadequacy
- Articulates traditional philosophical values (guided thought, intellectual honesty, methodological self-consciousness)
- Discusses what opacity destroys under AI production

**Assessment:** Section 6.1 is a **reasonable match** because:
- Already addresses philosophical values transparency serves
- Already discusses attribution and "whose thought you're following"
- Natural place to articulate what transparency must VERIFY

**Tension identified:** MHC literature comes from autonomous weapons—requires explicit justification for domain transfer.

**Initial recommendation:** Combination approach
- Section 3: Signal MHC as key concept, briefly justify transfer
- Section 6.1: Develop substantively, connect to transparency apparatus

---

### PDL-002: Source Analysis - Santoni de Sio & van den Hoven (2018)

**Task:** Extract core MHC framework from primary source

**Key findings from paper:**

**Two necessary conditions for MHC:**

1. **Tracking Condition** (from reason-responsiveness)
   - System behavior must covary with relevant human moral reasons
   - System must be responsive to relevant features of environment
   - Derived from Fischer & Ravizza's guidance control + Nozick's tracking

2. **Tracing Condition** (from ownership)
   - System actions must trace back to proper moral understanding by humans
   - At least one human must: (a) understand system capabilities and effects, (b) understand others may have legitimate moral reactions toward them
   - Distinguishes meaningful control from merely formal presence

**Critical insight:** "Systems whose actions and states are not traceable to relevant understanding and endorsing by some human person—be they a designer, a controller, a user, etc.—no matter how intelligent and reason-responsive they may be, are not under meaningful human control. They would be like human actions carried out under psychological manipulation, subliminal persuasion, brainwashing, and indoctrination." (Section 6.2)

**Relevance to scholarship:** A scholar who merely endorses AI output without understanding its commitments exercises formal involvement but not meaningful control—parallel to soldier pressing button without understanding weapon's action.

---

### PDL-003: Discovery of Prior Transfer Work

**Event:** User pointed to III_4.7.1_Reasonable_Human_Control_in_AI.md

**Finding:** Sophisticated transfer already completed. Key elements:

**Tracking for writing:**
- Does AI output covary with author's intended arguments, commitments, constraints?
- Requires: explicit reason-specification, iterative supervised generation, environmental sensitivity

**Tracing for writing:**
- Can responsibility be traced to human who can explain/defend/own the argument?
- Requires: role clarity, upstream responsibility, preservation of traceability

**Critical passage from III_4.7.1:**
> "If the author cannot explain, defend, or take ownership of key moves in the argument, tracing is already in trouble—because 'ownership' (in the guidance-control sense) is undermined."

**Implication:** The philosophical transfer is done. What's missing is:
1. Justification for WHY transfer is warranted (the "philosophical leap")
2. Connection to paper's specific transparency requirements

---

### PDL-004: The Philosophical Leap - Justification Structure

**Problem:** Transfer from lethal weapons to scholarship seems to involve incommensurable stakes (death vs. text). Why is it warranted?

**Analysis developed:**

| Autonomous Weapons | AI-Assisted Scholarship |
|--------------------|------------------------|
| Can we trace lethal action to human who understood what weapon would do? | Can we trace intellectual contribution to human who understood what was being created? |
| Worry: "responsibility gap" | Worry: "attribution gap" |
| Formal control ≠ meaningful control | Formal contribution ≠ meaningful contribution |

**The structural analogy:**
- Both domains involve human-AI systems where we care whether human involvement was **constitutive** of the outcome
- Both face the problem of distinguishing meaningful from merely formal human presence
- The tracing condition addresses this in both: can outcomes be properly attributed to human agency?

**Key argumentative move:**
> The transfer is warranted because scholarship, like lethal action, involves outcomes where we care not just WHETHER a human was involved, but WHETHER the human's involvement was MEANINGFUL in the sense that:
> - The human understood what was being produced
> - The human's reasons/intentions genuinely shaped the outcome
> - The outcome can be properly attributed to the human's intellectual agency

This justification should appear in **Section 3**.

---

### PDL-005: Connection to Transparency Apparatus

**Problem:** III_4.7.1 gives operational checklist but doesn't connect to paper's specific artifacts (SP-1 through SP-5, reproduction test).

**Analysis developed:**

| MHC Condition | What It Requires | How Paper's Transparency Verifies It |
|---------------|------------------|-------------------------------------|
| **Tracking** | AI output covaries with author's reasons | Process documentation shows iterative correction, explicit reason-specification, responsiveness to author direction |
| **Tracing** | At least one human can explain/defend/own argument | Reproduction test: can intellectual architecture be regenerated from documented human inputs? |

**Key insight - Reproduction test as tracing verification:**
> If a reviewer can reproduce the intellectual trajectory from documented inputs, this demonstrates the author's understanding and direction were SUFFICIENT to generate the work. The outcome traces to human comprehension. If reproduction fails—if major insights cannot be generated from what the author documented—then either documentation is incomplete or the tracing condition is not satisfied.

This connection should be developed in **Section 6.1**.

---

### PDL-006: Revised Structural Proposal

**Section 3 revisions needed:**
1. Simplify to ONE reason: understanding how philosophy evolves on the human side
2. Introduce MHC as key concept
3. **Add:** Explicit justification for transfer from weapons/autonomous systems to scholarship
4. Signal that Section 6 develops operational implications

**Section 6.1 revisions needed:**
1. Draw explicitly on III_4.7.1's tracking/tracing analysis
2. **Add:** Connection between tracking/tracing and paper's specific transparency apparatus
3. **Add:** Reproduction test framed as tracing verification
4. Explain WHY these requirements matter (not just what they are)

**Argumentative unity:**
- Section 3 poses the question: What does meaningful human control over intellectual production require?
- Section 6 answers it: The tracing condition, verified through transparency

---

## Draft Materials Produced (Phase 1)

### Section 3 Draft Framework

Opening acknowledges wonder-driven inquiry (existing), then pivots:

> **The practice of philosophy is evolving on the human side.** When scholars work extensively with AI systems, fundamental questions arise about what human creativity, judgment, and intellectual ownership become under these conditions. These are not questions about AI—they are questions about *us*.

Introduces MHC:

> These questions have philosophical precedent in an unexpected domain. In debates over autonomous weapons systems, ethicists developed the concept of *meaningful human control* (Santoni de Sio & van den Hoven, 2018) to articulate conditions under which human involvement remains substantive rather than nominal.

Justifies transfer:

> The structural problem transfers to intellectual production. A scholar who merely endorses AI-generated text exercises formal involvement but perhaps not meaningful control over the intellectual contribution. The question parallels the weapons case: under what conditions does human involvement in AI-mediated production remain *constitutive* of the outcome in ways that make attribution appropriate?

### Section 6.1 Draft Framework

Opens by connecting to Section 3:

> Section 3 introduced meaningful human control as the conceptual framework for understanding what human intellectual agency becomes under AI mediation. The transparency requirements proposed here operationalize that framework—specifically, its *tracing condition*.

Develops tracing for scholarship:

> Transferred to scholarship, the tracing condition requires that intellectual contributions be traceable to human understanding and direction. This is not satisfied by mere endorsement of AI output. It requires:
> 1. **Understanding of capabilities**: The author understood what the AI system could and could not contribute
> 2. **Understanding of contribution**: The author understood what they themselves were contributing
> 3. **Ownership of trajectory**: The intellectual architecture traces to human direction

Connects to reproduction test:

> The reproduction test operationalizes tracing assessment. The reviewer asks: can the intellectual contribution be reproduced from the documented human inputs? If yes, this demonstrates the author's inputs were *sufficient* to generate the work's intellectual architecture—the trajectory traces to documented human direction.

---

## Status and Next Steps

**Phase 1 (Complete):** Brainstorming and framework development
- Analyzed MHC source
- Discovered prior transfer work (III_4.7.1)
- Identified what paper lacks: justification + connection to apparatus
- Produced draft frameworks for both sections

**Phase 2 (Pending):** Guidance development
- Develop full Section Guidance for Section 3
- Develop full Section Guidance for Section 6.1
- Coordinate with existing guidance files
- Document in continuation of this PDL

---

## Key Insights from Phase 1

1. **Transfer already done, justification missing:** III_4.7.1 applies MHC to writing but doesn't justify why the transfer is warranted. This is the "philosophical leap" that needs articulation.

2. **Structural analogy is deep:** Both weapons and scholarship involve distinguishing meaningful from merely formal human involvement. The tracing condition addresses this in both domains.

3. **Reproduction test = tracing verification:** The paper's reproduction test operationalizes the MHC tracing condition. This connection makes the transparency requirements philosophically grounded rather than merely procedural.

4. **Argumentative unity across sections:** Section 3 poses the question (what does MHC require?), Section 6 answers it (tracing condition verified through transparency). This creates coherent flow.

5. **One reason suffices:** The "human side" reason (how philosophy evolves, what creativity becomes) subsumes other reasons when framed through MHC.

---

## Cross-Reference Summary

**Content sources:**
- Santoni de Sio & van den Hoven (2018): MHC framework (tracking/tracing)
- III_4.7.1: Prior transfer to AI-assisted writing
- Note on Lloyd.md: Early thinking connecting replicability to MHC

**Outputs (pending):**
- Section Guidance for Section 3
- Section Guidance for Section 6.1

**Integration points:**
- Section 3 → Section 6 forward reference
- Section 6 → reproduction test (Section 7) connection
- Transparency apparatus (SP-1 through SP-5) → MHC tracing condition

---

## Phase 2: Nature-of-Activities Framework and Essentially Contested Concepts

*Added: 2026-01-26 via Claude Code (no chat ID)*

### PDL-007: Source Analysis - Santoni de Sio et al. (2016) Enhancement Paper

**Task:** Analyze "Why Less Praise for Enhanced Performance?" for analogical transfer to AI-assisted philosophy

**Source:**
- Santoni de Sio, F., Faber, N. S., Savulescu, J., & Vincent, N. A. (2016). "Why Less Praise for Enhanced Performance?" In *Handbook of Neuroethics*. OUP, pp. 27–41.

**Core Problem Addressed:** Why do people intuit that enhanced performance deserves less praise (the "Less Praise Intuition" or LPI)?

**Three Inadequate Justifications (rejected by authors):**

| Justification | Claim | Why It Fails |
|---------------|-------|--------------|
| Responsibility-shifting | The enhancer "did it," not the person | Factual mistake: enhancers don't replace human effort |
| Authenticity | The enhanced person is a "different" person | Implausible metaphysics of identity |
| Cheating | Unfair advantage | If everyone can enhance, no unfairness—yet concerns remain |

**The Nature-of-Activities Approach (authors' novel solution):**

Key conceptual tools:
1. **Goal-directed** vs **Practice-oriented** activities (external vs internal goals)
2. **Constitutive** vs **Regulative** rules (define vs regulate the activity)
3. **Coarse-grained** vs **Fine-grained** descriptions of activities

**Core Insight:** Enhancement may change *what activity is being performed*. Enhanced-A ≠ A. The enhanced person doesn't deserve *less* praise for A—they deserve *no* praise for A because they didn't do A. They did A_E (enhanced-A), which requires a different yardstick.

**Critical Passages:**

On fine-grained descriptions (p. 35):
> "On coarse-grained descriptions, 1950's and today's car racing are the same game... However, on more fine-grained descriptions, these are significantly different activities."

On the contested middle ground (p. 34):
> "Still, many rules in sport and education fall somewhere between these two extremes. They are neither as vital as the ban on wheels in marathons nor as arbitrary as allocating 90 minutes to football games."

---

### PDL-008: The Analogy to AI-Assisted Philosophy

**Structural Parallel:**

| Enhancement Debate | AI-Assisted Philosophy |
|--------------------|------------------------|
| Does modafinil change what "studying" is? | Does AI change what "philosophizing" is? |
| Is this the same sport or different? | Is this the same intellectual activity or different? |
| Which rules are constitutive? | What is constitutive of philosophy? |
| Contested—depends on activity's "point" | Contested—philosophy is essentially contested |

**The Deep Point:** Whether enhancement changes the activity depends on:
- Which features are **constitutive** (not just regulative)
- What **level of description** you adopt

For philosophy: *what counts as constitutive is itself philosophically contested*.

---

### PDL-009: Essentially Contested Concepts - The Meta-Level Move

**Source:** Gallie, W. B. (1956). "Essentially Contested Concepts." *Proceedings of the Aristotelian Society*, 56, 167–198.

**The Move:** "Philosophy" is an **essentially contested concept** (Gallie). What counts as "doing philosophy" is itself a philosophical question with no neutral adjudication.

**Consequence:** The question "Does AI fundamentally change philosophy?" cannot be settled because it presupposes an answer to "What is philosophy?"—which is contested.

**This reframes Section 3 entirely:**

1. The practice of philosophy is changing (empirical fact)
2. Whether this change is *continuous* (like word processors) or *discontinuous* (like roller-skates in a marathon) depends on what features of philosophy are constitutive
3. But "philosophy" is an essentially contested concept—what is constitutive is itself contested
4. Therefore: **We cannot settle whether AI fundamentally changes philosophy without settling what philosophy is**
5. What we *can* do: create conditions for an informed meta-philosophical discussion
6. This requires: **transparency that enables tracking what philosophy becomes**

---

### PDL-010: Revised Nesting Structure for Three Concerns

**User direction (2026-01-26):** Three distinct focuses, with epistemic integrity first, but all nested under the meta-philosophical tracking goal.

**The Nesting:**

```
OUTERMOST: Track what philosophy becomes (meta-philosophical goal)
    │
    ├── Why? Because philosophy is essentially contested, so we can't
    │   settle whether AI changes it without tracking what it becomes
    │
    └── MIDDLE: Ensure meaningful human control (MHC—tracing condition)
            │
            ├── Why? Proper attribution requires tracing intellectual
            │   contributions to human understanding and direction
            │
            └── INNERMOST: Maintain epistemic integrity (Lloyd)
                    │
                    └── Why? Knowledge claims must be trustworthy;
                        confabulation must be controlled; verification
                        must be possible
```

**The Logic:**
- Epistemic integrity (Lloyd) ensures knowledge claims are trustworthy
- MHC tracing ensures those claims can be attributed to human agency
- Both are **instrumental** to the higher goal: enabling informed meta-philosophical discussion about what philosophy is becoming

**Key Difference from Lloyd:**
- Lloyd wants "demarcation of text" (intra-textual clarity marking AI vs human text)
- User objection (from Note on Lloyd): this relies on "primitive view of AI assistance"
- Our approach: "the real in-principle replicability follows from the clarity of the process documentation" (SP4), not from text-level demarcation

---

### PDL-011: Source Analysis - Lloyd (2025)

**Source:** Lloyd, D. (2025). "Epistemic responsibility: toward a community standard for human-AI collaborations." *Frontiers in Artificial Intelligence*, 8, 1635691.

**Four Standards Proposed:**

1. **Prominence** - AI content immediately apparent (title header, not buried)
2. **Replicability** - Prompts explicitly stated; evolution documented
3. **Content cross-checking** - Human verifier for all AI factual claims
4. **Intra-textual clarity** - AI-generated content demarcated via style markers

**Key Argumentative Moves:**
- Goals are **transparency** and **replicability** - mutually reinforcing
- Standards should become "community expectations" (not imposed from above)
- Differs from COPE: wants frontend prominence, not buried acknowledgment

**Relevance to Our Paper:**

| Lloyd's Standard | Our Approach | Comparison |
|------------------|--------------|------------|
| Prominence | SP-1 (Declaration) | Compatible |
| Replicability | SP-4 (Process documentation) | Compatible but deeper |
| Cross-checking | Implied in review process | Less explicit |
| Intra-textual clarity | **Rejected** | Primitive view of AI assistance |

**User's Objection to Standard 4 (from Note on Lloyd):**
> "the idea of 'demarcation of text' (inter textual clarity) relies on a primitive view of ai assistance. We could have papers that are almost entirely AI outputted. They could range from lots of human input (but full stylistic rewrite) to various forms of prompting to shaping workflows. We can't anticipate what the salient human input is"

---

## Updated Status and Next Steps

**Phase 1 (Complete):** MHC framework analysis
**Phase 2 (Complete):** Nature-of-activities framework; essentially contested concepts framing

**Phase 3 (In Progress):** Guidance development

**Constraint (added 2026-01-26):** All Section Guidance prompts must be either:
- **Self-sufficient** (contain all information needed for drafting AI to produce the section), OR
- **Include explicit pointers** to source documents the drafting AI should read

This ensures prompts remain usable across conversation clears.

**Completed:**
- III_4.4.4_SectionGuidance_Section3_EssentiallyContested.md (2026-01-26)
- III_4.4.5_SectionGuidance_Section6_MHC.md (2026-01-26)

**Post-completion addition (2026-01-26):**
Added concept of **unknown future philosophical skills** to both guidance files:

**Steering note created (2026-01-26):**
Created III_5.3.21_SteeringNote_v3_Section_Revisions.md to track git workflow and drafting process. Modeled on epistemic constitutional ai/CLAUDE_UPDATE_BRIEF_SWISS.md.

**Constraint added (2026-01-26):**
All Section Guidance prompts must be self-sufficient OR include explicit pointers to source documents. This ensures prompts remain usable across conversation clears.

**Unknown future skills addition (2026-01-26):**
- We don't know what AI-assisted practice will look like
- Evolution: prompting → steering → architecture building → unknown
- Compounds the essentially contested uncertainty (Section 3)
- Strengthens rejection of text demarcation: process documentation captures *whatever* contribution emerges (Section 6)

**Section 3 Guidance Summary:**
- Section 3 should now be **completely rewritten** around:
  - Practice is changing (empirical)
  - Whether continuously or discontinuously is contested (Santoni de Sio)
  - Because philosophy is essentially contested (Gallie)
  - Goal: track what philosophy becomes (meta-philosophical)
  - Everything else nests under this
- Develop full Section Guidance for Section 6.1 with MHC connection

---

## Updated Cross-Reference Summary

**Content sources:**
- Santoni de Sio & van den Hoven (2018): MHC framework (tracking/tracing)
- Santoni de Sio et al. (2016): Nature-of-activities approach (constitutive vs regulative rules)
- Gallie (1956): Essentially contested concepts
- Lloyd (2025): Epistemic responsibility standards (partial adoption)
- III_4.7.1: Prior transfer of MHC to AI-assisted writing
- Note on Lloyd.md: Early thinking; objection to text demarcation

**Outputs (completed):**
- III_4.4.4_SectionGuidance_Section3_EssentiallyContested.md (2026-01-26)
- III_4.4.5_SectionGuidance_Section6_MHC.md (2026-01-26)

**New integration points:**
- Gallie → Section 3 (essentially contested framing)
- Santoni de Sio (2016) → Section 3 (nature-of-activities analogy)
- Lloyd → Section 6 (partial engagement; rejection of Standard 4)

**Process documentation:**
- III_5.3.21_SteeringNote_v3_Section_Revisions.md (git workflow + progress tracking)
- III_4.7.2_WorkingDrafts_Belong_to_SP5.md (epistemic trace on artifact placement)


---

## Phase 4: Drafting Attempts and Guidance Revision

*Added: 2026-01-28 via Claude Code / Claude Opus 4.5*

### PDL-012: Section 3 Draft — Successful

**Date:** 2026-01-28
**Output:** III_5.4.1_Section3_v3.md
**Source guidance:** III_4.4.4_SectionGuidance_Section3_EssentiallyContested.md

Section 3 was a complete rewrite (as specified in guidance). The guidance was self-sufficient: it contained the full argumentative structure, key references, and all conceptual content needed. The drafting AI produced a ~950-word draft following the guidance structure. Author reviewed and manually edited the draft.

**Outcome:** Draft accepted after manual edits.

### PDL-013: Section 6 Draft — FAILED

**Date:** 2026-01-28
**Output:** III_5.4.2_Section6_v3.md (defective — to be replaced)
**Source guidance:** III_4.4.5_SectionGuidance_Section6_MHC.md (original version)

**What went wrong:** The drafting AI produced a blank-slate rewrite of Section 6 without reading the existing version. The guidance file listed the existing paper as "optional reading" under "Source Documents for Drafting AI." The AI treated this as permission to ignore it.

**What was lost:**
- Discovery/justification framework critique (Reichenbach)
- Traditional philosophical values discussion (Williams, Cavell, Nozick, Lewis examples)
- Attribution argument ("whose thought you're following")
- Connection to Section 5 design principles
- Three functions of disclosure
- Concrete implementation (paper as demonstration)
- Experimental development framing (6.3)
- Pilot observations (6.4)
- The entire subsection structure (6.1-6.4)

**Root cause:** The guidance distinguished Section 3 ("COMPLETE REWRITE") from Section 6 ("SIGNIFICANT REVISION") but did not enforce reading the existing version. The existing content was listed under "optional reading" alongside other reference materials.

**Lesson:** For revision tasks (as opposed to complete rewrites), guidance must:
1. Make reading the existing version **mandatory**, not optional
2. Specify what to **keep**, what to **modify**, and what to **add**
3. List hard constraints on existing content that must not be lost
4. Treat SP-1 through SP-5 as fixed framework constraints

### PDL-014: Guidance Revision

**Date:** 2026-01-28
**File revised:** III_4.4.5_SectionGuidance_Section6_MHC.md

**Changes made:**
1. Added `CRITICAL INSTRUCTION` block requiring mandatory reading of existing Section 6
2. Added `Hard Constraints` section listing all v1 content to preserve, organized by subsection (6.1-6.4)
3. Added `SP-1 through SP-5: Fixed Framework` as top-level hard constraint
4. Added `What the Revision ADDS` section separating new MHC content from preserved content
5. Restructured `Argumentative Structure` to use KEEP/REVISE/ADD format for each subsection
6. Added preservation checks to `Draft Checklist`
7. Moved existing paper from "optional reading" to `MANDATORY Reading` section
8. Added `Revision History` table documenting the change and its reason
9. Changed header from "SIGNIFICANT REVISION" to "SIGNIFICANT REVISION (NOT a complete rewrite)"

**Constraint identified (2026-01-28):** SP-1 through SP-5 as specified in v1 are hard constraints on the entire paper — all revisions ground the existing apparatus, they do not redesign it.


## Connections (auto)

### Explicit links (inputs/outputs/etc.)
**related_documents:**
- UNRESOLVED: III_4.7.1_Reasonable_Human_Control_in_AI.md, Full paper2511.08639v1.md
