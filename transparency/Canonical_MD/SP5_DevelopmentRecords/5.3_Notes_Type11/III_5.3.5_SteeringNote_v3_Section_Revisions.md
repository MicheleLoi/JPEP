---
project: JPEP
document_type: Type 11 - Steering Note
label: III_5.3.21_SteeringNote_v3_Section_Revisions
title: "Steering Note: Stage III Section 3 and 6 Revisions"
date_created: 2026-01-26
status: Active
source: "Claude Code (no chat ID)"
purpose: "Process guide for v3 section drafting with git workflow"
modeled_on: "epistemic constitutional ai/CLAUDE_UPDATE_BRIEF_SWISS.md"
---

# Steering Note: Stage III Section 3 and 6 Revisions

**Date:** 2026-01-26
**Status:** Active
**Production:** Claude Code (no chat ID)

---

## Overview

This note steers the process of drafting revised Sections 3 and 6 for the JPEP paper (Stage III / v3 revision). It tracks progress, documents git workflow, and ensures traceability.

---

## Progress Checklist

### Phase 1: Preparation (COMPLETE)
- [x] Analyze source materials (Santoni de Sio 2016, 2018; Lloyd 2025; Gallie 1956)
- [x] Develop conceptual framework (essentially contested concepts + MHC)
- [x] Create PDL: III_5.2.1_pdl_sections_3_and_6_MHC_integration.md
- [x] Write epistemic trace: III_4.7.2_WorkingDrafts_Belong_to_SP5.md
- [x] Update reference logs (references_doc.md, references-master-list.md)
- [x] Create Section 3 guidance: III_4.4.4_SectionGuidance_Section3_EssentiallyContested.md
- [x] Create Section 6 guidance: III_4.4.5_SectionGuidance_Section6_MHC.md
- [x] Add "unknown future skills" concept to both guidance files
- [x] Create this steering note

### Phase 2: Git Setup (COMPLETE)
- [x] Create branch `III-v3-mhc-revision` (2026-01-26)
- [x] Create folder structure: `SP5_DevelopmentRecords/5.4_SectionDrafts/` (2026-01-26)
- [x] Create index file for 5.4 (2026-01-26)
- [x] Verify git status shows branch III-v3-mhc-revision (2026-01-26)

### Phase 3: Section Drafting (PENDING)
- [ ] Draft Section 3 using guidance file → save to `5.4_SectionDrafts/III_5.4.1_Section3_v3.md`
- [ ] Review Section 3 draft
- [ ] Draft Section 6 using guidance file → save to `5.4_SectionDrafts/III_5.4.2_Section6_v3.md`
- [ ] Review Section 6 draft

### Phase 4: Integration (PENDING)
- [ ] Create `Paper/MDversion/Full paper2511.08639v3.md` (copy of v1)
- [ ] Replace Section 3 content with draft
- [ ] Replace Section 6 content with draft
- [ ] Update modification logs (4.2.X)
- [ ] Final review of integrated paper

### Phase 5: Git Finalization (PENDING)
- [ ] Stage all changes
- [ ] Commit with message: "Stage III revision: Sections 3 and 6 rewrite (MHC + essentially contested)"
- [ ] Push branch
- [ ] Merge to main (after review)

---

## Edit Targets

### Files to CREATE (on branch)
```
transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/
├── _INDEX_5.4.md
├── III_5.4.1_Section3_v3.md
└── III_5.4.2_Section6_v3.md

Paper/MDversion/
└── Full paper2511.08639v3.md
```

### Files to UPDATE (on branch)
```
transparency/Canonical_MD/SP4_ProcessDocumentation/4.2_ModificationLogs/
├── 4.2.X_ModificationLog_Section3_v3.md (NEW)
└── 4.2.X_ModificationLog_Section6_v3.md (NEW)
```

### Files NOT to edit
- `Full paper2511.08639v1.md` (frozen - arXiv v1/v2)
- Any files outside the transparency structure and Paper folder

---

## Git Workflow

### Branch Creation
```bash
git checkout -b III-v3-mhc-revision
```

### Verify Before Drafting
Before any drafting session, run:
```bash
git status
```
Confirm: `On branch III-v3-mhc-revision`

### After Drafting Session
1. Check what changed:
   ```bash
   git status
   ```

