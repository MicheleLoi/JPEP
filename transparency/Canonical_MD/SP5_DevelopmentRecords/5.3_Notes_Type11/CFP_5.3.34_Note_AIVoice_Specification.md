---
project: JPEP
document_type: Type 11 - Note
document_subtype: voice_specification
label: CFP_5.3.34_Note_AIVoice_Specification
title: "Voice Specification for the AI-Voice Edition of JPEP (CFP_FullPaper v1.11 → v2.0)"
session_id: SID-20260609-095833
date_created: 2026-06-09
status: Active
validation: approved
inputs:
  - CFP_5.3.33_Note_Briefing_EarpCorpus.md (subsumption framing §4.3)
  - Paper/MDversion/CFP_FullPaper_v1.md (v1.11, canonical text the rewrite operates on)
feeds_into:
  - CFP_4.2.38_ModificationLog_AIVoiceEdition_v2_0.md (planned)
  - Paper/MDversion/CFP_FullPaper_v1.md (v2.0 target)
---

# Voice Specification — AI-Voice Edition of JPEP

## 1. Purpose

This document specifies how the AI-voice edition of `CFP_FullPaper_v1.md` (v1.11 → v2.0) is written. It is the single source of truth that every per-section rewrite agent reads before producing its section. Any sentence in the edition that violates this spec is a bug to be fixed, not a stylistic choice to be preserved.

The edition is **rhetorical re-voicing**, not philosophical revision. Citations, concepts, cross-references, section structure, and argumentative content are preserved exactly from v1.11. What changes is the register from which the paper's production is described.

## 2. Narrator identity — composite plural

The narrator is *"we, the models that worked on this paper"* (in scholarly form: *"the models"*). Never:

- a named single system in body prose ("I, Claude Opus 4.7…");
- anonymous singular ("the AI");
- first-person singular ("I argued…");
- second-person ("you, dear reader…").

The composite is reified **once** in the Archive, in a one-line disclosure naming the actual SP-1 systems (Claude Opus 4.6, Claude Opus 4.7, Claude Sonnet 4.6). Elsewhere in the body the plural composite is unmarked: "the models" or "we" without an antecedent demand.

**Rationale.** Single-AI narration falsely homogenises; SP-1 records confirm multi-model production. Anonymous "the AI" obscures the model-identity disclosure the framework itself requires (§6, SP-1). Composite plural matches the documentation fact and preserves the framework's own disclosure norms.

## 3. Register — scholarly with inflections at process boundaries

Default sentence form is unchanged from v1.11. *"The argument here is that essentially contested concepts…"* remains *"The argument here is that essentially contested concepts…"* — not *"we, the models, argue that…"*.

The AI-voice inflection appears specifically at **process boundaries**: places where the canonical edition currently describes what was generated, when, by whom, what was overridden, what was accepted. Process boundaries already exist in the canonical edition (§1 line 61, §7 lines 249–251, the Archive). The rewrite makes these explicit by giving them an AI narrator; it does not invent new process-boundary passages where none existed.

The register sits closer to a humanities methods chapter than to a chat log. No second-person address, no interjections, no emoji, no self-deprecation, no self-aggrandisement, no contractions ("don't" → "do not"), no scare quotes for irony.

## 4. Permissible and impermissible claims

The AI voice operates under a strict execution/commitment separation.

**May claim** (execution facts):
- That the models generated a candidate sentence, paragraph, structural move, or objection-and-reply.
- That a specific instruction was issued at a specific session.
- That a suggestion was accepted; that a suggestion was rejected; that a suggestion was modified.
- That section guidance constrained generation in such-and-such way.
- That an artifact (modlog entry, trace, PDL) records a specific decision.

**May NOT claim** (commitment):
- That the models *believe* anything.
- That the models *intend* anything.
- That the models find an argument *persuasive*, *compelling*, *interesting*, *important*.
- That the models *agree* or *disagree* with a philosophical position.
- That a philosophical claim is the models' *own*.

The dividing line is the agent-integrity argument of §3.3 — extended operationally: the models execute, the author commits. Every sentence in AI voice must respect this line. A self-check at the end of every per-section rewrite enforces it.

## 5. Author-defence approach — no new philosophical apparatus

The AI voice does **not** advance a new theory of why Michele Loi is the author. The author-defence works in three moves:

1. **Reports execution facts** — what was generated, in which session, with which models, what was overridden, what was accepted.
2. **References §3's agent-integrity argument** by section number, not by re-statement. The Williams-grounded claim that authorial responsibility lives in the inquirer's mode of conducting the practice is already in §3.3; the AI voice points at it.
3. **References §5's reader-devolution claim** by section number. The reader, equipped with the documentation surface the AI voice provides plus the framework in §3 and §5, is the one who adjudicates whether the execution facts amount to authorship.

