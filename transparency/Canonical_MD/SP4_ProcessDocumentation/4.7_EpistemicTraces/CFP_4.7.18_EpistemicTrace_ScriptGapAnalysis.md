---
project: JPEP
document_type: Type 2 - Epistemic Trace
label: CFP_4.7.18_EpistemicTrace_ScriptGapAnalysis
title: "Epistemic Trace: Hub Script Gap Analysis — What the Normalized Metadata Reveals"
date_created: 2026-04-04
session_id: SID-20260404-083911
source_conversation: ""
status: Complete
inputs:
  - obsidian_connections_with_chat_hubs.py
  - hub_annotations.yaml
  - CFP_5.3.16_Note_HubMetadataArchitectureDecisions.md
feeds_into:
  - obsidian_connections_with_chat_hubs.py
related:
  - CFP_4.2.26_ModificationLog_FrontmatterNormalization.md
  - CFP_4.7.17_EpistemicTrace_HubMetadataArchitectureDesign.md
---

# Hub Script Gap Analysis

## Triggering question

After normalizing all CFP-era frontmatter to canonical field names, the user asked: do we need YAML entries for CFP sessions, or can the script work directly from the metadata? This led to an analysis of what the script actually reads vs. what the metadata now provides.

## Finding 1: `session_id` is invisible

The script groups artifacts into session hubs by `source_chat_id` (line 591). CFP-era artifacts use `session_id` instead. The script never reads `session_id`, so every CFP artifact is invisible to the hub builder. This is why CFP hubs are auto-generated as near-empty shells — the script can't link artifacts to their sessions.

**Fix:** Fall back to `session_id` when `source_chat_id` is absent.

## Finding 2: Alias table is dead code

`V1V2_FIELD_ALIASES` (lines 51-71) defines mappings from non-standard field names to canonical names. But no function ever applies these mappings. The connection renderer (`add_rel_section`, line 233) reads frontmatter keys directly by canonical name. If an artifact has `output_completed`, it's silently ignored because the renderer looks for `outputs`.

Post-normalization this matters less (artifacts now use canonical names), but the alias table should either be wired or deleted.

## Finding 3: Key CFP fields not in REL_FIELDS

The renderer recognizes four groups of relational fields:

- `REL_FIELDS_STRONG`: `inputs`, `outputs`
- `REL_FIELDS_DERIVED`: `input_artifacts`, `influenced_artifacts`, `one_to_many_influence`
- `REL_FIELDS_CONTINUITY`: emptied this session (was `continuation_of`, `continued_by`)
- `REL_FIELDS_RELATED`: `related_documents`, `salient_outputs`

Not recognized: `derived_from`, `feeds_into`, `output_completed`, `related`. These are the most-used CFP relational fields. They exist in 40+ artifacts but are invisible to the connection renderer.

## Finding 4: YAML is only needed for what metadata can't capture

The user's question ("why do we need YAML entries?") surfaced a clean principle: `hub_annotations.yaml` exists for information that is NOT encapsulated in artifact frontmatter. For v1/v2 sessions, that's almost everything (dates, models, chain links, roles). For CFP sessions, frontmatter is rich — YAML is only needed for:

- `continues_from` (session predecessor — a session-level fact, not artifact-level; per CFP_5.3.16)
- `role` / `note` (session narrative — not derivable from artifact metadata)
- Information about sessions that produced no artifacts

Everything else (date, model, inputs, artifacts_produced) can be aggregated from artifact frontmatter by the script.

## Finding 5: Three edge types, not two

User clarified that `inputs` is empirical ("what entered the context window"), not structural. This distinguishes:

- **Empirical provenance:** `inputs` (context window contents), `output_completed` (what was produced)
- **Structural version chain:** `derived_from` (this is v2 of v1)
- **Structural dependency:** `feeds_into` (this will be used by X)

`derived_from` should NOT be folded into `inputs` — a prior version may not have been loaded into the context window. The distinction is between "what I was built from as material" and "what I am a new version of."

## Recommended script changes

1. Read `session_id` as fallback for `source_chat_id` — makes CFP artifacts visible
2. Add `derived_from` and `feeds_into` as new REL_FIELDS categories (distinct sections in connection blocks)
3. Add `output_completed` and `related` to existing REL_FIELDS groups
4. Aggregate artifact-level date/model/inputs onto hub pages for sessions without YAML
5. Either wire the alias table or remove it (currently misleading — looks functional but isn't)
