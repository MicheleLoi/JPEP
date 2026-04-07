---
project: JPEP
document_type: Type 3 - Modification Log
label: CFP_4.2.26_ModificationLog_FrontmatterNormalization
title: "Modification Log: CFP-Era Frontmatter Normalization + Hub Cleanup"
date_created: 2026-04-04
session_id: SID-20260404-083911
source_conversation: JPEP_20260404_061930.md
status: Complete
inputs:
  - hub_annotations.yaml
  - obsidian_connections_with_chat_hubs.py
output_completed:
  - obsidian_connections_with_chat_hubs.py
related:
  - CFP_5.3.16_Note_HubMetadataArchitectureDecisions.md
  - CFP_4.7.17_EpistemicTrace_HubMetadataArchitectureDesign.md
  - CFP_4.7.18_EpistemicTrace_ScriptGapAnalysis.md
---

# Modification Log: CFP-Era Frontmatter Normalization + Hub Cleanup

## Context

Session examined the hub system (48 hubs, hub_annotations.yaml, generation script) and audited CFP-era artifact frontmatter for field naming consistency. Found systematic divergence: 13+ non-standard field names for `inputs`, inconsistent `outputs` vs `output_completed`, two files with no frontmatter, and a script regex bug creating false VERIFICATION_QUEUE alerts.

## Changes

### MOD-001: Hub .bak file audit and cleanup

**What:** Diffed all 36 .bak/.md pairs in `_HUBS/`. Found 35 byte-identical (ignoring timestamp), 1 differing only in YAML formatting. Deleted all 36 .bak files.

**Why:** .bak files were snapshots from two consecutive script runs 34 seconds apart. No manual content existed in any backup. Confirmed by exhaustive diff.

### MOD-002: VERIFICATION_QUEUE regex fix

**What:** In `obsidian_connections_with_chat_hubs.py` line 323, changed `r"^## Artifacts generati.*$"` to `r"^## Artifacts.*$"`.

**Why:** The script's manual-content detection flagged 28 hubs as having manual content. All 28 were false positives — the regex matched the old heading (`## Artifacts generated in this chat`) but not the current heading (`## Artifacts produced`).

### MOD-003: Non-standard input field names → canonical `inputs` (7 files)

**What:** Replaced `source_documents`, `sources_read`, `cowork_input` + `imported_chats` + `artifacts_consulted`, `depends_on` + `depends_on_2`, `source_epistemic_trace` + `source_pdl` + `source_design_analysis`, `prerequisite_reading` with canonical `inputs`.

**Files:** CFP_4.4.20, CFP_5.3.18, CFP_4.7.13, CFP_4.7.14, CFP_4.4.19, CFP_5.3.14, CFP_5.3.15.

**Why:** 13+ ad hoc field names accumulated across sessions. Script reads `inputs` as canonical; non-standard names were invisible to the graph.

### MOD-004: `outputs` → `output_completed` in 4 modlogs

**What:** Renamed field in CFP_4.2.21, CFP_4.2.22, CFP_4.2.24, CFP_4.2.25.

**Why:** Field naming consistency. Both names work via alias, but artifacts should use one canonical name.

### MOD-005: Added `inputs` to epistemic traces (11 files)

**What:** Added canonical `inputs` field to CFP_4.7.5 through CFP_4.7.17 (excluding 4.7.13, 4.7.14 which were handled in MOD-003). Inputs derived from `related` fields and cross-references.

**Why:** Traces had `feeds_into` (forward links) but no `inputs` (backward links). Graph could trace forward from traces but not backward to them.

### MOD-006: Normalized section drafts (19 files)

**What:** Replaced `source_file` + `source_guidance` with canonical `inputs` in all CFP_5.4.* files. Removed self-referential `source_file` entries from batch-session drafts (SID-20260401-173934).

**Why:** `source_file` and `source_guidance` are semantically inputs (things entering the context window). Self-referential entries (file pointing to itself) were artifacts of the batch generation process, not meaningful metadata.

### MOD-007: Added `inputs` to notes (11 files)

**What:** Added canonical `inputs` to CFP_5.3.2 through CFP_5.3.17.

**Why:** Notes had `related` and `feeds_into` but no backward input links.

### MOD-008: Added YAML frontmatter to 2 bare files

**What:** CFP_5.3.6_CoworkFindings_ArtifactLinks.md and CFP_5.3.11_Note_Chat30a52e69_OntologyDiscoveryAnalysis.md received standard frontmatter with session_id, inputs, feeds_into.

**Why:** Only files in the CFP archive with no YAML frontmatter at all.

### MOD-009: Script field aliases (safety net)

**What:** Added 13 non-standard field names to `V1V2_FIELD_ALIASES` in `obsidian_connections_with_chat_hubs.py`.

**Why:** Belt-and-suspenders. Artifacts are normalized, but future files might reintroduce non-standard names. Note: alias table is currently dead code (not applied by renderer). Retained as documentation and for future wiring.

### MOD-010: Removed `continuation_of`/`continued_by` from 4.7.3

**What:** Deleted two frontmatter fields from `4.7.3_PreliminaryChat 1.md`. Emptied `REL_FIELDS_CONTINUITY` in script.

**Why:** The 4.7.3 → 4.7.4 continuation link was triple-encoded: (1) artifact continuity fields, (2) artifact input/output chain (4.7.3 salient_outputs = 4.7.4 inputs), (3) `hub_annotations.yaml` (`fb6251ae.continues_from: 5b8de38b`). Removed encoding (1) as redundant. Used by exactly one file; never adopted as a convention.

## Key design insight: `inputs` vs `derived_from` vs `feeds_into`

User clarified that `inputs` is an empirical field recording what actually entered the context window — not a structural relationship. This distinguishes three edge types:

| Field | Meaning | Type |
|-------|---------|------|
| `inputs` | What entered the context window | Empirical provenance |
| `output_completed` | What was produced/finalized | Empirical provenance |
| `derived_from` | Prior version in chain | Structural (version) |
| `feeds_into` | Downstream consumer | Structural (dependency) |

`derived_from` and `feeds_into` were correctly left untouched during normalization — they are not synonyms for `inputs`/`outputs`.

## Remaining script improvements identified

1. **Read `session_id` as fallback for `source_chat_id`** — CFP artifacts invisible to hub builder
2. **Add `derived_from`, `feeds_into`, `output_completed`, `related` to REL_FIELDS** — as distinct categories
3. **Aggregate artifact metadata onto auto hubs** — reduce YAML dependency for CFP sessions
4. **Wire alias table** — currently dead code

## Commits

- `3d6c6ef` — Normalize CFP-era frontmatter (55 files)
- `5965e01` — Remove continuation_of/continued_by (2 files)
