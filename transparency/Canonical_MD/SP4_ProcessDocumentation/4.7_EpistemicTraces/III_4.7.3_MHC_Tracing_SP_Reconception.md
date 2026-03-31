---
project: JPEP
document_type: Type 2 - Epistemic Trace
label: III_4.7.3_MHC_Tracing_SP_Reconception
title: "MHC Tracing Condition and SP Structure Reconception"
date: 2026-03-02
source: Claude Code session (Claude Sonnet 4.6)
status: Complete
influence: "One-to-many — affects Section 6 draft, Section 7 revision (pending), appendix revision (pending), section guidance III_4.4.5"
related:
  - "III_4.7.1_Reasonable_Human_Control_in_AI.md (MHC source analysis)"
  - "III_5.4.2_Section6_v3.md (revised Section 6 draft)"
  - "III_4.4.5_SectionGuidance_Section6_MHC.md (guidance — needs update)"
  - "appendix.md (A.1–A.3 → SP-3; A.4–A.5 → SP-2)"
---
# MHC Tracing Condition and SP Structure Reconception

## Origin

This trace documents a conceptual development that emerged during the Section 6 v3 drafting session (2026-03-02). The immediate trigger was a close reading of the SP table in the draft, which prompted the question: what does "enables reproduction attempts" actually mean as a function of SP-2 under the tracing condition?

The question opened a larger problem with the reproduction test as the operationalization of MHC tracing.

---

## The Problem with the Reproduction Test

The original Section 7 framework proposed a **reproduction test**: given only the documented human inputs (prompts, guidance, iterative corrections), can a reviewer reproduce the intellectual trajectory of the work? The test was framed as the operationalization of the MHC tracing condition.

Three problems emerged:

**1. Technological infeasibility.** AI systems are updated, deprecated, and replaced. A paper may take months or years to produce; by the time it is reviewed, the system used may no longer be accessible in its original form. Non-deterministic outputs mean the same system with the same prompt yields different results. The test cannot be reliably conducted.

**2. Time-scale of scholarship.** Good philosophical work is slow. The pace of AI development means the technological context at writing time will not be recoverable at review time. The test presupposes a stability that scholarly timelines cannot guarantee.

**3. The romantic author assumption.** The reproduction test implicitly assumes that the human author's inputs *uniquely determine* the intellectual contribution — that the same prompts through the same system would yield "the same" argument. This overstates what documentation can establish. It romanticizes the human author as the source of a special, reproducible insight, when in fact other prompts might generate comparable intellectual architecture, and the "intellectual architecture" is partly a function of how readers perceive the text.

---

## The Reconception: Documentation Adequacy

The tracing condition (Santoni de Sio & van den Hoven 2018) says outputs must be *traceable to* proper understanding and endorsement by some human person. Tracing does not require re-enacting or reproducing the process. It requires that the process is documented well enough that a reader can follow the intellectual thread back to human decision points.

This suggests a different operationalization: not **reproducibility** but **documentation adequacy**.

The question is no longer:
> Could the documented inputs reproduce this work?

But:
> Does the documentation adequately show how the intellectual trajectory traces to human understanding and direction?

What counts as "adequate" is a matter of judgment, not a pass/fail test. The burden falls on the author (in SP-3) to explain the documentation system and make the case for its adequacy. Reviewers, editors, and readers assess that case.

---

## The SP Structure Reconception

This reconception requires revising the SP roles:

### Old structure (reproduction-test oriented)
- **SP-1**: Declaration that AI was used
- **SP-2**: Reproduction Package — processed compilation to support the test
- **SP-3**: Reproduction Guide — instructions for running the test
- **SP-4**: Process Documentation
- **SP-5**: Development Records

### New structure (documentation-adequacy oriented)
- **SP-1**: Declaration summarizing *how* AI was used — a concise account pointing to SP-3 for the full version
- **SP-2**: Navigation document — structured index enabling access to SP-3, SP-4, and SP-5; makes the documentation system legible
- **SP-3**: Documentation account — detailed explanation of how AI was used, how the documentation system works, and the argument for its adequacy; references SP-4 and SP-5 for underlying materials
- **SP-4**: Process Documentation — unchanged in substance; primary material against which SP-3's adequacy claim is assessed
- **SP-5**: Development Records — unchanged in substance; enables deeper tracing of intellectual direction

### The hierarchy for a reader/reviewer
```
SP-1 (summary of how AI was used)
    |
    → SP-2 (navigation)
            |
            → SP-3 (full documentation account + adequacy argument)
                    |
                    → SP-4 (process documentation)
                    → SP-5 (development records)
```

SP-1 summarizes SP-3. SP-2 navigates to SP-3 (and onward). SP-3 is the primary tracing claim.

---

## Connection to the Appendix

The old appendix structure maps onto the new SP roles as follows:

| Old appendix section | New SP role |
|---------------------|-------------|
| A.1 Overview of Reproduction Procedure | → SP-3 (reframed: documentation system + adequacy argument) |
| A.2 Document Creation Flow | → SP-3 |
| A.3 Document Types | → SP-3 |
| A.4 This Article's Supplementary Materials | → SP-2 (navigation/index) |
| A.5 Guide to Using Supplementary Materials | → SP-2 |

In the appendix revision, A.1–A.3 will be reframed: the reproduction-test framing throughout A.1 is dropped; the content becomes an explanation of the documentation system and the adequacy argument. A.4–A.5 become the navigation layer (SP-2).

---

## Lloyd Engagement: Update

Under the new structure:
- SP-1 serves Lloyd's **prominence** standard, now extended: rather than merely noting AI involvement, it summarizes how AI was used
- SP-3 serves Lloyd's **replicability** standard, extended: a full account of the documentation system and the argument for its adequacy goes beyond prompt logging

The rejection of Lloyd's **Standard 4** (intra-textual demarcation) is strengthened: the adequacy-argument model makes the case for process documentation over text demarcation even more directly. What matters is not which sentences came from where, but whether SP-3 can make a credible case for tracing. Text demarcation is irrelevant to that case.

---

## Downstream Implications

1. **Section 6 draft** (III_5.4.2_Section6_v3.md) — revised in this session. SP table updated; reproduction test removed; SP-3 adequacy-argument framing introduced.

2. **Section 7** (Review Mechanism) — needs separate revision. Currently describes the reproduction test in detail (7.1–7.5). The review mechanism needs to be reconceived around documentation-adequacy assessment rather than reproduction. **Pending.**

3. **Appendix** — A.1–A.3 need reframing from reproduction-test orientation to documentation-adequacy orientation. A.4–A.5 become SP-2 as described above. **Pending.**

4. **Section Guidance III_4.4.5** — written before this reconception; references reproduction test and the old SP structure. Should be updated for completeness. **Low priority** (the draft already reflects the new conception).

---

## Key Formulation (for use in Section 6 and elsewhere)

> Rather than a reproduction test — which would require running documented inputs through a comparable AI system, and which proves unworkable given model deprecation, non-deterministic outputs, and the time-scale of scholarly production — SP-3 takes a different approach. It does not ask *could the documented inputs reproduce this work?* but *does the documentation adequately show how the intellectual trajectory traces to human understanding and direction?*


## Connections (auto)

_No connections found._
