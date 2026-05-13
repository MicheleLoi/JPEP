---
project: JPEP
document_type: Type 11 - Steering Note / Decision Record
label: CFP_5.3.16_Note_HubMetadataArchitectureDecisions
title: "Hub Metadata Architecture: Decision Record"
branch: cfp-ai-ethics-inquiry
date_created: 2026-04-03
status: Active — authoritative governance document for hub system
source_conversation: "SID-20260403-154700 — direct turn-by-turn export of this session was never generated (export pipeline gap). The session's content is integrated in JPEP_20260403_193831.md (the successor session, started 19:38 same day), which references SID-20260403-154700 by name 5 times and summarises the architecture decision recorded here. Rollup confirmed in SID-20260513-094035 audit; see CFP_5.3.30 §3.1."
inputs:
  - CFP_4.7.17_EpistemicTrace_HubMetadataArchitectureDesign.md
  - hub_annotations.yaml
related:
  - CFP_4.7.17_EpistemicTrace_HubMetadataArchitectureDesign.md (reasoning trace)
  - hub_annotations.yaml (SCRIPTS/) — the authoritative data store this document governs
  - obsidian_connections_with_chat_hubs.py (SCRIPTS/) — the script this document constrains
  - CFP_5.3.13_Note_SP3_WriterBriefing.md
---

# Hub Metadata Architecture: Decision Record

## Governing principle

Hub `.md` files are **derived artifacts**. `hub_annotations.yaml` is the
**authoritative source** for session-level metadata that cannot be inferred
from SP4/SP5 frontmatter alone.

Do not treat hub `.md` content as ground truth. If hub `.md` and
`hub_annotations.yaml` disagree, the YAML is correct.

---

## Where each type of information lives

| Information | Field | Location | Authoritative |
|---|---|---|---|
| Which session produced an artifact | `source_chat_id` | SP4/SP5 artifact frontmatter | Yes — artifact level |
| Session title, date, model, platform | various | `hub_annotations.yaml` | Yes |
| Session predecessor(s) | `continues_from: []` | `hub_annotations.yaml` | Yes |
| Session predecessor (complex flows) | `continues_from_note` | `hub_annotations.yaml` | Yes |
| Inputs received by a session | `inputs: []` | `hub_annotations.yaml` | Yes |
| Artifacts produced by a session | `artifacts_produced: []` | `hub_annotations.yaml` | Yes |
| Gitignore / import status | `gitignored`, `import_file` | `hub_annotations.yaml` | Yes |
| Session role / narrative | `role` or `note` | `hub_annotations.yaml` | Yes |
| Human-readable rendering of all above | hub `.md` body + frontmatter | `_HUBS/CHAT_*.md` | No — derived |

---

## What does NOT belong in artifact frontmatter

`continues_from` / `continues_from` must **not** be added to SP4/SP5 artifact
frontmatter. Reason: predecessor-session is a session-level fact, not an
artifact-level fact. Artifact frontmatter already captures the correct
artifact-level relationship (`source_chat_id`). Adding session topology to
artifact frontmatter would:

- Conflate two distinct provenance levels
- Require an arbitrary choice of which artifact in a session "carries" the link
- Misrepresent complex flows where a session has multiple or non-linear
  predecessors

---

## Complex flows

For sessions with non-linear predecessors (resumptions, parallel tracks,
sessions that drew on exports from multiple prior sessions), use:

```yaml
continues_from:
  - UUID-or-SID-1
  - UUID-or-SID-2
continues_from_note: >
  [Explanation of the relationship — e.g., "this session resumed after user
  read the export from SID-X and incorporated findings from SID-Y"]
```

A single-valued `continues_from` field is acceptable only when the predecessor
relationship is unambiguous and singular.

---

## Script safety rule

**Do not run `obsidian_connections_with_chat_hubs.py` until it is wired to
read `hub_annotations.yaml`.**

Current script behaviour: `p.write_text()` — unconditional overwrite. Running
it now destroys all manually-inserted hub content for sessions not yet in the
YAML (48+ hub files; YAML currently covers 4 sessions + 1 signifier entry).

Before running the script:
1. Expand `hub_annotations.yaml` to cover all sessions with manually-set values
2. Wire the script to read YAML and merge/override before writing `.md` outputs
3. Or add a `--no-overwrite` flag as a short-term safety measure

---

## Hub signifier pattern

For sessions where the YAML entry itself is the definitive record (no separate
`.md` hub file needed), add a `signifier_for` field:

```yaml
SID-20260403-154053:
  signifier_for: 6c8d9101-cd3f-4f61-aaf9-f293de92d11c
  signifier_note: >
    [Explanation of why this session is the hub signifier for the target session]
```

Currently used for: SID-20260403-154053 (ur-conversation import session).
