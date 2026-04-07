---
artifact_type: section_guidance
document_type: Type 4 - Section Guidance
label: CFP_4.4.20_SectionGuidance_SP3
project: JPEP CFP Adaptation
version: v7 (synthetic merge — story spine + thin figure callouts)
date: 2026-04-07
session_id: SID-20260407-181422
source_conversation:
  - SID-20260407-181422
inputs:
  - "CFP_4.7.20_EpistemicTrace_Section6History.md (Section 6 throughline data)"
  - "CFP_5.4.9_Section7_v3.md (paper Section 7 — defines the goals SP-3 must serve)"
  - "CFP_5.2.4_pdl_SP1_SP2_SP3.md PDL-024 (decision: thin guidance + draft-first refine workflow)"
  - "CFP_5.3.13_Note_SP3_WriterBriefing.md (research findings — read first)"
  - "CFP_5.3.18_Note_CFPChainWalk_Findings.md (CFP-phase chain walk findings)"
  - "CFP_4.7.19_EpistemicTrace_StageIII_InputOutputAnalysis.md (Stage III I/O + infrastructure findings)"
  - "CFP_5.3.15_Note_OriginStoryForSP3.md (origin layer narrative)"
  - "CFP_5.3.17_Note_PreliminaryChat_ChainVerification.md (PreliminaryChat chain)"
  - "III_4.7.3_MHC_Tracing_SP_Reconception.md (SP reconception)"
output_file: ""
validated: ""
validation: ""
supersedes:
  - "CFP_4.4.20_SectionGuidance_SP3.md v6 (2026-04-05; replaced by Section 6 throughline + draft-first workflow per PDL-024)"
  - "CFP_4.4.17_Guidance_SelectedGraphSpecifications.md (graph-spec separation eliminated; figure detail moves to consolidated note)"
---

# Section Guidance: SP-3 — Documentation Adequacy Account

*Synthetic merge. Story spine and figure callouts only. Layout, label, and data details for figures live in the consolidated figure-data note (CFP_5.3.X). Section 6 history is canonical in CFP_4.7.20.*

---

## Purpose

SP-3 is a research paper in its own right — a dissertation-chapter-length study that uses the JPEP documentation archive as its primary source.

**Research question:** What role did the human author play in JPEP, and how did that role evolve as a function of the changing technological infrastructure?

**The goals SP-3 must serve are defined in the paper's Section 7.** Section 7 specifies that documentation is adequate when it enables evaluators to answer three questions:

1. **Attribution.** Can evaluators locate where human judgment operated — what directions were set, what choices made, where did the work depart from AI-generated material and why?
2. **Intellectual trajectory.** Can evaluators follow how the work developed — the sequence of questions posed, the moments of revision and redirection, the emergence and testing of key ideas, what was retained under pressure?
3. **Understanding and endorsement.** Does the documentation give reason to believe the author understood and endorsed what they present — corrections to AI outputs, places where authorial judgment overrode AI suggestion, capacity to explain and defend the argument?

SP-3 is the part of the paper's supplementary materials where the author argues that the JPEP record satisfies these three criteria. Section 7 explicitly invites the community to assess whether SP-3's tracing claim is supported by SP-4 and SP-5. SP-3 is the bridge.

**What SP-3 is not:** SP-3 is not a document-type index (SP-2 handles that), not a high-level AI-usage declaration (SP-1 handles that), not a defence against anticipated objections, and not a development story. It is research: it reads the archive, reports what it finds, interprets it.

---

## How SP-3 reads — the Section 6 throughline

**SP-3 follows the history of one section — Section 6 — from first writing to current state, as the illustrative case for the three Section 7 criteria.**

The reader meets a single concrete case and walks it from beginning to end across two technological regimes and five distinct production stages. They do not have to build a separate mental model for every section in the archive. The throughline IS the argument: by following Section 6, the reader exercises attribution, trajectory, and understanding-and-endorsement on a real case, including its failure modes.

Section 6 is the right illustrative example for four converging reasons:

1. **It carries the central theoretical move.** Section 6 integrates Santoni de Sio & van den Hoven's meaningful human control framework into the paper's argument. It is the section the rest of the paper leans on.

2. **It self-instantiates the paper's argument.** §6.3 makes the methodological claim that documentation practice produces its own requirements — and that claim was *empirically generated* by the experience of writing Section 6 itself. The SP reconception (III_4.7.3, 2026-03-02) emerged inside the Section 6 redraft session. The illustrative example is the paper's argument.

