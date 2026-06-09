# Compression proposals for v1.11 → v1.12

**Baseline commit:** 5f93850
**Generated:** 2026-06-09 in SID-20260609-095833
**Target reduction:** ~700 words
**Current body word count:** ~8,930
**Target body word count post-compression:** ~8,230–8,300

**Decision pattern:** Each candidate stands alone. User reads each, decides keep/cut/modify. Selected cuts are applied to `CFP_FullPaper_v1.md` (and propagated to relevant staging files where applicable) before the v1.12 assembly + build.

**Off-limits (Earp v1.11 insertions, not touched):**
- §3.3 AUTOGEN paragraph (Porsdam Mann et al. 2023 — "Porsdam Mann, Earp, Møller, Vynn & Savulescu (2023), defending a model…")
- §5.4 disaggregation paragraph (Earp, Porsdam Mann, Sawai & Wangmo 2026 — "Because there is no settled view…")
- §4 JME policy paragraph (Earp, Shahvisi & Frith 2025 — "Movement at the policy layer is already visible…")
- §3.3 Williams inversion defense paragraph ("A scrupulous reader will register an inversion…")
- §3.3 Cordasco footnoted engagement paragraph ("A natural objection from informal welfare-oriented analysis…")

---

### C-01 — §6 — Compress the SP-1–SP-5 inventory paragraph (~110 words saved)

**Location:** §6, paragraph beginning "Five elements compose the apparatus, each answering…"

**Words saved:** ~110

**BEFORE (with context):**

> As Santoni de Sio and van den Hoven put it… the question that, on §3's reading, Kierkegaard's truth-as-subjectivity makes constitutive and that Williams's agent-integrity tradition requires.
>
> **Five elements compose the apparatus, each answering to one or more of the three criteria specified in §5.2. SP-1 (Declaration) is the entry point — a concise statement of how AI was used and what kind of record the reader is entering; it discharges *attribution* at the orientation level, before any deeper inspection. SP-2 (Navigation) is a structured index that makes the archive legible: the document-type ontology and the metadata infrastructure linking each section to the process materials that produced it. SP-2 is structurally enabling for all three criteria — without it, none of them is assessable in practice. SP-3 (Documentation Account) is the primary site of the tracing claim — the author's argument that the record satisfies the criteria of §5; because the account must speak to each criterion, SP-3 carries all three explicitly rather than structurally. SP-4 (Process Documentation) is the substance against which SP-3's claim is assessed: *modification logs* documenting each substantive revision (prior text, revised text, source model and session, reasoning); *epistemic traces* crystallising exploratory turns into stable claims; *prompt-development logs* documenting what was specified before generation. SP-4 is where *attribution* becomes locatable and where the modlog's reasoning fields make *understanding-and-endorsement* inspectable at the level of individual decisions. SP-5 (Development Records) holds the section guidance that constrained drafting and the pattern summaries distilling what successive revisions taught — the *before* and *after* of the writing project's instructions to itself; the *intellectual trajectory* is what becomes visible across SP-5's versioned instructions, and the constraints the author placed on themselves before generation are evidence for *understanding-and-endorsement* of a different kind than SP-4 supplies. The focus is explanation, not reconstruction: the canonical trace of what changed and why is the modlog in SP-4, more compressed and more narrative than any complete snapshot could be.**
>
> The framework is a sketch requiring experimentation…

**AFTER (same context):**

