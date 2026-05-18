---
project: JPEP
document_type: Type 3 - Modification Log
label: CFP_4.2.29_ModificationLog_SP1_SP2
title: "Modification Log: SP-1 and SP-2 v1 production"
date_created: 2026-04-09
date_last_updated: 2026-05-16
session_id:
  - SID-20260409-150705
  - SID-20260512-111348
  - SID-20260516-152731
status: Active
inputs:
  - CFP_5.4.11_SP3.md
  - CFP_5.4.9_Section7_v3.md
  - CFP_5.2.4_pdl_SP1_SP2_SP3.md (PDL-005, PDL-006)
  - 06_conversations/imported/ (ChatGPT conversation metadata)
  - transparency/SCRIPTS/hub_annotations.yaml
output_completed:
  - CFP_5.4.12_SP2.md (v1)
  - CFP_5.4.13_SP1.md (v1)
related:
  - CFP_4.2.27_ModificationLog_SP3.md
  - CFP_5.2.4_pdl_SP1_SP2_SP3.md
---

# Modification Log: SP-1 and SP-2 v1 production

## Context

Phase 3c of the CFP adaptation. SP-3 was complete at v3 (CFP_4.2.27 MOD-006). This session drafted SP-2 and SP-1 in that order, reading SP-3 and Section 7 as the primary inputs. Both documents are v1 drafts under the single-file versioning convention (no `_v1` suffix; git commit is the version anchor). SP-2 is marked provisional; SP-1 is not.

---

## Changes

### MOD-001: SP-2 v1 drafted — full artifact enumeration

**What:** `CFP_5.4.12_SP2.md` produced. Per PDL-006 (Option B — map with legend), SP-2 contains: the eleven-type document type ontology with folder locations and descriptions; the metadata infrastructure (SID conventions, key frontmatter fields, versioning convention distinction); the hub system and `hub_annotations.yaml` as authoritative topology source; the graph infrastructure (three SVG files, four HTML interactive graphs); a complete SP-4 file inventory (all files in 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7 enumerated by name); a complete SP-5 file inventory (all files in 5.2, 5.3, 5.4 enumerated by name); the conversation layer policy (gitignored directory, manifest pointer); and the section numbering reference table (old Roman numerals → current Arabic, with Section IV cut and Appendix absorbed noted).

**Decision on enumeration strategy:** real artifact enumeration (all file names listed) rather than category descriptions with representative examples. This makes SP-2 a genuine navigation tool rather than an overview. A final enumeration check is scheduled for Phase 5 before submission; the document is marked provisional accordingly.

**Why:** PDL-006 specifies Option B (map with legend). The file inventories are only useful if they are actual inventories. The provisional marker and Phase 5 check handle the maintenance cost.

### MOD-002: SP-1 v1 drafted — AI usage declaration and archive orientation

**What:** `CFP_5.4.13_SP1.md` produced. Per PDL-005 (~2 pages, two parts), SP-1 contains: a models/platforms table across all three phases (rows: v1/v2 Claude.ai with Sonnet 4.5; v1/v2 ChatGPT with GPT-5 Thinking; Stage III Claude Code with Opus 4.5 then Sonnet 4.6; CFP Claude Code with Sonnet 4.6 and Opus 4.6); roles by phase (drafter / modlog author / ontology contributor in v1/v2; drafter / infrastructure builder in Stage III; drafter / Reviewer B / automated metadata handler in CFP); the human author's role enumerated across the project; the phase/prefix table (plain number = v1/v2, `III_` = Stage III, `CFP_` = CFP); SID conventions with UUID note for v1/v2; documentation conventions across phases; and an entry-points table for SP-2 through SP-5.

**Why:** PDL-005 specifies a short document (~2 pages) that gives a philologist enough archival orientation to navigate the record without redundancy with SP-2 (architecture) or SP-3 (adequacy argument).

### MOD-003: In-session corrections to SP-1

Four corrections made during the drafting session before commit.

**1. ChatGPT model — GPT-4o struck, GPT-5 Thinking confirmed.** The initial draft used GPT-4o as the ChatGPT model. The locally saved conversation files (`06_conversations/imported/`) were checked: all six imported ChatGPT conversations have `model: gpt-5-thinking` in frontmatter except one (`chatgpt.com_690c9b9f_Creative_paper_titles.md` which has `gpt-4o`). The SVG/figure generation thread (`chatgpt.com_68f54fc3_JPEP_Picture_Appendix_0.md`) records GPT-5 Thinking. Corrected throughout.

