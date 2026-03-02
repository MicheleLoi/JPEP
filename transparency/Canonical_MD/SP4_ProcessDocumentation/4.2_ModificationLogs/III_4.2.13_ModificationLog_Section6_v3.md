---
project: JPEP
sp: SP4
document_type: Modification Log
title: "Modification Log: Section 6 - Stage III MHC Revision"
section_focus: "Section 6 (Mandatory Transparency in Practice)"
version: III (v3 revision cycle)
models:
  - "Claude Opus 4.5 (2026-01-28, guidance revision)"
  - "Claude Sonnet 4.6 (2026-03-02, redraft and SP reconception)"
date_started: 2026-01-28
date_last_updated: 2026-03-02
status: Draft revised — SP reconception complete; Section 7 and Appendix revisions pending

phase1_label: guidance_revision
phase1_source: "Claude Code / Claude Opus 4.5"
phase1_date: 2026-01-28

related_documents:
  - "III_4.4.5_SectionGuidance_Section6_MHC.md (guidance file — revised 2026-01-28)"
  - "III_5.2.1_pdl_sections_3_and_6_MHC_integration.md (PDL — Phase 4 added 2026-01-28)"
  - "III_5.4.2_Section6_v3.md (current working draft)"
  - "4.2.9_ModificationLog_Section_VIII_6__S06.md (original Section 6 modification log)"
  - "III_4.7.3_MHC_Tracing_SP_Reconception.md (epistemic trace — 2026-03-02)"
---

# Modification Log: Section 6 - Stage III MHC Revision

## Overview

This log tracks the Stage III revision of Section 6 ("Mandatory Transparency in Practice"). The revision integrates the Meaningful Human Control (MHC) framework into the existing section, grounding the paper's transparency apparatus (SP-1 through SP-5) in the tracking/tracing conditions from Santoni de Sio & van den Hoven (2018).

## Key Constraint (original — superseded in part)

~~**SP-1 through SP-5 as specified in v1 are hard constraints.** The revision grounds the existing apparatus in MHC — it does not redesign, rename, or restructure it.~~

**Update (2026-03-02):** The SP labels (SP-1 through SP-5) are retained, but their *roles* were reconceived during this revision cycle. See Entry 4 and Entry 5 below, and epistemic trace III_4.7.3.

---

## Entry 1: Failed First Draft (2026-01-28)

**Action:** Attempted to draft Section 6 v3 from guidance file III_4.4.5_SectionGuidance_Section6_MHC.md

**Result:** DEFECTIVE. The drafting AI (Claude Opus 4.5, via Claude Code) produced a blank-slate rewrite without reading the existing Section 6 (subsections 6.1-6.4).

**Content lost in defective draft:**
- Discovery/justification framework critique (Reichenbach)
- Traditional philosophical values (Williams, Cavell, Nozick, Lewis examples)
- Attribution argument ("whose thought you're following")
- Connection to Section 5 design principles
- Three functions of disclosure (verification, methodological learning, preservation of values)
- Concrete implementation (paper as demonstration)
- Experimental development framing (6.3)
- Pilot observations (6.4)
- Entire subsection structure (6.1-6.4)

**Root cause:** Guidance file listed existing paper as "optional reading" and did not specify what to keep vs. add.

**File:** III_5.4.2_Section6_v3.md (to be replaced with corrected draft)

---

## Entry 2: Guidance Revision (2026-01-28)

**Action:** Revised guidance file III_4.4.5_SectionGuidance_Section6_MHC.md

**Changes:**
1. Made reading existing Section 6 MANDATORY (was "optional reading")
2. Added "Hard Constraints" section listing v1 content to preserve per subsection
3. Added SP-1 through SP-5 as top-level fixed framework constraint
4. Added "What the Revision ADDS" section separating new from preserved content
5. Restructured argumentative structure to KEEP/REVISE/ADD format
6. Added preservation checks to draft checklist
7. Added revision history table

**Lesson recorded:** For revision tasks (vs. complete rewrites), guidance must specify what to keep, modify, and add. Existing content must be mandatory reading, not optional.

---

## Entry 3: Section 6 Redraft (COMPLETE — 2026-03-02)

**Action:** Redrafted Section 6 v3 using revised guidance file (III_4.4.5, revised 2026-01-28).

**Source:** Claude Code / Claude Sonnet 4.6

**Process:** Read existing Section 6 (6.1–6.4) in full before drafting. Identified all hard-constraint content to preserve. Produced revised draft that keeps v1 structure while adding MHC framework as theoretical grounding.

**File:** III_5.4.2_Section6_v3.md (replaces defective first draft)