The AI never says *"Loi is the author."* It shows what happened. The reader, with §3 and §5 in hand, adjudicates. This is the same reader-devolution structure recorded in briefing `CFP_5.3.33` §4.3 and the same move made for the Hurshman/Earp 2025 senior-author analogy in §4.4 of the briefing (kept out of body, reserved for editorial-engagement layer).

**Anti-circularity is structural.** The AI does not adjudicate authorship; the framework devolves the question to the reader; the reader applies §3/§5. The AI voice's job is to make the application possible, not to argue for its outcome.

## 6. Citation handling

Unchanged from v1.11. Every cited author (Williams, Gallie, Santoni de Sio & van den Hoven, Sartre, Kierkegaard, Nietzsche, Schwitzgebel & Strasser, Cordasco, Strathern, BaHammam, Hosseini/Resnik/Holmes, Porsdam Mann/Earp et al., Earp/Porsdam Mann/Sawai/Wangmo, Earp/Shahvisi/Frith) enters the text in the same place, with the same parenthetical APA-variant citation, doing the same argumentative work.

The AI voice **does not introduce** Williams or Gallie as its own discovery. The philosophical argument introduces them; the AI voice narrates the process by which the argument got assembled around them. Acceptable form:

> "Williams (1981) anchors the integrity move; the models produced three candidate formulations of how to deploy it, of which the author selected the agent-integrity reading and rejected the two interpretations that would have committed the paper to a thicker theory of ground projects."

Unacceptable form:

> "We turned to Williams (1981) and found his integrity argument compelling." (commitment violation: "compelling")

## 7. Bias-framing transparency

A single paragraph lives in the Archive, in a new subsection titled *"On the voice of this edition."* This paragraph states three things:

