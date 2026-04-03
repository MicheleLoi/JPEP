---
project: JPEP
document_type: Type 6 - Section Guidance
title: "Cowork Prompt: Hypothesis Verification — V1/V2 Artifact Link Recovery"
date_created: 2026-04-01
status: ready_for_cowork
session_id: SID-20260401
derived_from: "CFP_5.3.6_CoworkFindings_ArtifactLinks.md"
feeds_into: "CFP_5.3.6_CoworkFindings_ArtifactLinks.md"
relevance_for: [cowork, graph-visualization, v1-v2-metadata]

consolidation_note: |
  CFP_5.3.3 (raw Cowork findings) reported chat artifact titles, not SP4/SP5 archive IDs.
  This prompt operationalizes the next step: Claude Code generated testable hypotheses
  mapping chat artifact descriptions to candidate archive files, with explicit verification
  instructions. Cowork tests each hypothesis by reading the candidate file and checking
  whether content matches the description. Verdicts are written back to CFP_5.3.3.
  Claude Code then performs file edits and graph rebuild from confirmed verdicts.
---

# Cowork Prompt: Hypothesis Verification — Artifact Link Recovery

Read `CFP_5.3.6_CoworkFindings_ArtifactLinks.md` for context. Your task is to verify whether specific project files match the chat artifact descriptions recorded there. For each hypothesis below, open the candidate file and check the stated condition. Record your verdict (confirmed / refuted / inconclusive) and the correct archive ID where confirmed.

Save results back into `CFP_5.3.6_CoworkFindings_ArtifactLinks.md` by appending a **Verification Results** section at the bottom.

All file paths are relative to the JPEP project root.

---

## Hypotheses to test

### 4.2.5 inputs

| # | Hypothesis | Candidate file | Test condition |
|---|---|---|---|
| H1 | "Section Guidance: Consolidated Section 2" pasted into ffea5b8a = the section guidance archive file | `transparency/Canonical_MD/SP4_ProcessDocumentation/4.4_SectionGuidance/4.4.9_Section_Guidance_Consolidate_Section_2_Systemic_Barriers__S02.md` | Does it begin with "Objective: Merge current sections 2, 3, and 4..."? |
| H2 | "Pattern Summary Collection Section 2" pasted into ffea5b8a = the Section 2 pattern summary | `transparency/Canonical_MD/SP4_ProcessDocumentation/4.3_PatternSummaries/4.3.1_Section_II_2__S02.md` | Does it reference MOD-19 and MOD-20? |

### 4.2.10 inputs

| # | Hypothesis | Candidate file | Test condition |
|---|---|---|---|
| H3 | "Section Guidance - Section 9" pasted into fa1829d1 = the Section IX guidance archive | `transparency/Canonical_MD/SP4_ProcessDocumentation/4.4_SectionGuidance/4.4.6_For_Section_IX_now_7_S7.md` | Does it specify target length ~1,400–1,600 words and tone "philosophical, analytical (NOT technical specification)"? |
| H4 | "Summary: Introduction Section" pasted into fa1829d1 = the Introduction section summary | `transparency/Canonical_MD/SP4_ProcessDocumentation/4.5_SectionSummaries/4.5.1_SectionSummary_Introduction__S01.md` | Does it begin with "Word count: ~1,400 words, Status: Complete, author-approved, Modification tracker: MOD-1..."? |
| H5 | "Pattern Summary Collection Section 2" = same file as H2 | Same as H2 | Same as H2 — shared input across chats |
| H6 | "Feed-forward guidance from Section 8" = a section guidance file for Section 8→9 transition | List files in `transparency/Canonical_MD/SP4_ProcessDocumentation/4.4_SectionGuidance/` | Is there a file explicitly covering Section 8 or the Section 8→9 transition? If yes, open and verify. |

### 4.2.10 outputs

| # | Hypothesis | Candidate file | Test condition |
|---|---|---|---|
| H7 | "Feed-Forward Guidance - Conclusion" produced in fa1829d1 = the Conclusion guidance archive | `transparency/Canonical_MD/SP4_ProcessDocumentation/4.4_SectionGuidance/4.4.7_For_Conclusion.md` | Does it contain guidance for writing the Conclusion, with a note that it originates from Section IX? |
| H8 | "Section Summary - Section IX" produced in fa1829d1 = the Section IX summary archive | `transparency/Canonical_MD/SP4_ProcessDocumentation/4.5_SectionSummaries/4.5.8_SectionSummary_Section_IX__S07.md` | Does it contain a content overview of Section IX with reference to MOD-001 through MOD-006? |

### 4.2.2 and 4.2.3 shared inputs

| # | Hypothesis | Candidate file | Test condition |
|---|---|---|---|
| H9 | "COMPLETE PROMPT" pasted into both 4177422b and 6e92907a = the complete prompt archive | `transparency/Canonical_MD/SP4_ProcessDocumentation/4.1_CompletePrompt/4.1_Complete_Prompt.md` | Does it begin with or prominently feature "Paper on Journal for AI-Assisted Scholarship Context and Central Problem"? |
| H10 | "EPISTEMIC TRACE: Original Text Extract..." pasted into both = the redacted original text trace | `transparency/Canonical_MD/SP4_ProcessDocumentation/4.7_EpistemicTraces/4.7.1_OriginalTextConversationExtract_Redacted.md` | Does it begin with "PROBLEM (IDENTIFICATION) Core Question: If an argument is developed through AI-assisted dialogue..."? |

### 4.2.3 outputs

| # | Hypothesis | Candidate file | Test condition |
|---|---|---|---|
| H11 | "REFERENCES: Master List for Paper" produced in 6e92907a = the references master list | `transparency/Canonical_MD/SP4_ProcessDocumentation/4.6_ReferenceLogs/references-master-list.md` | Is there a header or provenance note suggesting it was first compiled in October 2025, during or around Section 3 writing? |

### 4.2.1 (structural check — no output_completed expected)

| # | Hypothesis | Candidate file | Test condition |
|---|---|---|---|
| H12 | MOD-004 in the 4.2.1 body = "Meta-Status Declaration Revision" from the revision chat ae493f0b | `transparency/Canonical_MD/SP4_ProcessDocumentation/4.2_ModificationLogs/4.2.1_ModificationLog_I_Introduction__S01.md` | Find MOD-004 in the body. Does its description match "Meta-Status Declaration Revision"? If yes: the revision chat IS the source of 4.2.1's MOD-004 entries — output_completed is self-referential and should be omitted. |

---

## Output format for CFP_5.3.3 appendix

```
## Verification Results (Cowork, 2026-04-01)

| # | Verdict | Archive ID confirmed | Notes |
|---|---|---|---|
| H1 | confirmed / refuted / inconclusive | e.g. 4.4.9 | ... |
...
```
