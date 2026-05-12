"""
Figure 6 — Where Section 6 sits in the project.
H5 implementation: three phase-colored bands per section, width = temporal span
of that phase's activity on that section. No quantification.
Modlog-coverage count lives in caption prose only.
Output: transparency/Canonical_MD/_GRAPHS/fig6_swimlanes.png
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.dates as mdates
from datetime import date, timedelta

d = lambda y, m, day: date(y, m, day)

# Minimum band width for single-event phases (so they stay legible)
MIN_DAYS = 8

def span(start, end=None):
    """Return (start, end) — if end is None, use start + MIN_DAYS."""
    if end is None:
        return start, start + timedelta(days=MIN_DAYS)
    # Ensure at least MIN_DAYS wide
    if (end - start).days < MIN_DAYS:
        end = start + timedelta(days=MIN_DAYS)
    return start, end

# ── Phase spans per section ───────────────────────────────────────────────────
# (section_num, short_label, { phase: (start, end) })
# Phases: "v12", "s3", "cfp"

sections = [
    (1, "Sect. 1\nIntroduction", {
        "v12": span(d(2025,10,12)),
        "cfp": span(d(2026,3,3), d(2026,3,12)),   # modlog: started 03-03, last 03-12
    }),
    (2, "Sect. 2\nSystemic Barriers", {
        "v12": span(d(2025,10,12)),
        "cfp": span(d(2026,3,12), d(2026,4,1)),   # v1 03-12 → v4 04-01
    }),
    (3, "Sect. 3\nWhy Engage", {
        "v12": span(d(2025,10,14)),
        "s3":  span(d(2026,1,28)),                 # III_5.4.1 date 01-28; III_4.2.12 complete
        "cfp": span(d(2026,3,5), d(2026,4,3)),     # modlog 03-05→03-12; v3 draft 04-03
    }),
    (4, "Sect. 4\nCognitivist Obj.", {
        "v12": span(d(2025,10,15)),
        # No Stage III, no CFP draft completed (work plan checklist unchecked)
    }),
    (5, "Sect. 5\nConditions", {
        "v12": span(d(2025,10,14)),
        "cfp": span(d(2026,3,17), d(2026,4,1)),   # modlog 03-17; v2 04-01
    }),
    (6, "Sect. 6\nMandatory\nTransparency", {
        "v12": span(d(2025,10,15), d(2025,11,6)),  # S1 first writing → S2 feedback loop
        "s3":  span(d(2026,1,26), d(2026,3,2)),    # III modlog: started 01-28, last 03-02
        "cfp": span(d(2026,3,23), d(2026,4,1)),    # three-draft session → redundancy pass
    }),
    (7, "Sect. 7\nCommunity\nAssessment", {
        "v12": span(d(2025,10,18)),
        "cfp": span(d(2026,3,24), d(2026,4,1)),   # modlog 03-24; v3 04-01
    }),
]

# ── Colors ────────────────────────────────────────────────────────────────────
PHASE_COLORS = {
    "v12": "#9b8fce",   # muted purple
    "s3":  "#f0a500",   # amber
    "cfp": "#2ecc71",   # green
}
PHASE_LABELS = {
    "v12": "v1/v2  (Claude.ai web · Sonnet 4.5)",
    "s3":  "Stage III  (Claude Code · Opus 4.5 / Sonnet 4.6)",
    "cfp": "CFP phase  (Claude Code · Sonnet 4.6 / Opus 4.6)",
}

S6_IDX = 5   # 0-indexed position of Section 6

# ── Figure setup ──────────────────────────────────────────────────────────────
N = len(sections)
LANE_H   = 0.42    # height of each phase band
LANE_GAP = 1.2     # vertical spacing between section rows
Y_OFFSET = 0.15    # vertical offset between stacked phase bands within a row

fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor("white")
ax.set_facecolor("#fafafa")

xmin = d(2025, 9, 20)
xmax = d(2026, 4, 22)

def xn(dt): return mdates.date2num(dt)

ax.set_xlim(xn(xmin), xn(xmax))
ax.set_ylim(-0.8, N * LANE_GAP + 0.4)

phase_order = ["v12", "s3", "cfp"]

for row, (sec_num, label, phases_dict) in enumerate(sections):
    y_base = row * LANE_GAP
    is_s6  = (row == S6_IDX)

    # Row background
    bg_alpha = 0.12 if is_s6 else 0.04
    bg_color = "#2ecc71" if is_s6 else "#dfe6e9"
    ax.barh(y_base, xn(xmax) - xn(xmin), left=xn(xmin),
            height=LANE_H * 3 + Y_OFFSET * 2 + 0.15,
            color=bg_color, alpha=bg_alpha, zorder=0,
            align="edge")

    # Phase bands — stacked vertically within the row
    for p_idx, phase in enumerate(phase_order):
        if phase not in phases_dict:
            continue
        start, end = phases_dict[phase]
        y_band = y_base + p_idx * (LANE_H + Y_OFFSET)

        alpha = 0.92 if is_s6 else 0.42
        lw    = 1.0  if is_s6 else 0.4

        rect = mpatches.FancyBboxPatch(
            (xn(start), y_band), xn(end) - xn(start), LANE_H,
            boxstyle="round,pad=0.5",
            facecolor=PHASE_COLORS[phase], edgecolor="white",
            linewidth=lw, alpha=alpha, zorder=2
        )
        ax.add_patch(rect)

    # Section label (left margin)
    ax.text(xn(xmin) - 0.5, y_base + LANE_H,
            label,
            ha="right", va="center",
            fontsize=7.5 if is_s6 else 6.8,
            fontweight="bold" if is_s6 else "normal",
            color="#1a1a2e" if is_s6 else "#555")

    # Section 6 annotation
    if is_s6:
        ax.text(xn(d(2026,2,10)), y_base + LANE_H * 3 + Y_OFFSET * 2 + 0.25,
                "▲  Section 6 — highlighted worked example",
                ha="center", va="bottom",
                fontsize=7, color="#1a7a4a", fontstyle="italic")

# ── X-axis ────────────────────────────────────────────────────────────────────
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.tick_params(axis="x", labelsize=7.5, length=3, pad=4)
ax.yaxis.set_visible(False)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.xaxis.set_ticks_position("bottom")
ax.spines["bottom"].set_visible(True)
ax.spines["bottom"].set_color("#ccc")

# ── Phase legend ──────────────────────────────────────────────────────────────
legend_handles = [
    mpatches.Patch(color=PHASE_COLORS[p], label=PHASE_LABELS[p], alpha=0.85)
    for p in phase_order
]
ax.legend(handles=legend_handles, loc="upper left", fontsize=7,
          frameon=True, framealpha=0.95, edgecolor="#ddd")

# ── Caption ──────────────────────────────────────────────────────────────────
fig.text(
    0.5, 0.01,
    "Figure 6. Where Section 6 sits in the project. "
    "Each band shows the temporal span of one phase's documented activity on that section; "
    "width encodes duration, not depth.\n"
    "All seven paper sections have modlog coverage in both the v1/v2 and CFP phases. "
    "Section 6 was chosen as the worked example because it exercises all three "
    "Section 7 adequacy criteria simultaneously;\nthe other sections are not abandoned "
    "— their histories exist and the Section 6 patterns recur across them. "
    "Verify: CFP_4.2.14–4.2.20, CFP_5.4.* draft dates, CFP_4.7.20.",
    ha="center", va="bottom", fontsize=6.5, color="#444"
)

plt.tight_layout(rect=[0, 0.09, 1, 0.98])
out = "transparency/Canonical_MD/_GRAPHS/fig6_swimlanes.svg"
plt.savefig(out, bbox_inches="tight", facecolor="white")
print(f"Saved {out}")