2. Review changes (optional):
   ```bash
   git diff
   ```

3. Stage intended files only:
   ```bash
   git add transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/
   git add Paper/MDversion/Full\ paper2511.08639v3.md
   git add transparency/Canonical_MD/SP4_ProcessDocumentation/4.2_ModificationLogs/
   ```

4. Commit with clear message:
   ```bash
   git commit -m "Stage III revision: Sections 3 and 6 rewrite (MHC + essentially contested)"
   ```

5. Push branch:
   ```bash
   git push -u origin III-v3-mhc-revision
   ```

### Merge (only after full review)
```bash
git checkout main
git merge III-v3-mhc-revision
git push
```

---

## Drafting Instructions

### For Section 3
1. Clear conversation (or start fresh session)
2. Read guidance file: `III_4.4.4_SectionGuidance_Section3_EssentiallyContested.md`
3. Draft section following the structure in guidance
4. Save output to: `5.4_SectionDrafts/III_5.4.1_Section3_v3.md`
5. Include metadata header linking to guidance file

### For Section 6
1. Clear conversation (or start fresh session)
2. Read guidance file: `III_4.4.5_SectionGuidance_Section6_MHC.md`
3. Draft section following the structure in guidance
4. Save output to: `5.4_SectionDrafts/III_5.4.2_Section6_v3.md`
5. Include metadata header linking to guidance file

---

## Source Documents

### Guidance Files (self-sufficient prompts)
- `SP4_ProcessDocumentation/4.4_SectionGuidance/III_4.4.4_SectionGuidance_Section3_EssentiallyContested.md`
- `SP4_ProcessDocumentation/4.4_SectionGuidance/III_4.4.5_SectionGuidance_Section6_MHC.md`

### Development Log
- `SP5_DevelopmentRecords/5.2_SectionPromptDevelopmentLogs_Type8b/III_5.2.1_pdl_sections_3_and_6_MHC_integration.md`

### Primary Sources (for optional deeper context)
- `transparency/TEMP/Santoni de Sio et al. (2016) Why less praise for enhanced performance - OUP.pdf`
- `transparency/TEMP/Santoni_de_sio_frobt-05-00015.xml`
- `transparency/TEMP/Lloyd_frai-08-1635691.xml`

### Current Paper (for integration)
- `Paper/MDversion/Full paper2511.08639v1.md`

---

## Key Concepts for Drafting AI

### Section 3: Why Engage
- Philosophy is an **essentially contested concept** (Gallie 1956)
- Whether AI changes philosophy depends on what is constitutive—which is contested
- **Nature-of-activities** framework (Santoni de Sio 2016): constitutive vs regulative rules
- **Unknown future skills**: prompting → steering → architecture building → ?
- Goal: **track what philosophy becomes** (not prejudge)

### Section 6: Mandatory Transparency
- **MHC framework** (Santoni de Sio & van den Hoven 2018): tracking + tracing conditions
- **Tracing** is the key challenge for scholarship
- **Reproduction test** = tracing verification
- **Reject Lloyd's Standard 4** (text demarcation): process documentation captures *whatever* contribution emerges
- Three nested concerns: epistemic integrity → tracing → tracking what philosophy becomes

---

## Session Log

| Date | Action | Status | Notes |
|------|--------|--------|-------|
| 2026-01-26 | Created PDL and guidance files | Complete | Phase 1 done |
| 2026-01-26 | Created this steering note | Complete | Modeled on epistemic constitutional AI |
| 2026-01-26 | Committed prep files to main | Complete | 8 files, commit 26cba4c |
| 2026-01-26 | Created branch III-v3-mhc-revision | Complete | Phase 2 done |
| 2026-01-26 | Created 5.4_SectionDrafts folder + index | Complete | Type 12 artifacts |
| | Section 3 drafting | Pending | |
| | Section 6 drafting | Pending | |
| | Integration | Pending | |
| | Merge to main | Pending | |

---

## Cross-References

- **PDL:** III_5.2.1_pdl_sections_3_and_6_MHC_integration.md
- **Epistemic Trace:** III_4.7.2_WorkingDrafts_Belong_to_SP5.md
- **Reference Logs:** references_doc.md (Stage III section)
- **Model:** epistemic constitutional ai/CLAUDE_UPDATE_BRIEF_SWISS.md
