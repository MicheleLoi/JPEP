---
project: JPEP
document_type: Type 11 - Steering Note
label: CFP_5.3.3_Note_MetadataReportingStructure
title: "Metadata Reporting Structure: Phases, Limitations, and Relevance for SP-1/2/3 Rewrite"
date_created: 2026-03-31
status: Active
session_id: SID-20260331-000000
session_id_precision: date-only
inputs:
  - CFP_5.3.1_WorkPlan_CFP_Adaptation.md
source: "Claude Sonnet 4.6 (Claude Code session) + user direction"
relevance_for:
  - SP-1 rewrite (AI use declaration)
  - SP-2 rewrite (navigation document)
  - SP-3 rewrite (documentation adequacy account)
related:
  - "CFP_5.3.1_WorkPlan_CFP_Adaptation.md (master work plan)"
  - "CFP_5.4.9_Section7_v1.md (Section 7 — adequacy criteria)"
  - "transparency/Canonical_MD/obsidian_connections_with_chat_hubs.py (hub script)"
  - "transparency/Canonical_MD/_HUBS/ (generated hub nodes)"
---
# Metadata Reporting Structure: Phases, Limitations, and Relevance for SP-1/2/3 Rewrite

## Note to AI reader

If you are an AI agent responsible for rewriting SP-1, SP-2, or SP-3, this document is written for you. It explains: (a) how the process documentation metadata is structured; (b) how that structure varies across the phases of this project; (c) what the limitations are and how they are documented; and (d) what this means concretely for each of the three supplementary packages you are rewriting.

Read this document before reading any SP draft. It provides the factual basis for claims about documentation coverage that SP-3 must make honestly.

---

## 1. Structure of the reporting mechanism

The metadata embedded in SP-4 artifact frontmatter is the machine-readable layer of process documentation. It operates at three levels:

**Level 1 — Session identity.** Every artifact ideally records which AI session produced it. The field name and format vary by phase (see Section 2). The hub script (`obsidian_connections_with_chat_hubs.py`) reads these fields and generates hub nodes in `_HUBS/` — one hub per session, with all artifacts from that session as spokes. The hub graph is the primary navigational entry point into SP-4 for an evaluator following the intellectual trajectory criterion (Section 7.2).

**Level 2 — Artifact identity.** Each artifact records: document type (modification log, epistemic trace, section draft, etc.), date created, model used, and the phase/section it belongs to. This enables evaluators to understand what kind of epistemic work the artifact represents.

**Level 3 — Relational links.** Fields including `inputs`, `outputs`, `influenced_artifacts`, `feeds_into`, `related_documents`, `output_completed`, and others record what each artifact consumed and produced. These are directed edges connecting artifacts across sessions into a processual chain. Coverage is uneven (see Section 3).

These three levels together are meant to support the three adequacy criteria Section 7 specifies: attribution (Level 2), intellectual trajectory (Levels 1 + 3), and understanding-and-endorsement (Level 3, especially modification logs).

---

## 2. What changes across phases

The project used different tools at different stages. This created genuine variation in metadata completeness. The variation is a fact to be documented, not a deficiency to be concealed.

### Phase v1/v2 — Claude.ai web (Oct 2025 – Jan 2026)

**Tool:** Claude Sonnet 4.5 via claude.ai web interface. Occasional ChatGPT sessions for external review (identifiable by `participants` field or former `c/` UUID prefix, now stripped).

**Session identity field:** `source_chat_id` with UUID (e.g. `34b5c72a-899f-42fc-8d44-8f81b8393c5a`). Assigned by Claude.ai. Reliable, exact, unique per conversation.

**Hub coverage:** 34 hubs, 62 files. Well-populated. The UUID is the skeleton.

**Relational metadata:** Sparse. Most artifacts in this phase do not have structured input/output links. Relational information exists in artifact bodies and modification logs but is not uniformly encoded in frontmatter.

**Information limit:** None on session identity. Relational links partially recoverable but not systematically encoded.

---

### Phase III — Early Claude Code (Jan – Mar 2026)

**Tool:** Claude Code (pre-MHC-W SID system, before v3.36). Conversations were exported but not linked to artifacts via frontmatter at creation time.

**Session identity field:** None recorded at creation. Retroactive reconstruction is possible via: (a) `date_created` fields present on all 12 III_ artifacts; (b) content matching — exported conversation files in `06_conversations/exported/` reference III_ artifact IDs in their body text.

**Retroactive convention:** `session_id: SID-YYYYMMDD-000000` with `session_id_precision: date-only`. The time component (000000) is an explicit placeholder. The epistemic limitation is documented here and in SP-3; it is not encoded per-artifact to avoid cluttering frontmatter.

