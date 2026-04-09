---
project: JPEP
document_type: Type 12 - Section Draft
label: CFP_5.4.13_SP1
section: "SP-1 — AI Usage Declaration and Archive Orientation"
version: v1
date_created: 2026-04-09
status: Draft
source: "Claude Sonnet 4.6 (Claude Code session)"
session_id: SID-20260409-150705
produced_by_prompt: ""
inputs:
  - CFP_5.4.11_SP3.md
  - CFP_5.4.9_Section7_v3.md
  - CFP_5.2.4_pdl_SP1_SP2_SP3.md (PDL-005)
cfp_target: "AI Tools in Ethics Research (topical collection)"
versioning_convention: git_inplace
word_count: ~700
pending:
  - "Part 2 / Documentation conventions: branch merge sentence written in future tense as of 2026-04-09. Update to past tense and remove inline marker when cfp-ai-ethics-inquiry is merged into main."
---

# SP-1 — AI Usage Declaration and Archive Orientation

## Part 1 — AI Usage Declaration

This paper was written with AI assistance throughout. The following records the models used, the platforms on which they ran, the roles AI played, and the role the human author played across the project.

### Models and platforms

| Phase | Period | Platform | Models |
|-------|--------|----------|--------|
| v1/v2 | Oct–Nov 2025 | Claude.ai web | Claude Sonnet 4.5 |
| v1/v2 | Oct–Nov 2025 | ChatGPT | GPT-5 Thinking (paper evaluation; SVG/figure generation) |
| Stage III | Jan–Mar 2026 | Claude Code | Claude Opus 4.5; Claude Sonnet 4.6 |
| CFP | Mar–Apr 2026 | Claude Code | Claude Sonnet 4.6; Claude Opus 4.6 |

Model identity was constant within a session and is recorded in session-level metadata. In Stage III, the author switched from Opus 4.5 to Sonnet 4.6 between two attempts at the same task; the decision and its timing are recorded in the relevant modification log (`III_4.2.13`). In the CFP phase, model selection was explicit and per-task: Sonnet 4.6 for drafting and light revision, Opus 4.6 for deep review, corpus analysis, and sessions requiring extended reasoning.

### Roles

**v1/v2 phase.** AI acted as section drafter (prompted and directed by the author), modification log author (producing modlog entries which the author reviewed and accepted), pattern summary author (distilling methodological lessons from each session's modlogs for handoff to the next session), and contributor to the artifact ontology (naming categories in response to the author's organizational decisions). All artifacts were produced inside chat sessions; the author reviewed, accepted, or rejected each output before it entered the archive.

**Stage III.** AI continued as drafter and modlog author. Additionally, AI operated within Claude Code, which introduced session IDs and automated some infrastructure. The workflow tooling that became MHC-W was being built in parallel with the writing it supported; Stage III sessions tolerated the resulting inconsistencies, which were resolved retrospectively in the CFP phase.

**CFP phase.** AI acted as drafter, Reviewer B (Claude Opus 4.6 acting as a critical reviewer rather than a co-writer, in dialogue with the author as Reviewer A), modification log author, and automated metadata handler. SessionEnd hooks captured every Claude Code session as a conversation file. All substantive decisions — what to draft, what to revise, what to accept or reject, what to cut — remained with the author.

### Human author's role

The human author was the project's continuous agent across all three phases. Specifically: directing what was written and in what order; authoring and revising all section guidance documents; selecting models for each task; reviewing and endorsing all outputs before they entered the archive; making all structural decisions (section consolidation, the SP reconception, the redundancy pass, the elimination of the appendix); conducting and directing the retrospective philological work that recovered the v1/v2 chain. The documentation system exists to make this role traceable. SP-3 is the document that argues, from the archive, that the tracing claim is satisfied.

---

## Part 2 — Archive Orientation

The supplementary materials span five packages (SP-1 through SP-5). This part orients a reader who is about to navigate them.

### The three phases

The project has three distinct phases, differing in platform, tooling, and what each made possible. Artifact file name prefixes encode phase:

| Prefix | Phase | Period | Platform |
|--------|-------|--------|----------|
| *(plain number or II_)* | v1/v2 | Oct–Nov 2025 | Claude.ai web |
| `III_` | Stage III | Jan–Mar 2026 | Claude Code |
| `CFP_` | CFP adaptation | Mar–Apr 2026 | Claude Code |

SP-3 Part I describes each phase in detail.

### Session identification

Every Claude Code session (Stage III and CFP) has a session ID of the form `SID-YYYYMMDD-HHMMSS`. Artifacts carry their session ID in frontmatter. v1/v2 artifacts carry a chat UUID in place of a session ID; several UUIDs were recovered retrospectively during the CFP-phase philological sessions.

The authoritative record of session topology — which session followed which, what each session took as input and produced as output — is `hub_annotations.yaml` in `transparency/SCRIPTS/`. SP-2 §4 describes the hub system.

### Documentation conventions

v1/v2 artifacts were authored by hand inside chat sessions and extracted manually into the archive. Stage III introduced session IDs and Claude Code tooling. CFP added automated frontmatter, hub annotations, and conversation file exports via SessionEnd hook. A frontmatter normalization pass in early April 2026 (`CFP_4.2.26`) brought the entire archive into uniform field conventions.

The CFP adaptation was developed on branch `cfp-ai-ethics-inquiry` [to be merged into `main` before submission — update tense when done]. The full commit history of the branch is preserved in git.

### Entry points

| Package | What it contains | Start here if you want to… |
|---------|-----------------|---------------------------|
| SP-2 | Document type ontology, metadata infrastructure, file inventories | Understand the archive's architecture or locate a specific artifact |
| SP-3 | Documentation adequacy account: three-phase narrative, Section 6 worked example, adequacy argument | Assess whether the record satisfies the Section 7 criteria |
| SP-4 | Process documentation (Types 1–7): complete prompt, modification logs, epistemic traces, section guidance, pattern summaries | Read the primary-source documentation of how the paper was written |
| SP-5 | Development records (Types 8, 11, 12): prompt development logs, notes, section drafts | Read the prompt development decisions or working notes |

The conversation layer (`06_conversations/`) is described in SP-2 §7.

---

*SP-1 — SID-20260409-150705.*
