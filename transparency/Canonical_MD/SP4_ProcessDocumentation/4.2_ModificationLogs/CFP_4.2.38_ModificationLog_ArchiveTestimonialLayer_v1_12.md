---
artifact_type: modlog
document: CFP_FullPaper v1.11 → v1.16 — Archive testimonial layer, compression, Earp-cluster in-text engagement, author-position registration, reference audit
project: JPEP
created: 2026-06-09
session_id:
  - SID-20260609-095833
inputs:
  - Paper/MDversion/CFP_FullPaper_v1.md (v1.11, baseline post-Earp integration per CFP_4.2.37)
  - transparency/Canonical_MD/SP5_DevelopmentRecords/5.3_Notes_Type11/CFP_5.3.34_Note_AIVoice_Specification.md (voice spec, with post-verdict §11 Scope clarification)
  - transparency/Canonical_MD/SP5_DevelopmentRecords/5.2_SectionPromptDevelopmentLogs_Type8b/CFP_5.2.6_pdl_AIVoiceArchiveTestimonialLayer.md (PDL recording design and narrowing)
  - transparency/Canonical_MD/SP1_AIUsageDeclaration/CFP_5.4.13_SP1.md (process facts source)
  - Paper/MDversion/aivoice_v2_staging/_voice_additions_audit.md (mid-session audit that triggered the AI-voice verdict)
  - Workflow wf_1f8e061c-537 — adversarial verification of AI-voice scope, verdict P1-modified
  - transparency/TEMP/death_authorship_revised_final_acad.pdf (Earp/Porsdam Mann/Sawai/Wangmo 2026, DA editorial — read in full)
  - transparency/TEMP/Meta-Authorship_Draft12ACAD.pdf (Earp/Guernon/Porsdam Mann 2026, SHC self-test essay — read in full)
  - Workflow wf_899bd25b-c09 — adversarial verification of author-position disclosure, verdict P-OMIT-modified
  - target-venue/jmepb_commentary_proposal.md (the author-position defense, kept out of the paper body, sole defended venue)
output_completed: Paper/MDversion/CFP_FullPaper_v1.md (v1.13)
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

## State at v1.12

`CFP_FullPaper_v1.md` reached v1.12 with both the compression pass and the Archive testimonial-layer assembly applied. The body retains scholarly register with 12 scoped AI-voice markers at genuine process boundaries; the Archive carries the composite-plural testimonial layer; the bias-framing subsection scopes its claim honestly to the Archive.

Validation: approved through MOD-017.

---

### MOD-018 — v1.12 → v1.13: Earp-cluster in-text engagement + author-position registration + pandoc build engine

| Field | Value |
|-------|-------|
| Date | 2026-06-10 |
| Type | Substantive scholarly engagement (§5.4 in-text) + author-position registration (Archive) + build-infrastructure change |
| Trigger | Author's direct reading of both Earp-cluster preprints and the Gallian insight: "gli editors non convergono su una lettura univoca collima con l'idea di Gallie, che si tratti un contested concept; la nostra idea però è qualcosa di originale" |
| Verification | Both preprints read in full from local PDFs: `transparency/TEMP/death_authorship_revised_final_acad.pdf` (DA editorial) and `transparency/TEMP/Meta-Authorship_Draft12ACAD.pdf` (SHC self-test essay), by author and by Claude Opus 4.8. The §5.4 verbatim DA quote was re-checked against the revised-final body and confirmed unchanged. |

**Context — two papers, both forthcoming JME Practical Bioethics 2026:**
- DA = Earp, Porsdam Mann, Sawai & Wangmo, "Death, authorship, and generative AI — a call for commentaries" (already cited §5.4 since v1.11).
- SHC = Earp, Guernon & Porsdam Mann, "A substantial human contribution: Do we deserve to be authors of this essay?" — a self-test essay written with LLM assistance in ~48h, claiming authorship while marking it contestable and attaching a full production record (own DOI'd supplemental file). SHC's own footnote 1 records a submission history (AJOB desk-reject for scope → resubmission to Neuroethics) — a structural rhyme with JPEP's own P&T → EthIT path; recorded here as process observation, not in the citation (which follows SHC's cite-as box: "Preprint", not formally peer reviewed).