> As Santoni de Sio and van den Hoven put it… the question that, on §3's reading, Kierkegaard's truth-as-subjectivity makes constitutive and that Williams's agent-integrity tradition requires.
>
> Five elements compose the apparatus, each answering to one or more of the three criteria specified in §5.2. SP-1 (Declaration) is the entry point — a concise statement of how AI was used and what record the reader is entering; it discharges *attribution* at the orientation level. SP-2 (Navigation) is a structured index — the document-type ontology and metadata infrastructure linking each section to the process materials that produced it — and is structurally enabling for all three criteria. SP-3 (Documentation Account) is the primary site of the tracing claim: the author's argument that the record satisfies the criteria of §5, speaking to each criterion explicitly. SP-4 (Process Documentation) is the substance against which SP-3's claim is assessed: *modification logs* documenting each substantive revision (prior text, revised text, source model and session, reasoning); *epistemic traces* crystallising exploratory turns into stable claims; *prompt-development logs* documenting what was specified before generation. SP-4 is where *attribution* becomes locatable and the modlog's reasoning fields make *understanding-and-endorsement* inspectable at the level of individual decisions. SP-5 (Development Records) holds the section guidance that constrained drafting and pattern summaries distilling what successive revisions taught; the *intellectual trajectory* becomes visible across SP-5's versioned instructions, and the constraints the author placed on themselves before generation are evidence for *understanding-and-endorsement* of a different kind than SP-4 supplies. The canonical trace of what changed and why is the modlog in SP-4 — more compressed and more narrative than any complete snapshot could be.
>
> The framework is a sketch requiring experimentation…

**Justification:** This paragraph carries significant redundancy: "before any deeper inspection," "makes the archive legible," "without it, none of them is assessable in practice," "because the account must speak to each criterion … rather than structurally," and "The focus is explanation, not reconstruction" all duplicate work already done by the surrounding clauses. Each SP keeps its function statement and its criterion-mapping; only the connective throat-clearing is trimmed.

---

### C-02 — §7 — Compress the "limitations should be stated plainly" + "further limitation" sequence (~95 words saved)

**Location:** §7, paragraph beginning "The framework's limitations should be stated plainly" and the next paragraph beginning "A further limitation the framework itself makes visible".

**Words saved:** ~95

**BEFORE:**

> **The framework's limitations should be stated plainly.** It has been developed and tested through a single case: one paper, one author, one disciplinary context. The author assessed their own implementation — no independent evaluation has been conducted. Whether the argument extends to other humanistic disciplines that share philosophy's evaluative contestedness — history, literary criticism, political theory — is an open question not addressed here. And there is a bootstrapping problem: arguing for documentation standards while simultaneously implementing them means the adequacy of the implementation cannot be fully verified before the standards it motivates are themselves settled.
>
> **A further limitation the framework itself makes visible: the ratio of documentation produced to argument delivered in this case is, plausibly, disproportionate to what the framework actually requires. The author chose to produce more than an austere reading of SP-1 through SP-5 would demand. That choice is part of the disclosed record, and the community is in a position to assess it — as zealous responsibility, as self-indulgence, or as some mixture. The framework supports the assessment rather than preempting it. Where over-documentation begins to substitute for the inquiry it is meant to make visible is a community-level question the dual assessment structure of §5 is positioned to address.**

**AFTER:**

> The framework's limitations should be stated plainly. It has been developed and tested through a single case: one paper, one author, one disciplinary context. The author assessed their own implementation — no independent evaluation has been conducted. Whether the argument extends to other humanistic disciplines that share philosophy's evaluative contestedness — history, literary criticism, political theory — is an open question not addressed here. There is a bootstrapping problem: arguing for documentation standards while simultaneously implementing them means the adequacy of the implementation cannot be fully verified before the standards it motivates are themselves settled. And the ratio of documentation produced to argument delivered here is plausibly disproportionate to what the framework actually requires: the author chose to produce more than an austere reading of SP-1 through SP-5 would demand. That choice is part of the disclosed record, and whether it reads as zealous responsibility, self-indulgence, or some mixture is a community-level question the dual assessment structure of §5 is positioned to address.

**Justification:** Folding the "further limitation" paragraph into the limitations paragraph eliminates two transitional sentences ("The framework itself makes visible…", "The framework supports the assessment rather than preempting it") and the duplicative "Where over-documentation begins to substitute for the inquiry it is meant to make visible" — both ideas are already carried by the merged version. Borderline — preserve if you value the over-documentation point as a free-standing limitation rather than a coda.

---

### C-03 — §3.7 — Trim the Nozick/Parfit/Williams/Cavell exemplar elaboration (~75 words saved)

**Location:** §3.7, paragraph beginning "Traditional philosophical writing was already rich with implicit process evidence."

**Words saved:** ~75

**BEFORE:**

