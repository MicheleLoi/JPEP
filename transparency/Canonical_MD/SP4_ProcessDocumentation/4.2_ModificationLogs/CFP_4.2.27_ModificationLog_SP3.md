---
project: JPEP
document_type: Type 3 - Modification Log
label: CFP_4.2.27_ModificationLog_SP3
title: "Modification Log: SP-3 v1 → v2 (criterion-spine → phase-spine restructure)"
date_created: 2026-04-07
session_id:
  - SID-20260407-181422
  - SID-20260407-190627
  - SID-20260408-122758
  - SID-20260409-132703
  - SID-20260409-145640
source_conversation: SID-20260407-181422
status: Complete
inputs:
  - CFP_5.4.11_SP3.md (v1, frozen at commit 6a2b844)
  - CFP_4.4.20_SectionGuidance_SP3.md (v7)
  - CFP_4.7.20_EpistemicTrace_Section6History.md
  - CFP_5.3.19_Note_SP3_FigureDataSpecs.md
  - Paper/MDversion/appendix.md (v2 appendix — structural model)
output_completed:
  - CFP_5.4.11_SP3.md (v3 — figure callouts revised per MOD-006)
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

### MOD-004: Conversations-as-source-material policy — five-touch revision pass on v2

Session `SID-20260408-122758`. The user and Claude discussed where `06_conversations/` should live (gitignored vs. SP4/5/6 vs. quarantined-but-tracked) and confirmed that the directory is *already* gitignored, with one tracked exception (the anonymized founding conversation `Claude_JPEP_idea_origination_(real_world_journal).md`) and one explicitly excluded item (the unanonymized ur-conversation `6c8d9101`). The remaining decision was therefore not *whether* to gitignore but *how SP-3 should describe the arrangement and what claim it should make on top of it*. The user drew a sharp distinction the previous v2 §11 had blurred: dual-source reading was a *philological method* used during the early-April 2026 reconstruction, not a *standing claim* about what SP-4/SP-5 offers a reader. SP-3's actual offering is an artifact-layer account organized around meaningful human control — explicitly not an auditability claim. The reasons for the negative claim live in Sections 3 and 6 of the paper proper and are not relitigated in SP-3. A future-end work-plan reminder was added (`CFP_5.3.1` "Remaining work" list) to create a tracked SP-5 manifest of `06_conversations/` (`document_type: manifest`, one-off value, no adapt.md subtype-table inflation) before final commit. The five SP-3 touches below were then executed in one pass.

**Five edits, one decision:**

1. **§3.3 (CFP capability list)** — struck "full conversation file-exports for every session into `06_conversations/`" and replaced with "a SessionEnd hook that captures every Claude Code session as a conversation file into a local-only `06_conversations/` directory indexed by a public manifest in SP-5 (see §11)." The capability described is now what is actually true under the policy.
2. **§4.1 (v1/v2 negative list)** — removed "inside the public repository" from the list of things v1/v2 did not produce. Replaced "conversation file-exports inside the public repository" with "session-by-session conversation file-exports." The distinction between v1/v2 and CFP at this point in the document is now about *whether session-level exports happened at all*, not about *whether they are public*.
3. **§4.3 (CFP artifact section)** — rewrote the "Full conversation file-exports..." paragraph to state the actual arrangement: SessionEnd hook captures exports; the directory is gitignored; conversations are retained as source material on the author's machine and indexed by a public manifest in SP-5; the v1/v2 platform-hosted situation is a parenthetical, not the centerpiece; the principle is deferred to §11.
4. **§10 (scope note)** — expanded the "two places worth naming" inventory to include the standing fact that `06_conversations/` is gitignored in its entirety. Now lists the model-switch deliberation, Chat 1, the unanonymized origin chat `6c8d9101`, *and* the directory-level policy, framed as "not a defect" — the manifest is the public anchor; the criterion is good-faith adequacy, not tamper-resistance.
5. **§11 — full restructure (largest change).** Section title changed from "Two evidence sources, and an asymmetry between phases" to **"What SP-4/SP-5 offers, and what it does not."** The phase-asymmetry framing is gone — under the new policy the asymmetry has largely dissolved (neither v1/v2 nor CFP conversations live in the public repo, just by different mechanisms). Four paragraphs:
   - **¶1 — Dual-source reconstruction was the historical method, not the standing claim.** Past tense. Names the philological work explicitly (`CFP_5.3.18`, `CFP_4.7.20`, `CFP_4.7.16`, `CFP_5.3.15`) and keeps the concrete examples (mislaid SID, `4.1` provenance) that show why neither layer alone was sufficient *for that recovery work*. Closes with "this was the method by which the artifact chain was *recovered*. It is not what the SP-4/SP-5 set offers a reader."
   - **¶2 — What SP-4/SP-5 offers.** The standing claim, in present tense, framed against the three Section 7 criteria (attribution / trajectory / understanding-and-endorsement) with a forward pointer to §8's mapping table and Part IV's worked example.
   - **¶3 — Explicitly not an auditability claim.** Names the negative claim outright (no reproduction, no prompt-by-prompt replay, no full transcript publication) and refuses to defend it on the spot, pointing instead to Sections 3 and 6 of the paper proper where the reproduction-test rejection and the meaningful-human-control reframe live.
   - **¶4 — What is not in the public package and how it could be had.** CFP exports local-only; v1/v2 conversations on host platforms; SP-5 manifest as the public index; available on request. Closes with the principle: "meaningful human control does not require full conversation publication, and SP-3 does not pretend to offer what it does not need to offer."