3. **Its history exercises every kind of evidence the documentation system produces.** Across five stages: parallel prompt steering with mid-course correction from a sideways chat (Stage 1); a cross-section feedback loop from the appendix into §6.2 (Stage 2); a failed draft, model switch, and SP reconception (Stage 3); a three-draft session with two reviewers and a 13-entry modlog (Stage 4); a redundancy compression pass (Stage 5).

4. **It contains exactly one ghost.** The Jan 28 lost draft is the only irrecoverable item in the Section 6 history. This is a clean, scoped, acknowledgeable limit case for the "where the record falls short" requirement — not a defining failure of the system.

The full data for the throughline is consolidated in **CFP_4.7.20_EpistemicTrace_Section6History**. Drafters do not need to re-do the philological work; CFP_4.7.20 is canonical for Section 6 facts, dates, UUIDs, and stage transitions.

### Reader background — required before the throughline starts

Before the first figure, SP-3 gives the reader a short paragraph (≤150 words) that:

- Says **what Section 6 is about** (one or two sentences: it argues that mandated transparency requires specified frameworks; it integrates meaningful human control; §6.3 claims documentation practice produces its own requirements).
- Says **why following its history is worth their time** (one sentence: it lets the reader exercise the three Section 7 criteria on a single concrete case across six months and two technological regimes).
- Tells them **what to look for** (one sentence: as you read this history, ask yourself the three questions; the figures will help you see the answers).

This background is not optional. Without it, the throughline reads as parochial.

### The other sections are not abandoned

The Section 6 throughline does not mean other sections vanish from SP-3. Other sections are referenced *in support* of claims grounded in Section 6 — to show that the patterns visible on Section 6 recur, that Section 6 is the densest worked example rather than an exception. The synthesis figure (Figure 6) zooms back out to the whole project to make this explicit. The CFP chain walk findings (CFP_5.3.18) and the Stage III infrastructure requirements (CFP_4.7.19) provide the cross-section material the prose draws on.

---

## Methodology

### Approach: philological, with digital humanities tools

The methodology is philological. The drafter treats the JPEP documentation archive as a primary source corpus and applies the methods of textual scholarship: systematic reading, structured note-taking, hypothesis generation from internal evidence, cross-referencing across documents. Digital humanities tools — sub-agents for parallel reading, metadata extraction scripts, graph visualizations — assist the philological work but do not replace it.

### Two evidence sources — artifacts and conversations

Artifacts and conversations are complementary evidence sources with different strengths. **Artifacts** preserve structure, scope, encoded reasoning, and sibling relationships (via `source_chat_id` and hub files). **Conversations** preserve agency attribution, provenance chains, and the interactional dynamics of human-AI collaboration. Neither alone is sufficient for the adequacy argument. The chain walk (CFP_5.3.13 §10) demonstrated this concretely: artifact-based reconstruction recovered scope, date, and reasoning for session e5ec43be — but only the conversation confirmed who initiated the reading, and only conversation access revealed 4.1's true provenance (human-sourced, Claude-synthesized, human-endorsed). SP-3 should present both evidence types and be explicit about which claims rest on which source.

### Research basis

The corpus was read in full across nine research sessions (SID-20260401 through SID-20260404) conducted jointly by the author and Claude. The v1/v2 and Stage III findings are consolidated in `CFP_5.3.13` (writer briefing). The CFP-phase findings are in `CFP_5.3.18` (chain walk note). The Section 6 throughline data is consolidated in `CFP_4.7.20` (Section 6 history trace). The drafter works from these three documents; individual source files may be consulted to clarify specific doubts, but a fresh corpus pass is not required or expected.

### The corpus and its structural history

The corpus did not always have its current structure. SP-3's methodology section should explain this as part of describing what the corpus is and how it came to be.

Three structural moments matter:

1. **The paper originally had an appendix** (A.1–A.5), built around a reproduction test — could a reviewer reproduce the work from the documented inputs?