> Traditional philosophical writing was already rich with implicit process evidence. Citation patterns, argumentative structure, and stylistic signatures all functioned as signals from which the scholarly community could infer features of the author's intellectual process. **When Nozick deployed decision-theoretic reasoning to motivate libertarian conclusions, when Parfit developed objections with a transparency that displayed a mind encountering and working through difficulties in real time, when Williams brought Greek tragedy into dialogue with contemporary moral philosophy, or when Cavell paired ordinary-language philosophy with film criticism — these were not decorative choices. They constituted implicit methodological declarations that enabled readers across traditions to assess whether the process criteria they cared about had been satisfied. The expressivist reader could evaluate whether evaluative commitments had been formed through genuine confrontation with alternatives. The reader in the personal/existential tradition could assess whether the author's mode of engagement bore the marks of authentic philosophical labor.** These assessments were fallible — philosophers have always been capable of performing depth they do not possess — but the connection between textual signal and underlying process was reliable enough to function as a *de facto* transparency mechanism.

**AFTER:**

> Traditional philosophical writing was already rich with implicit process evidence. Citation patterns, argumentative structure, and stylistic signatures all functioned as signals from which the scholarly community could infer features of the author's intellectual process. When Nozick deployed decision-theoretic reasoning to motivate libertarian conclusions, when Parfit displayed a mind working through objections in real time, when Williams brought Greek tragedy into dialogue with contemporary moral philosophy, or when Cavell paired ordinary-language philosophy with film criticism, these were implicit methodological declarations that enabled readers across traditions to assess whether the process criteria they cared about had been satisfied. These assessments were fallible — philosophers have always been capable of performing depth they do not possess — but the connection between textual signal and underlying process was reliable enough to function as a *de facto* transparency mechanism.

**Justification:** The two sentences spelling out what "the expressivist reader" and "the reader in the personal/existential tradition" could each evaluate restate §3.2's two-conceptions argument in slightly different language; the foregoing sentence ("enabled readers across traditions to assess whether the process criteria they cared about had been satisfied") already does the work. The Parfit description is also tightened. All four exemplar names and the Cavell/Williams citations preserved.

---

### C-04 — §6 — Compress the implementation-honesty paragraph (~70 words saved)

**Location:** §6, paragraph beginning "The framework is a sketch requiring experimentation"

**Words saved:** ~70

**BEFORE:**

> The framework is a sketch requiring experimentation: a community of practice within which authors experiment with documentation, reviewers with assessment, and shared norms evolve through use. **The documentation requirements are substantial — prompts, modification logs, epistemic traces, and session records accumulate rapidly — and synthesising them into the coherent account SP-3 requires is intractable if attempted retrospectively. AI-assisted synthesis applied immediately after each working session is what makes the framework implementable. The dependency is honest: a framework requiring transparency about AI use depends, in implementation, on AI assistance to sustain the documentation it requires. The relevant constraint is that synthesis be honest — working from the raw session record, rather than from memory alone, reduces the risk of the account becoming more coherent than the process actually was.**

**AFTER:**

> The framework is a sketch requiring experimentation: a community of practice within which authors experiment with documentation, reviewers with assessment, and shared norms evolve through use. The documentation requirements are substantial, and synthesising them into the coherent account SP-3 requires is intractable retrospectively; AI-assisted synthesis applied immediately after each working session is what makes the framework implementable. The dependency is honest — a framework requiring transparency about AI use depends, in implementation, on AI assistance to sustain the documentation it requires — and the relevant constraint is that synthesis work from the raw session record rather than memory alone, so the account does not become more coherent than the process actually was.

**Justification:** Two sentences merged into one each; the parenthetical inventory ("prompts, modification logs, epistemic traces, and session records") restates what was already itemised in the SP-4/SP-5 paragraph immediately above; "reduces the risk of the account becoming more coherent than the process actually was" tightened.

---

### C-05 — §7 — Trim the implementation/Neurath-boat passage (~65 words saved)

**Location:** §7, paragraph beginning "This self-exemplification requires honest acknowledgment."

**Words saved:** ~65

**BEFORE:**

