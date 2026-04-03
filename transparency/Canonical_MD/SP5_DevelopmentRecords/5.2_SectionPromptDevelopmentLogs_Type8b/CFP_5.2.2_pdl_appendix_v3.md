---
artifact_type: pdl
project: JPEP CFP Adaptation
created: 2026-04-01
last_updated: 2026-04-01
status: active
session_id: SID-20260401-111336
output_completed: ""
feeds_into:
  - "CFP_4.4.18_SectionGuidance_AppendixA_v3.md (to be finalised)"
  - "Appendix A v3 draft"
  - "SP-2: Reproduction Package"
  - "SP-3: Reproduction Guide"
source_conversations:
  - session: "SID-20260401-111336"
    exported_as: JPEP_20260401_091152.md
---
# Prompt Development Log (PDL): Appendix A v3 — SP2/SP3 Guidance

**Scope:** Development of the guidance/prompt for Appendix A v3, a revised appendix that (1) verifies whether the story told in v2 is accurately tracked by current SP4 metadata, (2) identifies richer stories the metadata now enables, and (3) is structured to feed SP2 and SP3 directly.

The output of this PDL is `CFP_4.4.18_SectionGuidance_AppendixA_v3.md` (currently a draft produced autonomously by Opus — see PDL-001). That file will be rewritten once the prompt converges.

**Note on CFP_4.4.18 status:** The file at that path is an analytical draft produced by Opus in PDL-001, not yet a user-validated guidance document. It should not be used for drafting until this PDL closes.

---

## Development Entries

### PDL-000: User steering intent

| Field | Value |
|-------|-------|
| Date | 2026-04-01 |
| Session | SID-20260401-111336 |
| Authored by | User (human-directed) |

**The prompt as stated:**

> "Opus has read appendix v2. In previous runs we consolidated the documentation of v1–v2. Now I want opus to design a process to verify whether the story told in appendix v2 is tracked by the metadata in SP4; and I want also to know whether there are more interesting stories to tell. Treat this as a prompt for Appendix v3 (to be recorded as guidance). Appendix v3 is a modified appendix that will feed into SP2 and SP3."

**Three components unpacked:**

1. **Verification task:** Does the SP4 metadata (session IDs, hub files, derived_from chains, feeds_into links, version chains — all built during the CFP phase) actually support the claims made in Appendix v2? v2 was written before this infrastructure existed.

2. **Story discovery:** Given the richer metadata, are there more interesting or more accurate things to say than v2 says? Candidate stories were identified in CFP_5.3.7 (selected graph candidates) and CFP_4.7.8 (self-referential documentation).

3. **SP2/SP3 orientation:** v3 is not just a narrative update — it must be structured so that SP2 (Reproduction Package) and SP3 (Reproduction Guide) can be derived from it. The shift from reproduction model to documentation-adequacy model (CFP adaptation) changes what SP2/SP3 need to say.

---

### PDL-001: Opus autonomous analysis (iteration 1)

| Field | Value |
|-------|-------|
| Date | 2026-04-01 |
| Session | SID-20260401-111336 |
| Produced by | Opus (autonomous — not user-validated) |
| Output file | `CFP_4.4.18_SectionGuidance_AppendixA_v3.md` (draft, not final) |

**What Opus did:** Read appendix v2, CFP work plan, metadata infrastructure note (CFP_5.3.4), selected graph candidates (CFP_5.3.7), self-referential documentation trace (CFP_4.7.8), and one modlog (CFP_4.2.19). Produced a structured analysis covering: (1) nine specific v2 claims flagged for verification; (2) five new stories enabled by the metadata; (3) a proposed SP2/SP3 framing shift; (4) drafting instructions and word targets.

**Issue identified by user:** The output is an analytical note, not guidance in the MHC sense. Guidance should be derived from user-stated intent, not AI autonomous research. CFP_4.4.18 should be rewritten as a formalization of PDL-000, not of PDL-001's analysis.

**Status:** PDL-001 content is retained as analytical input. It may inform later iterations but does not constitute the guidance document.

**Decision:** Continue with feedback to Opus. Iterate until the prompt/guidance reflects user intent with Opus's analysis as substrate, not as author.

---

### PDL-002: User correction — do not demote v1/v2; the figure is substantive

