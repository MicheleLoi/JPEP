---
artifact_type: modlog
label: CFP_4.2.42_ModificationLog_ArchiveToSupplement_v1_27
document: "Full_paper_canonical.md v1.26 → v1.27 — 'AI Usage and Documentation Archive' closing note cut from the body and moved to an anonymized Supplementary Material file (EthIT length)"
project: JPEP
created: 2026-06-23
last_updated: 2026-06-23
session_id: SID-20260622-191852
inputs:
  - "Paper/MDversion/Full_paper_canonical.md (v1.26 — revision base)"
  - "EthIT '~8,000 words' soft limit (Word reported the body over ~8,300)"
  - "Snapp 'Supplementary material (optional)' upload field (double-anonymous: identifying information must be removed)"
  - "CFP_4.2.41_ModificationLog_PreSubmissionReadingPass_v1_26.md (predecessor)"
output_completed:
  - "Paper/MDversion/Full_paper_canonical.md (v1.27)"
  - "target-venue/Supplementary_AIUsageArchive_anon.md + .docx (the extracted closing note, anonymity blocklist passed)"
  - "Paper/MDversion/Full_paper_submission_anon.md + Paper/journal/Full_paper_submission_anon.docx (re-derived/rebuilt; Archive section absent, identifier-free, footnotes intact)"
  - "Paper/MDversion/Full_paper_arxiv_v4.md (re-derived) + Paper/journal/CFP_FullPaper_v1_27.docx"
feeds_into: "EthIT submission — the supplement goes in Snapp's 'Supplementary material (optional)' published slot (anonymized), separate from the non-anon SP-1–SP-5 archive zip that goes to the editorial office"
validation: approved
---

# Modification Log: Full_paper_canonical.md v1.26 → v1.27 — Archive Note → Supplementary Material

## Provenance & method

The author judged the body over EthIT's ~8,000-word soft limit (Word reported >8,300) and chose to **cut the unnumbered closing note "AI Usage and Documentation Archive" (571 words) from the manuscript and re-submit it as anonymized Supplementary Material** via Snapp's optional published-supplement slot. Single-file `git_inplace` versioning; the v1.26 → v1.27 commit diff is the authoritative change record.

The cut was done at the canonical-MD level first, then propagated downstream (re-derive → rebuild → verify), per the author's instruction ("fai la divisione a livello di canonical MD, e poi downstream").

---

## Modification Entries

### MOD-001 — Closing note "AI Usage and Documentation Archive" cut and moved to Supplementary Material

| Field | Value |
|-------|-------|
| Date | 2026-06-23 |
| Type | Relocation (body → supplement) + length reduction |

The entire closing section (heading + the AI-usage intro, the SP-1…SP-5 "It comprises" list, *Source conversations*, *Inline excerpts*, *Scope and limits*, *The author's operative conception of authorship*, *On the testimonial layer*) was removed from the body. Body word count **~8,665 → ~8,083** (excl. references), bringing it to the ~8,000 soft limit. One `---` separator was kept between §7 (Conclusion) and the References.

The removed section was written verbatim to **`target-venue/Supplementary_AIUsageArchive_anon.md`** (+ `.docx`), prefaced by a one-line note stating it accompanies the manuscript and is anonymized. The content was already identifier-free; it was passed through the same `ANON_BLOCKLIST` used by `derive_distributions.py` (name / affiliation / email / repo / ORCID) and confirmed clean before shipping.

**Why a supplement, not a deletion:** the paper's self-exemplification thesis still needs the archive to exist and to be pointed to; moving the detailed closing note out of the body keeps the in-body argument (§5 framework, §6 apparatus, §5.4 feasibility-exhibit) intact while shedding 571 words.

### MOD-002 — Three dangling cross-references reconciled

| Field | Value |
|-------|-------|
| Date | 2026-06-23 |
| Type | Cross-reference repair |

Three in-body references explicitly pointed to "the end" / "the closing note that follows" and would have dangled once the section was cut. Redirected to the supplementary material:

- **§1 (intro):** "…the documentation record instantiates them and is archived at the persistent identifier *given at the end*." → "…and is **provided as supplementary material**."
- **§1 (roadmap):** "…Section 7 concludes, *followed by a closing note on the documentation archive*." → "…Section 7 concludes. **The documentation archive is provided as supplementary material**."
- **§7 (conclusion):** "…is described, with a persistent identifier, *in the closing note that follows this conclusion*." → "…is **described in the supplementary material accompanying this paper**."

Left intact (still true, no dangle): the abstract's "archived at a persistent identifier", the §5.4 "documentation archive serves here as evidence of feasibility", and the §7 "testimonial layer" sentence (a self-contained claim about the archive).

---

## Build, derivation & verification

- `derive_distributions.py` re-derived the arXiv and anonymized editions from v1.27; **anonymity blocklist passed**. (The pre-existing "GitHub archive line not found" warning is unchanged from v1.25/v1.26 — the Archive line is the `[persistent identifier: forthcoming]` placeholder; tracked in `CFP_5.3.1` as an arXiv-only item, not affecting the anon submission.)
- Rebuilt `Full_paper_submission_anon.docx` and `CFP_FullPaper_v1_27.docx` (pandoc 3.8.3, native footnotes).
- **Manuscript docx verified:** no "AI Usage and Documentation Archive" section; "provided as supplementary material" present; identifier leaks NONE; `footnotes.xml` present.
- **Supplement docx verified:** identifier leaks NONE; carries the full SP-1…SP-5 list.

---

## Modification Summary

| Type | Count | Examples |
|------|-------|----------|
| Relocation (body → supplement) | 1 | MOD-001 |
| Cross-reference repair | 1 | MOD-002 |

A length-driven relocation, not a deletion: the documentation archive's closing note becomes an anonymized published supplement, and the body's three pointers to it are redirected. Distinct from the **non-anon** SP-1–SP-5 archive zip (`CFP_5.3.1` work plan) that goes to the editorial office — the two are different Snapp channels.

---

*Modification Log generated: 2026-06-23 | SID-20260622-191852 | MHC-W Rules 2, 3, 4*
