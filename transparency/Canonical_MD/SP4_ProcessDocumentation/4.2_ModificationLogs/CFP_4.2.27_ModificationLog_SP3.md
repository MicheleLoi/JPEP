---
project: JPEP
document_type: Type 3 - Modification Log
label: CFP_4.2.27_ModificationLog_SP3
title: "Modification Log: SP-3 v1 → v2 (criterion-spine → phase-spine restructure)"
date_created: 2026-04-07
session_id:
  - SID-20260407-181422
  - SID-20260407-190627
source_conversation: SID-20260407-181422
status: Complete
inputs:
  - CFP_5.4.11_SP3.md (v1, frozen at commit 6a2b844)
  - CFP_4.4.20_SectionGuidance_SP3.md (v7)
  - CFP_4.7.20_EpistemicTrace_Section6History.md
  - CFP_5.3.19_Note_SP3_FigureDataSpecs.md
  - Paper/MDversion/appendix.md (v2 appendix — structural model)
output_completed:
  - CFP_5.4.11_SP3.md (v2)
related:
  - CFP_5.2.4_pdl_SP1_SP2_SP3.md (PDL-024, PDL-025)
---

# Modification Log: SP-3 v1 → v2

## Context

SP-3 v1 (~5500 words, criterion-spine: §1 frame, §2 orientation, §3 evidence, then three big sections keyed to Attribution / Trajectory / Understanding-and-Endorsement, with Section 6 woven through as illustration) was the first draft produced under the PDL-024 draft-first refine workflow. On reading, the user identified that the Section 6 worked-example material started too early — by §3.2 the reader was being asked to grasp specific artifact IDs and stage details before having a mental model of the project's three writing phases. The first refine pass therefore became a structural rewrite, not surface revision. This is itself a finding about the draft-first workflow and is recorded in PDL-025.

## Changes

### MOD-001: Restructure — criterion-spine → phase-spine

