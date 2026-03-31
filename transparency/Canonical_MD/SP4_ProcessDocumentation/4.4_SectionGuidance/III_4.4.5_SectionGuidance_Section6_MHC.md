---
project: JPEP
document_type: Type 4 - Section Guidance
section: "VI - Mandatory Transparency in Practice (MHC Integration)"
version: III (Post-arXiv v2 revision cycle)
date_created: 2026-01-26
date_last_updated: 2026-01-28
status: Ready for Drafting (Revised)
source: "Claude Code (no chat ID)"
source_pdl: "III_5.2.1_pdl_sections_3_and_6_MHC_integration.md"
constraint: "Self-sufficient prompt with pointers to source documents for drafting AI"
target_length: "1200-1500 words"
revision_note: "Updated after failed first draft (2026-01-28). Existing Section 6 reading now MANDATORY. Added hard constraints on existing content. Restructured to specify keep/modify/add."
inputs_for_drafting_ai:
  - "This document (self-sufficient prompt)"
  - "Paper/MDversion/Full paper2511.08639v1.md — MANDATORY: read current Section 6 (all subsections 6.1-6.4) IN FULL before drafting"
  - "transparency/TEMP/Santoni_de_sio_frobt-05-00015.xml (optional - for direct quotes on tracking/tracing)"
  - "transparency/TEMP/Lloyd_frai-08-1635691.xml (optional - for engagement with Lloyd's standards)"
---
# Section Guidance: Section 6 - Mandatory Transparency in Practice

## SIGNIFICANT REVISION - Stage III (NOT a complete rewrite)

**Target length:** 1200-1500 words

**Core task:** Revise Section 6 to explicitly ground the paper's transparency requirements in the **Meaningful Human Control (MHC)** framework. The section operationalizes the meta-philosophical goal established in Section 3: if we cannot settle whether AI changes philosophy, we must at least ensure that whatever is produced remains *traceable* to human intellectual agency.

> **CRITICAL INSTRUCTION:** This is a REVISION of the existing Section 6, not a blank-slate rewrite. The drafting AI MUST read the current Section 6 (subsections 6.1-6.4) in `Paper/MDversion/Full paper2511.08639v1.md` before drafting. The existing content contains philosophical arguments, structural decisions, and specific formulations that must be preserved or built upon. A draft produced without reading the existing version will be defective.

---

## Hard Constraints: Existing Content to Preserve

The following elements from the v1 Section 6 are **hard constraints** — they must be retained or integrated, not replaced:

### SP-1 through SP-5: Fixed Framework

The transparency apparatus (SP-1 through SP-5) as specified in v1 is a **hard constraint** on the entire paper. The revision grounds this apparatus in MHC — it does not redesign, rename, or restructure it. Any reference to SP-1 through SP-5 must match the v1 specification.

### From 6.1 (From Principles to Practice) — KEEP and BUILD ON
- **Discovery/justification framework critique:** The rejection of Reichenbach's binary and the argument that article evaluation assesses thinking quality, not just validity
- **Traditional philosophical values:** Guided thought, intellectual honesty, methodological self-consciousness — and the specific examples (Williams, Cavell, Nozick, Lewis)
- **Attribution argument:** "When reading excellent philosophy, you must know whose thought you're following to learn from the example" — opacity destroys this even without fraud
- **Connection to Section 5 design principles:** Ecological validity, good faith orientation, cost structure through costly signaling
- **What the section explicitly does NOT argue:** Not from moral desert, not from economic necessity, not that traditional venues should adopt these practices

### From 6.2 (The Transparency Framework) — KEEP and EXTEND
- **Three functions of disclosure:** Verification, methodological learning, preservation of traditional philosophical values
- **Three-component structure:** Model/process information; representative prompts/outputs; process narrative
- **Concrete implementation:** The paper itself as demonstration (complete prompt, conversation excerpts, process documentation)
- **Accessibility emphasis:** No technical expertise required; documentation is text files and reflective writing

### From 6.3 (Experimental Development) — KEEP
- **Evolutionary framing:** Requirements as sketch requiring experimentation, not prescription
- **Community convergence:** Practices may vary by philosophical subfield
- **Level 2 orientation:** Serving philosophers doing philosophy, not technical specialists

### From 6.4 (Pilot observations) — KEEP
- **Practical constraints discovered:** Lack of timestamps in LLM platforms; synthesis risks post-hoc rationalization
- **Templates not protocols:** Artifacts as scaffold for documentation habits

---

## What the Revision ADDS

The MHC framework provides philosophical grounding for the existing apparatus. The revision should:

