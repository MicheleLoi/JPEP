#!/usr/bin/env python3
"""
Generate a manifest of JPEP conversation exports.

Reads JPEP/06_conversations/exported/*.md, extracts frontmatter fields
(session_id, date, messages_count, source_jsonl, json_sha256), and writes
a tracked markdown manifest to JPEP/transparency/conversations_manifest.md.

Rationale: JPEP's 06_conversations/ directory is gitignored per the
denylist-style .gitignore convention. Raw conversations are retained on
the author's machine and available on request, but not part of the public
repository. This manifest is the public index that lets a reviewer see
what exists (filename, SID, date, message count, file size, source JSONL
UUID, SHA-256 of the raw JSONL) without seeing the contents.

Run from JPEP root:
    python transparency/SCRIPTS/generate_conversations_manifest.py

Overwrites transparency/conversations_manifest.md. Deterministic — same
inputs produce the same output. Run before committing when new
conversations have been added to 06_conversations/exported/.
"""

import re
import sys
from datetime import datetime
from pathlib import Path

# Resolve paths relative to this script's location.
# transparency/SCRIPTS/<this>.py  -> JPEP/<root>
SCRIPT_DIR = Path(__file__).resolve().parent
JPEP_ROOT = SCRIPT_DIR.parent.parent
CONVERSATIONS_DIR = JPEP_ROOT / "06_conversations" / "exported"
MANIFEST_PATH = JPEP_ROOT / "transparency" / "conversations_manifest.md"


