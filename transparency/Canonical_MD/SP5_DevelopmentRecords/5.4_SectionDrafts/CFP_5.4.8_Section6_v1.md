---
project: JPEP
document_type: Type 12 - Section Draft
section: "6 - Mandatory Transparency in Practice"
version: "v1 (CFP adaptation)"
date_created: 2026-03-23
status: Draft
source: "Claude Sonnet 4.6 (Claude Code session)"
inputs:
  - CFP_5.3.1_WorkPlan_CFP_Adaptation.md
  - III_5.4.2_Section6_v3.md
cfp_target: "AI Tools in Ethics Research (topical collection)"
transformation: "Minor reframe: venue/journal → research practice/community; principles → conditions (harmonization with Section 5); explicit connection §6.1 thinking-quality argument → cognitivist-objection defeat (Introduction); virtue dimension added §6.1; adverse selection observation added §6.3; nested concerns diagram updated for ethics framing."
feeds_into: "CFP_4.2.18_ModificationLog_Section6.md"
word_count: ~1550
---
# 6. Mandatory Transparency in Practice

## 6.1 From Conditions to Practice

Section 3 established that the question of whether AI changes ethical inquiry admits of no neutral adjudication—"ethical inquiry" is an essentially contested concept, and any answer presupposes settling what the discipline constitutively is. The achievable goal is more modest: tracking what ethics research is becoming. This requires transparency. But what kind of transparency? Not every form of disclosure serves this goal equally. What is needed is transparency that ensures ethical work produced under AI assistance remains *attributable to human intellectual agency*—and the Meaningful Human Control (MHC) framework specifies what this requires.

Santoni de Sio and van den Hoven (2018) developed MHC for autonomous weapons systems, but the framework transfers structurally to AI-assisted scholarship. It identifies two necessary conditions. The **tracking condition** requires that system outputs covary with the human operator's relevant reasons—the system must be responsive to the intentions and corrections of those directing it. For scholarship, this is satisfied when the AI follows the author's intellectual direction and can be redirected when it drifts. The **tracing condition** is more demanding: outputs must be traceable to proper understanding and endorsement by some human person. As Santoni de Sio and van den Hoven put it, "systems whose actions and states are not traceable to relevant understanding and endorsing by some human person—be they a designer, a controller, a user, etc.—no matter how intelligent and reason-responsive they may be, are not under meaningful human control. They would be like human actions carried out under psychological manipulation, subliminal persuasion, brainwashing, and indoctrination" (§6.2). Tracing requires not merely that the system followed instructions, but that the directing person *understood* what was being produced and *endorses* it as their own intellectual contribution.

Tracing presents the distinctive challenge for scholarship. Tracking is relatively easy: if the author iterates with the AI—posing questions, correcting outputs, redirecting argumentation—the result will generally track their intentions. Tracing is harder. A soldier might press a button causing a drone strike—tracking is satisfied—but if the soldier did not understand what the weapon would do or what the consequences would be, tracing fails. The action cannot be attributed to the soldier's agency. For scholarship: an author might prompt an AI to generate an argument. But if the author cannot explain why the argument works, defend it against objections, or identify its philosophical commitments, tracing fails. The intellectual contribution cannot be attributed to the author's understanding.

Before specifying what transparency means in practice, the scholarly values motivating these requirements deserve clarification. What we do *not* argue is as important as what we do.

We do not work within the traditional discovery/justification framework (Reichenbach, 1938). That binary—context of discovery versus context of justification—proves inadequate for understanding what scholarly evaluation actually does. Article evaluation never assessed merely whether arguments are valid. It always also assessed thinking quality: Does this work show sophisticated judgment? Methodological competence? Understanding of what matters? These dimensions require assessing process, not because process affects truth-value, but because thinking quality is part of what we evaluate. The discovery/justification distinction obscured this dimension.

In the context of ethical inquiry specifically, this point has additional force. The Introduction established that "ethical inquiry" is an essentially contested concept: competent practitioners disagree about its constitutive methods, its epistemic structure, and its purpose. This means that the thinking quality at stake in evaluating ethical arguments cannot be reduced to formal validity. It encompasses evaluative sensibility, judgment about which considerations matter, and the understanding of what makes an ethical argument philosophically serious—dimensions on which the cognitivist and non-cognitivist, the particularist and the systematizer, differ in their criteria. These are precisely the dimensions that AI assistance may affect most significantly, and which process documentation is uniquely positioned to make visible. The cognitivist objection—"just evaluate the outputs"—fails in ethics not only because output-evaluation criteria are contested, but because the thinking quality that makes a contribution valuable in ethics cannot be read off the output alone.

We do not prioritize gaming resistance over ecological validity. While accountability matters, we explicitly choose procedures that work naturally in honest scholarly practice over maximum surveillance. Gaming-focused design creates unacceptable costs: surveillance bureaucracy burdens honest scholars, arms races between gaming and countermeasures, adversarial atmosphere preventing methodological experimentation. The real threat is opacity preventing knowledge accumulation, not gaming in a research community offering no credential benefits to those who successfully evade transparency.

