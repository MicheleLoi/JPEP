---
project: JPEP
document_type: Type 4 - Section Guidance
label: CFP_4.4.25_SectionGuidance_Section6_FeasibilitySketch
title: "Section Guidance: §6 — The Framework as Feasibility Sketch (post §5/§6 swap)"
section_number: 6
section_title: "A Feasibility Sketch (provisional)"
version: "v1 (CFP-era; supersedes the specification-style §5 of v1.x)"
date_created: 2026-05-13
status: Active
source: "Claude Opus 4.7 (Claude Code session) + user direction"
session_id: SID-20260513-current
validation: approved_with_user_direction
versioning_convention: git_inplace
feeds_into:
  - "Paper/MDversion/CFP_FullPaper_v1.md (v1.8 → v1.9 §5↔§6 swap + new §6 compression)"
related:
  - "CFP_4.4.23_SectionGuidance_Section4.md (Phase 1 §4 collapse)"
  - "CFP_4.4.24_SectionGuidance_Section6_GamingDefense.md (gaming-defense relocation — now §5.4 after swap)"
  - "CFP_4.2.18_ModificationLog_Section6.md (modlog records the §6→§5 renumbering knock-ons)"
  - "CFP_4.2.19_ModificationLog_Section7.md (modlog records the §5→§6 compression)"
inputs:
  - "Paper/MDversion/CFP_FullPaper_v1.md (pre-swap §5 at v1.8, ~852w specification)"
  - "/Users/micheleloi/.claude/plans/don-t-be-lazy-you-refactored-breeze.md (second restructure plan)"
---

# Section Guidance: §6 — The Framework as Feasibility Sketch

## Status

**Current authoritative draft:** `Paper/MDversion/CFP_FullPaper_v1.md` §6 (in-place; v1.9 after this revision).

**Word-count target:** ~450w (target band 400–500w). Pre-swap §5 was 852w. The compression cuts the specification-style elements (SP-N table, nested-concerns ASCII diagram, proximal/distal Mecacci paragraph) and reduces the section to a feasibility sketch.

## Rationale for Compression and Placement

§6 follows §5 (assessment criteria). Its job is to demonstrate that an apparatus satisfying those criteria is *feasible* — not to fully specify one. The specification belongs in the SP-3 documentation-adequacy account in the archive, not in the body paper. The reader has met SP-1 through SP-5 in §5.3's one-line descriptions; §6 elaborates briefly, then closes.

The §5↔§6 swap puts criteria before mechanism, which matches the philosophical reader's question order: "what should this enable?" then "here is one apparatus that enables it." Pre-swap §5 fired the apparatus before its purpose; post-swap §6 lands when the reader is actively asking *how*.

## Architecture

§6 runs as three short paragraphs (no subsections).

1. **Opening MHC paragraph (~100w).** Draw on Santoni de Sio and van den Hoven (2018). MHC distinguishes the **tracking condition** (system outputs covary with the operator's relevant reasons) from the **tracing condition** (outputs traceable to a human person's understanding and endorsement). The framework here adapts these to AI-assisted scholarship on the basis of §3's agent-integrity grounding. Keep the verbatim Santoni de Sio quote on tracing ("systems whose actions and states are not traceable to relevant understanding and endorsing by some human person — no matter how intelligent and reason-responsive they may be — are not under meaningful human control") if it fits the word budget. Drop the weapons-systems-debt-is-conceptual-not-analogical disclaimer (background a sketch doesn't need).

