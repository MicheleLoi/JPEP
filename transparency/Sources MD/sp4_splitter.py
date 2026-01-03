#!/usr/bin/env python3
"""
SP4 splitter (mechanical + deterministic)

Input:  one consolidated SP-4 markdown file
Output: one .md per SP-4 record heading, plus _PREAMBLE.md, _INDEX.md, _MISSING_OR_EXTRA.md

Split trigger (record header):
  Markdown heading line containing: <record_id> <label>
  e.g. "## 4.2.11 ModificationLog_Appendix"
  e.g. "### 4.4.6.i SectionGuidance_Section_VIII-B"

Naming:
  <record_id>_<sanitized_label><suffix>.md
Suffix is appended only for record_ids listed in SUFFIX_BY_ID (append strategy __SXX / __SXX-YY).

Run (from folder containing the input file):
  python sp4_splitter.py "SP-4_process Documentation.md" "SP4_SPLIT_OUT"
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


print("=== SP4_SPLITTER running ===")

# Accept any heading level #..######, but still purely mechanical.
# Captures:
#   group(2) record_id: 4.2.11 , 4.4.6.i , 4.7.7.4 , etc.
#   group(3) label: rest of the header line
RE_RECORD = re.compile(
    r"^(#{1,6})\s+"
    r"(4\.\d+(?:\.\d+)?(?:\.(?:\d+|[a-z]+))*)\s+"
    r"(.+?)\s*$",
    re.IGNORECASE,
)

# SP-4 seven parts -> output subfolders (matches your plan)
PART_FOLDER = {
    "4.1": "4.1_CompletePrompt",
    "4.2": "4.2_ModificationLogs",
    "4.3": "4.3_PatternSummaries",
    "4.4": "4.4_SectionGuidance",
    "4.5": "4.5_SectionSummaries",
    "4.6": "4.6_ReferenceLogs",
    "4.7": "4.7_EpistemicTraces",
}

# Append strategy suffix mapping (fixed; not inferred)
SUFFIX_BY_ID = {
    # 4.2 Modification logs
    "4.2.1": "__S01",
    "4.2.2": "__S02",
    "4.2.3": "__S02",
    "4.2.4": "__S02",
    "4.2.5": "__S02",
    "4.2.6": "__S03",
    "4.2.7": "__S04",
    "4.2.8": "__S05",
    "4.2.9": "__S06",
    "4.2.10": "__S07",
    # 4.2.11 Appendix, 4.2.12 Title/Abstract -> no suffix

    # 4.3 Pattern summaries
    "4.3.1": "__S02",
    "4.3.2": "__S02",
    "4.3.3": "__S02",
    "4.3.4": "__S03",
    "4.3.5": "__S06",

    # 4.4 Section guidance
    # 4.4.1 no suffix
    "4.4.2": "__S02",
    "4.4.3": "__S03-04",
    "4.4.4": "__S06",
    "4.4.5": "__S05",
    "4.4.6": "__S06-07",
    "4.4.6.i": "__S06",
    "4.4.6.ii": "__S06-07",
    "4.4.7": "__S07",
    "4.4.8": "__S01-02",
    "4.4.9": "__S06",
    "4.4.10": "__S02",
    # 4.4.11 no suffix
    # 4.4.12 no suffix
    "4.4.13": "__S06",

    # 4.5 Section summaries
    "4.5.1": "__S01",
    "4.5.2": "__S02",
    "4.5.3": "__S02",
    "4.5.4": "__S02",
    "4.5.5": "__S03",
    "4.5.6": "__S04",
    "4.5.7": "__S06",
    "4.5.8": "__S07",
    # 4.6, 4.7 -> no suffix
}

# Expected record IDs list for checking (split still works even if different; this is only a report)
EXPECTED_IDS = [
    "4.1",
    "4.2.1","4.2.2","4.2.3","4.2.4","4.2.5","4.2.6","4.2.7","4.2.8","4.2.9","4.2.10","4.2.11","4.2.12",
    "4.3.1","4.3.2","4.3.3","4.3.4","4.3.5",
    "4.4.1","4.4.2","4.4.3","4.4.4","4.4.5","4.4.6","4.4.6.i","4.4.6.ii","4.4.7","4.4.8","4.4.9","4.4.10","4.4.11","4.4.12","4.4.13",
    "4.5.1","4.5.2","4.5.3","4.5.4","4.5.5","4.5.6","4.5.7","4.5.8",
    "4.6.1","4.6.2",
    "4.7.1","4.7.2","4.7.3","4.7.4","4.7.5",
    "4.7.6","4.7.6.1","4.7.6.2","4.7.6.3",
    "4.7.7","4.7.7.1","4.7.7.2","4.7.7.3","4.7.7.4",
]


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def sanitize_label(s: str) -> str:
    """
    Deterministic filename-safe label:
    - spaces and slashes -> underscore
    - keep only A-Za-z0-9 . _ -
    - collapse multiple underscores
    """
    s = s.strip().replace(" ", "_").replace("/", "_").replace("\\", "_")
    s = re.sub(r"[^A-Za-z0-9._-]+", "", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "Record"


def part_key_from_record_id(record_id: str) -> str:
    bits = record_id.split(".")
    return f"{bits[0]}.{bits[1]}" if len(bits) >= 2 else record_id


def main() -> int:
    in_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("SP-4_process Documentation.md")
    out_root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("SP4_SPLIT_OUT")

    if not in_path.exists():
        print(f"ERROR: input file not found: {in_path}", file=sys.stderr)
        return 2

    text = normalize_newlines(in_path.read_text(encoding="utf-8", errors="strict"))
    lines = text.split("\n")

    headers: list[tuple[int, str, str]] = []
    for i, line in enumerate(lines):
        m = RE_RECORD.match(line)
        if m:
            headers.append((i, m.group(2), m.group(3).strip()))

    if not headers:
        print("ERROR: no SP-4 record headers found.", file=sys.stderr)
        print("Expected a line like: ## 4.2.11 ModificationLog_Appendix", file=sys.stderr)
        return 3

    out_root.mkdir(parents=True, exist_ok=True)

    # Create part folders
    for folder in PART_FOLDER.values():
        (out_root / folder).mkdir(parents=True, exist_ok=True)

    # Write preamble (everything before first record header)
    first_i = headers[0][0]
    preamble = "\n".join(lines[:first_i]).rstrip() + "\n"
    (out_root / "_PREAMBLE.md").write_text(preamble, encoding="utf-8", errors="strict")

    index_rows: list[str] = []
    found_ids: list[str] = []

    # Slice each record chunk
    for k, (start_i, record_id, label) in enumerate(headers):
        end_i = headers[k + 1][0] if k + 1 < len(headers) else len(lines)
        chunk = "\n".join(lines[start_i:end_i]).rstrip() + "\n"

        pk = part_key_from_record_id(record_id)
        part_folder = PART_FOLDER.get(pk, "UNKNOWN_PART")
        (out_root / part_folder).mkdir(parents=True, exist_ok=True)

        suffix = SUFFIX_BY_ID.get(record_id, "")
        safe_label = sanitize_label(label)
        filename = f"{record_id}_{safe_label}{suffix}.md"

        out_path = out_root / part_folder / filename
        out_path.write_text(chunk, encoding="utf-8", errors="strict")

        found_ids.append(record_id)
        index_rows.append(f"{record_id} | {label} | {part_folder}\\{filename}")

    # Index
    (out_root / "_INDEX.md").write_text(
        "# SP-4 split index\n\n"
        "record_id | heading_label | output_path\n"
        "---|---|---\n"
        + "\n".join(index_rows)
        + "\n",
        encoding="utf-8",
        errors="strict",
    )

    # Missing/extra report
    expected_set = set(EXPECTED_IDS)
    found_set = set(found_ids)

    missing = [rid for rid in EXPECTED_IDS if rid not in found_set]
    extra = sorted([rid for rid in found_set if rid not in expected_set])

    report = []
    report.append("# SP-4 expected record check\n")
    report.append("## Missing\n")
    report.extend([f"- {rid}" for rid in missing] if missing else ["- none"])
    report.append("\n## Extra\n")
    report.extend([f"- {rid}" for rid in extra] if extra else ["- none"])
    report.append("")

    (out_root / "_MISSING_OR_EXTRA.md").write_text(
        "\n".join(report),
        encoding="utf-8",
        errors="strict",
    )

    print(f"OK: wrote split files to: {out_root}")
    print(f"Index: {out_root / '_INDEX.md'}")
    print(f"Preamble: {out_root / '_PREAMBLE.md'}")
    print(f"Check: {out_root / '_MISSING_OR_EXTRA.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