We do not argue from moral desert, from economic necessity, or that traditional research venues should adopt these practices. The transparency requirements serve specific purposes for AI-assisted work where opacity creates unique epistemic problems.

The requirements actualize traditional values that opacity under AI production threatens. Philosophy has always valued guided thought—showing readers not just conclusions but reasoning processes. Williams's engagement with Greek tragedy, Cavell's pairing of ordinary language philosophy with film criticism, Nozick's deployment of decision theory in ethics, Lewis's systematic bridge-building between modal logic and metaphysics—each citation pattern constitutes an implicit methodological proposal about what resources matter for philosophy. Philosophy values intellectual honesty: admitting uncertainty, acknowledging objections, revealing limits. It values methodological self-consciousness: Socratic dialogue, phenomenological description, reflective equilibrium matter as contributions.

These values require attribution to function. When reading excellent philosophy, you must know whose thought you're following to learn from the example. Opacity under AI production destroys these values even when no fraud occurs. You cannot distinguish genuine intellectual struggle from AI rhetorical polish, cannot tell whether architectural elegance reflects human understanding or AI optimization, cannot assess whose judgment displays in the text. For citation patterns, you cannot determine whether connections reflect authorial insight or AI's training co-occurrences, cannot learn from methodological exemplars without knowing whose moves they are. Attribution becomes epistemically necessary, not merely ethically required. This is precisely what the tracing condition captures: the transparency requirements operationalize the condition under which contributions to ethics research remain genuinely attributable to human intellectual agency.

Full process disclosure is itself an expression of epistemic virtue. The vulnerability it entails—making visible the uncertainties, the iterations, the moments where AI output moved ahead of authorial understanding—is continuous with the intellectual vulnerability philosophy has always valued: admitting where your argument is weakest, acknowledging what the strongest objection is, showing the limits of your grasp. A transparency framework that demands this kind of vulnerability does not merely create accountability; it instantiates, under AI-mediated conditions, the same epistemic dispositions that have always marked genuine philosophical engagement.

The three conditions from Section 5—ecological validity, good faith orientation, cost structure through costly signaling—implement these traditional values under AI-mediated conditions. The transparency apparatus specified in 6.2 makes that implementation verifiable.

## 6.2 The Transparency Framework

Disclosure requirements must balance three functions: *verification* (establishing authorship and accountability), *methodological learning* (enabling community understanding of effective practices), and *preservation of traditional philosophical values* (maintaining attribution, guided thought, and thinking quality assessment). The framework requires accessibility—scholars without technical training must find documentation feasible.

Three components structure the disclosure: model and process information establishes technological context and role boundaries; representative prompts and outputs show the author's inputs and what they worked with; process narrative provides a reflective account of the intellectual journey. Together these materials enable tracing assessment while remaining ecologically valid—emerging naturally from thoughtful scholarly work rather than imposing artificial surveillance.

This article provides a concrete implementation. The supplementary materials include: identification of the AI systems used; the complete synthesized prompt that structured the article's development; representative excerpts from exploratory conversations where key ideas emerged; documentation of how sections were written showing human guidance patterns and AI contribution; and a reflective account of what worked, what proved difficult, where judgment operated. No technical expertise is required—the documentation consists of text files, conversation excerpts, reflective writing. Non-technical scholars can produce similar materials through ordinary reflection on their process.

The five transparency elements—SP-1 through SP-5—each serve the tracing condition:

| Transparency Element        | What It Documents                                                        | How It Serves Tracing                                                  |
| --------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| SP-1: Declaration           | Summary of how AI was used                                               | First point of contact; makes visible what requires tracing            |
| SP-2: Navigation            | Structured index enabling access to SP-3, SP-4, and SP-5                 | Makes the documentation system legible and accessible                  |
| SP-3: Documentation Account | Detailed explanation of how AI was used; argument for adequacy           | Primary site of the tracing claim: here is the intellectual trajectory, and the case that it traces to human understanding |
| SP-4: Process Documentation | All writing-phase materials (prompts, guidance, modifications, traces)   | Primary substance against which SP-3's adequacy claim is assessed      |
| SP-5: Development Records   | How instructions evolved; meta-level documentation                       | Enables deeper tracing of intellectual direction                       |

SP-3 is the primary site of the tracing claim. Rather than a reproduction test—which would require running documented inputs through a comparable AI system, and which proves unworkable given model deprecation, non-deterministic outputs, and the time-scale of scholarly production—SP-3 takes a different approach. It does not ask *could the documented inputs reproduce this work?* but *does the documentation adequately show how the intellectual trajectory traces to human understanding and direction?* SP-3 explains how the documentation system works and makes the author's case that it is sufficient for this purpose. SP-4 is the primary substance against which that case is assessed. SP-1 summarizes SP-3's core claims for the reader who needs only the essentials; SP-2 makes the documentation system navigable.

