---
project: JPEP
document_type: Type 12 - Section Draft
label: CFP_5.4.12_SP2
section: "SP-2 — Navigation and Architecture Guide"
version: v2
date_created: 2026-04-09
status: Draft (provisional)
source: "Claude Sonnet 4.6 (Claude Code session)"
session_id:
  - SID-20260409-150705
  - SID-20260512-111348
  - SID-20260513-003000
date_last_updated: 2026-05-13
produced_by_prompt: ""
inputs:
  - CFP_5.4.11_SP3.md
  - CFP_5.4.9_Section7_v3.md
  - CFP_5.2.4_pdl_SP1_SP2_SP3.md (PDL-006)
cfp_target: "AI Tools in Ethics Research (topical collection)"
versioning_convention: git_inplace
word_count: ~2300
note: "File inventories refreshed 2026-05-12 (SID-20260512-111348) to add: SP-4 entries CFP_4.2.29/30/31/32, CFP_4.4.21, paper_bibliography_FINAL.md; SP-5 entries CFP_5.2.5, CFP_5.3.23–28, CFP_session_log.md, CFP_5.4.13 (SP-1), CFP_5.4.14 (AI Usage Archive). §8 section-numbering table updated to post-2026-04-09 numbering; §2 Type 8a path corrected to SP-5/5.1; §4.1 hubs paragraph reframed honestly about the empty _HUBS directory. v2 (2026-05-13, SID-20260513-003000): SP-1/SP-2/SP-3 moved from 5.4_SectionDrafts/ to top-level sibling folders of SP4_*/SP5_* under transparency/Canonical_MD/ (commit e317eac); new §5.0 added to inventory them at their new paths; §6's §5.4 table trimmed of the three moved rows; §1 updated. Phase 5 final enumeration check pending."
section_numbering: pre_renaming
---

# SP-2 — Navigation and Architecture Guide

## 1. What this document is

SP-2 is a map. It describes the architecture of the JPEP documentation archive: the document type ontology, the metadata infrastructure that links artifacts across sessions and phases, and a structured inventory of everything in the archive.

**Archive layout.** SP-1, SP-2 (this document), SP-3, SP-4, and SP-5 sit as sibling folders at the top level of `transparency/Canonical_MD/`. SP-1, SP-2, and SP-3 each contain a single Markdown file (the archive part itself, retaining its CFP-era `CFP_5.4.X_*.md` filename for git-history continuity across the 2026-05-13 move from `5.4_SectionDrafts/`). SP-4 and SP-5 contain the numbered process-documentation and development-record subfolders inventoried in §§5–6 below. §5.0 inventories the three single-file SP archive parts at their post-move paths.

Read SP-1 before this document for the AI usage declaration and a one-page orientation to the archive. Read SP-3 for the documentation adequacy account — the argument that the record satisfies the attribution, trajectory, and understanding-and-endorsement criteria that Section 7 specifies.

**Provisional note.** File inventories in §§5.0–6 were refreshed 2026-05-12 (SID-20260512-111348) to incorporate artifacts created since 2026-04-09 (the externalization arc plus the SP-1/SP-2 production and review-response sessions), and again 2026-05-13 (SID-20260513-003000) to add §5.0 and trim §5.4 in light of the SP-1/SP-2/SP-3 move. A final enumeration check before submission (Phase 5) is being run alongside the v2 commit.

---

## 2. Document type ontology

JPEP uses eleven document types. Types 1–8 and 11–12 are listed here; the gaps in numbering are artifacts of the v1/v2 naming system and do not correspond to missing types. Types 3, 4, and 12 are JPEP custom types added to the MHC-W v5 core.

| Type | Name | SP location | Phase(s) | Description |
|------|------|-------------|----------|-------------|
| 1 | Complete Prompt | SP-4 / 4.1 | v1/v2 | The foundational input artifact. Human-sourced, Claude-synthesized, human-endorsed. Predates any individual section draft; anticipates the artifact ontology. One file. |
| 2 | Epistemic Traces | SP-4 / 4.7 | all | Records of exploratory dialogues with one-to-many influence on later writing. The asynchronous backbone of the project: strategy sessions, sideways chats, brainstorms, philological analyses. |
| 3 | Section Guidance | SP-4 / 4.4 | all | Versioned constraint documents specifying how a section is to be written. Accumulate mid-course corrections and reviewer feedback across sessions. Produced after traces, consumed by PDLs. JPEP custom type. |
| 4 | Pattern Summaries | SP-4 / 4.3 | all | Methodological lessons distilled from modification logs after a writing session, formatted as operational guidance for the next session's fresh AI instance. Originally called MOD summaries; renamed and formalized in the v1/v2 Section 6 consolidation. JPEP custom type. |
| 5 | Section Summaries | SP-4 / 4.5 | v1/v2 | Maintained continuity across sections during the long v1/v2 writing project. Dormant in CFP — the function is handled by session handoff conventions and hub annotations. |
| 6 | Reference Logs | SP-4 / 4.1 (root) | all | Static bibliography files. Not chain-linked artifacts; maintained by convention rather than by template. |
| 7 | Modification Logs | SP-4 / 4.2 | all | Record what changed during writing and why. Numbered per section (MOD-001 upward); each entry has a bounded subject. The primary evidence layer for attribution and understanding-and-endorsement claims. |
| 8a | Project-level PDLs | SP-5 / 5.1 | all | Prompt development logs that document decisions about what to generate at the project level (e.g., the design of `4.1`, the SP-1/2/3 architecture). The single Type 8a file lives in its own subfolder (`5.1_PaperPromptDevelopmentLog_Type8a/`) — distinct from the Type 8b section-level PDLs in `5.2_SectionPromptDevelopmentLogs_Type8b/`. |
| 8b | Section-level PDLs | SP-5 / 5.2 | all | Prompt development logs that document decisions about how a specific section was to be drafted. Stored in the same folder as 8a; distinguished by scope and naming. |
| 11 | Notes | SP-5 / 5.3 | all | Capture working decisions, organizational choices, and research findings that do not fit other types. Four subtypes distinguished by naming convention and `document_type` frontmatter field: `work_plan`, `decision_record`, `chain_walk`, `briefing`. |
| 12 | Section Drafts | SP-5 / 5.4 | III, CFP | Versioned drafts of paper sections and supplementary packages, treated as explicit artifacts with provenance. Produced by a prompt, consumed by a modification log. JPEP custom type. |