**Why these are one entry.** Each touch is small in isolation (a strike, a phrase, two new sentences, a paragraph rewrite, a section restructure). They are one decision because they all flow from a single reframing the user articulated mid-discussion: *dual source belongs to the past tense of philological reconstruction; SP-3's standing claim is a meaningful-human-control claim built on the artifact layer; the manifest indexes the source material that supported the reconstruction without pretending the source material is the offering*. None of the edits would be coherent without the others; together they make SP-3 stop conflating the reconstruction method with the publication offering.

**Forward reference.** §11 references the SP-5 manifest as if it exists. It does not exist yet. The work-plan reminder (`CFP_5.3.1`, Remaining work, dated 2026-04-08, SID-20260408-122758) commits to creating it before final commit. The user and Claude considered marking the SP-3 reference with a draft-stage placeholder and decided against it: SP-3 itself is a draft, internal readers know the manifest is on the work plan, and TODO markers in draft prose tend to leak into final.

**Out of scope for this entry.** Figure integration is the next session's work and is unrelated to the policy revision.

### MOD-005: §5.3 challenge reframed, §10/§11 merged, §11 synthesis corrected

Same session as MOD-004 (`SID-20260408-122758`), continuing the read-through of v2. Four substantive changes, all flowing from user corrections to claims that survived the v1 → v2 restructure intact but were wrong on closer reading.

**§5.3 — Challenges and Solutions rewritten.** The user flagged that the redundancy paragraph misclassifies its subject: modular section-by-section writing is the v1/v2 per-chat workflow, not a CFP innovation, and `CFP_4.2.22` (the cross-paper redundancy reduction) documents the phenomenon as a property of the modular workflow used across phases rather than a CFP-specific challenge. With MOD-003 having already cut the second CFP challenge ("automation hiding infrastructure failures"), removing redundancy left §5.3 with no challenge — a real structural choice, not a copy-edit. Claude's first attempt to find a replacement (a "reflexivity / standing-inside-the-system" framing built around PDL-024 → PDL-025) was rejected by the user as "complete bullshit" on the grounds that reflexivity was *stronger* in v1/v2 (the documentation ontology emerged from use), so it cannot be CFP-specific. The user then specified the actual CFP-specific challenge: the same Claude Code + Max-subscription affordances that let a single session hold dozens of artifacts and run dozens of operations in parallel produce a session record that is *complete and illegible* — every step captured, none of it readable end-to-end by a human. The trace becomes opaque by excess transparency. The user named the solution as well: borrow scope discipline from v1/v2 — operate, where possible, with the constrained per-chat workflow even when the tooling no longer requires it. Final §5.3 names the challenge "opacity by excess transparency", explains why it is CFP-specific (v1/v2 platform constraints enforced an upper bound on session complexity that doubled as a legibility floor; CFP removed the constraint and lost the floor), and cites the CFP-era chain walks (`CFP_5.3.18`, `CFP_4.7.20`) as evidence the project had to invest in *re-reading* its own captured record. The Solutions paragraph names the discipline as a regulative ideal (one unit of intent per session, sized so a modlog entry remains readable in one sitting), with `CFP_4.2.18` as the positive instance, and `CFP_4.2.22` + `CFP_4.2.26` reframed as *partial recovery passes* for sessions in which the discipline was not held. The solution is explicitly partial: the discipline has to be re-elected every session, and the recovery passes exist for sessions where it was not.