**Hub coverage:** Currently 0 (orphaned). Will be covered once retroactive SIDs are written and the hub script is extended to read `session_id`.

**12 files affected:**
- III_4.7.1 (date: 2026-01-24)
- III_4.7.2, III_4.4.4, III_4.4.5, III_5.2.1, III_5.3.5 (date: 2026-01-26)
- III_4.4.5 updated, III_5.4.1 (date: 2026-01-28)
- III_5.3.6 (date: 2026-03-01)
- III_4.7.3, III_4.7.4, III_5.4.2 (date: 2026-03-02)

**Information limit:** Session identity is date-approximate. Time of session within the day is unknown. No conversation export exists for January 2026 sessions (the export system was not yet active). Matching to conversation files is possible for March 2026 III_ artifacts (exports exist from 2026-02-02 onward).

---

### Phase CFP — Claude Code with MHC-W SID system (Mar 2026 – present)

**Tool:** Claude Code with full MHC-W infrastructure (v3.36+, SID system introduced 2026-03-11).

**Session identity field:** `session_id: SID-YYYYMMDD-HHMMSS`. Generated at session start, written to `.mhc-config.json`, embedded in artifact templates. Precise to the second.

**Conversation exports:** Systematic. Named `JPEP_YYYYMMDD_HHMMSS.md`, stored in `06_conversations/exported/`. 18 exports exist as of 2026-03-31.

**Hub coverage:** 14 artifacts with full SIDs. Hub script extension to read `session_id` is pending — once implemented, these will generate SID-based hub nodes.

**Relational metadata:** Richer than earlier phases. Modification logs have `related_documents`. Section drafts have `source_guidance`. PDLs have `source_conversations`.

**Information limit:** None on session identity. Hub coverage pending script update. Relational links still partially in free text rather than structured frontmatter.

---

### Summary table

| Phase | Tool | Session ID field | Precision | Hub coverage | Relational links |
|---|---|---|---|---|---|
| v1/v2 | Claude.ai web | `source_chat_id` (UUID) | Exact | ✓ 34 hubs, 62 files | Sparse |
| v1/v2 occasional | ChatGPT web | `source_chat_id` (UUID, was c/-prefixed) | Exact | ✓ included above | Sparse |
| III | Claude Code (early) | None → `session_id` (reconstructed) | Date only | ✗ pending | Sparse |
| CFP | Claude Code + MHC-W | `session_id` (SID-HHMMSS) | Exact | ✗ pending script update | Richer |

---

## 3. Summary statistics relevant to Section 7 adequacy criteria

Section 7 organizes documentation adequacy assessment around three criteria. The following statistics operationalize each. These are the figures SP-3 should report and SP-2 should make navigable.

**Attribution** — can evaluators locate human contribution?
- Total SP-4 artifacts: ~128 files
- Artifacts with identified session (any phase, including reconstructed): target ~74 (62 v1/v2 + 12 III retroactive) + 14 CFP = ~88 once script updated
- Artifacts with identified model: ~50 (from `model` / `source_chat_model` fields)
- Sessions with multiple artifacts (hub density ≥ 2): indicates substantive documented work per session

**Intellectual trajectory** — can evaluators follow how the work developed?
- Artifacts with at least one resolved input/output link: ~25 of 128 (see relational audit in CFP_5.3.3 context)
- Section drafts with multiple versions (v1 → v2 → v3): Introduction, Section 2, Section 3, Section 6 — each version is a trajectory node
- Modification log entries per section: quantifies revision depth
- Conversation exports: 18 sessions documented in `06_conversations/exported/`; temporal span Oct 2025 – Mar 2026

**Understanding-and-endorsement** — is authorial judgment evidenced?
- Modification log entries with explicit user revision instructions: countable from 4.2.x files
- Reviewer B assessments that led to revision: documented in CFP_4.2.14 through CFP_4.2.19
- Epistemic traces documenting analytical sessions: 4.7.1 through 4.7.7 + CFP_4.7.5 through CFP_4.7.7

**Coverage honesty** — the honest accounting Section 7 requires:
- % of artifacts with exact session ID: v1/v2 + CFP phases (~76 files once pending updates complete)
- % with date-approximate session ID: III phase (12 files)
- % genuinely orphaned: residual after both above — should approach 0 after retroactive III work

These statistics do not prove adequacy. They give evaluators a quantitative entry point into the tracing question Section 7 poses.

---

## 4. Implications for SP-1, SP-2, SP-3

### SP-1 (AI use declaration)