2. **SP-N apparatus paragraph (~200w).** Prose-only characterization of SP-1 through SP-5, one short sentence each. SP-1 (Declaration) is the entry point — a concise statement of how AI was used, what kind of record the reader is entering. SP-2 (Navigation) is a structured index that makes the archive legible. SP-3 (Documentation Account) is the primary site of the tracing claim — the author's argument that the record satisfies the assessment criteria of §5. SP-4 (Process Documentation) is the substance against which SP-3's claim is assessed — **modification logs documenting each substantive revision**, epistemic traces crystallising exploratory turns into stable claims, prompt-development logs documenting what was specified before generation. SP-5 (Development Records) holds versioned section drafts and the section guidance that constrained them — how instructions evolved across the writing process. **The modlog must be named explicitly** in this paragraph (per user direction: "briefly describe our inventions (the modlog etc)" — the concrete invention should be visible to the reader, not abstracted behind SP-4's general label).

3. **Experimental-status / synthesis paragraph (~150w).** Merge former §5.3 + §5.4. The framework is a sketch requiring experimentation: a community of practice tests authors' documentation against reviewers' assessment until shared practices evolve. The documentation requirements are substantial — prompts, modification logs, epistemic traces, session records accumulate rapidly — and synthesising them into SP-3's coherent account is intractable if attempted retrospectively. **AI-assisted synthesis applied immediately after each working session is what makes the framework's documentation requirements implementable.** Be honest about the dependency: a transparency-about-AI framework that depends on AI to maintain its own documentation. The relevant constraint is that synthesis be honest — working from the raw session record rather than from memory reduces the risk of the account becoming more coherent than the process was. The adverse-selection paragraph from former §5.3 can be kept or dropped depending on word budget (§7 already handles community dynamics).

## Hard Constraints

1. **§6 is a sketch, not a specification.** The full specification lives in SP-3 (Documentation Account) in the archive. Do not reintroduce the SP-N table or the nested-concerns ASCII diagram. Do not reintroduce the proximal/distal Mecacci & Santoni de Sio 2020 paragraph.

2. **MHC introduced for the first time here.** Pre-swap §5.1's MHC framing has been removed from §5. The reader meets tracking and tracing in §6 — in the act of seeing how the framework uses them, not as a separate genealogy. Keep the introduction action-oriented.

3. **Cite Santoni de Sio & van den Hoven (2018) and (optionally) Mecacci & Santoni de Sio (2020)**. The latter can be cut if the proximal/distal nuance is genuinely deferred to SP-3. If Mecacci is cut, the bibliography entry stays (it remains an honest debt of the conceptual framing) but the in-text citation drops.

4. **Name the modlog.** Per user direction, the concrete invention should be visible. SP-4's contents (modification logs, epistemic traces, prompts) should be named in the sentence, not abstracted into a category label.

5. **Honest synthesis-needs-AI sentence is non-negotiable.** "A framework requiring transparency about AI use depends, in implementation, on AI assistance to sustain the documentation it requires" (or close paraphrase). This is the paper's most honest self-implicating sentence and §7 cannot bear it alone.

6. **No subsections.** §6 is short enough that subsection headers would create noise rather than navigation.

## What §6 Does Not Do

- **Does not specify how SP-N elements are structured internally.** Internal anatomy (modification log entry format, epistemic trace fields, frontmatter conventions) is SP-2's and SP-3's job in the archive.
- **Does not develop the gaming-defense argument.** That is now §5.4 (former §6.4). §6 inherits its constraints (defense-in-depth, no-single-target) without re-arguing them.
- **Does not introduce the assessment criteria** (attribution / trajectory / understanding-and-endorsement). Those are §5.2.
- **Does not address the proximal/distal tracking nuance.** Cut intentionally. SP-3 in the archive carries this if it carries it anywhere.
- **Does not narrate the framework's genealogy.** The reader needs the framework's *function*, not its development history.

## Cut from Pre-Swap §5 (not relocated)

- **§5.1 paragraph 3 (~165w)** — the abrupt "thickening the tracking claim in two modest ways" paragraph. Reasons: (a) reads abruptly even on careful reading; (b) gaming-defense in §5.4 (former §6.4) now does the structural work this paragraph was attempting; (c) proximal/distal off-topic at sketch level. Mecacci & Santoni de Sio (2020) citation drops if not used elsewhere in new §6.
- **§5.2 nested-concerns ASCII diagram (~30w)** — visual scaffolding the sketch doesn't need; the reader can extract the same nested-concerns relationship from the prose.
- **§5.2 SP-N specification table (~95w)** — replaced by prose one-liners in the new SP-N paragraph.
- **§5.4 second paragraph (~80w) on adverse-selection community dynamics** — overlaps with §7's community-level monitoring claim; cut unless word budget allows.

## Open / Deferred

- **Section title finalization.** "A Feasibility Sketch" is a working title. Alternatives: "The Framework", "Mandatory Transparency in Practice" (preserved from pre-swap), "An Implementable Apparatus." Decide during execution; record in modlog. The pre-swap title "Mandatory Transparency in Practice" remains a credible option if the compression makes "feasibility" feel under-promised.
- **Mecacci citation retention.** If new §6 ends up not citing Mecacci in-text, the bibliography entry retains as an honest debt of the conceptual framework. Confirm at execution.
- **The "adverse-selection dynamics" paragraph fate.** Keep if word budget allows; drop if not. Recorded in modlog.