> This self-exemplification requires honest acknowledgment. The commitment to documentation was present from the outset — an ex ante intention, not a retrospective reconstruction. That intention is what made the later infrastructure work feasible: without it, the artifact chain that enabled chain-level traceability could not have been rebuilt at all. But feasible is not the same as costless. The infrastructure layer — automated session identifiers, standardized frontmatter, chain-level traceability — was not in place from the start and had to be built while the work was underway, in the manner of Neurath's boat: plank by plank, without the option of dry dock. **The three criteria of Section 5 were tested against the paper's own record and were applicable in the sense the framework requires — whether the record satisfies them is a question for the community, not the author. What the experience revealed is not a logical gap in the framework but a practical one:** documentation infrastructure planned from the beginning is substantially less costly than documentation infrastructure retrofitted to an existing record, even when the original intention was always there.

**AFTER:**

> This self-exemplification requires honest acknowledgment. The commitment to documentation was present from the outset — an ex ante intention, not a retrospective reconstruction. That intention is what made the later infrastructure work feasible: without it, the artifact chain that enabled chain-level traceability could not have been rebuilt at all. But feasible is not the same as costless. The infrastructure layer — automated session identifiers, standardized frontmatter, chain-level traceability — was not in place from the start and had to be built while the work was underway, in the manner of Neurath's boat. The lesson is practical: documentation infrastructure planned from the beginning is substantially less costly than documentation infrastructure retrofitted to an existing record, even when the original intention was always there.

**Justification:** "plank by plank, without the option of dry dock" is decorative gloss on "Neurath's boat" — the metaphor carries the meaning unaided. The sentence "The three criteria of Section 5 were tested against the paper's own record and were applicable in the sense the framework requires — whether the record satisfies them is a question for the community, not the author" duplicates what §5.4's feasibility-versus-adequacy paragraph already says ("Feasibility is what an author can demonstrate by exhibition; adequacy is what only the community can settle"). Borderline — preserve the "three criteria were tested and were applicable" sentence if you want §7 to restate the §5 distinction one final time.

---

### C-06 — §6 — Trim the MHC framing paragraph (~50 words saved)

**Location:** §6, paragraph beginning "The framework draws on Meaningful Human Control."

**Words saved:** ~50

**BEFORE:**

> The framework draws on Meaningful Human Control. Santoni de Sio and van den Hoven (2018) identify two conditions a system must satisfy to be under meaningful human control: the **tracking condition** — system outputs covary with the operator's relevant reasons — and the **tracing condition** — outputs traceable to a human person's understanding and endorsement. **We apply these to AI-assisted scholarship on the basis of §3's agent-integrity argument; the features that distinguish weapons systems (catastrophic stakes, physical irreversibility) play no role here.** As Santoni de Sio and van den Hoven put it, "systems whose actions and states are not traceable to relevant understanding and endorsing by some human person […] no matter how intelligent and reason-responsive they may be, are not under meaningful human control" (p. 9). For the framework here, tracing is the operative condition: it asks whether the directing person understood what was produced and endorses it as their own intellectual contribution — **the question that, on §3's reading, Kierkegaard's truth-as-subjectivity makes constitutive and that Williams's agent-integrity tradition requires.**

**AFTER:**

> The framework draws on Meaningful Human Control. Santoni de Sio and van den Hoven (2018) identify two conditions a system must satisfy to be under meaningful human control: the **tracking condition** — system outputs covary with the operator's relevant reasons — and the **tracing condition** — outputs traceable to a human person's understanding and endorsement. As Santoni de Sio and van den Hoven put it, "systems whose actions and states are not traceable to relevant understanding and endorsing by some human person […] no matter how intelligent and reason-responsive they may be, are not under meaningful human control" (p. 9). For the framework here, tracing is the operative condition: it asks whether the directing person understood what was produced and endorses it as their own intellectual contribution — the question §3's agent-integrity argument makes constitutive.

**Justification:** The weapons-systems disclaimer ("the features that distinguish weapons systems… play no role here") and the final clause naming Kierkegaard and Williams separately both restate what §3.5 already established. The collapsed final clause preserves the §3 cross-reference and the agent-integrity grounding. No citation lost. Borderline — preserve if you value the explicit weapons-systems disclaimer as a defense against MHC-misapplication objections.