---

## 3. Metadata infrastructure

### 3.1 Session IDs

Every Claude Code session has a session ID of the form `SID-YYYYMMDD-HHMMSS`. Every artifact authored inside a session carries that SID in its `session_id` frontmatter field. Session IDs first appear in Stage III (January 2026); v1/v2 artifacts use chat UUIDs, which play the same role.

### 3.2 Key frontmatter fields

| Field | Meaning |
|-------|---------|
| `session_id` | The Claude Code session in which this artifact was created or last substantially revised |
| `inputs` | Files held in context when this artifact was produced (empirical — records what was actually read) |
| `derived_from` | Structural version chain: which prior artifact this directly supersedes or derives from |
| `feeds_into` | Forward chain: what artifact this was produced to serve |
| `output_completed` | For modification logs: the file produced at the end of the logged session |
| `supersedes` | Explicit version chain for guidance and pattern summary documents |
| `status` | Workflow state: `Draft`, `Active`, `Complete`, `Finalized` |
| `version` | Manually bumped on substantive revision; matches what the modification log calls the version |
| `versioning_convention` | `legacy_multifile` for pre-2026-04-07 per-version files; `git_inplace` (or absent) for the current single-file convention |

### 3.3 Version chains

**Legacy convention (pre-2026-04-07).** Section drafts, section guidance, and pattern summary files were created as separate files per version: `CFP_5.4.8_Section6_v1.md`, `_v2.md`, `_v3.md`, `_v4.md`. These files are preserved as historical artifacts and marked with `versioning_convention: legacy_multifile` when next touched.

**Current convention (post-2026-04-07).** Each section draft / section guidance / pattern summary lives in one file with no version suffix. The file is updated in place; each substantive version is its own git commit; `git log -- <path>` is the version history; `git show <hash>:<path>` recovers any prior version. SP-3 (`CFP_5.4.11_SP3.md`) is the first instance. SP-2 (this file) and SP-1 follow the same convention.

---

## 4. Hub system and graph infrastructure

### 4.1 hub_annotations.yaml

`hub_annotations.yaml` (in `transparency/SCRIPTS/`) is the authoritative source for session topology. It records, for each session hub: the session ID, the chat UUID (for v1/v2 sessions), predecessor sessions (`continues_from`), and the inputs and outputs of that session.

Hub `.md` files (when present in `SP4_ProcessDocumentation/_HUBS/`) are derived from `hub_annotations.yaml`. As of 2026-05-12 the `_HUBS/` directory is empty — earlier hub `.md` files were removed during the UUID/SID recovery work (see `adapt.md` project rule 4: "deleted hub files in git status signal successful UUID/SID recovery, not missing sessions"). The hub-generation script has not been re-run because it is not yet wired to read `hub_annotations.yaml` directly. The YAML file remains the authoritative source for session topology regardless of the derived `.md` state. The architectural decision governing this is in `CFP_5.3.16_Note_HubMetadataArchitectureDecisions.md`.

The `continues_from` field records session predecessor relationships. It uses a YAML list form for complex multi-input flows (e.g. a session that continues both a prior writing session and a prior research session). `continues_from` is a session-level fact, recorded in the YAML only; it does not appear in individual artifact frontmatter.

### 4.2 Graph files

Static SVG figures and interactive HTML graphs are in `transparency/Canonical_MD/_GRAPHS/`:

| File | Description |
|------|-------------|
| `fig1_timeline.svg` | The JPEP writing project on one timeline. Three phase bands, four model identities, major structural events. Used in SP-3 Figure 1. |
| `fig_section6_network.svg` | The Section 6 artifact dependency network. Four-hub layout (SUN1–SUN4). Used in SP-3 Figure 2. |
| `fig6_swimlanes.svg` | Section-level activity across the project. Used in SP-3 Figure 3. |
| `jpep_graph.html` | Full interactive artifact graph (all phases). |
| `jpep_graph_CFP.html` | Interactive graph, CFP phase only. |
| `jpep_graph_III.html` | Interactive graph, Stage III only. |
| `jpep_graph_v1v2.html` | Interactive graph, v1/v2 phase only. |