**2. ChatGPT usage scope — "one thread / SVG only / Nov 2025" corrected.** The initial draft followed SP-3's phrasing ("one cross-tool thread that used ChatGPT for SVG generation") and described the ChatGPT row as one thread for SVG generation in November 2025. The epistemic traces and imported conversations show multiple ChatGPT conversations in v1/v2: the LinkedIn discussion (`4.7.2`), three paper evaluation sessions ("Is this AI slop?" series, `4.7.7.1–3`), and the SVG/picture generation thread. Period spans October–November 2025. Corrected to: "GPT-5 Thinking (paper evaluation; SVG/figure generation)" across Oct–Nov 2025.

**3. Deleted conversation — explanatory device vs. label.** The initial draft referred to the deleted v1/v2 conversation as "Chat 1, the Introduction writing session," treating "(Introduction writing)" from CFP_5.3.13 §4 as a label. The user corrected: real labels are artifact names, metadata, and file identifiers; parenthetical descriptions in briefing prose are explanatory devices, not labels. Corrected to "one v1/v2 conversation was deleted by the user and is not reconstructable." The same correction applies in SP-3 §10 (flagged for review pass).

**4. Branch merge tense — future-tense statement marked pending.** The sentence "The CFP adaptation was developed on branch `cfp-ai-ethics-inquiry` and merged into `main`" was written as if the merge had already occurred (it has not, as of 2026-04-09). The user flagged that writing in the future-as-past tense creates reconstruction confusion for future AI sessions inferring from the document when the merge occurred. Fix: inline marker added (`[to be merged into \`main\` before submission — update tense when done]`); `pending` field added to frontmatter recording the date and what to update. This is not a content error but a temporal accuracy discipline.

**5. "Versioned section drafts" removed from SP-5 entry points.** The SP-5 row in the entry-points table described the reading destination as "prompt development decisions, working notes, or versioned section drafts." The user flagged that versioned section drafts (the legacy per-version files) were a temporary departure from the process — the project now uses single-file git versioning — and should not be advertised as a destination. Corrected: "Read the prompt development decisions or working notes." Section drafts remain in the contents column (they exist and a reader may land there) but are no longer a named reading destination.

**Why these are one entry.** Five corrections all arising from the same drafting session read-through, all corrections to misstatements rather than design changes, all resolved before commit.

---

## Post-Update: SP-2 inventory refresh and corrections (2026-05-12)

**Session:** SID-20260512-111348

**Source:** disk enumeration of SP-4 and SP-5 (Explore subagent) vs SP-2's stated inventory; SP-2 §1's own provisional disclaimer (which explicitly scheduled a refresh). The day's externalization arc (commits 42be9de + 5eaf2ea + 285efbd) produced multiple new SP-4 and SP-5 artifacts that needed to be reflected in the navigation index for the archive to deliver on the closing note's (CFP_5.4.14) promise.

### MOD-004 — SP-2 inventory refresh + three corrections

**What:** `CFP_5.4.12_SP2.md` updated in place. Changes:

1. **Frontmatter** — converted `session_id` to a list (added SID-20260512-111348); added `date_last_updated: 2026-05-12`; rewrote the `note` field to reflect the refresh and itemise the added entries.

2. **§1 provisional note** — rewritten to record that inventories were refreshed today; Phase 5 final pass before submission remains scheduled.

3. **§2 ontology table** — Type 8a row corrected: pointer changed from "SP-5 / 5.2" to "SP-5 / 5.1". The project-level PDL lives in its own `5.1_PaperPromptDevelopmentLog_Type8a/` subfolder, distinct from the Type 8b PDLs in `5.2_SectionPromptDevelopmentLogs_Type8b/`. Previously this navigation pointer was wrong; a reader following it would have landed in the wrong folder.

4. **§4.1 hub paragraph** — rewritten to acknowledge that the `_HUBS/` directory is currently empty. Earlier hub `.md` files were removed during the UUID/SID recovery work (per `adapt.md` project rule 4: "deleted hub files in git status signal successful UUID/SID recovery, not missing sessions"). The hub-generation script has not been re-run because it is not yet wired to read `hub_annotations.yaml` directly. The YAML file remains authoritative.

5. **§5.1 (4.6 Reference Logs)** — added `paper_bibliography_FINAL.md` row.