---

### C-07 — §3.7 — Trim the second paragraph's "not accidental" framing (~50 words saved)

**Location:** §3.7, paragraph beginning "This reliability was not accidental."

**Words saved:** ~50

**BEFORE:**

> **This reliability was not accidental. It rested on a contingent but stable fact about how philosophical texts were produced: a philosopher who cited Korsgaard with precision and engaged her arguments at the level of their internal structure had, in all likelihood, read and wrestled with Korsgaard. The essential contestedness of ethical inquiry was always present, the need for process information always real. But the need did not present itself acutely, because the implicit signals were adequate. The transparency requirement existed; it was satisfied by the ordinary features of philosophical writing itself.**

**AFTER:**

> This reliability rested on a contingent but stable fact about how philosophical texts were produced: a philosopher who cited Korsgaard with precision and engaged her arguments at the level of their internal structure had, in all likelihood, read and wrestled with Korsgaard. The transparency requirement existed; it was satisfied by the ordinary features of philosophical writing itself.

**Justification:** "This reliability was not accidental" is throat-clearing replaced by simply opening with the substantive claim. The middle two sentences ("The essential contestedness of ethical inquiry was always present… implicit signals were adequate") restate what the final sentence ("transparency requirement existed; satisfied by ordinary features") delivers in one line. The Korsgaard example and the closing sentence carry the paragraph.

---

### C-08 — §7 — Trim the "deepest reason" closing paragraph (~50 words saved)

**Location:** §7, paragraph beginning "The deepest reason for these requirements"

**Words saved:** ~50

**BEFORE:**

> The deepest reason for these requirements, however, is not that AI introduces something unprecedented into philosophical practice but that it removes something that was always there: the implicit signals — citation patterns, reasoning structure, engagement with sources — by which the community could once infer process from text (§3.7). **What is lost in this break is not a convenience. The philosopher whose citational precision and argumentative texture once just *were* the visible mark of having done the work can no longer count on prose to carry that mark; and the reader can no longer read the text as a window onto the inquiry behind it.** The explicit transparency requirement proposed here is therefore not a new imposition on philosophy. It is the conscious replacement of something that was always needed and is now, for the first time, no longer reliably supplied by the text itself.

**AFTER:**

> The deepest reason for these requirements, however, is not that AI introduces something unprecedented into philosophical practice but that it removes something that was always there: the implicit signals — citation patterns, reasoning structure, engagement with sources — by which the community could once infer process from text (§3.7). The philosopher can no longer count on prose to carry the mark of having done the work; the reader can no longer read the text as a window onto the inquiry behind it. The explicit transparency requirement proposed here is therefore not a new imposition on philosophy. It is the conscious replacement of something that was always needed and is now, for the first time, no longer reliably supplied by the text itself.

**Justification:** "What is lost in this break is not a convenience" is rhetorical scaffolding; the two-clause sentence that follows it carries the substance. The "citational precision and argumentative texture once just *were* the visible mark" wording is compressed to its load-bearing element. §3.7 cross-reference preserved; closing two sentences preserved verbatim.

---

### C-09 — §3.7 — Trim the Schwitzgebel-introducing prose (~45 words saved)

**Location:** §3.7, paragraph beginning "The disruption is concrete."

**Words saved:** ~45

**BEFORE:**

> The disruption is concrete. AI can produce text exhibiting every surface marker of genuine philosophical engagement — citation depth, the structure of reasoning-as-discovery, the elaboration of objections — without any corresponding human intellectual process. **The link between signal and process is not merely weakened but structurally detachable.** Early empirical work supports the trajectory while reminding us how recent it is: Schwitzgebel, Schwitzgebel & Strasser (2024) found that experts on Daniel Dennett's work could distinguish Dennett's own answers from those of a GPT-3 model fine-tuned on his corpus only 51% of the time — above chance (20%) but well below the hypothesized 80%. **The current rate is speculative; the direction is not.** This is not the familiar risk that a philosopher might exaggerate engagement with sources; it is a qualitative break in the signal-to-process inference, and the reason AI *specifically* triggers an explicit transparency requirement. The Conclusion returns to what this means.

