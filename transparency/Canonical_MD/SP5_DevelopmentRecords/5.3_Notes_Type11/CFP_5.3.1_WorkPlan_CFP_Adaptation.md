---
project: JPEP
document_type: Type 11 - Steering Note / Work Plan
label: CFP_5.3.1_WorkPlan_CFP_Adaptation
title: "Work Plan: CFP Adaptation for AI Tools in Ethics Research"
branch: cfp-ai-ethics-inquiry
date_created: 2026-03-02
status: Active
source: "Claude Code / Claude Opus 4.6 (analytical session) + user direction"
related:
  - "III_4.7.4_CFP_AIEthicsInquiry_BranchAndFitAnalysis.md (fit analysis)"
  - "III_5.4.1_Section3_v3.md (authoritative Section 3 draft)"
  - "III_5.4.2_Section6_v3.md (authoritative Section 6 draft)"
  - "target-venue/cfp_ai-ethics-inquiry.md (CFP text)"
  - "III_5.3.5_SteeringNote_v3_Section_Revisions.md (prior steering note)"
---
# Work Plan: CFP Adaptation for AI Tools in Ethics Research

---

## RESUME HERE (last updated 2026-06-13, after the v1.11→v1.16 cycle + EthIT submission prep — paper at v1.16 on `main`)

**Quick state.** Paper: `Paper/MDversion/CFP_FullPaper_v1.md` at **v1.16**. Submitted to *Philosophy & Technology* at v1.10 (14 May 2026); **desk-rejected 2 June 2026** by Floridi (EiC-level "Reject — transfer options available", not a quality verdict). **Next venue: Ethics and Information Technology** (Springer, **double-blind**) — van den Hoven (EiC) co-authored the Santoni de Sio & van den Hoven 2018 paper §6 builds on, so recusal is expected and a Co-Editor handles. Title + abstract held unchanged (author declined the AI-proposed wink-removal, on §3 agent-integrity grounds). Branch `cfp-ai-ethics-inquiry` **merged to `main`** (2026-06-09, `f828fe9`); all work since is on `main`.

Since v1.10: **Earp-cluster integration** (v1.11 AUTOGEN/DA/JME; v1.13 in-text §5.4 + author-position registration in the Archive, full defence reserved for a JMEPB commentary), **Archive testimonial layer** + 12 scoped AI-voice markers (v1.12, after an adversarial-verification pass rejected a fuller "AI-voice edition"), a **14-cut compression pass**, and a **reference audit (v1.14→v1.16)** that cut the unverified bias-mitigation apparatus, verified every empirical claim against source PDFs, and caught + fixed a fabricated Abdulhai co-author list. **Reference reliability: closed for submission.** Build engine switched to **pandoc** (native footnotes). Distribution editions derive from the canonical via `derive_distributions.py`: `Full_paper_arxiv_v4.md` (public; arXiv 2511.08639) and `Full_paper_submission_anon.md` (verified zero identity leak). See `CFP_session_log.md` SID-20260609-095833 (+ its 2026-06-10/11 continuation) for the full arc; `CFP_4.2.38` / `CFP_4.2.39` for per-change detail.

**Next action — actual EthIT submission (not yet done):**

- Complete the EthIT submission form incl. the AI-use declaration field; upload the **anon PDF** (`Full_paper_submission_anon.pdf`) + **cover letter** (`target-venue/cover_letter_ethit.md`); upload **arXiv v4** to update 2511.08639.
- **Confirm cover-letter seminar tense** before sending — "was presented" assumes the Jan-2026 TU/e Santoni de Sio seminar has occurred; flip to "is scheduled to be presented" if still upcoming.
- Earp DA + SHC are forthcoming preprints — re-check their final DOIs at/after publication.
- **Zenodo DOI** deferred to the final-accepted version (mint at the submission/acceptance tag; insert into `CFP_5.4.14` and SP-1).
- Decide whether to git-track `build_paper.py` + `derive_distributions.py` for reproducibility (currently gitignored; the pandoc/footnote fix lives only locally).

**This section is the canonical entry point for resuming JPEP work.** Per-session granular history is in `CFP_session_log.md` (same folder); this section summarises state and points forward. Older parked polish items (Opus §6/§7 compression, §3 eval) were absorbed by the v1.12 compression pass and the v1.14→v1.16 audit; the detailed history below is preserved as the original plan.

**Paper body status (post-2026-04-09 numbering, post-2026-05-12 externalization):**

| § | Title | File | Status |
|---|---|---|---|
| 1 | Introduction | `CFP_5.4.3_Introduction_v2.md` | Done; SP-claim externalised |
| 2 | Systemic Barriers to Disclosure | `CFP_5.4.5_Section2_v4.md` | Done |
| 3 | Why Engage with AI-Assisted Scholarship? | `CFP_5.4.4_Section3_v3.md` (frontmatter v5) | Done — Cordasco objection-response (v4) + reproducibility disanalogy / agent-integrity grounding (v5) added 2026-05-12. See `CFP_4.7.21` (trace), `CFP_4.2.23` (modlog), `CFP_4.4.22` (section guidance), `CFP_5.3.29` (Cordasco briefing) |
| 4 | Conditions for Adequate Transparency | `CFP_5.4.7_Section5_v2.md` | Done (good-faith extension 2026-04-10) |
| 5 | Mandatory Transparency in Practice | `CFP_5.4.8_Section6_v4.md` | Done; SP-claim externalised |
| 6 | Community Assessment of Documentation Adequacy | `CFP_5.4.9_Section7_v3.md` | Done; Abdulhai hedge + SP-claim externalised |
| 7 | Conclusion | `CFP_5.4.10_Conclusion_v1.md` | Done; opening recast 2026-05-12 |
| — | AI Usage and Documentation Archive (unnumbered closing note) | `CFP_5.4.14_AIUsageArchive.md` | v1, 2026-05-12 |

**SP-1/SP-2/SP-3 externalization (2026-05-12):** SP-1, SP-2, SP-3 no longer appear in the paper body. They live in a documentation archive (Zenodo or equivalent, DOI pending) alongside the SP-4 and SP-5 folders. The closing note introduces the archive; the §5 SP-1–SP-5 framework table and §6 assessment description remain framework-level. PDL: `CFP_5.2.5_pdl_AIUsageArchive.md`. Per-section to-dos with exact before/after text: `CFP_4.4.21_SectionGuidance_ExternalizationImplementation.md`.

Archive contents on disk:

- SP-1: `transparency/Canonical_MD/SP1_AIUsageDeclaration/CFP_5.4.13_SP1.md` (v1)
- SP-2: `transparency/Canonical_MD/SP2_NavigationAndArchitecture/CFP_5.4.12_SP2.md` (v1, inventory refreshed 2026-05-12; final enumeration check 2026-05-13)
- SP-3: `transparency/Canonical_MD/SP3_DocumentationAdequacy/CFP_5.4.11_SP3.md` (v3)
- SP-4 folder: `transparency/Canonical_MD/SP4_ProcessDocumentation/`
- SP-5 folder: `transparency/Canonical_MD/SP5_DevelopmentRecords/`

**Note (2026-05-13, SID-20260513-003000, commit `e317eac`):** SP-1, SP-2, SP-3 moved from `5.4_SectionDrafts/` to top-level sibling folders of `SP4_*` and `SP5_*` under `transparency/Canonical_MD/`. Filenames preserved (pure `git mv`); use `git log --follow` to traverse history across the rename. Files retain `document_type: Type 12 - Section Draft` for now — relabelling deferred (out of scope of the move commit).

**Note (2026-05-13, SID-20260513-094035):** Pipeline relocation. The hub-system pipeline (`transparency/SCRIPTS/` contents, `transparency/Canonical_MD/_HUBS/` directory, and the HTML/PNG outputs in `transparency/Canonical_MD/_GRAPHS/`) was moved out of `transparency/` into a top-level `_pipeline/` folder (gitignored — does not ship). The three SVG figures referenced in SP-3 narrative (`fig1_timeline.svg`, `fig_section6_network.svg`, `fig6_swimlanes.svg`) remain in `transparency/Canonical_MD/_GRAPHS/` as part of the shipped archive. The decision and the deferred plan for bringing hubs + interactive graphs to publication-quality state are documented in `_pipeline/README.md` and `_pipeline/HUBS_AND_GRAPHS_PLAN.md`. Cross-references in shipped documents (SP-1, SP-2, this work plan) updated to acknowledge the freeze; historical modlogs and traces describing past pipeline states are intentionally left as-is.

**§3 Cordasco + reproducibility-disanalogy / agent-integrity grounding — RESOLVED 2026-05-12 (SID-20260512-154043).** Two changes treated as one philosophical movement clarifying what kind of argument JPEP's transparency duty is.

