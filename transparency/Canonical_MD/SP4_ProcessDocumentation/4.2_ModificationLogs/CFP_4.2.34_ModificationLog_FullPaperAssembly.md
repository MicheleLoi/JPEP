---
artifact_type: modlog
document: CFP_FullPaper v1.1 cleanup (Phase 5 Commit 2)
output_file: CFP_4.2.34_ModificationLog_FullPaperAssembly.md
project: JPEP
created: 2026-05-12
last_updated: 2026-05-12
session_id: SID-20260512-223052
inputs:
  - Paper/MDversion/CFP_FullPaper_v1.md (v1, commit ca921f3)
  - transparency/Canonical_MD/SP4_ProcessDocumentation/4.6_ReferenceLogs/paper_bibliography_FINAL.md
  - Crossref API (Boden & Edmonds 2009 DOI verification)
  - Frontiers article via WebFetch (Santoni de Sio & van den Hoven 2018 section structure verification)
  - CFP_5.3.1_WorkPlan_CFP_Adaptation.md (Phase 5 Commit 2 plan)
output_completed: Paper/MDversion/CFP_FullPaper_v1.md (v1.1)
feeds_into: Phase 5 final consistency review
validation: approved
---

# Modification Log: CFP_FullPaper v1.1 Cleanup

The v1 assembly (commit `ca921f3`) preserved three known cross-reference / citation defects flagged in its frontmatter `known_issues`. This log records the v1.1 cleanup pass that resolved them. Single-file `git_inplace` versioning: v1 → v1.1 lives in the same file; `git diff ca921f3..HEAD -- Paper/MDversion/CFP_FullPaper_v1.md` is the authoritative change record.

---

## Modification Entries

### MOD-001 — Cross-reference reconciliation (§4 / §5 / §6 body)

| Field | Value |
|-------|-------|
| Date | 2026-05-12 |
| Type | Mechanical correction (post-renumbering residue) |

**Issue:** Section drafts carry `section_numbering: pre_renaming`. The post-2026-04-09 renaming (old §5/§6/§7/§8 → new §4/§5/§6/§7) was applied to section headings during assembly but four cross-references in body text were missed.

**Changes (in `Paper/MDversion/CFP_FullPaper_v1.md` only — source drafts untouched per project rule):**

| Location | Before | After |
|---|---|---|
| §4 closing (4.4) | "Section 6 develops the framework designed to satisfy all three." | "Section 5 develops the framework designed to satisfy all three." |
| §5 (5.1, near end) | "The three conditions from Section 5—ecological validity, good faith orientation, costly signaling—" | "The three conditions from Section 4—ecological validity, good faith orientation, costly signaling—" |
| §6 (6.1) | "Section 6 established what transparency documentation must do:" | "Section 5 established what transparency documentation must do:" |
| §6 (6.4) | "The good faith orientation from Section 5 shapes documentation assessment." | "The good faith orientation from Section 4 shapes documentation assessment." |

**Rationale:** New numbering: §4 = Conditions for Adequate Transparency, §5 = Mandatory Transparency in Practice (where the framework is specified), §6 = Community Assessment of Documentation Adequacy. Each pre-renaming reference was checked against the post-renaming destination by inspection.

**Scope discipline:** The source section drafts retain `section_numbering: pre_renaming` and are *not* edited. Cross-ref corrections live only in the assembled paper, per project rule 1 (authoritative drafts in `5.4_SectionDrafts/`, assembled paper in `Paper/MDversion/`).

---

### MOD-002 — Boden & Edmonds (2009): page number corrected

| Field | Value |
|-------|-------|
| Date | 2026-05-12 |
| Type | Citation correction |

**Issue:** §3.2 cited Boden & Edmonds (2009) with `p. 138`, but the article runs pp. 21–46 in *Digital Creativity* 20(1–2). The page reference was out of range.

**Change:** §3.2 (Personal/Existential conception subsection, paragraph on creative practice):

