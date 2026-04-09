---
project: JPEP
document_type: Type 3 - Modification Log
label: CFP_4.2.28_ModificationLog_GraphInfrastructure
title: "Modification Log: Graph infrastructure overhaul — arrow direction, comma parsing, era filters, fig_section6 aesthetic pass"
date_created: 2026-04-08
session_id: SID-20260408-191811
status: Complete
inputs:
  - transparency/SCRIPTS/build_graph.py
  - transparency/SCRIPTS/fig_section6_network.py
  - transparency/SCRIPTS/hub_annotations.yaml
  - transparency/Canonical_MD/SP4_ProcessDocumentation/4.2_ModificationLogs/4.2.9_ModificationLog_Section_VIII_6__S06.md
  - transparency/Canonical_MD/SP4_ProcessDocumentation/4.4_SectionGuidance/4.4.4_For_Section_VIII-A_now_6_from_5.2.1__S06.md
  - transparency/Canonical_MD/SP4_ProcessDocumentation/4.4_SectionGuidance/4.4.5_For_Section_VIII-B_from_Sideway_chat.md
  - transparency/Canonical_MD/SP4_ProcessDocumentation/4.5_SectionSummaries/4.5.7_SectionSummary_Section_VIII__S06.md
  - transparency/Canonical_MD/_HUBS/CHAT_3b4ee4d7-939e-4cb7-8830-571952d5b5a4.md
  - transparency/Canonical_MD/SP4_ProcessDocumentation/4.7_EpistemicTraces/4.7.3_PreliminaryChat 1.md
output_completed:
  - transparency/SCRIPTS/build_graph.py (multiple fixes — see MOD-001 through MOD-005)
  - transparency/SCRIPTS/fig_section6_network.py (aesthetic + structural pass — see MOD-006 through MOD-010)
  - transparency/SCRIPTS/hub_annotations.yaml (3b4ee4d7 entry added)
  - transparency/SCRIPTS/fig1_timeline.py (SVG output)
  - transparency/SCRIPTS/fig6_swimlanes.py (SVG output)
  - transparency/Canonical_MD/_GRAPHS/jpep_graph.html
  - transparency/Canonical_MD/_GRAPHS/jpep_graph_v1v2.html (new)
  - transparency/Canonical_MD/_GRAPHS/jpep_graph_III.html (new)
  - transparency/Canonical_MD/_GRAPHS/jpep_graph_CFP.html (new)
  - transparency/Canonical_MD/_GRAPHS/fig_section6_network.svg
  - transparency/Canonical_MD/_GRAPHS/fig1_timeline.svg
  - transparency/Canonical_MD/_GRAPHS/fig6_swimlanes.svg
---

# Modification Log: Graph infrastructure overhaul

---

## MOD-001 — hub_annotations.yaml: add missing 3b4ee4d7 entry

**File:** `transparency/SCRIPTS/hub_annotations.yaml`

**Problem:** The Section VIII writing hub (`3b4ee4d7`) had no top-level entry in
`hub_annotations.yaml`. `hub_date()` in `fig_section6_network.py` fell back to
the short UUID, displaying `3b4ee4d7` on the sun node instead of a date.

