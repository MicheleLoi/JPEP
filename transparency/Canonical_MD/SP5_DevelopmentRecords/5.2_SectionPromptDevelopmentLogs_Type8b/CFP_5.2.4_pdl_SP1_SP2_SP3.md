---
artifact_type: pdl
project: JPEP CFP Adaptation
created: 2026-04-02
last_updated: 2026-04-02
status: active
session_id: SID-20260402-105621
output_completed: ""
feeds_into:
  - "SP-1 draft"
  - "SP-2 draft"
  - "CFP_4.4.20_SectionGuidance_SP3.md (v5 — graph-led + research-paper combined)"
  - "SP-3 draft"
source_conversations:
  - session: "SID-20260402-105621"
    exported_as: JPEP_20260402_085522.md
  - session: "SID-20260402-165839"
    exported_as: ""
  - session: "SID-20260403-213917"
    exported_as: ""
  - session: "SID-20260404-103931"
    exported_as: ""
  - session: "SID-20260405-094022"
    exported_as: ""
related:
  - "CFP_5.2.2_pdl_appendix_v3.md (predecessor — appendix-oriented design, partially superseded)"
  - "CFP_4.4.18_SectionGuidance_AppendixA_v3.md (predecessor — content analysis still valid)"
  - "CFP_4.7.8_EpistemicTrace_SelfReferentialDocumentation.md"
  - "CFP_5.3.7_SelectedGraphCandidates.md"
---
# Prompt Development Log (PDL): SP-1 / SP-2 / SP-3 Design

**Scope:** Design of the three supplementary packages that replace Appendix A. The appendix is eliminated; SP-1/2/3 absorb all functions previously served by the appendix plus their own post-reconception roles.

**Predecessor PDL:** `CFP_5.2.2_pdl_appendix_v3.md` (PDL-000 through PDL-003). That PDL designed an "Appendix v3 that feeds SP-2 and SP-3." The architectural decision in PDL-004 below supersedes that framing. Content analysis from CFP_5.2.2 (especially PDL-002/003 corrections) remains valid input.

---

## Development Entries

### PDL-004: No appendix — SP-1/2/3 absorb all appendix functions

| Field | Value |
|-------|-------|
| Date | 2026-04-02 |
| Session | SID-20260402-105621 |
| Authored by | User (architectural decision) |

**Decision:** There is no appendix. SP-1, SP-2, and SP-3 must cover all ground previously covered by Appendix A. No section of the paper body references "Appendix A." The figure moves out of the paper body. Supplementary materials have no word limit.

**Rationale:** The appendix was a compressed pointer to supplementary materials. Now the supplementary materials must stand on their own.

**Impact:** CFP_4.4.18's proposed A.1–A.6 structure is obsolete as a structure (it maps onto an appendix that no longer exists). Its content analysis and the PDL-002/003 corrections remain valid inputs. SP-1/2/3 need to be reconceived as a coherent set, not a migration of appendix subsections.

---

### PDL-005: SP-1 scope — AI usage declaration with philological navigation

| Field | Value |
|-------|-------|
| Date | 2026-04-02 |
| Session | SID-20260402-105621 |
| Authored by | User (steering) + Opus (development) |

**User's formulation:** "This should be short — as near as it gets to an AI usage declaration but with sufficient navigation information to enable philology."

**Decision:** SP-1 is a short document (~2 pages). Two parts: (1) AI usage declaration (models, platforms, roles, period, human role), (2) archive orientation (phases, branch structure, session identification, documentation conventions, entry points to SP-2/3/4/5). Enough that a philologist knows what kind of archive this is before diving in. Not the full map — that's SP-2.

---

### PDL-006: SP-2 scope — map with legend (Option B)

| Field | Value |
|-------|-------|
| Date | 2026-04-02 |
| Session | SID-20260402-105621 |
| Authored by | User (decision) |

**Options considered:**

- **A: Pure index.** File lists, folder structure, pointers. Library catalogue.
- **B: Index + structural reference.** The index, plus the eleven document types explained, plus the metadata infrastructure (session IDs, hub files, version chains). Reader understands the *architecture*.
- **C: Index + structural reference + writing process narrative.** Everything in B, plus the six-phase story, the three v2 patterns, the figure. Architecture *and* history.

**Decision:** Option B. SP-2 is a map with a legend — architecture and navigation, not narrative. The writing process narrative and the figure belong in SP-3, where they serve as evidence for the adequacy argument.

**Rationale:** Decided jointly with SP-3 scope (PDL-007). The narrative is not just orientation — it is the substance of the trajectory claim. Placing it in SP-3 means the reader encounters it as evidence, not background.

**SP-2 contains:**
- File inventories for SP-3/4/5 (updated for all phases: v1/v2, III, CFP)
- The eleven document types with descriptions
- Metadata infrastructure: session IDs, hub files, `derived_from`/`feeds_into`/`output_completed` fields, version chains
- The hub system and graph infrastructure
- Section numbering reference table (old → new)
- No word limit