The interactive HTML graphs support pan, zoom, and node inspection. They are local-only (same evidential status as conversation files): indexed by the SP-5 manifest, available on request. The static SVG figures are the public-facing evidence in SP-3.

Generation scripts for all figures are in `transparency/SCRIPTS/`.

---

## 5.0 SP-1 / SP-2 / SP-3 inventory (single-file top-level archive parts)

The three orientation documents lifted from the paper body by the 2026-05-12 externalization decision live at the top level of `transparency/Canonical_MD/`, each in its own folder containing one Markdown file. Filenames preserve the CFP-era `CFP_5.4.X_*.md` form for git-history continuity across the 2026-05-13 `git mv` (commit `e317eac`); `git log --follow` traverses the rename. `versioning_convention: git_inplace` applies to all three.

| Folder | File | Subject |
|--------|------|---------|
| `transparency/Canonical_MD/SP1_AIUsageDeclaration/` | `CFP_5.4.13_SP1.md` | SP-1 — AI Usage Declaration and Archive Orientation. Models, platforms, roles, and phase/prefix conventions across the project. Short orientation document (~700 words). |
| `transparency/Canonical_MD/SP2_NavigationAndArchitecture/` | `CFP_5.4.12_SP2.md` | SP-2 — Navigation and Architecture Guide. **This file.** Document-type ontology, metadata infrastructure, hub system, and structured inventory of the archive. |
| `transparency/Canonical_MD/SP3_DocumentationAdequacy/` | `CFP_5.4.11_SP3.md` | SP-3 — Documentation Adequacy Account. Four-movement phase-spine reading of the writing process; the argument that the record satisfies Section 7's attribution, trajectory, and understanding-and-endorsement criteria. |

The `document_type: Type 12 - Section Draft` frontmatter on these files is a vestige of their pre-externalization filing as section drafts inside SP-5/5.4. It is retained as a known imprecision until a project decision is made about what to relabel them; this does not affect their function as top-level archive parts.

The closing-note `CFP_5.4.14_AIUsageArchive.md` is **not** an archive part — it is the unnumbered closing section that remains in the paper body and introduces this archive. It is inventoried in §6's §5.4 table.

---

## 5. SP-4 file inventory

SP-4 (`transparency/Canonical_MD/SP4_ProcessDocumentation/`) contains process documentation: Types 1–7 plus the hub files and graph outputs.

### 4.1 — Complete Prompt (Type 1)

| File | Description |
|------|-------------|
| `4.1_Complete_Prompt.md` | The foundational input artifact. Human-sourced from origin chat `6c8d9101`, Claude-synthesized in session `2ca5888a`, human-endorsed. Provenance established in CFP-era philological sessions (CFP_4.7.16, CFP_5.3.15). |

Reference logs (Type 6) are also stored in this folder:

| File | Description |
|------|-------------|
| `citations-complete.md` | Full citation list |
| `paper_bibliography.md` | Paper bibliography (working) |
| `paper_bibliography_FINAL.md` | Paper bibliography (finalized 2026-04-10 after Shoulders bibliography verification pass; see CFP_4.2.31) |
| `references-master-list.md` | Master reference list |
| `references_doc.md` | References document |
| `section5_refs.md` | Section 5 references |

### 4.2 — Modification Logs (Type 7)

**v1/v2 phase** (Roman numeral prefix or plain number):

| File | Section covered |
|------|----------------|
| `4.2.1_ModificationLog_I_Introduction__S01.md` | Introduction |
| `4.2.2_ModificationLog_Section_II__S02.md` | Section II (→ §2) |
| `4.2.3_ModificationLog_Section_III__S02.md` | Section III (→ §2) |
| `4.2.4_ModificationLog_Section_IV__S02.md` | Section IV (→ §2) |
| `4.2.5_ModificationLog_Section_II-III-IV_Consolidation__S02.md` | II/III/IV consolidation into §2 |
| `4.2.6_ModificationLog_Section_V_3__S03.md` | Section V (→ §3) |
| `4.2.7_ModificationLog_Section_VI_4__S04.md` | Section VI (→ §4, later cut) |
| `4.2.8_ModificationLog_Section_VII_5__S05.md` | Section VII (→ §5) |
| `4.2.9_ModificationLog_Section_VIII_6__S06.md` | Section VIII (→ §6) |
| `4.2.10_ModificationLog_Section_IX_7__S07.md` | Section IX (→ §7) |
| `4.2.11_ModificationLog_Appendix.md` | Appendix (v1/v2; eliminated in CFP) |
| `4.2.12_ModificationLog_Title_and_Abstract.md` | Title and abstract |

**Stage III phase** (III_ prefix):

| File | Section covered |
|------|----------------|
| `III_4.2.12_ModificationLog_Section3_v3.md` | Section 3 v3 |
| `III_4.2.13_ModificationLog_Section6_v3.md` | Section 6 v3 (includes failed Jan 28 attempt record) |

**CFP phase** (CFP_ prefix):