- Before: `(Boden & Edmonds, 2009, p. 138)`
- After: `(Boden & Edmonds, 2009, p. 29)`

Quote unchanged: "partly responsible for coming up with the idea itself".

**Provenance:** Page 29 verified against the article PDF (second column, opening of the CG-art definition discussion).

---

### MOD-003 — Santoni de Sio & van den Hoven (2018): [VERIFY] tag removed

| Field | Value |
|-------|-------|
| Date | 2026-05-12 |
| Type | Citation format correction |

**Issue:** §5.1 cited the MHC tracing-condition passage with `(§6.2) [VERIFY: replace with page number]`. The cited article is open-access on Frontiers (DOI `10.3389/frobt.2018.00015`) and online-only — Frontiers articles do not carry traditional page numbers. The article uses numbered sections; the quote appears in **Section 6, "Tracing" subsection** (verified via Frontiers HTML structure). `§6.2` is therefore the correct locator and `[VERIFY: replace with page number]` was a category error: there is no page number to replace it with.

**Change:** §5.1, MHC introduction passage:

- Before: `are not under meaningful human control" (§6.2) [VERIFY: replace with page number].`
- After: `are not under meaningful human control" (§6.2).`

**Rationale:** Frontiers articles are cited by section/subsection for specific quote locations, not by page number. The locator is now clean and final.

---

### MOD-004 — Bibliography additions: Sartre (1956), Boden & Edmonds (2009)

| Field | Value |
|-------|-------|
| Date | 2026-05-12 |
| Type | Bibliography completeness |

**Issue:** Two in-text citations had no corresponding entry in `paper_bibliography_FINAL.md`: Sartre (1956, §3.3 Sartrean bad-faith passage) and Boden & Edmonds (2009, §3.2 modular-synth / generative-art passage).

**Additions (alphabetically inserted):**

- **Boden, M. A., & Edmonds, E. A.** (2009). "What is Generative Art?" *Digital Creativity*, 20(1–2), 21–46. [https://doi.org/10.1080/14626260902867915](https://doi.org/10.1080/14626260902867915)
- **Sartre, J.-P.** (1956). *Being and Nothingness: An Essay on Phenomenological Ontology* (H. E. Barnes, Trans.). New York: Philosophical Library. (Original work published 1943)

**Provenance:** Boden & Edmonds DOI verified via Crossref API. Sartre publisher / translator / pagination cross-checked via Cambridge Core review of the 1956 Philosophical Library first English edition. No ISBN (pre-ISBN era).

**Bibliography frontmatter:** `session_id` extended with SID-20260512-223052.

---

### MOD-005 — Frontmatter: v1 → v1.1, git_inplace convention recorded

| Field | Value |
|-------|-------|
| Date | 2026-05-12 |
| Type | Versioning metadata |

**Changes to `CFP_FullPaper_v1.md` frontmatter:**

- `version`: `v1` → `v1.1`
- `source`: extended with "v1.1 cleanup pass in SID-20260512-223052"
- `assembly`: rewritten to describe both v1 (initial concatenation) and v1.1 (this cleanup pass)
- `versioning_convention: git_inplace` added (per Adaptation Log 2026-04-07 — no `_v1.1` filename suffix; commits are the version history)
- `session_id`: extended to list form `[SID-20260512-171552, SID-20260512-223052]`
- `inputs`: bibliography entry annotated "(v1.1: Sartre 1956 + Boden & Edmonds 2009 added)"
- `known_issues`: three items resolved (cross-refs, bib entries, VERIFY tag); only the Cavell-without-formal-citation note retained as an intentional design decision

**Rationale:** No new file (`_v1.1.md`) created — single-file convention preserves the chain of commits as the version history. `git log -- Paper/MDversion/CFP_FullPaper_v1.md` will show v1 (commit `ca921f3`) → v1.1 (the commit this modlog accompanies).