---

### PDL-007: SP-3 scope — argument + narrative + honest assessment (Option C)

| Field | Value |
|-------|-------|
| Date | 2026-04-02 |
| Session | SID-20260402-105621 |
| Authored by | User (decision) |

**Options considered:**

- **A: Pure argument.** Claims the documentation satisfies the three criteria; presents selected graphs and self-referential story as evidence. Assumes reader knows architecture from SP-2.
- **B: Argument + writing process narrative.** Everything in A, plus the six-phase story and the figure. The narrative is the substance of the trajectory claim.
- **C: Argument + narrative + honest assessment of gaps.** Everything in B, plus the v1/v2 vs CFP comparison (different architectures, not weak vs. strong), the self-referential problem, explicit acknowledgment of what the record doesn't cover.

**Decision:** Option C. SP-3 is the documentation account: it argues adequacy, tells the story, and is honest about limits.

**Rationale:** The paper's credibility depends on not overclaiming. The self-referential documentation trace (CFP_4.7.8) already establishes that the record is an instance of the problem the paper analyses, not a solved example. SP-3 must reflect this.

**SP-3 contains:**
- The adequacy argument: how the documentation satisfies attribution, trajectory, and understanding-and-endorsement
- The writing process narrative (six phases, three patterns from v2 A.2)
- The figure as primary evidence for the v1/v2 phase
- Selected graphs (CFP_5.3.7) as argumentative figures for the CFP phase
- The self-referential documentation story (from CFP_4.7.8)
- The self-philology argument and conditions for retrospective recovery
- Honest assessment: v1/v2 and CFP as different documentation architectures (not weak vs. strong, per PDL-002 correction); explicit gaps
- No word limit

---

### PDL-008: Paper body — appendix references and SP-1/2/3 explanation

| Field | Value |
|-------|-------|
| Date | 2026-04-02 |
| Session | SID-20260402-105621 |
| Authored by | User (decision) + Opus (execution) |

**Issue 1: Appendix references in paper body.** Searched all eight authoritative CFP section drafts for "appendix" or "appendices." No matches found. The CFP adaptation already eliminated all appendix references. No action needed.

**Issue 2: Section 7 needs a paragraph explaining SP-1/2/3.** §7.3 referenced "SP-1 through SP-3" without explaining what they contain. A reader encountering this for the first time would not know what the assessor is being asked to read.

**Action taken:** Inserted a three-sentence explanation after the first mention of SP-1 through SP-3 in §7.3, describing each SP's role (declaration + orientation / navigation + architecture / adequacy argument + evidence + honest assessment). Also added SP-5 to the "as needed" list. Output: `CFP_5.4.9_Section7_v3.md` updated in place (~60 words added).

---

### PDL-009: Graph/metadata coherence verification — heuristic, not audit

| Field | Value |
|-------|-------|
| Date | 2026-04-02 |
| Session | SID-20260402-113529 |
| Authored by | User (steering) |

**Context:** The last SVG graph of the documentation archive is a primary evidence figure for SP-3. The metadata infrastructure (frontmatter fields, session IDs, hub links) was manually inserted by the user across multiple sessions. The graph is generated from this metadata.

**Goal:** Verify that manually inserted metadata are coherent with the content of the documentation. This is NOT a 1:1 correspondence check between graph nodes/edges and metadata fields. The graph is a visualization; the metadata are the substrate. The check is: does the metadata tell a story that is consistent with what the documentation actually contains?

**Method:**
1. Develop a heuristic for coherence (what counts as a red flag — e.g., a `feeds_into` link pointing to a file whose content shows no evidence of that input; a session ID attributed to a file whose content doesn't match that session's known scope)
2. Run the heuristic against the current state of metadata + documentation
3. Flag apparent inconsistencies
4. Present flags to the human user for verification — the user decides what is an error vs. an artifact of legitimate complexity

**Design principle:** The heuristic is a tool for the human, not a replacement for human judgment. Metadata coherence in a complex, multi-phase, multi-platform archive cannot be fully automated. The flags are questions, not verdicts.

---

### PDL-010: SP-3 content — documentation platforms, affordances, and limitations

| Field | Value |
|-------|-------|
| Date | 2026-04-02 |
| Session | SID-20260402-113529 |
| Authored by | User (steering) |

**Decision:** SP-3 must include an assessment of the various AI platforms used in the project and their affordances and limitations for documentation. This is internal to SP-3's honest-assessment section.

**Rationale:** These are exactly the kind of practical details needed to form a community of practice around AI-assisted research documentation. A reader who wants to implement similar transparency needs to know: what did Claude Code make easy? What did Claude.ai web sessions make hard? Where did ChatGPT's project memory help or hinder? What was lost in platform switches? What metadata survived and what had to be reconstructed?