1. **Add MHC as the theoretical foundation** — explain WHY the existing transparency requirements take the form they do (answer: they operationalize the tracing condition for meaningful human control)
2. **Reframe the existing transparency apparatus through MHC** — show how SP-1 through SP-5 each serve the tracking/tracing conditions
3. **Add engagement with Lloyd (2025)** — adopt Standards 1-2, reject Standard 4 (text demarcation)
4. **Make explicit the three nested concerns** — epistemic integrity, tracing, tracking what philosophy becomes

---

## Connection to Section 3

Section 3 establishes:
- Philosophy is an essentially contested concept
- Whether AI changes philosophy cannot be settled without settling what philosophy is
- The achievable goal is *tracking what philosophy becomes*
- This requires transparency

**Section 6's role:** Answer the question *what kind of transparency?* The answer: transparency that satisfies the **tracing condition** for meaningful human control.

---

## The MHC Framework (Core Conceptual Content)

### Source: Santoni de Sio & van den Hoven (2018)

The MHC framework was developed for autonomous weapons systems but transfers structurally to AI-assisted scholarship. It identifies **two necessary conditions** for meaningful human control:

#### 1. The Tracking Condition

**Definition:** The system's behavior must *covary* with relevant human moral reasons. The system must be responsive to the reasons of the humans deploying it.

**Derived from:** Fischer & Ravizza's "reason-responsiveness" + Nozick's tracking theory of knowledge.

**For AI-assisted scholarship:** Does the AI output track the author's intended arguments, commitments, and constraints? Is the system responsive to the author's intellectual direction?

**What satisfies tracking:**
- Explicit specification of argumentative goals before generation
- Iterative refinement where author corrects AI drift
- Documentation showing responsiveness to author direction

#### 2. The Tracing Condition

**Definition:** The system's actions/outputs must be *traceable* to proper understanding and endorsement by some human person—designer, controller, user.

**The critical insight (quote for use):**
> "Systems whose actions and states are not traceable to relevant understanding and endorsing by some human person—be they a designer, a controller, a user, etc.—no matter how intelligent and reason-responsive they may be, are not under meaningful human control. They would be like human actions carried out under psychological manipulation, subliminal persuasion, brainwashing, and indoctrination." (Santoni de Sio & van den Hoven, 2018, §6.2)

**For AI-assisted scholarship:** Can the intellectual contribution be traced to a human who:
1. **Understood** what the AI system could and could not contribute
2. **Understood** what they themselves were contributing
3. **Can explain, defend, and own** the resulting argument

**What satisfies tracing:**
- Process documentation showing human decision points
- Ability to reconstruct intellectual trajectory from documented inputs
- Author capable of defending argumentative moves

---

## The Tracing Condition as the Key Requirement

### Why Tracing Matters More Than Tracking

Both conditions are necessary, but **tracing** is the distinctive challenge for scholarship:

- Tracking is relatively easy to satisfy: if the author iterates with the AI, the output will generally track their intentions
- Tracing is harder: even with tracking, the author might not *understand* what was produced well enough to own it

**The parallel to weapons:**
A soldier might press a button that causes a drone strike (tracking—the system did what was commanded). But if the soldier didn't understand *what the weapon would do* or *what the consequences would be*, tracing fails. The action cannot be properly attributed to the soldier's agency.

**For scholarship:**
A scholar might prompt an AI to produce an argument (tracking—the AI followed the prompt). But if the scholar cannot *explain why that argument works*, *defend it against objections*, or *identify its commitments*, tracing fails. The intellectual contribution cannot be properly attributed to the scholar's agency.

---

## Operationalizing Tracing: The Paper's Transparency Requirements

### The Reproduction Test as Tracing Verification

**The key move:** The paper's proposed "reproduction test" (Section 7) operationalizes the tracing condition.

**The test:** Can a reviewer, given only the documented human inputs (prompts, guidance, iterative corrections), reproduce the intellectual trajectory of the work?

**What this verifies:**
- If YES: The author's documented inputs were *sufficient* to generate the work's intellectual architecture. The trajectory traces to human direction.
- If NO: Either documentation is incomplete, OR the tracing condition is not satisfied (the work contains intellectual moves that cannot be traced to human understanding).

**This is not about identical outputs.** Different AI systems or runs will produce different text. The test is whether the *intellectual architecture*—the argumentative structure, key moves, and commitments—can be regenerated from what the human documented.

### How the Transparency Apparatus (SP-1 through SP-5) Serves Tracing

| Transparency Element | What It Documents | How It Serves Tracing |
|---------------------|-------------------|----------------------|
| **SP-1: Declaration** | That AI was used | Signals tracing assessment is needed |
| **SP-2: Tool Specification** | Which AI systems, when | Enables reproduction attempts |
| **SP-3: Contribution Summary** | What AI contributed | Identifies what must be traceable |
| **SP-4: Process Documentation** | Prompts, iterations, decision points | The *substance* of tracing verification |
| **SP-5: Development Records** | Full interaction history | Enables deep tracing assessment |

