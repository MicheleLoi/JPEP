---
artifact_type: section_guidance
document_type: Type 4 - Section Guidance
label: CFP_4.4.20_SectionGuidance_SP3
project: JPEP CFP Adaptation
version: v6
date: 2026-04-05
session_id: SID-20260405-094022
source_conversation:
  - SID-20260404-103931
  - SID-20260405-094022
inputs:
  - "CFP_5.2.4_pdl_SP1_SP2_SP3.md (PDL-004 through PDL-022)"
  - "CFP_5.3.13_Note_SP3_WriterBriefing.md (research findings — read first)"
  - "CFP_5.3.15_Note_OriginStoryForSP3.md (origin layer narrative)"
  - "CFP_5.3.17_Note_PreliminaryChat_ChainVerification.md (PreliminaryChat chain)"
  - "CFP_5.3.18_Note_CFPChainWalk_Findings.md (CFP-phase chain walk findings)"
  - "CFP_4.7.13_EpistemicTrace_SP3DesignBrainstorm.md"
  - "CFP_4.7.14_EpistemicTrace_SP3VisualDesign.md (figure specifications + production plan)"
  - "CFP_4.7.8_EpistemicTrace_SelfReferentialDocumentation.md"
  - "CFP_5.3.7_SelectedGraphCandidates.md"
  - "CFP_5.3.1_WorkPlan_CFP_Adaptation.md"
  - "CFP_4.7.19_EpistemicTrace_StageIII_InputOutputAnalysis.md (Stage III I/O analysis + infrastructure findings)"
  - "III_4.7.3_MHC_Tracing_SP_Reconception.md"
  - "CFP_5.2.2_pdl_appendix_v3.md"
output_file: ""
validated: ""
validation: ""
supersedes: "CFP_4.4.20_SectionGuidance_SP3.md v5 (2026-04-04; Stage III section lacked infrastructure-requirements framing)"
---

# Section Guidance: SP-3 — Documentation Account

---

## Purpose Statement

SP-3 is a research paper in its own right — a dissertation-chapter-length study that uses the JPEP documentation archive as its primary source.

**Research question:** What role did the human author play in JPEP, and how did that role evolve as a function of the changing technological infrastructure?

**Connection to the paper body:** Section 3 argues that the way philosophy is produced — and with it the role of the author — is changing. SP-3 is a case study: the first-person, documented account of what that change looked like from the inside. An older version of the paper also traced how the interaction itself evolved — from prompting and refining outputs, to designing documentation architectures and methodology. SP-3 should trace this evolution as part of its research narrative.

**What SP-3 is not:** SP-3 is not a document-type index (SP-2 handles that), not a high-level AI-usage declaration (SP-1 handles that), and not a defence of the record against anticipated objections. SP-3 is research: it reads the archive, reports what it finds, and interprets it.

**How SP-3 reads:** The figures carry the narrative. Each major section is anchored by a visual — the prose introduces the figure, gives the reader time to look, and then unpacks what it shows. This is a research paper with depth, not a slideshow — but the figures are the spine, not decoration. A reader who looked only at the figures and their captions should grasp the main story.

---

## Methodology

### Approach: philological, with digital humanities tools

The methodology is philological. The drafter treats the JPEP documentation archive as a primary source corpus and applies the methods of textual scholarship: systematic reading, structured note-taking, hypothesis generation from internal evidence, cross-referencing across documents. Digital humanities tools — sub-agents for parallel reading, metadata extraction scripts, graph visualizations — assist the philological work but do not replace it.

### Two evidence sources — artifacts and conversations

Artifacts and conversations are complementary evidence sources with different strengths. **Artifacts** preserve structure, scope, encoded reasoning, and sibling relationships (via `source_chat_id` and hub files). **Conversations** preserve agency attribution, provenance chains, and the interactional dynamics of human-AI collaboration. Neither alone is sufficient for the adequacy argument. The chain walk (CFP_5.3.13 §10) demonstrated this concretely: artifact-based reconstruction recovered scope, date, and reasoning for session e5ec43be — but only the conversation confirmed who initiated the reading, and only conversation access revealed 4.1's true provenance (human-sourced, Claude-synthesized, human-endorsed). SP-3 should present both evidence types and be explicit about which claims rest on which source.

