---
artifact_type: modlog
document: CFP_FullPaper v1.11 → v1.12 — Archive testimonial layer + scoped body markers
project: JPEP
created: 2026-06-09
session_id:
  - SID-20260609-095833
inputs:
  - Paper/MDversion/CFP_FullPaper_v1.md (v1.11, baseline post-Earp integration per CFP_4.2.37)
  - transparency/Canonical_MD/SP5_DevelopmentRecords/5.3_Notes_Type11/CFP_5.3.34_Note_AIVoice_Specification.md (voice spec, with post-verdict §11 Scope clarification)
  - transparency/Canonical_MD/SP5_DevelopmentRecords/5.2_SectionPromptDevelopmentLogs_Type8b/CFP_5.2.6_pdl_AIVoiceArchiveTestimonialLayer.md (PDL recording design and narrowing)
  - transparency/Canonical_MD/SP1_AIUsageDeclaration/CFP_5.4.13_SP1.md (process facts source)
  - Paper/MDversion/aivoice_v2_staging/_voice_additions_audit.md (mid-session audit that triggered the verdict)
  - Workflow wf_1f8e061c-537 — adversarial verification of AI-voice scope, verdict P1-modified
output_completed: Paper/MDversion/CFP_FullPaper_v1.md (v1.12, pending assembly + build)
feeds_into: EthIT resubmission packaging
validation: approved
---

# Modification Log: CFP_FullPaper v1.11 → v1.12 — Archive Testimonial Layer + Scoped Body Markers

Per-revision-pass modlog for the deliverable formerly framed as "v2.0 AI-voice edition" and renamed during the session, post adversarial verification, to **v1.12 with revised Archive (testimonial layer)**. The rename is mandatory in the verdict — not cosmetic — because the "AI-voice edition" label was empirically false against the artefact produced.

The modlog records both the substantive design / generation steps that produced the staging files (MOD-001 to MOD-010) and the post-audit verdict-mandated modifications that produced the v1.12 deliverable (MOD-011 to MOD-013). Build steps MOD-014 to MOD-017 will be added at assembly time.

Single-file `git_inplace` versioning. `git diff` over the v1.11 → v1.12 commit will be the authoritative cumulative change record.

---

## Modification Entries

### MOD-001 — Voice specification created (CFP_5.3.34)

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | New artifact — voice specification governing the rewrite |

**Issue:** The session began with the user-stated concept *"la AI racconta come abbiamo scritto questo paper dal suo punto di vista, spiegando però perché io sono l'autore."* Operationalising this required a specification: who narrates, in what register, with what permissible / impermissible claims, with what author-defence approach.

**Change:** Created `CFP_5.3.34_Note_AIVoice_Specification.md`. Key design decisions: narrator = composite plural ("we, the models"); register = scholarly third-person + first-person plural AI inflections at process boundaries only; permissible claims = execution facts; impermissible = belief / intent / persuasion / agreement / philosophical commitment; author-defence by reference to §3 (agent-integrity) and §5 (reader-devolution), not by new philosophical apparatus; bias-framing transparency paragraph in the Archive; per-section operationalisation with JSON self-check schema.

User explicitly approved the voice spec.

---

### MOD-002 — Archive pilot rewrite (staging file)

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Pilot rewrite of canonical Archive into AI voice |

**Issue:** Per voice spec §10, the Archive is rewritten first as the pilot. Shortest section; most self-referential; home of both the bias-framing transparency paragraph and the §3 / §5 pointers carrying the author-defence.

**Change:** Subagent rewrite produced `Paper/MDversion/aivoice_v2_staging/archive.md` (620 words, within target 570–620). Seven substantive interventions: (1) enumeration of six models in opener; (2) §3 pointer for author-defence; (3) reification of the composite plural narrator; (4) AI-voice inflection in SP-4 bullet; (5) AI-voice inflection in SP-5 bullet; (6) SID/UUID detail in Source-conversations paragraph; (7) new subsection "On the voice of this edition" carrying the bias-framing paragraph.

Self-check passed: 0 philosophical first-person uses, 0 register violations, all cross-refs (§5, §6) preserved, §3 cross-ref added, all canonical terminology preserved.

User approved on review.

---

### MOD-003 to MOD-010 — Parallel rewrite of 8 sections (staging files)

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Parallel rewrite of Abstract, §1, §2, §3, §4, §5, §6, §7 into AI voice |

