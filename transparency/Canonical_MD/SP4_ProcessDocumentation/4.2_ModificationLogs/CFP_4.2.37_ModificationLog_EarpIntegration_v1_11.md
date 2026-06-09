---
artifact_type: modlog
document: CFP_FullPaper v1.10 → v1.11 — Earp corpus integration pass
project: JPEP
created: 2026-06-09
session_id:
  - SID-20260609-095833
inputs:
  - Paper/MDversion/CFP_FullPaper_v1.md (v1.10, baseline at commit prior to this session's edits)
  - transparency/Canonical_MD/SP5_DevelopmentRecords/5.3_Notes_Type11/CFP_5.3.33_Note_Briefing_EarpCorpus.md (in-session briefing — verified-evidence + JPEP alignment map, constraint document)
  - transparency/Canonical_MD/SP5_DevelopmentRecords/5.3_Notes_Type11/CFP_5.3.29_Note_CordascoBriefing.md (structural model for the welfare-objection / Earp-engagement pattern; referenced in CFP_5.3.33 §1)
  - Porsdam Mann, Earp, Møller, Vynn & Savulescu (2023) AUTOGEN — body verified via Academia.edu mirror (academia.edu/104478807)
  - Earp, Porsdam Mann, Sawai & Wangmo (2026) Death/Authorship — body verified via Academia.edu mirror (academia.edu/167307834)
  - Earp, Shahvisi & Frith (2025) JME editorial — paywalled; reported substance only
output_completed: Paper/MDversion/CFP_FullPaper_v1.md (v1.11)
feeds_into: AI-voice rewrite pass (Change B, planned as v1.11 → v2.0; voice spec to land at CFP_5.3.34)
validation: approved
---

# Modification Log: CFP_FullPaper v1.10 → v1.11 — Earp Integration

Per-revision-pass modlog for the Earp corpus integration into the JPEP body, following the pattern established by `CFP_4.2.35` (v1.2 reviewer revisions) and `CFP_4.2.36` (v1.3 Reviewer-B integration).

The integration is constrained by the standing briefing `CFP_5.3.33_Note_Briefing_EarpCorpus.md`, which rules:
1. JPEP does not import a theory of authorship; the senior-author-analogy paper (Hurshman/Earp 2025) is reserved for editorial-engagement layer (cover letter / reviewer-objection responses), not body.
2. Only pieces with verified body text or confirmed reported substance enter the body. The provenance-problem paper (Earp et al. 2025 NMI) is paywalled with no OA mirror and remains in the verification backlog — not cited in v1.11.

Single-file `git_inplace` versioning. `git diff` over the v1.10→v1.11 commit will be the authoritative cumulative change record.

---

## Modification Entries

### MOD-001 — §3.3: AUTOGEN engaged as a contested-terrain verdict subsumed by the reader-devolution framework

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Citation + substantive philosophical engagement (one new paragraph after the welfare-economic exchange) |
| Source of finding | In-session briefing `CFP_5.3.33` §2.2 (body-text-verified piece), §4.1 alignment claim, and §4.3 subsumption framing |

**Issue:** §3.3's existing Cordasco welfare-economic exchange (now partly footnoted in v1.10) closes on "the moral duty is independent of the welfare calculation … not to the duty itself." This handles the welfare-economic objection-type but does not address a structurally distinct competing position: the **author-side quality-of-contribution** view, on which AI-assisted scholarship is legitimate only when human substantive contribution + costly evaluation are in place (Porsdam Mann, Earp, Møller, Vynn & Savulescu 2023, the AUTOGEN proposal). An initial draft of this MOD framed AUTOGEN as a parallel route converging with JPEP's argument on the operational claim that yes/no disclosure cannot be the duty; on author review that framing was rejected as fence-sitting — it amounted to "two roads to the same conclusion" rather than to a position. The corrected framing aligns with briefing §4.3: JPEP does not compete with author-side criteria, it subsumes them by making them applicable. Whether AI-assisted work exhibits *enough* contribution, *substantial enough* judgment, *costly enough* evaluation is itself a contested question; reader-side process transparency is the condition under which such verdicts can be reached at all.

**Change:** One new paragraph inserted after the Cordasco closer, before the §3.4 heading. Text:

> Porsdam Mann, Earp, Møller, Vynn & Savulescu (2023), defending a model of personalized AI-assisted academic enhancement, hold that transparency is necessary but not sufficient: legitimacy demands substantial human contribution and costly evaluation of AI output, measured on the author side. The framework developed here goes further. Whether AI-assisted scholarship exhibits *enough* human contribution, *substantial enough* judgment, *costly enough* evaluation is itself a contested question; it cannot be settled by the framework itself without forcing one of the answers as the operative standard — which is precisely what the essential contestedness of ethical inquiry forbids. Earp et al.'s author-side criterion is therefore not a competing answer to the same question this paper is asking but one of the verdicts a community equipped with process documentation can reach about a given work. The framework here does not adjudicate it; it makes its application possible. Process transparency is the condition under which such verdicts can be reached at all.

**Words:** +154 (initial draft was +66; expanded to +154 after author review identified the compressed version as fence-sitting and the corrected position as load-bearing for §3.3).

**Constraint compliance:** Honours briefing §4.3 directly — JPEP does not adopt Earp et al.'s author-side criterion, does not reject it, makes it applicable through the reader-side evidentiary record. The closer ("Process transparency is the condition under which such verdicts can be reached at all") is the paper's position, not a triangulation move. Paraphrase only — no verbatim quote (a quoted Servant/Co-Creation distinction would commit JPEP to a framing it does not adopt).

**Scope discipline:** Source draft (`CFP_5.4.4_Section3_v3.md`) is unchanged, per project rule 1 — Earp integration lands only in the assembled paper.

**Author decision recorded:** the rejected "triangulation across three independent routes" closer was identified by the author as fence-sitting — "this amounts to not taking a position." The replacement closer ("Process transparency is the condition under which such verdicts can be reached at all") asserts the framework's distinctive claim rather than treating the framework as one option among several converging on the same operational conclusion.

---

### MOD-002 — §5.4 close: disaggregation editorial added as institutional evidence of unsettlement

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Anchor sentence + citation paragraph (~111 words combined) at end of §5 |
| Source of finding | Briefing `CFP_5.3.33` §2.1 (body-text-verified) and §4.1 |

**Issue:** §5.4 closes at v1.10 with *"Feasibility is what an author can demonstrate by exhibition; adequacy is what only the community can settle."* The section makes the no-single-normative-target argument structurally but does not cite the institutional evidence that the authorship concept is, in fact, presently unsettled — and could be cited for that fact without endorsing any particular disaggregation diagnosis.

**Change:** New paragraph appended to §5.4, immediately before the §6 horizontal rule. The anchor sentence (first sentence of the inserted paragraph) is itself new — it did not appear verbatim in v1.10 (grep-confirmed). Text:

> Because there is no settled view of what philosophical authorship requires, the framework must not presuppose one. That the concept is presently unsettled is not an internal claim of this paper: writing in the inaugural issue of *JME Practical Bioethics*, Earp, Porsdam Mann, Sawai & Wangmo (2026) observe that "generative AI can now separate these functions, creating the possibility that, in some cases, neither the human contributor nor the AI would individually satisfy traditional authorship criteria," and call for commentaries on the resulting conceptual question. The framework here neither endorses their disaggregation diagnosis nor any of the candidate models. It registers the unsettlement as a fact about the community to which transparency documentation must answer.

**Words:** +111.

**Constraint compliance:** The non-endorsement language is explicit (*"neither endorses their disaggregation diagnosis nor any of the candidate models"*). Citation function is *existence of institutional unsettledness*, exactly as briefing §4.1 specifies. Verbatim body quote is permitted (briefing §2.1 — confirmed body access via Academia.edu mirror).

**Hedge carried to bibliography and frontmatter `known_issues`:** the DOI `10.1136/jmepb-2025-000046` is flagged for BMJ re-verification — Unpaywall reportedly resolves it to a different paper (Wang & Parent, NRP frameworks). Bibliography entry carries the flag inline; frontmatter `known_issues` carries the deferral pointer.

---

### MOD-003 — §4 close: JME mandatory AI Use Declaration policy added as existence proof

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Citation paragraph (~94 words) inserted before §4's closer |
| Source of finding | Briefing `CFP_5.3.33` §3.5 (reported substance — paywalled source) and §4.1 |

**Issue:** §4 critiques the Hosseini/Resnik/Holmes three-location disclosure prescription (lines 185–189 in v1.10) and closes at line 191 *"This is not an argument against transparency..."* The critique does not register that an alternative structured-mandatory format is already operating at a leading ethics journal — which is both an existence proof that "structured-mandatory beyond yes/no" is operationally workable, and a counterweight to the anticipated objection that JPEP's framework is unimplementable.

**Change:** New paragraph inserted between §4's "self-defeat" paragraph (ending *"…intensifies the asymmetry it was meant to neutralize"*) and the existing closer (*"This is not an argument against transparency…"*). Text:

> Movement at the policy layer is already visible. The *Journal of Medical Ethics* now requires a structured Generative AI Use Declaration before the reference list, with tiered options — no use, limited use of a specified kind, or substantial use (Earp, Shahvisi & Frith 2025). The implementation shows that structured mandatory disclosure beyond a yes/no checkbox is operationally workable in a leading ethics journal without committing it to a single normative theory of AI involvement. It does not by itself answer the format question this paper raises for philosophy; it does show that the question is being asked institutionally, and that the answer is not the binary checkbox.

**Words:** +94.

**Constraint compliance:** Paraphrase only — the JME editorial body text was not accessed (paywalled). The cited substance (tiered declaration, placed before reference list, mandatory) rests on the public reporting summarised in briefing §3.5. The paragraph does **not** endorse the JME policy as philosophically correct for the philosophy case; the third-to-last sentence makes that explicit (*"It does not by itself answer the format question this paper raises for philosophy"*). Citation function is **existence-proof of operationalisability**, exactly as briefing specifies.

**Hedge carried to bibliography and frontmatter `known_issues`:** the title "Clarifying our editorial approach, with some important updates for authors and reviewers" is the **confirmed** title (per CrossRef DOI 10.1136/jme-2025-111363). A Google-Scholar-snippet alternate title "Normalising transparency: an argument for requiring generative AI use declarations in all manuscripts" could not be confirmed as same/distinct piece. Frontmatter `known_issues` carries the disambiguation deferral.

---

### MOD-004 — Two micro-cuts to absorb the word budget

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Two prose deletions, ~26 words total, recovered from compression headroom |

**Issue:** MOD-001 + MOD-002 + MOD-003 add 271 net words. To stay within the ≤250 net-add soft target tracked against the ~700-word Opus-identified compression headroom (work plan), two surgical micro-cuts are applied that do not change argument or evidence:

**Cut 4a (§3.7).** Removed the parenthetical *", in a study that used technology now several generations behind"* from the Schwitzgebel/Schwitzgebel/Strasser 2024 citation. The argumentative function (a 51% Dennett-discrimination rate documented in a study, the rate is speculative but the direction is not) is preserved exactly; the deleted clause was an inline editorial qualifier whose substance is implied by the publication year. -13 words.

- Before: *"…above chance (20%) but well below the hypothesized 80%, in a study that used technology now several generations behind. The current rate is speculative; the direction is not."*
- After: *"…above chance (20%) but well below the hypothesized 80%. The current rate is speculative; the direction is not."*

**Cut 4b (§5.4).** Removed the em-dash aside *"— treating, say, execution-level engagement as the threshold for authentic philosophical authorship —"* from the Strathern/gameability paragraph. The sentence's structural claim (if the community converges on one view, documentation becomes gameable) is preserved; the deleted aside was an illustrative example whose specificity was not load-bearing. -13 words.

- Before: *"…what the proper distribution of human and AI contributions should look like — treating, say, execution-level engagement as the threshold for authentic philosophical authorship — then documentation becomes gameable along that conception."*
- After: *"…what the proper distribution of human and AI contributions should look like, then documentation becomes gameable along that conception."*

**Net effect:** -26 words recovered. v1.10→v1.11 net body delta is **+333 words** (A1 +154, A2 +111, A3 +94, cuts -26). This overshoots the original ≤250 soft target by ~83 words. The overshoot is recorded honestly here: the A1 expansion was load-bearing — the compressed 66-word version was identified by the author as fence-sitting (see MOD-001) — so the soft target was traded against argumentative clarity. The ~700-word Opus-identified compression headroom (parked, work plan reference) remains substantially intact; the v1.11 net add sits well inside total compression budget.

---

### MOD-005 — Bibliography entries added to `paper_bibliography_FINAL.md` and the paper's internal References block

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Three new APA-variant entries, alphabetically inserted in both locations |

Entries inserted (both `paper_bibliography_FINAL.md` and `CFP_FullPaper_v1.md` References block):

Between Cordasco (2026b) and Elsevier (2023):

> **Earp, B. D., Porsdam Mann, S., Sawai, T., & Wangmo, T.** (2026). "Death, authorship, and generative AI — a call for commentaries." *JME Practical Bioethics*, 2, e000046. [DOI 10.1136/jmepb-2025-000046 — flagged for BMJ re-verification: Unpaywall reportedly resolves this DOI to a different paper.]
>
> **Earp, B. D., Shahvisi, A., & Frith, L.** (2025). "Clarifying our editorial approach, with some important updates for authors and reviewers." *Journal of Medical Ethics*, 51(11), 731–734. https://doi.org/10.1136/jme-2025-111363

Between Plato and Resnik & Hosseini (2025):

> **Porsdam Mann, S., Earp, B. D., Møller, N., Vynn, S., & Savulescu, J.** (2023). "AUTOGEN: A personalized large language model for academic enhancement — ethics and proof of principle." *The American Journal of Bioethics*, 23(10), 28–41. https://doi.org/10.1080/15265161.2023.2233356

**Honesty discipline:** The DOI flag for the 2026 entry travels with the citation inline; the title-disambiguation note for the 2025 entry is carried to frontmatter `known_issues` rather than inlined in the bibliography (CrossRef-confirmed title is used without a hedge marker, with the deferral living one level up).

---

### MOD-006 — Frontmatter bump v1.10 → v1.11

| Field | Value |
|-------|-------|
| Date | 2026-06-09 |
| Type | Metadata update to `CFP_FullPaper_v1.md` frontmatter |

Changes:

- `version: v1.10` → `version: v1.11`
- `date_last_updated: 2026-05-13` → `date_last_updated: 2026-06-09`
- `session_id`: list extended with `SID-20260609-095833`
- `assembly`: appended with `"v1.11 = Earp integration pass (3 paragraph insertions in §3.3, §4 close, §5.4 close + 2 micro-cuts in §3.7, §5.4; net +333 w body — A1 expanded from compressed draft on author review); per CFP_4.2.37."`
- `word_count`: estimate updated to ~9,020 (pending Word recount post-build)
- `known_issues`: extended with two entries:
  - `"Earp, Porsdam Mann, Sawai & Wangmo (2026) — DOI 10.1136/jmepb-2025-000046 flagged for BMJ re-verification (Unpaywall reportedly mis-resolves to Wang & Parent NRP frameworks); confirm before any submission."`
  - `"Earp, Shahvisi & Frith (2025) — title disambiguation deferred: 'Clarifying our editorial approach…' is CrossRef-confirmed; an alternate Google-Scholar-snippet title 'Normalising transparency: an argument for requiring generative AI use declarations in all manuscripts' could not be confirmed as same/distinct piece."`

Build outputs produced post-bump: `Paper/journal/CFP_FullPaper_v1_11.docx` and `.pdf`.

---

## Carry-forward

- **Provenance-problem paper (Earp, Yuan, Koplin & Porsdam Mann 2025, NMI):** the briefing flags this as "the piece JPEP would most want to cite directly" but body access remains blocked (paywalled, no OA mirror). Deferred until library access or alternate route. If accessed, the natural body insertion point is §3 alongside the AUTOGEN paragraph (independent diagnosis of disclosure inadequacy, from an attribution angle).
- **Authorship-Without-Writing preprint (Hurshman, Porsdam Mann, Savulescu & Earp 2025):** held at the editorial-engagement layer per briefing §4.4 — material for cover letters, reviewer responses, post-rejection routing notes; **not** for body text.
- **Two flagged hedges:** DOI re-verification for `JMEPB 2:e000046` and title disambiguation for the JME editorial both live in v1.11 frontmatter `known_issues`. To be resolved before any EthIT submission tag.

---

*Modlog prepared 2026-06-09 in JPEP session SID-20260609-095833. Validation: approved.*