2. **Stage III reconception** (2026-03-02, documented in `III_4.7.3_MHC_Tracing_SP_Reconception.md`): the reproduction test was rejected on three grounds (technological infeasibility, scholarly time-scale, the romantic-author assumption). SP roles were reconceived around documentation adequacy. The key formulation: *"Does the documentation adequately show how the intellectual trajectory traces to human understanding and direction?"* The old appendix sections mapped to new SP roles: A.1–A.3 to SP-3, A.4–A.5 to SP-2.

3. **CFP appendix elimination** (2026-04-02, documented in `CFP_5.2.4_pdl_SP1_SP2_SP3.md` PDL-004): the appendix was eliminated entirely. SP-1/2/3 absorb all its functions.

This structural history is itself part of the research evidence: the archive documents its own architectural decisions, and the artifacts proving those decisions are citable. The drafter should present this history as methodology — explaining what the corpus is and why it is structured as it is — not as a prefatory orientation block.

### Drafting process — draft-first refine workflow

PDL-024 establishes the workflow: draft SP-3 prose with concrete `[FIGURE N — purpose, what it must show]` placeholder blocks at each anchor point. Placeholders are specific enough that the prose unfolds around them (introduces, gives the reader time to look, then unpacks) but abstract enough that visual details emerge from what the prose actually needs. Each figure is drawn once, against stable surrounding prose, instead of multiple times against guesses. Figures that prove unnecessary when the prose is on the page are dropped without preciousness; figures that become obvious mid-drafting are added.

Sequence:

1. Read the briefing (CFP_5.3.13), the CFP chain walk findings (CFP_5.3.18), and the Section 6 history trace (CFP_4.7.20). Consult source files only to clarify specific doubts.
2. Write a long draft of SP-3 with placeholder figure blocks at each anchor point. No length constraint. Structure: Opening (background + research question) → Methodology → Throughline (the Section 6 history, narrated against the three criteria) → Honest Assessment → Synthesis.
3. When a section's prose is stable, draw that figure against the now-concrete prose needs. Read the consolidated figure-data note (CFP_5.3.X) for layout/label/data details.
4. Re-read and revise.
5. Produce final SP-3.

---

## Figure callouts (thin)

Six figures, all anchored on Section 6, mapped to Section 7 criteria. Layout, label text, color choices, node lists, and data sources live in the consolidated figure-data note (`CFP_5.3.X`), not here.

| # | Figure | Purpose (one line) | Section 7 criterion |
|---|---|---|---|
| 1 | **Section 6 across six months** | Orient the reader to the throughline. Show all five stages on one timeline, with platform/model bands and key artifacts annotated. | Trajectory (overview) |
| 2 | **The feedback loop** | Show that the appendix work modified Section 6 §6.2 — the documentation framework is recursive. Real artifact nodes (4.4.13, 4.2.9 MOD-009, chat 65a571f1). | Trajectory (recursion) + Attribution |
| 3 | **Two architectures, one section** | Show that documentation density is a property of the architecture, not the author or the effort. Same section, two regimes (Stage 1 vs Stage 4). | Attribution + Understanding-and-endorsement |
| 4 | **The three-draft session** | Show that intellectual trajectory is documentable as a directed sequence with annotated transitions. Reasons for each v1→v2→v3 step from CFP_4.2.18. | Trajectory + Understanding-and-endorsement |
| 5 | **Failure and the visible decision** | Make the model-switch decision visible (Opus 4.5 → Sonnet 4.6) and acknowledge the lost Jan 28 deliberation as the one ghost in the Section 6 history. | Understanding-and-endorsement + acknowledgment of limit |
| 6 | **Where Section 6 sits in the project** | Synthesis. Show that Section 6 is the densest worked example, not an exception — the same patterns recur across other sections. | All three |

The figure callouts above are *purpose statements*, not specifications. The drafter writes the prose first, with placeholder blocks; the figures are drawn when the prose is stable.

---

## What the Research Must Cover

