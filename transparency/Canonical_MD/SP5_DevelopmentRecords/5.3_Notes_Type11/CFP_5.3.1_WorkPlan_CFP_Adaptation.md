---
project: JPEP
document_type: Type 11 - Steering Note / Work Plan
label: CFP_5.3.1_WorkPlan_CFP_Adaptation
title: "Work Plan: CFP Adaptation for AI Tools in Ethics Research"
branch: cfp-ai-ethics-inquiry
date_created: 2026-03-02
status: Active
source: "Claude Code / Claude Opus 4.6 (analytical session) + user direction"
related:
  - "III_4.7.4_CFP_AIEthicsInquiry_BranchAndFitAnalysis.md (fit analysis)"
  - "III_5.4.1_Section3_v3.md (authoritative Section 3 draft)"
  - "III_5.4.2_Section6_v3.md (authoritative Section 6 draft)"
  - "target-venue/cfp_ai-ethics-inquiry.md (CFP text)"
  - "III_5.3.5_SteeringNote_v3_Section_Revisions.md (prior steering note)"
---

# Work Plan: CFP Adaptation for AI Tools in Ethics Research

---

## RESUME HERE (last updated 2026-03-17, session SID-20260317-191544)

**Immediate next action:** Draft Section 7 CFP adaptation (Phase 3).
Source: `Paper/MDversion/07_review_mechanism.md`
Plan: reframe from journal-specific review mechanism to community assessment of documentation adequacy. Drop reproduction test (already rejected). Reframe as: how should the scholarly community assess whether transparency documentation is adequate? Connect to Section 6's documentation-adequacy model.

**State summary:**
- Phase 1 complete — Introduction + Section 3 both revised post-finalization (first component/step cut; see CFP_4.7.7)
- Section 2 finalized — CFP_5.4.5_Section2_v3.md (~900 words); modlog CFP_4.2.15
- Section 4: cut (no standalone section)
- Section 5 finalized — CFP_5.4.7_Section5_v1.md (~1,350 words); modlog CFP_4.2.17 (9 entries); session SID-20260317-191544
- Section 6 finalized — CFP_5.4.8_Section6_v3.md (~1,520 words); modlog CFP_4.2.18 (13 entries); session SID-20260323-190000. Note: §6.1 substantially deepened with two-routes argument (process-constitutive + community-level essential contestedness); adverse selection paragraph added §6.3; §6.4 rewritten around AI-assisted synthesis as viability mechanism.
- Section 7: not started (Phase 3)

---

## HOW TO RESTART (mhc-start)

When the user types `mhc-start`, do the following in order:

1. **Read this file** in full. It is the master plan for the CFP adaptation.
2. **Read MEMORY.md** at `C:\Users\loimi\.claude\projects\C--Users-loimi-switchdrive-CURRENTLY-WORKING-ON-AI---assisted-papers-JPEP\memory\MEMORY.md` for project-wide instructions (especially: authoritative section drafts are in `5.4_SectionDrafts/`, NOT `Paper/MDversion/`).
3. **Check the progress checklist** (Section B below). Identify the next unchecked item.
4. **Run `git status` and `git branch`** on the working directory. Confirm you are on branch `cfp-ai-ethics-inquiry`. If not, switch to it.
5. **Read the source file** for the next section to be drafted (see Section C for locations).
6. **Follow the review protocol** (Section D) for that section.
7. **Follow the documentation protocol** (Section E) for artifact creation.

