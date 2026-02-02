---
project: JPEP
document_type: Type 12 - Section Draft
section: "6 - Mandatory Transparency in Practice"
version: v3 (Stage III revision)
date_created: 2026-01-28
status: Draft
source: "Claude Code / Claude Opus 4.5"
source_guidance: "III_4.4.5_SectionGuidance_Section6_MHC.md"
target_location: "Paper/MDversion/Full paper2511.08639v3.md"
word_count: ~1400
---

# Section 6: Mandatory Transparency in Practice

## From Meta-Philosophy to Operational Requirements

Section 3 argued that we cannot settle whether AI changes philosophy, because "philosophy" is an essentially contested concept—what counts as doing philosophy is itself philosophically disputed. The achievable goal is more modest: to track what philosophy is becoming by ensuring that AI-assisted work is produced with sufficient transparency for the scholarly community to observe, compare, and evaluate different modes of philosophical production.

But what kind of transparency? Not every form of disclosure serves this goal equally. What is needed is transparency that ensures philosophical work produced under AI assistance remains *attributable to human intellectual agency*—that the resulting arguments, commitments, and contributions can be traced to a human who understood, directed, and can defend them. This is the function of the transparency apparatus proposed in this paper, and it can be grounded in a framework originally developed for a very different domain.

## Meaningful Human Control: Tracking and Tracing

Santoni de Sio and van den Hoven (2018) developed the concept of *meaningful human control* (MHC) to address autonomous weapons systems. Their framework identifies two necessary conditions for human actions mediated by autonomous systems to remain genuinely under human control.

The first is the **tracking condition**: the system's behavior must covary with relevant human reasons. Drawing on Fischer and Ravizza's (1998) theory of guidance control and Nozick's tracking theory of knowledge, this condition requires that the system be responsive to the intentions, goals, and corrections of the humans directing it. For AI-assisted scholarship, the tracking condition is satisfied when the AI output is responsive to the author's argumentative goals—when the system follows the author's intellectual direction and the author can redirect it when it drifts.

The second is the **tracing condition**: the system's outputs must be traceable to proper understanding and endorsement by some human person. As Santoni de Sio and van den Hoven put it, "systems whose actions and states are not traceable to relevant understanding and endorsing by some human person—be they a designer, a controller, a user, etc.—no matter how intelligent and reason-responsive they may be, are not under meaningful human control. They would be like human actions carried out under psychological manipulation, subliminal persuasion, brainwashing, and indoctrination" (2018, §6.2). The tracing condition demands not merely that the system followed instructions, but that the person directing it *understood* what was being produced and *endorsed* it as their own intellectual contribution.

## Why Tracing Is the Distinctive Challenge

Both conditions are necessary, but tracing presents the distinctive challenge for scholarship. Tracking is relatively straightforward to satisfy: if the author iterates with the AI system—posing questions, correcting outputs, redirecting argumentation—the resulting work will generally track the author's intentions. The output covaries with the author's intellectual direction.

Tracing is harder. Even when tracking is satisfied, the author might not understand the resulting work well enough to own it. A parallel from the weapons domain makes this concrete: a soldier might press a button that causes a drone strike—the system tracked the command—but if the soldier did not understand what the weapon would do or what the consequences would be, tracing fails. The action cannot be properly attributed to the soldier's agency.

For scholarship: an author might prompt an AI to produce an argument that the AI generates competently. The output tracks the prompt. But if the author cannot explain why the argument works, defend it against objections, or identify its philosophical commitments, the tracing condition fails. The intellectual contribution cannot be properly attributed to the author's understanding.

## Operationalizing Tracing: The Transparency Apparatus

The paper's transparency requirements—the five Submission Packages (SP-1 through SP-5)—are designed to make the tracing condition verifiable. Each element serves a specific function in this verification:

**SP-1 (Declaration)** signals that tracing assessment is needed. By declaring AI involvement prominently, the author alerts reviewers and readers that the work's intellectual trajectory involves non-human components.

**SP-2 (Tool Specification)** documents which AI systems were used and when, enabling reproduction attempts and establishing the technological context of the work.

**SP-3 (Contribution Summary)** identifies what the AI contributed, delineating what must be traceable to the author's understanding and direction.