- The human author's role in each of the production stages of Section 6, grounded in documentary evidence from CFP_4.7.20 and the underlying artifacts
- How that role evolved as a function of the changing technological infrastructure (platforms, models, workflow tools, documentation conventions)
- The Section 6 feedback loop (Stage 2): the appendix work shaped §6.2, demonstrating the recursive character of documentation
- The Stage III theoretical turn within Section 6: meaningful human control integrated, the SP reconception emerging from the same redraft session
- **Infrastructure requirements for traceability** — derived empirically from the Stage 3b Section 6 case (no commit, no export) and other Stage III cases (CFP_4.7.19)
- The CFP three-draft session (Stage 4): the cleanest documented version chain in the archive, with both reviewers' input and a 13-entry modlog
- The redundancy pass (Stage 5): how Section 6 was compressed as part of the cross-paper redundancy work (CFP_4.2.22)
- The four reconstruction conditions (`CFP_4.7.8`) and their applicability to Section 6 reconstruction
- **Complementary evidence sources** — artifacts and conversations preserve different things; neither alone suffices for the adequacy claim (CFP_5.3.13 §8)
- Cross-section context where it supports the throughline: that the Section 6 patterns recur (Section VIII multi-AI production, CFP chain walk findings, etc.)
- An honest assessment with error typology, focused on what the Section 6 history shows and does not show (corrected per PDL-016: session ID gaps are infrastructure-driven, not user error; user-driven errors = forgetting to activate automation)
- **Still-open documentation gaps** specific to Section 6 (the Jan 28 lost draft) and to the project (Chat 1 deleted; 6c8d9101 gitignored; CFP_5.3.13 §4)
- Platform affordances and limitations as they shaped Section 6's history (Claude.ai web → Claude Code; model identities)

## What the Synthesis Must Achieve

- An overall assessment of the human author's role across the project, anchored in what Section 6 made visible
- A narrative of how that role evolved — from prompt author to architectural designer to philologist
- A connection between this evolution and the changing technological infrastructure
- A connection back to the paper body's argument in Section 3 and the criteria in Section 7
- The recognition that writing produces its own documentation needs — supporting the paper's argument for experimental, community-developed practice (Section 6.3)

---

## Voice and Tone

### Register

Accessible academic, with the rhetorical structure of scholarship. SP-3 is a research paper, not supplementary show-and-tell. It can be expansive where the research requires it — there is no word limit — but it earns its length through evidence and analysis.

### Tone

Direct and confident. The author is not defending the record — they are analyzing it.

### Stylistic Notes

- No hedging where the evidence is clear. "The modlog records 13 entries" — not "the modlog appears to record approximately 13 entries."
- Use artifact IDs when citing evidence (e.g., "4.2.9 MOD-009"). The reader has SP-2 for navigation.
- Always write "meaningful human control" in full — never abbreviate. The abbreviation is reserved for workflow commands and artifact prefixes.
- "Essentially contested concept" — use Gallie's term precisely.
- Prefer concrete artifact references over generalizations.
- Let figures speak. Introduce the figure, give the reader time to look, then explain what it shows. Do not summarize the figure before showing it.
- Describe findings plainly. Name the evidence, not the label.

---

## Constraints

### Must Include

- The Section 6 throughline as the spine of SP-3
- Reader-background paragraph before the throughline starts
- The philological research basis: joint author–AI reading across nine sessions, consolidated in CFP_5.3.13, CFP_5.3.18, and CFP_4.7.20
- **Phase 0 (origin layer)** as background — the intellectual chain before 4.1, with its privacy constraints and the provenance of 4.1 itself (human-sourced, Claude-synthesized, human-endorsed). This is context for Section 6's first stage; it does not require its own throughline.
- The structural history of the corpus (appendix, SP reconception, appendix elimination) as part of the methodology
- Stage III as a theoretical turning point — meaningful human control entered here; the artifacts document it via Section 6 specifically
- **Stage III infrastructure requirements** — concrete cases where missing infrastructure components produced specific gaps in the record; presented as empirical findings about what traceability requires, not as apology (CFP_4.7.19). The Section 6 Jan 28 case is one of these.
- The four reconstruction conditions (`CFP_4.7.8`)
- **Complementary evidence sources** — artifacts and conversations preserve different things; neither alone suffices for the adequacy claim (CFP_5.3.13 §8)
- **Section VIII multi-AI production** — Claude → ChatGPT → manual application as evidence of cross-tool orchestration with documented tool identity (Stage 1 of Section 6 history)
- **CFP-phase findings from the chain walk** (CFP_5.3.18): non-linear argument development, cascading dependencies, redundancy as structural effect of modular writing, expansion-then-contraction, ad hoc corrections, template design shaping capture, multi-model workflow, context exhaustion producing documentation
- **Template design determining what gets captured** — 89% vs 2% endorsement capture depending on whether the template asks for it; strongest empirical finding for the paper's framework argument
- An honest assessment with error typology
- **Still-open documentation gaps** (CFP_5.3.13 §4): Chat 1 (deleted), 6c8d9101 (gitignored), Section 6 Jan 28 lost deliberation
- Platform affordances and limitations
- Figures as narrative anchors — every major section has a visual that carries the claim, drawn against stable prose