**Key directories:**
- Project root: `C:\Users\loimi\switchdrive\CURRENTLY WORKING ON\AI - assisted papers\JPEP\`
- Section drafts (v3 authoritative): `transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/`
- Section files (v1 baseline): `Paper/MDversion/`
- Modification logs: `transparency/Canonical_MD/SP4_ProcessDocumentation/4.2_ModificationLogs/`
- Epistemic traces: `transparency/Canonical_MD/SP4_ProcessDocumentation/4.7_EpistemicTraces/`
- Notes/steering: `transparency/Canonical_MD/SP5_DevelopmentRecords/5.3_Notes_Type11/`

---

## A. THE ARGUMENTATIVE SPINE (Introduction)

This is the core intellectual architecture for the CFP Introduction. It was developed through a multi-turn analytical session (2026-03-02) and must not be altered without the user's explicit approval. Any drafting agent must reproduce this structure faithfully.

### Move 1: Literature gap

AI in education is debated; AI in scientific research is discussed; AI in ethics research is almost unaddressed. But ethics is where the question is hardest, because what constitutes ethical inquiry is fundamentally disputed.

### Move 2: The cognitivist objection and its defeat (argumentative hinge)

**The objection:** If ethics tracks truth, evaluate the outputs. A sound argument is sound regardless of how it was produced. Process transparency confuses discovery with justification. This is the strongest objection to the paper's entire project.

**The defeat (revised 2026-03-11):**

> *Note: The original spine had a "first step" arguing that output-evaluation is process-dependent because "ethicists have no moral truth-meter." This was cut on Opus structural review (2026-03-11) as a non sequitur: the cognitivist objection turns on the discovery/justification distinction, not on epistemic access to moral reality. The "thinking quality" intuition behind it belongs in Section 6.1 where it is properly developed. The defeat now rests on a single move:*

(i) "Ethical inquiry" is an essentially contested concept (Gallie 1956). Competent practitioners disagree about its constitutive methods, its epistemic structure, and its purpose. The cognitivism/non-cognitivism dispute -- one of the most fundamental and unresolved disputes in metaethics -- is the deepest instance: we do not even agree on whether ethics is in the business of tracking truth. The cognitivist objection presupposes what is contested. Output-evaluation criteria in ethics are themselves contested, so the objection is question-begging.

(ii) The essentially-contested nature of ethics does double duty: it motivates transparency directly (we cannot prejudge what AI does to ethics, so we must track it) AND it defeats the cognitivist objection (we cannot "just evaluate outputs" because output-evaluation criteria in ethics are contested too).

(iii) Qualification: The claim is not that process information is always necessary for any ethical argument. For simple applied ethics arguments with clear premises and valid inferences, the output may suffice. The claim is: for complex work involving judgment, contested methods, and genuine philosophical insight -- where AI assistance is most consequential -- output-evaluation alone is insufficient. AI systems can produce outputs that satisfy surface criteria without the understanding those criteria are meant to track.

**Key methodological point:** Cognitivism is NOT asserted as a premise. The cognitivism/non-cognitivism dispute is used as an *illustration* of the essential contestedness of ethical inquiry. The argument is ecumenical: cognitivists, constructivists, and particularists all have reason to want process visibility, because each needs to assess whether the process satisfied the criteria *their* view identifies as constitutive of ethical inquiry.

### Move 3: The pivot to tracking

Since output-evaluation in ethics is process-dependent, and process criteria are contested, the achievable goal is tracking what ethics research is becoming under AI assistance. Tracking requires visibility. Visibility requires a philosophically specified transparency framework -- not merely a disclosure mandate.

### Move 4: Contribution announcement

This paper provides such a framework, grounded in Meaningful Human Control (Santoni de Sio & van den Hoven 2018) and operationalized through documentation-adequacy rather than reproduction. The paper demonstrates the framework: it implements the transparency apparatus it argues for.

### Dialectical structure summary

```
Gap: AI in ethics research unaddressed
     |
     v
Objection: "Just evaluate outputs" (cognitivist challenge)
     |
     v
Defeat: Ethical inquiry is essentially contested
        (cognitivism dispute = deepest instance)
        → output-evaluation criteria are themselves contested
        → cognitivist objection is question-begging
     |
     v
Pivot: Track what ethics is becoming -> transparency required
     |
     v
