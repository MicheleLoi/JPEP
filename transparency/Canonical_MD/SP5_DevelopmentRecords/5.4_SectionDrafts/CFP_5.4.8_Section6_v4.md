---
project: JPEP
document_type: Type 12 - Section Draft
section: "6 - Mandatory Transparency in Practice"
version: "v4.2 (CFP adaptation, S1 Shoulders reviewer reply — MHC borrowing clarified as conceptual, not analogical)"
date_created: 2026-04-01
date_last_modified: 2026-05-12
status: Draft
source: "Claude Opus 4.6 (Claude Code session) / Claude Sonnet 4.6 for v4.2 clarification"
inputs:
  - CFP_4.4.19_SectionGuidance_SelfExpressionDistribution.md
  - CFP_5.4.8_Section6_v3.md
  - CFP_5.3.27_Note_ReviewResponse_Draft.md
  - "CFP_5.4.4_Section3_v3.md (frontmatter v5; cross-referenced as the independent ground for the conceptual borrowing of MHC)"
derived_from: "CFP_5.4.8_Section6_v4.md"
cfp_target: "AI Tools in Ethics Research (topical collection)"
session_id:
  - SID-20260401-173934
  - SID-20260512-154043
transformation: "v4 → v4.1: Redundancy pass 1. Compressed §5.1 opening and Convergence; shortened citation-pattern examples; merged §5.2 implementation paragraph into preceding; cut §5.4 second paragraph (hedging about limitations). Net −~350 words. v4.1 → v4.2: S1 Shoulders reviewer reply — MHC framework introduction rewritten to remove 'transfers structurally' analogy phrasing; conceptual-not-analogical clarification added with cross-reference to §3 v5 agent-integrity grounding. Net +~60 words."
word_count: ~1630
section_numbering: pre_renaming
versioning_convention: git_inplace
---
# 5. Mandatory Transparency in Practice

## 5.1 From Conditions to Practice

Section 3 established that ethical inquiry is essentially contested at two levels, and that both levels converge on comprehensive process documentation. The two routes to that conclusion are developed here.

*The meta-ethical route.*

The meta-ethical contestation generates the tracking requirement through two paths. For the expressivist, quality criteria are constitutively process-dependent: coherence on expressivist accounts is coherence of a *person's* evaluative attitudes — an AI can produce text exhibiting surface coherence among evaluative claims without any attitude being held, expressed, or revised. The output underdetermines whether the relevant process occurred. For the cognitivist, essential contestedness means no tradition can treat its evaluative criteria as the default for the field. The community of legitimate evaluators includes expressivists whose criteria are constitutively process-dependent, and their assessments cannot proceed from the output alone. Process documentation is therefore required on both accounts.

*The ethical route.*

The tradition named in Section 3—Socrates, Kierkegaard, Nietzsche—treats philosophical activity as constitutively self-expressive: the process of inquiry reveals and constitutes the inquirer. One might argue that if this tradition is right, delegating intellectual production to an AI introduces alien agency into a process whose value lies in disclosing the self — that if philosophy is confession, delegation is imposture.

But this objection locates self-expression in the wrong place. What expresses the self is not the manual production of sentences but the vision that organizes them — the questions selected, the risks taken, the intellectual judgments brought to the whole. Creative practice has long recognized this. In modular synthesis, the composer designs the system architecture — patching together oscillators, filters, and sequencers — rather than controlling every waveform; sonic properties emerge from module interactions in ways not fully predictable from individual settings. In computer-based generative art, the artist establishes abstract rules implemented by a computer such that the system is "partly responsible for coming up with the idea itself" (Boden & Edmonds, 2009, p. 138) — Harold Cohen's AARON is the paradigmatic case. In each instance, creative agency lies in designing the generative structure, not in manual execution.

Philosophy already recognizes process details as self-expressive. Citation patterns constitute implicit methodological proposals about what resources matter for philosophy; the community reads them as expressive of intellectual identity. AI usage is a new dimension of the same practice: the choice of interlocutor is itself a self-expressive act.

What different modes of AI engagement express matters. Documented delegation expresses willingness to test a new medium and commitment to visibility. Concealment misrepresents the process — the text performs a philosophical identity not the author's own. Documentation restores the conditions for self-expression: the vulnerability of disclosure — making visible uncertainties, iterations, moments where AI moved ahead of authorial understanding — is what distinguishes confession from curated narrative.

*Convergence.* The conditions enabling tracking are the same conditions enabling self-expression under AI assistance. A transparency framework does not constrain authorial identity; it is what makes authorial identity legible when the production process is no longer self-evident from the text.

*The framework.*

