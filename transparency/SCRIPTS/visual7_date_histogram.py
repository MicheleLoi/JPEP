#!/usr/bin/env python3
"""
Visual 7: Date Histogram of Artifact Creation Dates
====================================================
Reads YAML frontmatter from SP4 and SP5 markdown files, extracts dates,
classifies by phase (v1/v2, Stage III, CFP), and plots a weekly histogram.

Output: transparency/Canonical_MD/_GRAPHS/visual7_date_histogram.png
"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# ── Configuration ──────────────────────────────────────────────────────────
BASE = Path(r"C:\Users\loimi\switchdrive\CURRENTLY WORKING ON\AI - assisted papers\JPEP")
SCAN_DIRS = [
    BASE / "transparency" / "Canonical_MD" / "SP4_ProcessDocumentation",
    BASE / "transparency" / "Canonical_MD" / "SP5_DevelopmentRecords",
]
OUTPUT = BASE / "transparency" / "Canonical_MD" / "_GRAPHS" / "visual7_date_histogram.png"

# Phase colours
COLORS = {
    "v1/v2":      "#3B7DD8",   # blue
    "Stage III":   "#888888",   # grey
    "CFP":         "#E87722",   # orange
}

PHASE_ORDER = ["v1/v2", "Stage III", "CFP"]


def extract_frontmatter(filepath: Path) -> dict | None:
    """Return parsed YAML frontmatter dict, or None."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None
    m = re.match(r"^---\s*\n(.*?\n)---", text, re.DOTALL)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None


def classify_phase(filename: str) -> str:
    if filename.startswith("CFP_"):
        return "CFP"
    if filename.startswith("III_") or filename.startswith("II_"):
        return "Stage III"
    return "v1/v2"


def parse_date(fm: dict) -> datetime | None:
    """Try to get a valid date from frontmatter fields."""
    for key in ("reconstructed_date", "date_created", "date"):
        val = fm.get(key)
        if val is None:
            continue
        if isinstance(val, datetime):
            return val
        if hasattr(val, "isoformat"):          # datetime.date
            return datetime(val.year, val.month, val.day)
        if isinstance(val, str):
            for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M", "%d-%m-%Y", "%d %B %Y"):
                try:
                    return datetime.strptime(val.strip(), fmt)
                except ValueError:
                    continue
    return None


def is_plausible(dt: datetime) -> bool:
    """Reject dates clearly outside the project window."""
    return datetime(2025, 9, 1) <= dt <= datetime(2026, 5, 1)


# ── Collect data ───────────────────────────────────────────────────────────
records = []   # list of (date, phase)

for scan_dir in SCAN_DIRS:
    for md in scan_dir.rglob("*.md"):
        fm = extract_frontmatter(md)
        if fm is None:
            continue
        dt = parse_date(fm)
        if dt is None or not is_plausible(dt):
            continue
        phase = classify_phase(md.name)
        records.append((dt, phase))

print(f"Collected {len(records)} dated artifacts")
for ph in PHASE_ORDER:
    n = sum(1 for _, p in records if p == ph)
    print(f"  {ph}: {n}")

# ── Build weekly bins ──────────────────────────────────────────────────────
# Determine range
all_dates = [r[0] for r in records]
min_date = min(all_dates)
max_date = max(all_dates)

# Round down to Monday for bin start
start = min_date - timedelta(days=min_date.weekday())
end = max_date + timedelta(days=(7 - max_date.weekday()) % 7 or 7)

# Create weekly bin edges
bin_edges = []
d = start
while d <= end + timedelta(days=1):
    bin_edges.append(d)
    d += timedelta(days=7)

n_bins = len(bin_edges) - 1

# Count per phase per bin
phase_counts = {ph: np.zeros(n_bins, dtype=int) for ph in PHASE_ORDER}
for dt, phase in records:
    idx = int((dt - start).days // 7)
    idx = min(idx, n_bins - 1)
    phase_counts[phase][idx] += 1

# ── Plot ───────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 4.5))

bar_width = timedelta(days=5.5)    # slightly narrower than a full week
bin_centers = [bin_edges[i] + timedelta(days=3.5) for i in range(n_bins)]

bottoms = np.zeros(n_bins)
for phase in PHASE_ORDER:
    counts = phase_counts[phase]
    ax.bar(bin_centers, counts, width=bar_width, bottom=bottoms,
           color=COLORS[phase], label=phase, edgecolor="white", linewidth=0.4)
    bottoms += counts

# Axes
ax.set_ylabel("Artifacts created", fontsize=11)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
ax.tick_params(axis="x", which="minor", length=2, color="#ccc")

ax.set_xlim(start - timedelta(days=3), end + timedelta(days=3))
ax.set_ylim(0, None)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.legend(frameon=False, fontsize=10, loc="upper left")

fig.tight_layout()
fig.savefig(str(OUTPUT), dpi=300, bbox_inches="tight")
print(f"\nSaved -> {OUTPUT}")
plt.close(fig)
