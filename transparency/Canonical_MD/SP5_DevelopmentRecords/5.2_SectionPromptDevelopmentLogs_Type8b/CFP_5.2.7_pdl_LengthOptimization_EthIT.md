---
project: JPEP
sp: SP5
artifact_type: pdl
document_type: Type 8b - Section Prompt Development Log
label: CFP_5.2.7_pdl_LengthOptimization_EthIT
title: "PDL: Length Optimization + Conformance for Ethics and Information Technology submission (v1.16 → v1.17)"
created: 2026-06-14
last_updated: 2026-06-14
status: Active
session_id: SID-20260614-145954
inputs:
  - "Ethics and Information Technology submission guidelines (read 2026-06-14 via Chrome MCP: link.springer.com/journal/10676/submission-guidelines)"
  - "SNAPP Double Anonymous Peer Review Guidelines (springernature.com/gp/snapp/submitting/how-to-submit/double-anonymous)"
  - "Paper/MDversion/Full_paper_canonical.md (v1.17, canonical; renamed 2026-06-14 from CFP_FullPaper_v1.md)"
  - "Paper/MDversion/Full_paper_submission_anon.md (EthIT anonymized submission source)"
  - "Pre-submission citation + conformance audit (this session, /check-bibliography)"
feeds_into:
  - "Forthcoming compression modlog (v1.16 → v1.17)"
  - "Full_paper_submission_anon.docx (EthIT editable-manuscript deliverable)"
related:
  - "CFP_5.2.6_pdl_AIVoiceArchiveTestimonialLayer.md (prior compression/Archive context)"
  - "Opus length-optimization review agent (this session)"
validation: approved
versioning_convention: git_inplace
---

# PDL: Length Optimization + Conformance for EthIT submission (v1.16 → v1.17)

## Overview

After the desk-reject at *Philosophy & Technology*, the paper is being prepared for
*Ethics and Information Technology* (Springer, double-anonymous). A pre-submission
audit this session read the official EthIT submission guidelines and the SNAPP
double-anonymous guidelines in the live browser, then checked the citations in both
the reference list and the final built PDF. This PDL records the optimization-round
decisions and the prompt developed for the length review. The detailed findings are
not duplicated here; this log captures *what we decided to generate and why*.

---

## PDL-001 — Pre-submission conformance audit (decision context)

| Date | Session | Authored by |
|---|---|---|
| 2026-06-14 | SID-20260614-145954 | Claude Opus 4.8 audit; user direction |

**Findings, by severity:**

- **Tier 1 — build defect (FIXED this session).** In the pandoc-built PDF, three
  reference entries (Cheng 2025, Lloyd 2025, Shafer-Landau 2003) were swallowed into
  the preceding entry because the markdown source lacked a blank line between them.
  Fixed in `CFP_FullPaper_v1.md`, `Full_paper_submission_anon.md`, and
  `paper_bibliography_FINAL.md`. (Author had already fixed the arXiv edition.)
- **Tier 2 — submission blockers.** Body ≈ 8,905 words vs EthIT max ≈ 8,000
  (title/abstract/references excluded; Archive + footnotes counted) → ≥ ~900 words to
  cut. Editable manuscript required (.docx/LaTeX, **not** PDF). Keywords (4–6) absent.
  Declarations + Data-Availability handled via the Snapp interface / separate title page.
- **Tier 3 — reference style ≠ APA 7** (in-text comma; bold authors; quoted titles;
  publisher locations). Deferred.
- **Tier 4 — anonymization.** PDF metadata clean, body third-person, archive URL
  withheld. Distinctive title + public arXiv preprint = residual de-anonymization risk.
- **Citation integrity:** 40 entries, all cited, all in-text citations resolve. Only
  open item: `Hosseini et al. 2023` ambiguous between two 2023 works.

**Decision:** fix Tier 1 immediately; make length the active work item; sequence the rest.

---

## PDL-002 — Scope decisions for the EthIT round (author's calls)

| Date | Session | Authored by |
|---|---|---|
| 2026-06-14 | SID-20260614-145954 | User decisions |

1. **No PDF for EthIT — submit the editable `.docx`.** The journal requires an editable
   manuscript; the PDF is for arXiv only.
2. **Run a length-optimization pass before submitting** (PDL-003).
3. **APA-7 restyle deferred to the end** — applied after content is final, consistent
   with copyediting-stage practice.
4. **`Hosseini et al. 2023` to be disambiguated** (two distinct 2023 works).
5. **Anonymization risk accepted** — distinctive title + public arXiv is a tolerated
   double-blind risk, not a blocker.

---

## PDL-003 — The length-optimization review prompt