**Content preserved from v1:**
- Subsection structure (6.1–6.4) retained
- Discovery/justification framework critique (Reichenbach)
- Gaming resistance vs. ecological validity argument
- Level 1 vs. Level 2 orientation
- Not-from-moral-desert / not-economic-necessity clarifications
- Traditional philosophical values: Williams, Cavell, Nozick, Lewis examples
- Attribution argument ("whose thought you're following")
- Three functions of disclosure (verification, methodological learning, preservation of values)
- Three-component structure (model/process; prompts/outputs; process narrative)
- This paper as concrete implementation
- Accessibility emphasis (no technical expertise required)
- Section 5 connection (ecological validity, good faith, cost structure)
- 6.3: experimental/evolutionary framing, community convergence, Level 2
- 6.4: timestamps constraint, synthesis risks, templates-not-protocols

**Content added (MHC integration):**
- Opening: connection to Section 3's essentially-contested-concept conclusion
- MHC framework: tracking + tracing conditions (Santoni de Sio & van den Hoven 2018)
- Key quote on tracing (§6.2)
- Weapons parallel (drone strike) to make tracing concrete
- Closing of 6.1: attribution argument linked explicitly to tracing condition
- SP-1 through SP-5 mapped to tracing in a table (6.2)
- ~~Reproduction test framed as tracing verification (6.2)~~ ← **superseded by Entry 5**
- Lloyd engagement: adopt Standards 1–2, reject Standard 4 with explanation (6.2)
- Three nested concerns diagram: epistemic integrity → tracing → tracking what philosophy becomes (6.2)

**Status:** Superseded in part — see Entries 4 and 5 for SP reconception revisions applied to this draft.

---

## Entry 4: SP Table Critique — Reproduction Test Problem (2026-03-02)

**epistemic_trace:** III_4.7.3_MHC_Tracing_SP_Reconception.md
**source:** User (2026-03-02), developed in dialogue with Claude Sonnet 4.6

The reproduction test is not a viable operationalization of the MHC tracing condition (model deprecation, non-deterministic outputs, time-scale of scholarship, romantic author assumption); see III_4.7.3 for full analysis.

---

## Entry 5: SP Structure Reconception — Documentation Adequacy (2026-03-02)

**Action:** Reconceived the roles of SP-1 through SP-3 to replace the reproduction-test framework with a documentation-adequacy framework.

**New SP roles:**

| SP | Old role | New role |
|----|----------|----------|
| SP-1 | Declaration that AI was used | Summary of *how* AI was used (points to SP-3) |
| SP-2 | Reproduction Package (compiled to support test) | Navigation document — structured index enabling access to SP-3, SP-4, SP-5 |
| SP-3 | Reproduction Guide (instructions for test) | Documentation account — detailed explanation of how AI was used + argument for adequacy |
| SP-4 | Process Documentation | Unchanged — primary substance against which SP-3's adequacy claim is assessed |
| SP-5 | Development Records | Unchanged — enables deeper tracing of intellectual direction |

**Key conceptual shift:** The tracing condition (Santoni de Sio & van den Hoven 2018) requires outputs to be *traceable to* human understanding — not *reproducible from* human inputs. Documentation adequacy is the appropriate operationalization: SP-3 makes the author's case that the documentation sufficiently shows the intellectual trajectory traces to human understanding and direction.

**Appendix mapping:**
- Old appendix A.1–A.3 (Overview, Document Creation Flow, Document Types) → SP-3 (reframed)
- Old appendix A.4–A.5 (Supplementary Materials listing, Guide) → SP-2 (navigation)

**Epistemic trace:** III_4.7.3_MHC_Tracing_SP_Reconception.md

**Source:** User (2026-03-02), developed in dialogue with Claude Sonnet 4.6

---

## Entry 6: Draft Revisions — SP Reconception Applied (2026-03-02)

**Action:** Three targeted edits to 6.2 of III_5.4.2_Section6_v3.md to apply the SP reconception.

**Edit 1:** Three-component paragraph — "reproduction testing" → "tracing assessment" (one word change; corrects framing)

**Edit 2:** SP table and core paragraph — replaced entirely:
- Table: new SP-1/SP-2/SP-3/SP-4/SP-5 roles per Entry 5
- Paragraph: removed reproduction-test operationalization; replaced with adequacy-argument framing (SP-3 as primary tracing claim; SP-4 as substance; SP-1 summarizes SP-3; SP-2 navigates)

**Edit 3:** Lloyd paragraph — updated to reflect new SP roles:
- SP-1 "extended: rather than merely noting AI involvement, it summarizes how AI was used"
- SP-3 (not SP-4) carries the replicability function: "extends replicability beyond prompt logging to a full account of the documentation system and the argument for its adequacy"

**File after edits:** III_5.4.2_Section6_v3.md (current)

