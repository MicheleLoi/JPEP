"""
Figure 5 — Failure and the visible decision (Stage 3 detail).
Small horizontal flow: initial guidance → ghost draft → revised guidance → successful redraft.
Branch from redraft: SP reconception.
Output: transparency/Canonical_MD/_GRAPHS/fig5_visible_decision.png
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(13, 5.5))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.set_xlim(-0.5, 13)
ax.set_ylim(-2.5, 5.5)
ax.axis("off")

NODE_W = 2.6
NODE_H = 1.4

def box(ax, cx, cy, label, sublabel, fc, ec="#555", lw=1.2, ls="-", alpha=1.0):
    rect = mpatches.FancyBboxPatch(
        (cx - NODE_W/2, cy - NODE_H/2), NODE_W, NODE_H,
        boxstyle="round,pad=0.35", linewidth=lw,
        facecolor=fc, edgecolor=ec, linestyle=ls, alpha=alpha
    )
    ax.add_patch(rect)
    ax.text(cx, cy + 0.22, label, ha="center", va="center",
            fontsize=8, fontweight="bold", color="#2d3436", alpha=alpha)
    ax.text(cx, cy - 0.3, sublabel, ha="center", va="center",
            fontsize=6.5, color="#636e72", alpha=alpha)

def arrow(ax, x1, y1, x2, y2, label="", color="#555", lw=1.5, ls="-",
          head="->", rad=0.0, label_offset=(0, 0.25)):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(
                    arrowstyle=f"-|>,head_width=0.25,head_length=0.2",
                    color=color, lw=lw, linestyle=ls,
                    connectionstyle=f"arc3,rad={rad}"
                ))
    if label:
        mx = (x1 + x2) / 2 + label_offset[0]
        my = (y1 + y2) / 2 + label_offset[1]
        ax.text(mx, my, label, ha="center", va="center",
                fontsize=7, color=color,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none"))

# ── Node positions ────────────────────────────────────────────────────────────
Y_MAIN = 2.5
X1, X2, X3, X4 = 1.5, 4.5, 7.5, 10.5

# Node 1 — Initial guidance
box(ax, X1, Y_MAIN, "2026-01-26",
    "III_4.4.5 v1\nInitial guidance\nOpus 4.5 · target 1200–1500w",
    fc="#dfe6e9")

# Node 2 — Failed draft (ghost)
box(ax, X2, Y_MAIN, "2026-01-28",
    "Failed draft\nno git commit · no export\noverwritten · irrecoverable",
    fc="#f8f9fa", ec="#b2bec3", lw=1.2, ls="dashed", alpha=0.65)
# Ghost label above
ax.text(X2, Y_MAIN + NODE_H/2 + 0.3,
        "Known only from III_4.2.13\nEntry 1 + guidance revision timestamp",
        ha="center", va="bottom", fontsize=6, color="#b2bec3", fontstyle="italic")

# Node 3 — Guidance revised
box(ax, X3, Y_MAIN, "2026-01-28",
    "III_4.4.5 — guidance revised\n\"Existing Section 6 reading\nnow MANDATORY\"",
    fc="#ffeaa7")

# Node 4 — Successful redraft
box(ax, X4, Y_MAIN, "2026-03-02",
    "III_5.4.2_Section6_v3.md\n~1400 words\nSID-20260302-152952 · Sonnet 4.6",
    fc="#55efc4")

# Arrows
arrow(ax, X1 + NODE_W/2, Y_MAIN, X2 - NODE_W/2, Y_MAIN)
arrow(ax, X2 + NODE_W/2, Y_MAIN, X3 - NODE_W/2, Y_MAIN,
      label="same day:\nguidance revised\nin response")
arrow(ax, X3 + NODE_W/2, Y_MAIN, X4 - NODE_W/2, Y_MAIN,
      label="model switch:\nOpus 4.5 → Sonnet 4.6",
      color="#e17055", lw=2.0, label_offset=(0, 0.35))

# Branch from node 4 downward → SP reconception
X_BRANCH = X4
Y_BRANCH = Y_MAIN - NODE_H/2 - 0.5
Y_SPREC = -1.2

arrow(ax, X_BRANCH, Y_MAIN - NODE_H/2,
      X_BRANCH, Y_SPREC + 0.75,
      color="#6c5ce7", lw=1.5, ls="dashed")

# SP reconception box
rec = mpatches.FancyBboxPatch(
    (X4 - 2.0, Y_SPREC - 0.55), 4.0, 1.1,
    boxstyle="round,pad=0.3", linewidth=1.2,
    facecolor="#d8b4fe", edgecolor="#6c5ce7"
)
ax.add_patch(rec)
ax.text(X4, Y_SPREC, "Same session:\nIII_4.7.3 SP reconception\n— methodology of entire paper reorganized",
        ha="center", va="center", fontsize=7, color="#2d3436")
ax.text(X4 - 2.3, Y_SPREC, "↲ branch", ha="right", va="center",
        fontsize=6.5, color="#6c5ce7", fontstyle="italic")

# ── Caption ──────────────────────────────────────────────────────────────────
fig.text(0.5, 0.01,
         "Figure 5. Failure and the visible decision (Stage 3). "
         "The ghost node (dashed) is the one place the record falls short — scoped and acknowledged.\n"
         "The figure's subject is the visible decision (model switch) and its consequence (SP reconception). "
         "Verify: III_4.4.5, III_4.2.13 Entry 1, III_4.7.3, CFP_5.3.19.",
         ha="center", va="bottom", fontsize=6.5, color="#555")

plt.tight_layout(rect=[0, 0.06, 1, 0.97])
out = "transparency/Canonical_MD/_GRAPHS/fig5_visible_decision.png"
plt.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
print(f"Saved {out}")
