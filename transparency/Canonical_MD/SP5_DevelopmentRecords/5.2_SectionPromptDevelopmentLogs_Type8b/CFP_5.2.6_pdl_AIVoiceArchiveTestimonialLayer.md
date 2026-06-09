---
project: JPEP
sp: SP5
artifact_type: pdl
document_type: Type 8b - Section Prompt Development Log
label: CFP_5.2.6_pdl_AIVoiceArchiveTestimonialLayer
title: "PDL: Archive Testimonial Layer + Scoped Body Markers (v1.11 → v1.12)"
created: 2026-06-09
last_updated: 2026-06-09
status: Active
session_id: SID-20260609-095833
inputs:
  - "transparency/Canonical_MD/SP5_DevelopmentRecords/5.3_Notes_Type11/CFP_5.3.33_Note_Briefing_EarpCorpus.md (subsumption framing §4.3)"
  - "transparency/Canonical_MD/SP5_DevelopmentRecords/5.3_Notes_Type11/CFP_5.3.34_Note_AIVoice_Specification.md (voice spec — functional surrogate for per-section prompt template)"
  - "Paper/MDversion/CFP_FullPaper_v1.md (v1.11, canonical text)"
  - "User-stated original concept: 'la AI racconta come abbiamo scritto questo paper dal suo punto di vista, spiegando però perché io sono l'autore'"
feeds_into:
  - "CFP_4.2.38_ModificationLog_ArchiveTestimonialLayer_v1_12.md"
  - "Paper/MDversion/aivoice_v2_staging/archive.md (testimonial layer)"
  - "Paper/MDversion/aivoice_v2_staging/section1.md, section5.md, section7.md (scoped body markers)"
  - "Paper/MDversion/CFP_FullPaper_v1.md (v1.12 target)"
source_conversations:
  - session: SID-20260609-095833
    exported_as: TBD (pending /mhc-end)
related:
  - "CFP_5.2.5_pdl_AIUsageArchive.md (precedent: the v1.11 Archive that the testimonial layer extends)"
  - "Workflow wf_1f8e061c-537 (adversarial verification of the AI-voice scope; verdict P1-modified)"
  - "Paper/MDversion/aivoice_v2_staging/_voice_additions_audit.md (the audit that prompted the verdict)"
validation: approved
versioning_convention: git_inplace
---

# PDL: Archive Testimonial Layer + Scoped Body Markers (v1.11 → v1.12)

## Overview

This PDL is retrospective. It documents the prompt-development decisions that produced the v1.12 deliverable — Archive testimonial layer + scoped body markers — across a session in which a more ambitious target ("v2.0 AI-voice edition") was attempted, audited, adversarially verified, and narrowed.

The functional prompt template was the voice specification `CFP_5.3.34_Note_AIVoice_Specification.md`. This PDL records the higher-altitude design decisions: what to generate, what alternatives were considered, why this approach landed, and where the original concept was honestly narrowed mid-session.

The PDL substitutes for a separate epistemic trace by recording both "how the design decisions were reached" (PDL-001–003) and "what was specified for generation" (PDL-004–005), plus the post-execution audit and scope correction (PDL-006–007).

---

## PDL-001 — Concept origin: an AI-voice edition of the paper

| Date | Session | Authored by |
|---|---|---|
| 2026-06-09 | SID-20260609-095833 | User direction; Claude Opus 4.7 analysis |

**Concept.** The user stated the original concept verbatim: *"vorrei che provassi a fare riscrivere (con agenti con contesto puntuale, che lavorano sezione per sezione, da te coordinati) il saggio nella voce della AI. […] La AI racconta come abbiamo scritto questo paper dal suo punto di vista, spiegando però perché io sono l'autore."*

**Rhetorical motivation.** The user asked the search to surface psychological-bias research on AI-assisted writing. A pre-print he recalled — claiming that AI-voice narration reduces prejudice against AI-assisted content — would be the empirical anchor. If unconfirmed, the move is framed as an attempted application of mitigators the empirical literature identifies (visible human effort + process-transparency markers).

**Search verdict (Explore agent).** The specific pre-print does not exist as an indexable paper. Five solid empirical anchors confirmed: Liang et al. 2025 (arXiv 2507.01418, ~0.15 transparency penalty on 7pt scale); arXiv 2510.24011 (N=261 reader-perception shifts on disclosure); arXiv 2510.08831 ("everyone prefers human writers, including AI"); Bellaiche et al. 2023 (bias against AI-generated content); BaHammam 2025 (transparency paradox); DraftMarks arXiv 2509.23505 (process-transparency markers as mitigator). Literature establishes the penalty is real and identifies visible human effort as a mitigator; does **not** test AI-voice narration specifically.