| Date | Session | Authored by |
|---|---|---|
| 2026-06-14 | SID-20260614-145954 | User-specified single question; Claude Opus 4.8 framing |

**What to generate:** an analytic (non-editing) review of `CFP_FullPaper_v1.md`
answering the author's single question — *how can the paper be shortened; where is it
redundant; what is not useful, or an aside that does not contribute to the development
of the argument?*

**Options considered:**

1. **Single focused question, one Opus reviewer (chosen).** Pros: matches the author's
   explicit instruction; keeps the reviewer unanchored by our own priors; fast. Cons:
   one perspective.
2. **Multi-agent adversarial panel.** Pros: broader coverage. Cons: over-engineered for
   a compression pass; the author asked for one question, not a debate.

**Decision / specification given to the reviewer:**
- Target: cut ≥ 900–1,000 words (body ≈ 8,905 → ≤ 8,000, aim ~7,800 for margin).
- Output: prioritized, **located** list — section + anchor phrase; type
  (REDUNDANCY / ASIDE / COMPRESSIBLE); proposed action; est. words saved; risk to argument.
- Preserve the spine (two-level contestedness; three defeats; Williams agent-integrity;
  tracking pivot; SP-1..SP-5 framework; self-exemplification; dual-assessment / defense-in-depth).
- Out of scope: style, anonymization, references, typos.

**Rationale:** length is the one hard EthIT blocker that requires intellectual judgment
(the others are mechanical). A single blunt question keeps the reviewer honest about
genuine flab rather than trivial trims.

**What it affects:** the cut list selected from the review becomes v1.17 (logged as a
compression modlog), which is then re-derived into the anon `.docx` for submission.

---

## PDL-004 — Review outcome + selected cuts

| Date | Session | Authored by |
|---|---|---|
| 2026-06-14 | SID-20260614-145954 | Opus length-review agent; user selection |

**Review outcome (summary).** The reviewer's diagnosis: the paper is padded with
*restatement*, not digression. Three theses recur 3+ times (Williams agent-integrity;
the cognitivist conditional; the Zimmerman/Cheng cognitive-offloading reply) and the
"first iteration / not a settled standard" refrain appears ~6 times. ~1,155 words are
recoverable from redundancy with low risk to the spine. Highest-value cuts: §3.3 delete
the "Philosophy is, in the Williams sense" restatement (~175 w); Archive trim the
opening recap + the non-load-bearing "operative conception of authorship" block
(~235 w); §3.4 collapse the re-derived cognitivist conditional (~140 w); §7 compress the
limitations litany (~150 w); de-duplicate the offloading argument to §5.4 only (~70 w).
Explicitly protected: §3.3 inversion-paragraph body (l.138); §3.5 three beats + the
"extension, not third defeat" qualification; §5.4 defense-in-depth; the SP-1..SP-5
enumeration; the Porsdam Mann paragraph (§3.3 l.144).

**Selected cuts (option a — full low-risk set, applied 2026-06-14):** 19 surgical cuts
executed in `CFP_FullPaper_v1.md` (in-place → v1.17). Body 8,905 → 8,299 words (−606;
tool-counted, excl. title/abstract/refs); abstract unchanged (202 w). Every citation
preserved — Moseley, Cordasco (2026a/b), Zimmerman & Cheng (kept in §5.4), Levy, and
Sartre were re-homed rather than orphaned; no reference-list change.

**Author decision on length:** the EthIT guideline says "approx. 8,000 words"; the author
judged 8,000 a *soft*, not hard, limit and declined further (potentially
quality-degrading) cuts to chase the number — a paper can be desk-rejected for other
reasons, and this pass was an improvement on its own terms. v1.17 stands at ~8,300 body
words. If a length query arises at submission, address it then (moving the AI Usage
Archive to supplementary material remains the clean lever, ~650 w without touching the
argument).

---

## Current state

Complete (2026-06-14). Option (a) applied → v1.17 (body ~8,300 w). Length treated as a
soft limit per author decision; no further cuts. Remaining EthIT-submission to-dos
(tracked, not yet done): re-derive the anon `.docx` from v1.17; disambiguate
`Hosseini et al. 2023`; APA-7 restyle at the end; keywords (4–6); Declarations +
Data-Availability via the Snapp interface; separate non-anon title page. (Master file
renamed 2026-06-14: `CFP_FullPaper_v1.md` → `Full_paper_canonical.md`; label
`CFP_FullPaper_v1` retained as the cross-reference ID, CFP lineage in `cfp_branch`.)

---

*PDL prepared 2026-06-14 in JPEP session SID-20260614-145954. Validation: approved.*
