---
document_type: Pattern Summary
label: CFP_4.3.6_PatternSummary_CausalOverreach
project: JPEP
session_id: SID-20260408-115033
inputs:
  - 06_conversations/exported/JPEP_20260407_161422.md
  - CFP_4.2.27_ModificationLog_SP3.md (MOD-003)
  - CFP_5.4.11_SP3.md (v2 refine pass)
feeds_into:
  - CFP_5.2.4_pdl_SP1_SP2_SP3.md (future SP-1/2/3 PDL entries)
  - CFP_4.4.20_SectionGuidance_SP3.md
derived_from_section: "SP-3 (CFP_5.4.11)"
derived_from_artifact_type: Modification Log
pattern_scope: "Claude's tendency to impose causal/narrative stories on co-occurring facts when drafting transparency material about the writing process itself"
validation: approved
status: Complete
date: 2026-04-08
---

# Pattern Summary: Causal Overreach in Process Narration

**Source:** SP-3 v2 refine pass (session SID-20260407-190627 / SID-20260408-115033), as captured in CFP_4.2.27 MOD-003 and the JPEP_20260407_161422 export. Five of the ~15 substantive corrections in that session were instances of one underlying failure mode.

---

## Key Patterns

**1. Correlation read as causation when two facts co-occur in time.**
The clearest instance: Jan 28 Section 6 redraft failed on Opus 4.5; Mar 2 redraft succeeded on Sonnet 4.6. The draft asserted "the failure prompted the model switch." No archive evidence supports the causal claim — only the temporal sequence. *Rule:* if the only evidence is "X then Y," write "X then Y," not "X caused Y" or "Y in response to X."

**2. Stapling solutions to challenges that share only a phase, not a mechanism.**
§5.2 stapled the SP reconception onto the parallel-tooling problem because both happened in Stage III. Same failure mode at the structural level: temporal/locational co-occurrence read as functional relation. *Rule:* a Solution must answer the named Challenge by mechanism, not by adjacency.

**3. Promoting one-off habits to "formalized practices" the archive does not support.**
Drafted "v1/v2 versioned drafts/guidance/patterns become custom artifact types" — but v1/v2 had no section_draft practice at all, and guidance/patterns were one-off files. The narrative of continuous formalization was imposed where the archive shows discontinuity. *Rule:* before writing "X was formalized," check that X existed in the prior phase in the form being formalized.

**4. Heroizing the one ghost / over-featuring scoped failures.**
The lost Jan 28 draft kept being recruited as a hero or limit case (multiple sections, Figure 5 caption). The user repeatedly de-emphasized it: drafts are transforming artifacts (git's layer), modlogs carry process. *Rule:* a single anomaly is not the defining feature of a phase; mention it once at the level its evidential weight supports, then stop.

**5. Inverting figure-of-merit by importing an unstated baseline.**
Initial framing cast v1/v2 as "the gap" against CFP as "resolution," because Claude implicitly compared v1/v2 to the CFP-phase tooling rather than to the public baseline (no documentation system at all). *Rule:* check whose baseline the figure of merit is anchored on; the reader's, not the most-recently-written code.

---

## Application Notes

These patterns are concentrated in **process-narration writing** — SP-1/SP-2/SP-3 and any future text where Claude is describing the writing of the paper itself rather than its substance. The risk is highest when:
- two facts are nearby in time (model switch, tool change, phase boundary)
- a Challenge/Solution structure invites pairing
- a phase transition tempts a "habits → formalization" arc
- an anomaly is vivid and the rest of the corpus is bulk

Future SP-1/2/3 PDLs and drafting prompts should include an explicit instruction: *cite only causal claims for which the archive has direct evidence (a stated reason, a decision record); otherwise, write the temporal sequence and stop.* The Challenge/Solution sections in particular should be prompted to allow "no in-phase solution; paid down later" as a valid completion.

---

## Links

**Derived from:** CFP_4.2.27 MOD-003 (SP-3 v2 refine session corrections); JPEP_20260407_161422.md export, messages 09:10–09:13 (model-switch correction), 09:11–09:13 (Challenge/Solution stapling), 22:10 (formalization overclaim), 22:13 (ghost over-feature), 16:29 (figure-of-merit inversion).
**Feeds into:** CFP_5.2.4 PDL (next SP-1/2/3 entry), CFP_4.4.20 SectionGuidance_SP3 (Must Avoid section).
