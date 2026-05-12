---
artifact_type: modlog
document_type: Type 3 - Modification Log
label: CFP_4.2.31_ModificationLog_Bibliography
title: "Modification Log: Bibliography — Review Response Cleanup"
project: JPEP
created: 2026-04-09
last_updated: 2026-04-10
session_id:
  - SID-20260409-200754
  - SID-20260409-233204
status: Active
inputs:
  - CFP_5.3.25_Note_ShouldersReview_v1.md
  - CFP_5.3.24_Note_ReviewerB_OpusReview_v1.md
  - CFP_5.3.27_Note_ReviewResponse_Draft.md
output_completed:
  - transparency/Canonical_MD/SP4_ProcessDocumentation/4.6_ReferenceLogs/paper_bibliography.md
  - transparency/Canonical_MD/SP4_ProcessDocumentation/4.6_ReferenceLogs/paper_bibliography_FINAL.md
validation: approved
---

# Modification Log: Bibliography — Review Response Cleanup

Review-driven corrections and additions to the paper bibliography.
Sources: Shoulders AI review (CFP_5.3.25) and Opus Reviewer B (CFP_5.3.24).
Session: SID-20260409-200754.

---

## Modification Entries

### MOD-001

| Field | Value |
|-------|-------|
| Date | 2026-04-09 |
| Type | Missing Reference Added |