**Scope:** Not a product review. An honest account of how platform design shaped documentation possibilities — what the archive looks like is partly a function of what the tools afforded. This connects to the paper's tracking argument: you cannot track what the tools did not let you record.

---

### PDL-011: SP-3 content — honest analysis and the philological turn

| Field | Value |
|-------|-------|
| Date | 2026-04-02 |
| Session | SID-20260402-113529 |
| Authored by | User (steering) |

**Decision:** The honest-assessment section of SP-3 must NOT frame the data as "v1/v2 = weak, later phases = strong." The analysis must consider the final state of the data (after all reconstruction work, including the SID recovery sessions of 2026-04-02) and examine the various types of errors — including user-driven errors — and their recoverability.

**Error typology to develop:**
- Platform-driven gaps (no export, no session ID, ephemeral context)
- User-driven errors (wrong SIDs, misattributed sessions, inconsistent field names)
- Reconstructability: which errors were recoverable and how (content-matching, timestamp inference, cross-referencing exports)
- Irrecoverable gaps: what is permanently lost and why

**Theoretical insight:** The appropriate standard for this documentation is not the CS audit ideal (complete, machine-verifiable, tamper-evident). That ideal is hard to satisfy and arguably inappropriate for a humanities research archive produced under real working conditions. The better analogy is the **philological ideal**: a scholarly reconstruction of a textual tradition from imperfect witnesses. Philology is scientific — it has methods, criteria, and standards of evidence — but it is designed for exactly this situation: incomplete records, human error, multiple transmission paths, and the need to reason about what the evidence supports rather than to verify a hash.

**Implication for SP-3 argument:** The documentation-adequacy claim is not "we recorded everything perfectly." It is: "the record, including its gaps and errors, is sufficient to support the trajectory and attribution claims the paper makes — and we can show our reasoning." This is a philological adequacy standard, not a CS audit standard.

---

### PDL-012: SP-3 content — Stage III as theoretical turning point

| Field | Value |
|-------|-------|
| Date | 2026-04-02 |
| Session | SID-20260402-165839 |
| Authored by | User (steering) |

**Decision:** SP-3 must explicitly signal that Stage III is where the paper's two core theoretical commitments were introduced: meaningful human control (Santoni de Sio & van den Hoven 2018) and the essentially-contested-concept argument (Gallie 1956 applied to ethical inquiry). These were not present in v1/v2. The artifacts document this development.

**Rationale:** The macro story (CFP_4.7.13, Acts 1–6) covers v1/v2 as plan-driven writing, ontology co-development, feedback loops, and self-philology. But the Stage III theoretical shift — from a venue-design proposal to a philosophically grounded framework — is a distinct story that the documentation captures well. The epistemic trace for the SP reconception (III_4.7.3), the Section 3 v3 draft (III_5.4.1, essentially-contested argument), and the Section 6 v3 draft (III_5.4.2, meaningful human control integration) all document the moment these theoretical commitments entered and reshaped the paper.

**Impact on SP-3 narrative:** The seven-act structure (CFP_4.7.13) needs a clear marker within Act 7 — or as a distinct narrative beat — showing that Stage III was not just a platform shift and infrastructure upgrade but a theoretical reorientation. The artifacts (traces, drafts, modlogs) provide the evidence.

---

### PDL-013: SP-3 structure — graph-led narrative (not text-led)

| Field | Value |
|-------|-------|
| Date | 2026-04-02 |
| Session | SID-20260402-165839 |
| Authored by | User (steering) |

**Decision:** SP-3 is structured around figures, not around a text argument with figures inserted as evidence. Each major section is anchored by a visual from CFP_4.7.14; the prose introduces the figure and unpacks what it shows. The figures are the structure.

**Rationale:** SP-3 is show-and-tell, not a philosophical argument. CFP_4.7.14 specifies 10 visuals with a recommended set of 6. The previous text-led structure (Parts 1–6) underused the visuals and replicated an argumentative posture inappropriate for supplementary documentation material.

**Recommended figure set (from CFP_4.7.14):** Visual 7 (Date Histogram, opening), Visual 1 (Macro Timeline, process narrative spine), Visual 3 (Feedback Loop, embedded in Act 4), Visual 5 (Version Chain, trajectory claim), Visual 4 (Contrast Diptych, framework vs. mandate), Visual 8 (Hub Fan-Out, documentation yield). Visual 10 (Interactive Graph) referenced as digital supplement.

**Impact:** CFP_4.4.20_SectionGuidance_SP3.md rewritten as v2 with graph-led six-section structure. Previous v1 (text-led, six Parts) superseded.

---

### PDL-014: SP-3 opening — orientation for the reader who was told about an appendix

| Field | Value |
|-------|-------|
| Date | 2026-04-02 |
| Session | SID-20260402-165839 |
| Authored by | User (steering) |

