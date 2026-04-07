"""
Visual 5 -- Version Chain
Section 6's three CFP draft versions with derived_from links and modlog.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# -- nodes ----------------------------------------------------------------
# Layout: v3 left, v4 right, modlog bottom-centre, hub top-centre
nodes = {
    "v3":      {"label": "Section 6 v3\n(III_5.4.2)",
                "pos": (0.15, 0.55)},
    "v4":      {"label": "Section 6 v4\n(CFP_5.4.8)",
                "pos": (0.65, 0.55)},
    "modlog":  {"label": "Modlog\n(CFP_4.2.18)\n13 entries",
                "pos": (0.40, 0.10)},
    "hub":     {"label": "Session hub\n(SID-20260401\n-173934)",
                "pos": (0.40, 0.88)},
}

edges = [
    ("v3",     "v4",     "derived_from",          None),
    ("hub",    "v4",     "produced in",            None),
    ("hub",    "modlog", "produced in",            None),
    ("modlog", "v3",     "documents\nchanges to",  None),
    ("modlog", "v4",     "documents\nchanges to",  None),
]

# -- colours --------------------------------------------------------------
BG       = "#FAFAFA"
NODE_FC  = {"v3": "#E3ECF5", "v4": "#D6E8D6", "modlog": "#F5EBDB", "hub": "#EDE3F0"}
NODE_EC  = "#5B7FA5"
EDGE_C   = "#5B7FA5"
TEXT_C   = "#1E2A38"
LABEL_C  = "#6B4C8A"

# -- figure ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(5.2, 4.0), dpi=300)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(-0.05, 1.0)
ax.set_ylim(-0.08, 1.05)
ax.set_aspect("equal")
ax.axis("off")

# -- draw nodes ------------------------------------------------------------
box_w, box_h = 0.22, 0.18
for key, nd in nodes.items():
    x, y = nd["pos"]
    rect = mpatches.FancyBboxPatch(
        (x - box_w / 2, y - box_h / 2), box_w, box_h,
        boxstyle="round,pad=0.02",
        facecolor=NODE_FC.get(key, "#E8EDF2"),
        edgecolor=NODE_EC, linewidth=1.3, zorder=3,
    )
    ax.add_patch(rect)
    ax.text(x, y, nd["label"], ha="center", va="center",
            fontsize=6.5, color=TEXT_C, fontfamily="sans-serif",
            linespacing=1.15, zorder=4)

# -- edge helper -----------------------------------------------------------
def box_edge(src, dst, hw, hh):
    sx, sy = src; dx, dy = dst
    vx, vy = dx - sx, dy - sy
    L = np.hypot(vx, vy)
    if L == 0: return src
    ux, uy = vx / L, vy / L
    tx = (hw / abs(ux)) if abs(ux) > 1e-9 else 1e9
    ty = (hh / abs(uy)) if abs(uy) > 1e-9 else 1e9
    t = min(tx, ty)
    return (sx + ux * t, sy + uy * t)

hw, hh = box_w / 2 + 0.012, box_h / 2 + 0.012

arrow_style = mpatches.ArrowStyle("-|>", head_length=5, head_width=3)

# Manual label offsets keyed by (src, dst) to avoid overlap
label_offsets = {
    ("v3", "v4"):         (0.0,  0.06),
    ("hub", "v4"):        (0.15,  0.0),
    ("hub", "modlog"):    (-0.22,  0.12),
    ("modlog", "v3"):     (-0.15, -0.02),
    ("modlog", "v4"):     (0.15, -0.02),
}

curve_rad = {
    ("v3", "v4"):       0.0,
    ("hub", "v4"):      0.15,
    ("hub", "modlog"):  -0.15,
    ("modlog", "v3"):   -0.15,
    ("modlog", "v4"):   0.15,
}

for src_key, dst_key, label, _ in edges:
    sp = nodes[src_key]["pos"]
    dp = nodes[dst_key]["pos"]
    start = box_edge(sp, dp, hw, hh)
    end   = box_edge(dp, sp, hw, hh)

    rad = curve_rad.get((src_key, dst_key), 0.08)
    style = f"arc3,rad={rad}"

    arrow = mpatches.FancyArrowPatch(
        start, end,
        arrowstyle=arrow_style,
        connectionstyle=style,
        color=EDGE_C, linewidth=1.2, zorder=2,
    )
    ax.add_patch(arrow)

    if label:
        # For hub->modlog, use absolute position to avoid overlap with v3 node
        if (src_key, dst_key) == ("hub", "modlog"):
            lx, ly = -0.02, 0.72
        else:
            mx = (start[0] + end[0]) / 2
            my = (start[1] + end[1]) / 2
            ox, oy = label_offsets.get((src_key, dst_key), (0, 0))
            lx, ly = mx + ox, my + oy
        ax.text(lx, ly, label,
                ha="center", va="center",
                fontsize=5, color=LABEL_C, fontstyle="italic",
                fontfamily="sans-serif", zorder=5,
                linespacing=1.1,
                bbox=dict(boxstyle="round,pad=0.12", fc=BG, ec="none", alpha=0.85))

plt.tight_layout(pad=0.3)
out = r"C:\Users\loimi\switchdrive\CURRENTLY WORKING ON\AI - assisted papers\JPEP\transparency\Canonical_MD\_GRAPHS\visual5_version_chain.png"
fig.savefig(out, dpi=300, facecolor=BG, bbox_inches="tight")
plt.close(fig)
print(f"Saved -> {out}")