| File | Section covered |
|------|----------------|
| `CFP_4.2.14_ModificationLog_Introduction.md` | Introduction |
| `CFP_4.2.15_ModificationLog_Section2.md` | Section 2 |
| `CFP_4.2.16_ModificationLog_Section3.md` | Section 3 |
| `CFP_4.2.17_ModificationLog_Section5.md` | Section 5 |
| `CFP_4.2.18_ModificationLog_Section6.md` | Section 6 (three-draft session; 13 entries) |
| `CFP_4.2.19_ModificationLog_Section7.md` | Section 7 |
| `CFP_4.2.20_ModificationLog_Conclusion.md` | Conclusion |
| `CFP_4.2.21_ModificationLog_DoubleContestation_Implementation.md` | Cross-paper double contestation implementation |
| `CFP_4.2.22_ModificationLog_RedundancyReduction.md` | Cross-paper redundancy reduction (~28% cut) |
| `CFP_4.2.23_ModificationLog_Section3_v3.md` | Section 3 v3 (CFP) |
| `CFP_4.2.24_ModificationLog_MetadataAudit_ProseExplosion.md` | Metadata audit |
| `CFP_4.2.25_ModificationLog_SP3Briefing_PaperSnapshotImport.md` | SP-3 briefing + snapshot import |
| `CFP_4.2.26_ModificationLog_FrontmatterNormalization.md` | Frontmatter normalization pass |
| `CFP_4.2.27_ModificationLog_SP3.md` | SP-3 draft |
| `CFP_4.2.28_ModificationLog_GraphInfrastructure.md` | Graph infrastructure and figure integration |
| `CFP_4.2.29_ModificationLog_SP1_SP2.md` | SP-1 and SP-2 v1 production (2026-04-09) |
| `CFP_4.2.30_ModificationLog_Conclusion_ReviewResponse.md` | Conclusion review response — live Conclusion modlog target (MOD-001 2026-04-09; MOD-002 2026-04-10; MOD-003 2026-05-12 for externalization Edit 5) |
| `CFP_4.2.31_ModificationLog_Bibliography.md` | Bibliography verification pass (MOD-007–010, 2026-04-10) |
| `CFP_4.2.32_ModificationLog_AIUsageArchive.md` | AI Usage and Documentation Archive closing note (CFP_5.4.14), v1 (2026-05-12) |

### 4.3 — Pattern Summaries (Type 4)

| File | Section / scope |
|------|----------------|
| `4.3.1_Section_II_2__S02.md` | Section II (→ §2) |
| `4.3.2_Sections_II-III_later_consolidated_into_2__S02.md` | II/III consolidation |
| `4.3.3_Section_IV_later_consolidated_into_2__S02.md` | Section IV (→ §2) |
| `4.3.4_Section_V_now_3__S03.md` | Section V (→ §3) |
| `4.3.5_Section_VIII_now_6__S06.md` | Section VIII (→ §6) |
| `CFP_4.3.6_PatternSummary_CausalOverreach.md` | Causal overreach pattern (CFP cross-paper) |

### 4.4 — Section Guidance (Type 3)

**v1/v2 phase:**

| File | Section / scope |
|------|----------------|
| `4.4.1_For_Section_IV_S02.md` | Section IV (→ §2) |
| `4.4.2_For_Section_VI_S03.md` | Section VI |
| `4.4.3_For_Section_VII_now_5_from_SP5.2.2__S05.md` | Section VII (→ §5) |
| `4.4.4_For_Section_VIII-A_now_6_from_5.2.1__S06.md` | Section VIII-A (→ §6) |
| `4.4.5_For_Section_VIII-B_from_Sideway_chat.md` | Section VIII-B (mid-course correction from sideways chat) |
| `4.4.6_For_Section_IX_now_7_S7.md` | Section IX (→ §7) |
| `4.4.7_For_Conclusion.md` | Conclusion |
| `4.4.8_Section_6_Revision_Guidance__S06.md` | Section 6 revision |
| `4.4.9_Section_Guidance_Consolidate_Section_2_Systemic_Barriers__S02.md` | Section 2 consolidation |
| `4.4.10_Section_Guidance_Introduction_tone_changes_and_Section_IV__S01-02.md` | Introduction + Section IV |
| `4.4.11_Trajectory_Claims_Check_full_paper_analysis.md` | Cross-paper trajectory claims check |
| `4.4.12_From_Draft_1_Appendix_to_Appendix_A.md` | Appendix A |
| `4.4.13_From_Full_Draft_Appendix_to_Section_6__S06.md` | Bridging guidance: §6.2 and Appendix A.2 simultaneous revision |

**Stage III phase:**

| File | Section / scope |
|------|----------------|
| `III_4.4.4_SectionGuidance_Section3_EssentiallyContested.md` | Section 3 (essentially contested concepts) |
| `III_4.4.5_SectionGuidance_Section6_MHC.md` | Section 6 (meaningful human control integration) |
| `III_4.4.6_SectionGuidance_Section7_Rewrite.md` | Section 7 rewrite (created Feb 2 but never used — no output_completed) |

**CFP phase:**