**AFTER:**

> The disruption is concrete. AI can produce text exhibiting every surface marker of genuine philosophical engagement — citation depth, the structure of reasoning-as-discovery, the elaboration of objections — without any corresponding human intellectual process. Early empirical work supports the trajectory: Schwitzgebel, Schwitzgebel & Strasser (2024) found that experts on Daniel Dennett's work could distinguish Dennett's own answers from those of a GPT-3 model fine-tuned on his corpus only 51% of the time — above chance (20%) but well below the hypothesized 80%. This is not the familiar risk that a philosopher might exaggerate engagement with sources; it is a qualitative break in the signal-to-process inference, and the reason AI *specifically* triggers an explicit transparency requirement. The Conclusion returns to what this means.

**Justification:** "The link between signal and process is not merely weakened but structurally detachable" restates the preceding sentence's "without any corresponding human intellectual process." "The current rate is speculative; the direction is not" is hedge-language already implied by "Early empirical work supports the trajectory." Citation and 51%/20%/80% data preserved.

---

### C-10 — §6 — Compress the opening Santoni de Sio/van den Hoven block quote setup (~40 words saved)

**Location:** §6, paragraph beginning "The framework draws on Meaningful Human Control" (interacts with C-06 — apply at most one of {C-06, C-10}, not both; C-10 is the lighter-touch alternative).

**Words saved:** ~40

**BEFORE:**

> We apply these to AI-assisted scholarship on the basis of §3's agent-integrity argument; the features that distinguish weapons systems (catastrophic stakes, physical irreversibility) play no role here. As Santoni de Sio and van den Hoven put it, "systems whose actions and states are not traceable to relevant understanding and endorsing by some human person […] no matter how intelligent and reason-responsive they may be, are not under meaningful human control" (p. 9). **For the framework here, tracing is the operative condition: it asks whether the directing person understood what was produced and endorses it as their own intellectual contribution** — the question that, on §3's reading, Kierkegaard's truth-as-subjectivity makes constitutive and that Williams's agent-integrity tradition requires.

**AFTER (lighter-touch alternative to C-06):**

> We apply these to AI-assisted scholarship on the basis of §3's agent-integrity argument; the features that distinguish weapons systems (catastrophic stakes, physical irreversibility) play no role here. As Santoni de Sio and van den Hoven put it, "systems whose actions and states are not traceable to relevant understanding and endorsing by some human person […] no matter how intelligent and reason-responsive they may be, are not under meaningful human control" (p. 9). Tracing is the operative condition here: it asks whether the directing person understood what was produced and endorses it as their own — the question §3's agent-integrity argument makes constitutive.

**Justification:** Pure tightening of the sentence following the block quote and collapse of the Kierkegaard/Williams co-reference into "§3's agent-integrity argument." Borderline — flagged because C-06 covers similar ground. Use C-06 if you accept the larger trim; use C-10 if you want to keep the weapons-systems disclaimer.

---

### C-11 — §2.1 — Trim the "underreporting need not be dishonest" connective (~35 words saved)

**Location:** §2.1, paragraph beginning "The underreporting need not be dishonest."

**Words saved:** ~35

**BEFORE:**

> For minor work, honest disclosure carries relatively low cost. For potentially significant work, disclosure becomes fraught. For career-defining work, the incentive to underreport reaches maximum strength.
>
> **The underreporting need not be dishonest. Several mechanisms exploit genuine ambiguities in how AI-assisted processes might be characterized, operating even among scholars committed to honesty.**
>
> The first is *definitional flexibility*. Terms like "substantial AI assistance" and "minimal editorial support" lack precise boundaries.

**AFTER:**

> For minor work, honest disclosure carries relatively low cost. For potentially significant work, disclosure becomes fraught. For career-defining work, the incentive to underreport reaches maximum strength.
>
> Underreporting need not be dishonest — several mechanisms exploit genuine ambiguities, operating even among scholars committed to honesty.
>
> The first is *definitional flexibility*. Terms like "substantial AI assistance" and "minimal editorial support" lack precise boundaries.