**Decision:** SP-3 must open with an explicit orientation: the reader has been told about an appendix; SP-3 is what the appendix became. The documented decision trail must be shown, not summarized.

**Artifacts to cite:**
- `III_4.7.3_MHC_Tracing_SP_Reconception.md` (2026-03-02): reproduction test rejected on three grounds; SP roles reconceived around documentation adequacy; old appendix sections A.1–A.3 → SP-3, A.4–A.5 → SP-2
- `CFP_5.2.4_pdl_SP1_SP2_SP3.md PDL-004` (2026-04-02): appendix eliminated entirely; SP-1/2/3 absorb all functions
- `CFP_5.2.2_pdl_appendix_v3.md` (2026-04-01): last design iteration still called "Appendix A v3" — superseded by PDL-004

**Rationale:** The reader arriving at SP-3 after reading the paper body has been pointed here by references to supplementary materials. Disorienting them with an unmarked structural change is a transparency failure. The opening orientation is itself a demonstration of the documentation-adequacy model: the architecture decisions are documented and citable.

---

### PDL-015: SP-3 content — no anticipated objections; show-and-tell only

| Field | Value |
|-------|-------|
| Date | 2026-04-02 |
| Session | SID-20260402-165839 |
| Authored by | User (steering) |

**Decision:** SP-3 must not anticipate or rebut objections. It shows the record, narrates the process, and assesses honestly. Argumentative posture is inappropriate for supplementary documentation material.

**Impact:** "Anticipated Objections" section removed from CFP_4.4.20. Added to Must Avoid constraints.

---

### PDL-016: SP-3 honest assessment — design-for-reconstructability, not gap apology; error typology corrected

| Field | Value |
|-------|-------|
| Date | 2026-04-02 |
| Session | SID-20260402-165839 |
| Authored by | User (steering) |

**Decision (framing):** The normative lesson from v1/v2 is design-for-reconstructability, not "we had gaps we are acknowledging." The v1/v2 reconstruction succeeded because certain design features were already in place (stable UUIDs, sufficient artifact structure). The reconstruction work demonstrates the *opposite* incentive structure from Section 2's underreporting mechanisms — the author went back months later to recover everything, not minimize it. Temporal discounting and definitional flexibility do not apply and must not be attributed to this archive.

**Decision (error typology):** User-driven errors = forgetting to activate automation already created (e.g. the export hook). Session identifier gaps were infrastructure-driven — the workflow tooling did not generate them in early phases — not user error. PDL-011's error typology is superseded on this point.

**Impact:** CFP_4.7.8's first-layer self-referential claim (documentation reproduces Section 2 mechanisms) flagged as incorrect via `correction_note` in frontmatter. CFP_4.4.20 Part 5 / Honest Assessment section updated accordingly.

---

### PDL-017: SP-3 reconceived as research paper / dissertation chapter; full corpus methodology required

| Field | Value |
|-------|-------|
| Date | 2026-04-03 |
| Session | SID-20260403-093628 |
| Authored by | User (architectural decision) |

**Decision:** SP-3 is no longer show-and-tell supplementary material. It is a research paper / dissertation chapter in its own right.

**Research question:** What role did the human author play in JPEP, and how did that role evolve as a function of the changing technological infrastructure?

**Connection to paper body:** Section 3 argues that the way philosophy is produced — and with it the role of the author — is changing. SP-3 is a case study: the first-person, documented account of what that change looked like from the inside.

**Methodology — full corpus reading, v1/v2 and Stage III only:**
- The methodology is philological, drawing on digital humanities tools. The drafter reads every single document in the v1/v2 and Stage III corpus (files with no prefix, `II_` prefix, or `III_` prefix) across SP4, SP5, and _HUBS — without exception. This completeness is a methodological commitment: it is what distinguishes philological research from cherry-picking.
- Files prefixed `CFP_` are excluded. The CFP adaptation is still in development; the CFP corpus is not yet a stable object of philological study. Philological analysis requires a completed corpus.
- CFP-era hub files in `_HUBS/` are likewise excluded.
- Sub-agents (Sonnet or Haiku) are explicitly permitted and encouraged for systematic reading and note-taking across the corpus.
- Note-taking protocol: for each document, the drafter records artifact ID, type, phase, key content, and relevance to the research question (human author role + evolution).
- Drafting process: full corpus reading with structured notes, then long draft (no length constraint), then re-read and revise, then final SP-3.

**Status (PDL-018):** Research phase complete. This methodology stands but is now executed via the briefing-first approach in PDL-018 below. Full corpus reading remains the standard; the briefing (CFP_5.3.13) distils findings from research sessions that already performed the reading.

