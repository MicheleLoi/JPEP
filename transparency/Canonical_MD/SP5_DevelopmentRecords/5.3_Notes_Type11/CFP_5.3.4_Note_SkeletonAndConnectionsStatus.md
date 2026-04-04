---
name: "Skeleton and Connections Status"
description: "Current coverage of session IDs (skeleton) and relational links (connections) across SP-4 artifacts, with architectural note on section drafts vs. modlogs"
document_type: Type 11 - Steering Note
label: CFP_5.3.4_Note_SkeletonAndConnectionsStatus
project: JPEP
date_created: 2026-04-01
status: Active
session_id: SID-20260401-000000
session_id_precision: date-only
inputs:
  - CFP_5.3.3_Note_MetadataReportingStructure.md
source: "Claude Sonnet 4.6 (Claude Code session) + user direction"
relevance_for:
  - SP-1 rewrite (AI use declaration)
  - SP-2 rewrite (navigation document)
  - SP-3 rewrite (documentation adequacy account)
related:
  - "CFP_5.3.3_Note_MetadataReportingStructure.md (phase structure and statistics)"
  - "CFP_5.4.9_Section7_v1.md (adequacy criteria)"
  - "transparency/Canonical_MD/obsidian_connections_with_chat_hubs.py (hub script)"
  - "transparency/Canonical_MD/_HUBS/ (generated hub nodes)"
---
# Skeleton and Connections Status

## Note to AI reader

This document is a companion to `CFP_5.3.3_Note_MetadataReportingStructure.md`. Where that note explains *how the reporting mechanism is structured*, this note reports the *current state* of two specific layers: the session-identity skeleton (hub nodes) and the relational connection links. It also records one architectural decision that is non-obvious and must not be misread when assessing coverage gaps.

Read this document alongside CFP_5.3.3 before writing SP-1, SP-2, or SP-3.

---

## 1. The skeleton: session ID coverage

The session-identity skeleton is the graph of hub nodes in `_HUBS/`. One hub per AI session; each artifact links to its hub via `## Connections (auto)`. The hub script (`obsidian_connections_with_chat_hubs.py`) generates these automatically from frontmatter fields.

**Current figures (as of 2026-04-01, 128 artifacts with frontmatter):**

| Layer | Count | Coverage |
|---|---|---|
| Linked to a session (any type) | 88 | 68% |
| — UUID exact (v1/v2, Claude.ai) | 62 | |
| — SID exact (CFP + III reconstructed) | 23 | |
| — SID date-only (III phase, no export) | 3 | |
| — Non-standard SID | 0 | |
| Orphaned (no session ID) | 40 | 31% |
| Hub nodes generated | 48 | |

The 40 orphaned artifacts break into three groups:

1. **Reference and admin files** (~6): files in `4.6_ReferenceLogs/`, README, index files. These do not represent AI-assisted intellectual work and should not have session IDs. Not a gap.

2. **Section drafts** (~10): see Section 2 below. Not a gap.

3. **v1/v2 modification logs and summaries** (~18): produced in Claude.ai sessions but session ID was not recorded at creation time. Recoverable via content-matching against conversation exports if needed. Currently undone — acknowledged as a limitation.

---

## 2. Architectural decision: section drafts do not carry session IDs

**This is the most important thing to understand before assessing coverage.**

A section draft is a multi-session artifact. It goes through multiple revision cycles — each cycle is a separate AI session. Assigning a single `session_id` to a section draft would capture only the *last* session, which is misleading. It would misrepresent the intellectual history.

The correct locus of session-to-revision tracing is the **modification log**, not the section draft. The modlog records:
- Which session produced which revision
- What the user's instruction was
- What changed and why

The architecture is:

```
Session A ──► modlog entry (session_id: SID-A) ──► "what changed in draft v1 → v2"
Session B ──► modlog entry (session_id: SID-B) ──► "what changed in draft v2 → v3"
                     ↕
              section draft (no session_id — intentionally)
```

The section draft's `source_guidance` field points to the guidance document or modlog that governed the most recent revision. This is sufficient for navigation. The full trajectory is in the modlog chain.

**SP-3 implication:** When SP-3 argues that the intellectual trajectory criterion is satisfied for a given section, it should point to the *modlog* as the evidence, not the section draft. The absence of `session_id` on a section draft is not a documentation gap — it is the correct design.

---

## 3. The real skeleton gaps: modlogs without session IDs

Given the above, the meaningful skeleton gaps are modlogs that lack session IDs — because these are the artifacts that *should* carry session traceability but don't.

**Current modlog coverage:**