**Justification:** "in how AI-assisted processes might be characterized" is implied by context (the entire surrounding section is about characterising AI use); the sentence-pair becomes a single tightened transition.

---

### C-12 — §3.5 — Trim the disciplinary-scope hedge (~35 words saved)

**Location:** §3.5, paragraph beginning "Philosophy does not have this structure."

**Words saved:** ~35

**BEFORE:**

> A reader who wants to test a philosophical claim re-reads the argument, considers objections, traces the inferences — but does not, in any literal sense, replicate the process by which the author arrived at it. The standard of evaluation is the argument's force, not the recoverability of the steps the author took to formulate it. **The contrast we draw is between ethics and empirical science specifically; we make no claim here about disciplines whose evidentiary structures fall between these poles, like history, literary criticism, or political theory, which mix factual and interpretive elements in ways that may have transparency implications distinct from both.**

**AFTER:**

> A reader who wants to test a philosophical claim re-reads the argument, considers objections, traces the inferences — but does not, in any literal sense, replicate the process by which the author arrived at it. The standard of evaluation is the argument's force, not the recoverability of the steps the author took to formulate it.

**Justification:** The disclaimer about history/literary criticism/political theory is restated nearly verbatim in §7 ("Whether the argument extends to other humanistic disciplines that share philosophy's evaluative contestedness — history, literary criticism, political theory — is an open question not addressed here"). One occurrence is sufficient; §7 is the better location since that paragraph frames it as a limitation. Borderline — preserve if you value the early-flagged scope hedge to prevent reviewer objections in §3.5.

---

### C-13 — §1 — Trim the intro's tracking-vs-evaluation reprise (~35 words saved)

**Location:** §1, paragraph beginning "If output-evaluation criteria are contested"

**Words saved:** ~35

**BEFORE:**

> If output-evaluation criteria are contested, the achievable goal for transparency is not evaluation against agreed standards but *tracking*: monitoring what ethics research is becoming under AI assistance and accumulating the evidentiary record that makes future normative judgments possible. **Tracking is prior to evaluation: it creates the visibility without which damage cannot be detected.** If we cannot settle what ethical authoring demands of the author, documentation enables each tradition to assess work on its own terms. **Comprehensive process documentation serves both requirements through independent routes — for complex philosophical work involving contested methods and irreducible judgment, where AI assistance is most consequential.**

**AFTER:**

> If output-evaluation criteria are contested, the achievable goal for transparency is not evaluation against agreed standards but *tracking*: monitoring what ethics research is becoming under AI assistance and accumulating the evidentiary record that makes future normative judgments possible. If we cannot settle what ethical authoring demands of the author, documentation enables each tradition to assess work on its own terms.

**Justification:** "Tracking is prior to evaluation" is a maxim that §3.6 makes properly. The "Comprehensive process documentation serves both requirements through independent routes" sentence forward-references §3.4's qualification, which is delivered in full there. Borderline — preserve the "complex philosophical work / where AI is most consequential" qualifier if you want it flagged in §1 too; §3.4 already carries it.

---

### C-14 — §5.4 — Trim "Within these norms, calibration matters" framing (~30 words saved)

**Location:** §5.4, paragraph beginning "Within these norms, calibration matters."

**Words saved:** ~30

**BEFORE:**

> **Within these norms, calibration matters. Assessment is epistemic inquiry: the question is whether the record enables the assessor to understand how this work came to be.** Depth of review should be proportional to the complexity of the claimed contribution. Work claiming AI generated a central philosophical insight requires more sustained tracing than work claiming AI assisted with structuring a well-understood argument.

**AFTER:**

> Calibration matters. Depth of review should be proportional to the complexity of the claimed contribution: work claiming AI generated a central philosophical insight requires more sustained tracing than work claiming AI assisted with structuring a well-understood argument.

**Justification:** "Within these norms" is a transitional throat-clear; "Assessment is epistemic inquiry: the question is whether the record enables the assessor to understand how this work came to be" restates §5.1 / §5.3's stated standard. The substantive calibration point is preserved.

