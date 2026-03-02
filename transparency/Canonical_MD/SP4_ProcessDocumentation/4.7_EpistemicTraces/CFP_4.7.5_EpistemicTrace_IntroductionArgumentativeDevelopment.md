---
project: JPEP
document_type: Type 2 - Epistemic Trace
label: CFP_4.7.5_EpistemicTrace_IntroductionArgumentativeDevelopment
title: "CFP Introduction: Argumentative Spine Development"
date: 2026-03-02
source: "Claude Code session (Claude Sonnet 4.6) + Claude Opus 4.6 (subagent, agent-a37ba2f)"
status: Complete
influence: "One-to-many — determines CFP Introduction draft (CFP_5.4.3, pending), informs Section 3 adaptation (CFP_5.4.4, pending)"
related:
  - "CFP_5.3.1_WorkPlan_CFP_Adaptation.md (work plan produced in same session)"
  - "III_4.7.4_CFP_AIEthicsInquiry_BranchAndFitAnalysis.md (fit analysis — prior session)"
  - "III_5.4.1_Section3_v3.md (authoritative Section 3 draft — Gallie argument)"
  - "III_5.4.2_Section6_v3.md (authoritative Section 6 draft — MHC + documentation-adequacy)"
  - "target-venue/cfp_ai-ethics-inquiry.md (CFP text)"
---

# CFP Introduction: Argumentative Spine Development

## Session Context

This trace documents a Claude Code session (2026-03-02) that developed the argumentative spine for the CFP-adapted Introduction. The session followed directly from the prior session (III_4.7.4) which had established the CFP branch and corrected fit analysis. The user opened with `mhc-start` and selected the CFP adaptation workstream.

The session had three phases: (1) initial brainstorm by Sonnet, (2) Opus evaluation of the brainstorm plus a new idea from the user, (3) Opus re-evaluation after the user identified a synthesis move. The result was a four-move argumentative spine that is substantially different from—and stronger than—any of the individual ideas entering the session.

The raw conversation is preserved in `transparency/Canonical_MD/v3_Conversations_Claude_Code/` (exported via SessionEnd hook).

---

## Phase 1: The Brainstorm

Sonnet produced a six-move brainstorm for the CFP Introduction rewrite. The brainstorm correctly identified the framing shift required (from venue-design to methodological contribution), proposed positioning the paper relative to the CFP's own literature gap framing, and suggested briefly placing the essentially-contested argument in the Introduction.

**Strongest element:** Move 5 — placing the essentially-contested concept argument in the Introduction as the paper's central philosophical contribution.

**Weakest element:** Move 2 — listing ethics-specific methods (reflective equilibrium, casuistry, thought experiments) as "judgment-intensive in ways that make the human-contribution question especially acute." Opus later identified this as shallow and counterproductive: it implies there is an identifiable set of ethics methods whose judgment-intensiveness can be assessed, which is precisely what the essentially-contested framework denies.

**Style problem:** Six moves is too many. The brainstorm did not satisfy the user's stated preference (one deep argument over several shallow ones).

---

## Phase 2: First Opus Evaluation — Two Ideas

The user introduced a second idea: a cognitivist/truth-tracking argument. If ethics is truth-tracking (cognitivism), then the right question for AI use in ethics research is whether AI-assisted ethics contributes to truth-tracking or undermines it. This yields a mid-level institutional test: does rule/practice X contribute to ensuring that AI output enters public discourse in a way likely to contribute to convergence around truth in philosophical and normative matters?

The user explicitly noted the conditional structure ("IF one accepts cognitivism") and the limitation (analytic philosophers are largely realists; other humanities may not share the premise).

Opus evaluated both ideas. Key findings:

**On the brainstorm:** The essentially-contested argument (Move 5) is the only load-bearing element. The methods list (Move 2) is the weakest and should be dropped. Six moves does not satisfy the style preference.

**On the cognitivism argument:** The inference "IF cognitivism, THEN the institutional test follows straightforwardly" is not sound as stated. The missing premise is that *thinking quality* matters, not just logical validity — a cognitivist could still say "judge the argument, not the process." The IF-hedge does not work in a published paper: either you commit to cognitivism and get the argument, or you don't and have no argument.

**On the tension between the two ideas:** The essentially-contested argument is epistemically humble ("we don't know what ethics is"); cognitivism is epistemically confident ("we know ethics tracks truth"). Placing both in the same Introduction creates tonal whiplash. If forced to choose: the essentially-contested argument is more robust — it is ecumenical across metaethical positions and motivates the full apparatus without audience-narrowing.

**Recommendation at this stage:** Build the Introduction around the essentially-contested argument; use cognitivism as a brief aside in Section 3 or 6.

---

## Phase 3: The Synthesis Move — User's Insight

The user identified the synthesis:

> What if cognitivism IS the perfect example of an essentially contested feature of moral philosophy?

This reframes the relationship between the two ideas entirely. The cognitivism/non-cognitivism dispute — whether moral claims are truth-apt at all — is one of the most fundamental and unresolved disputes in metaethics. It may itself exemplify the essential contestedness of "ethical inquiry": competent practitioners persistently and reasonably disagree about what ethical inquiry is *for*.

Under this framing:
- Cognitivism is not asserted as a premise — it is *exhibited* as an illustration
- The cognitivism dispute becomes evidence of how deep the essential contestedness goes, not a competitor to the essentially-contested argument
- The tonal clash dissolves: the mood is uniformly humble — "we don't even agree on whether ethics tracks truth"

Opus evaluated this move:

**Tension dissolved:** Completely. The cognitivism dispute moves from premise to exhibit. The structure reverses: previously IF cognitivism THEN transparency; now the fact that cognitivism is contested shows how deep the contestation goes, THEREFORE tracking (and hence transparency) is the achievable goal.