**What:** Replaced the v1 criterion-spine (three big sections keyed to Section 7's three criteria) with a four-movement phase-spine adapted from the v2 paper appendix (`Paper/MDversion/appendix.md`):

- **Part I — How the paper was written** (§§1–3 + Figure 1 timeline). Reader meets the project at a glance, then the three writing phases (v1/v2 Claude.ai web Sonnet 4.5, Stage III Claude Code Opus 4.5/Sonnet 4.6, CFP Claude Code Sonnet/Opus 4.6) in broad strokes before any artifact ID is named.
- **Part II — What documentation was produced** (§4, three subsections by phase). The artifact ontology presented phase by phase, so the reader sees what each phase could record and what it couldn't.
- **Part III — Capabilities, challenges, solutions** (§5, three subsections by phase). Each phase gets a capability / challenges / solutions triple, exposing the dependency between technological regime and documentation possibility.
- **Part IV — Section 6 as worked example** (§§6–12 + Figures 2, 4, 5, 6). Section 6 demoted from spine to worked example, entered only after the reader has the phases, the artifacts, and the capabilities in hand. The five-stage history, the mapping to Section 7's criteria, the two scoped gaps, the two-evidence-source defense, and the synthesis of the human author's role across phases all live here.

The Section 7 criteria are no longer the spine — they appear in §8 as a mapping table over the worked example, which is where the user should perform the adequacy assessment.

**Why:** v1 made the reader hold the criteria in mind from the opening and then meet Section 6 details (Stage 3b's lost Jan 28 draft, the model switch, MOD-009) at a point where the project's phase structure was not yet clear. The v2 paper appendix had solved the same problem with a phase-spine: tell the story first, then point at it. Adopting the appendix's structural shape gave SP-3 the same affordance.

**Net change:** ~5500 → ~4500 words. The compression is real, not cosmetic: the criterion-spine forced repetition (each criterion section had to re-introduce the same Section 6 stages), which the worked-example structure absorbs into a single chronological pass.

**Where the v1 material went:**
- v1 §3.2 dual-source defense → §11 (where the asymmetry between phases is the actual point)
- v1 attribution / trajectory / understanding-and-endorsement narratives → §8 mapping table + §12 synthesis
- v1 Section 6 fragments scattered across three criterion sections → §7 single five-stage walkthrough
- v1 §1 framing → §1 unchanged (still names what the document is and grounds in Section 7)

### MOD-002: §3.2 dual-source defense rewritten and relocated

**What:** v1 §3.2 made the dual-source claim (artifacts + conversations) and then defended why v1/v2 phase conversations are not in the GitHub repo. Three iterative passes during v1 refinement landed on "cloud-hosted on Claude.ai/ChatGPT, accessible to the author via shareable links." In v2 the defense was rewritten into §11, where it sits alongside the two scoped Section 6 gaps and the project-level gaps — i.e. in the place SP-3 actually inventories what the record can and cannot show.

**Why:** in v1 the defense appeared as a methodology footnote attached to a structural claim the reader hadn't yet been given motivation to scrutinize. In v2 the reader has finished Part IV's worked example and is primed to ask exactly the question the defense answers.

### MOD-003: In-session factual corrections and framing refinements to v2

During the same post-compaction session (`SID-20260407-190627`) that recorded MOD-001 and MOD-002, the user read v2 and flagged a series of claims that required correction. The file was edited in place.

**Factual corrections:**

1. The 2026-04-05 custom-type formalization does *not* promote v1/v2 habits — v1/v2 had section guidance and pattern summaries as one-off files with no `version:` field, and no section-draft artifact at all. Versioned section drafts are a CFP-era invention. §3.2, §4.1, §4.3 rewritten accordingly. The verbose adapt.md-internal account was later trimmed to a single sentence at the user's request.
2. Pattern summaries were not "authored by hand from completed modlog material." The actual v1/v2 mechanism was a per-chat workflow (each section in a fresh chat) with two deliberate handoff artifacts between chats: a section content summary and a Claude-distilled *MOD summary* intended as operational guidance for the next chat's fresh AI instance. The category was renamed *pattern summary* only in the Section VIII (6) consolidation step; earlier files were retrospectively edited to conform. §4.1 bullet and §5.1 Solutions rewritten. Evidence: chat `4177422b-27c3-44d4-a52e-f065de4e72ab` ("JPEP section 2 writing", 2025-10-12, Sonnet 4.5) — the earliest preserved instance of the handoff artifact is titled *MOD-19-20-SUMMARY: Methodological Guidance for Next AI*, opening "Purpose: Operational lessons from Chat 2 for Chat 3's AI to apply" — i.e. authored under the per-chat operational-handoff framing, not under the later "pattern summary" category name.
3. `4.1`'s provenance is human-sourced via `5.3.21` → `da6a830c` → origin chat `6c8d9101`, Claude-synthesized inside `2ca5888a`, human-endorsed. §4.1 updated with the full provenance chain and references to `CFP_4.7.16` / `CFP_5.3.15`.
4. The claim that the Jan 28 Section 6 failure "prompted the model switch to Sonnet 4.6" was unwarranted causal inference from pure correlation. §5.2 Challenges cut from two to one (the second challenge removed entirely).
5. Stage 2 (Nov 5–6) did not surface "infrastructure constraints" — it surfaced a *conceptualization problem* about the process that had led to Section 6. §7 Stage 2 rewritten.

**Framing refinements:**

- Drafts are transforming artifacts, not SP-4/SP-5 evidence objects; the Jan 28 lost draft was over-featured throughout. De-emphasized across §3.2, §7 Stage 3, Figure 5 caption, §9, §10, and §6 (the fourth reason for choosing Section 6 — "exactly one ghost" — was removed; the list is now three reasons).
- §10 restructured: leads with a scope note ("the project tracks the writing process, not every textual artifact") before naming the two scoped items that remain.
- §5.2 Solution replaced twice. Initial version ("SP reconception generated the requirements") was judged exaggerated and off-topic for the tooling-parallelism challenge. Final version: retrospective CFP consolidation via `CFP_4.2.26` frontmatter normalization, made possible because MHC-W was already exporting Claude Code conversations out of the ephemeral system folder into the persistent repo — Stage III is the middle phase whose inconsistencies were cleaned up by CFP.
- §5.3 "second challenge" about automation hiding infrastructure failures cut as off-topic (the problem is considered solved).
- Reproduction-test term glossed on first use in §3.2 (the reader had been meeting it cold).

**Structural additions:**

- The "`4.1` anticipates the ontology; it crystallized by end of v1" claim was added to three places (§3.1, §4.1, §5.1) and then consolidated into §5.1 alone, with §3.1 carrying a one-line forward pointer. One canonical home.
- §3.1 gained a paragraph on v1 → v2 as a documentation-layer consolidation: v1 was posted to arXiv before the transparency material had been audited; v2 changed only the appendix (the part that corresponds to SP-2) to conform to the audited state of the artifacts. The paper proper was unchanged.

**Density / polish:**

- §4.1 bullets gained eight canonical / type-defining artifact IDs (`4.2.9` incl. MOD-009, `4.7.3`, `4.7.5`, `4.4.13`, `4.3.1`–`4.3.5`, `5.2.1` as "the PDL that documents the development of `4.1` itself", `5.2.2`, `5.3.1` as the note in which the ontology adds a category to itself).
- Adapt.md-internal detail about the 2026-04-05 Adaptation Log entries trimmed to one sentence.

**Why these are one entry.** Counted separately they are roughly fifteen edits; treated as a single modlog entry because they are the first refine pass applied to v2 by the same draft-first workflow that PDL-024 specifies, and they all came from one continuous read-through by the user in the same session.

## Validation

approved

---

*Modlog records the v1 → v2 restructure executed in session SID-20260407-181422 and logged in the post-compaction session SID-20260407-190627. v1 frozen at commit 6a2b844 and recoverable via `git show 6a2b844:transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/CFP_5.4.11_SP3.md`. v2 lives at the same path under the post-2026-04-07 single-file versioning convention.*