**18a — §5.4 in-text extension.** A new paragraph appended to the §5.4 close, after the existing DA-citation paragraph. Per the author's instruction the Earp engagement is **in-text, not footnoted** (the call for commentaries is an official editorial act meriting body treatment). Content: (i) the DA editorial catalogues five candidate conceptions (composition, ideation, direction, sustained engagement, accountability), observes each "has arguments in its favour," and declines to adjudicate — a call for commentaries is how a discipline behaves toward an essentially contested concept; (ii) the **two-level contestation** point — even were one criterion agreed (substantial human contribution), what counts as *substantial* would remain divided, as SHC concedes ("contested middle," "discipline-specific standards"); (iii) SHC performs the response in miniature (claims authorship, marks contestable, attaches production record — devolving the verdict with process evidence); (iv) JPEP's contribution framed as "not a sixth candidate answer" but the specification of what a disclosed record must enable; (v) the **enforceability point inline** (not footnote): SHC doubts disclosure could be *required* without perverse incentives — §2 locates those incentives, §§4–5 specify the format conditions that neutralise the disclosure penalty. Also corrected: "writing in the inaugural issue of *JME Practical Bioethics*" → "in a forthcoming *JME Practical Bioethics* editorial" (the journal is at vol. 2; what is inaugural is the call-for-commentaries format, not the issue). Net ~+235 w.

**Constraint compliance:** the paragraph is framework-level — it engages the cluster and asserts JPEP's contribution without adjudicating which conception of authorship is correct. Briefing §4.3/§4.4 respected: "not a sixth candidate answer" is the explicit non-adjudication.