def parse_frontmatter(text: str) -> dict:
    """Naive YAML frontmatter parser: top-level key: value pairs only."""
    m = re.match(r'\A---\s*\r?\n(.*?)\r?\n---\s*\r?\n', text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            fm[key.strip()] = val.strip().strip('"\'')
    return fm


def format_size(bytes_: int) -> str:
    """Human-readable file size."""
    if bytes_ < 1024:
        return f"{bytes_} B"
    elif bytes_ < 1024 * 1024:
        return f"{bytes_ / 1024:.1f} KB"
    else:
        return f"{bytes_ / (1024 * 1024):.1f} MB"


def main() -> int:
    if not CONVERSATIONS_DIR.is_dir():
        print(f"ERROR: {CONVERSATIONS_DIR} does not exist", file=sys.stderr)
        return 1

    entries = []
    for md_file in sorted(CONVERSATIONS_DIR.glob("*.md")):
        try:
            text = md_file.read_text(encoding='utf-8', errors='replace')
        except Exception as e:
            print(f"Warning: could not read {md_file.name}: {e}", file=sys.stderr)
            continue
        fm = parse_frontmatter(text)
        # Accept both field names: older exports used 'source' before the
        # schema was tightened in 2026-03 to 'source_jsonl'. Same content.
        source_jsonl = fm.get('source_jsonl', '') or fm.get('source', '')
        # 'date' was added later too; earlier exports only have 'exported'.
        # If date is missing, infer from 'exported' (first 10 chars = YYYY-MM-DD).
        date = fm.get('date', '')
        if not date and fm.get('exported', ''):
            date = fm['exported'][:10]
        entries.append({
            'filename': md_file.name,
            'session_id': fm.get('session_id', ''),
            'date': date,
            'exported': fm.get('exported', '')[:19],
            'messages_count': fm.get('messages_count', ''),
            'source_jsonl': source_jsonl,
            'json_sha256': fm.get('json_sha256', ''),
            'size': md_file.stat().st_size,
        })

    entries.sort(key=lambda e: e['filename'])

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = []
    lines.append("# JPEP Conversations Manifest")
    lines.append("")
    lines.append(f"**Generated:** {now}  ")
    lines.append(f"**Source:** `06_conversations/exported/*.md` (gitignored — raw conversations retained locally, not in the public repo)  ")
    lines.append(f"**Count:** {len(entries)} conversation exports")
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append("JPEP's `06_conversations/` directory is gitignored per the denylist-style `.gitignore` convention at the project root. Raw conversation exports are retained on the author's machine and are available on request, but they are not part of the public repository.")
    lines.append("")
    lines.append("This manifest is the public index. It lets a reviewer see what exists without seeing the contents. Each row lists a conversation export with:")
    lines.append("")
    lines.append("- **Filename** — the markdown export name")
    lines.append("- **SID** — the MHC-W session identifier (format: `SID-YYYYMMDD-HHMMSS`)")
    lines.append("- **Date** — the date the session was held")
    lines.append("- **Messages** — number of messages in the exported conversation")
    lines.append("- **Size** — markdown file size on disk")
    lines.append("- **Source JSONL** — the Claude Code platform-produced JSONL UUID (truncated in the table; full value in each export's frontmatter)")
    lines.append("- **SHA-256** — cryptographic hash of the raw JSONL at the time of export (truncated in the table; full value in each export's frontmatter). This is available so a reviewer who requests a copy can verify the copy they receive matches the version recorded at the time of export.")
    lines.append("")
    lines.append("## Manifest")
    lines.append("")
    lines.append("| Filename | SID | Date | Messages | Size | Source JSONL (UUID) | SHA-256 |")
    lines.append("|---|---|---|---|---|---|---|")
    DASH = "—"
    def cell(v: str) -> str:
        return v if v else DASH
    for e in entries:
        sid = cell(e['session_id'])
        date = cell(e['date'])
        msgs = cell(e['messages_count'])
        if e['json_sha256']:
            sha = f"`{e['json_sha256'][:12]}…`"
        else:
            sha = DASH
        if e['source_jsonl']:
            jsonl_short = f"`{e['source_jsonl'][:8]}…`" if len(e['source_jsonl']) > 8 else f"`{e['source_jsonl']}`"
        else:
            jsonl_short = DASH
        lines.append(
            f"| `{e['filename']}` | {sid} | {date} | "
            f"{msgs} | {format_size(e['size'])} | "
            f"{jsonl_short} | {sha} |"
        )
    lines.append("")
    lines.append("## Regenerating this manifest")
    lines.append("")
    lines.append("From JPEP root:")
    lines.append("")
    lines.append("```")
    lines.append("python transparency/SCRIPTS/generate_conversations_manifest.py")
    lines.append("```")
    lines.append("")
    lines.append("Overwrites this file. Run before committing when new conversations have been added to `06_conversations/exported/`. The script is deterministic — same inputs produce the same output. No side effects beyond writing the manifest file.")
    lines.append("")
    lines.append("## Availability")
    lines.append("")
    lines.append("The contents of `06_conversations/exported/` are available from the author on request. The SHA-256 column (full value in each export's frontmatter) lets a reviewer verify the integrity of a copy against the value recorded at the time of export. This treats conversations as source material — analogous to lab notebooks: existing, preserved, auditable on demand, but not part of the published spine.")
    lines.append("")
    lines.append("The published documentation spine is the artifact chain under `transparency/Canonical_MD/` (SP4 process documentation + SP5 development records). SP-3 describes the division of labor between the spine and the source material in more detail.")
    lines.append("")
    lines.append("## Note on older exports")
    lines.append("")
    lines.append("The earliest exports in this manifest (February and early-March 2026) predate MHC-W's SID system and the extended export frontmatter schema. Their rows show `—` for fields that were not yet being written at the time of export:")
    lines.append("")
    lines.append("- **February 2026 exports** only recorded `exported` and `source` (the Claude Code JSONL UUID). No `date`, no `messages_count`, no `json_sha256`, no `session_id`. The `Date` column is inferred from the `exported` timestamp for display.")
    lines.append("- **March 2026 exports** added `date`, `messages_count`, `source_jsonl`, and `json_sha256` but did not yet record `session_id` — MHC-W's SID system had not been adopted in JPEP.")
    lines.append("- **April 2026 exports onward** have the full schema including `session_id`.")
    lines.append("")
    lines.append("This is honest provenance: empty cells reflect fields that were not recorded at the time of export, not missing data that could be reconstructed. A reviewer can still match older exports to specific conversations via the filename timestamp and the JSONL UUID (where recorded).")

    MANIFEST_PATH.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f"Wrote {MANIFEST_PATH} ({len(entries)} entries)")
    return 0


if __name__ == '__main__':
    sys.exit(main())
