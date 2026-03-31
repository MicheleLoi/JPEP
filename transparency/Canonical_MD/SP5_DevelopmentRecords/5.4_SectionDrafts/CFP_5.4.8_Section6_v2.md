---
project: JPEP
document_type: Type 12 - Section Draft
section: "6 - Mandatory Transparency in Practice"
version: "v2 (CFP adaptation)"
date_created: 2026-03-23
status: Draft
source: "Claude Sonnet 4.6 (Claude Code session)"
source_guidance: "CFP_5.3.1_WorkPlan_CFP_Adaptation.md"
cfp_target: "AI Tools in Ethics Research (topical collection)"
source_file: "CFP_5.4.8_Section6_v1.md"
transformation: "v1 → v2: §6.1 reordered (two-routes derivation before MHC introduction); opening paragraph revised (removed premature attribution/tracing language); discovery/justification paragraph cut; 'we do not' negative paragraphs removed (positive argument carries the weight); traditional values paragraph reframed to ground attribution in process-dependent criteria; attribution/tracing bridge paragraph revised; 'principles' → 'conditions' harmonized; §6.2 nested-diagram middle-level explanation updated; overall compression."
revision_note: "Revised following Reviewer A verdict (cut discovery/justification paragraph) + Reviewer B REVISE instructions + multi-round philosophical revision of the ethics-specific paragraph."
word_count: ~1600
---
# 6. Mandatory Transparency in Practice

## 6.1 From Conditions to Practice

Section 3 established that the question of whether AI changes ethical inquiry admits of no neutral adjudication—"ethical inquiry" is an essentially contested concept, and any answer presupposes settling what the discipline constitutively is. The achievable goal is more modest: tracking what ethics research is becoming. This requires transparency. But what kind of transparency? Not every form of disclosure serves this goal equally. What is needed is transparency adequate to the full community of legitimate evaluators—one that can be specified philosophically rather than merely mandated formally.

The contestation that makes neutral adjudication impossible generates two distinct routes to that requirement. For non-cognitivists, particularists, and constructivists, quality criteria are constitutively process-dependent: non-cognitivist coherence is coherence of a *person's* evaluative attitudes, particularist sensitivity requires genuine perceptual attunement, and constructivist fidelity demands that a reasoning agent actually underwent the deliberative procedure. In each case, the output underdetermines whether the relevant process occurred—an AI can produce text that simulates all three without any of them taking place. For the cognitivist, validity and truth-tracking may well be output-sufficient within the cognitivist's own framework. But essential contestedness means no tradition can treat its evaluative criteria as the default for the field. The community of legitimate evaluators includes those whose criteria are constitutively process-dependent, and their assessments cannot proceed from the output alone. Process documentation is therefore required on both routes—because quality criteria are process-dependent, or because no tradition can foreclose assessment by those whose criteria are.

These requirements also actualize traditional values that opacity under AI production threatens. Philosophy has always valued guided thought—showing readers not just conclusions but reasoning processes. Williams's engagement with Greek tragedy, Cavell's pairing of ordinary language philosophy with film criticism, Nozick's deployment of decision theory in ethics, Lewis's systematic bridge-building between modal logic and metaphysics—each citation pattern constitutes an implicit methodological proposal about what resources matter for philosophy. Philosophy values intellectual honesty: admitting uncertainty, acknowledging objections, revealing limits. It values methodological self-consciousness: Socratic dialogue, phenomenological description, reflective equilibrium matter as contributions.

These values require that evaluators can locate the human contribution. Opacity under AI production makes this impossible even when no fraud occurs. For the evaluator whose criteria are constitutively process-dependent, opacity forecloses assessment entirely—you cannot assess whether genuine evaluative engagement, perceptual attunement, or deliberative fidelity occurred without process information. For the evaluator applying formal criteria, you cannot determine whether the author genuinely understands and endorses the argument rather than merely presenting it. In either case, attribution becomes epistemically necessary, not merely ethically required. This is precisely what the tracing condition captures: it operationalizes the condition under which contributions to ethics research remain assessable across the full range of legitimate evaluative positions.

