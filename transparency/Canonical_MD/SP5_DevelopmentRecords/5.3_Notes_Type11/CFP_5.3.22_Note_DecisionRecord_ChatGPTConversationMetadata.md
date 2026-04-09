---
project: JPEP
document_type: decision_record
label: CFP_5.3.22_Note_DecisionRecord_ChatGPTConversationMetadata
title: "Decision Record: ChatGPT v1/v2 conversation metadata design"
created: 2026-04-09
session_id: SID-20260409-115329
status: Complete
related:
  - 4.7.7.1_IsThisAISlop_1.md
  - 4.7.7.2_IsThisAISlop_2.md
  - 4.7.7.3_IsThisAISlop_3.md
  - 4.7.2_OriginalTextConversation_VisibilityAndStakeholders.md
  - 4.2.11_ModificationLog_Appendix.md
  - 4.2.12_ModificationLog_Titles.md
  - CFP_5.3.1_WorkPlan_CFP_Adaptation.md (manifest planned item)
  - transparency/SCRIPTS/build_graph.py
---

# Decision Record: ChatGPT v1/v2 conversation metadata design

Decided in session SID-20260409-115329 during graph audit completion.

---

## Context

Six ChatGPT conversations from the v1/v2 phase were imported in SID-20260409-093405 into
`06_conversations/imported/` as local Markdown files with MHC-W frontmatter. This session
resolved how to reference them in artifact metadata and in the graph.

---

## Decisions

### 1. UUID is the stable identifier — already correct

The `source_chat_id` in v1/v2 artifacts (e.g. `4.7.7.1`) uses the conversation UUID from
the `/c/<uuid>` part of the ChatGPT URL (e.g. `68f36a62-0ce8-8328-a3ed-d5c08c1b6791`).
This is the stable identifier. The project/GPT ID part of the URL
(`g-p-6960e68761108191967500de8cb7f87d-jpep`) is unstable and is not used as an identifier.

This correspondence already held before this session: the UUID in `source_chat_id` matches
the `conversation_id` in the downloaded JSON and the UUID prefix in the imported filename.
No changes were needed.

### 2. Double-field convention for ChatGPT artifacts

Both fields are kept in artifacts that reference ChatGPT v1/v2 conversations:

- `source_chat_id`: conversation UUID — the stable identifier; used by the graph as the
  join key to create hub stubs; used locally to find the imported file by grep.
- `source_chat_link`: full chatgpt.com URL — for direct web access while the author has
  platform access. Serves a different purpose from the UUID; both are worth keeping.

No `source_chat_file` field is added to individual artifacts. The UUID is sufficient for
local discovery (see §3).

### 3. Local file discovery without the manifest

Given only the UUID, the author can find the local imported file by:

1. Grepping for the UUID in `06_conversations/imported/` — the imported file has the full
   UUID in its `source_chat_id` frontmatter field.
2. OR searching filenames for the first 8 characters of the UUID — the imported files are
   named `chatgpt.com_<first-8-chars>_<name>.md`.

The manifest is not required for local discovery. The UUID + grep is sufficient.

### 4. Manifest role (planned — CFP_5.3.1 §Remaining work)

The manifest (`CFP_5.3.N_Note_RawConversationsManifest.md`, tracked in Canonical_MD/) serves
three distinct purposes:

1. **Public visibility**: tells readers who don't have the author's disk that local files
   exist and what they contain at a high level.
2. **Graph enrichment**: the graph builder (`build_graph.py`) reads the manifest and upgrades
   anonymous UUID stubs to named conversation nodes (name, platform, date, local path in
   tooltip). Requires ~45-line enrichment pass in `build_graph.py`. No field changes in
   artifacts.
3. **SP-3 policy anchor**: formal declaration of the "conversations retained locally,
   available on request" policy.

The manifest maps UUID → local file path + URL. It is the public bridge between the UUID
reference in artifacts and the gitignored local files.

### 5. Gitignore policy unchanged

`06_conversations/` remains gitignored. The author holds all local files. "Available on
request" policy holds. Un-gitignoring `06_conversations/imported/` is not necessary because
the UUID-grep path always works for the author, and the manifest provides public visibility
for everyone else.

### 6. Graph design (deferred until manifest is created)

Current state: `source_chat_id` with a ChatGPT UUID creates an anonymous hub stub in the
graph (amber dot, UUID label). This is correct but uninformative.

Future state (after manifest): ~45-line enrichment pass upgrades stubs to named
`imported_conversation` nodes. No field changes in any artifact. The parser's chatgpt.com
URL extractor is not needed — UUID-based stubs + manifest enrichment is the mechanism.

### 7. v1/v2 Claude.ai conversations (out of scope here)

Different situation: some have hub files in `_HUBS/CHAT_<uuid>.md` (locally anchored),
some remain web-only references. Not addressed by this decision record.

---

## What was done in this session

- Added `source_chat_link` to `4.7.7.1`, `4.7.7.2`, `4.7.7.3` (confirmed: keep, not revert)
- Confirmed `source_chat_id` fields in all 6 referencing artifacts were already correct
- Confirmed imported files in `06_conversations/imported/` already have correct frontmatter
- Confirmed no `source_chat_file` field needed

---

## Open

- Create manifest (CFP_5.3.1 §Remaining work item)
- Extend `build_graph.py` with manifest enrichment pass (~45 lines) at that point
