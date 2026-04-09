---
project: JPEP
document_type: Type 11 - Note
label: CFP_5.3.28_Note_ShouldersReview_Evaluation
document_subtype: review_evaluation
date_created: 2026-04-10
session_id: SID-20260409-233204
status: Active
validation: approved
rewrite_planned: true
rewrite_note: "This note is an internal evaluation document. To be rewritten as external feedback for Shoulders (the company) in a future session."
inputs:
  - CFP_5.3.25_ShouldersReview_raw.md
  - CFP_5.3.27_Note_ReviewResponse_Draft.md
  - CFP_4.2.17_ModificationLog_Section5.md (MOD-010)
  - CFP_4.2.18_ModificationLog_Section6.md (MOD-019)
  - CFP_4.2.19_ModificationLog_Section7.md (Entry 7)
  - CFP_5.4.10_Conclusion_v1.md (v2 rewrite)
related:
  - CFP_5.3.24_Note_ReviewerB_OpusReview_v1.md
---

# Evaluation: Shoulders AI Peer Review

**Reviewed artifact:** CFP assembled paper v1 (CFP_5.3.23 build)
**Reviewer:** Shoulders AI peer review (shoulde.rs), model unspecified
**Review filed:** CFP_5.3.25_Note_ShouldersReview_v1.md
**Evaluation produced:** SID-20260409-233204

---

## Character of the Review

The Shoulders review is formally well-structured and covers the paper systematically across 31 numbered comments. Its tone is authoritative — even dismissive ("submitted in a condition that is not ready for peer review") — and several of its more structural objections were already resolved or in the process of being resolved before the review arrived (section numbering, bibliography cleanup). This inflates the apparent severity of the critique.

The review is best understood as two overlapping things: a genuine philosophical critique with several sharp observations, and a systematic form-checking exercise that treats submission-state artefacts as substantive problems. Separating these is essential for evaluating what it actually contributed.

---

## What the Review Got Right: Changes Made

### S3/S25/S1,S2 — Abdulhai preprint over-relied on (→ implemented)

This is the review's most valuable substantive contribution. Three comments converge on the same problem from different angles: preprint status unacknowledged, operationalization of "stance neutralization" unexplained, inference from general LLM writing to ethics research specifically unjustified, and the quantitative figure presented as established fact. The objection is correct on all counts. The response (Entry 7, Section 7 modlog) hedged the passage substantially: preprint status flagged explicitly, study scope noted, inference to ethics research qualified conditionally. The improvement is real. The paper was overclaiming.

### S21 — "Ecological validity" non-standard usage (→ reversed, SID-20260410-002246)

The reviewer claimed the paper's usage conflicts with the methodological meaning (generalizability to real-world settings). MOD-010 accepted this and added a "non-standard sense" disclaimer. On further analysis, the reviewer's critique was mistaken: the paper's usage applies the same conceptual structure to a new domain. An experimental finding is ecologically valid if the phenomenon holds outside the lab; a documentation requirement is ecologically valid if it achieves its purpose in actual scholarly practice rather than only in an idealized model of that practice. The mapping is direct, not a departure from the concept. MOD-010 disclaimer removed (MOD-011); replaced with an affirmative formulation and a footnote candidate clarifying the analogy unapologetically.

### S22/S27 — Self-exemplification tension and audit machinery risk treated too cursorily (→ implemented via Conclusion v2)

S27 correctly identifies that disclosing retrospective documentation in a brief Conclusion caveat was insufficient given how central the ecological validity condition is to the argument. The disclosure needed to be framed honestly and earlier. The Conclusion v2 addresses this: the Neurath's boat passage explicitly addresses the infrastructure gap (plank-by-plank, no dry dock), the limitations paragraph opens with "should be stated plainly," and the audit-culture risk gets a full paragraph rather than a sentence. The reviewer's formal framing of where things stood contributed to the rewrite even if the author already knew the fix was needed.

Note: The author's internal note in CFP_5.3.25 correctly observes that the Conclusion had overstated the retrospective documentation problem ("the early phase was documented retrospectively" — an overstatement, since the v1/v2 modification logs were contemporaneous; what was retrospective was chain/infrastructure recovery). The Conclusion v2 navigates this more precisely without the distortion.

