---
title: SP-3 Visual Design — Figures for the Stories
document_type: Type 2 - Epistemic Trace
source_session: SID-20260402-145404
model: Claude Opus 4.6
date: 2026-04-02
status: In Progress
inputs:
  - CFP_4.7.13_EpistemicTrace_SP3DesignBrainstorm.md
  - CFP_5.3.7_SelectedGraphCandidates.md
---

# CFP 4.7.14 — SP-3 Visual Design: Figures for the Stories

## Premise

The big figure is dead. SP-3 tells stories, not shows infrastructure. Each visual must serve a specific narrative claim and be legible on its own. The question is: what visuals, and how to produce them?

## Constraint: What SP-3's Reader Has

The reader has the documentation artifacts (SP-4, SP-5) and their metadata. They do NOT have access to full chat transcripts. Visuals must be grounded in what the artifacts show — frontmatter fields, dated entries, input/output chains — not in private working material.

---

## Visual 1: The Macro Timeline

**Serves:** The seven-act macro story (the SP-3 spine).

**What it shows:** A horizontal timeline (Oct 14 2025 → Apr 2026) with swim lanes for parallel activities:
- **Lane 1: Paper writing** — sections as blocks, colored by phase (plan-driven I–VI vs. later VII–IX)
- **Lane 2: Ontology development** — discovery moments, type system evolution
- **Lane 3: Appendix / SP design** — appendix writing, SP reconception
- **Lane 4: Documentation consolidation** — MD conversion, metadata audit, hub construction
- **Lane 5: CFP adaptation** — branch, new drafts, modlogs

Key events annotated: Type 2b discovery (Oct 14), appendix → Section 6 feedback loop (Nov 5–6), SP reconception (Mar 2), double contestation (Apr 1).

**What it replaces:** The big figure's attempt to show everything at once. The timeline makes temporal sequence legible and shows where activities overlap.

**How it's different from the big figure:** Linear (time axis), not a directed graph. Parallel lanes instead of converging arrows. The reader follows left to right and sees which things happened simultaneously, not which artifacts fed into which.

**Production technology:**
- **Draft:** Mermaid gantt chart (viewable in Obsidian for iteration)
- **Final:** Python + matplotlib timeline with custom swim lanes, or TikZ if LaTeX submission
- **Fallback:** Hand-drawn in a vector editor (Inkscape/Illustrator)

**Size:** Wide and short — landscape orientation, one page width.

---

## Visual 2: The Input Accumulation Waterfall

**Serves:** Act 1 (plan-driven writing) — shows how each section inherits from all previous ones.

**What it shows:** A stacked column chart. X-axis: sections I through IX (old numbering). Y-axis: number/type of inputs. Each column is segmented by input type:
- Complete Prompt (constant — present I–VI, absent VII, returns VIII)
- Section Guidance (one per section)
- Pattern Summaries (accumulating — 0 for I, 1 for II, 2 for III, ...)
- Section Summaries (accumulating)
- Epistemic Traces (variable)

The visual point: by Section VIII, the input stack is tall. The Complete Prompt's absence from Section VII is visible as a gap. The accumulation is the process learning.

**Data source:** Can be extracted programmatically from modlog frontmatter `inputs` fields.

**Production technology:**
- **Draft:** Python + matplotlib stacked bar chart
- **Script:** Read modlog YAML frontmatter, count inputs by type, plot
- **Final:** Clean version with consistent colors matching other figures

**Size:** Compact — half-page, works in a column.

---

## Visual 3: The Feedback Loop

**Serves:** Act 4 — the most narratively interesting moment.

**What it shows:** A small, focused diagram with 4–5 nodes:

```
Paper body (Sections I–IX)
    → Appendix writing (Oct 19 – Nov 3)
        → Discovery: infrastructure constraints
            → Section 6.2 revision (Nov 5–6)
                ← (feeds back into paper body)
```

Annotated with dates and artifact IDs: 4.2.11 (appendix modlog), 4.4.13 (feedback prompt), 4.2.9 MOD-009 (the revision entry).

The visual point: the documentation framework is recursive — the appendix about transparency revealed constraints that changed what the paper says about transparency. A circle, not a line.

**Production technology:**
- **Draft:** Mermaid flowchart or simple SVG
- **Final:** Clean vector graphic, 4–5 nodes with labeled arrows

**Size:** Small — quarter page. Elegant, not busy.