**Audience-narrowing eliminated:** Both cognitivists and non-cognitivists are addressed symmetrically. Cognitivists need to assess whether AI-assisted ethics still tracks truth; non-cognitivists need to assess whether AI changes what ethics does. Both need process visibility.

**Gallie criteria applied to "ethical inquiry":** The claim that ethical inquiry is essentially contested is well-supported under Gallie's five criteria (appraisive, internally complex, variously describable, open, aggressive/defensive use). However, the correct formulation is that *ethical inquiry* is essentially contested, not that *cognitivism* is essentially contested — cognitivism is a position, not an appraisive concept. The cognitivism dispute is the deepest *instance* of the contestedness of ethical inquiry.

---

## Phase 4: The Cognitivist Objection Move

The user then recovered a move from Opus's earlier evaluation that had been lost in the synthesis:

> If ethics is truth-tracking, we don't care about anything beyond the outcome (Opus said). So no transparency! But wait — that's why the essentially contested nature of moral philosophy enters the picture and justifies transparency.

This identified the strongest objection to the paper's entire project and showed how the essentially-contested argument defeats it.

**The dialectical structure:**

1. *Objection (from pure cognitivism):* If ethics tracks truth, evaluate the outputs. A sound argument is sound regardless of how it was produced. Process transparency confuses discovery with justification.

2. *Defeat:* Output-evaluation in ethics is always partly process-evaluation — ethicists have no moral truth-meter; they assess whether the right considerations were weighed, the right methods followed, the right sensitivities exercised. "Evaluate the outputs" cannot be executed because there are no agreed, process-independent criteria for moral correctness.

3. *Why:* Because "ethical inquiry" is essentially contested. We don't even agree on whether ethics is in the business of tracking truth — the cognitivism dispute is the deepest instance. The cognitivist objection presupposes what is contested.

4. *Qualification:* The claim is not universal. For simple applied ethics arguments with clear premises and valid inferences, the output may suffice. The claim applies to complex work involving judgment, contested methods, and genuine philosophical insight — where AI assistance is most consequential, and where AI systems can produce outputs satisfying surface criteria without the understanding those criteria are meant to track.

**The cognitivism dispute does triple duty:** it generates the objection, illustrates the essential contestedness, and is defeated by that same contestedness.

Opus called this "the strongest version of the argument yet." Key additional finding: Section 6.1 of the v3 draft already makes the same claim in practical terms ("article evaluation never assessed merely whether arguments are valid — it always also assessed thinking quality"). Section 3 and Section 6.1 should be explicitly linked in the CFP adaptation.

---

## The Resulting Argumentative Spine

Four moves, one argument, one dialectical hinge:

**Move 1 (Literature gap):** AI in education is debated; AI in scientific research is discussed; AI in ethics research is almost unaddressed — but ethics is where the question is hardest, because what constitutes ethical inquiry is fundamentally disputed.

**Move 2 (Cognitivist objection + defeat — the hinge):**
- *Objection:* If ethics tracks truth, evaluate the outputs. Process transparency is irrelevant.
- *Defeat:* Output-evaluation in ethics is always partly process-evaluation because there are no agreed process-independent criteria for moral correctness.
- *Why:* "Ethical inquiry" is essentially contested (Gallie 1956). The cognitivism/non-cognitivism dispute is the deepest instance — we don't agree on whether ethics is in the business of tracking truth. The cognitivist objection presupposes what is contested.

**Move 3 (Pivot):** Since output-evaluation in ethics is process-dependent, and process criteria are contested, the achievable goal is tracking what ethics research is becoming under AI assistance. Tracking requires visibility; visibility requires a philosophically specified transparency framework.

**Move 4 (Contribution):** This paper provides that framework (MHC + documentation-adequacy) and demonstrates it: the paper implements the transparency apparatus it argues for.

---

## Philosophical Flags Identified

Five issues Opus flagged for the drafter:

1. "Ethical inquiry" as essentially contested needs brief support under Gallie's five criteria — do not merely assert it.
2. The cognitivism dispute as illustration requires accurate characterization. Cite canonical representatives: realism (Enoch 2011 or Shafer-Landau 2003); non-cognitivism (Gibbard 1990 or Blackburn 1993). Do not adjudicate; signal the illustration is informed.
3. Self-exemplification creates a reviewer problem: the CFP venue has no specialized infrastructure for SP-1 through SP-5. Anticipate this: the paper demonstrates what documentation-adequacy looks like; community assessment mechanisms remain to be developed.
4. "Tracking" risks quietism: gesture toward the fact that tracking creates the evidentiary basis for future normative judgment. You cannot prohibit damage you cannot see.
5. The framework is itself subject to the contestation it diagnoses. Acknowledge this (Section 6.3's experimental framing provides resources).

---

## Downstream Implications

1. **CFP Introduction (CFP_5.4.3):** Draft from scratch using the four-move spine above. Do NOT use the v1 Introduction as a template. The v1 may be consulted for Floridi references and literature citations only.

2. **Section 3 adaptation (CFP_5.4.4):** The v3 Section 3 presents the essentially-contested argument as a positive claim without confronting the cognitivist objection. The adaptation must add a subsection (working title: "Why Output-Evaluation Fails in Ethics") between "Philosophy as Essentially Contested" and "From Answer to Tracking." This subsection develops what the Introduction compresses.

3. **Section 6.1 link:** The CFP Section 6 adaptation must explicitly connect Section 6.1's thinking-quality argument to the Section 3 essentially-contested argument. They make the same claim at different levels (philosophical vs. practical).

4. **What this session did NOT produce:** A decision on Section 4 (compress vs. cut). This is deferred to after Introduction and Section 3 are finalized, when the Introduction frame will clarify how much institutional context is needed.