**Three phases and their characterization:**
- Phase 1 (v1/v2): Plan-driven writing; tools: Claude.ai web + ChatGPT; session IDs not established; author role: prompt author + content reviewer.
- Phase 2 (Stage III): Platform shift to Claude Code; meaningful human control theory integrated; documentation-adequacy model developed; session IDs partially reconstructed retrospectively; author role evolving toward architectural design; still "imperfect" implementation — session IDs did not exist in real time.
- Phase 3 (CFP): MHC-W infrastructure in place; prospective documentation throughout; errors present but reconstructable; author role: methodology designer + philologist. Not part of the philological corpus but characterized from the drafter's own position within it.

**What carries over from v2:** figures available as evidence (from CFP_4.7.14); three phases as narrative structure; honest assessment with error typology; philological standard (PDL-011); Must Avoid list (no "MHC" abbreviation, no weak/strong framing, no overclaiming, no temporal discounting attribution, no reproduction-test model, no anticipated objections).

**What is superseded from v2:** fixed six-section graph-led structure (PDL-013); figures as structural anchors; show-and-tell register; selective source list (replaced by full-corpus requirement with CFP exclusion); per-section checklists; ~4,500-word target (replaced by no upper limit); the "Opening Move" as a prefatory orientation block (folded into methodology section as corpus structural history).

**The "Opening Move" folding decision:** The structural history (appendix, SP reconception, appendix elimination) should be presented in the methodology section as part of explaining the corpus and its reconstruction history — not as a prefatory block before the research begins. Cite: `III_4.7.3` (SP reconception), `CFP_5.2.4 PDL-004` (appendix elimination), `CFP_5.2.2` (last "Appendix A v3" design, superseded).

**Impact:** CFP_4.4.20_SectionGuidance_SP3.md rewritten as v3 with research-paper methodology. Previous v2 (graph-led show-and-tell) superseded.

---

### PDL-018: Research complete — draft v1/v2 and III now, leave CFP phase as placeholder

| Field | Value |
|-------|-------|
| Date | 2026-04-03 |
| Session | SID-20260403-170017 |
| Authored by | User (decision) |

**Decision:** The research phase for SP-3 is complete. Enough material has been gathered through eight research sessions (SID-20260401 through SID-20260403) to begin drafting. Further research into the CFP phase will happen after the CFP adaptation itself is finished — you cannot do philology on an incomplete corpus.

**Drafting plan:**
- Draft SP-3 covering v1/v2 (Phase 1) and Stage III (Phase 2) in full
- Leave an explicit placeholder section for the CFP phase (Phase 3) — marked as "[CFP PHASE — to be written after CFP adaptation is complete]"
- The CFP placeholder should note what the section will need to cover (platform, methodology infrastructure, documentation characteristics) but not attempt to narrate it yet

**Entry point for the drafter:**
1. Read `CFP_5.3.13_Note_SP3_WriterBriefing.md` — consolidated findings, 12 sections covering the full evidence base
2. Read `CFP_5.3.15_Note_OriginStoryForSP3.md` — origin layer narrative (layers 0–3)
3. Read `CFP_5.2.4_pdl_SP1_SP2_SP3.md` — this PDL, especially PDL-007 (SP-3 scope: Option C), PDL-017 (research question + methodology), and the Must Avoid constraints accumulated across PDL-011 through PDL-016
4. Read `CFP_4.4.20_SectionGuidance_SP3.md` — current section guidance (v3, research-paper structure)
5. For depth on specific topics: source files listed in CFP_5.3.13 frontmatter

**What carries over from PDL-017:** Research question (human author role + evolution); philological methodology (full corpus reading distilled through briefing); three-phase structure; Must Avoid list; figures as evidence; no word limit; honest assessment with error typology; the "Opening Move" folding decision.

**What PDL-018 changes:** The drafter no longer performs fresh corpus reading — the research sessions already did this and the findings are consolidated in CFP_5.3.13. The drafter reads the briefing, reads the PDL, and drafts. Return to source files for depth when the briefing's pointers indicate it. The CFP phase is deferred; draft the document with a marked placeholder.

**Rationale:** Philological analysis requires a completed corpus. v1/v2 and Stage III are complete corpora; the CFP phase is not. Writing the v1/v2 and III sections now — while the research is fresh and consolidated — is more efficient than waiting for the entire project to complete. The CFP placeholder ensures the document's structure anticipates the final section without attempting premature analysis.

---

### PDL-019: Briefing audit complete — what becomes guidance vs. what stays as research notes

| Field | Value |
|-------|-------|
| Date | 2026-04-03 |
| Session | SID-20260403-213917 |
| Authored by | User (decision) + Opus (audit + execution) |

**Context:** §1–§9 of `CFP_5.3.13` (the SP-3 writer briefing) contained false and misleading claims about 4.1's authorship, 4.7.1's completeness, and the sufficiency of artifact-only reconstruction. An Opus audit against §10–§12 identified 17 problems (three clusters: mischaracterisation of 4.1/4.7.1, overclaiming artifact-only reconstruction, structural incompleteness of the phase sequence and input routing). All 17 corrected in-place. The briefing is now internally consistent.

**Decision — two documents, two roles:**

