---
artifact_type: epistemic_trace
date: 2026-04-01
project: JPEP
topic: "Version identification for LLMs: text traces vs. git"
session_id: SID-20260401-033111
source_conversation: ""
archive: MHC-W/00_full_conversations/exported/md/
validated: 2026-04-01
validation: approved_with_edits
---

# Epistemic Trace: Version Identification for LLMs

---

## Key Insights Discovered

1. **`Paper/MDversion/appendix.md` is the v1 appendix — a ground truth baseline, not v2.** The MDversion folder was created to hold the v1 text as a stable reference before the January 2026 edits. The A.4 rewrite (source_chat_6, 2026-01-04/05) produced the v2 content, which lives in `Paper/arXiv/Full_paper_v2.docx`. The MDversion file was committed to git in January 2026 with metadata added to its frontmatter, but its *content* represents the v1 state. This was the user's explicit intent.

2. **Git commit date ≠ publication version.** The initial wrong conclusion was: last git commit to appendix.md was 2026-01-06; arXiv v2 was submitted 2026-01-06; therefore appendix.md = v2. This reasoning failed because git commits happen for reasons other than submission — in this case, the January commits added frontmatter metadata to a v1 file, not v2 content. Commit date and submission date coinciding is coincidence, not identity.

3. **`contains_post_release_addendum: true` is ambiguous.** The field can mean either "this document contains the addendum" or "this document acknowledges that an addendum exists." The appendix.md frontmatter uses it in the second sense — it records the existence and source sessions of the A.4 rewrite without incorporating that rewrite into the file. An LLM reading the field cannot determine which sense is intended from the field alone. The field name conflates description with containment.

4. **The version identification problem.** An LLM asked "is this v1 or v2?" cannot reliably answer from this document. The frontmatter fields `release_baseline` and `contains_post_release_addendum` describe genealogy and extension status — but not *which document* this file is. Git date reasoning (as above) is unreliable. Fetching arXiv gives submission dates but not file-to-version mapping. The only reliable method here was the user's direct clarification of intent.

5. **The LLM-vs-git asymmetry.** Git is the reliable ground truth for tracking what changed, but it is opaque to LLMs working across sessions: it requires explicit tool calls, date cross-referencing, and knowledge of authorial intent behind each commit. Well-formed frontmatter is immediately readable in context. The two layers are complementary: text traces are the first resort for LLMs, git provides safety. The failure mode illustrated here is when text traces are ambiguous *and* git reasoning is applied without understanding authorial intent — producing a confident wrong answer.

---

## Conceptual Map

```
Document frontmatter (appendix.md)
  └── release_baseline: arXiv-2511.08639v1     ← derivation (correct)
  └── contains_post_release_addendum: true      ← ambiguous: contains or acknowledges?
  └── [MISSING] arxiv_version: v1              ← what it IS (absent → reasoning gap)
  └── [MISSING] ground_truth_baseline: true    ← authorial intent (absent → gap)

Git log
  └── last commit: 2026-01-06 "fixed metadata" ← date coincides with v2, misleading
  └── initial commit: 2026-01-04 "Add files via upload" ← content was already v1

arXiv registry
  └── v2 submission date: 2026-01-06           ← external fact, not file identity

User clarification (this session)
  └── "v1 is before the edits in january.      ← authoritative: intent > date inference
       I created it as a ground truth"
```

**Lesson:** When file identity cannot be resolved from the document's own text, the fallback chain is: git → external registry → user. Each step is less reliable than the previous. A self-declaring frontmatter field (`arxiv_version: v1`, `ground_truth_baseline: true`) would have made user clarification unnecessary.

**Design principle:** A document representing a specific publication state should self-declare:
- `arxiv_version:` — v1, v2, etc.
- `arxiv_submission_date:` — YYYY-MM-DD of that version's submission
- `role:` — e.g., `ground_truth_baseline` vs. `working_draft` vs. `final_submission`

`contains_post_release_addendum` should be split into two fields:
- `post_release_addendum_exists: true/false`
- `post_release_addendum_incorporated: true/false`

---

## Preserved Formulations

> "I still believe that for LLMs text traces are better but git provides a safety."

> "how do we know that appendix.md is the v2"

