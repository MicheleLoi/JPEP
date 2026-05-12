---
project: JPEP
document_type: Type 11 - Note
label: CFP_5.3.23_Note_AssembledPaperBuild
document_subtype: build_record
date_created: 2026-04-09
session_id: SID-20260409-155040
status: Complete
inputs:
  - "CFP_5.4.3_Introduction_v2.md (v2.1 at build time)"
  - "CFP_5.4.5_Section2_v4.md (v4.1 at build time)"
  - "CFP_5.4.4_Section3_v3.md (v3 at build time)"
  - "CFP_5.4.7_Section5_v2.md (v2.1 at build time)"
  - "CFP_5.4.8_Section6_v4.md (v4.1 at build time)"
  - "CFP_5.4.9_Section7_v3.md (v3.1 at build time)"
  - "CFP_5.4.10_Conclusion_v1.md (v1.1 at build time)"
  - "paper_bibliography.md (pre-FINAL bibliography at build time)"
  - "build_paper.py (assembly script)"
feeds_into:
  - "CFP_5.3.24_Note_ReviewerB_OpusReview_v1.md"
  - "CFP_5.3.25_Note_ShouldersReview_v1.md"
---

# Assembled Paper Build — CFP Version

## Purpose

Records the assembly of the CFP paper into reviewer-ready files for submission to an AI reviewer. These files are the primary inputs to the next session.

## Files produced

| File | Format | Path |
|------|--------|------|
| `CFP_paper_combined.md` | Markdown (combined source) | `build/CFP_paper_combined.md` |
| `CFP_paper.docx` | Word document | `build/CFP_paper.docx` |
| `CFP_paper.pdf` | PDF (pending MiKTeX setup) | `build/CFP_paper.pdf` |

## Assembly script

`build_paper.py` (project root) — strips frontmatter from each section draft and concatenates in order, then calls pandoc. Rerunnable at any time.

## Sections included (in order)

| File | Section | Version |
|------|---------|---------|
| `CFP_5.4.3_Introduction_v2.md` | 1. Introduction | v2.1 |
| `CFP_5.4.5_Section2_v4.md` | 2. Systemic Barriers to Disclosure | v4.1 |
| `CFP_5.4.4_Section3_v3.md` | 3. Why Engage Transparently with AI-Assisted Ethics Research? | v3 |
| *(Section 4 cut)* | — | — |
| `CFP_5.4.7_Section5_v2.md` | 5. Conditions for Adequate Transparency | v2.1 |
| `CFP_5.4.8_Section6_v4.md` | 6. Mandatory Transparency in Practice | v4.1 |
| `CFP_5.4.9_Section7_v3.md` | 7. Community Assessment of Documentation Adequacy | v3.1 |
| `CFP_5.4.10_Conclusion_v1.md` | 8. Conclusion | v1.1 |
| `paper_bibliography.md` | References | — |

## Known gaps at time of build

- Title: placeholder used (revision pending — Phase 4)
- Abstract: not yet drafted (Phase 4)
- Section numbering: gap at 4 (cut section) — not yet renumbered for submission
- PDF: pending MiKTeX package update (kvsetkeys and dependencies)

---

*CFP_5.3.23 — SID-20260409-155040*
