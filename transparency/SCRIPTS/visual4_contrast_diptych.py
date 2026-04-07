"""
Visual 4: Contrast Diptych
Compares documentation density for the Introduction section across two phases.
Left: v1/v2 (Oct 2025) — sparse, with ghost nodes for deleted chats.
Right: CFP (Mar 2026) — dense, with full MHC-W infrastructure.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx
import numpy as np
from pathlib import Path

# ── Colour palette ──────────────────────────────────────────────────
C_DRAFT   = "#4A90D9"   # blue — drafts
C_MODLOG  = "#5BA85B"   # green — modlogs
C_TRACE   = "#8E6FBF"   # purple — epistemic traces
C_HUB     = "#D4A24C"   # amber — session hubs
C_OTHER   = "#999999"   # grey — other / audit
C_GHOST   = "#D0D0D0"   # light grey fill for deleted nodes
C_EDGE    = "#555555"
C_EDGE_GHOST = "#AAAAAA"
C_WORK    = "#C27A3A"   # work plan (amber-brown)

FONT      = "sans-serif"
NODE_SIZE  = 1800
FONT_SIZE  = 8.0
EDGE_WIDTH = 1.4

# ── Helper: draw one panel ──────────────────────────────────────────
def draw_panel(ax, G, pos, node_styles, edge_styles, title):
    """
    node_styles: dict  node -> {color, edgecolor, linestyle, linewidth, alpha, fontweight}
    edge_styles: dict  (u,v) -> {style, color, alpha, width}
    """
    # Draw edges first
    for (u, v), style in edge_styles.items():
        xs = [pos[u][0], pos[v][0]]
        ys = [pos[u][1], pos[v][1]]
        ax.annotate(
            "",
            xy=(pos[v][0], pos[v][1]),
            xytext=(pos[u][0], pos[u][1]),
            arrowprops=dict(
                arrowstyle="-|>",
                color=style.get("color", C_EDGE),
                lw=style.get("width", EDGE_WIDTH),
                linestyle=style.get("style", "solid"),
                alpha=style.get("alpha", 0.7),
                shrinkA=18, shrinkB=18,
                connectionstyle="arc3,rad=0.05",
            ),
        )

    # Draw nodes
    for node, data in G.nodes(data=True):
        s = node_styles[node]
        x, y = pos[node]

        # Node ellipse
        ellipse = mpatches.FancyBboxPatch(
            (x - 0.18, y - 0.07), 0.36, 0.14,
            boxstyle="round,pad=0.02",
            facecolor=s["color"],
            edgecolor=s["edgecolor"],
            linewidth=s.get("linewidth", 1.6),
            linestyle=s.get("linestyle", "solid"),
            alpha=s.get("alpha", 1.0),
            zorder=3,
        )
        ax.add_patch(ellipse)

        # Label
        ax.text(
            x, y, data.get("label", node),
            ha="center", va="center",
            fontsize=FONT_SIZE,
            fontfamily=FONT,
            fontweight=s.get("fontweight", "normal"),
            color="#222222" if s["color"] != C_GHOST else "#888888",
            zorder=4,
        )

    ax.set_xlim(-0.50, 0.50)
    ax.set_ylim(-0.45, 0.45)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=10.5, fontfamily=FONT, fontweight="bold",
                 pad=10, color="#333333")


# ═══════════════════════════════════════════════════════════════════
#  LEFT PANEL — v1/v2 (Oct 2025): sparse
# ═══════════════════════════════════════════════════════════════════
G_left = nx.DiGraph()
G_left.add_node("intro",   label="Introduction\nv1")
G_left.add_node("chat1",   label="Chat 1\n(deleted)")
G_left.add_node("modlog1", label="4.2.1\nModlog")
G_left.add_node("audit",   label="4.4.10\nAudit guidance")

# Sparse edges — chat is deleted so link is broken; modlog has no session link
G_left.add_edge("chat1",  "intro")      # chat produced draft (but chat is gone)
G_left.add_edge("modlog1", "intro")      # modlog documents intro (no source_chat_id)
# audit is from a different session entirely — floating

pos_left = {
    "intro":   ( 0.00,  0.22),
    "chat1":   (-0.25, -0.05),
    "modlog1": ( 0.25, -0.05),
    "audit":   ( 0.00, -0.32),
}

nstyle_left = {
    "intro":   dict(color=C_DRAFT,  edgecolor="#2D6CB4", linestyle="solid", linewidth=1.6, fontweight="bold"),
    "chat1":   dict(color=C_GHOST,  edgecolor="#999999", linestyle="dashed", linewidth=1.6, alpha=0.6, fontweight="normal"),
    "modlog1": dict(color=C_MODLOG, edgecolor="#3D7E3D", linestyle="solid", linewidth=1.6, fontweight="normal"),
    "audit":   dict(color=C_OTHER,  edgecolor="#777777", linestyle="solid", linewidth=1.6, fontweight="normal"),
}

estyle_left = {
    ("chat1", "intro"):   dict(style="dashed", color=C_EDGE_GHOST, alpha=0.45, width=1.2),
    ("modlog1", "intro"):  dict(style="solid",  color=C_EDGE, alpha=0.5, width=1.2),
}

# ═══════════════════════════════════════════════════════════════════
#  RIGHT PANEL — CFP (Mar 2026): dense
# ═══════════════════════════════════════════════════════════════════
G_right = nx.DiGraph()
G_right.add_node("v1",      label="Introduction\nv1")
G_right.add_node("v2",      label="Introduction\nv2")
G_right.add_node("hub",     label="Session\nhub")
G_right.add_node("modlog2", label="4.2.14\nModlog")
G_right.add_node("trace",   label="4.7.5\nTrace")
G_right.add_node("wplan",   label="5.3.1\nWork plan")

# Dense edges
G_right.add_edge("v1", "v2")          # derived_from
G_right.add_edge("hub", "v1")         # hub → draft v1
G_right.add_edge("hub", "v2")         # hub → draft v2
G_right.add_edge("hub", "modlog2")    # hub → modlog
G_right.add_edge("hub", "trace")      # hub → trace
G_right.add_edge("trace", "v1")       # trace feeds into drafting
G_right.add_edge("modlog2", "v1")     # modlog documents v1
G_right.add_edge("modlog2", "v2")     # modlog documents v2
G_right.add_edge("wplan", "hub")      # work plan linked as input

pos_right = {
    "hub":     (-0.14,  0.28),
    "wplan":   ( 0.30,  0.28),
    "v1":      (-0.24,  0.00),
    "v2":      ( 0.24,  0.00),
    "trace":   (-0.24, -0.28),
    "modlog2": ( 0.24, -0.28),
}

nstyle_right = {
    "v1":      dict(color=C_DRAFT,  edgecolor="#2D6CB4", linestyle="solid", linewidth=1.6, fontweight="bold"),
    "v2":      dict(color=C_DRAFT,  edgecolor="#2D6CB4", linestyle="solid", linewidth=1.6, fontweight="bold"),
    "hub":     dict(color=C_HUB,    edgecolor="#A67C2E", linestyle="solid", linewidth=1.6, fontweight="bold"),
    "modlog2": dict(color=C_MODLOG, edgecolor="#3D7E3D", linestyle="solid", linewidth=1.6, fontweight="normal"),
    "trace":   dict(color=C_TRACE,  edgecolor="#6B4FA0", linestyle="solid", linewidth=1.6, fontweight="normal"),
    "wplan":   dict(color=C_WORK,   edgecolor="#8E5520", linestyle="solid", linewidth=1.6, fontweight="normal"),
}

estyle_right = {
    ("v1", "v2"):          dict(style="solid", color=C_DRAFT,  alpha=0.7, width=1.8),
    ("hub", "v1"):         dict(style="solid", color=C_HUB,    alpha=0.6, width=1.4),
    ("hub", "v2"):         dict(style="solid", color=C_HUB,    alpha=0.6, width=1.4),
    ("hub", "modlog2"):    dict(style="solid", color=C_HUB,    alpha=0.6, width=1.4),
    ("hub", "trace"):      dict(style="solid", color=C_HUB,    alpha=0.6, width=1.4),
    ("trace", "v1"):       dict(style="solid", color=C_TRACE,  alpha=0.6, width=1.3),
    ("modlog2", "v1"):     dict(style="solid", color=C_MODLOG, alpha=0.5, width=1.2),
    ("modlog2", "v2"):     dict(style="solid", color=C_MODLOG, alpha=0.5, width=1.2),
    ("wplan", "hub"):      dict(style="solid", color=C_WORK,   alpha=0.6, width=1.3),
}


# ═══════════════════════════════════════════════════════════════════
#  RENDER
# ═══════════════════════════════════════════════════════════════════
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))
fig.subplots_adjust(wspace=0.08, left=0.02, right=0.98, top=0.88, bottom=0.10)

draw_panel(ax1, G_left,  pos_left,  nstyle_left,  estyle_left,  "v1/v2 (Oct 2025)")
draw_panel(ax2, G_right, pos_right, nstyle_right, estyle_right, "CFP (Mar 2026)")

# ── Legend (shared, bottom centre) ──────────────────────────────────
legend_elements = [
    mpatches.Patch(facecolor=C_DRAFT,  edgecolor="#2D6CB4", label="Draft"),
    mpatches.Patch(facecolor=C_MODLOG, edgecolor="#3D7E3D", label="Modification log"),
    mpatches.Patch(facecolor=C_TRACE,  edgecolor="#6B4FA0", label="Epistemic trace"),
    mpatches.Patch(facecolor=C_HUB,    edgecolor="#A67C2E", label="Session hub"),
    mpatches.Patch(facecolor=C_WORK,   edgecolor="#8E5520", label="Work plan"),
    mpatches.Patch(facecolor=C_OTHER,  edgecolor="#777777", label="Audit guidance"),
    mpatches.Patch(facecolor=C_GHOST,  edgecolor="#999999", linestyle="dashed",
                   label="Deleted / unrecoverable"),
]

fig.legend(
    handles=legend_elements,
    loc="lower center",
    ncol=4,
    fontsize=7.5,
    frameon=False,
    handlelength=1.4,
    handleheight=1.0,
    columnspacing=1.2,
)

# ── Save ────────────────────────────────────────────────────────────
out_dir = Path(r"C:\Users\loimi\switchdrive\CURRENTLY WORKING ON\AI - assisted papers\JPEP\transparency\Canonical_MD\_GRAPHS")
out_path = out_dir / "visual4_contrast_diptych.png"
fig.savefig(str(out_path), dpi=300, bbox_inches="tight", facecolor="white")
plt.close(fig)
print(f"Saved: {out_path}")