**SP-4 (Process Documentation)** provides the substance of tracing verification. Prompts, iterative corrections, guidance documents, and decision points constitute the material record against which tracing is assessed. Without process documentation, tracing cannot be verified—there is only the author's unsubstantiated claim that they understood and directed the work.

**SP-5 (Development Records)** preserves the full interaction history, enabling deep tracing assessment when questions arise about specific argumentative moves or contributions.

SP-4 is the core. It is what transforms the tracing condition from a philosophical requirement into a verifiable standard.

The **reproduction test** proposed in Section 7 operationalizes this verification directly. The test asks: can a reviewer, given only the documented human inputs—prompts, guidance, iterative corrections—reproduce the intellectual trajectory of the work? If yes, the author's documented inputs were sufficient to generate the work's argumentative architecture, and the trajectory traces to human direction. If no, either the documentation is incomplete, or the tracing condition is not satisfied—the work contains intellectual moves that cannot be traced to human understanding.

This is not about identical outputs. Different AI systems or different runs will produce different text. The test is whether the *intellectual architecture*—the argumentative structure, key moves, and commitments—can be regenerated from what the human documented.

## Engagement with Lloyd's Standards

Lloyd (2025) proposes four standards for AI-assisted scholarship: *prominence* (AI use immediately apparent), *replicability* (prompts documented), *content cross-checking* (human verification of AI factual claims), and *intra-textual clarity* (AI-generated text demarcated via style markers).

We adopt the first two standards, which our framework extends. SP-1 serves the prominence function. SP-4 goes beyond prompt logging to capture the full process through which arguments are developed. Content cross-checking is implicit in standard scholarly responsibility and need not be singled out.

We reject the fourth standard—intra-textual demarcation. Lloyd's proposal assumes that transparency requires marking which text was AI-generated versus human-written. This fails for several reasons.

First, it presupposes a primitive model of AI assistance. Real workflows involve iterative refinement where "AI text" and "human text" blur. A sentence might be AI-generated, human-edited, AI-revised, and human-finalized. Assigning provenance to such text is not merely difficult but conceptually confused.

Second, text-level demarcation cannot capture what matters. Some papers might be entirely AI-outputted yet reflect enormous human intellectual input—conceptual architecture, iterative shaping, sustained quality control. Others might be mostly human-written with AI contributing a crucial insight. Sentence-level marking captures none of this.

Third, the very category of "human contribution" is evolving. Practice is moving from *prompting*—formulating queries that elicit useful outputs—to *steering*—iteratively guiding AI through complex argumentative terrain. Perhaps scholars will become *architecture builders*—designing intellectual structures that AI populates with content. As practice evolves, the nature of the salient human contribution shifts in ways that text demarcation cannot anticipate.

Process documentation is more fundamental. What matters is not which sentences came from where but whether the intellectual trajectory is traceable to human understanding. SP-4 captures *whatever* the human contribution turns out to be—without presupposing its form.

## Three Nested Concerns

The framework developed here makes explicit how the paper's concerns relate:

At the innermost level, **epistemic integrity** ensures that knowledge claims produced under AI assistance are trustworthy—confabulation is controlled, sources are verified, arguments are valid.

At the middle level, **meaningful human control** through the tracing condition ensures that intellectual contributions are attributable to human understanding and direction. This builds on epistemic integrity but goes beyond it: a claim might be factually accurate yet not traceable to the author's understanding.

At the outermost level, **tracking what philosophy becomes**—the meta-philosophical goal established in Section 3—requires that tracing be verifiable across the scholarly community. Individual authors must satisfy the tracing condition; the transparency apparatus makes that satisfaction assessable by others.

The transparency requirements proposed here serve all three levels simultaneously. They are not bureaucratic impositions but the operational infrastructure through which the scholarly community can maintain epistemic standards, verify intellectual attribution, and observe the evolution of philosophical practice under AI assistance.

---

## References

Fischer, J. M., & Ravizza, M. (1998). *Responsibility and Control: A Theory of Moral Responsibility*. Cambridge University Press.

Lloyd, D. (2025). Epistemic responsibility: toward a community standard for human-AI collaborations. *Frontiers in Artificial Intelligence*, 8, 1635691.

Santoni de Sio, F., & van den Hoven, J. (2018). Meaningful human control over autonomous systems: a philosophical account. *Frontiers in Robotics and AI*, 5, 15.