### S10 — Citation locator `(§6.2)` rather than page number (→ tagged, pending)

Correct and precise. All other direct quotations use page numbers; this one uses a section locator. Inconsistency flagged in MOD-019. Outstanding: the physical or digital source is needed to supply the page number.

### S12/S11 — Strathern and Mercier absent from bibliography (→ resolved)

The review correctly identified both as cited in-text but missing from the bibliography. Both have now been added and verified against sources (this session).

### S9 — Santoni de Sio 2016 editor inconsistency (→ resolved, with deeper correction)

The reviewer caught a real inconsistency: two parts of the paper gave different editors for the same volume. The reviewer's own diagnosis was incomplete — they assumed the question was Clausen & Levy vs. S. Nagel, when in fact the chapter is in an entirely different book (*Cognitive Enhancement*, Jotterand & Dubljević, OUP, not *Handbook of Neuroethics*, Clausen & Levy, Springer). The inconsistency was real; the reviewer's identification of its source was wrong. Resolved via author-copy verification (SID-20260409-233204).

### S18/S14 — Bibliography contained internal workflow artefacts (→ resolved)

The bibliography as submitted included verification flags, NEXT ACTIONS lists, section-by-section usage logs, and branch-name metadata. Accurate diagnosis. The split into `paper_bibliography.md` (working) and `paper_bibliography_FINAL.md` (submission-ready) addresses this structurally.

---

## What the Review Got Wrong or Was Rejected

### S1/S7/S23 — MHC transfer not argued (→ rejected)

The reviewer argues the paper fails to justify the transfer of MHC from autonomous weapons to scholarly authorship, because the stakes, reversibility, and nature of "control" are radically different. The objection misunderstands the argument structure. The paper does not argue by analogy from weapons systems to scholarship — it provides its own independent argument for why tracing and tracking are required in the scholarly context. MHC is cited because the framework already exists and the terminology is precise, not because the weapons-systems justification transfers. No elaboration of structural homologies is needed because no argument by structural analogy is being made. Authorial judgement: declined.

### S2/S5/S19 — Question-begging charge is symmetrically vulnerable (→ rejected with ironic concession)

The reviewer argues that if the cognitivist is question-begging by presupposing that ethics tracks truth, the paper equally question-begs by presupposing expressivism is a live option. This misunderstands Gallie's essentially contested concepts argument. The paper's point is not that expressivism is correct — it is that both cognitivists and expressivists exist within the same academic community and neither has succeeded in excluding the other. The cognitivist cannot appeal only to cognitivist evaluators; they are embedded in a community that has not settled the dispute. The symmetry the reviewer proposes would only hold if the community had expelled expressivists, which it has not. The reply (Section 3 v3 rewrite) adds an ironic concessive — "they may well be right" — to acknowledge the symmetry without conceding the normative conclusion.

### S4/S20 — Costly signaling undermined by AI fabrication capacity (→ partially accepted, demoted)

The reviewer's objection is that AI assistance can generate detailed-seeming process documentation at low cost, so the fabrication barrier the paper posits is illusory. This deserves a more serious response than the paper gives. The author's position: the costly thing is the documented activity (the volume and complexity of interactions, choices, reviews, and revisions), not the documentation itself; documentation of a complex process is genuinely expensive to fabricate convincingly; inconsistencies in real-world processes are detectable by AI reviewers. The costly-signaling argument was demoted from a primary justification to a supporting consideration, and the non-adversarial setting assumption made explicit. A fair trade: the reviewer identified genuine overreach in the original formulation.

### S31 — Williams "ground projects" citation locus (→ reviewer was wrong)

The reviewer suggested that "ground projects" was developed in Smart & Williams (1973) rather than "Persons, Character and Morality" in *Moral Luck* (1981). This is incorrect. Secondary literature consistently attributes "ground projects" to *Moral Luck*; Smart & Williams 1973 is cited for different aspects of the utilitarian critique. Verified via published secondary sources this session. The paper's citation was correct. No change needed.

### S26 — Modular synthesis and generative art analogy: artist designs the system (→ reviewer was wrong)