- **v4:** Three-paragraph engagement with Cordasco's welfare-economic objection added after the Williams paragraph: steelmanned objection, welfare-on-welfare reply (metacognitive monitoring + generative framework), register reply (moral duty does not reduce to welfare calculation). Moral-vs-post-institutional distinction made load-bearing.
- **v5:** New subsection "Reproducibility Is Not the Issue" added between cognitivist defeat and tracking pivot. Explicit disanalogy with science's reproducibility model; explicit grounding of the transparency duty in agent-integrity rather than methodological-integrity-as-reproducibility. Cavell added to exemplar list; Lewis explicitly excluded as instrumental methodology.

§3 v5 word count ~2,470. Three negative results closed off (not welfare-economic, not methodological-soundness, not reproducibility-style) + one positive grounding (agent-integrity, Williams). See trace `CFP_4.7.21` for philosophical development, modlog `CFP_4.2.23` for change record, section guidance `CFP_4.4.22` for hard constraints, briefing `CFP_5.3.29` for Cordasco corpus provenance.

The "visibility argument" sketch in `CFP_5.3.27` lines 76–81 (Williams Greek tragedy / Cavell / Nozick / Lewis as a values-language list) is *partially* absorbed in v5 (Cavell added; Lewis rejected; values-language deliberately omitted). Further integration would require respecting the agent-vs-methodology distinction now in section guidance.

**Tier 3 review edits — in progress:**

- **S1 (MHC transfer)** — DONE 2026-05-12. §5 MHC introduction rewritten: "transfers structurally" removed; borrowing characterized as conceptual not analogical; cross-reference to §3 v5 agent-integrity grounding added. See `CFP_4.2.18` MOD-023.
- **O5 (Circularity)** — DONE 2026-05-12. §6.4 self-exemplification passage rewritten to make the feasibility/adequacy distinction explicit; self-citation explicitly framed as evidence-of-feasibility (author-demonstrable), not evidence-of-adequacy (community-settled). See `CFP_4.2.19` Entry 9.
- **O2 (Comparison cases)** — DONE 2026-05-12. §3 v5.1: one-sentence scope marker added at end of paragraph 2 of "Reproducibility Is Not the Issue" — disanalogy limited to ethics-vs-empirical-science specifically; history, literary criticism, political theory explicitly out of scope. See `CFP_4.2.23` v5 → v5.1 entry.
- **S3 (Abdulhai preprint over-relied on)** — Already DONE 2026-04-09. Confirmed during S3 audit 2026-05-12. §6 v3.2 hedging covers all four Shoulders concerns: preprint status flagged ("An arXiv preprint... — unreviewed at the time of writing"); study design hedged ("appropriate caution"); operationalization explicitly named; domain inference flagged ("remains to be established... If the finding generalizes..."). Abdulhai cited only in §6; not in §3 or elsewhere. Global bibliography entry already marks it as arXiv. See `CFP_4.2.19` Entry 7. The work plan tracker was lagging the actual state; no new edit needed.

**Tier 3 review edits complete (S1, O2, O5, S3).**

**Phase 4 — Title + Abstract DONE 2026-05-12 (SID-20260512-171552, commit `a7294d0`).**