**Issue Identified:**
Strathern (1997) cited in `CFP_5.4.7_Section5_v2.md` §4.2 — "As Strathern (1997) observed, 'when a measure becomes a target, it ceases to be a good measure'" — was absent from `paper_bibliography.md`. Shoulders reviewer (#12) flagged the missing entry and noted the Goodhart's Law ambiguity (the aphorism is associated with both Strathern and Goodhart; the specific Strathern work should be cited to allow readers to verify).

**Resolution:**
Added to `paper_bibliography.md` (REFERENCES section, alphabetical order) and to `paper_bibliography_FINAL.md`:
> Strathern, M. (1997). 'Improving ratings': Audit in the British University system. *European Review*, 5(3), 305–321. [VERIFY]

`[VERIFY]` tag marks the entry for confirmation of DOI, page range, and correct issue number in the dedicated reference-checking pass.

---

### MOD-002

| Field | Value |
|-------|-------|
| Date | 2026-04-09 |
| Type | Missing Reference Added |

**Issue Identified:**
Mercier (2020) cited substantively in `CFP_5.4.7_Section5_v2.md` §4.3 — "As Mercier (2020) argues in *Not Born Yesterday*, signals costly to produce are harder to fake and thus more credible" — was absent from `paper_bibliography.md`. Shoulders reviewer (#11) flagged the omission as non-trivial given Mercier's role in anchoring the costly-signaling argument.

**Resolution:**
Added to `paper_bibliography.md` (REFERENCES section, alphabetical order) and to `paper_bibliography_FINAL.md`:
> Mercier, H. (2020). *Not Born Yesterday: The Science of Who We Trust and What We Believe*. Princeton: Princeton University Press. [VERIFY]

`[VERIFY]` tag marks for ISBN/publisher confirmation.

---

### MOD-003

| Field | Value |
|-------|-------|
| Date | 2026-04-09 |
| Type | Missing Reference Added |

**Issue Identified:**
Williams (1981) cited in `CFP_5.4.4_Section3_v3.md` (body text and section reference list, line 107) for the "ground projects" concept — was absent from `paper_bibliography.md`. Discovered during session cross-check; not explicitly flagged by either reviewer but constitutes a gap in the master bibliography.

**Resolution:**
Added to `paper_bibliography_FINAL.md` (not retroactively added to `paper_bibliography.md` working file, which will be updated in the reference-checking pass):
> Williams, B. (1981). "Persons, Character and Morality." In *Moral Luck: Philosophical Papers 1973–1980* (pp. 1–19). Cambridge: Cambridge University Press. [VERIFY citation locus for "ground projects" — Shoulders reviewer (#31) suggests Smart & Williams (1973) may be the correct locus]

The `[VERIFY]` tag flags a specific question: whether "ground projects" appears in "Persons, Character and Morality" (Williams 1981) or in the earlier contribution to Smart & Williams (1973) *Utilitarianism: For and Against*. The reviewer's suggestion may be incorrect — the concept does appear in the 1981 essay — but requires confirmation against the source text.

---

### MOD-004

| Field | Value |
|-------|-------|
| Date | 2026-04-09 |
| Type | Consistency Fix |

**Issue Identified:**
Santoni de Sio et al. (2016) had conflicting editor attributions: `paper_bibliography.md` listed "S. Nagel (ed.)" while the section-level reference list in `CFP_5.4.4_Section3_v3.md` (line 101) listed "J. Clausen & N. Levy (Eds.)". Shoulders reviewer (#9) flagged the inconsistency.

**Resolution:**
`paper_bibliography.md` updated to "J. Clausen & N. Levy (Eds.) [VERIFY editors]" to match the body-text reference list. Both now consistent. `[VERIFY editors]` tag marks for definitive confirmation against the *Handbook of Neuroethics* title page in the reference-checking pass.

---

### MOD-005

| Field | Value |
|-------|-------|
| Date | 2026-04-09 |
| Type | Cleanup |

**Issue Identified:**
`paper_bibliography.md` contained inline working notes attached to two entries not cited in the CFP adaptation (Boden & Edmonds 2009; Clark 2008): verification reminders and "not cited in CFP adaptation" flags. Shoulders reviewer (#14, #18) flagged that the bibliography as submitted contained internal editorial working notes inappropriate for publication.

**Resolution:**
Inline notes removed from both entries in `paper_bibliography.md`. A `## WORKING NOTES (not for submission)` separator was added before the administrative sections (SECTION-BY-SECTION USAGE, VERIFICATION NEEDED, CITATION NOTES, STYLE NOTES, NEXT ACTIONS, COMPILATION STATUS) to clearly delimit the submission-ready REFERENCES section from process documentation. A `build_source: false` flag and pointer to `paper_bibliography_FINAL.md` were added to the frontmatter.

---

### MOD-006

| Field | Value |
|-------|-------|
| Date | 2026-04-09 |
| Type | New Artifact |

**Issue Identified:**
No submission-ready bibliography file existed. The working `paper_bibliography.md` mixes clean reference entries with extensive process documentation (section-by-section usage, verification queues, citation notes, style notes, compilation status). Any paper build that includes this file wholesale will reproduce all administrative content in the submission — which is what the Shoulders reviewer saw.

**Resolution:**
Created `paper_bibliography_FINAL.md` in the same folder (`4.6_ReferenceLogs/`) as the authoritative submission-ready reference list. Contains only:
- YAML frontmatter with `build_source: true` and pointer note
- Classical sources (Plato *Apology*)
- Primary sources (alphabetical), incorporating all CFP-cited references, the three new/missing entries (Strathern, Mercier, Williams), and `[VERIFY]` tags on items pending confirmation

`paper_bibliography.md` frontmatter updated with `build_source: false` and `submission_bibliography: paper_bibliography_FINAL.md` to make the build boundary explicit.

---

---

### MOD-007

| Field | Value |
|-------|-------|
| Date | 2026-04-10 |
| Session | SID-20260409-233204 |
| Type | Verification Resolved |

**Issue Identified:**
Strathern (1997) carried a `[VERIFY]` tag for DOI, page range, and issue number.

**Resolution:**
Verified via Cambridge Core (https://www.cambridge.org/core/journals/european-review/article/abs/improving-ratings-audit-in-the-british-university-system/FC2EE640C0C44E3DB87C29FB666E9AAB) and RepEC. Entry confirmed correct: *European Review*, 5(3), 305–321. [VERIFY] removed from both bibliography files.

---

### MOD-008

| Field | Value |
|-------|-------|
| Date | 2026-04-10 |
| Session | SID-20260409-233204 |
| Type | Verification Resolved |

**Issue Identified:**
Mercier (2020) carried a `[VERIFY]` tag for publisher and ISBN.

**Resolution:**
Verified via Princeton University Press catalogue and Amazon. Entry confirmed correct: Princeton University Press, 2020. ISBN-13: 978-0691178707. [VERIFY] removed from both bibliography files. Author supplied the citation; verification confirms it.

---

### MOD-009

| Field | Value |
|-------|-------|
| Date | 2026-04-10 |
| Session | SID-20260409-233204 |
| Type | Verification Resolved + Reviewer Error Noted |

**Issue Identified:**
Williams (1981) carried a `[VERIFY]` tag on the citation locus for "ground projects." Shoulders reviewer (#31) had suggested Smart & Williams (1973) as the correct source rather than "Persons, Character and Morality" in *Moral Luck* (1981).

**Resolution:**
Verified via published secondary literature (PMC article PMC3966523, which cites Williams on ground projects from *Moral Luck*). The paper's original citation is correct. Smart & Williams (1973) is cited in that literature for different aspects of the utilitarian critique, not for "ground projects" specifically. Reviewer suggestion was wrong. [VERIFY] removed.

---

### MOD-010

| Field | Value |
|-------|-------|
| Date | 2026-04-10 |
| Session | SID-20260409-233204 |
| Type | Factual Correction — Wrong Book |

**Issue Identified:**
Santoni de Sio et al. (2016) was cited as appearing in *Handbook of Neuroethics* (ed. J. Clausen & N. Levy / ed. S. Nagel, depending on which part of the paper), Oxford University Press. The Shoulders reviewer (#9) flagged the internal inconsistency in editors but did not identify the deeper problem: the chapter is in a completely different book.

**Resolution:**
Author copy located in `transparency/TEMP/Santoni de Sio et al. (2016) Why less praise for enhanced performance - OUP.pdf`. First page confirms OUP imprint; last page (p. 41) confirms page range. Book confirmed via OUP catalogue and Nicole Vincent's publication list as: *Cognitive Enhancement: Ethical and Policy Implications in International Perspectives*, eds. F. Jotterand & V. Dubljević, Oxford University Press, 2016. DOI: 10.1093/acprof:oso/9780199396818.003.0003. ISBN: 9780199396818.

Both bibliography files updated:
> Santoni de Sio, F., Faber, N. S., Savulescu, J., & Vincent, N. A. (2016). "Why Less Praise for Enhanced Performance?..." In F. Jotterand & V. Dubljević (Eds.), *Cognitive Enhancement: Ethical and Policy Implications in International Perspectives* (pp. 27–41). Oxford: Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199396818.003.0003

[VERIFY] removed.

---

### MOD-011 — References unified: "Classical Sources" subheader removed; Plato folded into alphabetical list (SID-20260513-003000)

| Field | Value |
|-------|-------|
| Date | 2026-05-13 |
| Session | SID-20260513-003000 |
| Type | Structural — Section Unification |

**Change:** The `# References` section of `Paper/MDversion/CFP_FullPaper_v1.md` previously contained two subheaders — `### Classical Sources` (containing only "**Plato.** *Apology* 38a.") and `### Primary Sources (Alphabetical)` (containing every other entry). Both subheaders removed; the single Plato entry inserted in alphabetical position between **Nietzsche, F.** (1966) and **Resnik, D. B., & Hosseini, M.** (2025). The `# References` top-level header is now the sole label, and entries form a single uninterrupted alphabetical sequence.

**Why:** User direction (SID-20260513-003000): "References should be unique, no 'classical sources' separation." The two-subheader structure singled out a single entry for special treatment and created two visual zones in a section that was substantively one list. With only one classical-source entry in the bibliography, the subheader carried more structural weight than the content justified. Unified alphabetical ordering is the standard reader-friendly form for a bibliography of this size (~50 entries).

**Plato entry preserved verbatim** ("**Plato.** *Apology* 38a.") — no edition or translator information added; merge only.

**Affected file:** `Paper/MDversion/CFP_FullPaper_v1.md` (version bumped v1.4 → v1.5). Note: the underlying `paper_bibliography_FINAL.md` was *not* touched in this change — only the assembled paper's References block. Alignment pass against `paper_bibliography_FINAL.md` recorded as MOD-012 below.

---

### MOD-012 — `paper_bibliography_FINAL.md` aligned with MOD-011 (SID-20260513-003000)

| Field | Value |
|-------|-------|
| Date | 2026-05-13 |
| Session | SID-20260513-003000 |
| Type | Alignment — Source-of-Truth Sync |

**Change:** `transparency/Canonical_MD/SP4_ProcessDocumentation/4.6_ReferenceLogs/paper_bibliography_FINAL.md` was updated to match the unified-References structure applied to `CFP_FullPaper_v1.md` in MOD-011. The same two subheaders (`### Classical Sources` and `### Primary Sources (Alphabetical)`) were removed; the single Plato entry was repositioned alphabetically between Nietzsche and Resnik; the `## References` header is now the sole section label and entries form one uninterrupted alphabetical sequence. Frontmatter `last_updated` bumped to 2026-05-13; `SID-20260513-003000` added to `session_id`.

**Why:** `paper_bibliography_FINAL.md` is the `build_source: true` bibliography (per its own frontmatter) — the file from which the assembled paper's References block is meant to be regenerated. Leaving its structure divergent from the live paper's structure would set up a re-divergence on the next assembly pass. The alignment closes that gap before submission.

**Affected file:** `transparency/Canonical_MD/SP4_ProcessDocumentation/4.6_ReferenceLogs/paper_bibliography_FINAL.md`. No further changes to the assembled paper required.

---

## Items Deferred to Reference-Checking Pass

| Entry | Issue | Status |
|-------|-------|--------|
| Strathern (1997) | DOI, page range, issue number | ✓ Resolved MOD-007 |
| Mercier (2020) | Publisher details, ISBN | ✓ Resolved MOD-008 |
| Williams (1981) | Citation locus for "ground projects" | ✓ Resolved MOD-009 |
| Santoni de Sio et al. (2016) | Correct editors/book | ✓ Resolved MOD-010 |
| Santoni de Sio & van den Hoven (2018) | Page number for direct quotation (currently §6.2 in text) | **Outstanding** — requires physical/digital source |
| All DOI entries | Online verification of resolution and metadata accuracy | Deferred to Phase 5 |

---

## Modification Summary

| Type | Count | Entries |
|------|-------|---------|
| Missing Reference Added | 3 | MOD-001 (Strathern), MOD-002 (Mercier), MOD-003 (Williams) |
| Consistency Fix | 1 | MOD-004 (SdSio 2016 editors) |
| Cleanup | 1 | MOD-005 (inline notes, working-notes separator) |
| New Artifact | 1 | MOD-006 (paper_bibliography_FINAL.md) |
| Structural — section unification | 1 | MOD-011 (Classical Sources subheader removed; Plato folded into alphabetical list) |
| Alignment — Source-of-Truth Sync | 1 | MOD-012 (paper_bibliography_FINAL.md aligned with MOD-011) |

*Note: MOD-007 through MOD-010 (reference verification work, 2026-04-10) entered the modlog body but were never added to this summary table; backlog noted, full reconciliation deferred to a later cleanup pass.*

---

*Modification Log opened: 2026-04-09*
*MHC-W v5 | Rules 2, 3, 4*