**Authorship-defence approach decided in pre-design.** The user's instruction *"spiegando però perché io sono l'autore"* was further refined by the user during the design phase: the AI-voice edition must NOT advance a new theory of authorship; the author-defence relies on §3's agent-integrity argument and §5's reader-devolution claim already in the paper, with the AI voice providing the evidentiary surface for the reader's adjudication. This eliminated an early proposal to add a "candidate-evaluation pattern" Williams-based defence as a new philosophical move; the user judged that move would introduce new philosophical material the canonical edition does not need (briefing CFP_5.3.33 §4.3 anchored this constraint).

---

## PDL-002 — Voice specification design (CFP_5.3.34)

| Date | Session | Authored by |
|---|---|---|
| 2026-06-09 | SID-20260609-095833 | Claude Opus 4.7 drafting; user approval |

**Design decisions made in the voice spec:**

- **Narrator identity:** composite plural ("we, the models that worked on this paper"). Rejected: single named model ("I, Claude Opus 4.7") on grounds that SP-1 records multi-model production (six models across project lifetime: Sonnet 4.5, Sonnet 4.6, Opus 4.5, Opus 4.6, Opus 4.7, GPT-5 Thinking). Rejected: anonymous "the AI" on grounds that it obscures the model-identity disclosure the framework itself requires.
- **Register:** scholarly third-person + first-person plural AI inflections at process boundaries only. Default sentence form unchanged from v1.11. Closer to a humanities methods chapter than to a chat log. No contractions, no interjections, no emoji, no scare quotes for irony.
- **Permissible / impermissible claims:** strict execution / commitment separation. The models execute; the author commits. The models may report what was generated, in what session, with what model. The models may not claim belief, intent, persuasion, agreement, philosophical commitment.
- **Citation handling:** unchanged. Williams, Gallie, Santoni de Sio, etc. enter the text as in canonical. The AI voice narrates the process by which the argument got assembled around them; it does not "introduce" them as the models' own discovery.
- **Bias-framing transparency paragraph:** a single paragraph in the Archive ("On the voice of this edition") states three things: the edition is an attempt, not a tested intervention; the empirical literature establishes the transparency penalty and identifies visible-human-effort mitigators; no published study tests AI-voice narration specifically.
- **Per-section operationalisation:** each per-section agent receives a JSON self-check schema enforcing the constraints (philosophical_first_person_uses MUST be 0; process_facts_invented MUST be false; cross-references preserved; canonical terminology verbatim).
- **Pilot strategy:** Archive rewritten first. Shortest section, most self-referential, home of both the bias-framing paragraph and the §3/§5 pointers carrying the author-defence. Human-review gate before parallel rewrite of remaining 8 sections.

User explicitly approved the voice spec ("I approve the voice specification").

---

## PDL-003 — Per-section prompt template design

| Date | Session | Authored by |
|---|---|---|
| 2026-06-09 | SID-20260609-095833 | Claude Opus 4.7 drafting; user approval |

**Common scaffold for the 8 non-Archive agents:**

Each agent received:
- Voice spec by reference (not duplicated in prompt — load by file read).
- Reference to the Archive pilot for calibration.
- Full canonical text of its section (read from `Paper/MDversion/CFP_FullPaper_v1.md` v1.11).
- Cross-references in / out (preserve all `§N` references).
- Canonical terminology list (verbatim preservation).
- Recurring authors list (consistent APA-variant introduction).
- Word-count target (±5% of canonical section count).
- Process facts available (SP-1 phases + model list + role distribution).
- Output path: `Paper/MDversion/aivoice_v2_staging/<filename>.md`.
- JSON self-check schema (per voice spec §8) — failure conditions surfaced not silently fixed.

**Externalisation decision.** Mid-session the user directed: *"le prossime rewrite non nel contesto main: esternalizza scrivendo su progetto come md e fammi leggere lì."* Each per-section agent writes its rewrite directly to its staging file; the main context receives only the compact JSON self-check. This decision was governance-driven (preserve main-context for orchestration; let the user review at native pace in their editor) and is preserved in `_voice_additions_audit.md`.

