---
artifact_type: modlog
label: CFP_4.2.44_ModificationLog_DeclarationsSection_v1_29
document: "Full_paper_canonical.md v1.28 → v1.29 — added the Springer Nature 'Declarations' section before the References"
project: JPEP
created: 2026-06-23
last_updated: 2026-06-23
session_id: SID-20260622-191852
inputs:
  - "Paper/MDversion/Full_paper_canonical.md (v1.28)"
  - "Springer Nature Submission Guidelines — Authorship Principles / Declarations / AI policy (pasted by the author)"
  - "CFP_4.2.43_ModificationLog_TitleVerification_v1_28.md (predecessor)"
output_completed:
  - "Paper/MDversion/Full_paper_canonical.md (v1.29)"
  - "Paper/MDversion/Full_paper_submission_anon.md + Full_paper_arxiv_v4.md (re-derived; anon guard passed; identifier-free)"
  - "Paper/journal/CFP_FullPaper_v1_29.docx (built); Paper/journal/Full_paper_submission_anon.docx (rebuild PENDING — file was locked open in Word at build time; re-run pandoc once closed)"
feeds_into: "EthIT submission — required Declarations section"
validation: approved
---

# Modification Log: Full_paper_canonical.md v1.28 → v1.29 — Declarations Section

## Provenance & method

Springer Nature's guidelines state, repeatedly, that the declarations "should be summarized in a statement and included in a section entitled 'Declarations' before the reference list" — covering Funding, Competing interests, Ethics approval, Consent, Data/Code availability, and Author contributions. A `Declarations` section was added to the manuscript body, immediately before `# References`, with one `##` sub-heading per item (the format the guidelines call for).

**Anonymity:** every statement is phrased without identifying information ("the author", "the sole author", "no funding"), so the section is compatible with double-anonymous review. The intellectual-debt / TU/e-seminar connection to the EiC is **not** placed here — it stays in the cover letter (editor-only), where revealing it does not de-anonymize the manuscript.

## Why the AI item is only a cross-reference

Springer requires *substantive* LLM use to be documented in the manuscript (Methods or a suitable alternative part). The manuscript body **already** does this explicitly — §1: "an instance of substantially AI-assisted ethics research… the models drafted candidate passages and the author directed, accepting or overriding at every substantive turn"; abstract: "drafted by the models under the author's direction." A full AI paragraph in Declarations would therefore be redundant, so the `Use of generative AI` item is a single line cross-referencing §1 and the Supplementary Material and affirming human accountability / AI-not-authors.

---

## Modification Entries

### MOD-001 — `Declarations` section added before References

| Field | Value |
|-------|-------|
| Date | 2026-06-23 |
| Type | Addition (required submission element) |

Eight `##` items under a new `# Declarations` heading:

- **Funding** — none.
- **Competing interests** — none relevant to the content.
- **Ethics approval** — Not applicable (philosophical scholarship; no human/animal research).
- **Consent to participate** — Not applicable.
- **Consent to publish** — Not applicable.
- **Data and code availability** — no empirical datasets / custom code; the SP-1–SP-5 record is provided as Supplementary Material and available to the editorial office; Zenodo DOI at acceptance.
- **Author contributions** — sole author (conceived, argued, drafted, revised, approved).
- **Use of generative AI** — one-line cross-reference to §1 + the Supplementary Material; author accountable for the final text; AI tools not authors.

No existing body text changed; this is a pure addition between §7's closing separator and the References heading (one `---` separator kept on each side).

---

## Build, derivation & verification

- `derive_distributions.py` re-derived the arXiv + anonymized editions from v1.29; **anon guard passed**; the anon **markdown** carries all eight Declarations items and is identifier-free (verified).
- `CFP_FullPaper_v1_29.docx` built.
- ⚠️ `Full_paper_submission_anon.docx` rebuild **failed with "permission denied"** — the file was open in Microsoft Word. Re-run the pandoc step (or `build`/derive flow) once Word is closed; the source markdown is correct, so the rebuild is purely mechanical.

---

## Modification Summary

| Type | Count | Examples |
|------|-------|----------|
| Addition (required element) | 1 | MOD-001 (Declarations section) |

The last required structural element for the Springer/EthIT submission. The AI disclosure was already satisfied by the body; Declarations adds the non-AI items (funding, interests, ethics/consent N/A, data availability, contributions) plus a one-line AI cross-reference.

---

*Modification Log generated: 2026-06-23 | SID-20260622-191852 | MHC-W Rules 2, 3, 4*