**Fix:** Added entry under `sessions:` with `date: 2025-10-18` (date from `4.4.5`
`source_chat_date` field, the session's multi-day end date) and `artifacts_produced`
list.

**Result:** Both sun nodes now display consistent date labels (`2025-10-12` and
`2025-10-18`). Earlier date is on the left.

---

## MOD-002 — build_graph.py: reverse edge direction for `inputs` relationships

**File:** `transparency/SCRIPTS/build_graph.py`

**Problem:** `_add_rel_edges()` drew all relational edges as `src → target` regardless
of field semantics. For `inputs`, `derived_from`, and `source_file` fields, this
produced edges pointing from the consuming artifact back to its input — the opposite
of information flow. A visible symptom: `4.2.9 → 4.7.3` implied 4.2.9 fed into
4.7.3, which is chronologically impossible.

**Fix:** For `canonical in ("inputs", "derived_from", "source_file")`, swap source
and target: `G.add_edge(target_node, src_id, ...)`. All other fields unchanged.

**Result:** All arrows now mean "feeds into". Edge count: 526 → 527 (one previously
self-cancelling edge resolved). Interactive graphs and `fig_section6_network` both
updated.

---

## MOD-003 — build_graph.py: comma splitting in `flatten_value`

**File:** `transparency/SCRIPTS/build_graph.py`

**Problem:** `flatten_value()` split on semicolons only. v1/v2-era artifacts use
comma-separated strings for relational fields (e.g., `4.7.3` has
`input_artifacts: SP5.1, 4.7.1, 4.7.2, ..., 4.1` — 21 items as one string).
The entire string was treated as an unresolvable token, making all those edges
invisible.

**Scope audit:** 7 fields across 3 files affected — `4.7.3` (3 fields),
`4.7.6.1` (3 fields), `5.2.6` (1 field). All v1/v2 era; CFP and III use YAML
lists or semicolons.

**Fix:** Split on `[;,]` regex instead of `";"` only.

**Result:** +49 edges in full graph (527 → 576). `4.7.3 → 4.1` and 48 other
previously invisible relationships now resolved.

---

## MOD-004 — build_graph.py: strip prose prefixes before IDs in `flatten_value`

**File:** `transparency/SCRIPTS/build_graph.py`

**Problem:** `4.4.4`'s `input_artifacts` field contains `"see 4.7.4"`. The word
"see" prevented `stem_to_era_id` from matching the numeric part, so `4.7.4` was
not recognised as a predecessor of `4.4.4`.

**Fix:** Added regex strip for leading prose words (`see`, `cf.`, `from`, `ref.`)
before attempting ID resolution.

**Result:** `4.7.4 → 4.4.4` edge now present. `4.7.4` appears as a bridge
predecessor in `fig_section6_network`.

---

## MOD-005 — build_graph.py: era-prefixed labels, `full_title` attribute, era-filtered HTMLs

**File:** `transparency/SCRIPTS/build_graph.py`

**Changes (three related improvements):**

1. **Era-prefixed labels.** Node `label` attribute now preserves the era prefix
   (`CFP_`, `III_`) alongside the numeric code. Previously the prefix was stripped,
   making all nodes show bare numbers in both the HTML and static figures.

2. **`full_title` node attribute.** The full frontmatter `label`/`title` field is
   now stored separately as `full_title` on each node, making it available for
   figure rendering without re-reading source files.

3. **Era-filtered HTMLs.** Added `filter_era(G, era)` function and three additional
   renders in `__main__`: `jpep_graph_v1v2.html` (129 nodes), `jpep_graph_III.html`
   (23 nodes), `jpep_graph_CFP.html` (116 nodes). Each contains only artifacts from
   that era plus hub nodes connected to them.

---

## MOD-006 — fig_section6_network.py: bridge predecessor nodes

**File:** `transparency/SCRIPTS/fig_section6_network.py`

**Problem:** The figure showed 4.4.4 and 4.4.5 as "bridge" artifacts between the
two sun clusters but gave no indication of where they came from.

**Fix:** After identifying bridge nodes, compute `bridge_pred_ids` — all direct
predecessors of bridge nodes in the directed graph. These are split into
`bridge_pred_hubs` (fb6251ae 2025-10-13, e9d55db6 2025-10-15) and
`bridge_pred_arts` (4.7.4, 5.3.13). Hub predecessors are excluded from `hubs_ring`
and given their own position between SUN1 and centre; artifact predecessors are
positioned above the bridge nodes.

**Result:** The guidance input chain is now visible: fb6251ae → 4.4.4 and
e9d55db6 → 4.4.5 show how methodology design sessions channelled into section
writing.

---

## MOD-007 — fig_section6_network.py: remove capo ticks; add full two-line labels

**File:** `transparency/SCRIPTS/fig_section6_network.py`

**Changes:**

1. **Capo ticks removed.** The perpendicular bars drawn at each edge source were
   visually floating and aesthetically confusing. Entire block removed.

2. **Full two-line labels.** Artifact labels now render as two lines: the numeric
   code (bold, era-prefixed) on the first line, and the descriptive title from
   `full_title` in smaller italic on the second. Titles truncated at 30 characters.
   The `artifact_number()` helper function was removed; labels come directly from
   the node's `label` attribute (which now carries the full numeric code including
   4-part numbers like `4.7.6.1`).

3. **Date labels moved closer.** Sun date offset reduced from `y - 0.11` to
   `y - 0.082`; other hub date offset from `y - 0.09` to `y - 0.062`.

---

## MOD-008 — fig_section6_network.py: updated legend

**File:** `transparency/SCRIPTS/fig_section6_network.py`

**Problem:** Legend listed "Section draft (versioned output)" — no section drafts
appear in the figure. Orange entry read "Section guidance (constraints fed into
drafting)" — orange is used for three distinct types (section guidance 4.4.4/4.4.5/
4.4.6, pattern summary 4.3.5, section summary 4.5.7). Label-colour entries described
a blue/black distinction that was no longer meaningful (all artifact labels are now
blue bold).

**Fix:** Removed "Section draft" entry. Renamed orange entry to "Section guidance /
pattern summary / section summary". Removed label-colour entries entirely.

---

## MOD-009 — fig_section6_network.py: updated caption

**File:** `transparency/SCRIPTS/fig_section6_network.py`

**Problem:** Caption still described the original two-sun, Section-6-centric design:
"Larger nodes are Section 6 artifacts across all three project phases." The figure
now has four hubs and shows the guidance input chain, not a phase-spanning Section 6
survey.

**Fix:** Rewrote caption to describe the actual figure: four-hub chain from
PreliminaryChat 1 (2025-10-12) through two intermediate methodology sessions
(2025-10-13, 2025-10-15) into the Section 6/VIII writing session (2025-10-18),
with 4.4.4 and 4.4.5 as the bridging guidance artifacts.

---

## MOD-010 — All three figure scripts: SVG output only, PNGs deleted

**Files:** `fig_section6_network.py`, `fig1_timeline.py`, `fig6_swimlanes.py`

**Change:** All three scripts now save SVG only (no `dpi=150` PNG). Existing PNG
files (`fig1_timeline.png`, `fig6_swimlanes.png`, `fig_section6_network.png`) deleted.
User will apply final touches manually in SVG.
