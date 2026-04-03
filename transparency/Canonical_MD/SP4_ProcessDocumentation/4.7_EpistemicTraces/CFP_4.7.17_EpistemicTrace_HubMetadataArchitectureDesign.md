---
project: JPEP
document_type: Type 2 - Epistemic Trace
label: CFP_4.7.17_EpistemicTrace_HubMetadataArchitectureDesign
title: "Epistemic Trace: Hub Metadata Architecture Design"
branch: cfp-ai-ethics-inquiry
date_created: 2026-04-03
source_conversation: "SID-20260403-154700 (pending export; next session after JPEP_20260403_133025.md)"
status: Complete
relevance: SP-3 (the documentation architecture this trace describes is what SP-3 must narrate)
related:
  - CFP_5.3.16_Note_HubMetadataArchitectureDecisions.md (decision record produced from this trace)
  - CFP_5.3.13_Note_SP3_WriterBriefing.md
  - CFP_5.3.15_Note_OriginStoryForSP3.md
  - hub_annotations.yaml (SCRIPTS/)
  - CFP_5.2.4_pdl_SP1_SP2_SP3.md
---

# Epistemic Trace: Hub Metadata Architecture Design

## Context

This trace documents a design discussion that arose during session-start work
(mhc-start) on 2026-04-03, before SP-3 drafting commenced. The question was
prompted by the observation that hub `.md` files contain manually-inserted
information (prior_chat links, session metadata, chain corrections) that an
unconditional script run would destroy.

## The triggering observation

The hub-generation script (`obsidian_connections_with_chat_hubs.py`) uses
`p.write_text()` — unconditional overwrite. No merge, no check for existing
content, no reading of `hub_annotations.yaml`. Running the script in its
current state would destroy all manually-inserted hub content not already
captured in the YAML (which covers only 4 sessions out of 48+).

The `prior_chat` links are the most critical exposed data: they constitute the
session chain and are not recoverable from SP4/SP5 frontmatter alone.

## The redundancy proposal

The user proposed saving manually-inserted hub data redundantly: in a "lib"
location and as metadata. Discussion clarified:

- Both `lib/` directories in the project are JS visualization libraries —
  not suitable for data storage
- "Lib" was resolved to mean: `hub_annotations.yaml` in `SCRIPTS/` (the
  durable, script-readable, structured store)
- "Metadata" was resolved to mean: hub `.md` frontmatter (human-readable,
  Obsidian-visible, but derived and overwritable)

## The levels insight

The key architectural clarification emerged from the question of whether
`prior_chat` should also be added to SP4/SP5 artifact frontmatter as a
redundancy layer.

This was rejected on a principled ground: **`prior_chat` is a session-level
fact, not an artifact-level fact.**

Artifact frontmatter already captures the correct artifact-level session
relationship: `source_chat_id` — "which session produced me?" This has a
definite answer for every artifact.

`prior_chat` — "what session preceded this session?" — belongs to the session
node, not to any individual artifact. Placing it in artifact frontmatter would:

1. Conflate two distinct levels of the provenance graph
2. Require a design decision about which artifact in a session "carries" the
   chain link (arbitrary)
3. Fail for complex flows: a session may draw on multiple prior sessions, or
   resume after consulting an export from several sessions earlier — no single
   artifact in that session cleanly represents the predecessor relationship

## The complex-flow objection

The user raised this explicitly: "for very complex flows, `prior_chat` may not
have a clear reference."

This objection generalises: it is an argument against treating session
predecessorship as a single-valued field anywhere. The correct response is not
to abandon the field but to design it as a list (`prior_chats: []`) with an
optional `note` for cases requiring qualification. This is the pattern already
used in `hub_annotations.yaml` for the origin-chain sessions (da6a830c has a
`prior_chat_note` explaining the relationship type).

## The authoritative-source decision

`hub_annotations.yaml` (in `SCRIPTS/`) is authoritative for session topology.
Hub `.md` files are derived. This assignment is stable because:

- YAML survives script runs (different directory, never written by the script)
- The script is designed (per wiring instruction in the YAML header) to read
  the YAML and override auto-generated fields before writing `.md` outputs
- Hub `.md` files are the human-readable rendering, not the source of truth

## Relevance to SP-3

SP-3 must describe the documentation system — including the session-chain
infrastructure. This design discussion is part of that infrastructure's
development. Specifically:

- The `hub_annotations.yaml` mechanism (YAML-as-ground-truth, `.md`-as-derived)
  is itself an instance of the documentation-adequacy model the paper argues for
- The levels insight (artifact-level vs. session-level facts) is an example of
  the kind of architectural thinking the transparency framework requires
- The complex-flow objection illustrates why `prior_chat` as a single field
  misrepresents the actual topology of multi-session development — relevant to
  SP-3's honest account of documentation gaps

## Also from this session

- `hub_annotations.yaml` updated: SID-20260403-154053 entry added (signifier
  for the ur-conversation import session; no separate `.md` hub file)
- Feedback memory filed: deleted hub files in git status signal successful
  UUID/SID recovery, not gaps (`feedback_deleted_hubs_not_gaps.md`)
