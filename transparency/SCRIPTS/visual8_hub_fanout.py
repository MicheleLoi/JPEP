"""
Visual 8: Hub Fan-Out Chart
Horizontal bar chart showing artifact count per session hub, colored by phase.
"""

import os
import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

HUB_DIR = r"C:\Users\loimi\switchdrive\CURRENTLY WORKING ON\AI - assisted papers\JPEP\transparency\Canonical_MD\_HUBS"
OUT_PATH = r"C:\Users\loimi\switchdrive\CURRENTLY WORKING ON\AI - assisted papers\JPEP\transparency\Canonical_MD\_GRAPHS\visual8_hub_fanout.png"

# --- Phase classification ---

UUID_RE = re.compile(r'^CHAT_[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\.md$', re.IGNORECASE)
# Also match the continuation hub and the g_g-p-* hubs (v1/v2 era)
CONTINUATION_RE = re.compile(r'^CHAT_\(continuation', re.IGNORECASE)
GPT_HUB_RE = re.compile(r'^CHAT_g_g-p-', re.IGNORECASE)

SID_RE = re.compile(r'CHAT_SID-(\d{8})-\d+\.md$')
# 68-prefix UUIDs are Claude.ai project chats from Stage III era
CLAUDE_PROJECT_RE = re.compile(r'^CHAT_68[0-9a-f]{6}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\.md$', re.IGNORECASE)


def classify_phase(filename):
    """Return phase and short label for a hub file."""
    sid_match = SID_RE.search(filename)
    if sid_match:
        date_str = sid_match.group(1)  # e.g. 20260324
        year_month = int(date_str[:6])
        # Extract time portion for label
        time_match = re.search(r'SID-(\d{8}-\d+)', filename)
        label = time_match.group(1) if time_match else date_str
        if year_month <= 202602:
            return 'Stage III', label
        else:  # Mar-Apr 2026
            return 'CFP', label

    if UUID_RE.match(filename):
        uuid_part = filename.replace('CHAT_', '').replace('.md', '')
        return 'v1/v2', uuid_part[:8]

    if CONTINUATION_RE.match(filename):
        return 'v1/v2', 'cont...'

    if GPT_HUB_RE.match(filename):
        return 'v1/v2', 'gpt-proj'

    if CLAUDE_PROJECT_RE.match(filename):
        # 68xx UUIDs — these are Stage III era Claude project chats
        uuid_part = filename.replace('CHAT_', '').replace('.md', '')
        return 'Stage III', uuid_part[:8]

    # Fallback
    return 'v1/v2', filename[:12]


def count_artifacts(filepath):
    """Count artifacts listed in a hub file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Strategy: count lines that are list items referencing artifacts
    # These are lines starting with "- [[" or "- " followed by artifact references
    count = 0
    in_artifacts_section = False
    for line in content.split('\n'):
        stripped = line.strip()
        # Detect artifacts section headers
        if re.match(r'^##\s*(Artifacts|Artifacts produced)', stripped, re.IGNORECASE):
            in_artifacts_section = True
            continue
        # A new section header ends the artifacts section
        if stripped.startswith('##') and in_artifacts_section:
            in_artifacts_section = False
            continue
        # Count list items in the artifacts section
        if in_artifacts_section and stripped.startswith('- '):
            count += 1

    # If no explicit section found, try counting from YAML artifacts_count
    if count == 0:
        m = re.search(r'artifacts_count:\s*(\d+)', content)
        if m:
            yaml_count = int(m.group(1))
            # But also count "Artifacts produced" items as fallback
            # Actually for YAML-annotated hubs, artifacts are in "## Artifacts produced"
            # Let's recount more broadly
            for line in content.split('\n'):
                stripped = line.strip()
                if stripped.startswith('- ') and ('[[' in stripped or '.md' in stripped
                        or re.search(r'CFP_|III_|V1_|\d\.\d\.\d', stripped)):
                    count += 1
            if count == 0:
                count = yaml_count

    return count


def main():
    sessions = []

    for fname in os.listdir(HUB_DIR):
        if not fname.startswith('CHAT_') or not fname.endswith('.md'):
            continue

        filepath = os.path.join(HUB_DIR, fname)
        phase, label = classify_phase(fname)
        artifact_count = count_artifacts(filepath)

        # Skip hubs with 0 artifacts
        if artifact_count == 0:
            continue

        sessions.append({
            'filename': fname,
            'phase': phase,
            'label': label,
            'count': artifact_count,
        })

    # Sort descending by artifact count, then alphabetically for ties
    sessions.sort(key=lambda s: (-s['count'], s['label']))

    # Colors
    phase_colors = {
        'v1/v2': '#4878CF',       # blue
        'Stage III': '#999999',    # grey
        'CFP': '#E8832A',         # orange
    }

    # Build chart
    labels = [s['label'] for s in sessions]
    counts = [s['count'] for s in sessions]
    colors = [phase_colors[s['phase']] for s in sessions]

    fig, ax = plt.subplots(figsize=(7, max(5, len(sessions) * 0.28)))

    y_pos = range(len(sessions))
    bars = ax.barh(y_pos, counts, color=colors, height=0.7, edgecolor='white',
                   linewidth=0.5)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=7, fontfamily='monospace')
    ax.invert_yaxis()
    ax.set_xlabel('Artifacts per session', fontsize=10)
    ax.set_xlim(0, max(counts) + 1)

    # Integer ticks only
    ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

    # Add count labels on bars
    for i, (bar, count) in enumerate(zip(bars, counts)):
        ax.text(bar.get_width() + 0.15, bar.get_y() + bar.get_height() / 2,
                str(count), va='center', fontsize=7, color='#333333')

    # Legend
    legend_patches = [
        mpatches.Patch(color=phase_colors['v1/v2'], label='v1/v2 (pre-2026)'),
        mpatches.Patch(color=phase_colors['Stage III'], label='Stage III (Jan\u2013Feb 2026)'),
        mpatches.Patch(color=phase_colors['CFP'], label='CFP (Mar\u2013Apr 2026)'),
    ]
    ax.legend(handles=legend_patches, loc='lower right', fontsize=8,
              frameon=True, fancybox=False, edgecolor='#cccccc')

    # Clean up spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(left=False)

    plt.tight_layout()

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    fig.savefig(OUT_PATH, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    print(f"Saved to {OUT_PATH}")
    print(f"Total sessions plotted: {len(sessions)}")
    for s in sessions:
        print(f"  {s['label']:30s}  {s['phase']:12s}  {s['count']} artifacts")


if __name__ == '__main__':
    main()
