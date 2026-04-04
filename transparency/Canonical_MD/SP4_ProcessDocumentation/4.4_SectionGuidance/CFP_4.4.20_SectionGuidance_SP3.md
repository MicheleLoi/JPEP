---
artifact_type: section_guidance
document_type: Type 4 - Section Guidance
label: CFP_4.4.20_SectionGuidance_SP3
project: JPEP CFP Adaptation
version: v4
date: 2026-04-03
session_id: SID-20260403-213917
source_conversation: SID-20260403-213917
inputs:
  - "CFP_5.2.4_pdl_SP1_SP2_SP3.md (PDL-004 through PDL-019)"
  - "CFP_5.3.13_Note_SP3_WriterBriefing.md (research findings — read first)"
  - "CFP_5.3.15_Note_OriginStoryForSP3.md (origin layer narrative)"
  - "CFP_5.3.17_Note_PreliminaryChat_ChainVerification.md (PreliminaryChat chain)"
  - "CFP_4.7.13_EpistemicTrace_SP3DesignBrainstorm.md"
  - "CFP_4.7.14_EpistemicTrace_SP3VisualDesign.md"
  - "CFP_4.7.8_EpistemicTrace_SelfReferentialDocumentation.md"
  - "CFP_5.3.7_SelectedGraphCandidates.md"
  - "CFP_5.3.1_WorkPlan_CFP_Adaptation.md"
  - "III_4.7.3_MHC_Tracing_SP_Reconception.md"
  - "CFP_5.2.2_pdl_appendix_v3.md"
output_file: ""
validated: ""
validation: ""
supersedes: "CFP_4.4.20_SectionGuidance_SP3.md v3 (2026-04-03, research-paper structure without chain walk findings)"
---

# Section Guidance: SP-3 — Documentation Account

---

## Purpose Statement

SP-3 is a research paper in its own right — a dissertation-chapter-length study that uses the JPEP documentation archive as its primary source.

**Research question:** What role did the human author play in JPEP, and how did that role evolve as a function of the changing technological infrastructure?

**Connection to the paper body:** Section 3 of the paper argues that the way philosophy is produced — and with it the role of the author — is changing. SP-3 is a case study: the first-person, documented account of what that change looked like from the inside. An older version of the paper also traced how the interaction itself evolved — from prompting and refining outputs, to designing documentation architectures and methodology. SP-3 should trace this evolution as part of its research narrative.

**What SP-3 is not:** SP-3 is not a document-type index (SP-2 handles that), not a high-level AI-usage declaration (SP-1 handles that), and not a defence of the record against anticipated objections. SP-3 is research: it reads the archive, reports what it finds, and interprets it.

---

## Methodology

### Approach: philological, with digital humanities tools

The methodology is philological. The drafter treats the JPEP documentation archive as a primary source corpus and applies the methods of textual scholarship: systematic reading, structured note-taking, hypothesis generation from internal evidence, cross-referencing across documents. Digital humanities tools — sub-agents for parallel reading, metadata extraction scripts, graph visualizations — assist the philological work but do not replace it.

### Two evidence sources — artifacts and conversations

Artifacts and conversations are complementary evidence sources with different strengths. **Artifacts** preserve structure, scope, encoded reasoning, and sibling relationships (via `source_chat_id` and hub files). **Conversations** preserve agency attribution, provenance chains, and the interactional dynamics of human-AI collaboration. Neither alone is sufficient for the adequacy argument. The chain walk (CFP_5.3.13 §10) demonstrated this concretely: artifact-based reconstruction recovered scope, date, and reasoning for session e5ec43be — but only the conversation confirmed who initiated the reading, and only conversation access revealed 4.1's true provenance (human-sourced, Claude-synthesized, human-endorsed). SP-3 should present both evidence types and be explicit about which claims rest on which source.

### Full corpus reading requirement

The drafter must read **every single document** in the v1/v2 and Stage III corpus within SP4 and SP5, without exception. This completeness is itself a methodological commitment: it is what distinguishes philological research from cherry-picking.

**Corpus scope — v1/v2 and Stage III only:**
- `transparency/Canonical_MD/SP4_ProcessDocumentation/` — all subdirectories: 4.1 (Complete Prompts), 4.2 (Modification Logs), 4.3 (Pattern Summaries), 4.4 (Section Guidance), 4.5 (Section Summaries), 4.6 (Reference Logs), 4.7 (Epistemic Traces)
- `transparency/Canonical_MD/SP5_DevelopmentRecords/` — all subdirectories: 5.1 (Paper Prompt Development Log), 5.2 (Section Prompt Development Logs), 5.3 (Notes), 5.4 (Section Drafts)
- `transparency/Canonical_MD/_HUBS/` — session hub files for v1/v2 and Stage III sessions