**18b — Archive author-position registration.** New block in the Archive note ("The author's operative conception of authorship") between "Scope and limits" and "On the testimonial layer of this Archive." This is the surviving residual of workflow `wf_899bd25b-c09` (adversarial verification of whether/where to disclose the author's personal position), verdict **P-OMIT-modified, high confidence**: the body stays position-free; the full defense goes to the JMEPB commentary; a **registration-only** disclosure goes in the Archive record register. The block contains exactly five elements and no argument: (a) names the conception (accountability: presenting oneself as author = first-person commitment to stand behind the claims + justify on request); (b) marks it contested, names live opposition (Levy 2025); (c) names the congeniality (the §6 tracing condition is close kin — which is *why* disclosure is owed); (d) the swap test (a composition- or sustained-engagement-theorist can use the same SP-1–SP-5 record to deny the author authorship of this very paper); (e) "The conception is not defended here" — no forward-promise of the commentary. Net ~+120 w.

**Why P-ADD (a §7 defended paragraph) was rejected:** both adversarial refutations landed — (1) briefing §4.4 is a placement rule stricter than inferential dependence (the senior-author analogy was barred from the body despite carrying no inferential load), so a §7 paragraph stating the conception + rebutting the DA objection + conceding a wrinkle would be three argumentative moves in the same authorial voice that elsewhere disclaims endorsing any candidate model; (2) the de dicto/de re editor-objection reply faces a genuine dilemma (strong reading refuted by the ICMJE-statistician case inside the DA editorial + Levy 2025; weak reading collapses into the editor's process-directed commitment) that 175 words cannot secure. The reply and the recursive AI-aided-justification wrinkle are reserved for the commentary, where they have room to survive.

**18c — SHC bibliography entry.** Added to `paper_bibliography_FINAL.md` and the paper's References block, alphabetically before the DA entry (Guernon < Porsdam Mann): `Earp, B. D., Guernon, A.-S., & Porsdam Mann, S. (2026). "A substantial human contribution: Do we deserve to be authors of this essay?" Preprint. https://www.researchgate.net/publication/403018576`. Citation follows SHC's own cite-as box.

**18d — known_issues update.** The SHC "deferred engagement" flag is resolved (now cited §5.4 after full body-text read). Replaced with a preprint-status / re-check-before-submission note. The AJOB → Neuroethics submission history is recorded here (MOD-018 context), not in the citation.

**18e — Build engine switched to pandoc.** `build_paper.py` markdown→docx delegated to **pandoc** (always), replacing the MHC-L exporter. Reason: the MHC-L exporter emitted `^[...]` inline-footnote syntax as literal body text (verified: no `word/footnotes.xml`, literal `^[` present in `word/document.xml` of the v1_12 docx). Pandoc converts inline footnotes to native Word footnotes (verified post-switch: `word/footnotes.xml` present, zero literal `^[` in `word/document.xml`). The interim manual-warning hack was removed. The existing §3.3 Cordasco footnote now renders natively with no manual step. PDF step (docx2pdf) unchanged.

**18f — Author-position defense filed as separate artifact.** `target-venue/jmepb_commentary_proposal.md` — a proposal + full draft commentary for the DA call for commentaries, where the accountability conception is defended (bifurcation of authorial vs editorial commitment to answer the ICMJE/Levy dilemma; recursive AI-aided-justification as distinctive contribution; pre-emptive ownership of the §7 expert-delegated-approval self-application). This is the sole defended venue for the position per the P-OMIT-modified verdict; the paper carries only the 18b registration.

**18g — Frontmatter bump v1.12 → v1.13.** `version`, `date_last_updated` (2026-06-10), `source` (Claude Opus 4.8 added to the model list), `assembly` (v1.13 note), `word_count` (~8,800 est.). Build output: `Paper/journal/CFP_FullPaper_v1_13.docx`.

**18h — Post-full-read corrections (2026-06-10).** A complete read-through of the assembled v1.13 (author request "read the entire paper and compare it to the arguments we have") surfaced regressions and gaps from the incremental editing; all resolved before commit:
- **Duplicate sentence (§1 ¶6):** "The framework is a first iteration, not a settled standard." (added in the v1.12 §1 AI-voice rewrite) sat back-to-back with the pre-existing "The framework is a first iteration subject to revision, not a settled standard." The first was deleted.
- **Dangling cross-reference (Archive testimonial layer):** "consistent with the §4.3 reader-devolution architecture" pointed to a §4.3 that does not exist in the paper (§4 has no numbered subsections; "§4.3" was the briefing CFP_5.3.33's section). Corrected to "the reader-devolution architecture of §5."
- **Orphan citation — Levy:** Levy 2025 was cited in the Archive registration (18b) but absent from the References / `paper_bibliography_FINAL.md`. Levy was read by the author and web-verified (PhilPapers; PMC12015057; CrossRef DOI 10.1136/jme-2024-109912). Added to both bibliographies: `Levy, N. (2025). "Responsibility is not required for authorship." Journal of Medical Ethics, 51(4), 230–232. https://doi.org/10.1136/jme-2024-109912`. **Decision on depth of engagement:** Levy's argument (responsibility not required for authorship) is an argument *against* the accountability conception, i.e. authorship-debate material; per the P-OMIT-modified verdict and the §4.4 placement rule it stays *out* of the position-free body — retained only as the registration's "live opposition" mention. The detailed engagement (bifurcation move answering the ICMJE-statistician / Levy dilemma) lives in the JMEPB commentary (`target-venue/jmepb_commentary_proposal.md`), not the paper.
- **Levy precision:** "responsibility is not required for authorship **at all** (Levy 2025)" → "…for authorship (Levy 2025)"; the "at all" overshot Levy's nuanced position (he allows local responsibility for intellectual contributions as one of three options).
- **Citation back-reference (§3.3 AUTOGEN paragraph):** "Earp et al.'s author-side criterion" → "Porsdam Mann et al.'s author-side criterion" (the cited work's first author is Porsdam Mann, not Earp).
- **"Two levels" terminological collision:** §5.4's "the contestation runs two levels deep" (about authorship criteria) collided with the abstract/§1/§3 "two independent levels" (about ethical inquiry). §5.4 reworded to "does not stop at the choice of criterion."
- **Reference ordering:** Siddiqui (DraftMarks) had been inserted before Schwitzgebel; corrected to Schilke → Schwitzgebel → Science → Siddiqui in both bibliographies.

Non-defect observations recorded but not actioned: (a) Earp-cluster citation density in the body (three loci) is a reception risk, not an error — each does distinct work; (b) Van Woudenberg et al. (2024, "Authorship and ChatGPT: a Conservative View") is cited as §1 background but not engaged — engaging it would re-import the authorship debate into the position-free body, so it is left as background by design.

Validation: approved; committed at v1.13 (commit f0f1ec3).

---

### MOD-019 — v1.13 → v1.14: bias-mitigation Archive apparatus removed; testimonial post-script shortened

| Field | Value |
|-------|-------|
| Date | 2026-06-11 |
| Type | Cut — removes a non-load-bearing Archive apparatus + four citations; eases length budget |
| Trigger | Author judgment, on the "how important are these citations" question: the bias-mitigation citations and the testimonial post-script they served are Archive-only, the AI-voice register is marginal, and the paper has an EthIT length constraint (~8,000-word limit). "Lasciamo che siano le parti filosofiche a lavorare di più." |

**Issue.** The v1.12 Archive "On the testimonial layer of this Archive" paragraph (~150 w) framed the AI-voice register against the empirical bias-against-AI-text literature, citing five sources. Four of those (Liang et al. 2025; arXiv 2510.24011; arXiv 2510.08831; Siddiqui/DraftMarks 2509.23505) were (a) confined to that single Archive paragraph, (b) not load-bearing for the §1–§7 philosophical argument, (c) not independently verified beyond the v1.12 sub-agent search, and (d) carried incomplete author lists ("et al.") or no bibliography entry (the two bare arXiv IDs). Citing unverified preprints in a submission is a gratuitous reputational risk on a decorative paragraph.

**Change.**
- **Testimonial post-script shortened** from ~150 w to ~40 w: *"**On the testimonial layer.** Parts of this Archive are written in the composite voice of the models that produced the paper, reporting what they executed; that register is confined to the Archive, leaving the body's philosophical claims to be assessed on their merits."* All bias-mitigation framing and citations removed. The narrator-reification at the head of the Archive note (the composite-plural disclosure) is untouched, so the testimonial bullets and §7 inflections still have their referent.
- **Bibliography:** removed Liang et al. 2025 and Siddiqui/DraftMarks 2025 from `paper_bibliography_FINAL.md` and the paper's References. The two bare arXiv IDs (2510.24011, 2510.08831) had no entries and disappear with the paragraph. **BaHammam 2025 retained** — it is body-load-bearing (§2.1 transparency-paradox priority cite per CFP_4.2.36 MOD-001; §4).
- **Net:** ~−110 w body. Eases the EthIT ~8,000-word budget. No philosophical content lost — the cut material was an Archive aside about the AI-voice register's empirical status, which the paper does not need.

**Scope note.** The other ~12 scoped AI-voice markers (Abstract, §1 ¶6, §4 close, §5.4, §6, §7) are NOT removed — the author's instruction targeted the bias apparatus and the post-script specifically, not the whole voice register. The voice spec `CFP_5.3.34` is left as the historical record of the v1.12 reasoning; this MOD records that its bias-framing recommendation was retired at v1.14.

**Frontmatter:** v1.13 → v1.14; assembly note + word_count updated. Editions re-derived (arXiv v4, anon submission) and rebuilt (canonical docx, anon PDF, arXiv docx).

Validation: approved; committed at v1.14 (commit 6950e90).

---

### MOD-020 — v1.14 → v1.15: orphan-reference reconciliation

| Field | Value |
|-------|-------|
| Date | 2026-06-11 |
| Type | Reference-consistency fix — re-cite two orphans, remove one |
| Trigger | Pre-submission reference audit (author question "sulle reference siamo sicuri? quali elementi di prova abbiamo?"). An orphan check (first-author surname vs body) found 4 bibliography entries with no in-body citation: Boden & Edmonds 2009, Lloyd 2025, Mecacci & Santoni de Sio 2020, and a false positive (Plato — cited as "*Apology* 38a"). |

**Issue.** Three genuine orphans (bibliography entries cited nowhere in the v1.14 body), all leftovers from the v1.9 §6 compression and the v1.1 additions. Two of them are substantive works that lost their in-body citation, not junk:
- **Mecacci & Santoni de Sio (2020)**, "Meaningful human control as reason-responsiveness," *Ethics and Information Technology* — the canonical source for the §6 *tracking condition* ("system outputs covary with the operator's relevant reasons" = reason-responsiveness), and published in the target journal (EthIT).
- **Lloyd (2025)**, "Epistemic responsibility: toward a community standard for human-AI collaborations," *Frontiers in AI* — directly relevant to §5's community-assessment project.

**Change.**
- **§6 tracking condition:** re-cited Mecacci & Santoni de Sio (2020) — "...system outputs covary with the operator's relevant reasons, developed as *reason-responsiveness* by Mecacci & Santoni de Sio (2020)...". Gives the tracking condition its own source (previously the whole MHC paragraph rested only on Santoni de Sio & van den Hoven 2018) and cites a target-journal paper. Author confirmed the reference verified.
- **§5.1:** re-cited Lloyd (2025) — "A shared approach is required, and articulating a community standard for human–AI collaborations is itself an emerging project (Lloyd 2025)." Reference verified this session via CrossRef (DOI 10.3389/frai.2025.1635691 — title/author/venue/volume/article-number all confirmed).
- **Removed Boden & Edmonds (2009)** "What is Generative Art?" from both bibliographies — a genuine orphan (added v1.1 with Sartre; never cited in the current argument).

**Net:** ~+20 w body. Bibliography now has no orphans except Plato (false positive — cited via the work title *Apology* 38a, standard for classical sources).

**Verification — the two empirical-claim citations, checked against source PDFs (2026-06-11).** The author placed the source PDFs in `transparency/TEMP/` and requested a page-level check. Both claims VERIFIED:
- **Abdulhai et al. (2026), §5.2 "68.9% increase in stance neutralization":** confirmed on **p. 10** of `Abdulhai et al. (2026) 68%.pdf` (= arXiv:2603.18161) — Figure 6 caption ("extensive AI use results in a 68.9% increase in the proportion of essays that remain neutral… t(69) = −2.439, p = 0.017") and §4.3 body ("increases the proportion of users taking a neutral position by 68.9%, p < 0.036"). JPEP's claim is accurate.
- **Schwitzgebel, Schwitzgebel & Strasser (2024), §3.7 "51% … above chance (20%) … hypothesized 80%":** all three figures confirmed in `Schwitzgebel, Schwitzgebel & Strasser (2024).pdf` — 51% (§3.3, p. 14–15: experts "5.08 times out of 10 (51%)… t(24) = 7.13, p < .001"); 20% chance (five-alternative forced choice, p. 12/14); 80% hypothesized (§2.9 hypothesis 2, p. 13; "significantly below the hypothesized accuracy of 80%… contradicting our initial hypothesis," p. 15). Title and authors also confirmed. JPEP's claim is accurate.

**Error caught and fixed — Abdulhai author list.** The verification revealed the bibliography's Abdulhai entry carried a **fabricated co-author list**: "Abdulhai, M., Prabhu, A., Wongkamjan, W., Nasseri, S. A., Nenkova, A., Dreyer, M., Ren, X., & Mathur, N." — only the first author was correct. Corrected against the PDF title page to the actual authors: **Abdulhai, M., White, I., Wan, Y., Qureshi, I., Leibo, J., Kleiman-Weiner, M., & Jaques, N.** (UC Berkeley / UC San Diego / UW / Zaytuna / Google DeepMind). Fixed in both `paper_bibliography_FINAL.md` and the paper's References; the arXiv ID (2603.18161) and the in-text claim were already correct. This is exactly the failure the verification pass existed to catch — a hallucinated author list surviving from an earlier AI-assisted bibliography step.

**Still un-verified (recorded honestly):** the recent/obscure tier (Berg & Robbins 2024, Cheng et al. 2025, Hosseini/Resnik/Holmes 2023, Resnik & Hosseini 2025, Lund & Naheem 2023, Van Woudenberg et al. 2024, Jollimore 2025, Schilke & Reimann 2025) is not yet source-checked. Cordasco 2026a/b were verified in a prior session. Canonical works (Williams, Gallie, Sartre, Kierkegaard, Nietzsche, Plato, Gibbard, Blackburn, Enoch, Shafer-Landau, Santoni de Sio ×2, Strathern, Zimmerman, Moseley) are low fabrication-risk but page-level details unchecked. A further pass is advisable before final submission; the two highest-stakes (empirical) citations are now closed.

**Frontmatter:** v1.14 → v1.15; assembly + word_count updated. Editions re-derived and rebuilt.

Validation: approved; committed at v1.15 (commit 0c26ccb).

---

### MOD-021 — v1.15 → v1.16: full bibliography verification pass

| Field | Value |
|-------|-------|
| Date | 2026-06-11 |
| Type | Reference verification — agent pass over the whole bibliography + two fixes |
| Source | Background agent `ad99ac1bacac22d83` — CrossRef / publisher / arXiv checks of every entry not already verified this session; special attention to author lists (the dimension where the Abdulhai fabrication occurred) |

**Result.** 33 entries CORRECT, 1 correctness MISMATCH, 0 unverifiable. **No new fabrications.** Critically, on the author-list dimension, every co-author on every multi-author entry checked out against CrossRef — no invented or missing co-authors, no DOI-resolves-to-wrong-paper cases. The Abdulhai fabrication (fixed in MOD-020) was isolated.

**Fixes applied.**
- **Berg & Robbins — year 2024 → 2025** (the one substantive error). The Point article "The Cognitive Divide" was published 8 July 2025, not 2024. Authors and URL were correct. Fixed in the §1 in-text citation and in both bibliographies.
- **Hosseini, Resnik & Holmes (2023) — completeness:** added the missing locator *Research Ethics*, **19(4), 449–465** in both bibliographies.

**Noted, not changed.** COPE Council (2024): CrossRef's registered title is "Authorship and AI tools"; the entry's "COPE position — Authorship and AI" is a descriptive rendering of the same DOI'd document — left as-is (not an error). Cheng et al. (2025): CrossRef "issued" reads 2023 (online-first) but the print volume 37(1) is 2025 — the entry's 2025 is correct, kept.

**Reference-reliability status: closed for submission.** The two empirical-claim citations (MOD-020) and the full bibliography (this MOD) are now verified. Canonical works confirmed to exist with correct author/year/venue; page-level minutiae on a few are unchecked but low-risk.

**Frontmatter:** v1.15 → v1.16. Editions re-derived and rebuilt.

Validation: pending author confirmation (edits applied; rebuilds done).

---

## Carry-forward

- The bias-literature additions (Liang 2025; arXiv 2510.24011; arXiv 2510.08831; DraftMarks 2509.23505) are added to support the rewritten Archive testimonial-layer paragraph; they are not referenced from the body.
- The Earp briefing CFP_5.3.33 verification backlog persists: the provenance-problem paper (Earp et al. 2025 NMI) remains paywalled with no OA mirror; the Authorship Without Writing preprint (Hurshman/Porsdam Mann/Savulescu/Earp 2025) is filed locally but held at the editorial-engagement layer per briefing §4.4, not for body text.
- Earp et al. (2026, *JMEPB*, DA) and Earp/Guernon/Porsdam Mann (2026, SHC) are both FORTHCOMING preprints — re-check publication status and final DOIs before the EthIT submission tag.
- The Hurshman/Porsdam Mann/Savulescu/Earp (2025) "Authorship Without Writing" preprint remains held at the editorial-engagement layer per briefing §4.4, not for body text.
- JMEPB commentary (`target-venue/jmepb_commentary_proposal.md`): Part A (proposal) ready to send; Part B (full draft) ready on invitation. Author bio + JPEP self-citation are the two placeholders to fill.
- The session log entry for SID-20260609-095833 documents the broader narrative arc this modlog instantiates.

---

*Modlog prepared 2026-06-09, extended 2026-06-10, in JPEP session SID-20260609-095833. Validation: approved through MOD-017; MOD-018 pending author confirmation before commit.*
