"""
Figure 2 — The feedback loop (§6.2 ↔ Appendix A.2 recursion).
Six-node directed graph with a heavy dashed back-arrow.
Output: transparency/Canonical_MD/_GRAPHS/fig2_feedback_loop.png
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(11, 7))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.set_xlim(-0.5, 10.5)
ax.set_ylim(-1, 6)
ax.axis("off")

# ── Node definitions ─────────────────────────────────────────────────────────
# Laid out in a clockwise loop so the back-arrow is obvious
nodes = {
    1: (2.0, 4.5, "Section VIII\nwriting in progress\n(chat 3b4ee4d7,\n2025-10-15)"),
    2: (5.5, 4.5, "Appendix A.2\ndrafting\n(same chat,\n2025-11-05)"),
    3: (8.5, 3.0, "Infrastructure\nconstraint\nobserved"),
    4: (8.5, 1.0, "4.4.13 bridging\nguidance\n(§6.2 AND App. A.2\nsimultaneously)"),
    5: (5.5, -0.2, "Revision chat\n65a571f1\n(2025-11-06)"),
    6: (2.0, -0.2, "§6.2 modified\n4.2.9 MOD-009\n(manual_copy_paste)"),
}

NODE_W = 2.2
NODE_H = 1.1
BOX_STYLE = dict(boxstyle="round,pad=0.4", linewidth=1.2)

node_colors = {
    1: "#dfe6e9", 2: "#dfe6e9", 3: "#ffeaa7",
    4: "#b2bec3", 5: "#dfe6e9", 6: "#55efc4",
}

for nid, (cx, cy, label) in nodes.items():
    fc = node_colors[nid]
    rect = mpatches.FancyBboxPatch(
        (cx - NODE_W/2, cy - NODE_H/2), NODE_W, NODE_H,
        **BOX_STYLE, facecolor=fc, edgecolor="#636e72"
    )
    ax.add_patch(rect)
    ax.text(cx, cy, label, ha="center", va="center",
            fontsize=7, color="#2d3436")

# ── Helper: draw arrow between nodes ─────────────────────────────────────────
def arrow(ax, n1, n2, nodes, label="", color="#636e72", lw=1.5,
          ls="-", head=0.3, xoff=0, yoff=0):
    x1, y1, _ = nodes[n1]
    x2, y2, _ = nodes[n2]
    # offset midpoint text
    mx, my = (x1+x2)/2 + xoff, (y1+y2)/2 + yoff
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=f"-|>,head_width={head},head_length=0.2",
                                color=color, lw=lw, linestyle=ls,
                                connectionstyle="arc3,rad=0.0"))
    if label:
        ax.text(mx, my, label, ha="center", va="center",
                fontsize=6.5, color=color,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"))

# Forward arrows
arrow(ax, 1, 2, nodes, "writing\nproduces appendix")
arrow(ax, 2, 3, nodes, "appendix work\nsurfaces constraint", yoff=0.3)
arrow(ax, 3, 4, nodes, "constraint codified\nas bridging guidance")
arrow(ax, 4, 5, nodes, "guidance feeds\nrevision chat", yoff=-0.3)
arrow(ax, 5, 6, nodes, "§6.2 revised\n(loop closes)")

# Back arrow — dashed, heavier, red
x6, y6, _ = nodes[6]
x1, y1, _ = nodes[1]
ax.annotate("", xy=(x1, y1 - NODE_H/2), xytext=(x6, y6 - NODE_H/2),
            arrowprops=dict(
                arrowstyle="-|>,head_width=0.45,head_length=0.25",
                color="#d63031", lw=2.8, linestyle="dashed",
                connectionstyle="arc3,rad=-0.35"
            ))
ax.text(3.75, -1.1,
        "\"the section about transparency was modified\nby the act of documenting transparency\"",
        ha="center", va="top", fontsize=7, color="#d63031", fontstyle="italic")

# ── Caption ──────────────────────────────────────────────────────────────────
fig.text(0.5, 0.01,
         "Figure 2. The feedback loop. The §6.2 ↔ Appendix A.2 recursion: "
         "documenting Section VIII surfaced a constraint that fed back into the section itself.\n"
         "The dashed red arrow is the loop-closing edge — the figure's whole point. "
         "Verify: 4.4.13, 4.2.9 MOD-009, 4.7.7.4 epistemic trace.",
         ha="center", va="bottom", fontsize=6.5, color="#555")

plt.tight_layout(rect=[0, 0.07, 1, 0.97])
out = "transparency/Canonical_MD/_GRAPHS/fig2_feedback_loop.png"
plt.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
print(f"Saved {out}")
