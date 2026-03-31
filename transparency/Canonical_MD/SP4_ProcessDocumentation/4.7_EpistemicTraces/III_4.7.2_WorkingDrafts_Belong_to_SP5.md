---
project: JPEP
document_type: Type 10 - Epistemic Trace
label: III_4.7.2_WorkingDrafts_Belong_to_SP5
title: "Epistemic Trace: Working Drafts Belong to SP5"
date: 2026-01-26
session_id: SID-20260202-115248
session_id_precision: exact
source: "Claude Code (no chat ID)"
trigger: "Discussion of how to structure v3 section revisions"
status: Complete
implications: "Ontology revision needed - add Type 12 (Section Drafts) under SP5"
---
# Epistemic Trace: Working Drafts Belong to SP5

**Date:** 2026-01-26
**Context:** Planning the structure for Stage III revisions (Sections 3 and 6 rewrite)
**Production:** Claude Code (no chat ID)

---

## The Problem

We needed to determine where to place new section drafts (Section 3 v3, Section 6 v3) within the transparency structure. Options considered:

1. Place them directly in `Paper/MDversion/` alongside the main paper file
2. Create a staging folder outside the transparency structure
3. Place them within SP5 (Development Records)

---

## The Insight

**Working drafts are development records, not products.**

The paper file (`Full paper2511.08639v3.md`) is the *product*—the thing being produced. But the section drafts that feed into it are *process artifacts*—they document how the product came to be.

This maps cleanly onto the SP structure:

| SP | Contains | Character |
|----|----------|-----------|
| SP-1 | Declaration | Product metadata |
| SP-2 | Tool Specification | Product metadata |
| SP-3 | Contribution Summary | Product metadata |
| SP-4 | Process Documentation | Process artifacts |
| **SP-5** | **Development Records** | **Process artifacts** |

Section drafts are intermediate outputs of the development process. They are:
- Produced using guidance files (which are in SP4/SP5)
- Subject to revision before integration
- Evidence of how the final text was developed

Therefore: **working drafts belong to SP5**.

---

## The Structure

```
SP5_DevelopmentRecords/
├── 5.1_FullPaperPromptDevelopmentLogs_Type8a/
├── 5.2_SectionPromptDevelopmentLogs_Type8b/
├── 5.3_Notes_Type11/
└── 5.4_SectionDrafts/          ← NEW
    ├── III_5.4.1_Section3_v3.md
    └── III_5.4.2_Section6_v3.md
```

**Workflow:**
1. Guidance files (SP4 4.4 or SP5 5.2) specify what to produce
2. Drafting AI produces section draft → saved to SP5 5.4
3. Review/iteration on draft
4. Integration into paper file (`Paper/MDversion/`)
5. Git merge creates version boundary

---

## Why This Matters

1. **Traceability:** The path from guidance → draft → integrated paper is fully documented
2. **Artifact preservation:** Section drafts don't disappear after integration; they remain as evidence
3. **Review flexibility:** Sections can be reviewed/revised independently before collation
4. **Ontological consistency:** All process artifacts live in SP4/SP5; products live elsewhere

---

## Implications for Ontology

**Action required:** Add new artifact type to the ontology:

| Type | Name | Location | Description |
|------|------|----------|-------------|
| 12 | Section Draft | SP5 5.4 | Working draft of a paper section, produced from guidance, prior to integration into main paper file |

**Characteristics of Type 12:**
- Produced by drafting AI using Type 4 (Section Guidance) as input
- Contains section prose ready for integration
- Metadata links to source guidance file
- Versioned (e.g., "v3" indicates Stage III revision)
- Becomes historical artifact after integration (not deleted)

---

## Cross-References

- **Triggered by:** Planning discussion in III_5.2.1_pdl_sections_3_and_6_MHC_integration.md
- **Informs:** Artifact ontology revision (pending)
- **Related:** Git branching strategy for v3 revisions
## Connections (auto)

### Source chat (primary)
- [[_HUBS/CHAT_SID-20260202-115248]]
### Sibling artifacts (same chat)
- [[III_4.4.4_SectionGuidance_Section3_EssentiallyContested]]; [[III_4.4.5_SectionGuidance_Section6_MHC]]; [[III_5.2.1_pdl_sections_3_and_6_MHC_integration]]; [[III_5.4.1_Section3_v3]]

