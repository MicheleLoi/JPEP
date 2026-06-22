---
artifact_type: modlog
label: CFP_4.2.41_ModificationLog_PreSubmissionReadingPass_v1_26
document: "Full_paper_canonical.md v1.25 → v1.26 — pre-submission reading-pass over the v1.25 docx (line cuts, transparency-paradox citation hygiene, source verification, manuscript-wide bold removal)"
project: JPEP
created: 2026-06-22
last_updated: 2026-06-23
session_id: SID-20260622-191852
inputs:
  - "Paper/MDversion/Full_paper_canonical.md (v1.25, HEAD — revision base)"
  - "Paper/journal/Full_paper_submission_anon.docx (v1.25 build — the author's on-screen reading copy; passages flagged against it)"
  - "transparency/TEMP/BaHammam (2025) Transparency Paradox.pdf (Dove Press open-access full text — downloaded + read this session for citation verification)"
  - "transparency/TEMP/Schilke_Reimann (2025) Transparency Dilemma (OSF preprint).pdf (OSF preprint; abstract cross-checked via OpenAlex)"
  - "CrossRef + OpenAlex metadata/abstracts for BaHammam, Schilke & Reimann, Zimmerman 2002, Cheng et al. 2025 (source-fidelity checks)"
  - "CFP_4.2.40_ModificationLog_June19EditHarvest_v1_25.md (predecessor revision episode)"
output_completed:
  - "Paper/MDversion/Full_paper_canonical.md (v1.26)"
  - "Paper/MDversion/Full_paper_submission_anon.md (re-derived) + Paper/journal/Full_paper_submission_anon.docx (rebuilt; anonymity blocklist guard passed; verified identifier-free, Dennett-free, zero inline bold, native footnotes)"
  - "Paper/MDversion/Full_paper_arxiv_v4.md (re-derived) + Paper/journal/CFP_FullPaper_v1_26.docx"
feeds_into: "EthIT submission (Snapp upload of Full_paper_submission_anon.docx + target-venue/cover_letter_ethit.md)"
validation: approved
---

# Modification Log: Full_paper_canonical.md v1.25 → v1.26 — Pre-submission Reading-Pass

## Provenance & method

The author read the v1.25 submission `.docx` on screen ("comodo agli occhi, aiuta") and flagged passages to cut or revise; each was applied to the canonical markdown master in place. The `.docx` was held as a read-only reference and **not** rebuilt until the pass closed. Single-file `git_inplace` versioning; the v1.25 → v1.26 commit diff is the authoritative cumulative record, and the per-edit (a)–(k) ledger lives verbatim in the master's `assembly:` frontmatter.