- **Title:** *The Journal of Prompt Engineered (Moral) Philosophy: Or, Why AI-Assisted Ethics Research Requires Process Transparency.* The "Frankenstein; or, …" structure: a wink upfront (the project's own working name reread as a self-aware framing of what the paper is about), an argumentative CFP-anchor after the "Or." User-selected from a field of nine candidates; the sober variants foregrounding agent-integrity or documentation-adequacy were declined in favor of the argumentative subtitle that names the question rather than the answer.
- **Abstract:** ~80 words. Saved in `CFP_5.4.15_Abstract_v1.md` (numbers 11–14 were taken by SP-3, SP-2, SP-1, and the AI Usage Archive). Drafted in two passes: first an over-balanced v1 keyed to Introduction + §3 + Conclusion alone; then a v2 rebalanced against the actual post-v5 paper weights (§3 carries ~30% of body weight and defeats three truth-tracking-adjacent framings — cognitivist, Cordasco/welfare-economic, reproducibility; §5 framework + §6 dual assessment proportionally weighted); then v3 compressed by ~70% to the philosophical core (§3 contestedness + three defeats, agent-integrity grounding, framework name, self-exemplification + archive). §4 conditions, §6 dual assessment, and the "restoration" closing were explicit trade-offs against the compression target. Modlog `CFP_4.2.33_ModificationLog_AbstractTitle.md` records both decisions (MOD-001 abstract, MOD-002 title).

**Phase 5 — IN PROGRESS (started 2026-05-12, SID-20260512-171552; v1.1 cleanup completed in SID-20260512-223052).**

`Paper/MDversion/CFP_FullPaper_v1.md` now at v1.1 (commit `fb128e4`). v1 assembly anchor is preserved at commit `ca921f3`. Single-file `git_inplace` versioning: `git diff ca921f3..fb128e4 -- Paper/MDversion/CFP_FullPaper_v1.md` is the authoritative v1 → v1.1 change record. No submission-anchor pin needed (the Tier 3 review was of an earlier assembly, `CFP_5.3.23_Note_AssembledPaperBuild`, not of CFP_FullPaper_v1).

**Phase 5 — Commit 1 (Tier 3 review chain story-completeness) — DONE (commits `33aa741` + `13679ee`).**
Structured `inputs:` and `feeds_into:` added to `CFP_5.3.23`, `CFP_5.3.24`, `CFP_5.3.25`, `CFP_5.3.27`. The chain `5.3.23 → {5.3.24, 5.3.25} → 5.3.27 → {4.2.23, 4.2.18, 4.2.19, 4.7.21, 4.4.22, 5.3.29}` is now graph-traversable in frontmatter (no prose-only links). Modlog entries already linked review docs at the entry level via `Source:` lines — no body edits required.

Session-level fact added to `transparency/SCRIPTS/hub_annotations.yaml` for `SID-20260409-173842` (the response-draft session whose `session_topology.yaml` entry had `inputs: []` and an empty `goal`). hub_annotations.yaml is the project's documented authoritative source for non-inferable session-level facts (per `CFP_5.3.16` governance, 2026-04-03), git-tracked. `session_topology.yaml` itself is gitignored (local-only) and updated by `mhc_end.py` at session end — only `artifacts_produced` is auto-derived; goals/inputs are hand-maintained. **Backlog:** most SIDs from 2026-04-09 onwards are not yet in `hub_annotations.yaml`; the intended graph-builder wiring is also still pending. Both are flagged in the new hub_annotations entry's `note` for future backfill.

**Phase 5 — Commit 2 (CFP_FullPaper v1.1 cleanup) — DONE (commits `ca921f3` v1 anchor + `fb128e4` v1.1 cleanup).**

All five planned changes applied in `Paper/MDversion/CFP_FullPaper_v1.md`:

1. Cross-reference reconciliation (§4 / §5 / §6 body) — four post-renumbering references corrected (see MOD-001 in `CFP_4.2.34`).
2. Boden & Edmonds (2009) page corrected: `p. 138` → `p. 29`. Quote unchanged.
3. Santoni de Sio & van den Hoven (2018) `[VERIFY: replace with page number]` tag removed — Frontiers is online-only; `(§6.2)` is the correct locator.
4. Bibliography additions: Sartre (1956) and Boden & Edmonds (2009, with DOI `10.1080/14626260902867915`) added to `paper_bibliography_FINAL.md`.
5. Frontmatter bumped to `version: v1.1`; `versioning_convention: git_inplace`; `session_id` extended to list form; `assembly` rewritten; `known_issues` pruned to one remaining intentional design note (Cavell-without-formal-citation, by design).

Modlog: `transparency/Canonical_MD/SP4_ProcessDocumentation/4.2_ModificationLogs/CFP_4.2.34_ModificationLog_FullPaperAssembly.md` (MOD-001 through MOD-005, all approved).

**Next-up post-v1.1 (subsequent sessions):**

- Phase 5 final consistency review — full read-through of v1.1 against §5 transparency framework as a coherence check; no scope for further edits unless something material surfaces.
- Zenodo DOI mint: tag submission commit on GitHub; enable GitHub→Zenodo integration; cut Release; replace `[persistent identifier: forthcoming]` in `CFP_5.4.14_AIUsageArchive.md` and SP-1 line 81. Browser steps drivable via Chrome MCP plugin.
- Source-conversations manifest (`CFP_5.3.N_Note_RawConversationsManifest.md`) promised in SP-2 §7.
- Branch merge to `main` (housekeeping; not strictly required given tag + DOI).
- DOCX/PDF rebuild. Note: existing `build_paper.py` references `paper_bibliography.md` (not FINAL) and lacks the Abstract — needs a script fix before use.

**Other deferred items (Phase 5 / pre-submission):**

- **Persistent identifier (Zenodo DOI) for the externalized archive — Path A (publish at submission, not now).** Plan: after all intellectual revisions are complete (Williams, Tier 3 edits, Abstract, Title, Phase 5 read-through), tag the final submission commit on GitHub (e.g. `v1.0-jpep-cfp-submission`); enable the GitHub→Zenodo integration (one-time setup at https://zenodo.org/account/settings/github/); cut a GitHub Release on the tag; Zenodo auto-archives the tagged commit and mints a DOI; replace `[persistent identifier: forthcoming]` in `CFP_5.4.14` with the DOI. Repo remote: `https://github.com/MicheleLoi/JPEP.git`. **Tool note:** Claude can drive the Zenodo browser-side steps via the Chrome MCP plugin (`mcp__Claude_in_Chrome__*` tools) when the time comes; the user handles Zenodo login and OAuth approval (credential boundaries), Claude handles navigation, GitHub-toggle, release metadata, and the post-DOI updates to `CFP_5.4.14` and SP-1 line 81.
- Inline excerpts in `CFP_5.4.14` — pick one modlog entry + one figure to reproduce inline (forward promise currently kept as placeholder).
- SP-3 pre-renaming section references throughout `CFP_5.4.11_SP3.md`.
- SP-1 branch-merge-tense marker (`CFP_5.4.13_SP1.md` line 81) — resolve at submission. Merging the branch into `main` is **not strictly necessary** if the submission state is pinned via a tag + DOI; the SP-1 line can read "the submission state is preserved at tag `<name>` (commit `<SHA>`), archived at DOI `<DOI>`." Whether to also merge to `main` for discoverability is a separate housekeeping decision.
- Source-conversations manifest (`CFP_5.3.N_Note_RawConversationsManifest.md`) — promised in SP-2 §7.
- Figure-numbering reconciliation in SP-3 (file names 1/2/4/5/6 vs SP-3 narrative 1/2/3/4/5).
- Cleanup anomalies: `.bak` file in 4.4_SectionGuidance, `.patch.txt` in 5.3_Notes, space in `5.2.8 pdl-appendix-2.md`.
- Phase 5 final enumeration check of SP-2 inventory.

---

**This session (SID-20260512-111348, 2026-05-12):** Triage of uncommitted Apr 9–10 work + SP-1/SP-2/SP-3 externalization + SP-2 inventory refresh. 11 commits ending at `8eb8dc1`. Detail in `CFP_session_log.md`.

**Bridge period (2026-04-09 → 2026-04-10, five sessions):** Paper assembly via pandoc; Opus Reviewer B review + Shoulders external review; review-response revision pass; philosophical extensions (Sartre, good faith, tracing-condition ambiguity). SP-1 + SP-2 v1 produced. Section renumbering 2026-04-09 (old §5/§6/§7/§8 → new §4/§5/§6/§7; see `CFP_5.3.26_Note_DecisionRecord_SectionRenumbering.md`). Final commit of the bridge period: `19993b3`. Per-session detail in `CFP_session_log.md`.

---

**Previous session (SID-20260405-094022):** Documentation extraction + Stage III framing correction. First half: wrote work plan narrations for two prior sessions (SID-20260404-103931 and SID-20260405-085500) whose updates were not written before session end. Second half: analyzed what Stage III research contributes to SP-3. User corrected initial framing: the "incomplete infrastructure / user compensated manually" narrative was wrong — MHC-start and CLAUDE.md were in place; errors in field names and missing SIDs are routine session errors, not evidence of toolkit immaturity; SP-3 should not narrate the user's developing Claude skill. Correct framing: infrastructure was in development, and each gap shows empirically what a specific infrastructure component is for (version control preserves intermediate states; exports preserve reasoning; session IDs enable automated traceability; standardised fields enable machine-readable traceability). The failed Jan 28 draft would have been fully recoverable via `git show` if a commit had been made — two missed steps, not a structural limitation. Artifacts: PDL-023 in CFP_5.2.4; feedback file `20260405_user_commit_as_recovery_mechanism.md` in MHC-W-Prototype inbox. Updated: CFP_4.4.20 (v5 → v6, Phase 2 rewritten with infrastructure-requirements table), CFP_4.7.19 (§5.2–5.3 and §6.2 corrected), CFP_5.3.1 (this file).

**Previous session (SID-20260405-085500):** Stage III input/output analysis — completing the research base for SP-3 Phase 2 narrative. Read all 15 III_-prefixed artifacts and 14 exported Stage III conversations. Mapped input/output relations across 6 Stage III sessions (Jan 24 – Mar 2, 2026). Key findings: (1) metadata captures unexecuted designs — III_4.4.6 (Section 7 guidance) was created Feb 2 but never used; the first Section 7 draft (CFP_5.4.9 v1, Mar 24) was produced under different, CFP-specific guidance; the absence of `output_completed` and the missing draft file together tell the story. (2) First MHC-start in JPEP was Feb 2 (Session 4), path was `MHC-prototype` (not yet renamed). (3) The SP reconception (III_4.7.3) emerged during Session 5, not planned in advance. User correction: the Type 8a/4 (Complete Prompt vs Section Guidance) distinction is a v1 ontology, not a Stage III development — the III_4.1.2 → III_4.4.6 reclassification was a filing error, not an ontology evolution. Artifacts: CFP_4.7.19 (epistemic trace). Updated: CFP_5.3.13 (§14 on Stage III), CFP_4.4.20 (Stage III findings added).

**Previous session (SID-20260404-103931):** SP-3 guidance rewrite + figure generation. Three user decisions: (1) CFP phase is no longer excluded from SP-3 corpus — PDL-017 exclusion and PDL-018 placeholder plan both superseded; (2) combine graph-led structure (PDL-013, figures as narrative spine) with research-paper depth (PDL-017) — each section anchored by a visual; (3) no bloated language — describe findings plainly, don't coin labels. CFP_4.4.20 rewritten as v5: corpus scope expanded to all three phases; Phase 3 rewritten from placeholder to substantive section with 10 findings from CFP chain walk; figure–section mapping table added; drafting process simplified (drafter reads briefing + chain walk findings, not fresh corpus pass). User also corrected: the "full corpus reading" requirement was a leftover from PDL-017 experiment that failed — remove it. Generated 5 figures via parallel sub-agents: Visual 3 (Feedback Loop), Visual 4 (Contrast Diptych), Visual 5 (Version Chain), Visual 7 (Date Histogram), Visual 8 (Hub Fan-Out). Known issues: Visual 7 misclassifies unprefixed files as v1/v2; Visual 8 undercounts CFP artifacts (parses hub files instead of frontmatter); Visual 5 has an incorrect edge (hub → v3). Artifacts: PDL-022 in CFP_5.2.4; 5 Python scripts in SCRIPTS/; 5 PNGs in _GRAPHS/. Updated: CFP_4.4.20 (v5).

**Next substantive step:** SP-3 drafting (Phase 3c). Research is now complete across all three phases. Entry point: read CFP_5.3.13 (writer briefing, 14 sections), then CFP_4.4.20 v6 (section guidance with infrastructure-requirements table and figure anchors). Before drafting, consider fixing the three figure issues (Visual 7 phase classification, Visual 8 artifact counting, Visual 5 incorrect edge). Alternatively: implement script improvements from CFP_4.7.18.

**Previous session (SID-20260404-083911):** Metadata infrastructure — hub system examination + CFP-era frontmatter normalization. Audited all 36 hub .bak files (no manual content at risk; deleted). Fixed VERIFICATION_QUEUE regex bug. Normalized 55 CFP artifacts to canonical field names: non-standard input fields → `inputs`, `outputs` → `output_completed` in 4 modlogs, added missing `inputs` to 11 traces + 19 drafts + 11 notes, added frontmatter to 2 bare files. Script aliases updated as safety net. Removed redundant `continuation_of`/`continued_by` from 4.7.3 (triple-encoded). Analyzed script gaps: `session_id` not read (CFP artifacts invisible to hub builder), `feeds_into`/`derived_from`/`output_completed`/`related` not in REL_FIELDS. Key insight from user: `inputs` is empirical (context window contents), `derived_from` is structural (version chain) — distinct edge types. Artifacts: CFP_4.2.26 (modlog), CFP_4.7.18 (script gap analysis trace).

**Previous session (SID-20260403-170017):** Contradiction analysis — systematic check of work plan against actual artifact state. Found 3 sessions from 2026-04-03 not narrated in RESUME HERE (SID-20260403-110246, -122011, -163539); added below. Resolved 3 open contradictions in CFP_5.3.17 (#4: 4.7.4→4.4.5 influence is indirect/conceptual, correctly encoded; #5: 5.3.13 is legitimate sibling of fb6251ae, late extraction; #6: SP5.1/5.1 naming is v1-era convention, no correction needed). CFP_5.3.17 status → Complete. Updated CFP_5.3.13 (writer briefing): added §11 (origin layer), §12 (PreliminaryChat chain), 3 new source files, 3 new contributing sessions; status → "research complete; ready for drafting". Added PDL-018: research phase complete; draft v1/v2 and III now, leave CFP phase as placeholder.

**Next substantive step:** SP-3 drafting (Phase 3c). Research complete (PDL-018). Entry point: read CFP_5.3.13 (writer briefing, 12 sections), then CFP_5.3.15 (origin story), then CFP_5.2.4 PDL-017/018 (scope + methodology + drafting plan), then CFP_4.4.20 (section guidance v3). Draft covers v1/v2 and Stage III in full; CFP phase left as marked placeholder.

**Previous session:** 2026-04-03 — PreliminaryChat chain verification (SID-20260403-163539). Tested input-output mapping on PreliminaryChat cluster (4.7.3/4.7.4/4.7.5). Resolved contradictions #1–3 (date conflict, numbering artifact, script issues). Left #4–6 open. Added hub_annotations.yaml entries for 5b8de38b, fb6251ae, e9d55db6. Created CFP_5.3.17. Added 5.2.4.1 to synthetic_nodes.yaml. **Work plan was not updated in that session.**

**Previous session:** 2026-04-03 — Hub metadata architecture design (SID-20260403-154700). Arose during mhc-start before SP-3 drafting. Designed authoritative-source architecture: `hub_annotations.yaml` is ground truth; hub `.md` files are derived. Key decisions: `continues_from` replaces `prior_chat`; session-level facts stay in YAML only; list form for complex flows. Script must not run until wired to read YAML. Artifacts: CFP_4.7.17 (epistemic trace), CFP_5.3.16 (decision record). Updated `adapt.md` §5. **Work plan was not updated in that session.**

**Previous session:** 2026-04-03 — Ur-conversation import + origin story philology (SID-20260403-154053). Verified export from SID-20260403-135745; executed 3 deferred TODOs. MHC-import of 6c8d9101 ("How LLMs process conversational goals", 2025-10-10, Claude Sonnet 4.5 extended): imported (133K chars, gitignored), hub created, chain links completed. Chain coherence corrected: 2ca5888a hub, 4.7.1 prior_chat, da6a830c hub UUID. hub_annotations.yaml created. Read ur-conversation in full: (1) costly signaling argument originated here; (2) transparency paradox / laundering first named here; (3) the "mess" = pre-systematic starting condition. Created CFP_4.7.16 and CFP_5.3.15.

**Previous session:** 2026-04-03 — Chain walk + 4.1 provenance work (SID-20260403-135745). Chain walk complete; findings in CFP_5.3.13 §10. Moved `III_4.1.2` → `III_4.4.6`. Created `5.3.21_EpistemicOrigin_InputToSynthesis.md` (anonymized source dialogue, 26K chars). Wrote MOD-001 in 4.1. Resolved 5.3.21 vs 4.7.1 (5.3.21 is fuller version; 4.7.1 is incomplete extract).

**Previous session:** 2026-04-03 — SP-3 writer briefing consolidation (SID-20260403-122011). Consolidated all SP-3 preparation into single briefing document. Artifacts: CFP_5.3.13 (writer briefing — the entry point for SP-3 drafting), CFP_4.2.25 (modlog). **Previously not narrated in work plan; artifact was referenced but session was not.**

**Previous session:** 2026-04-03 — Metadata audit + phase sequence reconstruction (SID-20260403-110246). Produced CFP_5.3.12 (phase summary working trace) and CFP_4.2.24 (metadata audit modlog). **Previously not narrated in work plan; indirectly referenced via CFP_5.3.13.**

**Previous session:** 2026-04-03 — Session chain reconstruction + audit rewrite (SID-20260403-131122). Read all 4.4.x (20 files), 4.3.x (5 files), and 4.2.x modlogs. Rewrote `CFP_5.3.5` from scratch. Created `CFP_5.3.14_Note_ChainWalkPlan.md`.

**Previous session:** 2026-04-03 (earlier, SID-20260403-093628) — SP-3 redesign (research-paper approach), two-order argument structure, Opus corpus research on ~140 files. Section 3 v3 drafted. Artifacts: `CFP_4.4.20`, `CFP_5.4.4_Section3_v3.md`, `CFP_4.7.15`, `CFP_4.2.23` (draft, pending review), PDL-017 added to `CFP_5.2.4`.

**Track A — Selected graph research: COMPLETE**
`CFP_5.3.7_SelectedGraphCandidates.md` produced in session SID-20260401-033111. Three verified candidates; fourth deferred (weaker grounding). No further action needed.

**DOUBLE CONTESTATION + REDUNDANCY REDUCTION: COMPLETE**

All 8 implementation steps executed in SID-20260401-173934 (JPEP_20260401_153253.md). Three-pass redundancy reduction completed in SID-20260401-225323 (JPEP_20260401_205323.md). Additional Section 3/6 refinements in SID-20260401-184454 (JPEP_20260401_164454.md).

The paper's essentially-contested-concept argument now operates at TWO levels (the "double contestation"):
- Level 1 (meta-ethical): what ethical inquiry IS → tracking requirement
- Level 2 (ethical): what doing ethical inquiry REQUIRES of the inquirer → authenticity requirement

The authenticity argument has CO-EQUAL WEIGHT with the tracking argument. Tradition: Socrates, Nietzsche, Kierkegaard (NOT Taylor). Artistic parallels: Cohen/AARON, modular synth + Boden & Edmonds. §6.1 rewritten from scratch. Routes renamed: "meta-ethical" (expressivism only) / "ethical" (authenticity tradition).

**Design history:** PDL `CFP_5.2.3` (entries PDL-000 through PDL-009). Source argument: `CFP_4.7.11` (antecedent input — do NOT revise). Design analysis: `CFP_4.7.12` (superseded by PDL-009 decisions). Implementation spec: `CFP_4.4.19_SectionGuidance_SelfExpressionDistribution.md`.

**DO NOT revise CFP_4.7.11.** It is a dated generative input (SID-20260401-111336). The design decisions that transformed it (Taylor → Kierkegaard, Bridge A, AARON, co-equal weight) are recorded in the PDL and implemented through CFP_4.4.19.

**Implementation steps (ALL COMPLETE):**

| Step | Action | Output | Status |
|------|--------|--------|--------|
| 0 | Section 7 v2 additions (Abdulhai + SRL) | `CFP_5.4.9_Section7_v2.md` | Done |
| 1 | Section 3: double contestation | `CFP_5.4.4_Section3_v2.md` | Done |
| 2 | Section 6: §6.1 rewritten from scratch | `CFP_5.4.8_Section6_v4.md` | Done |
| 3 | Section 7: authenticity enrichments | `CFP_5.4.9_Section7_v3.md` | Done |
| 4 | Introduction: signal both levels | `CFP_5.4.3_Introduction_v2.md` | Done |
| 5 | Section 5: dual-purpose notes | `CFP_5.4.7_Section5_v2.md` | Done |
| 6 | Section 2: closing note | `CFP_5.4.5_Section2_v4.md` | Done |
| 7 | Conclusion: full rewrite | `CFP_5.4.10_Conclusion_v1.md` | Done |

**Redundancy reduction (SID-20260401-225323):** ~9,165 → ~6,630 words (28% cut). Three passes + targeted Section 6 edits (expressivism-only route, route renaming, art examples replaced with modular synth + Boden & Edmonds / Cohen/AARON).

**Cross-paper modlogs:**
- `CFP_4.2.21_ModificationLog_DoubleContestation_Implementation.md` — all 8 steps + author review + reviewer letter + fixes
- `CFP_4.2.22_ModificationLog_RedundancyReduction.md` — three-pass reduction + Section 6 targeted edits
- `CFP_4.2.20_ModificationLog_Conclusion.md` — Conclusion creation + redundancy reduction

**Self-referential documentation trace (still relevant for SP-1/2/3 writing):**
`CFP_4.7.8_EpistemicTrace_SelfReferentialDocumentation.md` — three layers of self-reference; implications for Conclusion (partial instance, not solved example), Section 7 (contemporaneous satisfaction), Appendix A (v1/v2 reconstruction acknowledged).

**Metadata infrastructure state** (updated 2026-04-01): See Section G. Key facts: skeleton 72% coverage (92/128); CFP modlog SID gaps resolved; all 10 section drafts have `feeds_into` links; version chains encoded; 5 v1/v2 modlogs still missing SIDs (medium priority). Steering notes: `CFP_5.3.3` (phase structure), `CFP_5.3.4` (skeleton + connections status).

**Current authoritative files:**

| Section | File | Words (approx) |
|---------|------|-----------------|
| Introduction | `CFP_5.4.3_Introduction_v2.md` | ~760 |
| Section 2 | `CFP_5.4.5_Section2_v4.md` | ~730 |
| Section 3 | `CFP_5.4.4_Section3_v2.md` | ~1,290 |
| Section 4 | CUT | — |
| Section 5 | `CFP_5.4.7_Section5_v2.md` | ~760 |
| Section 6 | `CFP_5.4.8_Section6_v4.md` | ~1,540 |
| Section 7 | `CFP_5.4.9_Section7_v3.md` | ~1,030 |
| Conclusion | `CFP_5.4.10_Conclusion_v1.md` | ~520 |
| **Total** | | **~6,630** |

**Remaining work:**
- Phase 3b bibliography/references tasks still open (paper_bibliography.md, references_doc.md updates)
- Phase 3c: SP-1, SP-2, SP-3 drafting (absorbs former Appendix A; see CFP_5.2.4_pdl_SP1_SP2_SP3.md)
- Phase 4: Review + finalize Conclusion, then Abstract + Title
- Phase 5: Integration, full consistency review, final commit
- **Before final commit:** create `CFP_5.3.N_Note_RawConversationsManifest.md` (`document_type: manifest`) listing all files in `06_conversations/`, and add a paragraph to SP-3 stating the policy (raw conversations retained locally, manifest in SP5, available on request, artifact chain is the public spine). Decided 2026-04-08, SID-20260408-122758. When manifest is created: extend `build_graph.py` with ~45-line manifest enrichment pass to upgrade anonymous ChatGPT UUID stubs to named nodes. See `CFP_5.3.22_Note_DecisionRecord_ChatGPTConversationMetadata.md` for full design rationale.

**Appendix A: ELIMINATED** (PDL-004, SID-20260402-105621). SP-1/2/3 absorb all former appendix functions. No section of the paper body references "Appendix A." See CFP_5.2.4_pdl_SP1_SP2_SP3.md.

---

## HOW TO RESTART (mhc-start)

When the user types `mhc-start`, do the following in order:

1. **Read this file** in full. It is the master plan for the CFP adaptation.
2. **Read `adapt.md`** (project root). Contains terminology rules, infrastructure requirements, and documentation conventions. Path: `adapt.md` — also registered in `.mhc-config.json` under `project_conventions.path`.
3. **Check the progress checklist** (Section B below). Identify the next unchecked item.
4. **Run `git status` and `git branch`** on the working directory. Confirm you are on branch `cfp-ai-ethics-inquiry`. If not, switch to it.
5. **Read the source file** for the next section to be drafted (see Section C for locations).
6. **Follow the review protocol** (Section D) for that section.
7. **Follow the documentation protocol** (Section E) for artifact creation.

**Key directories:**
- Project root: `C:\Users\loimi\switchdrive\CURRENTLY WORKING ON\AI - assisted papers\JPEP\`
- Section drafts (v3 authoritative): `transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/`
- Section files (v1 baseline): `Paper/MDversion/`
- Modification logs: `transparency/Canonical_MD/SP4_ProcessDocumentation/4.2_ModificationLogs/`
- Epistemic traces: `transparency/Canonical_MD/SP4_ProcessDocumentation/4.7_EpistemicTraces/`
- Notes/steering: `transparency/Canonical_MD/SP5_DevelopmentRecords/5.3_Notes_Type11/`

---

## A. THE ARGUMENTATIVE SPINE (Introduction)

This is the core intellectual architecture for the CFP Introduction. It was developed through a multi-turn analytical session (2026-03-02) and must not be altered without the user's explicit approval. Any drafting agent must reproduce this structure faithfully.

### Move 1: Literature gap

AI in education is debated; AI in scientific research is discussed; AI in ethics research is almost unaddressed. But ethics is where the question is hardest, because what constitutes ethical inquiry is fundamentally disputed.

### Move 2: The cognitivist objection and its defeat (argumentative hinge)

**The objection:** If ethics tracks truth, evaluate the outputs. A sound argument is sound regardless of how it was produced. Process transparency confuses discovery with justification. This is the strongest objection to the paper's entire project.

**The defeat (revised 2026-03-11):**

> *Note: The original spine had a "first step" arguing that output-evaluation is process-dependent because "ethicists have no moral truth-meter." This was cut on Opus structural review (2026-03-11) as a non sequitur: the cognitivist objection turns on the discovery/justification distinction, not on epistemic access to moral reality. The "thinking quality" intuition behind it belongs in Section 6.1 where it is properly developed. The defeat now rests on a single move:*

(i) "Ethical inquiry" is an essentially contested concept (Gallie 1956). Competent practitioners disagree about its constitutive methods, its epistemic structure, and its purpose. The cognitivism/non-cognitivism dispute -- one of the most fundamental and unresolved disputes in metaethics -- is the deepest instance: we do not even agree on whether ethics is in the business of tracking truth. The cognitivist objection presupposes what is contested. Output-evaluation criteria in ethics are themselves contested, so the objection is question-begging.

(ii) The essentially-contested nature of ethics does double duty: it motivates transparency directly (we cannot prejudge what AI does to ethics, so we must track it) AND it defeats the cognitivist objection (we cannot "just evaluate outputs" because output-evaluation criteria in ethics are contested too).

(iii) Qualification: The claim is not that process information is always necessary for any ethical argument. For simple applied ethics arguments with clear premises and valid inferences, the output may suffice. The claim is: for complex work involving judgment, contested methods, and genuine philosophical insight -- where AI assistance is most consequential -- output-evaluation alone is insufficient. AI systems can produce outputs that satisfy surface criteria without the understanding those criteria are meant to track.

**Key methodological point:** Cognitivism is NOT asserted as a premise. The cognitivism/non-cognitivism dispute is used as an *illustration* of the essential contestedness of ethical inquiry. The argument is ecumenical: cognitivists, constructivists, and particularists all have reason to want process visibility, because each needs to assess whether the process satisfied the criteria *their* view identifies as constitutive of ethical inquiry.

### Move 3: The pivot to tracking

Since output-evaluation in ethics is process-dependent, and process criteria are contested, the achievable goal is tracking what ethics research is becoming under AI assistance. Tracking requires visibility. Visibility requires a philosophically specified transparency framework -- not merely a disclosure mandate.

### Move 4: Contribution announcement

This paper provides such a framework, grounded in Meaningful Human Control (Santoni de Sio & van den Hoven 2018) and operationalized through documentation-adequacy rather than reproduction. The paper demonstrates the framework: it implements the transparency apparatus it argues for.

### Dialectical structure summary

```
Gap: AI in ethics research unaddressed
     |
     v
Objection: "Just evaluate outputs" (cognitivist challenge)
     |
     v
Defeat: Ethical inquiry is essentially contested
        (cognitivism dispute = deepest instance)
        → output-evaluation criteria are themselves contested
        → cognitivist objection is question-begging
     |
     v
Pivot: Track what ethics is becoming -> transparency required
     |
     v
Contribution: MHC framework + documentation-adequacy + self-exemplification
```

### Citations required in the Introduction

- Gallie, W. B. (1956). Essentially contested concepts.
- Santoni de Sio, F., Faber, N. S., Savulescu, J., & Vincent, N. A. (2016). Why less praise for enhanced performance? (constitutive/regulative distinction)
- Santoni de Sio, F., & van den Hoven, J. (2018). Meaningful human control over autonomous systems. (MHC framework)
- At least 2-3 citations for the cognitivism/non-cognitivism dispute. Recommended: Enoch (2011) or Shafer-Landau (2003) for realism; Gibbard (1990) or Blackburn (1993) for non-cognitivism; van Roojen SEP entry as neutral survey. Characterize the dispute accurately but do not adjudicate it.

### Philosophical flags (must be addressed in drafting)

1. "Ethical inquiry" as essentially contested needs brief support under Gallie's criteria (appraisive, internally complex, variously describable, open, aggressive/defensive use). Do not merely assert it.
2. Section 3 must develop the cognitivist objection and its defeat more fully than the Introduction. The Introduction compresses; Section 3 develops.
3. The self-exemplification creates a reviewer problem: the CFP venue has no specialized review infrastructure for SP-1 through SP-5. Anticipate this.
4. "Tracking" risks quietism objection. Gesture toward: tracking creates the evidentiary basis for future normative judgments.
5. The framework is itself subject to the contestation it diagnoses. Acknowledge this (Section 6.3's experimental framing helps).

---

## B. PROGRESS CHECKLIST

> **Note (2026-05-12):** The RESUME HERE section at the top of this file is the authoritative current status. The checklist below is preserved as historical evidence of the original plan; some items are now complete or superseded (Phase 3c SP-1/SP-2/SP-3 are done and have been externalised; the Conclusion has been finalised through Reviewer B). Update individual checkboxes opportunistically; do not treat as the source of truth.

### Phase 0: Setup
- [x] Branch created (`cfp-ai-ethics-inquiry` from `III-v3-mhc-revision` at 76435f2)
- [x] CFP text saved (`target-venue/cfp_ai-ethics-inquiry.md`)
- [x] Fit analysis complete (III_4.7.4)
- [x] Argumentative spine developed (this document)
- [x] Work plan created (this document)

### Phase 1: Introduction + Section 3 (priority — these carry the argument)
- [x] Draft Introduction (CFP_5.4.3_Introduction_v1.md)
- [x] Review Introduction (Reviewer A + Reviewer B)
- [x] Revise Introduction if needed (CFP_5.4.3_Introduction_v2.md, etc.)
- [x] Finalize Introduction (both reviewers approve)
- [x] Draft Section 3 adaptation (CFP_5.4.4_Section3_v1.md)
- [x] Review Section 3 (Reviewer A + Reviewer B)
- [x] Revise Section 3 if needed
- [x] Finalize Section 3 (both reviewers approve)
- [x] Create epistemic trace for Introduction development (CFP_4.7.5)

### Phase 2: Sections requiring reframing
- [x] Draft Section 2 compression (CFP_5.4.5_Section2_v1.md)
- [x] Review + finalize Section 2
- [ ] Draft Section 4 compression/cut (CFP_5.4.6_Section4_v1.md)
- [ ] Review + finalize Section 4
- [x] Draft Section 5 reframe (CFP_5.4.7_Section5_v1.md)
- [x] Review + finalize Section 5

### Phase 3: Sections requiring minor changes
- [x] Draft Section 6 minor reframe (CFP_5.4.8_Section6_v3.md)
- [x] Review + finalize Section 6
- [x] Draft Section 7 minor reframe (CFP_5.4.9_Section7_v1.md)
- [x] Review + finalize Section 7

### Phase 3b: Section 7 additions + double contestation (decided 2026-03-24; executed 2026-04-01)
- [x] Implement additions A + B + C → CFP_5.4.9_Section7_v2.md (SID-20260401-173934, Step 0)
- [x] Update paper_bibliography.md (3 new entries + Section VII block + housekeeping; SID-20260402-105621)
- [x] Update references_doc.md (new Section VII CFP block; SID-20260402-105621)
- [x] Create modlog CFP_4.2.20 (Conclusion; created 2026-04-02)
- [x] Double contestation: all 8 implementation steps (SID-20260401-173934); modlog CFP_4.2.21
- [x] Redundancy reduction: 3 passes, 28% cut (SID-20260401-225323); modlog CFP_4.2.22
- [x] Section 3/6 refinements: expressivism-only, tradition fixes (SID-20260401-184454)

### Phase 3c: SP-1/2/3 (supplementary materials — absorbs former Appendix A)
- [ ] Draft SP-1: Summary of how AI was used (CFP_5.2.4 PDL-001/002)
- [ ] Draft SP-2: Navigation document / index (CFP_5.2.4 PDL-003)
- [ ] Draft SP-3: Documentation account + adequacy argument (CFP_5.2.4 PDL-003)
- [ ] Review + finalize SP-1/2/3

### Phase 4: Conclusion, Abstract, Title
- [x] Draft Conclusion rewrite (CFP_5.4.10_Conclusion_v1.md — SID-20260401-173934, Step 7)
- [x] Redundancy-reduce Conclusion (SID-20260401-225323)
- [ ] Review + finalize Conclusion (Reviewer B pending)
- [ ] Draft Abstract rewrite (CFP_5.4.11_Abstract_v1.md)
- [ ] Review + finalize Abstract
- [ ] Draft Title revision
- [ ] Review + finalize Title

### Phase 5: Integration and documentation
- [ ] Integrate all finalized sections into single paper file
- [x] Create modification logs for all adapted sections (CFP_4.2.14–4.2.22 complete)
- [ ] Final consistency review (full paper read-through)
- [ ] Commit finalized CFP version to branch

---

## C. SECTION-BY-SECTION PLAN

### Section 1: Introduction
- **Current state:** v1 in `Paper/MDversion/01_introduction.md`. Argues for a new venue/journal; uses Floridi hook, four structural gaps, journal-design framing.
- **Transformation:** Major rewrite. New argumentative spine (Section A above). Drop: four structural gaps, journal-design language, reproduction test references, Section 4 preview. Keep: transparency paradox reference (briefly, as motivation -- the full treatment stays in Section 2). Add: cognitivist objection/defeat, essentially-contested argument applied to ethics, cognitivism/non-cognitivism as illustration.
- **Source for drafter:** Do NOT use the v1 Introduction as a template. Draft from scratch using the spine in Section A. The v1 may be consulted for Floridi references and literature citations only.
- **Priority:** FIRST. Everything else depends on the Introduction setting the frame.
- **Word target:** 800-1200 words.

### Section 2: Systemic Barriers to Disclosure
- **Current state:** v1 in `Paper/MDversion/02_systemic_barriers_to_disclosure.md`. Detailed analysis of incentive gradients, underreporting mechanisms, institutional design constraints.
- **Transformation:** Compress. The transparency paradox and incentive analysis are background for the CFP version, not the main argument. Retain the core insight (disclosure is mandatory but penalized; underreporting increases with significance). Cut or compress: the four underreporting mechanisms (definitional flexibility, temporal discounting, comparative framing, strategic vagueness) -- keep one or two as illustration. Cut or compress: institutional design constraints (2.2) -- this argues for a new venue, which is not the CFP frame.
- **Source for drafter:** `Paper/MDversion/02_systemic_barriers_to_disclosure.md`
- **Priority:** Phase 2.
- **Word target:** 500-800 words (down from ~1500).

### Section 3: Why Engage with AI-Assisted Scholarship?
- **Current state:** v3 draft at `transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/III_5.4.1_Section3_v3.md`. Contains the essentially-contested argument, constitutive/regulative distinction, Gallie, tracking pivot.
- **Transformation:** Reframe for ethics (currently generic "philosophy"). Add new subsection: the cognitivist objection and its defeat (output-evaluation is process-dependent in ethics). This develops what the Introduction compresses. Add explicit connection to Section 6.1's claim that "article evaluation never assessed merely whether arguments are valid -- it always also assessed thinking quality." The v3 Section 3 currently goes straight from essentially-contested to tracking; it needs the intermediate step showing why "just evaluate the outputs" fails.
- **Source for drafter:** `transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/III_5.4.1_Section3_v3.md` (authoritative). Also read Section 6.1 in `III_5.4.2_Section6_v3.md` for the thinking-quality argument.
- **Priority:** SECOND (immediately after Introduction).
- **Specific additions:**
  - Between "Philosophy as Essentially Contested" and "From Answer to Tracking," insert a subsection (working title: "Why Output-Evaluation Fails in Ethics") that: (a) states the cognitivist objection; (b) shows that the essential contestedness of ethics makes output-evaluation criteria themselves contested — the objection is question-begging. (Note: the earlier "first step" — output-evaluation is process-dependent because ethicists have no moral truth-meter — was cut as a non sequitur on 2026-03-11. The defeat rests solely on essential contestedness.)
  - Throughout: replace "philosophy" with "ethics/ethical inquiry" where appropriate for CFP framing. Not mechanically -- some passages should remain about philosophy generally.
- **Word target:** 1200-1500 words (up from ~950).

### Section 4: The Dilemma Reconsidered
- **Current state:** v1 in `Paper/MDversion/04_the_dilemma_reconsidered_short_term_positioning_and_long_term_transformation.md`. Argues about prestige dynamics, long-term positioning outside prestige systems.
- **Transformation:** Compress heavily or cut. This section exists to argue the proposed journal is viable despite being outside prestige systems. The CFP version does not propose a journal. If retained, compress to 1-2 paragraphs acknowledging the institutional challenge without the full prestige-dynamics argument. Consider folding surviving content into Section 2 or Section 5.
- **Source for drafter:** `Paper/MDversion/04_the_dilemma_reconsidered_short_term_positioning_and_long_term_transformation.md`
- **Priority:** Phase 2. Decision on cut vs. compress to be made after Introduction and Section 3 are finalized (the Introduction frame will clarify how much institutional context is needed).
- **Word target:** 0-400 words.

### Section 5: Signaling Discontinuity from Prestige System
- **Current state:** v1 in `Paper/MDversion/05_signaling_discontinuity_from_prestige_system.md`. Contains: ecological validity, good faith orientation, costly signaling. Framed as venue-design principles.
- **Transformation:** Reframe from "venue design principles" to "design conditions for responsible AI-assisted ethics research." The three principles (ecological validity, good faith, costly signaling) are sound and transferable -- they become conditions any transparency framework must meet, not features of a particular journal. Drop venue-specific language.
- **Source for drafter:** `Paper/MDversion/05_signaling_discontinuity_from_prestige_system.md`
- **Priority:** Phase 2.
- **Word target:** 800-1200 words.

### Section 6: Mandatory Transparency in Practice
- **Current state:** v3 draft at `transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/III_5.4.2_Section6_v3.md`. Contains MHC integration, tracing/tracking conditions, documentation-adequacy model, SP-1 through SP-5 table, three nested concerns diagram, Lloyd engagement, experimental development, pilot observations.
- **Transformation:** Minor. This is the paper's strongest CFP contribution. Changes needed: (a) replace any remaining "journal" or "venue" language with "research practice" or "community" language; (b) ensure Section 6.1's thinking-quality argument explicitly connects to the Introduction's cognitivist-objection defeat; (c) verify consistency with documentation-adequacy model (no reproduction-test remnants).
- **Source for drafter:** `transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/III_5.4.2_Section6_v3.md` (authoritative).
- **Priority:** Phase 3.
- **Word target:** ~1400 words (roughly same as current).

### Section 7: Review Mechanism
- **Current state:** v1 in `Paper/MDversion/07_review_mechanism.md`. Contains dual-reviewer architecture, trajectory-matching reproduction test.
- **Transformation:** Reframe from journal-specific review mechanism to community assessment of documentation adequacy. Drop reproduction test (already rejected in v3 Section 6). Reframe as: how should the scholarly community assess whether transparency documentation is adequate? This connects to Section 6's documentation-adequacy model.
- **Source for drafter:** `Paper/MDversion/07_review_mechanism.md`. Also consult v3 Section 6 for documentation-adequacy framing.
- **Priority:** Phase 3.
- **Word target:** 800-1200 words.

### Section 8: Conclusion
- **Current state:** v1 in `Paper/MDversion/08_conclusion.md`. Oriented toward journal-creation proposal.
- **Transformation:** Rewrite. The conclusion must land on: responsible AI-assisted ethics research requires a philosophically specified transparency framework; this paper has provided and demonstrated one; the essentially-contested nature of ethical inquiry means we cannot prejudge outcomes but must track them; the community assessment mechanisms remain to be developed.
- **Source for drafter:** `Paper/MDversion/08_conclusion.md` (for structure reference only).
- **Priority:** Phase 4.
- **Word target:** 400-600 words.

### Abstract and Title
- **Transformation:** Rewrite last, after all sections are finalized. The abstract must reflect the CFP framing, not the JPEP journal-creation framing. Title should signal: transparency + AI-assisted ethics research + methodology.
- **Priority:** LAST.

---

## D. REVIEW PROTOCOL

### Roles

- **Drafter:** Sonnet agent (working within the Claude Code session). Produces section drafts following the instructions in Section C. The drafter reads the source file, reads this work plan, and drafts the adapted section.
- **Reviewer A:** The user (human). Reviews each draft for philosophical accuracy, argumentative integrity, and alignment with the author's intentions.
- **Reviewer B:** Opus agent (within the same Claude Code session, or resumed). Reviews each draft against the criteria below.

### Review criteria (both reviewers assess all of these)

1. **Argumentative spine:** Does the draft follow the argumentative structure specified in this plan? (For the Introduction: does it execute Moves 1-4? For Section 3: does it include the cognitivist objection and defeat?)
2. **CFP framing:** Is the draft oriented toward "AI tools in ethics research" rather than toward journal-creation/venue-design?
3. **Philosophical defensibility:** Are the philosophical moves sound? Are claims supported? Are qualifications present where needed?
4. **Consistency with other sections:** Does the draft use the same terminology and conceptual framework as other finalized sections? (Especially: documentation-adequacy, not reproduction test; tracing condition; essentially contested concept; tracking.)
5. **Concision:** Does the draft meet its word target? Is there padding or repetition?

### Workflow per section

```
1. Session reads this plan, identifies next section
2. Drafter reads source file(s) for that section
3. Drafter produces draft -> saved as CFP_5.4.X_SectionName_v1.md
4. Reviewer B (Opus) reviews draft against criteria 1-5
5. Reviewer B assessment presented to user
6. User (Reviewer A) reads draft and Reviewer B assessment
7. User responds:
   - "approve" -> section finalized, committed, modification log created
   - "revise: [specific instruction]" -> drafter revises, new version saved
     as CFP_5.4.X_SectionName_v2.md, return to step 4
   - User may also provide own assessment before approving/requesting revision
8. Section finalized only when BOTH reviewers approve
```

### How Reviewer B (Opus) is invoked

Reviewer B operates within the same session. When a draft is ready for review, the session should:

1. Read the draft file
2. Read this work plan (specifically Section A for the argumentative spine, Section C for the section-specific instructions, and Section D for review criteria)
3. Produce a structured assessment with one paragraph per criterion (1-5 above)
4. End with a verdict: APPROVE, or REVISE with specific instructions

If the session is new (no prior Opus context), the work plan is self-contained. The reviewer needs only this document and the draft to assess.

### How Reviewer A (user) registers decisions

The user types one of:
- `approve` -- section is finalized
- `revise: [instruction]` -- e.g., `revise: Move 2 needs the qualification about simple applied ethics arguments`
- The user may also type extended comments before a decision

### Revision history

Every draft version is preserved:
- v1, v2, v3, etc. in `5.4_SectionDrafts/` with sequential numbering
- Reviewer comments are preserved in the modification log for that section (created at finalization)
- If a section goes through multiple revision rounds, the modification log records each round: what was requested, what changed

---

## E. DOCUMENTATION PROTOCOL

### Artifact types and locations

| Artifact type | Naming convention | Location |
|---|---|---|
| Type 12: Section Draft | `CFP_5.4.{N}_SectionName_v{M}.md` | `SP5_DevelopmentRecords/5.4_SectionDrafts/` |
| Type 3: Modification Log | `CFP_4.2.{N}_ModificationLog_SectionName.md` | `SP4_ProcessDocumentation/4.2_ModificationLogs/` |
| Type 2: Epistemic Trace | `CFP_4.7.{N}_Description.md` | `SP4_ProcessDocumentation/4.7_EpistemicTraces/` |
| Type 11: Steering Note | `CFP_5.3.{N}_Description.md` | `SP5_DevelopmentRecords/5.3_Notes_Type11/` |

### Numbering

Section draft numbers (Type 12) continue from the existing sequence:
- III_5.4.1 = Section 3 v3
- III_5.4.2 = Section 6 v3
- CFP_5.4.3 = Introduction (first CFP draft)
- CFP_5.4.4 = Section 3 CFP adaptation
- CFP_5.4.5 = Section 2 CFP adaptation
- CFP_5.4.6 = Section 4 CFP adaptation
- CFP_5.4.7 = Section 5 CFP adaptation
- CFP_5.4.8 = Section 6 CFP adaptation
- CFP_5.4.9 = Section 7 CFP adaptation
- CFP_5.4.10 = Conclusion CFP adaptation
- CFP_5.4.11 = Abstract CFP adaptation

Modification log numbers continue from III_4.2.13:
- CFP_4.2.14 = Introduction modification log
- CFP_4.2.15 = Section 2 modification log
- (etc., sequential)

Epistemic trace numbers continue from III_4.7.4:
- CFP_4.7.5 = Introduction argumentative development trace (documents the analytical session that produced the spine in Section A)

### What each artifact must contain

**Section Draft (Type 12) header:**
```yaml
---
project: JPEP
document_type: Type 12 - Section Draft
section: "[section name]"
version: "[vN] (CFP adaptation)"
date_created: [date]
status: Draft | Under Review | Finalized
source: "[agent model]"
source_guidance: "CFP_5.3.1_WorkPlan_CFP_Adaptation.md"
cfp_target: "AI Tools in Ethics Research (topical collection)"
word_count: ~[N]
---
```

**Modification Log (Type 3) must document:**
- What the JPEP version contained
- What the CFP version changed
- Why the change was made (link to CFP fit analysis and argumentative spine)
- Reviewer comments that led to revisions (if any)

**Epistemic Trace (Type 2) for the Introduction must document:**
- The analytical session (2026-03-02) that developed the argumentative spine
- The key intellectual moves: cognitivism as illustration (not premise), the cognitivist objection and its defeat, the essentially-contested argument applied to ethics
- The dialectical development: how Ideas 1 and 2 were synthesized through the user's insight that cognitivism is itself an essentially contested feature of ethics

### Git workflow

- All work happens on branch `cfp-ai-ethics-inquiry`
- Commit after each section is finalized (both reviewers approve)
- Commit message format: `CFP adaptation: [section name] finalized`
- Update `_INDEX_5.4.md` after each new section draft is added

---

## F. REFERENCE: CFP FIT ANALYSIS SUMMARY

From III_4.7.4 (corrected Phase 3 analysis):

| Paper section | CFP fit | Action |
|---|---|---|
| 1. Introduction | Partial -- journal-creation frame is JPEP-specific | **Rewrite** (spine in Section A) |
| 2. Systemic barriers | Background; not CFP's focus | **Compress** |
| 3. Why engage (v3) | Strong for "implications for ethics"; gap on methods | **Reframe + add cognitivist defeat** |
| 4. Dilemma/prestige | Weakest fit | **Compress or cut** |
| 5. Discontinuity/design | Moderate | **Reframe** (venue -> research practice) |
| 6. Mandatory transparency (v3) | Strongest contribution | **Keep, minor reframe** |
| 7. Review mechanism | Good | **Minor reframe** (journal -> community) |
| 8. Conclusion | Needs reorientation | **Rewrite** |

### Key CFP questions addressed by the adapted paper

| CFP question | Where addressed |
|---|---|
| What tasks can AI support in ethics? | Section 3 (implicitly, via tracking argument) |
| Which uses involve special risks? | Section 6 (opacity as epistemic risk) |
| What goods are lost? | Section 6.1 (attribution, guided thought, thinking quality) |
| Discovery vs. justification? | Section 6.1 (rejection of the binary) |
| Implications for ethics as a field? | Introduction + Section 3 (essentially-contested argument) |
| Could AI be an ethics expert? | Section 6 (tracing condition -- only if outputs trace to understanding) |
| Might AI help us understand our methods? | Section 3 (tracking what ethics is becoming) |

### Main gap remaining

Ethics-specific methods content (reflective equilibrium, casuistry, moral intuitions, thought experiments). The adapted paper does not contain detailed analysis of what AI can/cannot support for specific ethics methods. This is acknowledged as a gap. Options: (a) add a short subsection in Section 3; (b) acknowledge the gap and frame the paper as addressing the prior question (what framework do we need before we can assess method-specific impacts?). Option (b) is recommended -- it is honest and positions the paper correctly.

---

---

## G. METADATA INFRASTRUCTURE STATUS

*This section is updated in place as the skeleton and connections evolve. Last updated: 2026-04-01.*

### Skeleton (session-identity hub nodes)

| Layer | Count | Coverage |
|---|---|---|
| Total artifacts with frontmatter | 128 | — |
| Linked to a session (any type) | 92 | 72% |
| — UUID exact (v1/v2, Claude.ai) | 62 | |
| — SID exact (CFP + III reconstructed) | 27 | |
| — SID date-only (III phase) | 3 | |
| Orphaned (no session ID) | 36 | 28% |
| Hub nodes in `_HUBS/` | 51 | |

**Orphan breakdown:** ~6 admin/reference files (correct — no session ID needed); ~10 section drafts (correct by design — see below); ~18 v1/v2 modlogs and summaries (recoverable gap).

**Architectural note:** Section drafts intentionally carry no `session_id`. A draft spans multiple sessions; a single field would capture only the last session and misrepresent the history. The modification log is the correct locus of session-to-revision tracing. When assessing or narrating coverage, point to modlogs for trajectory evidence, not section drafts.

### Modlogs missing session IDs (real skeleton gaps)

| File | Phase | Priority | Notes |
|---|---|---|---|
| `CFP_4.2.14_ModificationLog_Introduction.md` | CFP | done | SID-20260303-102634 (JPEP_20260303_102634.md) |
| `CFP_4.2.16_ModificationLog_Section3.md` | CFP | done | SID-20260305-152034 (JPEP_20260305_152034.md) |
| `4.2.1_ModificationLog_I_Introduction__S01.md` | v1/v2 | medium | Content-matching needed |
| `4.2.2_ModificationLog_Section_II__S02.md` | v1/v2 | medium | Content-matching needed |
| `4.2.3_ModificationLog_Section_III__S02.md` | v1/v2 | medium | Content-matching needed |
| `4.2.5_ModificationLog_Section_II-III-IV_Consolidation__S02.md` | v1/v2 | medium | Content-matching needed |
| `4.2.9_ModificationLog_Section_VIII_6__S06.md` | v1/v2 | medium | Content-matching needed |
| `III_4.2.13_ModificationLog_Section6_v3.md` | III | medium | Use III reconstruction method (CFP_5.3.3 §5) |

### Connections (relational links)

| Layer | Count | Coverage |
|---|---|---|
| Artifacts with ≥1 relational link field | 44 / 128 | 34% |

Dense in: CFP phase artifacts, PDLs. Sparse in: v1/v2 modlogs and summaries (relational info in body text, not frontmatter).

**Known code gap:** `output_completed` references to `III_`-prefixed files render as UNRESOLVED in Connection blocks. The hub script's filename prefix regex does not match `III_`-prefixed filenames. Links are correctly recorded in frontmatter; they just do not generate resolved wikilinks. Fix is a one-line regex change in `obsidian_connections_with_chat_hubs.py`.

### Graph visualization

`transparency/SCRIPTS/build_graph.py` generates an interactive HTML graph from SP-4/SP-5 frontmatter. Output: `transparency/Canonical_MD/_GRAPHS/jpep_graph.html`. Run with `python3 build_graph.py` from the `SCRIPTS/` directory. Node colours: amber = session hubs, blue = section drafts, green = modlogs, purple = traces, teal = PDLs, grey = notes. Requires `pyvis` and `networkx` (`pip3 install pyvis networkx`).

### Reference documents for SP-1/2/3 writer

**→ START HERE: `CFP_5.3.13_Note_SP3_WriterBriefing.md`** — consolidated briefing for SP-3 drafting. Contains: confirmed phase sequence (Phases A–E), how documents were routed between writing sessions (the "generic links"), the format field effect (the single most important empirical finding), two author corrections about how to characterise the record, documentation gaps to acknowledge honestly, the three SP-3 strategy decisions already made, and the role of hubs in reconstruction. Read this before touching any of the files below.

For depth on specific topics:
- `CFP_5.3.9_Note_PhilologicalExplorationLessons.md` — source of the format field effect, author corrections, and SP-3 strategy decisions
- `CFP_5.3.6_CoworkFindings_ArtifactLinks.md` — verified input/output links for all 5 recovered v1/v2 writing sessions (12 hypotheses confirmed)
- `CFP_5.3.12_Note_SP3_PhaseSummary_WorkingTrace.md` — phase sequence reconstruction; hub-as-reconstruction-infrastructure; open questions
- `CFP_5.3.3_Note_MetadataReportingStructure.md` — how the reporting mechanism is structured across phases; summary statistics; SP implications
- `CFP_5.3.4_Note_SkeletonAndConnectionsStatus.md` — current coverage figures; architectural note on section drafts vs. modlogs; modlog gap table; SP-3 argument guidance
- `CFP_5.3.5_Note_V1V2MetadataAudit.md` — comprehensive audit of v1/v2 relational metadata; 91 files analyzed; field naming problems; graph extension requirements

**Origin-layer conversations (for SP-3 intellectual history):**
- `06_conversations/imported/Claude_JPEP_idea_origination_(real_world_journal).md` — da6a830c content (anonymized); the **second step** in the intellectual origin chain; developed Chat X's ideas into a full venue-design proposal over 49 turns; hub: `CHAT_da6a830c-...md`
- Chat X (UUID: 6c8d9101-cd3f-4f61-aaf9-f293de92d11c, title: "How LLMs process conversational goals") — the **first step**; true intellectual origin of the publishing-barriers argument; imported this session; **gitignored** (not anonymized); hub: `CHAT_6c8d9101-cd3f-4f61-aaf9-f293de92d11c.md`

---

*End of work plan.*
## Connections (auto)

_No connections found._