**Within each directory, include:** files with no phase prefix (v1/v2 baseline), files prefixed `II_`, and files prefixed `III_`.

**Exclude:** files prefixed `CFP_`. The CFP adaptation is still in development — the CFP corpus is not yet a stable object of philological study. Philological analysis requires a completed corpus; analyzing documents that are still being written or revised would violate the methodological standard the drafter is committed to. CFP-era hub files in `_HUBS/` are likewise excluded.

No document within the included scope may be skipped. No subdirectory may be sampled.

### Sub-agents

The drafter may — and should — spawn sub-agents (Sonnet or Haiku) to assist with systematic reading and note-taking across the corpus. The corpus is large enough that a single reading pass without sub-agent support would be impractical.

### Note-taking protocol

For each document read, the drafter records at minimum:
- **Artifact ID** (filename)
- **Type** (modification log, epistemic trace, PDL, section draft, hub, etc.)
- **Phase** (v1/v2 or Stage III)
- **Key content** (what the document records)
- **Relevance to the research question** (what it shows about the human author's role and/or how that role was shaped by the technological infrastructure)

Notes are accumulated before drafting begins. The note-taking phase is research; the drafting phase synthesizes the research.

### Completeness as methodological commitment

The full-corpus requirement is not merely procedural. It is the condition under which SP-3's claims about the archive carry evidential weight. A selective reading could miss patterns, miss counter-evidence, or produce a narrative that fits only the documents chosen. The philological standard is: read everything in the defined corpus, then write.

### The corpus and its structural history

The corpus the drafter will read did not always have its current structure. SP-3's methodology section should explain this as part of describing what the corpus is and how it came to be.

Three structural moments matter:

1. **The paper originally had an appendix** (A.1–A.5), built around a reproduction test — could a reviewer reproduce the work from the documented inputs?

2. **Stage III reconception** (2026-03-02, documented in `III_4.7.3_MHC_Tracing_SP_Reconception.md`): the reproduction test was rejected on three grounds (technological infeasibility, scholarly time-scale, the romantic-author assumption). SP roles were reconceived around documentation adequacy. The key formulation: *"Does the documentation adequately show how the intellectual trajectory traces to human understanding and direction?"* The old appendix sections mapped to new SP roles: A.1–A.3 to SP-3, A.4–A.5 to SP-2.

3. **CFP appendix elimination** (2026-04-02, documented in `CFP_5.2.4_pdl_SP1_SP2_SP3.md` PDL-004): the appendix was eliminated entirely. SP-1/2/3 absorb all its functions. No section of the paper body references "Appendix A." The last design iteration still called "Appendix A v3" (`CFP_5.2.2_pdl_appendix_v3.md`) was superseded by this decision.

This structural history is itself part of the research evidence: the archive documents its own architectural decisions, and the artifacts proving those decisions are citable. The drafter should present this history as methodology — explaining what the corpus is and why it is structured as it is — not as a prefatory orientation block.

### Drafting process

1. Read every document in the defined corpus (v1/v2 + Stage III); take structured notes using the protocol above (sub-agents permitted and encouraged)
2. Write a long draft — no length constraint; longer than a standard paper if the research requires it
3. Re-read and revise
4. Produce final SP-3

---

## Proposed Structure

SP-3 is a research paper. Its structure should be appropriate to that genre. What follows is a proposed structure, not a template to be filled in. The drafter is doing research; the structure should emerge from the research findings, not precede them. But the following elements are expected.

### Introduction

State the research question. Explain the connection to the paper body (Section 3). Introduce the archive as the primary source. Preview the three phases.

### Methodology

The philological approach. The full-corpus reading requirement and why it matters. The corpus description, including the structural history (appendix, SP reconception, appendix elimination — as described above). The note-taking protocol. The use of sub-agents and digital humanities tools. The conditions for successful retrospective reconstruction (from `CFP_4.7.8`): surviving identifiers, accessible conversations, sufficient internal structure for hypothesis generation, human judgment layer.

### Phase 0: Origin layer — before the documentation framework

The intellectual origin of JPEP predates the documentation framework. SP-3 must narrate this honestly as the starting condition. The chain: Chat X (UUID unknown, true origin of the publishing-barriers argument) → 6c8d9101 (Oct 10, Claude Sonnet 4.5 extended — the ur-conversation, where costly signaling, transparency paradox, and laundering were first named) → da6a830c (49 turns, anonymized, public — developed these into a full venue-design proposal) → 5.3.21 (Claude's anonymized extraction at end of da6a830c, pasted into 2ca5888a) → 4.1 (Claude synthesized 5.3.21 into the Complete Prompt, human endorsed).

**Key provenance fact:** 4.1 (Complete Prompt) is human-sourced, Claude-synthesized, human-endorsed — not human-composed. Every subsequent writing session operated within a framework the human directed and Claude structured. 4.7.1 is an incomplete extract of da6a830c that ends mid-sentence; it served as a register-calibration artifact.

**Privacy constraints:** 6c8d9101 is gitignored (not anonymized). Chat X's UUID is unknown. SP-3 can cite both via hubs and characterise their content via CFP_4.7.16 and CFP_5.3.15, but cannot point readers to the conversations themselves. da6a830c is available anonymized.

See: CFP_5.3.13 §10–§11, CFP_5.3.15.

### Phase 1: v1/v2 — Plan-driven writing

Tools: Claude.ai web + ChatGPT. Session IDs not established. The Complete Prompt (4.1 — see Phase 0 for its provenance) governed writing of Sections I–VI. Ontology co-development: the Type 2b category emerged from practice, not from pre-planning (evidence: `5.3.1` and `4.4.3` share `source_chat_id: 30a52e69`). The feedback loop: appendix written after the paper body, then fed back into Section 6 revision (evidence: `4.2.11`, `4.4.13`, `4.2.9` MOD-009). The self-philology story: Word/RTF to Canonical Markdown conversion, chat logs as primary ground truth for metadata reconstruction.

**Input routing:** 4.1 and 4.7.1 recurred across multiple writing sessions as shared context; guidance files (4.4.x) — full session-initiation prompts with explicit success criteria — were the operational grounding for each writing session. Section VIII involved a documented multi-AI cycle: Claude wrote the section, a ChatGPT GPT-5 Thinking session produced targeted revisions to §6.5, the author applied the revisions manually.

**Author role in Phase 1:** prompt author and content reviewer. The human wrote prompts, evaluated outputs, and directed revisions — but within a framework the human had designed (via 4.1). Documentation was not a conscious activity; it was a byproduct of using the tools.

### Phase 2: Stage III — Platform shift and theoretical reorientation

Platform shift to Claude Code. Meaningful human control theory integrated into the paper (Section 6). The essentially-contested-concept argument entered (Section 3). The reproduction test rejected and the documentation-adequacy model adopted — these are not separate events but emerged from the same session (`III_4.7.3`, 2026-03-02). Session IDs partially reconstructed retrospectively; this is "imperfect" implementation of the workflow — the session identification system did not exist in real time during this phase.

**Author role in Phase 2:** evolving toward architectural design. The human was no longer only prompting and reviewing outputs but designing the documentation infrastructure itself — the SP structure, the metadata conventions, the tracing condition. The role shifted from operating within a framework to designing the framework.

### Phase 3: CFP — Prospective documentation

The CFP phase is not part of the philological corpus (see Methodology above), but SP-3 must still characterize it as the third phase in the evolution of the author's role. The drafter draws on their own position within this phase — they are writing SP-3 as part of it — and on the structural facts visible from the archive boundary: the MHC-W workflow infrastructure is in place; prospective documentation is produced contemporaneously with the work; errors are present but reconstructable. Branch `cfp-ai-ethics-inquiry`, double contestation implementation, redundancy reduction, new section drafts.

**Author role in Phase 3:** methodology designer and philologist. The human designs the workflow, steers the documentation architecture, and — in producing SP-3 itself — becomes the philologist of the archive the human built.

### Synthesis

An overall assessment of the human author's role across the project. A narrative of how that role evolved — from prompt author to architectural designer to philologist — as a function of the changing technological infrastructure. This evolution is not a progress narrative (the phases represent different documentation architectures, not weak-to-strong development). The synthesis must connect back to the paper body's argument (Section 3): what the JPEP case shows about how AI-assisted philosophy is produced and what it means for the role of the author.

---

## Figures

Figures are available as evidence. They should be placed where the research argument needs them, not as structural anchors. The drafter decides where each figure belongs based on what the research requires.

### Available figures

The following figures were designed in `CFP_4.7.14_EpistemicTrace_SP3VisualDesign.md`. Their data sources are verified in `CFP_5.3.7_SelectedGraphCandidates.md` (for Graphs 1–3) and described in CFP_4.7.14 (for data-driven visuals).

| Visual | Description | Data source |
|--------|-------------|-------------|
| Visual 1 | Macro Timeline — horizontal timeline Oct 2025 to Apr 2026, five swim lanes | Manual construction from artifact dates |
| Visual 3 | Feedback Loop — small diagram (4–5 nodes) showing appendix to Section 6 revision cycle | Artifact IDs: 4.2.11, 4.4.13, 4.2.9 MOD-009 |
| Visual 4 | Contrast Diptych — Introduction documentation density, v1/v2 vs CFP | CFP_5.3.7 Graph 3 (verified, ghost nodes marked) |
| Visual 5 | Version Chain — Section 6, three CFP drafts with `derived_from` links | CFP_5.3.7 Graph 2 (verified) |
| Visual 7 | Date Histogram — artifact creation dates, colored by era | YAML `date` fields, extracted |
| Visual 8 | Hub Fan-Out — artifacts per session, sorted descending, colored by era | Hub script output |
| Visual 10 | Interactive Graph — 225-node HTML visualization | Already built at `_GRAPHS/jpep_graph.html` |

The drafter is not required to use all figures. Use what serves the research argument. Place figures where they provide evidence prose cannot. Reference Visual 10 (interactive graph) as a digital supplement where appropriate.

---

## What the Research Must Cover

- The human author's role in each of the three phases, grounded in documentary evidence from the archive (Phases 1 and 2) and from the drafter's own position (Phase 3)
- How that role evolved as a function of the changing technological infrastructure (platforms, workflow tools, documentation conventions)
- The feedback loop (Act 4 from `CFP_4.7.13`): the appendix shaped the paper, demonstrating the recursive character of documentation
- The ontology co-development (Act 2): the documentation system's categories emerged from the attempt to use them, not from a pre-existing plan
- The Stage III theoretical turn: meaningful human control and the essentially-contested-concept argument entered here, and the SP reconception happened in the same session — the artifacts document this
- The self-philology story: retrospective reconstruction of v1/v2 metadata, and the four conditions for successful reconstruction (`CFP_4.7.8`)
- Platform affordances and limitations: what each platform (Claude.ai web, ChatGPT, Claude Code) made possible and what it did not, and how this shaped the archive (PDL-010)
- An honest assessment of what the record covers and does not cover, including an error typology: platform-driven gaps, user-driven errors, reconstructable gaps, irrecoverable losses (PDL-011)
- Design-for-reconstructability as the normative lesson from v1/v2: the reconstruction succeeded because certain features (stable UUIDs, sufficient artifact structure) were already in place

## What the Synthesis Must Achieve

- An overall assessment of the human author's role across the project
- A narrative of how that role evolved — from prompt author to architectural designer to philologist
- A connection between this evolution and the changing technological infrastructure
- A connection back to the paper body's argument in Section 3

---

## Voice and Tone

### Register
Accessible academic, with the rhetorical structure of scholarship. SP-3 is a research paper, not supplementary show-and-tell. It can be expansive where the research requires it — there is no word limit — but it earns its length through evidence and analysis.

### Tone
Direct and confident. The author is not defending the record — they are analyzing it.

### Stylistic Notes
- No hedging where the evidence is clear. "The modlog records 13 entries" — not "the modlog appears to record approximately 13 entries."
- Use artifact IDs when citing evidence (e.g., "4.2.9, MOD-009"). The reader has SP-2 for navigation.
- Always write "meaningful human control" in full — never abbreviate. The abbreviation is reserved for workflow commands and artifact prefixes.
- "Essentially contested concept" — use Gallie's term precisely.
- Prefer concrete artifact references over generalizations. "The session hub CHAT_SID-20260323-190000 lists two artifacts" is better than "sessions were systematically documented."
- Let figures speak where they are used. Introduce the figure, give the reader a moment to look, then explain.

---

## Constraints

### Must Include
- Full corpus reading (every v1/v2 and Stage III document in SP4, SP5, _HUBS) as a methodological requirement
- The corpus restriction rationale (CFP phase excluded because still in development)
- **Phase 0 (origin layer)** — the intellectual chain before 4.1, with its privacy constraints and the provenance of 4.1 itself (human-sourced, Claude-synthesized, human-endorsed)
- The three writing phases with their characterization of the human author's role
- The structural history of the corpus (appendix, SP reconception, appendix elimination) as part of the methodology
- Stage III as a theoretical turning point — meaningful human control and the essentially-contested-concept argument entered here; the artifacts document it
- The four reconstruction conditions (`CFP_4.7.8`)
- Design-for-reconstructability as the normative lesson from v1/v2
- **Complementary evidence sources** — artifacts and conversations preserve different things; neither alone suffices for the adequacy claim (CFP_5.3.13 §8)
- **Section VIII multi-AI production** — Claude → ChatGPT → manual application as evidence of cross-tool orchestration with documented tool identity
- An honest assessment with error typology
- **Still-open documentation gaps** (CFP_5.3.13 §4): Chat 1 (deleted), 6c8d9101 (gitignored)
- Platform affordances and limitations

### Must Avoid
- Abbreviating "meaningful human control" as "MHC" in the text
- **Characterising 4.1 as "human-authored" in the sense of human-composed** — correct characterisation: human-sourced, Claude-synthesized, human-endorsed (see CFP_5.3.13 §10)
- **Treating 4.7.1 as a complete document** — it is an incomplete extract of da6a830c, ends mid-sentence
- **Claiming artifact-based reconstruction is self-sufficient** — artifacts preserve structure and scope; conversations preserve agency and provenance; SP-3 must use both
- Framing v1/v2 as "weak" and later phases as "strong" — use "different documentation architectures"
- **Overstating the v1/v2 vs. CFP quality gap** — both phases required reconstruction; both succeeded because the archive structure enabled it (CFP_5.3.13 §4, Correction 1)
- **Drifting toward adversarial verification standards** — the paper argues for good-faith adequacy, not tamper-resistance (CFP_5.3.13 §4, Correction 2)
- Overclaiming completeness
- Attributing temporal discounting or definitional flexibility to this archive
- Reintroducing the reproduction-test model
- Anticipating and rebutting objections — SP-3 is research, not apologetics
- Selective source reading — the full v1/v2 + Stage III corpus must be read; no cherry-picking
- Reading CFP-prefixed documents as part of the philological corpus (excluded; CFP phase still in progress)

### Length
No upper limit. Longer than a standard paper if the research requires it.

---

## Source Mapping

| Element | Source | Reference |
|---------|--------|-----------|
| **Research findings (read first)** | Writer briefing | CFP_5.3.13 |
| Origin layer narrative | Steering note | CFP_5.3.15 |
| PreliminaryChat chain verification | Steering note | CFP_5.3.17 |
| Seven-act macro story | Epistemic trace | CFP_4.7.13 |
| Visual design and figure specifications | Epistemic trace | CFP_4.7.14 |
| Graph specifications (verified) | Steering note | CFP_5.3.7 |
| Self-philology + reconstruction conditions | Epistemic trace | CFP_4.7.8 |
| Ur-conversation characterization | Epistemic trace | CFP_4.7.16 |
| SP reconception + reproduction test rejection | Epistemic trace | III_4.7.3 |
| Last "Appendix A" design iteration (superseded) | PDL | CFP_5.2.2 |
| Appendix elimination decision | PDL-004 | CFP_5.2.4 |
| SP-3 scope decision | PDL-007 | CFP_5.2.4 |
| Platform affordances | PDL-010 | CFP_5.2.4 |
| Philological standard + error typology | PDL-011 | CFP_5.2.4 |
| Stage III theoretical turn | PDL-012 | CFP_5.2.4 |
| SP-3 reconception as research paper | PDL-017 | CFP_5.2.4 |
| Briefing/guidance split decision | PDL-019 | CFP_5.2.4 |
| Section 3 (essentially-contested argument) | Stage III draft | III_5.4.1 |
| Section 6 (meaningful human control) | Stage III draft | III_5.4.2 |
| Three transparency criteria | Paper Section 7 | CFP_5.4.9_Section7_v3.md |

---

*Section Guidance v4 — updated 2026-04-03 (SID-20260403-213917)*
*Previous version (v3) superseded: chain walk findings, origin layer, complementary evidence sources, and author corrections now incorporated*
*Workflow: Design | Command: MHC-PDL*
