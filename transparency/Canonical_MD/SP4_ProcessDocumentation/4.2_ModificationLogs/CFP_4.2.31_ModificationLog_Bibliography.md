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

---

*Modification Log opened: 2026-04-09*
*MHC-W v5 | Rules 2, 3, 4*