Full process disclosure is itself an expression of epistemic virtue. The vulnerability it entails—making visible the uncertainties, the iterations, the moments where AI output moved ahead of authorial understanding—is continuous with the intellectual vulnerability philosophy has always valued: admitting where your argument is weakest, acknowledging what the strongest objection is, showing the limits of your grasp. A transparency framework that demands this kind of vulnerability does not merely create accountability; it instantiates, under AI-mediated conditions, the same epistemic dispositions that have always marked genuine philosophical engagement. This virtue-based observation is not the ground of the requirement—that ground was established above on metaethically neutral terms—but it shows that the requirement converges with what philosophy has always valued in honest intellectual practice.

The Meaningful Human Control (MHC) framework provides the precise operationalization of this requirement. Santoni de Sio and van den Hoven (2018) developed MHC for autonomous weapons systems, but the framework transfers structurally to AI-assisted scholarship. It identifies two necessary conditions. The **tracking condition** requires that system outputs covary with the human operator's relevant reasons—the system must be responsive to the intentions and corrections of those directing it. For scholarship, this is satisfied when the AI follows the author's intellectual direction and can be redirected when it drifts. The **tracing condition** is more demanding: outputs must be traceable to proper understanding and endorsement by some human person. As Santoni de Sio and van den Hoven put it, "systems whose actions and states are not traceable to relevant understanding and endorsing by some human person—no matter how intelligent and reason-responsive they may be—are not under meaningful human control. They would be like human actions carried out under psychological manipulation, subliminal persuasion, brainwashing, and indoctrination" (§6.2). Tracing requires not merely that the system followed instructions, but that the directing person *understood* what was being produced and *endorses* it as their own intellectual contribution.

Tracing presents the distinctive challenge for scholarship. Tracking is relatively easy: if the author iterates with the AI—posing questions, correcting outputs, redirecting argumentation—the result will generally track their intentions. Tracing is harder. A soldier might press a button causing a drone strike—tracking is satisfied—but if the soldier did not understand what the weapon would do or what the consequences would be, tracing fails. The action cannot be attributed to the soldier's agency. For scholarship: an author might prompt an AI to generate an argument. But if the author cannot explain why the argument works, defend it against objections, or identify its philosophical commitments, tracing fails. The intellectual contribution cannot be attributed to the author's understanding.

The three conditions from Section 5—ecological validity, good faith orientation, cost structure through costly signaling—implement these requirements under AI-mediated conditions. The transparency apparatus specified in 6.2 makes that implementation verifiable.

## 6.2 The Transparency Framework

Disclosure requirements must balance three functions: *verification* (establishing authorship and accountability), *methodological learning* (enabling community understanding of effective practices), and *preservation of traditional philosophical values* (maintaining attribution, guided thought, and thinking quality assessment). The framework requires accessibility—scholars without technical training must find documentation feasible.

Three components structure the disclosure: model and process information establishes technological context and role boundaries; representative prompts and outputs show the author's inputs and what they worked with; process narrative provides a reflective account of the intellectual journey. Together these materials enable tracing assessment while remaining ecologically valid—emerging naturally from thoughtful scholarly work rather than imposing artificial surveillance.

This article provides a concrete implementation. The supplementary materials include: identification of the AI systems used; the complete synthesized prompt that structured the article's development; representative excerpts from exploratory conversations where key ideas emerged; documentation of how sections were written showing human guidance patterns and AI contribution; and a reflective account of what worked, what proved difficult, where judgment operated. No technical expertise is required—the documentation consists of text files, conversation excerpts, reflective writing.

The five transparency elements—SP-1 through SP-5—each serve the tracing condition:

| Transparency Element        | What It Documents                                                        | How It Serves Tracing                                                  |
| --------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| SP-1: Declaration           | Summary of how AI was used                                               | First point of contact; makes visible what requires tracing            |
| SP-2: Navigation            | Structured index enabling access to SP-3, SP-4, and SP-5                 | Makes the documentation system legible and accessible                  |
| SP-3: Documentation Account | Detailed explanation of how AI was used; argument for adequacy           | Primary site of the tracing claim: here is the intellectual trajectory, and the case that it traces to human understanding |
| SP-4: Process Documentation | All writing-phase materials (prompts, guidance, modifications, traces)   | Primary substance against which SP-3's adequacy claim is assessed      |
| SP-5: Development Records   | How instructions evolved; meta-level documentation                       | Enables deeper tracing of intellectual direction                       |

SP-3 is the primary site of the tracing claim. Rather than a reproduction test—which proves unworkable given model deprecation, non-deterministic outputs, and the time-scale of scholarly production—SP-3 asks not *could the documented inputs reproduce this work?* but *does the documentation adequately show how the intellectual trajectory traces to human understanding and direction?* SP-3 makes the author's case that the documentation is sufficient for this purpose; SP-4 is the primary substance against which that case is assessed.

