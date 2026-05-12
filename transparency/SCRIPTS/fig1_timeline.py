"""
Figure 1 — The JPEP writing project on one timeline.
Three phase bands, two platforms, four model identities, major events.
Output: transparency/Canonical_MD/_GRAPHS/fig1_timeline.png
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import matplotlib.dates as mdates
from datetime import date
import numpy as np

# ── Dates ──────────────────────────────────────────────────────────────────
d = lambda y, m, day: date(y, m, day)

# Phase bands
phases = [
    ("v1/v2", d(2025,10,15), d(2025,12,31), "#d4e6f7"),
    ("Stage III", d(2026,1,26), d(2026,3,2),  "#fde8cc"),
    ("CFP",  d(2026,3,2),  d(2026,4,8),  "#d5f0d5"),
]

# Platform spans
platforms = [
    ("Claude.ai web", d(2025,10,15), d(2025,11,6),  "#7fb3d3"),
    ("Claude Code",   d(2026,1,26),  d(2026,4,8),   "#5dade2"),
]

# Model spans (approximate continuity)
models = [
    ("Sonnet 4.5", d(2025,10,15), d(2025,11,6),  "#a29bfe"),
    ("Opus 4.5",   d(2026,1,26),  d(2026,3,1),   "#6c5ce7"),
    ("Sonnet 4.6", d(2026,3,2),   d(2026,3,31),  "#00b894"),
    ("Opus 4.6",   d(2026,3,31),  d(2026,4,8),   "#00cec9"),
]

# Stage markers
stages = [
    (1, d(2025,10,15), "Stage 1\nFirst writing\nas Section VIII"),
    (2, d(2025,11,5),  "Stage 2\nAppendix →\n§6.2 feedback loop"),
    (3, d(2026,1,26),  "Stage 3\nMHC integration\n(Jan–Mar 2026)"),
    (4, d(2026,3,23),  "Stage 4\nThree-draft\nsession"),
    (5, d(2026,4,1),   "Stage 5\nRedundancy\npass"),
]

# Event markers
events = [
    (d(2025,11,5),  "Section VIII →\nSection 6", False),
    (d(2026,3,2),   "SP reconception", False),
    (d(2026,4,2),   "Appendix\nelimination", False),
    (d(2026,4,1),   "Redundancy\ncompression", False),
]

# ── Layout ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 6))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

xmin = d(2025,9,15)
xmax = d(2026,4,20)
ax.set_xlim(xmin, xmax)
ax.set_ylim(0, 10)
ax.axis("off")

def x(dt):
    return mdates.date2num(dt)

# ── Phase bands ─────────────────────────────────────────────────────────────
for label, start, end, color in phases:
    ax.axvspan(x(start), x(end), ymin=0, ymax=1, alpha=0.25, color=color, zorder=0)
    mid = x(start) + (x(end) - x(start)) / 2
    ax.text(mid, 9.5, label, ha="center", va="top", fontsize=9, color="#555",
            fontstyle="italic")

# ── Track rows ──────────────────────────────────────────────────────────────
ROW_PLATFORM = 7.5
ROW_MODEL    = 5.5
ROW_STAGE    = 3.2
BAR_H        = 0.7

# Row labels
for y_pos, label in [(ROW_PLATFORM, "Platform"), (ROW_MODEL, "Model"), (ROW_STAGE, "Stage")]:
    ax.text(x(xmin) + 1, y_pos + BAR_H/2, label, ha="left", va="center",
            fontsize=8, color="#333", fontweight="bold")

# Platform bars
for label, start, end, color in platforms:
    rect = mpatches.FancyBboxPatch(
        (x(start), ROW_PLATFORM), x(end) - x(start), BAR_H,
        boxstyle="round,pad=0.3", linewidth=0, facecolor=color, alpha=0.85
    )
    ax.add_patch(rect)
    mid = x(start) + (x(end) - x(start)) / 2
    ax.text(mid, ROW_PLATFORM + BAR_H/2, label, ha="center", va="center",
            fontsize=7.5, color="white", fontweight="bold")

# Model bars
for label, start, end, color in models:
    rect = mpatches.FancyBboxPatch(
        (x(start), ROW_MODEL), x(end) - x(start), BAR_H,
        boxstyle="round,pad=0.3", linewidth=0, facecolor=color, alpha=0.85
    )
    ax.add_patch(rect)
    mid = x(start) + (x(end) - x(start)) / 2
    ax.text(mid, ROW_MODEL + BAR_H/2, label, ha="center", va="center",
            fontsize=7, color="white", fontweight="bold")

# Stage markers (diamonds on a line)
ax.axhline(y=ROW_STAGE + BAR_H/2, xmin=0.05, xmax=0.95, color="#aaa",
           linewidth=1, zorder=1)
for num, dt, label in stages:
    cx = x(dt)
    cy = ROW_STAGE + BAR_H/2
    ax.plot(cx, cy, marker="D", markersize=10, color="#e17055", zorder=3)
    ax.text(cx, cy - 0.6, f"S{num}", ha="center", va="top",
            fontsize=7.5, color="#e17055", fontweight="bold")
    # Stagger labels above/below
    y_label = cy + 1.0 if num % 2 == 1 else cy - 2.2
    ax.annotate(label, xy=(cx, cy),
                xytext=(cx, y_label),
                ha="center", va="center", fontsize=6.5, color="#555",
                arrowprops=dict(arrowstyle="-", color="#ccc", lw=0.8))

# ── Event markers ───────────────────────────────────────────────────────────
EVENT_Y = 1.2
for dt, label, is_ghost in events:
    cx = x(dt)
    if is_ghost:
        ax.axvline(x=cx, color="#b2bec3", linewidth=1, linestyle="--",
                   ymin=0.05, ymax=0.85, zorder=2)
        ax.plot(cx, EVENT_Y, marker="o", markersize=7, markerfacecolor="white",
                markeredgecolor="#636e72", markeredgewidth=1.5, zorder=3)
        ax.text(cx, EVENT_Y - 0.45, label, ha="center", va="top",
                fontsize=6, color="#b2bec3")
    else:
        ax.axvline(x=cx, color="#636e72", linewidth=0.8, linestyle=":",
                   ymin=0.05, ymax=0.85, zorder=2)
        ax.text(cx, EVENT_Y, label, ha="center", va="top",
                fontsize=6.5, color="#555",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#ddd", lw=0.5))

# ── X-axis date ticks ────────────────────────────────────────────────────────
ax_x = ax.twiny()
ax_x.set_xlim(xmin, xmax)
ax_x.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
ax_x.xaxis.set_major_locator(mdates.MonthLocator())
ax_x.tick_params(labelsize=7, length=3)
ax_x.set_position([0.05, 0, 0.9, 1])
for spine in ax_x.spines.values():
    spine.set_visible(False)
ax_x.xaxis.set_ticks_position("bottom")

# ── Caption ──────────────────────────────────────────────────────────────────
fig.text(0.5, 0.01,
         "Figure 1. The JPEP writing project on one timeline. "
         "Five stages across three phases, two platforms, four model identities, and major structural events.\n"
         "Verify: CFP_4.7.20, CFP_5.3.19.",
         ha="center", va="bottom", fontsize=6.5, color="#555",
         wrap=True)

plt.tight_layout(rect=[0, 0.05, 1, 0.97])
out = "transparency/Canonical_MD/_GRAPHS/fig1_timeline.svg"
plt.savefig(out, bbox_inches="tight", facecolor="white")
print(f"Saved {out}")