Contribution: MHC framework + documentation-adequacy + self-exemplification
```

### Citations required in the Introduction

- Gallie, W. B. (1956). Essentially contested concepts.
- Santoni de Sio, F., Faber, N. S., Savulescu, J., & Vincent, N. A. (2016). Why less praise for enhanced performance? (constitutive/regulative distinction)
- Santoni de Sio, F., & van den Hoven, J. (2018). Meaningful human control over autonomous systems. (MHC framework)
- At least 2-3 citations for the cognitivism/non-cognitivism dispute. Recommended: Enoch (2011) or Shafer-Landau (2003) for realism; Gibbard (1990) or Blackburn (1993) for non-cognitivism; van Roojen SEP entry as neutral survey. Characterize the dispute accurately but do not adjudicate it.

### Philosophical flags (must be addressed in drafting)

1. "Ethical inquiry" as essentially contested needs brief support under Gallie's criteria (appraisive, internally complex, variously describable, open, aggressive/defensive use). Do not merely assert it.
2. Section 3 must develop the cognitivist objection and its defeat more fully than the Introduction. The Introduction compresses; Section 3 develops.
3. The self-exemplification creates a reviewer problem: the CFP venue has no specialized review infrastructure for SP-1 through SP-5. Anticipate this.
4. "Tracking" risks quietism objection. Gesture toward: tracking creates the evidentiary basis for future normative judgments.
5. The framework is itself subject to the contestation it diagnoses. Acknowledge this (Section 6.3's experimental framing helps).

---

## B. PROGRESS CHECKLIST

### Phase 0: Setup
- [x] Branch created (`cfp-ai-ethics-inquiry` from `III-v3-mhc-revision` at 76435f2)
- [x] CFP text saved (`target-venue/cfp_ai-ethics-inquiry.md`)
- [x] Fit analysis complete (III_4.7.4)
- [x] Argumentative spine developed (this document)
- [x] Work plan created (this document)

### Phase 1: Introduction + Section 3 (priority — these carry the argument)
- [x] Draft Introduction (CFP_5.4.3_Introduction_v1.md)
- [x] Review Introduction (Reviewer A + Reviewer B)
- [x] Revise Introduction if needed (CFP_5.4.3_Introduction_v2.md, etc.)
- [x] Finalize Introduction (both reviewers approve)
- [x] Draft Section 3 adaptation (CFP_5.4.4_Section3_v1.md)
- [x] Review Section 3 (Reviewer A + Reviewer B)
- [x] Revise Section 3 if needed
- [x] Finalize Section 3 (both reviewers approve)
- [x] Create epistemic trace for Introduction development (CFP_4.7.5)

### Phase 2: Sections requiring reframing
- [x] Draft Section 2 compression (CFP_5.4.5_Section2_v1.md)
- [x] Review + finalize Section 2
- [ ] Draft Section 4 compression/cut (CFP_5.4.6_Section4_v1.md)
- [ ] Review + finalize Section 4
- [x] Draft Section 5 reframe (CFP_5.4.7_Section5_v1.md)
- [x] Review + finalize Section 5

### Phase 3: Sections requiring minor changes
- [x] Draft Section 6 minor reframe (CFP_5.4.8_Section6_v3.md)
- [x] Review + finalize Section 6
- [ ] Draft Section 7 minor reframe (CFP_5.4.9_Section7_v1.md)
- [ ] Review + finalize Section 7

### Phase 4: Conclusion, Abstract, Title
- [ ] Draft Conclusion rewrite (CFP_5.4.10_Conclusion_v1.md)
- [ ] Review + finalize Conclusion
- [ ] Draft Abstract rewrite (CFP_5.4.11_Abstract_v1.md)
- [ ] Review + finalize Abstract
- [ ] Draft Title revision
- [ ] Review + finalize Title

### Phase 5: Integration and documentation
- [ ] Integrate all finalized sections into single paper file
- [ ] Create modification logs for all adapted sections
- [ ] Final consistency review (full paper read-through)
- [ ] Commit finalized CFP version to branch

---

## C. SECTION-BY-SECTION PLAN

### Section 1: Introduction
- **Current state:** v1 in `Paper/MDversion/01_introduction.md`. Argues for a new venue/journal; uses Floridi hook, four structural gaps, journal-design framing.
- **Transformation:** Major rewrite. New argumentative spine (Section A above). Drop: four structural gaps, journal-design language, reproduction test references, Section 4 preview. Keep: transparency paradox reference (briefly, as motivation -- the full treatment stays in Section 2). Add: cognitivist objection/defeat, essentially-contested argument applied to ethics, cognitivism/non-cognitivism as illustration.
- **Source for drafter:** Do NOT use the v1 Introduction as a template. Draft from scratch using the spine in Section A. The v1 may be consulted for Floridi references and literature citations only.
- **Priority:** FIRST. Everything else depends on the Introduction setting the frame.
- **Word target:** 800-1200 words.

### Section 2: Systemic Barriers to Disclosure
- **Current state:** v1 in `Paper/MDversion/02_systemic_barriers_to_disclosure.md`. Detailed analysis of incentive gradients, underreporting mechanisms, institutional design constraints.
- **Transformation:** Compress. The transparency paradox and incentive analysis are background for the CFP version, not the main argument. Retain the core insight (disclosure is mandatory but penalized; underreporting increases with significance). Cut or compress: the four underreporting mechanisms (definitional flexibility, temporal discounting, comparative framing, strategic vagueness) -- keep one or two as illustration. Cut or compress: institutional design constraints (2.2) -- this argues for a new venue, which is not the CFP frame.
- **Source for drafter:** `Paper/MDversion/02_systemic_barriers_to_disclosure.md`
- **Priority:** Phase 2.
- **Word target:** 500-800 words (down from ~1500).

### Section 3: Why Engage with AI-Assisted Scholarship?
- **Current state:** v3 draft at `transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/III_5.4.1_Section3_v3.md`. Contains the essentially-contested argument, constitutive/regulative distinction, Gallie, tracking pivot.
- **Transformation:** Reframe for ethics (currently generic "philosophy"). Add new subsection: the cognitivist objection and its defeat (output-evaluation is process-dependent in ethics). This develops what the Introduction compresses. Add explicit connection to Section 6.1's claim that "article evaluation never assessed merely whether arguments are valid -- it always also assessed thinking quality." The v3 Section 3 currently goes straight from essentially-contested to tracking; it needs the intermediate step showing why "just evaluate the outputs" fails.
- **Source for drafter:** `transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/III_5.4.1_Section3_v3.md` (authoritative). Also read Section 6.1 in `III_5.4.2_Section6_v3.md` for the thinking-quality argument.
- **Priority:** SECOND (immediately after Introduction).
- **Specific additions:**
  - Between "Philosophy as Essentially Contested" and "From Answer to Tracking," insert a subsection (working title: "Why Output-Evaluation Fails in Ethics") that: (a) states the cognitivist objection; (b) shows that the essential contestedness of ethics makes output-evaluation criteria themselves contested — the objection is question-begging. (Note: the earlier "first step" — output-evaluation is process-dependent because ethicists have no moral truth-meter — was cut as a non sequitur on 2026-03-11. The defeat rests solely on essential contestedness.)
  - Throughout: replace "philosophy" with "ethics/ethical inquiry" where appropriate for CFP framing. Not mechanically -- some passages should remain about philosophy generally.
- **Word target:** 1200-1500 words (up from ~950).

### Section 4: The Dilemma Reconsidered
- **Current state:** v1 in `Paper/MDversion/04_the_dilemma_reconsidered_short_term_positioning_and_long_term_transformation.md`. Argues about prestige dynamics, long-term positioning outside prestige systems.
- **Transformation:** Compress heavily or cut. This section exists to argue the proposed journal is viable despite being outside prestige systems. The CFP version does not propose a journal. If retained, compress to 1-2 paragraphs acknowledging the institutional challenge without the full prestige-dynamics argument. Consider folding surviving content into Section 2 or Section 5.
- **Source for drafter:** `Paper/MDversion/04_the_dilemma_reconsidered_short_term_positioning_and_long_term_transformation.md`
- **Priority:** Phase 2. Decision on cut vs. compress to be made after Introduction and Section 3 are finalized (the Introduction frame will clarify how much institutional context is needed).
- **Word target:** 0-400 words.

### Section 5: Signaling Discontinuity from Prestige System
- **Current state:** v1 in `Paper/MDversion/05_signaling_discontinuity_from_prestige_system.md`. Contains: ecological validity, good faith orientation, costly signaling. Framed as venue-design principles.
- **Transformation:** Reframe from "venue design principles" to "design conditions for responsible AI-assisted ethics research." The three principles (ecological validity, good faith, costly signaling) are sound and transferable -- they become conditions any transparency framework must meet, not features of a particular journal. Drop venue-specific language.
- **Source for drafter:** `Paper/MDversion/05_signaling_discontinuity_from_prestige_system.md`
- **Priority:** Phase 2.
- **Word target:** 800-1200 words.

### Section 6: Mandatory Transparency in Practice
- **Current state:** v3 draft at `transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/III_5.4.2_Section6_v3.md`. Contains MHC integration, tracing/tracking conditions, documentation-adequacy model, SP-1 through SP-5 table, three nested concerns diagram, Lloyd engagement, experimental development, pilot observations.
- **Transformation:** Minor. This is the paper's strongest CFP contribution. Changes needed: (a) replace any remaining "journal" or "venue" language with "research practice" or "community" language; (b) ensure Section 6.1's thinking-quality argument explicitly connects to the Introduction's cognitivist-objection defeat; (c) verify consistency with documentation-adequacy model (no reproduction-test remnants).
- **Source for drafter:** `transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/III_5.4.2_Section6_v3.md` (authoritative).
- **Priority:** Phase 3.
- **Word target:** ~1400 words (roughly same as current).

### Section 7: Review Mechanism
- **Current state:** v1 in `Paper/MDversion/07_review_mechanism.md`. Contains dual-reviewer architecture, trajectory-matching reproduction test.
- **Transformation:** Reframe from journal-specific review mechanism to community assessment of documentation adequacy. Drop reproduction test (already rejected in v3 Section 6). Reframe as: how should the scholarly community assess whether transparency documentation is adequate? This connects to Section 6's documentation-adequacy model.
- **Source for drafter:** `Paper/MDversion/07_review_mechanism.md`. Also consult v3 Section 6 for documentation-adequacy framing.
- **Priority:** Phase 3.
- **Word target:** 800-1200 words.

### Section 8: Conclusion
- **Current state:** v1 in `Paper/MDversion/08_conclusion.md`. Oriented toward journal-creation proposal.
- **Transformation:** Rewrite. The conclusion must land on: responsible AI-assisted ethics research requires a philosophically specified transparency framework; this paper has provided and demonstrated one; the essentially-contested nature of ethical inquiry means we cannot prejudge outcomes but must track them; the community assessment mechanisms remain to be developed.
- **Source for drafter:** `Paper/MDversion/08_conclusion.md` (for structure reference only).
- **Priority:** Phase 4.
- **Word target:** 400-600 words.

### Abstract and Title
- **Transformation:** Rewrite last, after all sections are finalized. The abstract must reflect the CFP framing, not the JPEP journal-creation framing. Title should signal: transparency + AI-assisted ethics research + methodology.
- **Priority:** LAST.

---

## D. REVIEW PROTOCOL

### Roles

- **Drafter:** Sonnet agent (working within the Claude Code session). Produces section drafts following the instructions in Section C. The drafter reads the source file, reads this work plan, and drafts the adapted section.
- **Reviewer A:** The user (human). Reviews each draft for philosophical accuracy, argumentative integrity, and alignment with the author's intentions.
- **Reviewer B:** Opus agent (within the same Claude Code session, or resumed). Reviews each draft against the criteria below.

### Review criteria (both reviewers assess all of these)

1. **Argumentative spine:** Does the draft follow the argumentative structure specified in this plan? (For the Introduction: does it execute Moves 1-4? For Section 3: does it include the cognitivist objection and defeat?)
2. **CFP framing:** Is the draft oriented toward "AI tools in ethics research" rather than toward journal-creation/venue-design?
3. **Philosophical defensibility:** Are the philosophical moves sound? Are claims supported? Are qualifications present where needed?
4. **Consistency with other sections:** Does the draft use the same terminology and conceptual framework as other finalized sections? (Especially: documentation-adequacy, not reproduction test; tracing condition; essentially contested concept; tracking.)
5. **Concision:** Does the draft meet its word target? Is there padding or repetition?

### Workflow per section

```
1. Session reads this plan, identifies next section
2. Drafter reads source file(s) for that section
3. Drafter produces draft -> saved as CFP_5.4.X_SectionName_v1.md
4. Reviewer B (Opus) reviews draft against criteria 1-5
5. Reviewer B assessment presented to user
6. User (Reviewer A) reads draft and Reviewer B assessment
7. User responds:
   - "approve" -> section finalized, committed, modification log created
   - "revise: [specific instruction]" -> drafter revises, new version saved
     as CFP_5.4.X_SectionName_v2.md, return to step 4
   - User may also provide own assessment before approving/requesting revision