**Section-specific deltas (high level):**
- *Abstract* (210w target ±5%): very low process-narration scope; expect 0–1 inflection.
- *§1* (729w): high process-narration scope; corporate "we" forward statements may stay scholarly, self-exemplification paragraph is the natural site for AI-voice.
- *§2* (598w): descriptive section; resist forcing AI-voice; agent licensed to return 0 inflections if no process boundary surfaces.
- *§3* (3,339w post-A1 expansion; 38% of paper): philosophical core, 7 sub-subsections; preserve canonical "we" passages as scholarly forward statements; the AUTOGEN paragraph in §3.3 close is load-bearing — re-voice minimally.
- *§4* (716w post-A3): meta-argument; thin process-narration scope; preserve JME paragraph substance.
- *§5* (1,320w post-A2): community-assessment framework; self-exemplification at §5.4 is a natural inflection site; preserve verbatim Earp et al. (2026) quote.
- *§6* (600w): apparatus specification; the AI-assisted-synthesis closing paragraph is the natural inflection site; preserve MHC verbatim quote.
- *§7* (1,014w): high process-narration; multiple canonical self-exemplification beats licence AI-voice inflection; the closing sentence is the natural site for a meta-statement about the edition.

---

## PDL-004 — Generation specification: Archive pilot

| Date | Session | Authored by |
|---|---|---|
| 2026-06-09 | SID-20260609-095833 | Claude Opus 4.7 drafting (subagent); user approval |

**Specification for the Archive pilot (the first rewrite executed):**