| Field | Value |
|-------|-------|
| Date | 2026-04-01 |
| Session | SID-20260401-111336 |
| Authored by | User (correction to PDL-001 framing) |

**Correction:**

PDL-001 (Opus's analysis) characterised the v1/v2 phase as a "partially-reconstructed" or "honestly limited" record to be contrasted with the stronger CFP-phase record. The user objects to this framing.

**What the v1/v2 record actually is:**

- There was careful, manual editing of all online documentation and produced chains across the v1/v2 phase
- The paper contains a figure (document creation flow diagram) that was carefully curated by the user — it is the canonical visual representation of the writing process
- The figure is at `Canonical_Figures/paper_writing_fig_ground_truth_v2_references.svg` (Inkscape, 1500×2100px, ~130K)
- The figure could not include all nodes (space constraints) but still explains the initial drafts more clearly than any other deliverable produced so far
- The figure covers: all six writing phases, section-specific input combinations, the SP4.7.x epistemic trace chain, the branching structure from 4.7.3 (Path A/B), SP5.1 lifecycle, feed-forward structure, consolidation event, coherence tests, external evaluations, appendix development chain — approximately 80+ distinct labelled nodes/edges

**Design constraint for Appendix v3:**

The v1/v2 record is not an apology — it is a substantive contribution. Appendix v3 must reflect this. The figure is potentially the single best anchor for explaining the v1/v2 phase; v3 should treat it as a primary source, not as a legacy artefact to be superseded.

**New question forwarded to Opus:**

1. Given the figure's richness, what should v3 do with the v1/v2 material — not demote, but how to integrate?
2. Could the metadata be improved to match the figure's level of detail? The figure encodes relationships (node-to-node, phase-to-artifact, input combinations per section) that current SP4 fields (derived_from, feeds_into, session_id) don't fully capture.
3. Is producing a richer metadata description — at the same level of detail as the graph — realistic, cost-effective, and worth doing?
4. If yes: plan for subsequent Haiku agent work on metadata enrichment.

**Status:** Forwarded to Opus. Awaiting response before PDL-003.

---

### PDL-003: Opus response to PDL-002 correction (Q1–Q4)

| Field | Value |
|-------|-------|
| Date | 2026-04-01 |
| Session | SID-20260401-111336 |
| Produced by | Opus (responding to user correction in PDL-002) |

---

#### Q1. How should Appendix v3 treat the v1/v2 material?

**The correction is accepted.** PDL-001's framing — characterising the v1/v2 phase as "partially reconstructed" and "honestly limited" in contrast to the CFP phase — was wrong in emphasis and misleading in implication. The figure (`Canonical_Figures/paper_writing_fig_ground_truth_v2_references.svg`) is not a legacy artefact. It is a primary source — arguably the single most information-dense deliverable about the v1/v2 writing process.

**What the figure actually encodes (verified by reading the SVG):**

The figure is titled "Document Creation Flow: Actual Input Structure" and maps the entire writing process across six phases. Having extracted the XML content, it encodes:

- **Phase 1 (Pre-Writing Foundation):** SP4.7.1 (Epistemic Trace 1, redacted conversation) and SP5.1 (Complete Prompt), with their feed-forward relationship.
- **Phase 2 (Main Writing, Sections I–VI):** Each section box specifies INPUTS, DOCUMENTATION, and FEED-FORWARD separately. The annotation "SP4.7.1 + SP5.1 used throughout" is stated explicitly. Section-specific differences are encoded:
  - Section I: inputs SP4.7.1 + SP5.1; documentation 4.2.1; feed-forward SP4.5.1 (Section Summary).
  - Section II: same base inputs but "NO intro summary | NO pattern summary" (explicitly labelled); documentation 4.2.2; feed-forward SP4.3.1 (First Pattern Summary).
  - Section III: three inputs including SP4.3.1 from Section II; feed-forward SP4.3.2 + SP4.4.2 (guidance for IV).
  - Section IV: five input types including pattern summaries (II, III), ALL section summaries (I, II, III), and SP4.4.2 guidance from III; feed-forward SP4.3.3 + SP4.5.1-4 summaries.
  - Section V: base inputs; feed-forward SP4.5.5 + SP4.4.3 (guidance for VI).
  - Section VI: base inputs marked "[LAST USE!]" for SP5.1; four additional feed-forward inputs (Section 5 Summary, pattern summaries, Section II/III/IV summaries); documentation 4.2.7; feed-forward SP4.5.5 (Section VI Summary).
- **Phase 3 (Further Brainstorming):** SP4.7.2 (Epistemic Trace 2, stakeholder requirements), SP4.7.3 (Methodological Conversation with 8 input types including all pattern summaries + all section summaries + all modification logs), and the branching structure:
  - Path A: 4.7.4 (Artifact Consolidation, based on 4.7.3 outputs) → SP5.2.1 (Prompt Development for VIII) → 4.4.4 (Guidance for Section VIII-A).
  - Path B: SP5.2.2 (Prompt Development for VII) → 4.4.5 (Thick guidance for Section VII, sources integrated) + SP11.1 (Artifact Ontology Expansion) → 4.7.5 (Transparency Value Exploration Part A) → SP5.2.3 → 4.4.6 (Guidance for Section VIII-B).
  - Also: 4.7.6.2 (Discovery of Section Prompt Development Logs and canonical type description production; output = SP5.3.2).
  - Reproduction Package Test (Chapter 1+2) is shown as a separate box.
- **Phase 4 (Later Writing, Sections VII–IX):** Explicitly annotated "NO SP5.1 COMPLETE PROMPT!" Section VII receives SP4.4.5 thick guidance + SP4.5.5 summaries; Section VIII receives SP4.7.1 + SP5.1 + SP4.7.2 plus guidance from VII (SP4.4.4 + SP4.4.6); Section IX receives all section summaries + all pattern summaries + 4.4.6 guidance from VIII; Conclusion receives similar comprehensive inputs. Outputs: First Complete Draft.
- **Phase 5 (Editorial Revision + Appendix Development):** First Complete Draft flows into: Colleague Feedback ("Review Trajectory Not a Clear Test"), SP4.7.7 ("Is this AI Slop?" — ChatGPT identifies style/redundancy problems), SP4.4.8-9 (Avoiding Slop Style), Introduction/IV/VI rewriting (with specific modlog entries: SP4.2.1 MOD-004, SP4.2.4 MOD-002-3, SP4.2.7 MOD-003), SP4.4.10 (Sections II+III+IV → Section 2 consolidation), SP4.4.11 (Trajectory Claims Check, revising claims about reviewing trajectory consistently), and the appendix development chain. Second Complete Draft (minus Appendix) and the Whole Paper Evals (ChatGPT) are shown. Also: Various Coherence Tests 1 and 2, and the complete paper versions (4.7.7.2, 4.7.7.3).
- **Legend:** Comprehensive colour-coding distinguishing epistemic traces, SP5.1 lifecycle ("Phase 2 ONLY"), modification logs ("NOT used as inputs"), summaries/patterns/guidance ("USED AS INPUTS"), section prompt development, and special input combinations. Also distinguishes main guidance/prompt from additional influences (initial prompt context material / mid-conversation additions).

**What this means for v3:**

1. **The figure is a primary source for Section A.2.** It should not be described as "the v2 figure" to be "retained" or "supplemented." It should be treated as the ground-truth reference for how the v1/v2 writing process actually worked. The prose in A.2 should be written *from the figure*, not alongside it.

2. **The figure already encodes much of what my PDL-001 analysis flagged as "needing verification."** The input combinations per section, the SP5.1 lifecycle (Phase 2 only), the branching structure, the feed-forward chain — these are all explicitly labelled in the figure. The v2 prose narrates these, and the figure visualises them. Together they constitute a substantive record, not a partially reconstructed one.

3. **The "two-phase narrative" structure in PDL-001 (Section 3.3) needs revision.** The proposed framing — "v1/v2 phase (retrospective, partial) and CFP phase (prospective, structured)" — implies a clean contrast between a weak record and a strong one. The actual situation is: the v1/v2 phase has a carefully curated visual representation (the figure) plus detailed modification logs plus frontmatter metadata; the CFP phase has structured session-linked metadata plus hub files. They are different documentation strategies, not a progression from weak to strong.

4. **Specific change to PDL-001 Section 4.5 (Tone):** The instruction "Be honest about gaps. The v1/v2 documentation is partly reconstructed. Say so plainly" should be revised. The v1/v2 documentation was not "partly reconstructed" in a pejorative sense. Some session IDs are missing (the `source_chat_id: null` case in 4.2.1); some dates were corrected after the fact (the hallucinated December dates in 4.2.1). But the modification logs are detailed, the figure is comprehensive, and the feed-forward structure is documented. The honest statement is: "The v1/v2 phase used a different documentation strategy — modification logs, section summaries, pattern summaries, and a carefully curated visual representation — rather than the session-linked metadata framework developed in the CFP phase."

**Changes required to PDL-001 nine-claim verification checklist:**

| PDL-001 claim | Revision needed |
|---|---|
| "Figure 2 covers only the v1/v2 writing process. The CFP phase is entirely absent." | **Factually correct but misleadingly framed.** Figure 2 is not incomplete — it is complete for its scope. The CFP phase requires additional representation, not a replacement of Figure 2. Revise to: "Figure 2 is a comprehensive representation of the v1/v2 process. It does not cover the CFP phase, which requires separate representation." |
| "80-110 pages across five packages — Outdated. Recount." | **Still needs updating** but the framing should not imply the original count was careless. |
| Section 3.2 item 3: "The v1/v2 phase has weaker documentation (40 orphaned artifacts, 5 modlogs without SIDs, ghost nodes)." | **Substantially misleading.** "Weaker documentation" implies inferior quality. The v1/v2 phase has detailed modlogs (e.g. 4.2.1 with 13 MOD entries, 4.2.6 with 13 MOD entries), rich frontmatter (source_chat_id, revision_chat_id, dates, process notes, date corrections, version-chain self-reference documentation), and the figure. What it lacks is the *CFP-phase metadata infrastructure* — session IDs on all artifacts, hub files, `derived_from`/`feeds_into` fields in YAML. Revise to: "The v1/v2 phase uses a different documentation architecture — modification logs, feed-forward summaries, and the canonical flow diagram — rather than session-linked metadata. Some artifacts lack session IDs. The two architectures are complementary, not hierarchical." |
| Section 4.7 "Key constraint" — the entire paragraph about "distinguishing between CFP (strong) and v1/v2 (honest about limitations)" | **Needs fundamental rewriting.** The distinction is not strong vs. limited. It is prospective-session-linked vs. retrospective-figure-plus-modlogs. Both are substantive. The key constraint should be: "v3 must not present the CFP-phase documentation as superseding the v1/v2 documentation. They are different strategies for the same purpose. The figure is the primary source for the v1/v2 phase; the hub/metadata infrastructure is the primary source for the CFP phase." |

The other five claims in the verification table (SP-2/SP-3 framing, reproduction workflow, time estimate, trajectory matching, navigation guidance) remain valid and do not require revision based on PDL-002.

---

#### Q2. Could the metadata be improved to match the figure's level of detail?

**Yes, but the figure encodes three categories of information, and the metadata can only realistically capture two of them.**

The figure encodes:

1. **Artifact-level provenance** (which artifact was produced from which inputs, in which chat). This is what the current metadata fields (`session_id`, `source_chat_id`, `derived_from`, `feeds_into`, `output_completed`) already capture — though incompletely for v1/v2 artifacts.

2. **Phase-level structural information** (which artifacts were used in which phase, the SP5.1 lifecycle, the "NO SP5.1!" annotation on Phase 4, the branching point at 4.7.3). This is *not* encoded in current metadata. It would require new fields such as `writing_phase`, `prompt_lifecycle_note`, `branching_point`, or similar.

3. **Input combination specificity per section** (e.g. "Section IV had 5 input types: SP4.7.1, SP5.1, Pattern Summaries II+III, ALL section summaries I+II+III, SP4.4.2 guidance from III"). This is partially captured by `inputs:` lists in some modlog frontmatter, but the specificity varies. Section V's modlog (4.2.6) lists only "4.7.1 epistemic trace" and "4.1 complete prompt" — it does not record that it also received no pattern summaries. The figure encodes both presences and absences; the metadata records only presences.

**What new fields would be needed:**

To match the figure's level of detail, each v1/v2 modlog and section artifact would need:

- `writing_phase:` — one of Phase1/Phase2/Phase3/Phase4/Phase5/Phase6
- `primary_inputs:` — explicit list with artifact IDs (already partially present as `inputs:`)
- `inputs_absent:` — explicit list of what was *not* available (e.g. "no pattern summaries available" for Section II). This is what the figure encodes with "NO intro summary | NO pattern summary" but metadata does not.
- `sp51_used:` — boolean, whether SP5.1 (Complete Prompt) was used as input. The figure tracks this lifecycle carefully.
- `feed_forward_outputs:` — what this section produced for subsequent sections (partially overlaps with `feeds_into` but more specific)
- `branching_structure:` — for Phase 3 artifacts, which path (A or B) they belong to

**Approximate count of artifacts that would need enrichment:**

- v1/v2 modlogs: 11 files (4.2.1 through 4.2.11)
- v1/v2 section summaries: ~7 files
- v1/v2 pattern summaries: ~5 files
- v1/v2 section guidance files: ~7 files
- v1/v2 epistemic traces: ~6 files (4.7.1 through 4.7.6.x)
- v1/v2 section drafts: ~9 files
- v1/v2 PDLs: ~5 files

Total: approximately 50 artifacts requiring metadata enrichment.

---

#### Q3. Is richer metadata realistic, cost-effective, and worth doing?

**Honest assessment: partially worth doing, but the figure already does the hard part.**

**Arguments for enrichment:**

- It would make the metadata machine-readable in ways the figure is not. A script could traverse `writing_phase` and `sp51_used` fields to generate the figure's structure automatically.
- SP-2 (Reproduction Package / Navigation Document) could reference metadata fields directly rather than requiring a reader to consult the figure.
- Future reproduction reviewers could verify claims by querying metadata rather than visually parsing a 1500x2100px SVG.
- It would demonstrate a higher standard of documentation practice — the paper argues for this.

**Arguments against enrichment:**

- **The figure already does this job.** The figure encodes exactly the phase structure, input combinations, SP5.1 lifecycle, and branching paths that the metadata would encode. A reader consulting the figure gets all the structural information that enriched metadata would provide. The metadata would be a machine-readable duplicate of what the figure already communicates visually.
- **Diminishing returns.** The most valuable metadata work has already been done: session IDs on CFP artifacts, hub files, `derived_from`/`feeds_into` chains. Adding `writing_phase` and `inputs_absent` to 50 v1/v2 artifacts fills in detail that the figure already provides.
- **Risk of error.** Enriching 50 artifacts with phase assignments, absent-input lists, and branching paths requires careful cross-referencing against the figure. Errors would be worse than gaps — incorrect metadata that contradicts the figure would undermine credibility.
- **The "inputs_absent" problem.** Recording what was *not* available to a writing session is inherently more error-prone than recording what was. The figure can annotate "NO intro summary" visually; encoding this in metadata requires asserting a negative for every artifact, which is fragile.
- **Opportunity cost.** Time spent enriching v1/v2 metadata is time not spent drafting Appendix v3, rewriting SP-2/SP-3, or completing remaining CFP tasks.

**Recommendation:**

Do a **minimal enrichment** — add `writing_phase` to the 11 v1/v2 modlogs and update incomplete `inputs:` lists where the figure provides clear evidence. Do not attempt to encode `inputs_absent`, branching paths, or SP5.1 lifecycle in metadata. Instead, treat the figure as the authoritative source for those details and reference it explicitly in v3 and SP-2.

Estimated effort for minimal enrichment: 11 modlog files, ~5 minutes each = ~1 hour of Haiku agent work plus ~30 minutes of user review.

Full enrichment (all 50 artifacts, all proposed fields): ~4-6 hours of Haiku work plus ~2 hours of user review. Not recommended given the figure's coverage.

---

#### Q4. Plan for Haiku agent work on metadata enrichment (minimal scope)

**If the minimal enrichment is approved:**

**Task definition:** Add `writing_phase` field and verify/complete `inputs:` lists for the 11 v1/v2 modlogs (4.2.1 through 4.2.11).

**Input materials Haiku would need:**

1. A **template** specifying the exact field names and allowed values:
   - `writing_phase:` — allowed values: `phase1_prewriting`, `phase2_main_writing`, `phase3_brainstorming`, `phase4_later_writing`, `phase5_editorial_appendix`
   - `inputs:` — format: list of artifact IDs with brief descriptions
   - `sp51_used:` — boolean

2. A **reference extract from the figure** — not the SVG itself (Haiku cannot parse 4200 lines of XML), but a structured text summary. This should be prepared before Haiku work begins. It would be a table:

   | Section | Phase | SP5.1 used | Inputs (from figure) | Feed-forward outputs |
   |---------|-------|-----------|---------------------|---------------------|
   | Section I (Intro) | phase2 | yes | SP4.7.1, SP5.1 | SP4.5.1 |
   | Section II | phase2 | yes | SP4.7.1, SP5.1 (no intro summary, no pattern summary) | SP4.3.1 |
   | ... | ... | ... | ... | ... |

3. **Read access to each modlog file** — Haiku reads the file, compares existing frontmatter against the reference table, and adds/corrects fields.

**Sequencing to minimise rework:**

1. *User prepares reference table from the figure* (15-20 minutes). This is the authoritative source; Haiku works from it, not from its own interpretation.
2. *Haiku processes modlogs 4.2.1 through 4.2.11* — one file per task, each task: read file, compare frontmatter to reference table, propose edits. Output: a diff for each file.
3. *User reviews all 11 diffs in one batch* (20-30 minutes).
4. *Approved edits are applied.*

**Risks:**

- **Low risk:** `writing_phase` assignment is unambiguous — the figure assigns each section to a phase. Haiku is unlikely to get this wrong with the reference table.
- **Medium risk:** `inputs:` completion. Haiku might misinterpret figure labels or add inputs that were mid-conversation additions rather than primary inputs. The figure distinguishes "Main Guidance/Prompt" from "Additional Influence (Initial Prompt Context Material/Mid-conversation Additions)" — this distinction should be explained in the template.
- **Mitigation:** Batch review. All 11 files reviewed together, so inconsistencies across files are visible.

**What Haiku should NOT do:**

- Interpret the figure directly from the SVG (too complex, high error risk).
- Add fields beyond `writing_phase`, `inputs:` completion, and `sp51_used`.
- Modify modlog body content (only frontmatter).
- Attempt `inputs_absent` encoding (too error-prone).

---

#### Revision summary for PDL-001 nine claims

| # | PDL-001 claim | Status after PDL-002 |
|---|---|---|
| 1 | SP-2/SP-3 framing obsolete | **Unchanged** — still valid, not affected by the figure correction |
| 2 | Reproduction workflow obsolete | **Unchanged** |
| 3 | Time estimate not meaningful | **Unchanged** |
| 4 | Trajectory matching operationalisation changed | **Unchanged** |
| 5 | Figure 2 covers only v1/v2 | **Reframe**: Figure 2 is complete for its scope, not incomplete. CFP phase needs *additional* representation. |
| 6 | Eleven types still hold | **Unchanged** |
| 7 | File inventories incomplete | **Unchanged** — still true for CFP artifacts |
| 8 | Page count outdated | **Minor reframe**: update needed but original was not careless |
| 9 | Navigation guidance assumes reproduction | **Unchanged** |

Additionally, **three structural claims in PDL-001 need revision:**

- Section 3.2 item 3 ("weaker documentation") — revise to "different documentation architecture"
- Section 4.5 tone instruction ("partly reconstructed") — revise to "different documentation strategy"
- Section 4.7 key constraint (strong vs. limited) — revise to recognise complementary architectures

---

**Status:** Complete. Awaiting user decision on (a) whether the minimal enrichment plan is approved, and (b) whether the reference table should be prepared now or deferred until after v3 structure is settled.

---

## Open

- [x] User decision on Q3/Q4: minimal enrichment approved — further reduced. No `writing_phase` field. Scope = input/output verification only: check `inputs:` and `outputs:` in 11 v1/v2 modlogs against figure, flag inconsistencies. No new fields, no body content.
- [ ] Prepare reference table from figure for Haiku input
- [ ] Convergence: rewrite CFP_4.4.18 from converged guidance (incorporating PDL-002/003 corrections)
- [ ] Reclassify CFP_4.4.18 current content to `5.3_Notes_Type11/` if superseded
- [ ] Close PDL: update status, fill output_completed and source_conversations.exported_as