The Meaningful Human Control (MHC) framework provides the operationalization. Santoni de Sio and van den Hoven (2018) developed MHC for autonomous weapons systems; our debt is conceptual, not analogical. We apply the tracking and tracing conditions to AI-assisted scholarship on the basis of §3's independent argument from agent-integrity. The features that distinguish weapons systems — catastrophic stakes, physical irreversibility, kinetic control — play no role here; what carries over is the philosophical content of what it means to track an agent's reasoning and to trace an output to an agent's understanding. MHC identifies two necessary conditions. The **tracking condition** requires that system outputs covary with the human operator's relevant reasons. The **tracing condition** is more demanding: outputs must be traceable to proper understanding and endorsement by some human person. As Santoni de Sio and van den Hoven put it, "systems whose actions and states are not traceable to relevant understanding and endorsing by some human person—no matter how intelligent and reason-responsive they may be—are not under meaningful human control" (§6.2) [VERIFY: replace with page number].

Tracing requires that the directing person *understood* what was being produced and *endorses* it as their own intellectual contribution. This is where the two levels converge operationally. The question "did the author understand and endorse?" is precisely the question that Kierkegaard's truth-as-subjectivity makes constitutive and that Nietzsche's confession metaphor requires. A framework satisfying tracing serves both levels of the double contestation.

Tracing presents the distinctive challenge. Tracking is relatively easy: if the author iterates with the AI, the result will generally track their intentions. But if the author cannot explain why an argument works, defend it against objections, or identify its philosophical commitments, tracing fails.

The three conditions from Section 5—ecological validity, good faith orientation, costly signaling—implement these requirements under AI-mediated conditions.

## 5.2 The Transparency Framework

Three components structure the disclosure: model and process information establishes technological context; representative prompts and outputs show the author's inputs; process narrative provides a reflective account of the intellectual journey. Together these enable tracing assessment while remaining ecologically valid.

The five transparency elements—SP-1 through SP-5—each serve the tracing condition:

| Transparency Element        | What It Documents                                                        | How It Serves Tracing                                                  |
| --------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| SP-1: Declaration           | Summary of how AI was used                                               | First point of contact; makes visible what requires tracing            |
| SP-2: Navigation            | Structured index enabling access to SP-3, SP-4, and SP-5                 | Makes the documentation system legible and accessible                  |
| SP-3: Documentation Account | Detailed explanation of how AI was used; argument for adequacy           | Primary site of the tracing claim                                      |
| SP-4: Process Documentation | All writing-phase materials (prompts, guidance, modifications, traces)   | Primary substance against which SP-3's adequacy claim is assessed      |
| SP-5: Development Records   | How instructions evolved; meta-level documentation                       | Enables deeper tracing of intellectual direction                       |

**Engagement with Lloyd's standards.** Lloyd (2025) proposes four standards for AI-assisted scholarship: *prominence*, *replicability*, *content cross-checking*, and *intra-textual clarity*. We adopt Standards 1 and 2. We reject Standard 4: in iterative prompt-revision workflows, human editorial judgment is embedded in every clause, making binary attribution of text to "AI" or "human" incoherent — as the process documentation in this paper's archived SP-4 illustrates. What matters is whether the intellectual trajectory is traceable to human understanding, which is what an SP-4 captures.

The requirements make explicit three nested concerns:

```
OUTERMOST: Track what ethics research becomes
    |
    +-- MIDDLE: Ensure meaningful human control (tracing condition)
            |
            +-- INNERMOST: Maintain epistemic integrity
```

## 5.3 Experimental Development and Community Evolution

This framework represents a sketch requiring experimentation. An early community of practice functions as exploratory search: authors experiment with documentation, reviewers with assessment, shared practices evolve through experience. What we propose aims at proof-of-concept. This article demonstrates one possible implementation, showing transparency requirements can be met without technical infrastructure or surveillance bureaucracy.

Research communities organized around opacity face an adverse selection dynamic: as non-transparent AI use becomes widespread, the epistemic value of all undisclosed work diminishes collectively, while scholars committed to transparency bear individual costs. Communities organized around transparency tend toward a different dynamic: they are more likely to attract scholars motivated by the desire to learn from one another's documented practice.

## 5.4 Pilot Observations

The documentation requirements are substantial: prompts, modification logs, epistemic traces, and session records accumulate rapidly. Synthesizing them into the coherent account SP-3 requires is intractable if attempted retrospectively. AI-assisted synthesis—applied immediately after each working session—is what makes the framework viable. A framework requiring transparency about AI use depends, in implementation, on AI assistance to sustain the documentation it requires. The relevant constraint is that synthesis be honest—that the documented account accurately represents the intellectual process. Working from the raw session record during synthesis, rather than from memory alone, reduces the risk of the account becoming more coherent than the process actually was.

---

## References

Boden, M. A., & Edmonds, E. A. (2009). What is generative art? *Digital Creativity*, 20(1-2), 21-46.

Lloyd, D. (2025). Epistemic responsibility: toward a community standard for human-AI collaborations. *Frontiers in Artificial Intelligence*, 8, 1635691.

Santoni de Sio, F., & van den Hoven, J. (2018). Meaningful human control over autonomous systems: a philosophical account. *Frontiers in Robotics and AI*, 5, 15.