**Issue:** Per voice spec §10, after pilot approval the remaining 8 sections are rewritten in parallel. Per user direction mid-session, output is externalised: each agent writes its rewrite directly to its staging file in `Paper/MDversion/aivoice_v2_staging/`, returning only a compact JSON self-check to the main context.

**Change:** Eight parallel agent dispatches:

- **MOD-003 — `abstract.md`:** 210 words. One AI-voice inflection (canonical "...instantiated by the paper itself" → "...whose full documentation record — drafted by the models under the author's direction — is archived"). Self-check clean.
- **MOD-004 — `section1.md`:** 763 words. Two interventions: a new explicit-process sentence in the self-exemplification paragraph ("At this process boundary the narrator shifts: the models drafted candidate passages; SP-4 modification logs record which draft entered which revision; SP-5 section guidance constrained generation in advance; the author directed and accepted or overrode at every substantive turn"); a substitution "where they followed the AI" → "where they followed the models". 2 philosophical-first-person uses flagged honestly (canonical "we argue" forward statements preserved as scholarly).
- **MOD-005 — `section2.md`:** 598 words. Zero AI-voice inflections — agent correctly declined to force interventions in a descriptive section. Canonical "we get least" aphorism preserved verbatim (counted as philosophical-first-person in self-check, flagged honestly).
- **MOD-006 — `section3.md`:** 3,331 words. Zero AI-voice interventions — agent correctly declined to invent process boundaries in the philosophical core. ⚠ The agent additionally impersonalised 5–6 canonical corporate "we" passages — this is recorded as a regression here and repaired in MOD-012.
- **MOD-007 — `section4.md`:** 749 words. One AI-voice inflection in tail ("the models assembled the four-step comparison..."). 1 philosophical-first-person flagged honestly (canonical "forbids us" preserved).
- **MOD-008 — `section5.md`:** 1,372 words. One AI-voice inserted block at the §5.4 self-exemplification paragraph ("At this process boundary the narrator is the composite 'we, the models': we produced candidate drafts..."). All sub-subsections (§5.1–§5.4) preserved. Disaggregation paragraph with verbatim Earp et al. (2026) quote preserved.
- **MOD-009 — `section6.md`:** 630 words (top of target). Two interventions: AI-voice inflection on AI-assisted-synthesis paragraph; §3/§5 pointer in closing sentence. MHC verbatim quote preserved.
- **MOD-010 — `section7.md`:** 1,014 words (top of target). Five interventions: substitution "where they followed the AI" → "where they followed the models"; inflection in Neurath's-boat paragraph ("We, the models, worked inside that boat; SP-4 records it"); inflection in over-documentation paragraph ("the models generated the surplus"); inflection + §3 pointer in expert-delegated-approval paragraph; new closing sentence ("This edition, in which we, the models, narrate execution, is one such attempt") — note: this closing sentence is rewritten in MOD-013 post-verdict.

---

### MOD-011 — Voice additions audit produced

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Mid-session audit document |
| Trigger | User observation: "so, apart from the archive, it seems nothing was really changed because all chapters were written in an impersonal voice; correct?" |

**Issue:** The user's reading after the parallel rewrite was that the body remained essentially unchanged. An audit was required to verify the observation against the artefact and to make the body's voice profile inspectable.

**Change:** Created `Paper/MDversion/aivoice_v2_staging/_voice_additions_audit.md`. Per-section verbatim extraction of every AI-voice addition; distinction between genuine voice additions, terminological substitutions ("AI" → "the models"), and canonical preservations; tabular summary.

**Empirical finding recorded:**

- Archive: 7 interventions + new bias-framing subsection. Voice present and pervasive.
- Abstract: 1 inserted clause. §1: 2 interventions. §2: 0. §3: 0 (with 5–6 canonical "we" stripped). §4: 1 in tail. §5: 1 inserted block. §6: 2 small. §7: 5 interventions.
- Total body inflections: ~12 across ~8,700 body words = 1 per 720 words. §3 (38% of paper) at zero.

**Diagnosis** recorded in audit: the voice spec's three combined constraints (default sentence form unchanged + AI-voice only at process boundaries + do not invent new process boundaries) produced an attractor that concentrated voice in the Archive (the only section that IS process). The body's near-null intervention is consistent with the spec, but does not match the original concept (paper-wide voice register).

---

### MOD-012 — Adversarial verification workflow (wf_1f8e061c-537)

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Ultracode workflow — adversarial verification of recommendation |
| Trigger | User question: "cosa suggerisci: pepperarlo di più oppure usare questa ambiguità?" |