### Research basis

The corpus was read in full across nine research sessions (SID-20260401 through SID-20260404) conducted jointly by the author and Claude. The v1/v2 and Stage III findings are consolidated in `CFP_5.3.13` (writer briefing, §1–§13). The CFP-phase findings are in `CFP_5.3.18` (chain walk note). The drafter works from these two documents; individual source files may be consulted to clarify specific doubts, but a fresh corpus pass is not required or expected.

### The corpus and its structural history

The corpus did not always have its current structure. SP-3's methodology section should explain this as part of describing what the corpus is and how it came to be.

Three structural moments matter:

1. **The paper originally had an appendix** (A.1–A.5), built around a reproduction test — could a reviewer reproduce the work from the documented inputs?

2. **Stage III reconception** (2026-03-02, documented in `III_4.7.3_MHC_Tracing_SP_Reconception.md`): the reproduction test was rejected on three grounds (technological infeasibility, scholarly time-scale, the romantic-author assumption). SP roles were reconceived around documentation adequacy. The key formulation: *"Does the documentation adequately show how the intellectual trajectory traces to human understanding and direction?"* The old appendix sections mapped to new SP roles: A.1–A.3 to SP-3, A.4–A.5 to SP-2.

3. **CFP appendix elimination** (2026-04-02, documented in `CFP_5.2.4_pdl_SP1_SP2_SP3.md` PDL-004): the appendix was eliminated entirely. SP-1/2/3 absorb all its functions. No section of the paper body references "Appendix A." The last design iteration still called "Appendix A v3" (`CFP_5.2.2_pdl_appendix_v3.md`) was superseded by this decision.

This structural history is itself part of the research evidence: the archive documents its own architectural decisions, and the artifacts proving those decisions are citable. The drafter should present this history as methodology — explaining what the corpus is and why it is structured as it is — not as a prefatory orientation block.

### Drafting process

1. Read the briefing (CFP_5.3.13) and CFP chain walk findings (CFP_5.3.18). Consult source files only to clarify specific doubts.
2. Write a long draft — no length constraint. Structure around the figures (see Proposed Structure below).
3. Re-read and revise.
4. Produce final SP-3.

---

## Proposed Structure

SP-3 is a research paper structured around its figures. Each major section is anchored by one or two visuals that carry the narrative claim; the prose introduces the visual, lets the reader look, and unpacks what it shows. The structure below maps sections to their anchor figures. The drafter may adjust the sequence if the research demands it, but every section should have a visual anchor.

### Opening — the archive at a glance

**Anchor figure: Date Histogram (Visual 7).** Artifact creation dates, bars colored by phase (v1/v2, Stage III, CFP). Two dramatic spikes — 33 artifacts in Oct 13–19 2025, 24 artifacts on Apr 1 2026 — with a gap between them. The visual tells the story before the prose begins: bursts, silence, resumed activity with different tooling.

State the research question. Introduce the archive as the primary source. The histogram is the first evidence: this is what the archive looks like as data.

### Methodology

The philological approach. The corpus description, including the structural history (appendix, SP reconception, appendix elimination). The research methodology: joint author–AI reading across nine sessions, consolidated into briefing and chain walk findings. The conditions for successful retrospective reconstruction (from `CFP_4.7.8`): surviving identifiers, accessible conversations, sufficient internal structure for hypothesis generation, human judgment layer. Two evidence sources: artifacts preserve structure and scope; conversations preserve agency and provenance; neither alone suffices.

### Phase 0: Origin layer — before the documentation framework