A standing instruction shaped two entries: **no forced citation re-homing.** When a cut would orphan a reference, the reference was reattached only where it genuinely supports a load-bearing claim, and the relevance was verified against the *source* (not the model's memory) before reattaching. Two source PDFs (BaHammam; Schilke & Reimann) were downloaded to `transparency/TEMP/` and read; Zimmerman (2002) and Cheng et al. (2025) were confirmed at title level via CrossRef/OpenAlex.

---

## Modification Entries

### MOD-001 — §3.3 Williams close: "both deployments" capstone cut (reverses v1.25 Option B)

| Field | Value |
|-------|-------|
| Date | 2026-06-22 |
| Type | Scope Adjustment (reversal) |
| Edit | (a) |

The capstone sentence *"Both deployments work against erasure; they differ only in the direction from which erasure threatens."* was cut. v1.25 (MOD-001 in `CFP_4.2.40`) had **restored** this sentence as the author's "Option B" choice during the June-19 harvest; on a fresh on-screen read the author reversed that call and cut it. The paragraph now closes on *"…to those for whom it is pursued."* followed by the Moseley 2014 parenthetical. Recorded as a deliberate reversal, not an oversight — both states are in the git history.

### MOD-002 — §3.3 Porsdam Mann paragraph: closing two sentences cut

| Field | Value |
|-------|-------|
| Date | 2026-06-22 |
| Type | Scope Adjustment (removal) |
| Edit | (b) |

*"The framework here does not adjudicate it; it makes its application possible. Process transparency is the condition under which such verdicts can be reached at all."* cut. The paragraph now closes on *"…one of the verdicts a community equipped with process documentation can reach about a given work."* The cut sentences restated the framework's enabling role already carried by the preceding clause.

### MOD-003 — Transparency-paradox citation hygiene (§2 + §4)

| Field | Value |
|-------|-------|
| Date | 2026-06-22 |
| Type | Attribution Correction + Source Verification |
| Edits | (h), (d), (e) |

Three coordinated changes to how the transparency-paradox literature is cited, prompted by the author's instruction that *the paper's own a priori reasoning must be credited to the paper, not to sources that do not make the claim.*

- **(h) §2 re-attribution.** The sentence had glossed *"transparency paradox (BaHammam 2025): where transparency matters most, we get least…"* with a colon, implying BaHammam asserts the "matters most/least" point. Restructured to attribute to BaHammam only what his editorial documents (wide adoption, rare disclosure, *"measurable professional costs"* of disclosure — his phrase) and to mark the "matters most → get least" sharpening explicitly as the authors' own a priori observation. **BaHammam full text verified** against the Dove Press PDF: the "transparency paradox" coinage, the Li-et-al disclosure-penalty data, and the asymmetry claim are confirmed; the "matters most/least" formulation is genuinely the paper's, not his.
- **(d) §4 de-duplicated re-citation.** *"(BaHammam 2025; cf. Schilke & Reimann 2025)"* in the §4 self-defeat paragraph replaced with the back-reference *"the reputational cost of the transparency paradox, as previously argued."* This had been the only in-text cite of Schilke & Reimann, so it was **reattached at §2** to the load-bearing clause *"incentive structures that penalize transparency,"* which its finding directly evidences. Verified against the source: Schilke & Reimann's abstract reports *thirteen experiments* showing AI disclosure lowers trust, robust to *voluntary or mandatory* disclosure — a precise fit for the §2 penalty claim, not a forced re-home.
- **(e) §4 sentence cut.** The paragraph's final sentence *"The format requirement, applied this way, reproduces and intensifies the asymmetry it was meant to neutralize."* cut as a redundant restatement.

### MOD-004 — §4 Hosseini-trichotomy clause: reworded

| Field | Value |
|-------|-------|
| Date | 2026-06-22 |
| Type | Clarification |
| Edit | (c) |

*"…without distorting either the discipline or the disclosure norm."* → *"…or what the goal of disclosure ought to be."* The original "disclosure norm" was ambiguous; the revised clause names the actual stake — the purpose disclosure is meant to serve.

### MOD-005 — §5.4 revisions: good-faith reframed, duplicate cut, self-test passage demoted

| Field | Value |
|-------|-------|
| Date | 2026-06-22 |
| Type | Conceptual Clarification + Scope Adjustment |
| Edits | (f), (g), (j) |

- **(f)** The defense-in-depth close *"Good faith at the community level … is the disposition under which the defense remains operative"* replaced with a speculation that the divergence among conceptions of authentic human authorship will widen rather than collapse. The author judged the "good faith" move incoherent here — it imported the §3.3 individual-level Sartrean concept to characterise a structural/community condition; the replacement makes a defensible empirical conjecture instead.
- **(g)** The paragraph *"A natural objection is that documentation requirements impose disproportionate costs…"* cut as a duplicate of the offloading / re-impose-structure reply already made in §3.3 (Cordasco response). Its two citations were **not** orphaned: Zimmerman (2002), the canonical self-regulated-learning overview, and Cheng et al. (2025), an SRL meta-analysis — both confirmed as SRL works via CrossRef/OpenAlex — were reattached to the §3.3 offloading sentence (*"re-impose the missing structure"*), the claim they actually support.
- **(j)** The passage *"That essay performs the response in miniature…"* (three sentences on the Earp/Guernon/Porsdam Mann self-test essay) demoted from body to a footnote; the body sentence now ends at the (Earp, Guernon & Porsdam Mann 2026) cite.

### MOD-006 — §4 footnote added: BaHammam's tiered framework as near-neighbour

| Field | Value |
|-------|-------|
| Date | 2026-06-22 |
| Type | Addition (footnote) |
| Edit | (i) |

A footnote was added at the §4 sentence on the *Journal of Medical Ethics* tiered Generative-AI-Use Declaration, noting that BaHammam (2025) independently proposes a four-level tiered disclosure framework whose top tier requires *"rigorous documentation of prompts, model versions, verification methods…"* — a near-neighbour of this paper's process-documentation argument arriving from the empirical-science side, while preserving the §4 caveat that it is a format built for disciplines with detachable methods. Surfaced during the BaHammam full-text read; the author asked for it as a note.

### MOD-007 — Manuscript-wide bold removal

| Field | Value |
|-------|-------|
| Date | 2026-06-23 |
| Type | Formatting |
| Edit | (k) |

All 49 markdown bold spans (`**…**`) stripped manuscript-wide: body lead-in labels (§3 "expressivist/personal conception", §6 "tracking/tracing condition", the Archive "Archive." lead-in) and the bold author surnames throughout the reference list. Italics (single `*`) and the YAML frontmatter were left untouched (verified: 0 `**` remain in source; 0 inline bold runs in the rebuilt docx). This also discharges the deferred EthIT APA-7 *"no bold authors"* restyle item for the bibliography.

---

## Build, derivation & verification

- `derive_distributions.py` re-derived the arXiv and anonymized editions from v1.26; the **anonymity blocklist guard passed** (no name / affiliation / email / repo / ORCID token in the anon body).
- `Full_paper_submission_anon.docx` and `CFP_FullPaper_v1_26.docx` rebuilt via pandoc 3.8.3 (inline `^[…]` footnotes → native Word footnotes).
- **Anon docx verified:** identifier leaks NONE; Dennett / Schwitzgebel absent (the v1.20 §3.7 cut holds); the four reading-pass cuts (a / b / e / f) absent from the rendered text; Schilke present at §2; **0 inline bold runs**; `word/footnotes.xml` present, carrying both new footnotes (BaHammam-tiered; demoted self-test passage).

### Known flag (pre-existing, not introduced here)

`derive_distributions.py` warns that the canonical body no longer carries the public GitHub archive line verbatim — the Archive section reads *"[persistent identifier: forthcoming]"*. This is present in committed v1.25 (HEAD), so it predates this pass and does not affect the anonymized submission (whose Archive line is correctly withheld). It does mean the **public arXiv edition's body** lacks the repo URL (it survives only in the arXiv frontmatter). Flagged for resolution before the next arXiv upload; out of scope for the EthIT submission.

---

## Modification Summary

### By Type

| Type | Count | Examples |
|------|-------|----------|
| Scope Adjustment (cut/removal) | 3 | MOD-001, MOD-002, parts of MOD-003/005 |
| Attribution Correction + Source Verification | 1 | MOD-003 |
| Clarification | 2 | MOD-004, MOD-005 (f) |
| Addition | 1 | MOD-006 |
| Formatting | 1 | MOD-007 |

### Key themes

A pre-submission read on the v1.25 docx, converted into in-place edits on the canonical master. Two threads dominate: **trimming restatement** (MOD-001/002/003e/005) and **citation integrity** (MOD-003/005g/006) — the latter conducted under an explicit *no-forced-re-homing* rule, with every reattached or re-attributed source checked against its actual text. The author corrected one genuine attribution error (the §2 "matters most/least" gloss leaning on BaHammam, who does not make it) and reclaimed it as the paper's own contribution. Manuscript-wide bold removal (MOD-007) doubles as a step in the deferred APA-7 restyle.

---

*Modification Log generated: 2026-06-23 | SID-20260622-191852 | MHC-W Rules 2, 3, 4*