**Engagement with Lloyd's standards.** Lloyd (2025) proposes four standards for AI-assisted scholarship: *prominence* (AI use immediately apparent), *replicability* (prompts documented), *content cross-checking* (human verification of AI factual claims), and *intra-textual clarity* (AI-generated text demarcated via style markers). We adopt Standards 1 and 2. SP-1 serves the prominence function, now extended: rather than merely noting AI involvement, it summarizes how AI was used. SP-3 extends replicability beyond prompt logging to a full account of the documentation system and the argument for its adequacy. Content cross-checking is implicit in standard scholarly responsibility.

We reject Standard 4. Text-level demarcation presupposes a primitive model of AI assistance: real workflows involve iterative refinement where "AI text" and "human text" blur across drafting, editing, revision, and finalization. Moreover, the category of human contribution is evolving. Practice is already moving from *prompting*—formulating queries—toward *steering*: iteratively guiding AI through complex argumentative terrain. Perhaps scholars will become *architecture builders*—designing intellectual structures that AI populates with content. As practice evolves, the nature of the salient human contribution shifts in ways that text marking cannot anticipate. Process documentation is more fundamental: what matters is not which sentences came from where, but whether the intellectual trajectory is traceable to human understanding. SP-4 captures *whatever* the human contribution turns out to be, without presupposing its form.

The requirements make explicit three nested concerns:

```
OUTERMOST: Track what ethics research becomes
    |
    +-- MIDDLE: Ensure meaningful human control (tracing condition)
            |
            +-- INNERMOST: Maintain epistemic integrity
```

At the innermost level, **epistemic integrity** ensures that claims produced under AI assistance are trustworthy—confabulation controlled, sources verified, arguments valid. At the middle level, **meaningful human control** through the tracing condition ensures that intellectual contributions are attributable to human understanding and direction: a claim may be factually accurate yet still fail tracing. At the outermost level, **tracking what ethics research becomes** requires that tracing be verifiable across the scholarly community, enabling the informed meta-level discussion that Section 3 identifies as the achievable goal. The transparency apparatus serves all three levels simultaneously.

## 6.3 Experimental Development and Community Evolution

This framework represents a sketch requiring substantial experimentation and refinement. An early community of practice functions as exploratory search: authors experiment with documentation approaches, reviewers experiment with assessment methods, shared practices evolve through experience. Community life itself becomes trial and error, testing what transparency requirements prove both sufficient for accountability and feasible for practitioners.

Convergence on stable practices may take years. Some elements might prove essential across all work—perhaps model identification and basic role mapping establish minimum requirements. Other elements might vary by area or argument type—formal work might require different documentation than historical scholarship, normative arguments different from metaphysical analysis. The community may converge on one standard model or develop several viable approaches.

What we propose now aims at proof-of-concept rather than prescription. This article demonstrates one possible implementation, showing transparency requirements can be met without technical infrastructure or surveillance bureaucracy. Other scholars will experiment differently. The research community succeeds at this task if it creates conditions for methodological knowledge to accumulate: we learn collectively what documentation practices enable both accountability and advancement in AI-assisted work in ethics.

There is a further structural consideration. Research communities organized around opacity face an adverse selection dynamic: as non-transparent AI use becomes widespread, the epistemic value of all undisclosed work diminishes collectively, while scholars committed to genuine transparency bear individual costs for doing so. Communities organized around transparency invert this: they tend to attract scholars motivated by the desire to learn—from one another's documented practice, from shared methodological experimentation, from the accumulating record of what works. The virtue of transparency becomes self-reinforcing when the community is constituted by those who find value in making their intellectual process visible.

This evolutionary perspective keeps methodological development grounded in practice. Development proceeds through philosophical and ethical inquiry, not imposed standardization. Early participants shape norms through experimentation; successful patterns spread through demonstrated value rather than prescription.

## 6.4 Pilot Observations

Two infrastructural constraints became apparent mid-way through development. LLM platforms lack timestamps within conversations, making temporal reconstruction require manual effort. More fundamentally, comprehensive documentation produces overwhelming archives that require synthesis—yet synthesis risks post-hoc rationalization. AI-assisted synthesis (immediately after writing) proves feasible but requires human verification.

From the author's perspective, what matters is tracking AI-assisted work in ways that remain lightweight and intelligible. The artifacts listed in Appendix A provide a scaffold—templates for documentation habits, not protocols. These materials function like training examples: individual implementations that enable pattern recognition across cases about what synthesis approaches, metadata choices, and documentation granularity prove workable.

---

## References

Lloyd, D. (2025). Epistemic responsibility: toward a community standard for human-AI collaborations. *Frontiers in Artificial Intelligence*, 8, 1635691.

Santoni de Sio, F., & van den Hoven, J. (2018). Meaningful human control over autonomous systems: a philosophical account. *Frontiers in Robotics and AI*, 5, 15.
## Connections (auto)

### Explicit links (inputs/outputs/etc.)
**feeds_into:**
- UNRESOLVED: CFP_4.2.18_ModificationLog_Section6.md