**SP-4 is the core.** It provides the material against which tracing is assessed. Without process documentation, tracing cannot be verified—we have only the author's claim that they understood and directed the work.

---

## Engagement with Lloyd (2025): Partial Adoption

### Lloyd's Four Standards

Dan Lloyd (2025) proposes four standards for AI-assisted scholarship:

1. **Prominence** - AI use immediately apparent (title/header)
2. **Replicability** - Prompts documented; evolution recorded
3. **Content cross-checking** - Human verifier for AI factual claims
4. **Intra-textual clarity** - AI-generated text demarcated via style markers

### Our Position

| Lloyd's Standard | Our Response |
|------------------|--------------|
| Prominence | **Adopt** - SP-1 serves this function |
| Replicability | **Adopt and extend** - SP-4 goes deeper than prompt logging |
| Content cross-checking | **Implicit** - standard scholarly responsibility |
| Intra-textual clarity | **Reject** |

### Why We Reject Intra-Textual Demarcation

Lloyd's Standard 4 requires marking which text was AI-generated versus human-written. We reject this because:

1. **It assumes a primitive model of AI assistance.** Real workflows involve iterative refinement where "AI text" and "human text" blur. A sentence might be AI-generated, human-edited, AI-revised, and human-finalized. What is it?

2. **It cannot anticipate what the salient human input is.** Some papers might be "entirely AI-outputted" yet reflect enormous human input (conceptual architecture, iterative shaping, quality control). Others might be "mostly human-written" with AI contributing a crucial insight. Text-level demarcation doesn't capture this.

3. **The very category of "human contribution" is evolving.** We do not know what AI-assisted philosophical skills will look like. Initially, practice focuses on *prompting*—formulating queries. But it is already evolving toward *steering*—iteratively guiding AI through argumentative terrain. Perhaps philosophers will become *architecture builders*—designing intellectual structures that AI populates. As practice evolves from prompting to steering to architecture (or something unimagined), the nature of the "human contribution" shifts radically. Text demarcation presupposes we know where to draw the line. We do not.

4. **Process documentation is more fundamental.** What matters is not which sentences came from where, but whether the intellectual trajectory is traceable to human understanding. SP-4 (process documentation) captures *whatever* the human contribution turns out to be—without presupposing its form. Text marking cannot do this.

**The point:** Transparency should verify *tracing*, not *provenance of sentences*.

---

## Three Nested Concerns

Section 6 should make explicit that three concerns are nested:

```
OUTERMOST: Track what philosophy becomes
    |
    +-- MIDDLE: Ensure meaningful human control (tracing condition)
            |
            +-- INNERMOST: Maintain epistemic integrity
```

- **Epistemic integrity** (knowledge claims are trustworthy, confabulation controlled) is necessary but not sufficient
- **Tracing** (contributions attributable to human understanding) builds on epistemic integrity
- **Tracking what philosophy becomes** (the meta-philosophical goal) requires tracing to be verifiable

---

## The Argumentative Structure for Section 6 (Revised)

### 6.1 From Principles to Practice — REVISE
- **Keep** the existing philosophical values discussion (guided thought, attribution, intellectual honesty, Williams/Cavell/Nozick/Lewis examples)
- **Keep** the discovery/justification critique
- **Keep** what the section does NOT argue
- **Add** connection to Section 3's essentially contested framing: these values require transparency, and MHC specifies what transparency must verify
- **Add** MHC framework introduction: tracking and tracing conditions
- **Add** why tracing is the distinctive challenge (weapons parallel)

### 6.2 The Transparency Framework — REVISE
- **Keep** the three functions of disclosure and the three-component structure
- **Keep** the concrete implementation (this paper as demonstration)
- **Keep** accessibility emphasis
- **Add** explicit mapping of SP-1 through SP-5 to tracing verification (table)
- **Add** reproduction test framed as tracing verification
- **Add** engagement with Lloyd (adopt Standards 1-2, reject Standard 4)

### 6.3 Experimental Development — KEEP (minor adjustments only)
- **Keep** evolutionary framing, community convergence, Level 2 orientation
- Minor updates for consistency with MHC language if needed

### 6.4 Pilot observations — KEEP (minor adjustments only)
- **Keep** practical constraints, templates-not-protocols framing
- Minor updates for consistency if needed

### NEW: Three Nested Concerns (integrate into 6.1 or 6.2)
- Epistemic integrity -> Tracing -> Tracking what philosophy becomes
- Everything is instrumental to the meta-philosophical goal

---

## Key References to Cite

1. **Santoni de Sio, F., & van den Hoven, J. (2018).** "Meaningful Human Control over Autonomous Systems: A Philosophical Account." *Frontiers in Robotics and AI*, 5, 15.
   - Use for: tracking/tracing conditions; the key quote on tracing