- Re-voice canonical Archive content per voice spec §3 and §4 (composite plural at process boundaries; default sentence form unchanged).
- Add explicit §3 pointer for the author-defence (canonical Archive does not currently make this explicit; the AI-voice edition's defence operates by pointer to §3, not by re-statement).
- Add new subsection *"On the voice of this edition"* (later renamed to *"On the testimonial layer of this Archive"* — see PDL-007) carrying the bias-framing transparency paragraph.
- Reify the composite plural ONCE in the Archive (name the six models in the opener); do not re-enumerate elsewhere.
- Word-count target: existing ~452 + ~120 bias-framing = ~570–620.
- Process facts: drawn from SP-1 table (phases, platforms, models, roles). Never invented.

The pilot returned 620 words (top of target), self-check clean (0 philosophical first-person, 0 register violations, all cross-refs preserved). User approved the voice on the pilot ("approvo"), then directed externalisation of subsequent rewrites.

---

## PDL-005 — Generation specification: parallel rewrite of 8 sections

| Date | Session | Authored by |
|---|---|---|
| 2026-06-09 | SID-20260609-095833 | Claude Opus 4.7 orchestration; 8 subagents executing |

**Execution.** Eight parallel agent dispatches, one per section. Each agent read the voice spec, read its section from canonical, rewrote per the common scaffold + section-specific delta (PDL-003), wrote output to its staging file, returned JSON self-check.

**Self-check results (compact summary):**

| Section | Word count | In target | Phil first-person uses | Process facts invented |
|---|---:|---|---:|---|
| Abstract | 210 | ✓ | 0 | false |
| §1 | 763 | ✓ | 2 (flagged honestly — corporate forward statements) | false |
| §2 | 598 | ✓ | 1 (canonical aphorism "we get least" preserved verbatim) | false |
| §3 | 3,331 | ✓ | 0 | false |
| §4 | 749 | ✓ | 1 (canonical "forbids us" preserved verbatim) | false |
| §5 | 1,372 | ✓ | 0 | false |
| §6 | 630 | ✓ | 0 | false |
| §7 | 1,014 | ✓ | 0 | false |

All within target; no invented process facts; cross-refs and terminology preserved.

---

## PDL-006 — Audit, narrowed scope, adversarial verification

| Date | Session | Authored by |
|---|---|---|
| 2026-06-09 | SID-20260609-095833 | User-prompted audit (Claude Opus 4.7); workflow wf_1f8e061c-537 |

**Audit triggered by user observation.** Post-rewrite, the user observed that apart from the Archive, the body read essentially unchanged: *"so, apart from the archive, it seems nothing was really changed because all chapters were written in an impersonal voice; correct?"*

**Audit (`_voice_additions_audit.md`)** confirmed: body received ~12 inflections across ~8,700 body words (~1 per 720 words). §3 (38% of paper) received zero interventions AND the parallel-rewrite agent had stripped 5–6 canonical corporate "we" by impersonalisation — §3 came out colder than v1.11.

**Diagnosis.** The voice spec's three combined constraints (default sentence form unchanged; AI-voice only at process boundaries; do not invent new process boundaries) had produced an attractor. The canonical's few process boundaries became the only sites for voice. The spec under-delivered against the original concept ("la AI racconta come abbiamo scritto questo paper").

**User question (the choice point):** *"cosa suggerisci: pepperarlo di più oppure usare questa ambiguità?"*

**Adversarial verification workflow.** Under Ultracode, candidate recommendation (P1: use the ambiguity with two surgical fixes) was tested against five adversarial refutations targeting the three positions (P1 vs P2 pepper more vs P3 abandon). Verdict: **P1-modified survives with high confidence**. P2 refuted on submission-risk + commitment-collapse grounds; P3 refuted on the Archive's substantive gains. P1 accepted with the concession that the edition must be renamed (the "v2.0 AI-voice edition" label was empirically false against the artefact).

---

## PDL-007 — Final generation specification (post-verdict)

| Date | Session | Authored by |
|---|---|---|
| 2026-06-09 | SID-20260609-095833 | Verdict from wf_1f8e061c-537; user direction "procedi" |

**The seven verdict-mandated modifications constitute the actual generation specification for the v1.12 deliverable:**

1. **Rename.** Drop "v2.0 AI-voice edition" → "v1.12 with revised Archive (testimonial layer)". Edition framing accurately scoped.
2. **Rewrite the Archive's bias-framing paragraph.** Title: *"On the voice of this edition"* → *"On the testimonial layer of this Archive"*. Four binding constraints on the rewrite: (a) localise voice claim to the Archive; (b) drop the false "exploits the mitigator" verb; (c) name the open empirical status; (d) reattach bias-mitigation work to documentation existence and §5, not body voice.
3. **Restore §3's canonical corporate "we"** in `section3.md` staging — the parallel-rewrite agent's impersonalisation of 5–6 canonical passages was a regression to be repaired.
4. **Preserve Archive's substantive gains:** 7 substantive interventions + testimonial-layer subsection.
5. **Keep body inflections at the few genuine process boundaries** (§1 self-exemplification; §5.4 self-exemplification; §7 process beats — Neurath's boat, over-documentation, expert-delegated approval) as **scoped markers**, not as a register. Rewrite the §7 closing sentence to scope its claim to the Archive: *"This edition, in which we, the models, narrate execution, is one such attempt"* → *"The documentation archive accompanying this paper includes a testimonial layer in which the models that worked on it report, in their composite voice, what they executed — one such attempt to make the inquiry inspectable rather than to obscure it."*
6. **Do NOT pepper §3.** Peppering §3 with "we, the models" meta-narration makes the paper enact in its own voice the dissolution of author-commitment §3 argues against; the EthIT submission-risk asymmetry post-P&T desk-reject strictly dominates the marginal bias-mitigation gain; the agent demonstrably could not execute §3 in this register in one pass.
7. **Do NOT discard the edition.** The Archive's substantive gains — testimonial layer + bias-framing — are not redundant with v1.11's inventory Archive, are on-thesis with §5 reader-devolution, and are reviewer-skippable rather than reviewer-poisonous at EthIT.

All seven modifications were applied 2026-06-09 in SID-20260609-095833; the staging files in `Paper/MDversion/aivoice_v2_staging/` are now ready for assembly into `Paper/MDversion/CFP_FullPaper_v1.md` as v1.12.

---

## Why this PDL is honest about narrowing

The original user concept implied a paper-wide voice register; the deliverable is an Archive-localised testimonial layer plus scoped markers in three other sections. This PDL records the narrowing explicitly — as a documented design decision driven by:

- Empirical evidence from the parallel rewrite (the agents converged on a near-null body intervention under the original spec).
- An adversarial verification verdict (P2 "pepper more" refuted on multiple independent grounds).
- The paper's own §4.3 architecture (the body must remain in scholarly register so the reader can adjudicate philosophy on its own terms; the testimonial layer is the executing-layer's evidence, not a competing voice over the philosophy).

The honest framing is not an admission of failure; it is the recognition that the voice spec's constraints produced the right shape, and that the original concept's "edition-wide voice" was philosophically incompatible with what the paper itself argues for. Narrowing in this case is correctness, not retreat.

---

*PDL prepared 2026-06-09 in JPEP session SID-20260609-095833. Validation: approved.*