| File | Section / scope |
|------|----------------|
| `CFP_4.4.14_SectionGuidance_Section7_Additions.md` | Section 7 additions |
| `CFP_4.4.15_CoworkPlan_V1V2ArtifactLinkRecovery.md` | v1/v2 artifact link recovery plan |
| `CFP_4.4.16_CoworkPrompt_HypothesisVerification.md` | Hypothesis verification |
| `CFP_4.4.18_SectionGuidance_AppendixA_v3.md` | Appendix A v3 (superseded by SP-1/2/3 architecture) |
| `CFP_4.4.19_SectionGuidance_SelfExpressionDistribution.md` | Self-expression and double contestation |
| `CFP_4.4.20_SectionGuidance_SP3.md` | SP-3 (current version: v7) |
| `CFP_4.4.21_SectionGuidance_ExternalizationImplementation.md` | Externalization of SP-1/2/3 from paper body — per-section to-dos (2026-05-12) |

### 4.5 — Section Summaries (Type 5)

All v1/v2 phase. Dormant in CFP.

| File | Section covered |
|------|----------------|
| `4.5.1_SectionSummary_Introduction__S01.md` | Introduction |
| `4.5.2_SectionSummary_Section_II__S02.md` | Section II |
| `4.5.3_SectionSummary_Section_III__S02.md` | Section III |
| `4.5.4_SectionSummary_Section_IV__S02.md` | Section IV |
| `4.5.5_SectionSummary_Section_V__S03.md` | Section V |
| `4.5.6_SectionSummary_Section_VI__S04.md` | Section VI |
| `4.5.7_SectionSummary_Section_VIII__S06.md` | Section VIII |
| `4.5.8_SectionSummary_Section_IX__S07.md` | Section IX |
| `4.5.9_SectionSummary_Conclusion__S10.md` | Conclusion |

### 4.7 — Epistemic Traces (Type 2)

**v1/v2 phase:**

| File | Subject |
|------|---------|
| `4.7.1_OriginalTextConversationExtract_Redacted.md` | Original text conversation extract (redacted) |
| `4.7.2_OriginalTextConversation_VisibilityAndStakeholders.md` | Visibility and stakeholders |
| `4.7.3_PreliminaryChat 1.md` | PreliminaryChat 1 |
| `4.7.4_PreliminaryChat 2.md` | PreliminaryChat 2 |
| `4.7.5_PreliminaryChat 3.md` | PreliminaryChat 3 |
| `4.7.6.1_primitive_artifacts_description.md` | Primitive artifacts description |
| `4.7.6.2_EpistemicTrace_Testing_CanonicalTypeDescriptionProduction.md` | Canonical type description testing |
| `4.7.7_ChatGPT_EvaluationsOfFullPaper.md` | ChatGPT evaluations of full paper |
| `4.7.7.1_IsThisAISlop_1.md` | AI slop evaluation 1 |
| `4.7.7.2_IsThisAISlop_2.md` | AI slop evaluation 2 |
| `4.7.7.3_IsThisAISlop_3.md` | AI slop evaluation 3 |
| `4.7.7.4_Integrating_Technological_Observations_into_JPEP.md` | Integrating technological observations |

**Stage III phase:**

| File | Subject |
|------|---------|
| `III_4.7.1_Reasonable_Human_Control_in_AI.md` | Reasonable human control in AI |
| `III_4.7.2_WorkingDrafts_Belong_to_SP5.md` | Working drafts belong to SP-5 |
| `III_4.7.3_MHC_Tracing_SP_Reconception.md` | SP reconception: reproduction-test rejected; SP roles reorganized around documentation adequacy (2026-03-02) |
| `III_4.7.4_CFP_AIEthicsInquiry_BranchAndFitAnalysis.md` | CFP fit analysis |

**CFP phase:**

| File | Subject |
|------|---------|
| `CFP_4.7.5_EpistemicTrace_IntroductionArgumentativeDevelopment.md` | Introduction argumentative development |
| `CFP_4.7.6_EpistemicTrace_Phase2StrategicAnalysis.md` | Phase 2 strategic analysis |
| `CFP_4.7.7_EpistemicTrace_NonSequiturRevision.md` | Non sequitur revision |
| `CFP_4.7.8_EpistemicTrace_SelfReferentialDocumentation.md` | Self-referential documentation (three layers) |
| `CFP_4.7.9_EpistemicTrace_SelectedGraphsVsMegagraph.md` | Selected graphs vs. megagraph design |
| `CFP_4.7.10_EpistemicTrace_VersionIdentificationForLLMs.md` | Version identification for LLMs |
| `CFP_4.7.11_EpistemicTrace_SelfExpressionArgument.md` | Self-expression argument (generative input for double contestation; do not revise) |
| `CFP_4.7.12_EpistemicTrace_SelfExpressionIntegrationDesign.md` | Self-expression integration design (superseded by PDL-009) |
| `CFP_4.7.13_EpistemicTrace_SP3DesignBrainstorm.md` | SP-3 design brainstorm |
| `CFP_4.7.14_EpistemicTrace_SP3VisualDesign.md` | SP-3 visual design (10 figures, 6 recommended) |
| `CFP_4.7.15_EpistemicTrace_AuthenticityArgumentDevelopment.md` | Authenticity argument development |
| `CFP_4.7.16_EpistemicTrace_UrConversationOriginLayer.md` | Ur-conversation / origin layer philology |
| `CFP_4.7.17_EpistemicTrace_HubMetadataArchitectureDesign.md` | Hub metadata architecture design |
| `CFP_4.7.18_EpistemicTrace_ScriptGapAnalysis.md` | Script gap analysis |
| `CFP_4.7.19_EpistemicTrace_StageIII_InputOutputAnalysis.md` | Stage III input/output analysis |
| `CFP_4.7.20_EpistemicTrace_Section6History.md` | Section 6 five-stage history (philological backing for SP-3 Part IV) |