**§10 — model-switch sentence deleted.** The user flagged the sentence "the deliberation behind the model switch from Opus 4.5 to Sonnet 4.6 ... was not exported as a separate chat ..." as an insignificant detail. Already noted in MOD-003 as a recurring correlation-for-causation error around the model switch; this removes the last residue of it from §10.

**§10 + §11 merged and halved.** The user asked to combine the two sections and cut by 50%. Result: a single §10 titled "What SP-4/SP-5 offers, and what it does not", roughly 410 words (down from ~800 combined). Three-paragraph structure: scope-and-policy (drafts as git's job, two scoped chat items, gitignore policy with manifest); dual-source as past-tense reconstruction method (chain walk anchors retained, illustrative examples compressed); standing claim (artifact-layer account against the three Section 7 criteria, explicit non-auditability with the negative claim refused defense and pointed to Sections 3 and 6 of the paper proper, manifest as public anchor / artifact chain as spine / conversations as source material). §12 (Synthesis) renumbered to §11. Two forward references in §3.3 and §4.3 updated from "see §11" to "see §10".

**§11 (Synthesis) — v1/v2 and Stage III paragraphs corrected; closing paragraph deleted.** The user flagged the Stage III paragraph as "completely wrong" on two counts: (a) the model-switch judgment is correlation-for-causation again, immaterial to the actual story; (b) "philologist of the author's own writing" is a great line but does not belong to Stage III — it belongs to v2. The user supplied the correct Stage III story: external human input (conversations with a colleague, feedback from presenting v2 at a workshop) was carried back into the project and implemented with AI in concentrated bursts. Final form: the v1/v2 paragraph keeps "prompt author and ontology inventor" as primary and gains a closing sentence locating *philologist of the author's own writing* in the v1 → v2 consolidation pass (re-reading v1's documentation against the audited state of the artifacts, revising the appendix layer to conform). The Stage III paragraph is fully rewritten with the role label *translator of off-page human input into the manuscript*; the March 2 Section 6 redraft is named as the largest documented instance of external dialogue being absorbed, translated, and committed in one session; the methodological reorganization in the same session is reframed as a consequence of the same absorption (off-page dialogue surfaced what the documentation needed to do; the SP reconception followed). The CFP paragraph is unchanged. The closing paragraph that began *"The role that runs through every phase is the role that §6.3 of the paper identifies: the practitioner whose practice produces its own requirements ..."* was deleted at user request as too repetitive (the §6.3 connection is already carried by Part IV's worked example and by the next paragraph's Section 3 connection).

**Why these are one entry.** Four edits, one continuous read-through of v2 by the user against the conversations-policy revision pass that produced MOD-004. They are bundled because the read-through was a single intent (correct everything that survived the v1 → v2 restructure but was wrong on its merits), and because three of the four corrections fix recurring failure modes already named in MOD-003: correlation-for-causation around the model switch, mislocated phase-attribution of phenomena that span phases, and over-featuring of insignificant gaps in §10.

### MOD-006: Figure integration — fig2/4/5 dropped, network added as Figure 2, captions embedded

Session `SID-20260409-132703`. Commits: `9c25cb7` (figure callout revisions), `c2ba911` (captions).

**Background.** After the graph infrastructure overhaul (`CFP_4.2.28`, sessions SID-20260408-145906 and SID-20260408-191811), the project had three SVG figures: `fig1_timeline.svg`, `fig6_swimlanes.svg`, and `fig_section6_network.svg`. SP-3 v2 still referenced five figures — fig1, fig2 (feedback loop), fig4 (three-draft session), fig5 (visible decision), and fig6 (swimlanes) — inherited from the CFP_5.3.19 figure spec. fig2, fig4, and fig5 had no corresponding SVG files.

**Diagnosis.** Session topology for SID-20260408-145906 (`artifacts_produced` list) showed only the three canonical figure scripts registered; `CFP_4.2.28` MOD-010 confirmed those three were converted to SVG-only while fig2/4/5 were not included in that conversion scope. No subsequent session built or converted them. The reason is structural: the session that produced fig2/4/5 scripts had a different, pre-specified goal (fig1 + fig6 + fig_section6_network + HTML bonus); fig2/4/5 were written as informal extras and never entered the artifact chain.