| Document | Role | What belongs here |
|----------|------|-------------------|
| `CFP_5.3.13` (Writer Briefing) | **Research findings** — the drafter reads this first | Evidence, specific findings, detailed modlog-by-modlog analysis, contradiction resolutions, source pointers. Everything the drafter needs to *know*. |
| `CFP_4.4.20` (Section Guidance) | **Drafting instructions** — the prompt that structures writing | Structure, methodology, constraints, Must Include / Must Avoid rules, voice and tone. Everything the drafter needs to *do*. |

**What moves from 5.3.13 into the guidance (4.4.20 v4):**

1. **Phase 0 (origin layer)** — the guidance's Phase 1 description must note that v1/v2 writing was preceded by an origin layer (Chat X → 6c8d9101 → da6a830c → 4.1). The drafter cannot tell the Phase 1 story without it.

2. **4.1 provenance rule** — Must Avoid: characterising 4.1 as "human-authored" in the sense of human-composed. Correct characterisation: human-sourced, Claude-synthesized, human-endorsed. Add to Must Avoid list.

3. **Complementary evidence sources** — the methodology section should state that artifacts and conversations are complementary: artifacts preserve structure and scope; conversations preserve agency and provenance. Neither alone is sufficient. This replaces any implication that artifact-based reconstruction is self-sufficient.

4. **Format field effect** — Must Include: the template effect finding (89% vs. 2% endorsement evidence) as key evidence for the framework argument.

5. **Author corrections** — Must Avoid: overstating v1/v2 vs. CFP quality gap; drifting toward adversarial verification standards.

6. **Updated gap list** — Must Include: the still-open gaps from §5 (Chat 1, modlogs 4.2.1–4.2.3/4.2.5, Chat X, 6c8d9101 privacy constraint). Must note that 4.1 provenance is reconstructed but not encoded in its own frontmatter.

7. **Multi-AI production** — Must Include: Section VIII's Claude → ChatGPT → manual application cycle as evidence of cross-tool orchestration.

**What stays in 5.3.13 only (research notes, not guidance):**

- §8 (II-III-IV consolidation detail) — specific evidence the drafter will use, but the guidance doesn't need to instruct about it
- §9 (artifacts as evidence — what they preserve and cannot) — analytical finding; the guidance incorporates its lesson (complementary evidence sources) without reproducing the analysis
- §10 subsection-level detail (modlog-by-modlog endorsement evidence, guidance file content analysis, Phase B audit detail) — the drafter reads this directly from the briefing
- §12 contradiction-level detail — resolved; the summary in the guidance suffices; 5.3.17 has depth

**Impact:** CFP_4.4.20 updated to v4. Previous v3 (research-paper structure without chain walk findings) superseded.

---

### PDL-020: CFP chain walk — extending the research methodology to the CFP corpus

| Field | Value |
|-------|-------|
| Date | 2026-04-03 |
| Session | SID-20260403-213917 (post-compaction portion) |
| Authored by | User (methodology decision, scope correction, scoping of findings) + Opus (corpus reading, synthesis) |

**Context:** PDL-017 established the philological methodology for SP-3 — full corpus reading, structured notes, evidence-first — but explicitly excluded `CFP_`-prefixed files because "the CFP adaptation is still in development." In this session the user declared the CFP rewriting finished, making the CFP corpus a stable object available for the same treatment.

**Human decision 1 — commissioning the chain walk:**

> "the cfp rewriting is finished. Scientifically explore issues that can be evidenced through the chainwalk. A not useful approach: acting like an immature phd. inventing a thesis, attempting to square the facts to confirm it. A useful approach: perform the chainwalk, note apparent conflicts; try to resolve them logically, identify what you learn: is anything interesting about the complexity of writing? is anything interesting about the ability of artifacts to capture it? is anything interesting about the use of technological affordances? Use those for briefing the writing agent"

This is an explicit methodology instruction: three research questions, evidence-first (not thesis-driven), findings intended as input to the SP-3 writer briefing.

**Human decision 2 — scope correction:**

> "you don't need to read v1/v2; we're done with that and III; now we need to cover CFP phase ground, and finalize"

Claude had spawned agents to read the v1/v2 corpus. The user interrupted and corrected: the chain walk covers the CFP phase only. v1/v2 and Stage III are already consolidated in the briefing (§1–§12). This session completes the research by covering the remaining phase.

**Execution:** Six parallel agents read the full CFP corpus — modlogs (12 files), epistemic traces (13 files), section guidance (7 files), notes + PDLs (17 + 4 files), section drafts (19 files), hubs (22 sessions). Context compaction destroyed the first round of agent results; a second round wrote findings to persistent files. Claude also read key modlogs and traces directly.