---

## 6. SP-5 file inventory

SP-5 (`transparency/Canonical_MD/SP5_DevelopmentRecords/`) contains development records: Types 8, 11, and 12.

### 5.2 — Prompt Development Logs (Types 8a/8b)

**v1/v2 phase:**

| File | Scope |
|------|-------|
| `5.2.1_pdl_section_viii_now_6_A.md` | Section VIII (→ §6) part A |
| `5.2.2_pdl_section_vii_now_5.md` | Section VII (→ §5) |
| `5.2.3_pdl_section_viii_now_6_B_transparency.md` | Section VIII part B (transparency) |
| `5.2.4_pdl_Appendix_a_initial_steps.md` | Appendix A initial steps |
| `5.2.5_pdl_section_6_after_review.md` | Section 6 after review |
| `5.2.6._first_development_sp2.md` | First SP-2 development |
| `5.2.7_pdl_appendix_1.md` | Appendix 1 |
| `5.2.8 pdl-appendix-2.md` | Appendix 2 |
| `5.2.9_pdl_appendix_overall.md` | Appendix overall |

**Stage III phase:**

| File | Scope |
|------|-------|
| `III_5.2.1_pdl_sections_3_and_6_MHC_integration.md` | Sections 3 and 6 (meaningful human control integration) |
| `III_5.2.2_pdl_Section7_Rewrite.md` | Section 7 rewrite |

**CFP phase:**

| File | Scope |
|------|-------|
| `CFP_5.2.1_pdl_section7_additions.md` | Section 7 additions |
| `CFP_5.2.2_pdl_appendix_v3.md` | Appendix v3 (predecessor PDL; superseded by CFP_5.2.4) |
| `CFP_5.2.3_pdl_selfexpression_integration.md` | Self-expression / double contestation (PDL-000 through PDL-009) |
| `CFP_5.2.4_pdl_SP1_SP2_SP3.md` | SP-1/2/3 design (PDL-004 onward; authoritative SP architecture decisions) |
| `CFP_5.2.5_pdl_AIUsageArchive.md` | AI Usage and Documentation Archive closing note + externalization decision (PDL-001–006, 2026-05-12) |

### 5.3 — Notes (Type 11)

**v1/v2 phase** (plain number or II_ prefix):

| File | Type / subject |
|------|---------------|
| `5.3.1_Artifact_ontology_expansion.md` | Oct 19 — Type 2b distinction named; ontology adds a category to itself |
| `5.3.2_canonical_description.md` | Canonical description |
| `5.3.3_proto_generative_prompt_x.md` | Proto generative prompt |
| `5.3.4_experimental_reproduction_prompt.md` | Experimental reproduction prompt |
| `5.3.5_first_proto_reviewer_prompt.md` | First proto reviewer prompt |
| `5.3.6_Artifact_1_Appendix_A_Documentation_Structure_and_Reproduction_Procedure.md` | Appendix A documentation structure |
| `5.3.7_Artifact_2_Figure_Prompts_for_Appendix_A.md` | Figure prompts for Appendix A |
| `5.3.8_epistemic_trace_emergence_crystallization.md` | Epistemic trace emergence |
| `5.3.9_architectural_guidance.md` | Architectural guidance |
| `5.3.10_section8_guidance.md` | Section 8 guidance |
| `5.3.11_reproduction_pack_demonstration.md` | Reproduction pack demonstration |
| `5.3.12_section_guidance_1_and_6.md` | Section guidance 1 and 6 |
| `5.3.13_appendix_guidance_rewritten.md` | Appendix guidance rewritten |
| `5.3.14_AppendixA_Writing_Reconstruction.md` | Appendix A writing reconstruction |
| `5.3.15_section5_synthesis.md` | Section 5 synthesis |
| `5.3.16_abstract_revision_log.md` | Abstract revision log |
| `5.3.17_nov3_complete_revision_summary.md` | Nov 3 complete revision summary |
| `5.3.18_ModificationLog_Appendix_A2.md` | Modification log, Appendix A.2 |
| `5.3.19_pdl-appendix-a.md` | PDL for Appendix A |
| `5.3.20_modification_tracker_appendix_commentary.md` | Modification tracker, appendix commentary |
| `5.3.21_EpistemicOrigin_InputToSynthesis.md` | Anonymized source dialogue (26K chars); input to `4.1` synthesis |
| `II_5.3.1_necessary_corrections_to_appendix_in_draft_II.md` | Corrections to appendix in draft II |
| `II_5.3.2_Complete Appendix Writing Process.md` | Complete appendix writing process |
| `II_5.3.3_A4_rewritten.md` | A4 rewritten |
| `II_5.3.4_Need_to_reconsider_technological_considerations.md` | Technological considerations |