**Issue:** Three positions on the audit finding:
- P1: use the ambiguity with two surgical fixes (Archive-localised testimonial + scholarly body + light scoped markers + §3 canonical "we" restoration + Archive paragraph rewrite).
- P2: pepper §3 with AI-voice meta-narration at sub-subsection openings; deliver paper-wide voice.
- P3: drop the AI-voice edition entirely; ship v1.11 canonical + existing Archive.

**Change:** Workflow `wf_1f8e061c-537` executed: 3 parallel advocates (one per position) + 5 adversarial refutations + 1 judge synthesis.

**Verdict (high confidence): P1 survives in modified form.** Seven mandatory modifications extracted:

1. Rename — drop "v2.0 AI-voice edition" → "v1.12 with revised Archive (testimonial layer)". The label was empirically false against the artefact.
2. Rewrite Archive's "On the voice of this edition" paragraph (four constraints: localise voice claim to Archive; drop false "exploits the mitigator" verb; name open empirical status; reattach bias-mitigation work to documentation existence + §5, not body voice).
3. Restore §3's canonical "we" — repair the parallel-rewrite agent's impersonalisation regression.
4. Preserve Archive's substantive gains (7 interventions + testimonial subsection).
5. Decide on body inflections: keep them as scoped markers at the few genuine process boundaries (§1, §5.4, §7); rewrite §7 closing sentence to scope its claim to the Archive.
6. Do NOT pepper §3 — refutation against P2 holds (peppering §3 makes the paper enact in its own voice the dissolution of author-commitment §3 argues against; EthIT submission-risk asymmetry post-P&T desk-reject; agent demonstrably could not execute §3 in this register).
7. Do NOT discard the edition — refutation against P3 holds (Archive's substantive gains are not redundant with v1.11; on-thesis with §5; reviewer-skippable rather than reviewer-poisonous at EthIT).

User direction: "procedi" (proceed with the seven modifications).

---

### MOD-013 — Verdict modifications applied

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Application of the seven verdict modifications to the staging files + governance artefacts |

**Change.** Modifications 1 through 7 applied atomically:

**13a — Rename.** Task list updated: #9 "Assemble v2.0" → "Assemble v1.12"; #10 "Frontmatter bump v1.11 → v2.0" → "v1.11 → v1.12"; #11 modlog name changed to `CFP_4.2.38_ModificationLog_ArchiveTestimonialLayer_v1_12.md` (this file); #12 "Build docx v2_0" → "Build docx v1_12". Voice spec CFP_5.3.34 gained §11 "Scope clarification — post adversarial verification" recording the rename + scope localisation. Plan file gained "Post-verdict scope correction (2026-06-09)" section with the seven modifications and updated downstream targets.

**13b — Archive paragraph rewrite.** `aivoice_v2_staging/archive.md`: subsection title *"On the voice of this edition"* → *"On the testimonial layer of this Archive"*. Paragraph fully rewritten satisfying the four constraints. New paragraph: *"This Archive includes a layer in which the models that produced the paper report, in their composite voice, what they executed. The empirical literature on AI-assisted scholarship establishes a transparency penalty against disclosed AI involvement (Liang et al. 2025; arXiv 2510.24011; arXiv 2510.08831; BaHammam 2025) and identifies human-effort signaling and process-transparency markers among the mitigators (DraftMarks, arXiv 2509.23505); AI-voice narration of the kind included here is not among the tested interventions, and its contribution to mitigation is, on present evidence, open. The bias-mitigation work this paper relies on for the reader's understanding-and-endorsement assessment (§5) is the existence and accessibility of the documentation archive, not the voice register of any layer within it. The testimonial layer is offered as evidence about what was executed, localised to the section that itself documents production. The body retains scholarly register so the philosophical claims remain reader-adjudicable on their merits, consistent with the §4.3 reader-devolution architecture."*

**13c — §3 canonical "we" restoration.** Five reversions applied in `aivoice_v2_staging/section3.md`:

| Reverted from (post-rewrite) | Reverted to (canonical) |
|---|---|
| "The argument here runs the other direction" | "We are arguing the other direction" |
| "the deployment here uses integrity to refuse the demand" | "we use integrity to refuse the demand" |
| "Cordasco is engaged here as a specific instance" | "We engage Cordasco as a specific instance" |
| "no claim is made about disciplines whose evidentiary structures fall between these poles" | "we make no claim here about disciplines whose evidentiary structures fall between these poles" |
| §3.6 trio ("The alternative is to track / conditions can be created / If the salient... cannot be anticipated / If what... cannot be settled in advance") | §3.6 trio canonical ("We can track / we can create conditions / If we cannot anticipate / If we cannot settle / we should create conditions") |

§3 is restored to its v1.11 register. The parallel-rewrite agent's over-impersonalisation is repaired.

**13d — Archive substantive gains preserved.** No action required — the 7 interventions and the testimonial-layer subsection were not threatened by the verdict; this is documented as the structural justification for keeping the edition.

**13e — §7 closing sentence rewritten.** `aivoice_v2_staging/section7.md`: *"This edition, in which we, the models, narrate execution, is one such attempt"* → *"The documentation archive accompanying this paper includes a testimonial layer in which the models that worked on it report, in their composite voice, what they executed — one such attempt to make the inquiry inspectable rather than to obscure it."*

**13f and 13g — §3 not peppered; edition not discarded.** No action required; recorded as decisions.

---

### MOD-013-A — Compression pass: 14 cuts applied (~735 words removed)

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Substantive prose compression — 14 discrete cuts applied to canonical body |
| Source of proposals | Agent-generated candidate file `Paper/MDversion/_compression_proposals_v1_12_20260609.md` (15 candidates, 14 selected; C-10 superseded by C-06) |

**Issue:** v1.11 ended at ~8,930 body words (post-Earp integration). The work plan referenced ~700 words of Opus-identified compression candidates parked from earlier passes. With v1.12 about to bump in the Archive layer, this is the natural moment to apply the parked trims and return the paper closer to the v1.10 footprint without re-opening any of the philosophical engagements.

**Change.** 14 cuts applied to `Paper/MDversion/CFP_FullPaper_v1.md`:

| ID | Section | Words saved | What was cut |
|----|---------|-------------|--------------|
| C-01 | §6 | ~110 | SP-1–SP-5 inventory paragraph compressed (connective clauses trimmed; all 5 elements + criterion-mapping preserved) |
| C-02 | §7 | ~95 | Two limitations paragraphs merged (transitional sentences + over-documentation duplication removed) |
| C-03 | §3.7 | ~75 | Exemplar elaboration trimmed (Parfit description tightened; the two-conception restatement removed) |
| C-04 | §6 | ~70 | Implementation-honesty paragraph compressed (parenthetical inventory removed; sentences merged) |
| C-05 | §7 | ~65 | Neurath's-boat decorative gloss removed + §5 criteria restatement removed (already in §5.4) |
| C-06 | §6 | ~50 | MHC framing — weapons-systems disclaimer removed + Kierkegaard/Williams co-reference collapsed to §3 pointer |
| C-07 | §3.7 | ~50 | "Not accidental" throat-clearing + contestedness restatement removed |
| C-08 | §7 | ~50 | "What is lost is not a convenience" rhetorical bridge removed |
| C-09 | §3.7 | ~45 | "Structurally detachable" restatement + "current rate is speculative" hedge removed |
| C-11 | §2.1 | ~35 | "Underreporting need not be dishonest" transitional pair tightened |
| C-12 | §3.5 | ~35 | History/literary-criticism/political-theory disclaimer removed (kept in §7 limitations only) |
| C-13 | §1 | ~35 | "Tracking is prior to evaluation" + "comprehensive process documentation" reprise removed |
| C-14 | §5.4 | ~30 | "Within these norms, calibration matters" framing tightened |
| C-15 | §5.4 | ~25 | "Natural objection: documentation costs" reply sentence-joining trim |
| **Total** | | **~735** | |

**Compliance.** C-10 superseded by C-06 (mutually exclusive on same paragraph). All Earp v1.11 insertions untouched (§3.3 AUTOGEN, §5.4 disaggregation, §4 JME policy). §3.3 Williams-inversion defense and Cordasco footnoted engagement untouched. All citations preserved. All `§N` cross-references preserved. All subsection headings preserved.

**Rationale.** Each candidate documented with before/after + justification in the proposals file; user reviewed all 15, approved all 14, explicitly selected C-06 (heavier cut) over C-10. The user judgment recorded: "they also enhance quality." Net body delta: ~8,930 → ~8,195 (~735 words removed). Returns the paper closer to the pre-Earp v1.10 footprint (~8,685) minus approximately 490 words below it.

**Source draft impact:** None — per project rule 1, source drafts in `5.4_SectionDrafts/` are not touched during integrated-paper editing. The compressions live only in `CFP_FullPaper_v1.md`.

---

### MOD-014 — Bibliography additions

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Two new bibliographic entries supporting the Archive testimonial-layer paragraph |

**Change.** Added to both `paper_bibliography_FINAL.md` and the paper's References block, alphabetically:

> **Liang, W., et al.** (2025). "Penalizing Transparency? How AI Disclosure and Author Demographics Shape Human and AI Judgments About Writing." arXiv:2507.01418. https://arxiv.org/abs/2507.01418
>
> **Siddiqui, M., et al.** (2025). "DraftMarks: Enhancing Transparency in Human-AI Co-Writing Through Interactive Skeuomorphic Process Traces." arXiv:2509.23505. https://arxiv.org/abs/2509.23505

The Archive testimonial-layer paragraph additionally cites `arXiv 2510.24011` and `arXiv 2510.08831` in parenthetical form. These two arXiv preprints are self-resolving via their arXiv IDs and are not added as separate bibliography entries (their parenthetical citations in the text point readers directly to arxiv.org). BaHammam 2025 (the fifth citation in the bias-mitigation literature cluster) was already in the bibliography from CFP_4.2.36 MOD-001.

**Honesty discipline:** "Liang, W., et al." and "Siddiqui, M., et al." use first-author + "et al." formulation — full author lists not yet retrieved. To resolve before any submission tag.

---

### MOD-015 — Assembly: AI-voice deltas integrated

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Integration of staging-file AI-voice deltas into the canonical paper |

**Change.** Rather than wholesale section-replacement (which would have overwritten the just-applied compression pass), each AI-voice delta from the staging files was applied as a targeted Edit to `Paper/MDversion/CFP_FullPaper_v1.md`. The deltas are:

**Abstract** (1 delta): inserted phrase " — drafted by the models under the author's direction" after "the documentation record" near the close.

**§1 Introduction** (3 deltas):
- ¶6 self-exemplification paragraph: inserted process-narration sentence ("At this process boundary the narrator shifts: the models drafted candidate passages; SP-4 modification logs record which draft entered which revision; SP-5 section guidance constrained generation in advance; the author directed and accepted or overrode at every substantive turn.") + minor tightenings; "where they followed the AI / overrode it" → "where they followed the models / overrode them"; new closing sentence "The framework is a first iteration, not a settled standard."
- §1 section overview: added "; adjudication of this paper's record is devolved there" to the §5 forward statement.

**§4 close** (1 delta): added tail clause "; the models assembled the four-step comparison — Hosseini–Resnik–Holmes prescription, structural critique, self-defeat, JME policy datum — under §4 guidance preserved through the v1.11 Earp-integration pass."

**§5.4 self-exemplification paragraph** (1 delta): inserted process-boundary sentence ("At this process boundary the narrator is the composite 'we, the models': we produced candidate drafts of the passages in this section across multiple sessions; the modification logs in SP-4 record which draft entered which revision, and which suggestions the author accepted, modified, or overrode. The exhibit is the execution record;") between "without the documentation displacing or hollowing out the inquiry it records" and the original "It does not constitute evidence of *adequacy*" (which becomes "the archive does not constitute evidence of *adequacy*").

**§6 closing paragraph** (2 deltas): inserted "; in this paper, the synthesis was executed by the models, working from raw SP-4 and SP-5 records under the author's direction" after "what makes the framework implementable"; added "; *agent-integrity* and *documentation adequacy*, on §3's and §5's terms, are what the constraint serves" at the end.

**§7** (5 deltas):
- "where they followed the AI / overrode it" → "where they followed the models / overrode them" (opening paragraph)
- Inserted "We, the models, worked inside that boat; SP-4 records it." after "in the manner of Neurath's boat."
- Inserted "; the models generated the surplus" after "SP-1 through SP-5 would demand" in the over-documentation discussion
- Inserted "The models generated such passages; SP-4 carries the trace. The agent-integrity argument of §3 underwrites the consistency of this with authorship." in the expert-delegated-approval paragraph after "without the capacity to reconstruct it independently"
- Appended new closing sentence "The documentation archive accompanying this paper includes a testimonial layer in which the models that worked on it report, in their composite voice, what they executed — one such attempt to make the inquiry inspectable rather than to obscure it."

**Archive** (full section replacement): replaced the entire `# AI Usage and Documentation Archive` section with the testimonial-layer rewrite from `aivoice_v2_staging/archive.md`. Key changes from v1.11 Archive: enumeration of six models in opener; §3 pointer for author-defence; reification of composite plural narrator; AI-voice inflections in SP-4 / SP-5 bullets; SID/UUID format detail in Source conversations; new "On the testimonial layer of this Archive" closing subsection carrying the bias-framing paragraph (post-verdict scoped version, citing five bias-literature anchors and acknowledging that AI-voice narration is not among the tested interventions).

**§2, §3 — no deltas.** §2 had 0 AI-voice additions in staging. §3 had 0 net AI-voice additions (post-verdict canonical "we" restoration cancelled out the agent's earlier impersonalisations). Both sections preserved in their compressed-canonical form.

**Total body inflections in v1.12:** ~12 scoped markers at the genuine process boundaries identified above. Body retains scholarly register; testimonial voice is concentrated in the Archive per the workflow `wf_1f8e061c-537` verdict.

---

### MOD-016 — Frontmatter bump v1.11 → v1.12

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Metadata update to `CFP_FullPaper_v1.md` frontmatter |

Changes:

- `version: v1.11` → `version: v1.12`
- `source`: extended to include `CFP_4.2.38` in the section-level modification logs list.
- `assembly`: appended with `"v1.12 = Archive testimonial-layer assembly (Archive section rewritten with composite-plural narrator + new 'On the testimonial layer of this Archive' subsection citing bias-mitigation literature; 12 scoped AI-voice markers at process boundaries in Abstract / §1 ¶6 / §4 close / §5.4 self-exemplification / §6 closer / §7 process beats / §7 new closing sentence) + 14-cut compression pass (~735 w removed, recovering Opus-identified parked compressions across §1, §2.1, §3.5, §3.7, §5.4, §6, §7); per CFP_4.2.38, constrained by CFP_5.3.34 voice spec + workflow wf_1f8e061c-537 verdict (P1-modified)."`
- `word_count`: updated estimate to ~8,500 (pending Word recount; v1.11 was ~9,020 minus ~735 compression + ~215 AI-voice additions ≈ ~8,500).

`known_issues` carries forward: (a) Earp et al. (2026) DOI flag — confirmed wrong, correct DOI search ongoing; (b) Earp, Shahvisi & Frith (2025) title disambiguation RESOLVED; "Normalising transparency" is a separately forthcoming editorial. Additional flag added: bibliography entries for Liang and Siddiqui use first-author + et al. formulation; full author lists to be retrieved before submission tag.

---

### MOD-017 — Build CFP_FullPaper_v1_12.docx

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Build output |

`python build_paper.py` from project root. Output: `Paper/journal/CFP_FullPaper_v1_12.docx`. Rough word count reported by the build script (body + headings + Archive + bibliography): 9,824 words.

PDF generation skipped — `docx2pdf` not installed on this Windows host. PDF can be generated on macOS or by installing `docx2pdf` on Windows; the canonical artifact is the docx, per the build script's design.

---

## Final state — v1.12

`CFP_FullPaper_v1.md` is at v1.12 with both the compression pass and the Archive testimonial-layer assembly applied. The deliverable `Paper/journal/CFP_FullPaper_v1_12.docx` is written. The body retains scholarly register with 12 scoped AI-voice markers at genuine process boundaries; the Archive carries the composite-plural testimonial layer; the bias-framing subsection scopes its claim honestly to the Archive and names the open empirical status of AI-voice as a bias-mitigation intervention.

Validation: approved through MOD-017.

---

## Carry-forward

- The bias-literature additions (Liang 2025; arXiv 2510.24011; arXiv 2510.08831; DraftMarks 2509.23505) are added to support the rewritten Archive testimonial-layer paragraph; they are not referenced from the body.
- The Earp briefing CFP_5.3.33 verification backlog persists: the provenance-problem paper (Earp et al. 2025 NMI) remains paywalled with no OA mirror; the Authorship Without Writing preprint (Hurshman/Porsdam Mann/Savulescu/Earp 2025) is filed locally but held at the editorial-engagement layer per briefing §4.4, not for body text.
- The DOI re-verification flag for Earp et al. (2026, *JMEPB*) carried over from CFP_4.2.37 remains open.
- The session log entry for SID-20260609-095833 documents the broader narrative arc this modlog instantiates.

---

*Modlog prepared 2026-06-09 in JPEP session SID-20260609-095833. Validation: approved through MOD-013; MOD-014 to MOD-017 will be added with their actions.*