**Engagement with Lloyd's standards.** Lloyd (2025) proposes four standards for AI-assisted scholarship: *prominence*, *replicability*, *content cross-checking*, and *intra-textual clarity* (AI-generated text demarcated via style markers). We adopt Standards 1 and 2. SP-1 serves the prominence function, extended to summarize how AI was used; SP-3 extends replicability beyond prompt logging to a full documentation account and adequacy argument. We reject Standard 4: real workflows involve iterative refinement where "AI text" and "human text" blur across drafting, editing, and revision. What matters is not which sentences came from where, but whether the intellectual trajectory is traceable to human understanding—which is what SP-4 captures regardless of how the human contribution evolves.

The requirements make explicit three nested concerns:

```
OUTERMOST: Track what ethics research becomes
    |
    +-- MIDDLE: Ensure meaningful human control (tracing condition)
            |
            +-- INNERMOST: Maintain epistemic integrity
```

At the innermost level, **epistemic integrity** ensures that claims produced under AI assistance are trustworthy—confabulation controlled, sources verified, arguments valid. At the middle level, **meaningful human control** through the tracing condition ensures that intellectual contributions are attributable to human understanding and direction. This requirement holds on both grounds established in Section 6.1: evaluators whose quality criteria are constitutively process-dependent require tracing to perform their assessments; evaluators operating within a contested field cannot foreclose assessment by those whose criteria are not output-sufficient. At the outermost level, **tracking what ethics research becomes** requires that tracing be verifiable across the scholarly community, enabling the informed meta-level discussion that Section 3 identifies as the achievable goal.

## 6.3 Experimental Development and Community Evolution

This framework represents a sketch requiring substantial experimentation and refinement. An early community of practice functions as exploratory search: authors experiment with documentation approaches, reviewers experiment with assessment methods, shared practices evolve through experience. Community life itself becomes trial and error, testing what transparency requirements prove both sufficient for accountability and feasible for practitioners.

Convergence on stable practices may take years. Some elements might prove essential across all work—perhaps model identification and basic role mapping establish minimum requirements. Other elements might vary by area or argument type—formal work might require different documentation than historical scholarship, normative arguments different from metaphysical analysis.

What we propose now aims at proof-of-concept rather than prescription. This article demonstrates one possible implementation, showing transparency requirements can be met without technical infrastructure or surveillance bureaucracy. The research community succeeds at this task if it creates conditions for methodological knowledge to accumulate: we learn collectively what documentation practices enable both accountability and advancement in AI-assisted work in ethics.

There is a further structural consideration. Research communities organized around opacity face an adverse selection dynamic: as non-transparent AI use becomes widespread, the epistemic value of all undisclosed work diminishes collectively, while scholars committed to genuine transparency bear individual costs for doing so. Communities organized around transparency invert this: they tend to attract scholars motivated by the desire to learn—from one another's documented practice, from shared methodological experimentation, from the accumulating record of what works. The virtue of transparency becomes self-reinforcing when the community is constituted by those who find value in making their intellectual process visible.

This evolutionary perspective keeps methodological development grounded in practice. Early participants shape norms through experimentation; successful patterns spread through demonstrated value rather than prescription.

## 6.4 Pilot Observations

Two infrastructural constraints became apparent mid-way through development. LLM platforms lack timestamps within conversations, making temporal reconstruction require manual effort. More fundamentally, comprehensive documentation produces overwhelming archives that require synthesis—yet synthesis risks post-hoc rationalization. AI-assisted synthesis (immediately after writing) proves feasible but requires human verification.

From the author's perspective, what matters is tracking AI-assisted work in ways that remain lightweight and intelligible. The artifacts listed in Appendix A provide a scaffold—templates for documentation habits, not protocols. These materials function like training examples: individual implementations that enable pattern recognition across cases about what synthesis approaches, metadata choices, and documentation granularity prove workable.

---

## References

Lloyd, D. (2025). Epistemic responsibility: toward a community standard for human-AI collaborations. *Frontiers in Artificial Intelligence*, 8, 1635691.

Santoni de Sio, F., & van den Hoven, J. (2018). Meaningful human control over autonomous systems: a philosophical account. *Frontiers in Robotics and AI*, 5, 15.
## Connections (auto)

_No connections found._

