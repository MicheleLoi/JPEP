"""
Visual 3 — Feedback Loop
Appendix → Section 6 revision cycle showing recursive transparency discovery.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── layout ──────────────────────────────────────────────────────────────
# Arrange nodes in a roughly circular/loop shape so the recursion is obvious.
# Positions chosen by hand for clarity.

nodes = {
    "paper":     {"label": "Paper body\n(Sections I–IX)",
                  "pos": (0.18, 0.72)},
    "appendix":  {"label": "Appendix writing\n(Oct 19 – Nov 3)",
                  "pos": (0.72, 0.85)},
    "discovery": {"label": "Discovery:\ninfrastructure\nconstraints",
                  "pos": (0.88, 0.42)},
    "revision":  {"label": "Section 6.2\nrevision\n(Nov 5–6)",
                  "pos": (0.50, 0.12)},
}

edges = [
    ("paper",     "appendix",  "4.2.11"),
    ("appendix",  "discovery", ""),
    ("discovery", "revision",  "4.4.13"),
    ("revision",  "paper",     "4.2.9\nMOD-009"),
]

# ── colours ─────────────────────────────────────────────────────────────
BG       = "#FAFAFA"
NODE_FC  = "#E8EDF2"
NODE_EC  = "#5B7FA5"
EDGE_C   = "#5B7FA5"
TEXT_C    = "#1E2A38"
LABEL_C  = "#6B4C8A"

# ── figure ──────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(5.5, 4.2), dpi=300)
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(-0.05, 1.05)
ax.set_ylim(-0.05, 1.05)
ax.set_aspect("equal")
ax.axis("off")

# ── draw nodes as rounded rectangles ────────────────────────────────────
box_w, box_h = 0.22, 0.18
for key, nd in nodes.items():
    x, y = nd["pos"]
    rect = mpatches.FancyBboxPatch(
        (x - box_w / 2, y - box_h / 2), box_w, box_h,
        boxstyle="round,pad=0.02",
        facecolor=NODE_FC, edgecolor=NODE_EC, linewidth=1.3,
        zorder=3,
    )
    ax.add_patch(rect)
    ax.text(x, y, nd["label"], ha="center", va="center",
            fontsize=7, color=TEXT_C, fontfamily="sans-serif",
            linespacing=1.2, zorder=4)

# ── helper: compute connection points on box edges ──────────────────────
def box_intersect(src_pos, dst_pos, hw, hh):
    """Return the point on the edge of the source box closest to dst."""
    sx, sy = src_pos
    dx, dy = dst_pos
    vx, vy = dx - sx, dy - sy
    length = np.hypot(vx, vy)
    if length == 0:
        return src_pos
    ux, uy = vx / length, vy / length
    # time to hit vertical / horizontal edges
    tx = (hw / abs(ux)) if abs(ux) > 1e-9 else 1e9
    ty = (hh / abs(uy)) if abs(uy) > 1e-9 else 1e9
    t = min(tx, ty)
    return (sx + ux * t, sy + uy * t)

# ── draw edges ──────────────────────────────────────────────────────────
arrow_style = mpatches.ArrowStyle("-|>", head_length=6, head_width=3.5)
hw, hh = box_w / 2 + 0.015, box_h / 2 + 0.015  # half-widths with padding

for src_key, dst_key, label in edges:
    sp = nodes[src_key]["pos"]
    dp = nodes[dst_key]["pos"]
    start = box_intersect(sp, dp, hw, hh)
    end   = box_intersect(dp, sp, hw, hh)

    # Determine curvature: the loop-closing edge gets more curve
    if src_key == "revision" and dst_key == "paper":
        style = "arc3,rad=-0.35"
    else:
        style = "arc3,rad=0.10"

    arrow = mpatches.FancyArrowPatch(
        start, end,
        arrowstyle=arrow_style,
        connectionstyle=style,
        color=EDGE_C, linewidth=1.3, zorder=2,
    )
    ax.add_patch(arrow)

    # edge label
    if label:
        mx = (start[0] + end[0]) / 2
        my = (start[1] + end[1]) / 2
        # offset label slightly outward from circle centre (0.5, 0.5)
        cx, cy = 0.5, 0.5
        ox = (mx - cx) * 0.18
        oy = (my - cy) * 0.18
        ax.text(mx + ox, my + oy, label,
                ha="center", va="center",
                fontsize=5.5, color=LABEL_C, fontstyle="italic",
                fontfamily="sans-serif", zorder=5,
                bbox=dict(boxstyle="round,pad=0.15", fc=BG, ec="none", alpha=0.85))

# ── small annotation: the recursive insight ─────────────────────────────
ax.annotate(
    "recursion",
    xy=(0.14, 0.42), fontsize=6, color="#888888",
    fontstyle="italic", ha="center", va="center",
    fontfamily="sans-serif",
)
# thin curved arrow hint near the loop-back edge
ax.annotate(
    "", xy=(0.16, 0.48), xytext=(0.16, 0.36),
    arrowprops=dict(arrowstyle="->", color="#BBBBBB", lw=0.7,
                    connectionstyle="arc3,rad=0.5"),
    zorder=1,
)

plt.tight_layout(pad=0.3)
out = r"C:\Users\loimi\switchdrive\CURRENTLY WORKING ON\AI - assisted papers\JPEP\transparency\Canonical_MD\_GRAPHS\visual3_feedback_loop.png"
fig.savefig(out, dpi=300, facecolor=BG, bbox_inches="tight")
plt.close(fig)
print(f"Saved -> {out}")