**Outputs:**
- `CFP_5.3.18_Note_CFPChainWalk_Findings.md` — synthesised findings under three headings + four cross-cutting observations
- `_chainwalk_complexity.md` — working notes on writing complexity (~4,000 words, 7 sections)
- `_chainwalk_drafts.md` — working notes on draft evolution and guidance-vs-reality comparison
- `_chainwalk_artifacts_tech.md` — working notes on artifact capture ability + technological affordances

**Human decision 3 — format field effect is not a CFP finding:**

The initial synthesis included the "format field effect" (89% vs. 2% endorsement evidence depending on template field presence) as a CFP chain walk finding. The user directed its removal: this finding comes from CFP_5.3.9 (the v1/v2 philological exploration session, SID-20260401-205323) and was already present in the briefing §3. It is not a finding *of* the CFP chain walk; it is a finding *about* the v1/v2 corpus that the chain walk agents picked up from a note file. Removed from CFP_5.3.18, CFP_5.3.13 §13, and CFP_4.4.20. The finding remains where it belongs: in CFP_5.3.9 and in the briefing's pre-existing sections.

**Human decision 4 — integration into briefing and guidance:**

User directed that chain walk findings be compressed into a new §13 of the writer briefing (CFP_5.3.13) and that the section guidance (CFP_4.4.20) be updated with CFP-phase-specific Must Include / Must Avoid items derived from the chain walk. The briefing/guidance split principle from PDL-019 applies: 5.3.13 gets the evidence; 4.4.20 gets the drafting instructions.

**Impact:** PDL-017's CFP exclusion is no longer operative — the CFP corpus has been walked. PDL-018's drafting plan now has a complete evidence base across all three phases. The "CFP placeholder" in the SP-3 draft can be written with the same research depth as v1/v2 and Stage III sections, once the author decides the CFP documentation itself is complete.

---

### PDL-021: Section 6 ethical route — rhetorical correction

| Field | Value |
|-------|-------|
| Date | 2026-04-03 |
| Session | SID-20260403-213917 |
| Authored by | User (diagnosis + framing instruction) + Opus (analysis) + Sonnet (edit) |

**User's diagnosis:**

> "in section 6: [...] This objection confuses the medium of expression with its locus. this is not well stated. it's saying P then not P"

And the framing instruction:

> "The problem is starting with what we don't believe as a statement of our voice, instead of 'one may argue that' or similar"

**Analysis (Opus):** The passage stated the authenticity objection in the paper's own voice ("If this tradition is right, delegating intellectual production to an AI introduces alien agency..."), then immediately dismissed it ("This objection confuses the medium of expression with its locus"). The logical structure was: assert P, then assert not-P. The real argument the paragraph makes — that self-expression lies in designing the generative structure, not in manual production — was obscured by the dismissive transition sentence.

**Two changes applied to `CFP_5.4.8_Section6_v4.md`:**
1. Objection reframed as attributed position: "One might argue that..." — no longer in the paper's own voice
2. Transition sentence replaced: "This objection confuses the medium of expression with its locus" → "But this objection locates self-expression in the wrong place" — says what the paragraph actually argues instead of asserting the negation

**Note:** This is a paper-body edit, not a design decision. It is recorded here rather than in a separate modlog because the change is small (two sentences) and originated from the same session as PDL-019 and PDL-020. A modlog entry for Section 6 (CFP_4.2.18) should reference this PDL entry.

---

### PDL-022: CFP phase included in corpus; graph-led structure restored and combined with research-paper depth

| Field | Value |
|-------|-------|
| Date | 2026-04-04 |
| Session | SID-20260404-103931 |
| Authored by | User (three decisions) + Opus (guidance rewrite) |

**Context:** The guidance (CFP_4.4.20 v4) still excluded CFP-prefixed files from the corpus and treated Phase 3 as a placeholder the drafter would characterize from the outside. Meanwhile, the CFP chain walk (PDL-020, SID-20260403-213917) had already read the full CFP corpus and produced substantive findings (CFP_5.3.18). Separately, the graph-led structure from PDL-013 — figures as narrative spine, prose unpacking what each figure shows — had been dropped when SP-3 was reconceived as a research paper (PDL-017). The user judged that the graph-led approach made SP-3 more readable and should be brought back.

**Human decision 1 — CFP phase is no longer excluded:**

> "CFP phase is no longer excluded."

The PDL-017 exclusion ("files prefixed CFP_ are excluded — the CFP adaptation is still in development") and the PDL-018 placeholder plan ("leave an explicit placeholder for CFP phase") are both superseded. The CFP corpus has been walked (PDL-020); its findings are consolidated in CFP_5.3.18 and CFP_5.3.13 §13. The drafter works from these consolidated findings; all three phases are covered.

**Human decision 2 — combine graph-led structure with research-paper depth:**

> "The guidance should use the graphs. The idea of writing around the graph was a good one, but that artifact had a lot of good ideas that make SP3 better to read. The two should be combined."