---

### C-15 — §5.4 — Compress the "natural objection: documentation costs" reply (~25 words saved)

**Location:** §5.4, paragraph beginning "A natural objection: documentation requirements impose disproportionate costs."

**Words saved:** ~25

**BEFORE:**

> **A natural objection: documentation requirements impose disproportionate costs. But AI tools create a reduced-structure epistemic environment that invites indiscriminate cognitive offloading. The documentation requirements re-impose metacognitive monitoring — forethought, self-evaluation, attribution tracking — that counteracts this risk (Zimmerman, 2002; Cheng et al., 2025).**

**AFTER:**

> A natural objection is that documentation requirements impose disproportionate costs. But AI tools create a reduced-structure epistemic environment that invites indiscriminate cognitive offloading; the documentation requirements re-impose metacognitive monitoring — forethought, self-evaluation, attribution tracking — that counteracts this risk (Zimmerman, 2002; Cheng et al., 2025).

**Justification:** Minor sentence-joining trim. The §3.3 Cordasco-engagement footnoted paragraph already carries the same Zimmerman/Cheng-cited point at greater length; this paragraph at §5.4 is the second occurrence. The compression keeps both citations and the substantive reply but tightens sentence boundaries. (If the user prefers, the whole paragraph could be cut as full redundancy with the §3.3 footnoted passage — would save ~55w — but that risks weakening the §5.4 cost reply, so this conservative tightening is proposed instead.)

---

## Summary table

| ID | Section | Words saved | One-line description |
|----|---------|-------------|----------------------|
| C-01 | §6 | 110 | Compress SP-1 through SP-5 inventory: trim connective/explanatory clauses, preserve all five elements and their criterion-mapping |
| C-02 | §7 | 95 | Fold "further limitation" paragraph into main limitations paragraph |
| C-03 | §3.7 | 75 | Trim Nozick/Parfit/Williams/Cavell exemplar elaboration; cut the two-conception restatement |
| C-04 | §6 | 70 | Compress implementation-honesty paragraph (sketch + AI-dependency) |
| C-05 | §7 | 65 | Trim Neurath's-boat decorative gloss + §5 criteria restatement |
| C-06 | §6 | 50 | Trim MHC framing (weapons-systems disclaimer + Kierkegaard/Williams co-reference) — mutually exclusive with C-10 |
| C-07 | §3.7 | 50 | Trim §3.7 second paragraph's "not accidental"/contestedness restatement |
| C-08 | §7 | 50 | Trim "deepest reason" closing — cut "What is lost is not a convenience" rhetorical bridge |
| C-09 | §3.7 | 45 | Trim Schwitzgebel paragraph: drop "structurally detachable" and "speculative; direction is not" |
| C-10 | §6 | 40 | Lighter-touch alternative to C-06 — keeps weapons disclaimer, trims only the closing co-reference |
| C-11 | §2.1 | 35 | Tighten "underreporting need not be dishonest" transitional pair |
| C-12 | §3.5 | 35 | Cut history/literary-criticism/political-theory disclaimer (duplicated in §7) |
| C-13 | §1 | 35 | Cut "Tracking is prior to evaluation" + "Comprehensive process documentation" reprise in intro |
| C-14 | §5.4 | 30 | Tighten "Within these norms, calibration matters" framing |
| C-15 | §5.4 | 25 | Compress "natural objection: documentation costs" reply (conservative tightening) |
| **Total (all candidates)** |  | **~810** | |
| **Total if C-06 and C-10 treated as mutually exclusive (recommended: pick C-06)** |  | **~770** | |

Notes on totals:
- C-06 and C-10 overlap on the same paragraph. The summed total above assumes both; the recommended target assumes C-06 only (which subsumes C-10's trims and adds more).
- All candidates preserve every citation, every subsection heading, and every §N cross-reference.
- No proposed cut touches any of the Earp-integration paragraphs from v1.11, the §3.3 Williams-inversion defense, or the §3.3 Cordasco-engagement footnoted paragraph.
- C-02, C-05, C-06, C-12, C-13 flagged as borderline in their justifications.