The reviewer claims that in both modular synthesis and Harold Cohen's AARON the artist "designs the generative system from scratch," and that LLM users, who prompt a pre-existing model they did not design, therefore occupy a structurally different position. The premise is false on both counts. Modular synthesists buy pre-designed modules — oscillators, filters, VCAs — from manufacturers whose internal circuits they do not design and mostly do not understand. What they design is the patch: the routing, the connections, the control relationships. Cohen wrote rules in a programming language he did not design, running on hardware he did not design; his authorship was at the level of representational rules and aesthetic constraints, not the underlying substrate. The structure is identical across all three cases: a pre-designed component layer (modules / language+hardware / trained model) over which the author exercises compositional agency (patch / rule set / prompt architecture and intellectual direction). The reviewer's disanalogy does not hold. No paper change warranted; the analogy stands as written.

---

## Left Standing: Legitimate Objections Not Engaged With

### S28/S6 — Adverse selection claim unargued (→ **resolved, SID-20260410-002246**)

The reviewer correctly notes that the adverse selection framing is asserted rather than demonstrated, and that "first-mover disadvantage" is at least as plausible a community dynamic as the transparency-inverts-selection claim. Resolution: "invert this" hedged to "tend toward a different dynamic: they are more likely to attract" — preserves the intuition without promising a formal result. See CFP_4.2.18 MOD-020.

### S29 — Lloyd Standard 4 dismissed too quickly (→ **resolved, SID-20260410-002246**)

One sentence dismisses Lloyd (2025)'s intra-textual clarity standard. Resolution: expanded to two sentences — premise supported by self-reference to SP-4 ("as the process documentation in SP-4 illustrates"), pivot preserved. See CFP_4.2.18 MOD-021.

### S30 — Sartrean bad faith underspecified (→ **resolved, SID-20260410-002246**)

The reviewer's objection is precise: Sartrean bad faith is a first-person psychological and ontological concept (self-deception about one's own freedom and facticity), not naturally applicable as a normative charge against non-disclosure to others. Resolution: paragraph substantially rewritten via Opus consultation. First-person dimension made explicit; intersubjective bridge built via being-for-others ("my freedom never exists in isolation; it is constituted in a field of other freedoms"). A genuine philosophical improvement — the reviewer's input was accepted as substantive. See CFP_4.2.16 (Section 3 modlog, post-review second pass entry).

---

## Pre-Existing Problems or Submission Artefacts

**S15/S16 — Abstract absent:** Phase 4 work item, not a substantive critique. Already in the queue.

**S8/S24 — Section numbering inconsistency:** Already fixed by the renumbering session (SID-20260409-155040) before the review response session. The reviewer caught the pre-fix state.

**S17/S3 — SP packages not submitted:** Submission-format issue, not a content failure. The SPs exist and are documented. A genuine submission would include them.

---

## Overall Assessment

The Shoulders review performed three distinct functions, of unequal value.

**Useful:** A small cluster of observations genuinely improved the paper — Abdulhai hedging, ecological validity flag, bibliography hygiene, and the self-exemplification disclosure prominence. These are the review's real contribution.

**Serviceable:** Several form-checking comments (abstract, numbering, bibliography workflow artefacts) accurately described the paper's pre-submission state without adding philosophical insight. They would have been caught in any ordinary editorial check.

**Mistaken or miscalibrated:** The MHC-transfer objection fundamentally misreads the argument structure. The question-begging symmetry argument misunderstands Gallie. The Williams citation locus was wrong. The modular synthesis/AARON disanalogy (S26) rests on a false premise — neither modular synthesists nor Cohen design "from scratch"; both work with pre-designed component layers and exercise compositional agency above them, exactly as LLM authors do. The overall framing as "not ready for peer review" overstates the structural problems, most of which were already resolved or in train.

**Left standing:** None. All three — S28/S6 (adverse selection), S29 (Lloyd Standard 4), S30 (Sartre) — resolved in SID-20260410-002246.

Compared to the Opus review (CFP_5.3.24), the Shoulders review is more granular on bibliographic and presentation issues and less penetrating philosophically. The Opus review identified the deeper structural problems (proves too much, underdetermined framework derivation, Conclusion summary vs. conclusion) with greater precision. The Shoulders review's most distinctive contribution is the Abdulhai hedging cluster, which Opus also flagged but less specifically.

---

*CFP_5.3.28 — SID-20260409-233204*