The PDL-013 approach (figures as structural anchors, each section built around a visual) and the PDL-017 approach (research paper with depth, no length constraint, philological methodology) are combined. Each major section gets an anchor figure; the prose introduces the figure, lets the reader look, and unpacks what it shows. The result is a research paper that reads visually — depth and accessibility together.

**Human decision 3 — no bloated language:**

> "Don't use bloated language like 'format field effect'."

Added to Must Avoid: do not coin labels for findings. Describe what was observed plainly. Say "modlogs with a user-feedback field capture endorsement evidence 89% of the time; those without capture it 2%" — not "the format field effect."

**Impact:** CFP_4.4.20 rewritten as v5. Three changes from v4:

1. **Corpus scope:** All three phases included. The exclusion rationale removed. The methodology section notes that research was completed across prior sessions; the drafter reads the briefing and chain walk findings first, returns to source files for depth.

2. **Structure:** Each section mapped to an anchor figure. Section–figure mapping table added. The figures carry the narrative; the prose unpacks them. A reader who saw only the figures and captions should grasp the main story. Visual specifications from CFP_4.7.14 integrated directly.

3. **Phase 3 content:** Rewritten from a placeholder characterization into a substantive research section with ten numbered findings from the CFP chain walk (CFP_5.3.18), organized under three headings: writing complexity, artifact capture, technological affordances. These are drafting instructions, not research notes — the drafter must narrate them as Phase 3 evidence.

**What is superseded:** PDL-017's CFP exclusion; PDL-018's CFP placeholder plan; the v4 guidance's passive treatment of figures ("available as evidence, placed where the drafter decides"). The PDL-013 graph-led structure is restored in combination with PDL-017's research-paper methodology.

**What carries forward unchanged:** Research question (PDL-017); philological approach; three-phase structure; Must Avoid list (extended with the no-labels rule); honest assessment; error typology (corrected per PDL-016); briefing/guidance split (PDL-019).

**What is also superseded:** PDL-017's "full corpus reading requirement" as a drafting-time instruction. The corpus was read jointly by the author and Claude across nine research sessions. The drafter works from the consolidated findings (CFP_5.3.13, CFP_5.3.18), consulting source files only to clarify specific doubts.

---

### PDL-023: Stage III I/O analysis complete; infrastructure requirements as empirical findings

| Field | Value |
|-------|-------|
| Date | 2026-04-05 |
| Session | SID-20260405-085500 (research), SID-20260405-094022 (integration) |
| Authored by | User (framing correction) + Opus (trace + guidance rewrite) |

**Context:** The Stage III input/output analysis (CFP_4.7.19, SID-20260405-085500) mapped all 6 sessions and 15 artifacts. An initial draft framed the gaps as "incomplete infrastructure" and narrated the user's developing skill with Claude Code. The user corrected this: MHC-start and CLAUDE.md were in place; errors in field names and missing SIDs are routine session errors, not infrastructure immaturity; SP-3 should not tell the story of the user learning to use Claude.

**Human decision — infrastructure in development, not user learning curve:**

The user reframed the Stage III findings: both the failed draft (no commit, no export) and the session errors (non-standard fields, missing SIDs) are instances of infrastructure that was still being developed. The useful thing for SP-3 is not narrating the development, but noting what each missing element was for. Each gap is a concrete case where a specific infrastructure component — had it been in place — would have preserved something now lost or requiring reconstruction.

The user also identified that the failed draft would have been fully recoverable via `git show` if a commit had been made. This is not a structural limitation of the methodology; it is a missed step. The JSONL for that session is also gone.

**Impact:** CFP_4.4.20 updated to v6. Phase 2 section rewritten:

1. **Removed:** "incomplete infrastructure" narrative, "user compensated manually," toolkit feature comparison (no session IDs, no CLAUDE.md, non-standard fields presented as evidence of MHC-W immaturity).

2. **Added:** Infrastructure requirements table — four concrete cases (no commit, no export, no session ID, unexecuted design) with what each gap means for traceability. Framed as empirical findings, not apology.

3. **Added to Must Include / What the Research Must Cover:** the infrastructure requirements table as a required element of SP-3's Phase 2 narrative.

**What is superseded:** The v5 Phase 2 section's framing of Stage III as a story of toolkit immaturity and user compensation.

**What carries forward unchanged:** Everything else from PDL-022 (three-phase corpus, graph-led structure, no bloated language, consolidated research basis).

---

## Open design questions

- Drafting sequence: SP-1 first (shortest), SP-2 next (structural), SP-3 last (depends on the other two)? — likely yes, but SP-3 can begin in parallel given briefing readiness
- Visual production: scripts in `transparency/SCRIPTS/`; data for Visuals 7 and 8 already extracted; Visuals 3, 4, 5 need Graphviz/Mermaid drafts before final production

---

*PDL generated: 2026-04-02*
*Last updated: 2026-04-05 (PDL-023 added, session SID-20260405-094022)*
*Workflow: Design | Command: MHC-PDL*
