---
artifact_type: modlog
label: CFP_4.2.43_ModificationLog_TitleVerification_v1_28
document: "Full_paper_canonical.md v1.27 → v1.28 — final pre-submission citation-title web check; COPE title correction"
project: JPEP
created: 2026-06-23
last_updated: 2026-06-23
session_id: SID-20260622-191852
inputs:
  - "Paper/MDversion/Full_paper_canonical.md (v1.27 — 39-entry reference list)"
  - "CrossRef REST API (api.crossref.org/works/{DOI}) for the 19 DOI'd references"
  - "Page fetches (substack / thewalrus / acm.org / elsevier.com / researchgate.net) for the web-source references"
  - "CFP_4.2.42_ModificationLog_ArchiveToSupplement_v1_27.md (predecessor)"
output_completed:
  - "Paper/MDversion/Full_paper_canonical.md (v1.28)"
  - "Paper/MDversion/Full_paper_submission_anon.md + Paper/journal/Full_paper_submission_anon.docx (re-derived/rebuilt; identifier-free)"
  - "Paper/MDversion/Full_paper_arxiv_v4.md (re-derived) + Paper/journal/CFP_FullPaper_v1_28.docx"
feeds_into: "EthIT submission (reference list final)"
validation: approved
---

# Modification Log: Full_paper_canonical.md v1.27 → v1.28 — Citation-Title Web Check + COPE Correction

## Provenance & method

A final pre-submission pass checked **every reference title (title only) against the web**:

- **19 DOI'd entries** → CrossRef `works/{DOI}`, comparing the registered title (title + subtitle, normalized) against the bibliography.
- **Web-source entries** (ACM, Elsevier, Science, two Cordasco Substacks, Berg & Robbins, Jollimore, the Earp/Guernon ResearchGate preprint) → page fetches comparing the page/headline title.
- **Book/classic entries** (Sartre, Williams, Enoch, Gibbard, Blackburn, Shafer-Landau, Kierkegaard, Nietzsche, Plato, Reichenbach, Strathern) → standard editions, titles confirmed by inspection (not on CrossRef).

**Result: 38 of 39 titles correct.** One genuine discrepancy, corrected below. (Lund & Naheem 2023 looked off only because CrossRef wraps "ChatGPT"/"artificial intelligence" in `<scp>` small-caps markup — the text is identical. Science 2023 returned HTTP 403 to automated fetches but is the known editorial-policies page; Earp/Porsdam Mann/Sawai/Wangmo 2026 is forthcoming with no DOI yet — both unchanged.)

---

## Modification Entries

### MOD-001 — COPE Council (2024) reference title corrected to the registered title

| Field | Value |
|-------|-------|
| Date | 2026-06-23 |
| Type | Citation correction (title accuracy) |

The bibliography gave a **paraphrased** title, "COPE position — Authorship and AI." CrossRef for the entry's DOI (`10.24318/cCVRZBms`) returns the **registered** title **"Authorship and AI tools."** Corrected in the reference list (author/source unchanged: COPE Council / Committee on Publication Ethics). The in-text citation (§2) uses author–year only and was unaffected.

---

## Build, derivation & verification

- `derive_distributions.py` re-derived the arXiv + anonymized editions from v1.28; **anonymity blocklist passed** (the standing "GitHub archive line not found" warning is unchanged — tracked in `CFP_5.3.1` as an arXiv-only item).
- Rebuilt `Full_paper_submission_anon.docx` and `CFP_FullPaper_v1_28.docx` (pandoc).
- **Verified:** the new title "Authorship and AI tools" is present in the rebuilt docx; "COPE position" is gone; identifier leaks NONE.
- The SP-1–SP-5 documentation-archive zip was rebuilt at the v1.28 label (its transparency/ content is unchanged by this paper-body correction).

---

## Modification Summary

| Type | Count | Examples |
|------|-------|----------|
| Citation correction | 1 | MOD-001 (COPE title) |

A verification-driven one-line fix: the only error surfaced by a full title-by-title web check of the 39-entry reference list. Reference-title reliability is now closed for submission.

---

*Modification Log generated: 2026-06-23 | SID-20260622-191852 | MHC-W Rules 2, 3, 4*