### Must Avoid

- Abbreviating "meaningful human control" as "MHC" in the text
- **Characterising 4.1 as "human-authored" in the sense of human-composed** — correct characterisation: human-sourced, Claude-synthesized, human-endorsed (see CFP_5.3.13 §10)
- **Treating 4.7.1 as a complete document** — it is an incomplete extract of da6a830c, ends mid-sentence
- **Claiming artifact-based reconstruction is self-sufficient** — artifacts preserve structure and scope; conversations preserve agency and provenance; SP-3 must use both
- Framing v1/v2 as "weak" and later phases as "strong" — use "different documentation architectures"
- **Overstating the v1/v2 vs. CFP quality gap** — both phases required reconstruction; both succeeded because the archive structure enabled it (CFP_5.3.13 §3, Correction 1)
- **Treating the Section 6 lost Jan 28 draft as the defining feature of any phase** — it is one slip in an otherwise working system; one ghost in the Section 6 history
- **Treating the modlog as the central documentation unit** — the documentation system is a combination of artifacts (modlogs, traces, PDLs, guidance, notes, hubs, section drafts, pattern summaries); modlogs are one kind of evidence among many
- **Drifting toward adversarial verification standards** — the paper argues for good-faith adequacy, not tamper-resistance (CFP_5.3.13 §3, Correction 2)
- Overclaiming completeness
- Reintroducing the reproduction-test model
- Anticipating and rebutting objections — SP-3 is research, not apologetics
- **Coining labels for findings** — describe what was observed plainly
- Presenting redundancy as an LLM defect — it is a structural consequence of modular section-by-section writing
- Attributing session ID gaps to user error — the workflow tooling did not generate them in early phases (PDL-016)
- **Specifying figure layouts in this guidance** — figure detail lives in the consolidated figure-data note (CFP_5.3.X)

### Length

No upper limit. Longer than a standard paper if the research requires it.

---

## Source Mapping

| Element | Source | Reference |
|---------|--------|-----------|
| **Goals SP-3 must serve** | Paper Section 7 v3 | CFP_5.4.9_Section7_v3.md |
| **Section 6 throughline data (canonical)** | Epistemic trace | CFP_4.7.20 |
| **Research findings (read first)** | Writer briefing | CFP_5.3.13 |
| **CFP chain walk findings** | Chain walk note | CFP_5.3.18 |
| **Figure layout/label/data details** | Consolidated note | CFP_5.3.X (figure-data note) |
| Origin layer narrative | Steering note | CFP_5.3.15 |
| PreliminaryChat chain verification | Steering note | CFP_5.3.17 |
| Stage III I/O analysis + infrastructure requirements | Epistemic trace | CFP_4.7.19 |
| Self-philology + reconstruction conditions | Epistemic trace | CFP_4.7.8 |
| Ur-conversation characterization | Epistemic trace | CFP_4.7.16 |
| SP reconception + reproduction test rejection | Epistemic trace | III_4.7.3 |
| Workflow + restructure decision | PDL | CFP_5.2.4 PDL-024 |
| Appendix elimination decision | PDL | CFP_5.2.4 PDL-004 |
| SP-3 scope decision | PDL | CFP_5.2.4 PDL-007 |
| Platform affordances | PDL | CFP_5.2.4 PDL-010 |
| Philological standard + error typology | PDL | CFP_5.2.4 PDL-011 |
| Section 3 (essentially-contested argument) | Stage III draft | III_5.4.1 |
| Section 6 (meaningful human control) — current state | CFP draft | CFP_5.4.8_Section6_v4.md |
| Three transparency criteria (canonical statement) | Paper Section 7 | CFP_5.4.9_Section7_v3.md |

---

*Section Guidance v7 — synthetic merge, 2026-04-07 (SID-20260407-181422)*
*v6 → v7 (per PDL-024): merged with CFP_4.4.17; figure detail externalized to consolidated note; Section 6 throughline replaces multi-section figure plan; draft-first refine workflow replaces upfront figure specification*
*Workflow: Design | Command: MHC-PDL*