**Decision: drop fig2/4/5.** Prose in SP-3 §7 covers the content of all three in full — the feedback-loop structure, the three-draft session, and the visible-decision example are named and explained in the running text. The figures were illustrative, not load-bearing. Decision recorded in `CFP_4.2.28` MOD-011.

**SP-3 changes (first commit, 9c25cb7):**

1. **Part IV figure numbering revised.** The three remaining figures renumbered: `fig1_timeline.svg` stays as Figure 1; `fig_section6_network.svg` becomes Figure 2 (promoted from the former "bonus" §10 slot); `fig6_swimlanes.svg` becomes Figure 3.
2. **[FIGURE 2], [FIGURE 4], [FIGURE 5] callouts removed.** Three inline callouts deleted from Part IV body text. Associated placeholder prose ("see Figure X") removed or absorbed into surrounding sentences where needed.
3. **fig_section6_network relocated to Part IV.** The network figure placed as Figure 2 immediately after §7 (Stage 5 / the five-stage walkthrough), where it functions as the visual synthesis of the Section 6 history just recounted. Previously it sat only in §10 as a bonus; in that position the figure arrived after the reader had left the worked example. The §10 bonus paragraph trimmed to HTML interactive graphs only.
4. **fig6_swimlanes retained as Figure 3 in §9.** Position unchanged; callout updated from `[FIGURE 6]` to `[FIGURE 3]`.

**SP-3 changes (second commit, c2ba911):**

5. **Figure captions embedded.** Each figure callout followed by an italic caption line drawn directly from the corresponding Python script's `caption` variable. This is to make Word integration easier: SVG files do not carry extractable text, so the caption must be present in the MD. The three captions:
   - *Figure 1.* From `fig1_timeline.py`: the project timeline, five stages, three phases, two platforms, four model identities, major structural events.
   - *Figure 2.* From `fig_section6_network.py`: four-hub chain from PreliminaryChat 1 (2025-10-12) through two methodology sessions (2025-10-13, 2025-10-15) into the Section 6/VIII writing session (2025-10-18); lower-rail version chain; bridge artifacts 4.4.4 and 4.4.5; SUN4 cross-paper scope.
   - *Figure 3.* From `fig6_swimlanes.py`: swimlane view of where Section 6 sits across stages and phases.

**Why these are one entry.** Both commits serve the same intent — integrate the three final SVGs into SP-3 coherently — and the caption commit is a direct follow-on to the callout commit. The decision about fig2/4/5 is recorded separately in `CFP_4.2.28` MOD-011 because it pertains to the graph infrastructure record, not to SP-3 prose structure.

### MOD-007: §11 CFP synthesis — expert-delegated approval case added (SID-20260410-002246)

**Change:** Four sentences added to the CFP paragraph in §11 (Synthesis — the human author's role), after the redundancy-pass sentence. Describes the Sartre passage revision as a case where the human role approximated expert-delegated approval rather than understanding-grounded endorsement; frames it as a recognizable mode of collaborative scholarship; records that the author's reflection generated an independently developed observation about the tracing condition's internal ambiguity; points to the Conclusion for the theoretical implication.

**Why:** The §11 CFP synthesis described the phase role uniformly as "editor in dialogue with a second reader." The Sartre case is a different shade: the author followed Opus's philosophical lead on execution while independently developing the meta-level theoretical observation about what that deferral reveals. SP-3 is the right place to record the empirical instance; the Conclusion carries the theoretical payoff. The addition keeps the synthesis honest about the variation in the depth of understanding across the CFP phase, and connects the local instance to the paper's broader argument about the tracing condition.

**Affected text:** SP-3 §11, CFP paragraph.

---

## Validation

approved

---

*Modlog records the v1 → v2 restructure executed in session SID-20260407-181422, logged in post-compaction session SID-20260407-190627; the conversations-as-source-material policy revision pass executed in session SID-20260408-122758; and the figure integration pass executed in session SID-20260409-132703. v1 frozen at commit 6a2b844 and recoverable via `git show 6a2b844:transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/CFP_5.4.11_SP3.md`. v2 at commit 57fb483. v3 lives at the same path under the single-file versioning convention; substantive intra-version revisions tracked as MOD-NNN entries here.*
