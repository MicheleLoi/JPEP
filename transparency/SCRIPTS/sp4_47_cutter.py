#!/usr/bin/env python3
"""
sp4_47_cutter.py

Cuts ONLY Part 7 (SP4.7.x Epistemic Traces) out of the consolidated
"SP-4_process Documentation.md" and writes the pieces into:

  <OUT_ROOT>/4.7_EpistemicTraces/

Robust to one known conversion issue:
- In the DOCX, the 4.7.4 heading can appear as just "Preliminary Chat"
  (missing the "4.7.4" prefix). In markdown this is typically:
      ## Preliminary Chat
  The script maps that heading to 4.7.4 and patches the output heading.

Usage (Windows):
  python sp4_47_cutter.py "SP-4_process Documentation.md" "Canonical MD\\SP4_ProcessDocumentation"

Outputs:
  4.7_EpistemicTraces\\<the 14 planned files>
  4.7_EpistemicTraces\\_INDEX_4.7.md
  4.7_EpistemicTraces\\_DIAGNOSTIC_4.7.md
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# Planned outputs (from your folder scheme)
ID_TO_FILENAME: Dict[str, str] = {
    "4.7.1": "4.7.1_OriginalTextConversationExtract_Redacted.md",
    "4.7.2": "4.7.2_OriginalTextConversation_VisibilityAndStakeholders.md",
    "4.7.3": "4.7.3_PreliminaryChat.md",
    "4.7.4": "4.7.4_PreliminaryChat.md",
    "4.7.5": "4.7.5_PreliminaryChat.md",
    "4.7.6": "4.7.6_EpistemicTrace_Discovery_EpistemicTrace_vs_PDL_Distinction.md",
    "4.7.6.1": "4.7.6.1_Note_ArtifactOntologyExpansion_Type2b.md",
    "4.7.6.2": "4.7.6.2_EpistemicTrace_IntroducesType8DistinctionAndSectionPDLs.md",
    "4.7.6.3": "4.7.6.3_EpistemicTrace_Testing_CanonicalTypeDescriptionProduction.md",
    "4.7.7": "4.7.7_ChatGPT_EvaluationsOfFullPaper.md",
    "4.7.7.1": "4.7.7.1_IsThisAISlop_1.md",
    "4.7.7.2": "4.7.7.2_IsThisAISlop_2.md",
    "4.7.7.3": "4.7.7.3_IsThisAISlop_3.md",
    "4.7.7.4": "4.7.7.4_InfrastructureLimitationsAndTransparencyFramework.md",
}

# Parent records that also have child files (so parent file should stop before children)
PARENT_IDS_WITH_CHILD_FILES = {"4.7.6", "4.7.7"}


@dataclass
class Heading:
    level: int
    line_idx: int  # index within the FULL file (0-based)
    text: str
    id: Optional[str]  # extracted 4.7.* id, if any


HEADING_RE = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<title>.*)\s*$")
ID_RE = re.compile(r"\b(4\.7(?:\.\d+){1,3})\b")  # 4.7.1 ... 4.7.7.4
BOLD_STRIP_RE = re.compile(r"[*_`]+")            # strips bold/italic/code marks


def normalize_heading_title(title: str) -> str:
    t = BOLD_STRIP_RE.sub("", title).strip()
    t = t.replace("\u00a0", " ").strip()
    return t


def extract_id_from_heading(title: str) -> Optional[str]:
    raw = normalize_heading_title(title)
    m = ID_RE.search(raw)
    return m.group(1) if m else None


def find_part7_bounds(lines: List[str]) -> Tuple[int, int]:
    """
    Returns (start_idx, end_idx) inclusive-exclusive bounds for Part 7.
    Start: line with '# Part 7 ...'
    End: next '# Part X ...' for X!=7, or EOF
    """
    start = None
    part7_re = re.compile(r"^#\s+Part\s+7\b", re.IGNORECASE)
    any_part_re = re.compile(r"^#\s+Part\s+(\d+)\b", re.IGNORECASE)

    for i, line in enumerate(lines):
        if part7_re.search(line):
            start = i
            break
    if start is None:
        raise SystemExit("ERROR: Could not find '# Part 7' header in the input file.")

    end = len(lines)
    for j in range(start + 1, len(lines)):
        m = any_part_re.search(lines[j])
        if m and m.group(1) != "7":
            end = j
            break

    return start, end


def collect_headings(lines: List[str], start: int, end: int) -> List[Heading]:
    hs: List[Heading] = []
    for i in range(start, end):
        m = HEADING_RE.match(lines[i])
        if not m:
            continue
        level = len(m.group("hashes"))
        title = m.group("title")
        hid = extract_id_from_heading(title)
        hs.append(Heading(level=level, line_idx=i, text=title, id=hid))
    return hs


def infer_missing_474(headings: List[Heading]) -> None:
    """
    Map a level-2 heading titled exactly 'Preliminary Chat' (no id),
    between 4.7.3 and 4.7.5, to id '4.7.4'.
    """
    h47_3 = next((h for h in headings if h.level == 2 and h.id == "4.7.3"), None)
    h47_5 = next((h for h in headings if h.level == 2 and h.id == "4.7.5"), None)
    if not (h47_3 and h47_5):
        return

    for h in headings:
        if h.level != 2 or h.id is not None:
            continue
        t = normalize_heading_title(h.text)
        if t.lower() == "preliminary chat" and h47_3.line_idx < h.line_idx < h47_5.line_idx:
            h.id = "4.7.4"
            return


def slice_block(lines: List[str], start: int, end: int) -> List[str]:
    block = lines[start:end]
    # trim outer blank lines
    while block and block[0].strip() == "":
        block = block[1:]
    while block and block[-1].strip() == "":
        block = block[:-1]
    return block


def compute_ranges(lines: List[str], part7_start: int, part7_end: int) -> Tuple[Dict[str, Tuple[int, int]], List[str]]:
    diagnostics: List[str] = []
    headings = collect_headings(lines, part7_start, part7_end)
    infer_missing_474(headings)

    # first occurrence per id
    by_id: Dict[str, Heading] = {}
    for h in headings:
        if h.id and h.id.startswith("4.7"):
            by_id.setdefault(h.id, h)

    missing = [k for k in ID_TO_FILENAME.keys() if k not in by_id]
    if missing:
        diagnostics.append("Missing expected headings (by id): " + ", ".join(missing))

    def next_heading_after(line_idx: int, pred) -> Optional[int]:
        for h in headings:
            if h.line_idx > line_idx and pred(h):
                return h.line_idx
        return None

    ranges: Dict[str, Tuple[int, int]] = {}

    # Level-2 records
    level2_ids = ["4.7.1", "4.7.2", "4.7.3", "4.7.4", "4.7.5", "4.7.6", "4.7.7"]
    for rid in level2_ids:
        h = by_id.get(rid)
        if not h:
            continue
        start = h.line_idx

        # sibling end: next level-2 heading inside Part 7, else part7_end
        def is_part7_level2(x: Heading) -> bool:
            if x.level != 2:
                return False
            if x.id and x.id.startswith("4.7"):
                return True
            # also treat plain "Preliminary Chat" as a level-2 boundary marker
            return normalize_heading_title(x.text).lower() == "preliminary chat"

        sib_end = next_heading_after(start, is_part7_level2)
        if sib_end is None:
            sib_end = part7_end

        if rid in PARENT_IDS_WITH_CHILD_FILES:
            # for parent file, stop before first child
            child_prefix = rid + "."
            child_start = next_heading_after(start, lambda x: x.level == 3 and x.id and x.id.startswith(child_prefix))
            end = child_start if (child_start is not None and child_start < sib_end) else sib_end
        else:
            end = sib_end

        ranges[rid] = (start, end)

    # Level-3 child records
    child_ids = ["4.7.6.1", "4.7.6.2", "4.7.6.3", "4.7.7.1", "4.7.7.2", "4.7.7.3", "4.7.7.4"]
    for rid in child_ids:
        h = by_id.get(rid)
        if not h:
            continue
        start = h.line_idx
        parent = rid.rsplit(".", 1)[0]

        sib3 = next_heading_after(start, lambda x: x.level == 3 and x.id and x.id.startswith(parent + "."))
        sib2 = next_heading_after(start, lambda x: x.level == 2 and x.id and x.id.startswith("4.7"))
        candidates = [c for c in [sib3, sib2, part7_end] if c is not None]
        end = min(candidates)
        ranges[rid] = (start, end)

    for rid in sorted(ranges.keys(), key=lambda s: [int(p) for p in s.split(".") if p.isdigit()]):
        s, e = ranges[rid]
        diagnostics.append(f"{rid}: lines {s+1}-{e} (len={e-s})")

    return ranges, diagnostics


def patch_heading_for_474(block: List[str]) -> List[str]:
    """
    If the block starts with '## Preliminary Chat' (no id), rewrite to:
      ## **4.7.4 Preliminary Chat**
    """
    if not block:
        return block
    # find first non-empty line (should be the heading)
    for i, line in enumerate(block):
        if line.strip() == "":
            continue
        if line.strip() == "## Preliminary Chat":
            block[i] = "## **4.7.4 Preliminary Chat**"
        return block
    return block


def write_outputs(lines: List[str], out_dir: Path, ranges: Dict[str, Tuple[int, int]], diagnostics: List[str]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    index_rows: List[Tuple[str, int, str]] = []

    for rid, fname in ID_TO_FILENAME.items():
        if rid not in ranges:
            continue
        start, end = ranges[rid]
        block = slice_block(lines, start, end)

        if rid == "4.7.4":
            block = patch_heading_for_474(block)

        content = "\n".join(block).rstrip() + "\n"
        (out_dir / fname).write_text(content, encoding="utf-8")

        heading_line = lines[start].strip()
        index_rows.append((fname, start + 1, heading_line))

    # INDEX
    index_lines = ["# SP4.7 split index", "", "file | start_line | matched_heading", "---|---:|---"]
    for fname, start_line, heading in sorted(index_rows, key=lambda r: r[1]):
        index_lines.append(f"{fname} | line {start_line} | {heading}")
    (out_dir / "_INDEX_4.7.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    # DIAGNOSTIC
    diag_lines = ["# SP4.7 split diagnostic", ""]
    diag_lines.extend(f"- {d}" for d in diagnostics)
    (out_dir / "_DIAGNOSTIC_4.7.md").write_text("\n".join(diag_lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description="Split ONLY SP4 Part 7 (4.7.x) from a consolidated markdown file.")
    ap.add_argument("input_md", help="Path to SP-4_process Documentation.md")
    ap.add_argument("out_root", help="Output root directory (e.g., Canonical MD\\SP4_ProcessDocumentation)")
    args = ap.parse_args()

    in_path = Path(args.input_md)
    if not in_path.exists():
        raise SystemExit(f"ERROR: input file not found: {in_path}")

    out_root = Path(args.out_root)
    out_dir = out_root / "4.7_EpistemicTraces"

    text = in_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    part7_start, part7_end = find_part7_bounds(lines)
    ranges, diagnostics = compute_ranges(lines, part7_start, part7_end)

    if not ranges:
        raise SystemExit("ERROR: No 4.7.* headings/ranges found inside Part 7.")

    write_outputs(lines, out_dir, ranges, diagnostics)

    print("=== sp4_47_cutter.py ===")
    print(f"Input: {in_path}")
    print(f"Output folder: {out_dir}")
    wrote = len([k for k in ID_TO_FILENAME.keys() if k in ranges])
    print(f"Wrote {wrote} files (+ index + diagnostic).")
    if any(d.startswith("Missing expected headings") for d in diagnostics):
        print("WARNING: Some expected headings were missing; see _DIAGNOSTIC_4.7.md")


if __name__ == "__main__":
    main()