8. Section finalized only when BOTH reviewers approve
```

### How Reviewer B (Opus) is invoked

Reviewer B operates within the same session. When a draft is ready for review, the session should:

1. Read the draft file
2. Read this work plan (specifically Section A for the argumentative spine, Section C for the section-specific instructions, and Section D for review criteria)
3. Produce a structured assessment with one paragraph per criterion (1-5 above)
4. End with a verdict: APPROVE, or REVISE with specific instructions

If the session is new (no prior Opus context), the work plan is self-contained. The reviewer needs only this document and the draft to assess.

### How Reviewer A (user) registers decisions

The user types one of:
- `approve` -- section is finalized
- `revise: [instruction]` -- e.g., `revise: Move 2 needs the qualification about simple applied ethics arguments`
- The user may also type extended comments before a decision

### Revision history

Every draft version is preserved:
- v1, v2, v3, etc. in `5.4_SectionDrafts/` with sequential numbering
- Reviewer comments are preserved in the modification log for that section (created at finalization)
- If a section goes through multiple revision rounds, the modification log records each round: what was requested, what changed

---

## E. DOCUMENTATION PROTOCOL

### Artifact types and locations

| Artifact type | Naming convention | Location |
|---|---|---|
| Type 12: Section Draft | `CFP_5.4.{N}_SectionName_v{M}.md` | `SP5_DevelopmentRecords/5.4_SectionDrafts/` |
| Type 3: Modification Log | `CFP_4.2.{N}_ModificationLog_SectionName.md` | `SP4_ProcessDocumentation/4.2_ModificationLogs/` |
| Type 2: Epistemic Trace | `CFP_4.7.{N}_Description.md` | `SP4_ProcessDocumentation/4.7_EpistemicTraces/` |
| Type 11: Steering Note | `CFP_5.3.{N}_Description.md` | `SP5_DevelopmentRecords/5.3_Notes_Type11/` |

### Numbering

Section draft numbers (Type 12) continue from the existing sequence:
- III_5.4.1 = Section 3 v3
- III_5.4.2 = Section 6 v3
- CFP_5.4.3 = Introduction (first CFP draft)
- CFP_5.4.4 = Section 3 CFP adaptation
- CFP_5.4.5 = Section 2 CFP adaptation
- CFP_5.4.6 = Section 4 CFP adaptation
- CFP_5.4.7 = Section 5 CFP adaptation
- CFP_5.4.8 = Section 6 CFP adaptation
- CFP_5.4.9 = Section 7 CFP adaptation
- CFP_5.4.10 = Conclusion CFP adaptation
- CFP_5.4.11 = Abstract CFP adaptation

Modification log numbers continue from III_4.2.13:
- CFP_4.2.14 = Introduction modification log
- CFP_4.2.15 = Section 2 modification log
- (etc., sequential)

Epistemic trace numbers continue from III_4.7.4:
- CFP_4.7.5 = Introduction argumentative development trace (documents the analytical session that produced the spine in Section A)

### What each artifact must contain

**Section Draft (Type 12) header:**
```yaml
---
project: JPEP
document_type: Type 12 - Section Draft
section: "[section name]"
version: "[vN] (CFP adaptation)"
date_created: [date]
status: Draft | Under Review | Finalized
source: "[agent model]"
source_guidance: "CFP_5.3.1_WorkPlan_CFP_Adaptation.md"
cfp_target: "AI Tools in Ethics Research (topical collection)"
word_count: ~[N]
---
```

**Modification Log (Type 3) must document:**
- What the JPEP version contained
- What the CFP version changed
- Why the change was made (link to CFP fit analysis and argumentative spine)
- Reviewer comments that led to revisions (if any)

**Epistemic Trace (Type 2) for the Introduction must document:**
- The analytical session (2026-03-02) that developed the argumentative spine
- The key intellectual moves: cognitivism as illustration (not premise), the cognitivist objection and its defeat, the essentially-contested argument applied to ethics
- The dialectical development: how Ideas 1 and 2 were synthesized through the user's insight that cognitivism is itself an essentially contested feature of ethics

### Git workflow

- All work happens on branch `cfp-ai-ethics-inquiry`
- Commit after each section is finalized (both reviewers approve)
- Commit message format: `CFP adaptation: [section name] finalized`
- Update `_INDEX_5.4.md` after each new section draft is added

---

## F. REFERENCE: CFP FIT ANALYSIS SUMMARY

From III_4.7.4 (corrected Phase 3 analysis):

| Paper section | CFP fit | Action |
|---|---|---|
| 1. Introduction | Partial -- journal-creation frame is JPEP-specific | **Rewrite** (spine in Section A) |
| 2. Systemic barriers | Background; not CFP's focus | **Compress** |
| 3. Why engage (v3) | Strong for "implications for ethics"; gap on methods | **Reframe + add cognitivist defeat** |
| 4. Dilemma/prestige | Weakest fit | **Compress or cut** |
| 5. Discontinuity/design | Moderate | **Reframe** (venue -> research practice) |
| 6. Mandatory transparency (v3) | Strongest contribution | **Keep, minor reframe** |
| 7. Review mechanism | Good | **Minor reframe** (journal -> community) |
| 8. Conclusion | Needs reorientation | **Rewrite** |

### Key CFP questions addressed by the adapted paper

| CFP question | Where addressed |
|---|---|
| What tasks can AI support in ethics? | Section 3 (implicitly, via tracking argument) |
| Which uses involve special risks? | Section 6 (opacity as epistemic risk) |
| What goods are lost? | Section 6.1 (attribution, guided thought, thinking quality) |
| Discovery vs. justification? | Section 6.1 (rejection of the binary) |
| Implications for ethics as a field? | Introduction + Section 3 (essentially-contested argument) |
| Could AI be an ethics expert? | Section 6 (tracing condition -- only if outputs trace to understanding) |
| Might AI help us understand our methods? | Section 3 (tracking what ethics is becoming) |

### Main gap remaining

Ethics-specific methods content (reflective equilibrium, casuistry, moral intuitions, thought experiments). The adapted paper does not contain detailed analysis of what AI can/cannot support for specific ethics methods. This is acknowledged as a gap. Options: (a) add a short subsection in Section 3; (b) acknowledge the gap and frame the paper as addressing the prior question (what framework do we need before we can assess method-specific impacts?). Option (b) is recommended -- it is honest and positions the paper correctly.

---

*End of work plan.*