SP-1 declares what AI tools were used and in what capacity. It should:
- List the three phases and their tools (Claude.ai web, early Claude Code, Claude Code + MHC-W)
- Acknowledge the phase variation in metadata precision — specifically that III_ phase session identity is date-approximate and time is unknown
- State that the epistemic limitation is documented in this note and in SP-3, and that it does not affect artifact content, only session-level traceability

SP-1 should not claim uniform precision it does not have.

### SP-2 (Navigation document)

SP-2 guides evaluators into SP-4. It should:
- Direct evaluators to `transparency/Canonical_MD/_HUBS/` as the primary entry point for session-level navigation
- Explain the two hub types: UUID hubs (v1/v2, exact) and SID hubs (CFP, exact; III, date-approximate)
- Note that relational links (inputs/outputs) are encoded in artifact frontmatter and rendered in each artifact's `## Connections (auto)` block — the hub script generates these automatically
- Provide the summary statistics from Section 3 above as orientation before evaluators dive into individual artifacts

### SP-3 (Documentation adequacy account)

SP-3 makes the author's case that the tracing condition is satisfied. It should:
- Use the three-criteria structure from Section 7 as its organizing framework
- Report the summary statistics honestly, including the coverage limitations
- Argue that the III_ phase limitation (date-approximate session IDs, no conversation exports for January sessions) does not defeat the tracing claim for those artifacts, because: (a) artifact content and type are fully documented; (b) their relationship to other artifacts is partially recoverable via input/output links and modification logs; (c) the limitation is acknowledged rather than concealed
- Note that the self-regulated learning parallel (Section 7.4, Addition B) applies to this documentation system itself: the metacognitive overhead of maintaining SP-4 is not mere compliance — it is what constitutes genuine intellectual engagement with the AI-assisted process

---

## 5. Reconstruction method for III_ session IDs

This section documents how the retroactive `session_id` fields in III_ files were derived. This information does not appear in artifact frontmatter — it is recorded here only, as the per-artifact convention was decided to be minimal (`session_id` + `session_id_precision` only).

### Method

Two evidence sources were used in combination:

**Primary — content matching:** Each conversation export file in `06_conversations/exported/` was scanned for mentions of III_ artifact IDs (e.g. `4.7.3`, `5.4.1`) and stems (e.g. `III_4.7.3`). A match means the artifact was discussed or produced in that session.

**Secondary — date proximity:** The artifact's `date_created` field was compared to the conversation file timestamp (`JPEP_YYYYMMDD_HHMMSS.md`). A conversation within ~7 days of the artifact date was treated as a candidate.

**Decision rules:**
1. If a conversation export mentions the artifact AND its timestamp is close to `date_created`: use the conversation timestamp. `session_id_precision: exact`.
2. If multiple conversation exports match: prefer the one closest in date to `date_created`.
3. If no conversation export exists for the artifact's date (January 2026 files — no exports before 2026-02-02): use `date_created` with 000000 time placeholder. `session_id_precision: date-only`.

### Per-artifact reconstruction record

| File | date_created | session_id | precision | confirmed by |
|---|---|---|---|---|
| III_4.7.1 | 2026-01-24 | SID-20260124-000000 | date-only | date only (no Jan exports) |
| III_4.7.2 | 2026-01-26 | SID-20260202-115248 | exact | JPEP_20260202_115248.md |
| III_4.4.4 | 2026-01-26 | SID-20260202-115248 | exact | JPEP_20260202_115248.md |
| III_4.4.5 | 2026-01-26 | SID-20260202-115248 | exact | JPEP_20260202_115248.md |
| III_5.2.1 | 2026-01-26 | SID-20260202-115248 | exact | JPEP_20260202_115248.md |
| III_5.3.5 | 2026-01-26 | SID-20260126-000000 | date-only | date only (no Jan exports) |
| III_5.4.1 | 2026-01-28 | SID-20260202-115248 | exact | JPEP_20260202_115248.md |
| III_5.3.6 | 2026-03-01 | SID-20260303-102634 | exact | JPEP_20260303_102634.md |
| III_4.7.3 | 2026-03-02 | SID-20260302-152952 | exact | JPEP_20260302_152952.md |
| III_4.7.4 | 2026-03-02 | SID-20260302-190708 | exact | JPEP_20260302_190708.md |
| III_5.4.2 | 2026-03-02 | SID-20260302-152952 | exact | JPEP_20260302_152952.md |

### What this does NOT record

- The full text of matches found in conversation files (not reproduced here — consult the conversation exports directly)
- The time of day within a session (unknown for date-only entries)
- Whether the artifact was *created* in the session or merely *referenced* (the distinction is recoverable from conversation content but not encoded in metadata)

---

*End of note.*
## Connections (auto)

### Source chat (primary)
- [[_HUBS/CHAT_SID-20260331-000000]]