6. **§5.2 (4.2 Modlogs)** — added rows for `CFP_4.2.29`, `CFP_4.2.30`, `CFP_4.2.31`, `CFP_4.2.32`.

7. **§5.4 (4.4 Section Guidance)** — added `CFP_4.4.21` row.

8. **§6.1 (5.2 PDLs)** — added `CFP_5.2.5` row.

9. **§6.2 (5.3 Notes)** — added rows for `CFP_5.3.23`, `5.3.24`, `5.3.25` (note + raw), `5.3.26`, `5.3.27`, `5.3.28`, and `CFP_session_log.md`.

10. **§6.3 (5.4 Section Drafts)** — added rows for `CFP_5.4.13` (SP-1) and `CFP_5.4.14` (AI Usage Archive) in the authoritative-current-versions table.

11. **§8 section-numbering table** — rewritten. Replaced the three-column "v1/v2 Roman / Intermediate / Current" layout (which used pre-2026-04-09 numbers in the Current column) with a two-column "v1/v2 Roman / Current CFP §" layout using post-2026-04-09 numbering throughout. Added a row for the new unnumbered closing note (`CFP_5.4.14`) and updated the Appendix A row to record both the 2026-03-02 SP reconception and the 2026-05-12 externalization. The supporting prose now cites `CFP_5.3.26` (renumbering decision record) and `CFP_5.2.5` (externalization PDL).

**Why:** SP-2 §1 marked the inventories provisional with a scheduled refresh; the externalization arc made that refresh load-bearing for the archive's navigability (the closing note in the paper body points readers to the archive, and SP-2 is where they orient). The three corrections (Type 8a path, _HUBS honesty, §8 numbering) addressed gaps already present in SP-2 v1 but salient under the externalization. The full Phase 5 enumeration check remains scheduled for pre-submission.

**Anomalies surfaced (flagged, not addressed in this pass):**

- `III_4.4.5_SectionGuidance_Section6_MHC.md.bak` — tracked .bak file in 4.4_SectionGuidance.
- `II_5.3.4_cfd43f4c6a1c3a1e70bedf1ed3109c8425e35ef6.patch.txt` — patch file in 5.3_Notes.
- `5.2.8 pdl-appendix-2.md` — leading space in filename.

Pre-existing housekeeping items unrelated to the externalization; left for a separate cleanup pass.

---

## Post-Update: SP-1 "Documentation conventions" — residual "hand-authored" cleanup (2026-05-16)

**Session:** SID-20260516-152731

**Source:** User read-through of SP-3 surfaced a residual "hand-authored" misstatement that the CFP_4.2.27 MOD-003 item 2 pass had not fully swept; grep confirmed a parallel surviving statement in SP-1's "Documentation conventions" paragraph.

### MOD-005 — SP-1 §"Documentation conventions" sentence corrected

**What:** First sentence of the "Documentation conventions" sub-section in `CFP_5.4.13_SP1.md` rewritten from "v1/v2 artifacts were authored by hand inside chat sessions and extracted manually into the archive" to "v1/v2 artifacts were AI-generated inside chat sessions (Claude.ai, plus one cross-tool ChatGPT thread) and extracted manually into the archive." Preserves the (correct) manual-extraction point; removes the (wrong) hand-authorship claim. Aligns the sentence with the controlling framing in SP-3 §5.1 line 139 (*"the user prompted, reviewed, and accepted, and Claude distilled"*).

**Why:** Same misconception that `CFP_4.2.27` MOD-003 item 2 and MOD-008 corrected in SP-3. SP-1 carried a parallel statement that the earlier SP-3-scoped passes had no occasion to touch; brought into alignment in the same pass as the SP-3 residual cleanup. See `CFP_4.2.27` MOD-008 for the SP-3 side and for the controlling vocabulary.

**Affected text:** SP-1 §"Documentation conventions", first sentence.

---

## Validation

approved (v1 production, 2026-04-09); approved (Post-Update MOD-004, 2026-05-12); approved (Post-Update MOD-005, 2026-05-16).

---

*Modlog records SP-1 and SP-2 v1 production in session SID-20260409-150705. Both files committed at 7f8d8a0. Single-file versioning convention: revisions tracked as MOD-NNN entries here; prior versions recoverable via git. SP-2 refreshed in SID-20260512-111348 (MOD-004 above). SP-1 "Documentation conventions" sentence corrected in SID-20260516-152731 (MOD-005 above) — paired with `CFP_4.2.27` MOD-008 in SP-3.*