**Stage III phase:**

| File | Type / subject |
|------|---------------|
| `III_5.3.5_SteeringNote_v3_Section_Revisions.md` | Steering note — v3 section revisions |
| `III_5.3.6_Floridi_style_sheet.md` | Floridi style sheet |

**CFP phase:**

| File | Type / subject |
|------|---------------|
| `CFP_5.3.1_WorkPlan_CFP_Adaptation.md` | Work plan — master plan for the CFP adaptation |
| `CFP_5.3.2_ReviewerB_Section2_PendingDecision.md` | Reviewer B — Section 2 pending decision |
| `CFP_5.3.3_Note_MetadataReportingStructure.md` | Metadata reporting structure |
| `CFP_5.3.4_Note_SkeletonAndConnectionsStatus.md` | Skeleton and connections status |
| `CFP_5.3.5_Note_V1V2MetadataAudit.md` | v1/v2 metadata audit |
| `CFP_5.3.6_CoworkFindings_ArtifactLinks.md` | Cowork findings — artifact links |
| `CFP_5.3.7_SelectedGraphCandidates.md` | Selected graph candidates |
| `CFP_5.3.8_ReviewerLetter_DoubleContestation.md` | Reviewer letter — double contestation |
| `CFP_5.3.9_Note_PhilologicalExplorationLessons.md` | Philological exploration lessons |
| `CFP_5.3.10_Note_UUIDRecovery_CoworkSessions.md` | UUID recovery — cowork sessions |
| `CFP_5.3.11_Note_Chat30a52e69_OntologyDiscoveryAnalysis.md` | Chat 30a52e69 — ontology discovery (Oct 19, Type 2b named) |
| `CFP_5.3.12_Note_SP3_PhaseSummary_WorkingTrace.md` | SP-3 phase summary working trace |
| `CFP_5.3.13_Note_SP3_WriterBriefing.md` | SP-3 writer briefing (entry point for SP-3 drafting; 14 sections) |
| `CFP_5.3.14_Note_ChainWalkPlan.md` | Chain walk plan |
| `CFP_5.3.15_Note_OriginStoryForSP3.md` | Origin story (for SP-3; `4.1` provenance) |
| `CFP_5.3.16_Note_HubMetadataArchitectureDecisions.md` | Hub metadata architecture decisions (authoritative governance) |
| `CFP_5.3.17_Note_PreliminaryChat_ChainVerification.md` | PreliminaryChat chain verification |
| `CFP_5.3.18_Note_CFPChainWalk_Findings.md` | CFP chain walk findings |
| `CFP_5.3.19_Note_SP3_FigureDataSpecs.md` | SP-3 figure data specifications |
| `CFP_5.3.20_Note_SessionLog_Fig6Network.md` | Session log — fig6 network |
| `CFP_5.3.21_Note_SessionLog_GraphAudit.md` | Session log — graph audit |
| `CFP_5.3.22_Note_DecisionRecord_ChatGPTConversationMetadata.md` | Decision record — ChatGPT conversation metadata design |
| `CFP_5.3.23_Note_AssembledPaperBuild.md` | Assembled paper build record (2026-04-09) |
| `CFP_5.3.24_Note_ReviewerB_OpusReview_v1.md` | Reviewer B (Claude Opus 4.6) review of the assembled paper (2026-04-09) |
| `CFP_5.3.25_Note_ShouldersReview_v1.md` + `CFP_5.3.25_ShouldersReview_raw.md` | Shoulders external review (structured note + raw file, 2026-04-09) |
| `CFP_5.3.26_Note_DecisionRecord_SectionRenumbering.md` | Decision record — section renumbering effective 2026-04-09 (old 5/6/7/8 → new 4/5/6/7) |
| `CFP_5.3.27_Note_ReviewResponse_Draft.md` | Consolidated review response draft (Opus + Shoulders) |
| `CFP_5.3.28_Note_ShouldersReview_Evaluation.md` | Shoulders review evaluation, per-item (2026-04-10) |
| `CFP_session_log.md` | Per-session log (`document_subtype: session_log`; appended as-we-go, one section per SID) |

### 5.4 — Section Drafts (Type 12)

**Authoritative current versions** (used in submission):

| File | Content | Convention |
|------|---------|------------|
| `CFP_5.4.3_Introduction_v2.md` | Introduction | legacy_multifile |
| `CFP_5.4.5_Section2_v4.md` | Section 2 | legacy_multifile |
| `CFP_5.4.4_Section3_v3.md` | Section 3 | legacy_multifile |
| `CFP_5.4.7_Section5_v2.md` | Section 5 | legacy_multifile |
| `CFP_5.4.8_Section6_v4.md` | Section 6 | legacy_multifile |
| `CFP_5.4.9_Section7_v3.md` | Section 7 | legacy_multifile |
| `CFP_5.4.10_Conclusion_v1.md` | Conclusion | legacy_multifile |
| `CFP_5.4.14_AIUsageArchive.md` | AI Usage and Documentation Archive (unnumbered closing note in the paper body; introduces the externalized archive) | git_inplace |