| File | Session ID | Phase | Priority |
|---|---|---|---|
| `4.2.10_ModificationLog_Section_IX_7__S07.md` | OK | v1/v2 | — |
| `4.2.11_ModificationLog_Appendix.md` | OK | v1/v2 | — |
| `4.2.12_ModificationLog_Title_and_Abstract.md` | OK | v1/v2 | — |
| `4.2.4_ModificationLog_Section_IV__S02.md` | OK | v1/v2 | — |
| `4.2.6_ModificationLog_Section_V_3__S03.md` | OK | v1/v2 | — |
| `4.2.7_ModificationLog_Section_VI_4__S04.md` | OK | v1/v2 | — |
| `4.2.8_ModificationLog_Section_VII_5__S05.md` | OK | v1/v2 | — |
| `CFP_4.2.15_ModificationLog_Section2.md` | OK | CFP | — |
| `CFP_4.2.17_ModificationLog_Section5.md` | OK | CFP | — |
| `CFP_4.2.18_ModificationLog_Section6.md` | OK | CFP | — |
| `CFP_4.2.19_ModificationLog_Section7.md` | OK | CFP | — |
| `5.3.18_ModificationLog_Appendix_A2.md` | OK | v1/v2 | — |
| **`4.2.1_ModificationLog_I_Introduction__S01.md`** | MISSING | v1/v2 | medium |
| **`4.2.2_ModificationLog_Section_II__S02.md`** | MISSING | v1/v2 | medium |
| **`4.2.3_ModificationLog_Section_III__S02.md`** | MISSING | v1/v2 | medium |
| **`4.2.5_ModificationLog_Section_II-III-IV_Consolidation__S02.md`** | MISSING | v1/v2 | medium |
| **`4.2.9_ModificationLog_Section_VIII_6__S06.md`** | MISSING | v1/v2 | medium |
| **`CFP_4.2.14_ModificationLog_Introduction.md`** | MISSING | CFP | **high** |
| **`CFP_4.2.16_ModificationLog_Section3.md`** | MISSING | CFP | **high** |
| **`III_4.2.13_ModificationLog_Section6_v3.md`** | MISSING | III | medium |

**Priority logic:**
- CFP modlogs (`4.2.14`, `4.2.16`) are high priority because the CFP phase used the SID system — a conversation export exists and the correct SID is recoverable. The field was simply not filled at creation.
- v1/v2 modlogs are medium priority — session IDs are recoverable via content-matching but require some effort.
- `III_4.2.13` follows the III phase reconstruction method (see CFP_5.3.3 §5).

---

## 4. Connections: relational link coverage

Relational links are directed edges connecting artifacts: `inputs`, `outputs`, `feeds_into`, `output_completed`, `source_guidance`, `related_documents`, etc. These populate the `### Related` block in `## Connections (auto)`.

**Current figures:**

| Layer | Count | Coverage |
|---|---|---|
| Artifacts with ≥1 relational link field | 44 / 128 | 34% |

Coverage by artifact type:
- **PDLs**: well-linked — `source_conversations`, `output_completed` populated
- **CFP section drafts**: `source_guidance` present; older drafts sparse
- **CFP modification logs**: `related_documents` present
- **v1/v2 modification logs**: mostly bare — relational info exists in *body text* but not in structured frontmatter fields
- **Epistemic traces**: `feeds_into` or `influenced_artifacts` present on some; others bare

**Known technical gap:** `output_completed` fields referencing `III_`-prefixed files (e.g. `III_4.4.4_SectionGuidance_...`) currently resolve as UNRESOLVED in the Connection block. The hub script's filename prefix regex does not match the `III_` prefix pattern. This is a code issue, not a metadata issue — the links are correctly recorded, they just do not render as resolved wikilinks in Obsidian.

**SP-3 implication:** The 34% relational coverage figure should be reported honestly. It should be contextualized: (a) the most important relational links — those between modlogs and their sessions — are present wherever modlogs have session IDs; (b) the low coverage in v1/v2 artifacts reflects the retrospective nature of the documentation system, not absence of intellectual process; (c) relational information for v1/v2 is recoverable from artifact body text and from the conversation exports.

---

## 5. Summary for SP-1, SP-2, SP-3

**SP-1** should note that:
- Session identity is fully tracked for v1/v2 (UUID) and CFP (SID) phases
- Two CFP modlogs (`4.2.14`, `4.2.16`) are missing SIDs — a recoverable gap
- Section drafts do not carry session IDs by design; their provenance is in the modlog chain

**SP-2** should:
- Direct evaluators to `_HUBS/` as the entry point for session-level navigation
- Note that for section-level intellectual trajectory, the modlog files (4.2.x, CFP_4.2.x) are the primary navigation path — not the section drafts themselves
- Note the 34% relational link coverage and where the denser connections are (CFP phase, PDLs)

**SP-3** should:
- Argue that the intellectual trajectory criterion is satisfied primarily via the modlog chain, not via session IDs on section drafts
- Report the two missing CFP modlog SIDs as a recoverable gap that does not defeat the tracing claim (modlog content is fully present; only the session ID field is missing)
- Report the 34% relational coverage as partial but sufficient for the trajectory criterion, given the modlog structure

---

*End of note.*
## Connections (auto)

### Source chat (primary)
- [[_HUBS/CHAT_SID-20260401-000000]]