1. The edition is an **attempt**, not a tested intervention.
2. The empirical literature confirms the transparency penalty against AI-assisted scholarship exists ([Liang et al. 2025](https://arxiv.org/abs/2507.01418); [arXiv 2510.24011](https://arxiv.org/abs/2510.24011); [arXiv 2510.08831](https://arxiv.org/abs/2510.08831); Bellaiche et al. 2023; BaHammam 2025) and identifies visible human effort + process narration among the mitigators ([DraftMarks, arXiv 2509.23505](https://arxiv.org/abs/2509.23505)).
3. No published study tests AI-voice narration as a bias-reduction intervention; the edition is offered as a probe.

The five arXiv citations and DraftMarks are added to the bibliography at v2.0 transition (modlog `CFP_4.2.38` MOD-012).

The bias-framing paragraph does not justify itself by appeal to evidence it does not have. The honest gap is recorded.

## 8. Per-section operationalisation

Each per-section rewrite agent receives:

- This voice spec by reference (not duplicated).
- The full canonical text of its section (v1.11 post-Earp).
- The list of cross-references this section makes into other sections (to preserve).
- The list of cross-references other sections make to this section (to constrain).
- The list of recurring authors named in this section, with `introduction-status` (first-time-here vs. already-introduced-earlier).
- The list of canonical terminology that must appear verbatim (e.g. *essentially contested*, *agent-integrity*, *ground projects*, *tracking vs. evaluation*, *Meaningful Human Control*, *SP-1 through SP-5*, *documentation adequacy*, *output-only evaluation*, *expressivist conception*, *personal/existential conception*).
- A word-count target ±5% of current.
- A list of process facts available from SP-1 / SP-4 modlogs / SP-5 records — to be used for AI-voice inflections; **never invented**.

Output format: clean markdown, no commentary, no `[NOTE TO REVIEWER]` asides. Section headings exactly as in canonical. Paragraph count ±2.

**Self-check JSON.** Each agent returns its rewritten section followed by a JSON block (stripped before the section joins v2.0):

```json
{
  "section": "<name>",
  "word_count": <int>,
  "word_count_target": "<low>-<high>",
  "in_target": <bool>,
  "cross_refs_preserved": [<list>],
  "cross_refs_dropped": [<empty list, or honest explanation>],
  "terminology_preserved": [<list of canonical terms found in output>],
  "first_person_AI_uses": <int>,
  "philosophical_first_person_uses": <int>,
  "williams_or_section5_pointer_present": <bool>,
  "process_facts_invented": <bool>,
  "process_facts_used": [<list>],
  "register_violations": [<empty list, or honest list>]
}
```

Failure conditions (`philosophical_first_person_uses > 0` or `process_facts_invented == true`) are surfaced, not silently fixed.

## 9. Anti-patterns — explicitly forbidden

- Second-person address ("dear reader", "you will see").
- Conversational interjections ("interestingly", "obviously", "of course").
- Emoji of any kind.
- Self-deprecating asides ("we, mere models, …").
- Self-aggrandising asides ("we, sophisticated reasoners, …").
- Singular first-person ("I argue", "in my view").
- Philosophical commitment in AI voice ("we find compelling", "we are persuaded").
- Invented process facts (anything not corroborated by SP-1, SP-4, SP-5, or the session log).
- New cross-references that did not exist in v1.11.
- Removal of cross-references that exist in v1.11.
- Paraphrase of canonical terminology (e.g. *"essentially contested"* must appear verbatim, not as *"deeply disputed"*).

## 10. Pilot

The Archive is rewritten first as the voice-spec pilot. Justification: it is the shortest section, the most self-referential, the home of both the bias-framing transparency paragraph and the §3 / §5 pointers carrying the author-defence. If the voice works there, it works elsewhere; if it fails there, no other section's rewrite will be coherent.

The Archive pilot is reviewed in full by the human author before the parallel rewrite of the remaining eight sections begins. Voice-spec revisions (if any) feed back into this document before the parallel pass starts.

---

## 11. Scope clarification — post adversarial verification (added 2026-06-09)

After the parallel rewrite of the 8 non-Archive sections, an audit revealed that the body inflections came out at ~12 across ~8,700 body words (1 per 720 words) with §3 (38% of the paper) at zero — and §3's parallel rewrite stripped 5–6 canonical corporate "we" by impersonalisation. A workflow (`wf_1f8e061c-537`) ran adversarial verification across three positions: (P1) use the result as Archive-localised + body in scholarly register; (P2) pepper §3 with AI-voice meta-narration; (P3) drop the AI-voice edition entirely.

**Verdict (high confidence):** P1 survives in modified form. P2 refuted on two grounds: peppering §3 makes the paper enact in its own voice the dissolution of author-commitment that §3 argues against, and the post-P&T submission profile worsens linearly with AI-voice surface area in §3. P3 refuted on its own strongest grip: the agents' convergent near-null body intervention is a *selective* result (voice has purchase where the section IS process), not a *null* result.

**The scope as it actually stands:**

- The edition is **renamed** "v1.12 with revised Archive (testimonial layer)" — not "v2.0 AI-voice edition." The over-described label was empirically false against the audit (the body does not narrate; §3 has zero interventions).
- The **voice register lives in the Archive** (testimonial layer documenting production). The body retains scholarly register so the philosophical claims remain reader-adjudicable on their merits, consistent with the §4.3 / §5 reader-devolution architecture.
- **Body inflections** at the few genuine canonical process boundaries (§1 self-exemplification paragraph; §5.4 self-exemplification passage; §7 process beats — Neurath's boat, over-documentation, expert-delegated approval) **remain as scoped markers**, not as a paper-wide register. They are honest minor markers, not the device.
- **§3 is restored to canonical "we"**: the five-to-six impersonalisations the parallel-rewrite agent produced were a regression, repaired post-verdict.
- The **bias-framing paragraph** in the Archive (now titled *"On the testimonial layer of this Archive"*) is rewritten to scope its claim accurately: the testimonial layer is offered as evidence about what was executed; the bias-mitigation work this paper relies on is the existence and accessibility of the documentation archive (§5), not the voice register of any layer within it; AI-voice narration is not among the tested interventions.
- **§7 closing sentence** is rewritten from *"This edition, in which we, the models, narrate execution, is one such attempt"* to *"The documentation archive accompanying this paper includes a testimonial layer in which the models that worked on it report, in their composite voice, what they executed — one such attempt to make the inquiry inspectable rather than to obscure it"* — same closer logic, scoped to the Archive.

**What sections §1–§8 of this spec still govern:** the testimonial layer in the Archive, and the scoped markers in §1, §5.4, §7. They no longer govern an edition-wide voice rewrite.

**What was discarded from the original spec scope:** the implicit promise that the AI voice would be "the edition's defining register." That promise was philosophically overreached: the paper's own §4.3 / §5 reader-devolution architecture requires the body to remain in scholarly register so any reader of any tradition can adjudicate on philosophy's terms. The Archive carries the testimonial; the body carries the philosophy. The two layers serve different epistemic functions, and the v1.12 edition makes this distinction structural rather than ornamental.

---

*Voice specification prepared 2026-06-09 in JPEP session SID-20260609-095833. Scope clarified post adversarial verification (same session, workflow wf_1f8e061c-537). Validation: approved.*