---

## Visual 4: The Contrast Diptych

**Serves:** The documentation-adequacy argument — showing *why* a specified framework matters.

**Already specified** in CFP_5.3.7 as Graph 3 (Introduction contrast). Two panels side by side:

**Left panel (v1/v2):** Ghost nodes (null chat ID, unarchived intermediate states), no hub, self-referential loop. Sparse.

**Right panel (CFP):** Session hub, named inputs, related_documents links, epistemic trace connection. Dense.

**The visual point:** Same section, same author, same topic. The documentation difference comes from having a framework, not from having different intentions. The ghosts on the left are what mandates without frameworks produce. The connections on the right are what a specified framework enables.

**Production technology:**
- **Draft:** Graphviz/dot (automatic layout for small directed graphs)
- **Final:** Graphviz export to SVG, cleaned up in vector editor
- Could also do Mermaid, but Graphviz handles the two-panel layout better

**Size:** Half page, two panels.

---

## Visual 5: The Version Chain

**Serves:** The trajectory claim — showing that intellectual development is traceable.

**Already specified** in CFP_5.3.7 as Graph 2 (Section 6 version chain). Three successive drafts with `derived_from` links, a modlog with 13 entries, and a session hub.

**The visual point:** Three versions in one session, each addressing specific philosophical problems identified in the prior version. The modlog records what changed and why. This is what "documentable intellectual trajectory" looks like concretely.

**Production technology:** Same as Visual 4 (Graphviz/dot → SVG).

**Size:** Compact — third of a page.

---

## Visual 6: The Three Eras (optional)

**Serves:** Act 7 — the infrastructure shift as a story about documentation technology evolution.

**What it shows:** Three columns (triptych):

| v1/v2 (Oct–Nov 2025) | Stage III (Jan–Feb 2026) | CFP (Mar–Apr 2026) |
|---|---|---|
| Claude.ai chat windows | Claude Code + early MHC-W | Claude Code + MHC-W with SIDs |
| Word/RTF artifacts | Git + Canonical Markdown | Git + structured automation |
| Manual extraction | In-place file editing | JSONL auto-export |
| Ad hoc documentation | MHC-W commands (no SIDs) | Full session tracking + Cowork |
| `source_chat_id: null` or manual | `session_id` absent/reconstructed | `session_id: SID-YYYYMMDD-HHMMSS` |

**The visual point:** Three distinct tooling regimes, each with characteristic documentation affordances and gaps. The evolution is from "documentation despite the tools" (v1/v2) through "documentation with nascent tooling" (III: Claude Code + MHC-W but no session identifiers) to "documentation because of the tools" (CFP: full session tracking, automated export, cross-platform collaboration). Stage III is the transitional era — already using Claude Code and git, but the MHC-W version didn't yet deliver session IDs, so some metadata had to be reconstructed retroactively.

**Production technology:**
- **Draft:** Markdown table (already legible in Obsidian)
- **Final:** Styled table or simple infographic with icons/colors per era

**Size:** Half page.

---

## Data-Driven Visuals (from hub/graph analysis, Apr 2)

Running `build_graph.py` and `obsidian_connections_with_chat_hubs.py` on the full archive produced: **225 nodes, 279 edges, 65 hub nodes across 32 unique chats**. Era breakdown: 82 v1/v2 (Claude.ai + Word/RTF), 12 III (Claude Code + early MHC-W, no SIDs), 56 CFP (Claude Code + MHC-W with SIDs). Stage III and CFP are both Claude Code eras but differ in metadata maturity.

### Visual 7: Artifact Date Histogram

**Serves:** The macro timeline story — but with real data, not schematic illustration.

**What it shows:** A histogram of artifact creation dates, bars colored by era (v1/v2 = blue, III = grey, CFP = orange). Two dramatic spikes visible:
- **Oct 13–19, 2025:** 33 artifacts in one week (entire v1 writing phase + ontology discovery)
- **Apr 1, 2026:** 24 artifacts in a single day (CFP double-contestation + documentation blitz)

The gap between them (Nov 2025 – Feb 2026) is the consolidation period. The visual tells the story of bursts, silence, and resumed activity with different tooling.

**Production technology:** Python/matplotlib histogram. Data already extracted. Script: ~20 lines reading YAML `date` fields.

**Size:** Half page, landscape.

### Visual 8: Hub Fan-Out — Documentation Density by Chat

