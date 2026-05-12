---
project: JPEP
sp: SP4
document_type: Type 4 - Section Guidance
label: CFP_4.4.21_SectionGuidance_ExternalizationImplementation
title: "Section Guidance: Externalization of Supplementary Packages (Implementation)"
version: v1
date: 2026-05-12
session_id: SID-20260512-111348
inputs:
  - "CFP_5.2.5_pdl_AIUsageArchive.md"
feeds_into:
  - "CFP_5.4.14_AIUsageArchive.md"
  - "CFP_5.4.3_Introduction_v2.md"
  - "CFP_5.4.8_Section6_v4.md"
  - "CFP_5.4.9_Section7_v3.md"
  - "CFP_5.4.10_Conclusion_v1.md"
sections_affected: ["1", "5", "6", "7", "closing-note"]
supersedes: ""
validation: approved
status: Active
versioning_convention: git_inplace
---

# Section Guidance: Externalization of Supplementary Packages (Implementation)

## Purpose

This guidance translates the strategic decision in `CFP_5.2.5_pdl_AIUsageArchive.md` into section-scoped to-dos. Each to-do specifies the file to edit, the exact before/after text, and the PDL entry that justifies the change.

The decision: SP-1, SP-2, SP-3 are externalized to a documentation archive (Zenodo or equivalent, persistent DOI). Five surgical inline edits to four existing section drafts re-point in-paper claims to archive claims. One new unnumbered closing section ("AI Usage and Documentation Archive") introduces the archive between §7 Conclusion and References.

---

## §1 Introduction — file: `CFP_5.4.3_Introduction_v2.md`

### Edit 1 — Framework/contribution sentence (paragraph 5 of v2)

**Anchor:** PDL-005 (specification); PDL-001 (rationale).

**Before:**

> The transparency apparatus — supplementary packages SP-1 through SP-5, documenting AI involvement, decision rationale, and process records — is implemented in the work here presented.

**After:**

> The framework specifies five transparency elements (SP-1 through SP-5); the documentation record produced during this paper's writing instantiates them and is archived at the persistent identifier given at the end of this paper.

**Why:** Re-points the self-claim from "in this paper" to "in the archive associated with this paper." Preserves the framework's normative force (specifying five elements) while removing the implicit promise that those elements physically follow within the article.

### Edit 2 — Roadmap final paragraph

**Anchor:** PDL-005 (specification); PDL-002 (unnumbered closing-note placement).

**Before:**

> Section 2 examines structural barriers to disclosure. Section 3 develops the essentially-contested argument. Section 4 addresses conditions for adequate transparency. Section 5 specifies the framework. Section 6 addresses community assessment of documentation adequacy. Section 7 reflects on the paper's own practice.

**After:**

> Section 2 examines structural barriers to disclosure. Section 3 develops the essentially-contested argument. Section 4 addresses conditions for adequate transparency. Section 5 specifies the framework. Section 6 addresses community assessment of documentation adequacy. Section 7 concludes. A closing note describes the documentation archive associated with this paper.

**Why:** The previous roadmap line ("Section 7 reflects on the paper's own practice") was stale — under the 2026-04-09 renumbering, §7 is the Conclusion, not a reflective section. The replacement correctly characterises §7 and introduces the new unnumbered closing note.

---

## §5 Mandatory Transparency — file: `CFP_5.4.8_Section6_v4.md` *(pre-renaming filename; current §5)*

### Edit 3 — Lloyd-engagement sentence + §5.4 Pilot Observations voice

**Anchor:** PDL-005 (specification).

**Before (Lloyd-engagement, end of §5.2):**

> …making binary attribution of text to "AI" or "human" incoherent — as the process documentation in SP-4 illustrates. What matters is whether the intellectual trajectory is traceable to human understanding, which is what SP-4 captures.

**After:**

> …making binary attribution of text to "AI" or "human" incoherent — as the process documentation in this paper's archived SP-4 illustrates. What matters is whether the intellectual trajectory is traceable to human understanding, which is what an SP-4 captures.