> **Note (2026-05-13).** SP-1 / SP-2 / SP-3 were previously listed here (`CFP_5.4.13_SP1.md`, `CFP_5.4.12_SP2.md`, `CFP_5.4.11_SP3.md`). At commit `e317eac` they moved to top-level sibling folders of SP-4 / SP-5 and are now inventoried in §5.0 above. `git log --follow` traverses the rename.

**Superseded per-version files** (historical; not for submission):

`CFP_5.4.3_Introduction_v1.md`, `CFP_5.4.4_Section3_v1.md`, `CFP_5.4.4_Section3_v2.md`, `CFP_5.4.5_Section2_v1.md`, `CFP_5.4.5_Section2_v2.md`, `CFP_5.4.5_Section2_v3.md`, `CFP_5.4.7_Section5_v1.md`, `CFP_5.4.8_Section6_v1.md`, `CFP_5.4.8_Section6_v2.md`, `CFP_5.4.8_Section6_v3.md`, `CFP_5.4.9_Section7_v1.md`, `CFP_5.4.9_Section7_v2.md`

**Stage III drafts:**

| File | Content |
|------|---------|
| `III_5.4.1_Section3_v3.md` | Section 3 v3 (Stage III; source for CFP Section 3 drafts) |
| `III_5.4.2_Section6_v3.md` | Section 6 v3 (Stage III; source for CFP Section 6 drafts) |

**Other:**

| File | Content |
|------|---------|
| `V1_5.4.0_PaperSnapshot_PreConsolidation_Oct18_2025.md` | Full paper snapshot, pre-consolidation (Oct 18, 2025) |
| `_INDEX_5.4.md` | Folder index |

---

## 7. Conversation layer

The `06_conversations/` directory (project root) is gitignored. It contains exported Claude Code session transcripts captured by the SessionEnd hook for every CFP-phase session. These are retained as source material on the author's machine.

v1/v2 conversations remain on the platforms where they were authored (Claude.ai, ChatGPT) and are accessible via the author's accounts. One conversation is excluded even at the manifest layer: the origin chat (`6c8d9101`), which is not anonymized and is gitignored; its intellectual content was extracted in anonymized form into `da6a830c`, which is public. One further v1/v2 conversation was deleted by the user and is not reconstructable.

A manifest note (`CFP_5.3.N_Note_RawConversationsManifest.md`, to be created before submission) indexes all conversation files with session IDs, dates, and fingerprints, and states the retention policy. Conversations are available on request.

---

## 8. Section numbering reference

The paper's section numbering changed across phases as the argument was reorganized and one section was cut.

The paper's section numbering changed across phases as the argument was reorganized, one section was cut, and a second renumbering took effect 2026-04-09 (recorded in `adapt.md` `section_renumbering` and `CFP_5.3.26_Note_DecisionRecord_SectionRenumbering.md`). The table below shows v1/v2 Roman numerals against the current (post-2026-04-09) CFP numbering.

| v1/v2 title (Roman) | Current CFP § | Title |
|---|---|---|
| I — Introduction | §1 | Introduction |
| II — [original §2] | →§2 (consolidated) | Systemic Barriers to Disclosure |
| III — [original §3] | →§2 (consolidated) | (merged into Systemic Barriers) |
| IV — [original §4] | →§2 (consolidated) | (merged into Systemic Barriers) |
| V — [original §5] | §3 | Essentially Contested Concepts and the Community Approach (Why Engage with AI-Assisted Scholarship?) |
| VI — [original §6] | (cut) | Cut in CFP phase |
| VII — [original §7] | §4 | Conditions for Adequate Transparency |
| VIII — [original §8] | §5 | Mandatory Transparency in Practice |
| IX — [original §9] | §6 | Community Assessment of Documentation Adequacy |
| Conclusion | §7 | Conclusion |
| — | (unnumbered closing note) | AI Usage and Documentation Archive (added 2026-05-12; introduces the externalized SP-1–SP-5 archive) |
| Appendix A | (eliminated) | Replaced by SP-1/SP-2/SP-3 in 2026-03-02 SP reconception; SP-1/SP-2/SP-3 externalized to documentation archive 2026-05-12 |

The consolidation of II/III/IV into current Section 2 is documented in `4.2.5_ModificationLog_Section_II-III-IV_Consolidation__S02.md`. The elimination of former Section 4 (old VI) and the appendix are documented in `CFP_5.2.4_pdl_SP1_SP2_SP3.md` (PDL-004). The SP reconception that replaced the appendix with SP-1/2/3 is documented in `III_4.7.3_MHC_Tracing_SP_Reconception.md`. The 2026-04-09 renumbering (which shifted old §5/§6/§7/§8 to current §4/§5/§6/§7) is documented in `CFP_5.3.26_Note_DecisionRecord_SectionRenumbering.md`. The 2026-05-12 externalization of SP-1/SP-2/SP-3 from paper body to documentation archive is recorded in `CFP_5.2.5_pdl_AIUsageArchive.md` (PDL-001).

---

*SP-2 — v1 SID-20260409-150705; v2 SID-20260513-003000 (commit `e317eac`: SP-1/2/3 moved to top-level folders; §5.0 added; §5.4 trimmed). Phase 5 final enumeration check in progress.*
