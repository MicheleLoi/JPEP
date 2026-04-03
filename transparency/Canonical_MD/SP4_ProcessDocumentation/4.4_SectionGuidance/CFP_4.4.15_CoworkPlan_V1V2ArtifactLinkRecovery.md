---
project: JPEP
document_type: Type 6 - Section Guidance
title: "Cowork Plan: V1/V2 Modlog Artifact Link Recovery"
date_created: 2026-04-01
status: ready_for_cowork
author: Claude Code (SID-20260401)
relevance_for: [cowork, graph-visualization, v1-v2-metadata]
feeds_into: "CFP_5.3.5_Note_V1V2MetadataAudit.md"
---

# Cowork Plan: V1/V2 Modlog Artifact Link Recovery

## Purpose

Five v1/v2 modlogs are missing `inputs` and `output_completed` frontmatter fields that link them to their artifact chain. These fields cannot be reconstructed without reading the source conversations on Claude.ai. This plan is designed for a Claude Cowork session with browser access.

Phase 1 (build_graph.py V1V2 extension), Phase 3 (priority file fixes) are **complete**. This is Phase 4.

---

## Target Files

| File | UUID to open | What to find |
|------|-------------|--------------|
| 4.2.1 | `ae493f0b-cc8a-43b0-b32f-0fc597b297a2` | `revision_chat_id` — open and extract: which section draft version was produced, what was input |
| 4.2.2 | `4177422b-27c3-44d4-a52e-f065de4e72ab` | Source chat for Old Section II — extract: input prompt/guidance, output draft ID |
| 4.2.3 | `6e92907a-03f7-413f-b99f-2983f8f44b22` | Source chat for Old Section III — extract: input guidance, output draft ID |
| 4.2.5 | `ffea5b8a-9c81-46c9-bb3c-8138d45c8eec` | Consolidation chat — extract: what three sections were merged, output draft |
| 4.2.10 | `fa1829d1-1f58-4e33-b423-bcc78ea6fb79` | Section IX/7 writing chat — extract: input guidance docs, output draft |

**Note on 4.2.1:** The original draft chat (`source_chat_id`) is lost (set to null). The `revision_chat_id` (`ae493f0b-...`) covers post-completion rewriting. Open it to extract the revision's inputs/outputs for that modlog.

---

## How to Open Each Conversation

Open in browser: `https://claude.ai/chat/{UUID}`

Example: `https://claude.ai/chat/ae493f0b-cc8a-43b0-b32f-0fc597b297a2`

---

## What to Extract Per Chat

For each chat, find:
1. **inputs** — what documents/artifacts were pasted or referenced at the start (section guidance, previous drafts, complete prompt)
2. **output_completed** — what section draft was produced (look for artifact IDs like `4.5.X`, `5.X.X`, or draft version labels)
3. **date** — confirm or correct the date field if different from frontmatter

---

## Frontmatter Fields to Add

After reading each chat, add to the file's YAML frontmatter:

```yaml
inputs:
  - "<artifact ID or description>"
output_completed: CFP_5.3.6_CoworkFindings_ArtifactLinks.md
```

For 4.2.1 specifically, also check:
- Was an `inputs` list documented in the body? (It may already be there)
- The revision produced — which final draft version?

---

## Files to Edit After Recovery

```
transparency/Canonical_MD/SP4_ProcessDocumentation/4.2_ModificationLogs/4.2.1_ModificationLog_I_Introduction__S01.md
transparency/Canonical_MD/SP4_ProcessDocumentation/4.2_ModificationLogs/4.2.2_ModificationLog_Section_II__S02.md
transparency/Canonical_MD/SP4_ProcessDocumentation/4.2_ModificationLogs/4.2.3_ModificationLog_Section_III__S02.md
transparency/Canonical_MD/SP4_ProcessDocumentation/4.2_ModificationLogs/4.2.5_ModificationLog_Section_II-III-IV_Consolidation__S02.md
transparency/Canonical_MD/SP4_ProcessDocumentation/4.2_ModificationLogs/4.2.10_ModificationLog_Section_IX_7__S07.md
```

---

## After All Five Files Updated

Run from `transparency/SCRIPTS/`:
```bash
python3 build_graph.py
```

Expected result: ~5–15 additional edges in the graph (each modlog gaining input and output connections). Verify the graph node count stays at ~186 and edge count increases.

---

## Context

- Audit report: `CFP_5.3.5_Note_V1V2MetadataAudit.md`
- Graph script: `transparency/SCRIPTS/build_graph.py`
- Graph output: `transparency/Canonical_MD/_GRAPHS/jpep_graph.html`
- Current state after Phase 1+3: 186 nodes, 191 edges