2. **Lloyd, D. (2025).** "Epistemic responsibility: toward a community standard for human-AI collaborations." *Frontiers in Artificial Intelligence*, 8, 1635691.
   - Use for: engagement with four standards; justify divergence on Standard 4

3. *Optional:* **Fischer, J. M., & Ravizza, M. (1998).** *Responsibility and Control: A Theory of Moral Responsibility.* Cambridge University Press.
   - Use for: background on guidance control (only if needed for depth)

---

## What This Section Does NOT Do

- Does NOT re-argue why we need transparency (Section 3 did this)
- Does NOT present the reproduction test in detail (Section 7 does this)
- Does NOT discuss specific artifacts or file structures (appendices do this)
- Does NOT adjudicate whether AI changes philosophy (explicitly impossible per Section 3)
- Does NOT redesign or restructure SP-1 through SP-5 (hard constraint from v1)

---

## Connections to Other Sections

| Section | Relationship |
|---------|-------------|
| Section 3 | Establishes meta-philosophical goal; Section 6 operationalizes it |
| Section 5 | [Design principles - may need coordination] |
| **Section 6** | **Grounds transparency in MHC; introduces tracing condition** |
| Section 7 | Reproduction test as tracing verification (forward reference) |
| Appendices | Specific artifacts (SP-1 through SP-5) |

---

## Tone and Style Notes

- Philosophical but practical
- The MHC framework should feel like a *resource* for thinking, not imposed jargon
- The Lloyd engagement should be collegial (adopt where possible, explain divergence respectfully)
- Avoid bureaucratic tone—transparency serves intellectual goals, not compliance

---

## Draft Checklist

Before finalizing, verify:

- [ ] **Read the existing Section 6 (6.1-6.4) in full before drafting**
- [ ] Preserves existing philosophical arguments from 6.1 (values, attribution, discovery/justification critique)
- [ ] Preserves SP-1 through SP-5 exactly as specified in v1
- [ ] Preserves three functions of disclosure and three-component structure from 6.2
- [ ] Preserves evolutionary framing from 6.3 and pilot observations from 6.4
- [ ] Opens by connecting to Section 3's meta-philosophical goal
- [ ] Introduces MHC framework (tracking and tracing)
- [ ] Explains why tracing is the key challenge for scholarship
- [ ] Uses weapons parallel to make tracing concrete
- [ ] Includes Santoni de Sio & van den Hoven quote on tracing
- [ ] Presents reproduction test as tracing verification
- [ ] Shows how SP-1 through SP-5 serve tracing (table helpful)
- [ ] Engages Lloyd's four standards
- [ ] Adopts Standards 1-2, rejects Standard 4 with explanation
- [ ] Notes evolving skills (prompting -> steering -> architecture) as reason process documentation beats text demarcation
- [ ] Makes explicit the three nested concerns
- [ ] Forward references Section 7 for reproduction test details
- [ ] Cites Santoni de Sio & van den Hoven (2018) and Lloyd (2025)
- [ ] Does NOT re-argue need for transparency
- [ ] Does NOT present reproduction test in detail
- [ ] Approximately 1200-1500 words

---

## Source Documents for Drafting AI

### MANDATORY Reading

1. **Current Section 6 (MUST READ BEFORE DRAFTING):**
   `Paper/MDversion/Full paper2511.08639v1.md`
   - Read ALL of Section 6 (subsections 6.1 through 6.4)
   - Identify content to preserve, content to extend, and where new material fits

### Optional Reading (for deeper context)

2. **For MHC framework details:**
   `transparency/TEMP/Santoni_de_sio_frobt-05-00015.xml`
   - Sections on "Tracking" and "Tracing" contain the core framework
   - Section 6.2 has the key quote

3. **For Lloyd's standards:**
   `transparency/TEMP/Lloyd_frai-08-1635691.xml`
   - Body contains the four standards with justifications

4. **For prior MHC transfer work:**
   `transparency/Canonical_MD/SP4_ProcessDocumentation/4.7_EpistemicTraces/III_4.7.1_Reasonable_Human_Control_in_AI.md`
   - Already completed transfer of MHC to AI-assisted writing (operational checklist)

5. **For PDL development history:**
   `transparency/Canonical_MD/SP5_DevelopmentRecords/5.2_SectionPromptDevelopmentLogs_Type8b/III_5.2.1_pdl_sections_3_and_6_MHC_integration.md`

---

## Revision History

| Date | Change | Reason |
|------|--------|--------|
| 2026-01-26 | Original guidance created | Phase 3 preparation |
| 2026-01-28 | Major revision: added hard constraints, mandatory reading, keep/modify/add structure | First draft (III_5.4.2_Section6_v3.md) was defective — produced without reading existing Section 6, resulting in blank-slate rewrite that lost existing philosophical arguments and structural decisions |
## Connections (auto)

_No connections found._