**§5.4 Pilot Observations — voice instruction (no exact rewrite mandated; preserve abstraction):** The current paragraph generalises ("Synthesizing them into the coherent account SP-3 requires is intractable if attempted retrospectively"). It already speaks in framework-level voice and need not be changed unless explicit per-paper claims have crept in. Verify on edit: no sentence in §5.4 should claim that *this paper's* SP-3 was the one synthesised. If any such claim is present, re-phrase to maintain the abstract framework voice.

**Why:** Edit 3 keeps the entire SP-1–SP-5 table in §5.2 (the table specifies the framework's transparency elements — this is the framework specification). What changes is two sentences that, in the existing draft, slipped from framework voice into self-claim. "An SP-4" instead of "SP-4" signals genericity. "This paper's archived SP-4" makes the self-instance explicit and locates it in the archive.

---

## §6 Community Assessment — file: `CFP_5.4.9_Section7_v3.md` *(pre-renaming filename; current §6)*

### Edit 4 — §6.4 closing sentence

**Anchor:** PDL-005 (specification).

**Before (last paragraph of §6.4):**

> The self-exemplification of this article creates an immediate opportunity. The supplementary materials represent one implementation. Whether SP-3's tracing claim is supported by SP-4's underlying materials is the question this article invites the community to address.

**After:**

> The self-exemplification of this article creates an immediate opportunity. The documentation archive associated with this article represents one implementation. Whether the SP-3 in that archive supports its tracing claim against the underlying SP-4 materials is the question this article invites the community to address.

**Why:** Replaces "the supplementary materials" (which previously meant the SPs embedded with the paper) with "the documentation archive associated with this article" (the new externalised locus). The community-invitation framing is preserved; only the referent shifts.

**Note on §6.3 (line 43):** The §6.3 paragraph beginning "*Documentation adequacy assessment* examines whether the tracing condition is satisfied. The assessor reads SP-1 through SP-3 and, as needed, SP-4 and SP-5…" is **kept unchanged**. It is framework-level voice (describing what an assessor reads in general). No edit needed.

---

## §7 Conclusion — file: `CFP_5.4.10_Conclusion_v1.md`

### Edit 5 — Opening sentence reformulation

**Anchor:** PDL-005 (specification); PDL-002 (closing-note placement).

**Before (line 20, opening paragraph of §7):**

> The paper's documentation apparatus — SP-1 through SP-5 — functions simultaneously as tracking instrument and as philosophical self-expression: a record of what the author chose to investigate, where they followed the AI, where they overrode it.

**After:**

> The framework specifies a documentation apparatus — SP-1 through SP-5 — that functions simultaneously as tracking instrument and as philosophical self-expression: a record of what an author chose to investigate, where they followed the AI, where they overrode it. The instantiation of that apparatus for the present paper is described, with a persistent identifier, in the closing note that follows this conclusion.

**Why:** Recasts the documentation apparatus claim as a *framework specification* (what the framework requires) rather than a *self-description* (what this paper contains). A second sentence then points the reader to the closing note for the per-paper instantiation, including the persistent identifier.

**Note on the rest of the Conclusion:** The remainder of §7 is unchanged. The honest-acknowledgment paragraph about Neurath's-boat infrastructure, the limitations paragraph, the tracing-condition-ambiguity paragraph (added in `19993b3`), and the closing reflection on traditional process signals are all preserved verbatim. No further inline edits.

---

## Closing note — new section: `CFP_5.4.14_AIUsageArchive.md`

### Structure (per PDL-004; ~430 words, five paragraphs)

1. **Opening paragraph** — paper produced with substantial AI assistance; framework from §5 was applied; tracing requirements stated as (i)/(ii)/(iii); criteria in §6.
2. **Archive intro sentence** — "The full documentation record produced during the writing of this paper is archived at [persistent identifier: forthcoming]. It comprises:"
3. **Bulleted list of archive contents in numerical order:** SP-1, SP-2, SP-3, SP-4, SP-5, source conversations. (Order corrected per user push-back on the original draft's weird ordering.)
4. **Inline excerpts paragraph** — forward promise of two worked examples (one modification-log entry, one figure). Specific picks deferred.
5. **Scope and limits paragraph** — framework was developed alongside the paper; not every phase carried the required infrastructure; gaps themselves are part of the disclosed record; archive is the empirical instance from which the framework's specification was derived, not a model of perfect compliance.

### Frontmatter requirements

```yaml
project: JPEP
sp: SP5
document_type: Type 12 - Section Draft
label: CFP_5.4.14_AIUsageArchive
title: "AI Usage and Documentation Archive (closing note)"
section: "AI Usage and Documentation Archive (unnumbered)"
section_number_new: "unnumbered (between §7 Conclusion and References)"
version: v1
date_created: 2026-05-12
status: Draft
source: "Claude Sonnet 4.6 (Claude Code session SID-20260512-111348)"
produced_by_pdl: CFP_5.2.5_pdl_AIUsageArchive.md
source_guidance: CFP_4.4.21_SectionGuidance_ExternalizationImplementation.md
inputs:
  - CFP_5.2.5_pdl_AIUsageArchive.md
  - CFP_4.4.21_SectionGuidance_ExternalizationImplementation.md
session_id: SID-20260512-111348
cfp_target: "AI Tools in Ethics Research (topical collection)"
word_count: ~430
versioning_convention: git_inplace
validation: approved
```

### Open placeholders (per PDL-006)

- `[persistent identifier: forthcoming]` — Zenodo/OSF DOI to be assigned after archive upload.
- Inline excerpts — which modification-log entry, which figure. Both deferred per user instruction. Forward promise kept as a placeholder sentence.

---

## Verification

After all edits and the new section are committed:

1. **Word count.** Concatenated body of finalized section drafts (CFP_5.4.3 v2, CFP_5.4.5 v4, CFP_5.4.4 v3, CFP_5.4.7 v2, CFP_5.4.8 v4, CFP_5.4.9 v3, CFP_5.4.10 v1) plus CFP_5.4.14: should land near ~7,030 words.

2. **No residual "embedded SP" claims.** Run:

   ```
   grep -ni "this paper.*SP-\|SP-.*this paper\|supplementary materials" \
     transparency/Canonical_MD/SP5_DevelopmentRecords/5.4_SectionDrafts/CFP_5.4.{3,4,5,7,8,9,10,14}*.md
   ```

   Remaining hits should be archive-pointing ("the SP-3 in that archive", "this paper's archived SP-4"), not in-paper-claiming.

3. **Chain coherence.**
   - CFP_4.4.21 frontmatter: `inputs: [CFP_5.2.5]`. ✓ (this file)
   - CFP_5.4.14 frontmatter: `produced_by_pdl: CFP_5.2.5`, `source_guidance: CFP_4.4.21`, `inputs: [CFP_5.2.5, CFP_4.4.21]`.
   - CFP_4.2.32 frontmatter: `inputs: [CFP_5.2.5, CFP_4.4.21]`, `output_completed: CFP_5.4.14_AIUsageArchive.md`.
   - Appended modlog entries (CFP_4.2.14 / 4.2.18 / 4.2.19 / 4.2.30): each `Source:` line references CFP_5.2.5 and CFP_4.4.21.

4. **Roadmap consistency.** Introduction final paragraph names §2 through §7 plus the closing note; matches the section drafts actually present.

5. **Reader-flow check.** Read the paper top-to-bottom (without the archive). The reader should reach an understanding of (a) what the framework requires (§5) and (b) how it would be assessed (§6) without needing to consult the archive. The closing note adds *where the archive lives*, not the framework itself.

---

## Connections (auto)

*To be populated by hub-generation script.*