**Serves:** The documentation-adequacy argument — shows that CFP-era chats produce more artifacts per session.

**What it shows:** Horizontal bar chart. Each bar = one chat session, length = number of artifacts produced. Sorted descending. Colored by era.

Key data points:
- Busiest chat: `SID-20260401` (11 artifacts) — CFP session
- Typical v1/v2 chat: 2–4 artifacts
- The fan-out asymmetry is the visual argument: same author, different framework, different documentation yield

**Production technology:** Python/matplotlib barh chart. Data from hub script output.

**Size:** Half page.

### Visual 9: Connection Density — v1/v2 vs CFP

**Serves:** The metadata-web argument — CFP artifacts are more interconnected.

**What it shows:** Two distributions (box plot or violin plot):
- v1/v2 artifacts: average ~2 connections, max 7 (appendix modlog)
- CFP artifacts: average ~4 connections, max 16 (double-contestation modlog)

The visual point: the framework doesn't just produce more artifacts — it produces artifacts that are more explicitly linked to each other. The metadata web is denser.

**Production technology:** Python/matplotlib box plot. Data from frontmatter relational field counts.

**Size:** Quarter page.

### Visual 10: The Interactive Graph (already built)

**Serves:** Exploration, not argument. For readers who want to see the full picture.

**What it is:** `_GRAPHS/jpep_graph.html` — 225-node interactive HTML graph (pyvis/vis.js). Nodes colored by type (amber=hubs, blue=drafts, green=modlogs, purple=traces, teal=PDLs). Hoverable tooltips with metadata. Physics-based layout.

**Not for print.** This is a supplementary digital artifact. SP-3 can reference it: "An interactive visualization of the full artifact graph is available at [link]."

**Production technology:** Already built by `build_graph.py`. Self-contained HTML file.

---

## What NOT to visualize

- The full artifact dependency graph (the megagraph) — replaced by the timeline + selected subgraphs
- Individual section production chains beyond the examples — one (Section 5) is enough to show the pattern
- The ontology taxonomy itself — it's a text description, not a visual argument
- Anything requiring access to chat content the reader doesn't have

---

## Production Plan

| # | Visual | Draft tool | Final tool | Priority | Data ready? |
|---|--------|-----------|------------|----------|-------------|
| 1 | Macro Timeline | Mermaid gantt | matplotlib or TikZ | **High** — SP-3 spine | Manual |
| 2 | Input Waterfall | Python script | matplotlib stacked bar | **High** — accumulation | From modlog YAML |
| 3 | Feedback Loop | Mermaid/SVG | Clean vector | **High** — best story | Manual (4 nodes) |
| 4 | Contrast Diptych | Graphviz | SVG + cleanup | **High** — core argument | From 5.3.7 spec |
| 5 | Version Chain | Graphviz | SVG + cleanup | **Medium** — specified | From 5.3.7 spec |
| 6 | Three Eras | Markdown table | Styled table | **Low** — works as text | Manual |
| 7 | Date Histogram | Python script | matplotlib | **High** — data-driven | Extracted |
| 8 | Hub Fan-Out | Python script | matplotlib barh | **Medium** — density argument | Extracted |
| 9 | Connection Density | Python script | matplotlib box | **Low** — detail | Extracted |
| 10 | Interactive Graph | build_graph.py | HTML (already built) | **Bonus** — digital only | Done |

**Recommended set for SP-3 (6 figures):**
- Visuals 7, 3, 4, 5 tell the strongest story with least production effort
- Visual 1 (timeline) replaces the megagraph as the orienting figure
- Visual 8 (fan-out) is the most direct documentation-density evidence

**Scripts location:** `transparency/SCRIPTS/`. Data extraction already prototyped.

---

## Open Questions

1. **Submission format?** LaTeX → TikZ. Word/PDF → SVG/PNG exports. HTML → interactive possible.
2. **How many figures?** 10 candidates, recommend 5–6 for SP-3. The interactive graph (10) is a digital supplement, not a figure.
3. **Which tell a story vs. which are decoration?** The date histogram (7) and contrast diptych (4) are the most argumentatively loaded. The feedback loop (3) is the most narratively compelling. Others support but don't carry claims.
4. **Can some be combined?** The timeline (1) and date histogram (7) could be one figure: a timeline with bar heights showing activity density. The fan-out (8) and connection density (9) could merge into a single "documentation density" panel.
