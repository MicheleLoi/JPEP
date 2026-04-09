---
project: JPEP
document_type: Type 11 - Note
label: CFP_5.3.26_Note_DecisionRecord_SectionRenumbering
document_subtype: decision_record
date_created: 2026-04-09
session_id: SID-20260409-155040
status: Complete
feeds_into: adapt.md (section_renumbering block)
related: CFP_4.2.30_ModificationLog_Conclusion_ReviewResponse
---

# Decision Record: Section Renumbering (2026-04-09)

## Decision

Close the section numbering gap left by the cut of Section 4 (The Dilemma Reconsidered). Renumber sections 5–8 to 4–7.

## Mapping

| Old number | New number | Section title |
|-----------|-----------|---------------|
| 4 | CUT | The Dilemma Reconsidered (cut from CFP version) |
| 5 | 4 | Conditions for Adequate Transparency |
| 6 | 5 | Mandatory Transparency in Practice |
| 7 | 6 | Community Assessment of Documentation Adequacy |
| 8 | 7 | Conclusion |

Sections 1–3 unchanged.

## Why

Section 4 was cut from the CFP adaptation (decision recorded in CFP_5.3.1 work plan, Phase 2). The gap persisted through all CFP drafting because section files were produced independently. Two AI reviewers (CFP_5.3.24, CFP_5.3.25) flagged the missing section and dual-numbering as a structural incoherence that must be resolved before submission.

## What was changed

The 7 working paper section files used by `build_paper.py`:
- `CFP_5.4.3_Introduction_v2.md` — roadmap paragraph updated
- `CFP_5.4.4_Section3_v3.md` — heading format fixed (`# Section 3:` → `# 3.`)
- `CFP_5.4.7_Section5_v2.md` — heading and subsections: 5→4, 5.x→4.x
- `CFP_5.4.8_Section6_v4.md` — heading and subsections: 6→5, 6.x→5.x
- `CFP_5.4.9_Section7_v3.md` — heading and subsections: 7→6, 7.x→6.x
- `CFP_5.4.10_Conclusion_v1.md` — heading: 8→7

Script used: `renumber_sections.py` (project root), with two manual fixes applied afterward.

## What was NOT changed

- Legacy per-version files (`_v1`, `_v2`, `_v3`) — preserved per adapt.md convention
- Archive artifacts (modlogs, traces, PDLs, notes, section guidance) — historical records; use this mapping to resolve old-number references
- SP-2 and SP-3 — SP-internal section numbers are independent; paper cross-references in SPs need updating when SPs are revised

## Policy

All artifacts created before 2026-04-09 use OLD section numbering. Do not update them. Use the mapping table above to resolve references. The authoritative quick-lookup is the `section_renumbering` block in `adapt.md`.

---

*CFP_5.3.26 — SID-20260409-155040*