> "no, v1 is before the edits in january. I created it as a ground truth."

The third formulation is the resolution — and the fact that it required a third-turn clarification is itself the evidence that the documentation was insufficient. The diagnostic question ("how do we know?") is the right one to ask at the start of any session using a versioned document. If the document can't answer it from its own text, the frontmatter is incomplete.

---

## Open Questions

- [ ] Should `Paper/MDversion/appendix.md` be annotated with `arxiv_version: v1` and `ground_truth_baseline: true` to make future sessions self-sufficient?
- [ ] Is there a markdown version of the v2 appendix anywhere, or does v2 exist only in docx/pdf form?
- [ ] Should the `Full paper2511.08639v1.md` and section files in MDversion also carry explicit `arxiv_version: v1` fields for symmetry?
- [ ] Does the `contains_post_release_addendum: true` field need a clarifying annotation to distinguish "acknowledges existence" from "incorporates content"?

---

## The Fix Applied (this session)

Two frontmatter additions were made to close the version identification gap:

**`Paper/MDversion/appendix.md`** — added:
```yaml
arxiv_version: v1
v2_diff: "transparency/Canonical_MD/SP5_DevelopmentRecords/5.3_Notes_Type11/II_5.3.3_A4_rewritten.md"
v2_file: "Paper/arXiv/Full_paper_v2.docx (binary — not readable as text)"
```

**`transparency/Canonical_MD/SP5_DevelopmentRecords/5.3_Notes_Type11/II_5.3.3_A4_rewritten.md`** — added:
```yaml
role: v2_diff_appendix_A4
v1_baseline: "Paper/MDversion/appendix.md"
incorporated_in: "Paper/arXiv/Full_paper_v2.docx"
```

The chain is now bidirectional: v1 points to the diff and the binary; the diff points back to v1 and forward to the binary.

## The Broader Lesson

**The documentation system has no version registry.** It is excellent at tracking *how* documents were produced (modification logs, PDLs, epistemic traces) but has no structural answer to "where is version X of document Y?" The gap is acute when a version exists only in binary format (docx/pdf) — the trail goes cold because there is no markdown to read, no frontmatter to find.

**Text-based pointers from the readable v1 to the unreadable v2 are the only bridge an LLM has.**

**The technical context that created the gap:** The project was split across two persistence layers — SwitchDrive (live sync between machines) and GitHub (versioned audit record). While travelling, git was decoupled from the sync folder to avoid conflicts; files were uploaded to GitHub via the web UI ("Add files via upload" commits). This is why the git record is reliable as a *what* (diffs visible) but unreliable as a *when* and *why* (commit messages degrade, sequencing blurs). Text frontmatter is more useful than git history for LLMs precisely because it survives this kind of infrastructure split intact.

## Transfer Notes

### Context to Carry Forward

- `Paper/MDversion/appendix.md` = arXiv **v1** appendix, ground truth baseline. Now self-declares as such.
- v2 appendix A.4 rewrite = `II_5.3.3_A4_rewritten.md`. Now declares its role and both endpoints.
- v2 full paper = `Paper/arXiv/Full_paper_v2.docx` (binary only).
- The A.2 narratives in v1 (branching/convergence at 4.7.3, tangential-becomes-foundational, self-recursion at 4.7.5) are valid sources for graph candidates — they are present in both v1 and v2.

### Recommended Next Steps

1. Consider whether graph candidates from appendix A.2 (branching/convergence, tangential-becomes-foundational, self-recursion) should supplement or replace the three candidates in CFP_5.3.7.
2. Apply the same `arxiv_version:` field to `Paper/MDversion/` section files if they will be referenced in future sessions.

### Warnings / Pitfalls to Avoid

- Do NOT infer publication version from git commit date. Commits happen for metadata, formatting, and housekeeping; dates coinciding with submission dates is coincidence, not identity.
- `contains_post_release_addendum: true` does NOT mean the file contains the addendum — it means the addendum is documented in the source metadata. The field conflates description with containment.
- `release_baseline: arXiv-2511.08639v1` describes derivation, not identity. It does not mean the file is v1.

---

*Trace generated: 2026-04-01*
*Workflow: Brainstorm | Command: MHC-trace*