The intellectual origin of JPEP predates the documentation framework. SP-3 must narrate this honestly as the starting condition. The chain: Chat X (UUID unknown, true origin of the publishing-barriers argument) → 6c8d9101 (Oct 10, Claude Sonnet 4.5 extended — the ur-conversation, where costly signaling, transparency paradox, and laundering were first named) → da6a830c (49 turns, anonymized, public — developed these into a full venue-design proposal) → 5.3.21 (Claude's anonymized extraction at end of da6a830c, pasted into 2ca5888a) → 4.1 (Claude synthesized 5.3.21 into the Complete Prompt, human endorsed).

**Key provenance fact:** 4.1 (Complete Prompt) is human-sourced, Claude-synthesized, human-endorsed — not human-composed. Every subsequent writing session operated within a framework the human directed and Claude structured. 4.7.1 is an incomplete extract of da6a830c that ends mid-sentence; it served as a register-calibration artifact.

**Privacy constraints:** 6c8d9101 is gitignored (not anonymized). Chat X's UUID is unknown. SP-3 can cite both via hubs and characterise their content via CFP_4.7.16 and CFP_5.3.15, but cannot point readers to the conversations themselves. da6a830c is available anonymized.

See: CFP_5.3.13 §10–§11, CFP_5.3.15.

### Phase 1: v1/v2 — Plan-driven writing

**Anchor figure: Feedback Loop (Visual 3).** Small diagram (4–5 nodes) showing the appendix → Section 6 revision cycle. Artifact IDs annotated: 4.2.11, 4.4.13, 4.2.9 MOD-009. The visual point: the documentation framework is recursive — the appendix about transparency revealed constraints that changed what the paper says about transparency. A circle, not a line.

Tools: Claude.ai web + ChatGPT. Session IDs not established. The Complete Prompt (4.1 — see Phase 0 for its provenance) governed writing of Sections I–VI. Ontology co-development: the Type 2b category emerged from practice, not from pre-planning (evidence: `5.3.1` and `4.4.3` share `source_chat_id: 30a52e69`). The feedback loop: appendix written after the paper body, then fed back into Section 6 revision (evidence: `4.2.11`, `4.4.13`, `4.2.9` MOD-009). The self-philology story: Word/RTF to Canonical Markdown conversion, chat logs as primary ground truth for metadata reconstruction.

**Input routing:** 4.1 and 4.7.1 recurred across multiple writing sessions as shared context; guidance files (4.4.x) — full session-initiation prompts with explicit success criteria — were the operational grounding for each writing session. Section VIII involved a documented multi-AI cycle: Claude wrote the section, a ChatGPT GPT-5 Thinking session produced targeted revisions to §6.5, the author applied the revisions manually.

**Author role in Phase 1:** prompt author and content reviewer. The human wrote prompts, evaluated outputs, and directed revisions — but within a framework the human had designed (via 4.1). Documentation was not a conscious activity; it was a byproduct of using the tools.

### Phase 2: Stage III — Theoretical reorientation and infrastructure in development

**Anchor figure: Contrast Diptych (Visual 4).** Two panels side by side — same section (Introduction), same author, same topic. Left panel (v1/v2): ghost nodes (null chat ID, unarchived intermediate states), no hub, sparse. Right panel (CFP): session hub, named inputs, related_documents links, epistemic trace connection, dense. The visual point: the documentation difference comes from having a framework, not from having different intentions.

Stage III is where the intellectual content and the documentation infrastructure transform together. Meaningful human control theory integrated into the paper (Section 6). The essentially-contested-concept argument entered (Section 3). The reproduction test rejected and the documentation-adequacy model adopted — these are not separate events but emerged from the same session (`III_4.7.3`, 2026-03-02). The SP reconception emerged from practice during the Section 6 redraft, not from advance planning — supporting the paper's argument (Section 6.3) that documentation practice produces its own requirements.

**Input/output chain (6 sessions, 15 artifacts):** External sources (Santoni de Sio 2016/2018, Lloyd 2025, Gallie 1956, paper v1) → PDL and guidance documents → section drafts (Sections 3 and 6 only; Section 7 designed but deferred) → modlogs. Multi-model orchestration begins here: Sonnet for metadata tasks, Opus for analytical discussion, then a model switch after a failed draft (Opus 4.5 → Sonnet 4.6 for Section 6). See `CFP_4.7.19` for the full input/output analysis.

**Infrastructure requirements — empirical findings from the Stage III record.** The recording infrastructure was in development during Stage III. The gaps in the record show concretely what each infrastructure component is for:

| Missing component | Consequence in the record | What it tells you about traceability |
|---|---|---|
| No git commit around failed Section 6 draft (Jan 28) | Defective draft overwritten; intermediate state irrecoverable. Known only from modlog entry (III_4.2.13 Entry 1) and guidance revision timestamp. | **Version control preserves intermediate states**, including failures. A commit before or after the session would have made the defective draft recoverable via `git show`. |
| No conversation export (Jan 28; also SID-20260124-000000) | Reasoning behind the failure and the guidance revision is lost. The artifact record preserves the *fact* of the failure, not the dialogue. | **Conversation exports preserve reasoning and agency attribution** — who identified the problem, how the decision to revise was reached. |
| No session IDs generated by MHC-W | Session-to-artifact links required retrospective reconstruction via content-matching and timestamps. | **Session identification enables automated traceability.** Without it, every session link is a manual research act. |
| Unexecuted Section 7 design (III_4.4.6) | Guidance and PDL created but no draft produced. Metadata captures this through absence: no `output_completed`, no matching draft file, steering note never included Section 7 in its plan. | **Metadata preserves negative evidence** — what was planned but never done, and the surrounding context that explains why (the CFP reconception redirected priorities). |

These are not errors to narrate apologetically. They are empirical evidence about what a traceability infrastructure requires — derived from the actual record, not from theory. Each row is a concrete case where a specific infrastructure element, had it been in place, would have preserved something that is now lost or required reconstruction. The drafter should present these as findings, connected to the paper's argument that mandated transparency without specified frameworks produces different results than transparency with them.

**Author role in Phase 2:** evolving toward architectural design. The human was no longer only prompting and reviewing outputs but designing the documentation infrastructure itself — the SP structure, the metadata conventions, the tracing condition.

### Phase 3: CFP — Prospective documentation and its surprises

**Anchor figure: Version Chain (Visual 5).** Section 6, three CFP drafts with `derived_from` links, a modlog with 13 entries, a session hub. The visual point: three versions in one session, each addressing specific philosophical problems identified in the prior version. This is what documentable intellectual trajectory looks like concretely.

**Second anchor: Hub Fan-Out (Visual 8).** Artifacts per session, sorted descending, colored by phase. Busiest session: SID-20260401 (11 artifacts). Typical v1/v2 session: 2–4 artifacts. The asymmetry is the visual argument: same author, different framework, different documentation yield.

The CFP phase is now part of the corpus. The chain walk (SID-20260403-213917, findings in CFP_5.3.18) read 12 modlogs, 13 traces, 17 notes, 4 PDLs, 19 section drafts, 7 guidance documents, and 22 hub files. The findings below are what the drafter must narrate for this phase.

**What the CFP rewriting process reveals about AI-assisted writing:**

1. **Non-linear argument development.** Arguments that look locally sound can be structurally wrong in context. The cognitivist-objection reply had a "first component" that survived through planning, Introduction draft, and Section 3 draft — until an Opus structural review confirmed the user's suspicion it was a non sequitur (CFP_4.7.7). Cutting it modified six files. The artifact record preserves the fact it was cut, but the moment it became visible as a problem lives in conversation.

2. **Cascading cross-section dependencies.** The double contestation implementation (CFP_4.2.21) modified all seven paper sections in sequence, plus author review, simulated reviewer letter, and fixes — in one session. Argument-level changes cannot be localized: adding Level 2 (ethical/authenticity) required touching every section because each contained claims that now needed to serve two justificatory routes.

3. **Redundancy as a structural consequence of modular writing.** The redundancy pass (CFP_4.2.22) found core claims stated 5 times each across sections. Three-pass editing achieved ~28% reduction. This is not primarily LLM stylistic verbosity — it is what happens when each section is drafted in a separate session with its own guidance document. The modularity that enables human control (each section gets its own prompt, its own review) produces redundancy that requires a cross-paper editing pass. That pass is a structural necessity of the methodology, not optional polish.

4. **Expansion-then-contraction.** Across 19 draft versions, first drafts expand (argument, examples, scaffolding), later versions compress (cut signposting, hedging, redundancy). Net paper length barely changed (+2%) despite massive internal restructuring. New content (double contestation, self-expression, artistic parallels) was paid for by cutting boilerplate. Compression concentrated at the edges (Introduction −32%, Section 2 −21%); core sections maintained or grew (Section 3 +6%, Section 7 +7%).

5. **Major argument direction changes.** At least three: Section 4 cut entirely + Section 5 derivation changed from institutional to normative (CFP_4.7.6); self-expression/authenticity argument developed from trace through PDL to cross-paper implementation (CFP_4.7.11 → CFP_4.4.19 → CFP_4.2.21); meta-ethical route narrowed to expressivism only after the user found constructivism and particularism arguments unconvincing (CFP_4.2.22 MOD-R1). The artifacts preserve the trajectory of these changes — what they do NOT preserve is the full reasoning behind user interventions (that lives in conversation).

**What the CFP phase reveals about artifact capture:**

6. **Corrections are ad hoc, not systematic.** CFP_4.7.8 carries a correction_note in frontmatter; date errors in 4.2.3 survived until explicit audit. The record self-corrects over time, but corrections are driven by human audit, not system design. Errors persist until someone looks for them.

7. **Template design determines what gets captured.** Modlogs with a "User Feedback/Decision" field capture endorsement evidence 89% of the time; those without capture it 2% of the time (CFP_5.3.9). This is not a quality difference between authors or sessions — it is what happens when the template asks for something versus when it does not. For SP-3: documentation design shapes what gets recorded, independent of conscientiousness. This is the strongest empirical finding for the paper's argument that mandates without frameworks produce different results than specified frameworks.

**What the CFP phase reveals about technological affordances:**

8. **Claude Code enables cross-paper operations.** The double contestation session (CFP_4.2.21) executed 8 implementation steps writing directly to files. This would have required 8+ copy-paste operations in a web session. The platform affordance changes what kinds of revision are attempted, not just how fast they happen.

9. **Multi-model workflow as quality control.** Sonnet for drafting, Opus for structural review. The non-sequitur case (CFP_4.7.7): Sonnet draft preserved the error; Opus confirmed the user's diagnosis. Different models in different roles, orchestrated by the human.

10. **Context exhaustion produces documentation.** The origin chain (6c8d9101 → da6a830c → 5.3.21 → 2ca5888a → 4.1) exists because context limits required manual extraction across sessions. The extraction acts created artifacts (5.3.21, 4.1) that would not exist in an unlimited-context scenario. Technological constraints can produce documentation.

**Author role in Phase 3:** methodology designer and philologist. The human designs the workflow, steers the documentation architecture, and — in producing SP-3 itself — becomes the philologist of the archive the human built.

### Honest assessment

What the record covers and does not. Error typology: platform-driven gaps (no export, no session ID in early phases), user-driven errors (forgetting to activate automation already created), reconstructable gaps (session IDs recovered via content-matching and timestamps), irrecoverable losses (Chat 1 deleted; 6c8d9101 gitignored). Design-for-reconstructability as the normative lesson: the v1/v2 reconstruction succeeded because certain features (stable UUIDs, sufficient artifact structure) were already in place. The CFP reconstruction succeeded because the infrastructure had matured. Both required reconstruction; both succeeded because the archive structure enabled it — not because one phase was better or worse than the other.

Correctability, not completeness: the documentation record improves through correction (chain walk corrections to CFP_5.3.13, correction_note on CFP_4.7.8, date fixes in 4.2.3), not through initial perfection. SP-3's adequacy argument rests on the fact that errors can be found and fixed, not on a claim that the record was right the first time.

Self-referentiality: applying the paper's own criteria to its own record produced findings not available from theoretical analysis — the self-philology concept, four conditions for reconstruction, the correction_note mechanism. The record is an instance of the problem the paper analyses (CFP_4.7.8), not a solved example.

Platform affordances and limitations: what each platform (Claude.ai web, ChatGPT, Claude Code) made possible and what it did not, and how this shaped the archive (PDL-010). The entire reconstruction depends on vendor-specific affordances — Claude.ai retaining conversation history under stable URLs. The documentation framework's feasibility depends on platform decisions outside the scholar's control.

### Synthesis

**Anchor figure: Macro Timeline (Visual 1).** Horizontal timeline Oct 2025 to Apr 2026, five swim lanes (paper writing, ontology development, appendix/SP design, documentation consolidation, CFP adaptation). Key events annotated. The visual tells the full story in one image: where activities overlap, where bursts happen, where the tooling changes.

An overall assessment of the human author's role across the project. A narrative of how that role evolved — from prompt author to architectural designer to philologist — as a function of the changing technological infrastructure. This evolution is not a progress narrative (the phases represent different documentation architectures, not weak-to-strong development). The synthesis must connect back to the paper body's argument (Section 3): what the JPEP case shows about how AI-assisted philosophy is produced and what it means for the role of the author.

Writing produces its own documentation needs — edge cases discovered through practice, not designed in advance (the synthetic node problem, the correction_note mechanism). This supports the paper's argument for experimental, community-developed practice (Section 6.3).

---

## Figures

Each section has an anchor figure. The figures are the narrative spine — they carry the claims, and the prose unpacks them. Full specifications and production notes are in `CFP_4.7.14_EpistemicTrace_SP3VisualDesign.md`. Data sources verified in `CFP_5.3.7_SelectedGraphCandidates.md` (for Graphs 1–3).

### Section–figure mapping

| Section | Anchor figure | What it shows | Data source |
|---------|---------------|---------------|-------------|
| Opening | **Visual 7: Date Histogram** | Artifact creation dates by phase; two activity spikes, gap between | YAML `date` fields |
| Phase 1 | **Visual 3: Feedback Loop** | Appendix → Section 6 revision cycle; recursion | Artifact IDs: 4.2.11, 4.4.13, 4.2.9 |
| Phase 2 | **Visual 4: Contrast Diptych** | Same section, v1/v2 vs CFP documentation density | CFP_5.3.7 Graph 3 |
| Phase 3 | **Visual 5: Version Chain** | Section 6 three-draft trajectory with `derived_from` | CFP_5.3.7 Graph 2 |
| Phase 3 | **Visual 8: Hub Fan-Out** | Artifacts per session, colored by phase | Hub script output |
| Synthesis | **Visual 1: Macro Timeline** | Full project timeline, five swim lanes | Manual from artifact dates |

### Additional figures (use where they serve the argument)

| Visual | Description | When to use |
|--------|-------------|-------------|
| Visual 9 | Connection Density — v1/v2 vs CFP box plot | If the metadata-web density argument needs quantitative support |
| Visual 10 | Interactive Graph — 225-node HTML | Reference as digital supplement; not for print |

### Production

Scripts in `transparency/SCRIPTS/`. Data for Visuals 7 and 8 already extracted. Visuals 3, 4, 5 need Graphviz/Mermaid drafts. Visual 1 (timeline) needs manual construction (Mermaid gantt → matplotlib or TikZ). See CFP_4.7.14 for tool recommendations per figure.

---

## What the Research Must Cover

- The human author's role in each of the three phases, grounded in documentary evidence from the archive
- How that role evolved as a function of the changing technological infrastructure (platforms, workflow tools, documentation conventions)
- The feedback loop (Act 4 from `CFP_4.7.13`): the appendix shaped the paper, demonstrating the recursive character of documentation
- The ontology co-development (Act 2): the documentation system's categories emerged from the attempt to use them, not from a pre-existing plan
- The Stage III theoretical turn: meaningful human control and the essentially-contested-concept argument entered here, and the SP reconception happened in the same session — the artifacts document this
- **Infrastructure requirements for traceability** — derived empirically from Stage III gaps: what version control, conversation export, session IDs, and metadata each preserve; each gap is a concrete case, not a theoretical claim (CFP_4.7.19)
- The self-philology story: retrospective reconstruction of v1/v2 metadata, and the four conditions for successful reconstruction (`CFP_4.7.8`)
- **CFP-phase writing complexity:** non-linear argument development, cascading cross-section dependencies, redundancy as structural consequence of modular writing, expansion-then-contraction pattern, major argument direction changes (findings 1–5 above)
- **CFP-phase artifact capture:** ad hoc corrections, template design determining what gets captured (89% vs 2%), complementary evidence sources (findings 6–7 above)
- **CFP-phase technological affordances:** Claude Code enabling cross-paper operations, multi-model workflow as quality control, context exhaustion producing documentation (findings 8–10 above)
- Platform affordances and limitations: what each platform (Claude.ai web, ChatGPT, Claude Code) made possible and what it did not, and how this shaped the archive (PDL-010)
- An honest assessment of what the record covers and does not cover, including an error typology: platform-driven gaps, user-driven errors, reconstructable gaps, irrecoverable losses (PDL-011, corrected by PDL-016)
- Design-for-reconstructability as the normative lesson from v1/v2: the reconstruction succeeded because certain features (stable UUIDs, sufficient artifact structure) were already in place

## What the Synthesis Must Achieve

- An overall assessment of the human author's role across the project
- A narrative of how that role evolved — from prompt author to architectural designer to philologist
- A connection between this evolution and the changing technological infrastructure
- A connection back to the paper body's argument in Section 3
- Writing produces its own documentation needs — supports the argument for experimental, community-developed practice

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
- Let figures speak. Introduce the figure, give the reader time to look, then explain what it shows. Do not summarize the figure before showing it.
- Describe findings plainly. Say "modlogs with a user-feedback field capture endorsement evidence 89% of the time; those without capture it 2%" — not "the format field effect." Name the evidence, not the label.

---

## Constraints

### Must Include
- The philological research basis: joint author–AI reading across nine sessions, consolidated in CFP_5.3.13 and CFP_5.3.18
- **Phase 0 (origin layer)** — the intellectual chain before 4.1, with its privacy constraints and the provenance of 4.1 itself (human-sourced, Claude-synthesized, human-endorsed)
- The three writing phases with their characterization of the human author's role
- The structural history of the corpus (appendix, SP reconception, appendix elimination) as part of the methodology
- Stage III as a theoretical turning point — meaningful human control and the essentially-contested-concept argument entered here; the artifacts document it
- **Stage III infrastructure requirements table** — four concrete cases where missing infrastructure components (commit, export, session ID, metadata fields) produced specific gaps in the record; presented as empirical findings about what traceability requires, not as apology (CFP_4.7.19)
- The four reconstruction conditions (`CFP_4.7.8`)
- Design-for-reconstructability as the normative lesson from v1/v2
- **Complementary evidence sources** — artifacts and conversations preserve different things; neither alone suffices for the adequacy claim (CFP_5.3.13 §8)
- **Section VIII multi-AI production** — Claude → ChatGPT → manual application as evidence of cross-tool orchestration with documented tool identity
- **CFP-phase findings from the chain walk** (CFP_5.3.18): non-linear argument development, cascading dependencies, redundancy as structural effect of modular writing, expansion-then-contraction, ad hoc corrections, template design shaping capture, multi-model workflow, context exhaustion producing documentation
- **Template design determining what gets captured** — 89% vs 2% endorsement capture depending on whether the template asks for it; strongest empirical finding for the paper's framework argument
- An honest assessment with error typology (corrected per PDL-016: session ID gaps are infrastructure-driven, not user error; user-driven errors = forgetting to activate automation)
- **Still-open documentation gaps** (CFP_5.3.13 §4): Chat 1 (deleted), 6c8d9101 (gitignored)
- Platform affordances and limitations
- Figures as narrative anchors — every major section has a visual that carries the claim

### Must Avoid
- Abbreviating "meaningful human control" as "MHC" in the text
- **Characterising 4.1 as "human-authored" in the sense of human-composed** — correct characterisation: human-sourced, Claude-synthesized, human-endorsed (see CFP_5.3.13 §10)
- **Treating 4.7.1 as a complete document** — it is an incomplete extract of da6a830c, ends mid-sentence
- **Claiming artifact-based reconstruction is self-sufficient** — artifacts preserve structure and scope; conversations preserve agency and provenance; SP-3 must use both
- Framing v1/v2 as "weak" and later phases as "strong" — use "different documentation architectures"
- **Overstating the v1/v2 vs. CFP quality gap** — both phases required reconstruction; both succeeded because the archive structure enabled it (CFP_5.3.13 §3, Correction 1)
- **Drifting toward adversarial verification standards** — the paper argues for good-faith adequacy, not tamper-resistance (CFP_5.3.13 §3, Correction 2)
- Overclaiming completeness
- Attributing temporal discounting or definitional flexibility to this archive
- Reintroducing the reproduction-test model
- Anticipating and rebutting objections — SP-3 is research, not apologetics
- **Coining labels for findings** — describe what was observed plainly, do not give it a name (e.g., say "modlogs with a user-feedback field capture endorsement evidence 89% of the time" — not "the format field effect")
- Presenting redundancy as an LLM defect — it is a structural consequence of modular section-by-section writing with separate guidance documents
- Attributing session ID gaps to user error — the workflow tooling did not generate them in early phases (PDL-016)

### Length
No upper limit. Longer than a standard paper if the research requires it.

---

## Source Mapping

| Element | Source | Reference |
|---------|--------|-----------|
| **Research findings (read first)** | Writer briefing | CFP_5.3.13 |
| **CFP chain walk findings** | Chain walk note | CFP_5.3.18 |
| Origin layer narrative | Steering note | CFP_5.3.15 |
| PreliminaryChat chain verification | Steering note | CFP_5.3.17 |
| Seven-act macro story | Epistemic trace | CFP_4.7.13 |
| Visual design and figure specifications | Epistemic trace | CFP_4.7.14 |
| Graph specifications (verified) | Steering note | CFP_5.3.7 |
| Self-philology + reconstruction conditions | Epistemic trace | CFP_4.7.8 |
| Ur-conversation characterization | Epistemic trace | CFP_4.7.16 |
| Stage III I/O analysis + infrastructure requirements | Epistemic trace | CFP_4.7.19 |
| SP reconception + reproduction test rejection | Epistemic trace | III_4.7.3 |
| Last "Appendix A" design iteration (superseded) | PDL | CFP_5.2.2 |
| Appendix elimination decision | PDL-004 | CFP_5.2.4 |
| SP-3 scope decision | PDL-007 | CFP_5.2.4 |
| Platform affordances | PDL-010 | CFP_5.2.4 |
| Philological standard + error typology | PDL-011 | CFP_5.2.4 |
| Stage III theoretical turn | PDL-012 | CFP_5.2.4 |
| Graph-led narrative structure | PDL-013 | CFP_5.2.4 |
| SP-3 reconception as research paper | PDL-017 | CFP_5.2.4 |
| CFP chain walk methodology and findings | PDL-020 | CFP_5.2.4 |
| Briefing/guidance split decision | PDL-019 | CFP_5.2.4 |
| Section 3 (essentially-contested argument) | Stage III draft | III_5.4.1 |
| Section 6 (meaningful human control) | Stage III draft | III_5.4.2 |
| Three transparency criteria | Paper Section 7 | CFP_5.4.9_Section7_v3.md |

---

*Section Guidance v6 — updated 2026-04-05 (SID-20260405-094022)*
*v5 → v6: Stage III reframed around infrastructure requirements for traceability (four empirical cases); removed "incomplete infrastructure" / "user compensated" narrative; added CFP_4.7.19 to inputs and source mapping*
*v4 → v5: CFP phase included in corpus; figures as narrative spine; CFP chain walk findings as substantive Phase 3 content*
*Workflow: Design | Command: MHC-PDL*
