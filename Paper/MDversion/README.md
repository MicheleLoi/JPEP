# Paper/MDversion — version map and build provenance

This folder holds the markdown forms of the JPEP paper across versions. The naming and provenance differ by version and are not self-evident from the filenames; this README is the authoritative map.

## arXiv version map

| arXiv version | arXiv ID | Markdown form in this folder | Build path to the published artifact |
|---|---|---|---|
| **v1** | [2511.08639v1](https://arxiv.org/abs/2511.08639v1) | Multi-file: `01_introduction.md` … `08_conclusion.md` + `appendix.md` + `references.md`. Also `Full paper2511.08639v1.md` (integrated single file, assembled retroactively May 2026 for reference). | Authored as section markdown files (Oct–Nov 2025). Submitted as PDF generated from the integrated form. |
| **v2** | [2511.08639v2](https://arxiv.org/abs/2511.08639v2) | **No markdown source in this folder.** v2 was authored directly in Microsoft Word — `Paper/arXiv/Full_paper_v2.docx`. The published `Full_paper_v2.pdf` was exported from that DOCX. The section .md files in this folder remain at their v1 content (they were the stable v1 baseline preserved while the v2 edits were made in Word). | Word DOCX → PDF export, January 2026. No `.md` intermediary. |
| **v3** | (to be uploaded) | `Full_paper_arxiv_v3.md` — single integrated markdown. | Derived from the CFP-form integrated markdown `CFP_FullPaper_v1.md` (v1.10, 2026-05-13) with the author block restored and the archive reference wired to GitHub. See file frontmatter `based_on:` field. |

## Why v2 has no markdown counterpart here

The MDversion folder was created in early Nov 2025 to hold v1 as a stable reference baseline before the v2 edits began. The A.4 appendix rewrite that produced the v2 content was performed in Word (source chats in `appendix.md` frontmatter, sessions of 2026-01-04/05). The v2 PDF on arXiv was generated from that Word file directly. There is no concatenation script and no canonical markdown for v2.

The frontmatter field `release_baseline: arXiv-2511.08639v1` in `appendix.md` records this baseline-status explicitly; `contains_post_release_addendum: true` acknowledges that v2's addendum exists but is not contained in this file.

Documented in detail in [`transparency/Canonical_MD/SP4_ProcessDocumentation/4.7_EpistemicTraces/CFP_4.7.10_EpistemicTrace_VersionIdentificationForLLMs.md`](../../transparency/Canonical_MD/SP4_ProcessDocumentation/4.7_EpistemicTraces/CFP_4.7.10_EpistemicTrace_VersionIdentificationForLLMs.md).

## Build script — what `build_paper.py` does and doesn't do

[`../../build_paper.py`](../../build_paper.py) builds the **CFP/journal version**, not the arXiv versions. It reads `CFP_FullPaper_v1.md` (the integrated CFP markdown), strips the YAML frontmatter, and exports a versioned `.docx` to `Paper/journal/`, then converts to `.pdf` via docx2pdf. It does not concatenate the section files in this folder and was not used to produce v1 or v2 of the arXiv paper.

## Companion artifacts (not in this folder)

- `Paper/arXiv/Full_paper_v2.pdf` — canonical arXiv v2 (kept on disk, currently gitignored).
- `Paper/arXiv/Full paper-Arxiv-V1redaction.docx` — older blinded v1 draft (kept on disk, currently gitignored).
- `Paper/journal/CFP_FullPaper_v1_10.docx/.pdf` — CFP submission artifacts built by `build_paper.py`.
