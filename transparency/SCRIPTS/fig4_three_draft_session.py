"""
Figure 4 — The three-draft session (Stage 4 detail).
Vertical chain: inputs → v1 → v2 → v3 → modlog, with side annotations.
Output: transparency/Canonical_MD/_GRAPHS/fig4_three_draft_session.png
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(10, 9))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.set_xlim(-1, 11)
ax.set_ylim(-0.5, 10)
ax.axis("off")

# ── Chain nodes (centered at x=5) ────────────────────────────────────────────
CX = 5.0
NODE_W = 3.4
NODE_H = 0.85

chain = [
    (9.0, "#ced6e0", "Inputs",
     "III_5.4.2_Section6_v3.md\n+ CFP_5.3.1_WorkPlan"),
    (7.5, "#a29bfe", "CFP_5.4.8 v1",
     "~1550 words"),
    (5.8, "#6c5ce7", "CFP_5.4.8 v2",
     "~1600 words   derived_from: v1"),
    (4.1, "#00b894", "CFP_5.4.8 v3",
     "~1520 words   derived_from: v2"),
    (2.4, "#ffeaa7", "CFP_4.2.18 Modlog",
     "13 entries  ·  finalized"),
]

# Right-side annotations (transition reasons)
right_annots = [
    (7.5 - 0.75, "v1:\nVenue reframe · §6.1 virtue dimension\nadverse-selection §6.3 added"),
    (5.8 - 0.75, "v1→v2:\nReviewer A: cut discovery/\njustification paragraph\nReviewer B REVISE · §6.1 reordered\n\"we do not\" paragraphs removed"),
    (4.1 - 0.75, "v2→v3:\n§6.2 rewritten positively\n§6.4 architectural rewrite\n(two-layer structure)"),
    (2.4 - 0.6,  "13 decision entries\nboth reviewers visible per change"),
]

def draw_node(ax, cx, cy, w, h, label, sublabel, fc, ec="#555"):
    rect = mpatches.FancyBboxPatch(
        (cx - w/2, cy - h/2), w, h,
        boxstyle="round,pad=0.3", linewidth=1.3,
        facecolor=fc, edgecolor=ec
    )
    ax.add_patch(rect)
    ax.text(cx, cy + 0.12, label, ha="center", va="center",
            fontsize=9, fontweight="bold", color="#2d3436")
    ax.text(cx, cy - 0.2, sublabel, ha="center", va="center",
            fontsize=7, color="#636e72")

for cy, fc, label, sub in chain:
    draw_node(ax, CX, cy, NODE_W, NODE_H, label, sub, fc)

# Arrows between nodes
arrow_pairs = [(chain[i][0], chain[i+1][0]) for i in range(len(chain)-1)]
for y_from, y_to in arrow_pairs:
    ax.annotate("", xy=(CX, y_to + NODE_H/2), xytext=(CX, y_from - NODE_H/2),
                arrowprops=dict(arrowstyle="-|>,head_width=0.25,head_length=0.18",
                                color="#555", lw=1.5))

# Right annotations
AX_RIGHT = CX + NODE_W/2 + 0.25
for cy, text in right_annots:
    ax.text(AX_RIGHT + 0.1, cy, text, ha="left", va="center",
            fontsize=6.5, color="#555",
            bbox=dict(boxstyle="round,pad=0.3", fc="#f8f9fa", ec="#dee2e6", lw=0.7))
    # Connector line
    ax.plot([AX_RIGHT, AX_RIGHT + 0.05], [cy, cy], color="#ccc", lw=0.7)

# Left session annotation
AX_LEFT = CX - NODE_W/2 - 0.2
ax.text(AX_LEFT - 0.1, 5.8,
        "All three drafts\nin one session:\n\nSID-20260323-190000\nSonnet 4.6\nTwo reviewers:\nA = author\nB = Opus 4.6",
        ha="right", va="center", fontsize=7.5, color="#2d3436",
        bbox=dict(boxstyle="round,pad=0.5", fc="#dfe6e9", ec="#b2bec3", lw=1))
# Bracket
for cy in [7.5, 5.8, 4.1, 2.4]:
    ax.plot([AX_LEFT, AX_LEFT - 0.05], [cy, cy], color="#aaa", lw=0.6)
ax.plot([AX_LEFT]*2, [2.4, 7.5], color="#aaa", lw=1)

# ── Caption ──────────────────────────────────────────────────────────────────
fig.text(0.5, 0.01,
         "Figure 4. The three-draft session (Stage 4). "
         "Inputs → v1 → v2 → v3 → finalized modlog, all within SID-20260323-190000.\n"
         "Side annotations show the reason for each transition. "
         "Verify: CFP_5.4.8 v1–v3, CFP_4.2.18.",
         ha="center", va="bottom", fontsize=6.5, color="#555")

plt.tight_layout(rect=[0, 0.04, 1, 0.98])
out = "transparency/Canonical_MD/_GRAPHS/fig4_three_draft_session.png"
plt.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
print(f"Saved {out}")
