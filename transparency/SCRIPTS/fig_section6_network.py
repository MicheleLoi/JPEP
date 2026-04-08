"""
Static Section 6 full-history network — four-sun horizontal timeline.

Four session clusters arranged left-to-right in chronological order:
  SUN1  Oct 2025   PreliminaryChat 1 — methodology design
  SUN2  Oct 2025   Section VIII first writing
  SUN3  Jan–Mar 2026  Stage III MHC integration
  SUN4  Apr 2026   CFP rewrite (double-contestation + redundancy pass)

Output: transparency/Canonical_MD/_GRAPHS/fig_section6_network.svg
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
from pathlib import Path
import sys, re as _re
import numpy as np

# ── Import graph builder ──────────────────────────────────────────────────────
SCRIPTS_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPTS_DIR))
from build_graph import build_graph, TYPE_COLORS, safe_node_id

VAULT       = (SCRIPTS_DIR / "../Canonical_MD").resolve()
OUT         = VAULT / "_GRAPHS" / "fig_section6_network.svg"
ANNOTATIONS = SCRIPTS_DIR / "hub_annotations.yaml"

import yaml
G = build_graph(VAULT)

# ── Hub date helpers ──────────────────────────────────────────────────────────
_hub_dates = {}
if ANNOTATIONS.exists():
    _ann = yaml.safe_load(ANNOTATIONS.read_text(errors="ignore")) or {}
    _sessions = _ann.get("sessions", _ann)
    for _k, _v in _sessions.items():
        if isinstance(_v, dict):
            _hub_dates[str(_k).strip()] = str(_v.get("date", ""))

def hub_date(stem):
    m = _re.match(r"SID-(\d{4})(\d{2})(\d{2})", stem)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    if stem in _hub_dates:
        return _hub_dates[stem]
    for k, v in _hub_dates.items():
        if stem.startswith(k[:8]):
            return v
    return ""

def hub_short(stem):
    if stem.startswith("SID-"):
        return stem[4:18]
    return stem[:8]

# ── Four suns ─────────────────────────────────────────────────────────────────
SUN1_NODE = safe_node_id("HUB_5b8de38b-0044-4726-8eab-75e54460ec3e")  # PreliminaryChat 1
SUN2_NODE = safe_node_id("HUB_3b4ee4d7-939e-4cb7-8830-571952d5b5a4")  # §VIII writing
SUN3_NODE = safe_node_id("HUB_SID-20260202-115248")                    # III MHC guidance
SUN4_NODE = safe_node_id("HUB_SID-20260401-173934")                    # CFP rewrite

ALL_SUNS = {SUN1_NODE, SUN2_NODE, SUN3_NODE, SUN4_NODE}

G_undir = G.to_undirected()

def nbrs(node):
    return set(G_undir.neighbors(node)) if node in G.nodes else set()

n1_nbrs = nbrs(SUN1_NODE)
n2_nbrs = nbrs(SUN2_NODE)
n3_nbrs = nbrs(SUN3_NODE)
n4_nbrs = nbrs(SUN4_NODE)

all_nbrs = n1_nbrs | n2_nbrs | n3_nbrs | n4_nbrs
filtered = ALL_SUNS | all_nbrs

# Bridge: 4.4.4 and 4.4.5 (connect SUN1-cluster to SUN2-cluster)
BRIDGE_STEMS = {
    "4.4.4_For_Section_VIII-A_now_6_from_5.2.1__S06",
    "4.4.5_For_Section_VIII-B_from_Sideway_chat",
}
bridge_ids = {safe_node_id(s) for s in BRIDGE_STEMS if safe_node_id(s) in G.nodes}
filtered |= bridge_ids

# Bridge predecessors (hub + artifact inputs to 4.4.4 / 4.4.5)
bridge_pred_ids = set()
for bn in bridge_ids:
    if bn in G.nodes:
        for pred in G.predecessors(bn):
            if pred not in filtered:
                bridge_pred_ids.add(pred)
filtered |= bridge_pred_ids

# ── Chain intermediates: the actual input-output path SUN2→SUN3→SUN4 ─────────
# These are NOT 1-hop neighbours of any sun but form the documented version chain.
CHAIN_NODE_IDS = {
    "III_4.2.13_ModificationLog_Section6_v3",     # Stage III modlog: 4.2.9→III_4.4.5/III_5.2.1
    "III_5.4.2_Section6_v3",                        # Section 6 v3 draft: III_4.2.13→CFP_5.4.8
    "HUB_SID-20260302-152952",                      # Hub that produced III_5.4.2
    "CFP_4.2.18_ModificationLog_Section6",          # CFP Section 6 modlog: III_5.4.2→CFP_5.4.8
    "CFP_4.7.20_EpistemicTrace_Section6History",    # Synthesis trace aggregating all stages
}
filtered |= {n for n in CHAIN_NODE_IDS if n in G.nodes}

sub = G.subgraph(filtered).copy()
print(f"Subgraph: {sub.number_of_nodes()} nodes, {sub.number_of_edges()} edges")

bridge_pred_hubs = {n for n in bridge_pred_ids if n in sub.nodes
                    and sub.nodes[n]["node_type"] == "hub"}
bridge_pred_arts = {n for n in bridge_pred_ids if n in sub.nodes
                    and sub.nodes[n]["node_type"] != "hub"}

# ── Classify artifact nodes ───────────────────────────────────────────────────
def arts(nbr_set, *exclude_sets):
    out = {n for n in nbr_set
           if n in sub.nodes and sub.nodes[n]["node_type"] != "hub"}
    for ex in exclude_sets:
        out -= ex
    return out - bridge_ids

art1 = arts(n1_nbrs, n2_nbrs, n3_nbrs, n4_nbrs)
art2 = arts(n2_nbrs, n1_nbrs, n3_nbrs, n4_nbrs)
art3 = arts(n3_nbrs, n1_nbrs, n2_nbrs, n4_nbrs)
art4 = arts(n4_nbrs, n1_nbrs, n2_nbrs, n3_nbrs)
art_shared = (arts(all_nbrs)
              - art1 - art2 - art3 - art4
              | {n for n in bridge_ids if n in sub.nodes})

chain_nodes = {n for n in CHAIN_NODE_IDS if n in sub.nodes}
all_companion_ids = art1 | art2 | art3 | art4 | art_shared | bridge_pred_ids | chain_nodes

# ── Layout helpers ────────────────────────────────────────────────────────────
def half_ring(nodes, center, radius, facing_angle, spread=np.pi * 0.90):
    nodes = sorted(nodes, key=lambda n: G.nodes[n].get("label", n))
    n = len(nodes)
    if n == 0:
        return {}
    angles = ([facing_angle] if n == 1
              else [facing_angle + spread * (i / (n - 1) - 0.5) for i in range(n)])
    return {node: (center[0] + radius * np.cos(a),
                   center[1] + radius * np.sin(a))
            for node, a in zip(nodes, angles)}

# ── Sun positions: horizontal timeline ───────────────────────────────────────
S1 = np.array([-1.30,  0.0])   # methodology design
S2 = np.array([-0.45,  0.0])   # §VIII writing
S3 = np.array([ 0.40,  0.0])   # III MHC
S4 = np.array([ 1.35,  0.0])   # CFP rewrite

pos = {}
for node, p in [(SUN1_NODE, S1), (SUN2_NODE, S2),
                (SUN3_NODE, S3), (SUN4_NODE, S4)]:
    if node in sub.nodes:
        pos[node] = tuple(p)

# Each cluster fans away from its neighbour to avoid overlap:
#   SUN1 → LEFT   (π)
#   SUN2 → DOWN   (-π/2)
#   SUN3 → UP     (+π/2)
#   SUN4 → RIGHT  (0)
pos.update(half_ring(art1, S1, 0.44, facing_angle=np.pi))
pos.update(half_ring(art2, S2, 0.32, facing_angle=-np.pi * 0.75))   # down-left: clear chain rail
pos.update(half_ring(art3, S3, 0.32, facing_angle= np.pi * 0.60))   # up-right
pos.update(half_ring(art4, S4, 0.54, facing_angle=np.pi * 0.10,     # slightly up-right
                     spread=np.pi * 0.90))

# ── Chain intermediates: placed below the spine as a connecting rail ──────────
# Laid out left-to-right in the order they appear in the version chain.
chain_layout = {
    "III_4.2.13_ModificationLog_Section6_v3":    (-0.05, -0.35),  # SUN2→SUN3 bridge
    "HUB_SID-20260302-152952":                    ( 0.58, -0.22),  # hub: produced III_5.4.2
    "III_5.4.2_Section6_v3":                      ( 0.72, -0.42),  # Section 6 v3 draft
    "CFP_4.2.18_ModificationLog_Section6":        ( 1.00, -0.32),  # CFP Section 6 modlog
    "CFP_4.7.20_EpistemicTrace_Section6History":  ( 0.42, -0.50),  # synthesis: reads all stages
}
for nid, xy in chain_layout.items():
    if nid in sub.nodes:
        pos[nid] = xy

# Shared / bridge artifacts: above the midpoint of SUN2-SUN3
BRIDGE_MID = np.array([-0.80, 0.0])
pos.update(half_ring(art_shared, np.array([0.0, 0.0]), 0.18,
                     facing_angle=np.pi / 2, spread=np.pi * 0.70))

# Bridge predecessor hubs: above the SUN1-SUN2 midpoint
BPHUB_CENTER = np.array([-0.80, 0.42])
pos.update(half_ring(bridge_pred_hubs, BPHUB_CENTER, 0.20,
                     facing_angle=np.pi / 2, spread=np.pi * 0.70))
pos.update(half_ring(bridge_pred_arts, np.array([-0.80, 0.62]), 0.20,
                     facing_angle=np.pi / 2, spread=np.pi * 0.80))

# ── Figure ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(26, 13))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.axis("off")

# ── Node styling ──────────────────────────────────────────────────────────────
node_colors, node_sizes = [], []
node_size_map = {}
for n in sub.nodes:
    if n in ALL_SUNS:
        c, s = "#FFD700", 1600
    elif sub.nodes[n]["node_type"] == "hub":
        c, s = TYPE_COLORS["hub"], 700
    elif n in all_companion_ids:
        c, s = TYPE_COLORS.get(sub.nodes[n]["node_type"], "#E67E22"), 320
    else:
        c, s = TYPE_COLORS.get(sub.nodes[n]["node_type"], "#E67E22"), 180
    node_colors.append(c)
    node_sizes.append(s)
    node_size_map[n] = s

# ── Node radius (data units) ──────────────────────────────────────────────────
# Axes span ~3.2 units wide over 22 inches
_PT2DATA = 3.8 / (26 * 72)   # axes span ~3.8 units wide, figure 26 in

def node_radius_data(n):
    return (node_size_map.get(n, 200) ** 0.5) * 0.60 * _PT2DATA

# ── Radial label anchor ───────────────────────────────────────────────────────
_group_center = {}
for n in art1:             _group_center[n] = S1
for n in art2:             _group_center[n] = S2
for n in art3:             _group_center[n] = S3
for n in art4:             _group_center[n] = S4
for n in art_shared | bridge_ids:
                           _group_center[n] = np.array([0.0, -0.10])
for n in chain_nodes:      _group_center[n] = np.array([pos[n][0], pos[n][1] + 0.20]) if n in pos else np.array([0.0, 0.0])
for n in bridge_pred_hubs: _group_center[n] = BPHUB_CENTER
for n in bridge_pred_arts: _group_center[n] = np.array([-0.80, 0.40])

def radial_label_anchor(n, gap=0.024):
    x, y = pos[n]
    ctr  = _group_center.get(n, np.array([0.0, 0.0]))
    dx, dy = x - ctr[0], y - ctr[1]
    dist = np.hypot(dx, dy)
    if dist < 1e-6:
        dx, dy = 0.0, 1.0
    else:
        dx, dy = dx / dist, dy / dist
    r  = node_radius_data(n) + gap
    lx = x + dx * r
    ly = y + dy * r
    ha = "left" if dx > 0.28 else ("right" if dx < -0.28 else "center")
    va = "bottom" if dy > 0.18 else ("top" if dy < -0.18 else "center")
    return lx, ly, ha, va, dx, dy

# ── Draw edges ────────────────────────────────────────────────────────────────
nx.draw_networkx_edges(
    sub, pos, ax=ax,
    edge_color=[d.get("color", "#999") for _, _, d in sub.edges(data=True)],
    alpha=0.45, width=0.85,
    arrows=True, arrowsize=10, arrowstyle="-|>",
    node_size=node_sizes,
    min_source_margin=10,
    min_target_margin=14,
    connectionstyle="arc3,rad=0.12",
)

# ── Draw nodes ────────────────────────────────────────────────────────────────
nx.draw_networkx_nodes(
    sub, pos, ax=ax,
    node_color=node_colors,
    node_size=node_sizes,
    alpha=0.92, linewidths=0.5, edgecolors="#ffffff44",
)

# Sun halos
for sn, sp in [(SUN1_NODE, S1), (SUN2_NODE, S2),
               (SUN3_NODE, S3), (SUN4_NODE, S4)]:
    if sn in pos:
        ax.add_patch(plt.Circle(tuple(sp), 0.10, color="#FFD700",
                                alpha=0.15, zorder=1))

# ── Small date labels directly below each sun ────────────────────────────────
sun_dates = [(S1, "Oct 2025"), (S2, "Oct 2025"),
             (S3, "Jan–Mar 2026"), (S4, "Apr 2026")]
for sp, lbl in sun_dates:
    ax.text(sp[0], -0.12, lbl,
            ha="center", va="top", fontsize=6.5,
            color="#b8860b", fontweight="bold", alpha=0.85)

# ── Node labels ───────────────────────────────────────────────────────────────
for n, (x, y) in pos.items():
    ntype = sub.nodes[n]["node_type"]

    if n in ALL_SUNS:
        stem = sub.nodes[n].get("stem", "")
        dt   = hub_date(stem)
        lbl  = dt if dt else hub_short(stem)
        r    = node_radius_data(n) + 0.018
        ax.text(x, y - r, lbl,
                ha="center", va="top",
                fontsize=5.5, color="#b8860b", fontweight="bold", alpha=0.95)
        continue

    if ntype == "hub":
        stem = sub.nodes[n].get("stem", n)
        dt   = hub_date(stem)
        lbl  = dt if dt else hub_short(stem)
        lx, ly, ha, va, *_ = radial_label_anchor(n, gap=0.022)
        ax.text(lx, ly, lbl,
                ha=ha, va=va,
                fontsize=5.5, color="#b8860b", alpha=0.85)
        continue

    label = sub.nodes[n].get("label", n)
    is_companion = n in all_companion_ids
    fs  = 8.0 if is_companion else 6.0
    col = "#1a5fa8" if is_companion else "#555555"
    fw  = "bold" if is_companion else "normal"

    lx, ly, ha, va, *_ = radial_label_anchor(n, gap=0.026)
    ax.text(lx, ly, label,
            ha=ha, va=va,
            fontsize=fs, fontweight=fw, color=col, alpha=0.95)

# ── Legend ────────────────────────────────────────────────────────────────────
legend_items = [
    ("Session hub (one documented working episode)", TYPE_COLORS["hub"]),
    ("Modification log", TYPE_COLORS["modification_log"]),
    ("Epistemic trace", TYPE_COLORS["epistemic_trace"]),
    ("Section guidance / pattern summary", TYPE_COLORS["other"]),
    ("Prompt development log (PDL)", TYPE_COLORS["pdl"]),
    ("Section draft", TYPE_COLORS.get("section_draft", TYPE_COLORS["other"])),
    ("Note / work plan", TYPE_COLORS["note"]),
]
handles = [mpatches.Patch(facecolor=c, label=l, linewidth=0) for l, c in legend_items]

plt.tight_layout(rect=[0, 0.28, 1, 0.98])

ax.legend(
    handles, [l for l, _ in legend_items],
    loc="upper left",
    bbox_to_anchor=(0.01, 0.28),
    bbox_transform=fig.transFigure,
    fontsize=9, frameon=True,
    facecolor="white", edgecolor="#aaa",
    labelcolor="#222", framealpha=0.95,
    title="Artifact types",
    title_fontsize=10,
)

caption_text = (
    "Figure 3. The documented history of Section 6 across four production phases (Oct 2025 – Apr 2026).\n"
    "Each node is an artifact in SP-4 or SP-5; each directed edge is a documented input, derivation,\n"
    "or output relationship. Amber nodes are session hubs (one working episode each); node colour\n"
    "indicates artifact type (see legend). Four session clusters are arranged left-to-right:\n"
    "SUN1 — PreliminaryChat 1, methodology design (Oct 2025); SUN2 — Section VIII first writing\n"
    "(Oct 2025, Claude.ai / Sonnet 4.5); SUN3 — Stage III MHC integration (Jan–Mar 2026, Claude\n"
    "Code); SUN4 — CFP rewrite (Apr 2026, Claude Code / Opus 4.6).\n"
    "  The lower rail shows the documented version chain connecting the clusters. III_4.2.13\n"
    "(Stage III modlog) is the bridge between SUN2 and SUN3: it records that 4.2.9 (SUN2's primary\n"
    "modlog) was the source text, and its outputs include the revised guidance III_4.4.5 and PDL\n"
    "III_5.2.1 (both SUN3 neighbours). The hub SID-20260302-152952 produced III_5.4.2 (Section 6\n"
    "v3 draft), which is the direct source_jpep of CFP_5.4.8 (SUN4's Section 6 draft); CFP_4.2.18\n"
    "records that three-draft CFP session. CFP_4.7.20 (bottom, teal) is a synthesis epistemic trace\n"
    "that aggregates all four phases and feeds directly into SP-3 drafting.\n"
    "  The full trace exercises all three Section 7 criteria: attribution (model switch Opus 4.5 →\n"
    "Sonnet 4.6 after irrecoverable Jan 2026 draft; dual-reviewer verdicts in CFP_4.2.18);\n"
    "intellectual trajectory (seven documented transformations across 5.5 months); understanding-\n"
    "and-endorsement (13-entry modlog with both Reviewer A and Reviewer B records visible)."
)
fig.text(
    0.26, 0.01, caption_text,
    ha="left", va="bottom",
    fontsize=8.0, color="#222", linespacing=1.50,
    bbox=dict(boxstyle="round,pad=0.7", facecolor="white",
              edgecolor="#aaa", linewidth=1),
)

plt.savefig(str(OUT), bbox_inches="tight", facecolor="white")
print(f"Saved {OUT}")
