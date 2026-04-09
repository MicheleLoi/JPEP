---
project: JPEP
document_type: Type 3 - Modification Log
label: CFP_4.2.29_ModificationLog_SP1_SP2
title: "Modification Log: SP-1 and SP-2 v1 production"
date_created: 2026-04-09
session_id: SID-20260409-150705
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

## Validation

approved

---

*Modlog records SP-1 and SP-2 v1 production in session SID-20260409-150705. Both files committed at 7f8d8a0. Single-file versioning convention: future revisions tracked as MOD-NNN entries here; prior versions recoverable via git.*
