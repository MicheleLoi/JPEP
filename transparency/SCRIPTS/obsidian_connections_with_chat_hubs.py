#!/usr/bin/env python3
"""
Obsidian Chat-Skeleton generator:
- builds chat hubs: _HUBS/CHAT_<source_chat_id>.md
- updates each note that has `source_chat_id` in YAML frontmatter with a
  "## Connections (auto)" section linking to its chat hub + sibling artifacts.
- reads hub_annotations.yaml for session-level metadata (authoritative source)
- backs up existing hubs before overwriting; generates verification queue
  for hubs with manual content not covered by YAML

Designed to be re-runnable + idempotent via markers:
  <!-- CONNECTIONS_AUTO_START -->
  <!-- CONNECTIONS_AUTO_END -->
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    import yaml  # type: ignore
except Exception as e:  # pragma: no cover
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    raise

AUTO_START = "<!-- CONNECTIONS_AUTO_START -->"
AUTO_END = "<!-- CONNECTIONS_AUTO_END -->"
CONN_HEADER = "## Connections (auto)"

FRONTMATTER_RE = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---\s*\r?\n", re.DOTALL)

DOT_ID_RE = re.compile(r"(?<!\d)(\d+(?:\.\d+)+)(?!\d)")
UNDERSCORE_ID_RE = re.compile(r"(?<!\d)(\d+(?:_\d+)+)_?(?!\d)")
SP_ID_RE = re.compile(r"\b(proto-)?SP-?\d+(?:\.\d+)*\b", re.IGNORECASE)

OBSIDIAN_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")

REL_FIELDS_STRONG = ["inputs", "outputs"]
REL_FIELDS_DERIVED = ["input_artifacts", "influenced_artifacts", "one_to_many_influence"]
REL_FIELDS_CONTINUITY = ["continuation_of", "continued_by"]
REL_FIELDS_RELATED = ["related_documents", "salient_outputs"]

# V1/V2 field name variants — map to canonical names for connection rendering
V1V2_FIELD_ALIASES = {
    "output_completed": "outputs",
    "derived_from_artifact": "inputs",
    "source_chat_id_1": "source_chat_id",
    "source_chat_id_2": "source_chat_id",
    "source_chat_id_3": "source_chat_id",
}

ALL_REL_FIELDS = (
    REL_FIELDS_STRONG
    + REL_FIELDS_DERIVED
    + REL_FIELDS_CONTINUITY
    + REL_FIELDS_RELATED
)

@dataclass(frozen=True)
class NoteInfo:
    path: Path
    stem: str
    frontmatter: Dict[str, Any]
    body: str
    doc_id: Optional[str] = None  # internal artifact id (e.g., 5.2.4.1) if detectable

def _read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")

def _split_frontmatter(text: str) -> Tuple[Dict[str, Any], str]:
    """
    Returns (frontmatter_dict, body_without_frontmatter).
    If no YAML frontmatter, returns ({}, full_text).
    """
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    yaml_text = m.group(1).strip()
    body = text[m.end():]
    if not yaml_text:
        return {}, body
    data = yaml.safe_load(yaml_text)
    if data is None:
        data = {}
    if not isinstance(data, dict):
        data = {}
    return data, body

def _extract_doc_id(stem: str, fm: Dict[str, Any]) -> Optional[str]:
    v = fm.get("document_id")
    if isinstance(v, str):
        v = v.strip()
        if DOT_ID_RE.fullmatch(v):
            return v
        if UNDERSCORE_ID_RE.fullmatch(v):
            return v.replace("_", ".").rstrip(".")
        if SP_ID_RE.fullmatch(v):
            return v

    m = re.match(r"^(\d+(?:\.\d+)+)\b", stem)
    if m:
        return m.group(1)

    m = re.match(r"^(\d+(?:_\d+)+)\b", stem)
    if m:
        return m.group(1).replace("_", ".").rstrip(".")

    m = re.match(r"^((?:proto-)?SP-?\d+(?:\.\d+)*)\b", stem, re.IGNORECASE)
    if m:
        return m.group(1)

    return None

def _iter_md_files(roots: Iterable[Path], exclude_dirs: Iterable[str]) -> Iterable[Path]:
    """Iterate markdown files under one or more roots."""
    exclude_set = set(exclude_dirs)
    for root in roots:
        for p in root.rglob("*.md"):
            parts = set(p.parts)
            if any(part.startswith(".") for part in p.parts):
                continue
            if parts & exclude_set:
                continue
            yield p

def _safe_wikilink(target_stem_or_path: str, alias: Optional[str] = None) -> str:
    if alias:
        return f"[[{target_stem_or_path}|{alias}]]"
    return f"[[{target_stem_or_path}]]"

def _normalize_rel_item(item: str) -> str:
    item = item.strip()
    m = OBSIDIAN_LINK_RE.search(item)
    if m:
        inner = m.group(1)
        inner = inner.split("|", 1)[0].strip()
        return inner
    return item

def _extract_candidate_ids(text: str) -> List[str]:
    found: List[str] = []

    def add(x: str) -> None:
        if x not in found:
            found.append(x)

    for m in DOT_ID_RE.finditer(text):
        add(m.group(1))
    for m in UNDERSCORE_ID_RE.finditer(text):
        add(m.group(1).replace("_", ".").rstrip("."))
    for m in SP_ID_RE.finditer(text):
        add(m.group(0))
    return found

def _sort_key_for_note(n: NoteInfo) -> Tuple[int, Tuple[int, ...], str]:
    if n.doc_id and DOT_ID_RE.fullmatch(n.doc_id):
        nums = tuple(int(x) for x in n.doc_id.split("."))
        return (0, nums, n.stem.lower())
    return (1, tuple(), n.stem.lower())

def _resolve_to_link(
    raw_item: str,
    id_index: Dict[str, str],
    stem_index: Dict[str, str],
) -> Tuple[Optional[str], Optional[str]]:
    item = _normalize_rel_item(raw_item)

    if item in stem_index:
        return _safe_wikilink(stem_index[item]), None

    for candidate in _extract_candidate_ids(item) or [item]:
        if candidate in id_index:
            return _safe_wikilink(id_index[candidate]), None

    if item and all(ch not in item for ch in "\n\r"):
        return _safe_wikilink(item), None

    return None, raw_item

def _render_connections_block(
    note: NoteInfo,
    hub_link: Optional[str],
    siblings: List[NoteInfo],
    id_index: Dict[str, str],
    stem_index: Dict[str, str],
    max_siblings: int,
    include_relations: bool,
) -> str:
    lines: List[str] = []
    lines.append(AUTO_START)

    if hub_link:
        lines.append("### Source chat (primary)")
        lines.append(f"- {hub_link}")
        lines.append("")

        if siblings:
            lines.append("### Sibling artifacts (same chat)")
            shown = siblings[:max_siblings] if max_siblings >= 0 else siblings
            for sib in shown:
                lines.append(f"- {_safe_wikilink(sib.stem)}")
            if max_siblings >= 0 and len(siblings) > max_siblings:
                lines.append(f"- … (and {len(siblings) - max_siblings} more)")
            lines.append("")

    unresolved: List[str] = []
    if include_relations:
        def add_rel_section(title: str, keys: List[str]) -> None:
            nonlocal unresolved
            items: List[str] = []
            for k in keys:
                v = note.frontmatter.get(k)
                if v is None:
                    continue
                if isinstance(v, str):
                    vals = [v]
                elif isinstance(v, list):
                    vals = [str(x) for x in v]
                else:
                    vals = [str(v)]
                for raw in vals:
                    link, bad = _resolve_to_link(raw, id_index, stem_index)
                    if link:
                        items.append(link)
                    elif bad:
                        unresolved.append(bad)
            if items:
                lines.append(f"### {title}")
                for it in items:
                    lines.append(f"- {it}")
                lines.append("")

        add_rel_section("Inputs", REL_FIELDS_STRONG[:1])
        add_rel_section("Outputs", REL_FIELDS_STRONG[1:])
        add_rel_section("Derived / influenced", REL_FIELDS_DERIVED)
        add_rel_section("Continuity", REL_FIELDS_CONTINUITY)
        add_rel_section("Related", REL_FIELDS_RELATED)

    if unresolved:
        seen = set()
        uniq = []
        for x in unresolved:
            if x not in seen:
                seen.add(x)
                uniq.append(x)
        lines.append("### UNRESOLVED")
        for x in uniq:
            lines.append(f"- [ ] {x}")
        lines.append("")

    lines.append(AUTO_END)
    return "\n".join(lines).rstrip() + "\n"

def _upsert_connections_section(original_text: str, new_auto_block: str) -> str:
    if AUTO_START in original_text and AUTO_END in original_text:
        before = original_text.split(AUTO_START, 1)[0]
        after = original_text.split(AUTO_END, 1)[1]
        return before.rstrip() + "\n\n" + CONN_HEADER + "\n\n" + new_auto_block + after.lstrip("\n")

    header_idx = original_text.find(CONN_HEADER)
    if header_idx != -1:
        line_end = original_text.find("\n", header_idx)
        if line_end == -1:
            line_end = len(original_text)
        insert_pos = line_end + 1
        return (
            original_text[:insert_pos].rstrip()
            + "\n\n"
            + new_auto_block
            + "\n"
            + original_text[insert_pos:].lstrip("\n")
        )

    sep = "\n\n" if not original_text.endswith("\n") else "\n"
    return original_text.rstrip() + sep + CONN_HEADER + "\n\n" + new_auto_block + "\n"


# ---------------------------------------------------------------------------
# Hub annotation loading
# ---------------------------------------------------------------------------

def _load_hub_annotations(yaml_path: Path) -> Dict[str, Dict[str, Any]]:
    """Load session metadata from hub_annotations.yaml.

    Returns dict keyed by session ID (UUID or SID string) → annotation dict.
    Returns empty dict if file doesn't exist.
    """
    if not yaml_path.exists():
        return {}
    with yaml_path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("sessions", {})


def _extract_manual_content(hub_path: Path) -> Optional[str]:
    """Read an existing hub file and extract content that looks manually added.

    Returns the manual content as a string, or None if the file doesn't exist
    or has no content beyond auto-generated structure.
    """
    if not hub_path.exists():
        return None
    text = _read_text(hub_path)
    fm, body = _split_frontmatter(text)

    # Strip auto-generated blocks
    cleaned = body
    if AUTO_START in cleaned and AUTO_END in cleaned:
        before = cleaned.split(AUTO_START, 1)[0]
        after = cleaned.split(AUTO_END, 1)[1]
        cleaned = before + after

    # Strip known auto-generated headers and artifact lists
    auto_patterns = [
        r"^# Chat Hub:.*$",
        r"^## Artifacts generati.*$",
        r"^- \[\[.*\]\]$",
        r"^\s*$",
    ]
    remaining_lines = []
    for line in cleaned.split("\n"):
        is_auto = False
        for pat in auto_patterns:
            if re.match(pat, line):
                is_auto = True
                break
        if not is_auto:
            remaining_lines.append(line)

    manual = "\n".join(remaining_lines).strip()
    if not manual:
        return None

    # Also capture any non-standard frontmatter fields
    auto_fm_keys = {"source_chat_name", "source_chat_id", "artifacts_count", "generated_at"}
    manual_fm = {k: v for k, v in fm.items() if k not in auto_fm_keys}
    if manual_fm:
        fm_text = yaml.safe_dump(manual_fm, sort_keys=False, allow_unicode=True).strip()
        manual = f"### Frontmatter (non-auto)\n```yaml\n{fm_text}\n```\n\n{manual}"

    return manual if manual.strip() else None


def _build_hub_content(
    chat_id: str,
    chat_name: str,
    notes: List[NoteInfo],
    annotation: Optional[Dict[str, Any]] = None,
) -> str:
    """Build hub .md content from artifact scan + optional YAML annotation."""
    notes_sorted = sorted(notes, key=_sort_key_for_note)
    now = _dt.datetime.now().isoformat(timespec="seconds")

    # Base frontmatter from artifact scan
    fm: Dict[str, Any] = {
        "source_chat_name": chat_name,
        "source_chat_id": chat_id,
        "artifacts_count": len(notes),
        "generated_at": now,
    }

    # Enrich with YAML annotation if available
    if annotation:
        if "title" in annotation:
            fm["source_chat_name"] = annotation["title"]
        if "date" in annotation:
            fm["date"] = str(annotation["date"])
        if "date_end" in annotation:
            fm["date_end"] = str(annotation["date_end"])
        if "model" in annotation:
            fm["model"] = annotation["model"]
        if "platform" in annotation:
            fm["platform"] = annotation["platform"]
        if "gitignored" in annotation:
            fm["gitignored"] = annotation["gitignored"]
        if "continues_from" in annotation:
            cf = annotation["continues_from"]
            if cf is not None:
                fm["continues_from"] = cf
        fm["yaml_annotated"] = True

    fm_text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    lines = [
        "---",
        fm_text,
        "---",
        "",
    ]

    # Title — use annotation title if available
    title = annotation.get("title", chat_name) if annotation else chat_name
    lines.append(f"# Chat Hub: {title}")
    lines.append("")

    # Session metadata section (from YAML)
    if annotation:
        meta_lines = []
        if "role" in annotation:
            role = annotation["role"].strip() if isinstance(annotation["role"], str) else str(annotation["role"])
            meta_lines.append(f"**Role:** {role}")
        if "continues_from" in annotation and annotation["continues_from"] is not None:
            cf = annotation["continues_from"]
            if isinstance(cf, list):
                cf_links = ", ".join(f"[[_HUBS/CHAT_{c}|{c}]]" for c in cf)
                meta_lines.append(f"**Continues from:** {cf_links}")
            elif cf:
                meta_lines.append(f"**Continues from:** [[_HUBS/CHAT_{cf}|{cf}]]")
            if "continues_from_note" in annotation:
                note_text = annotation["continues_from_note"].strip()
                meta_lines.append(f"> {note_text}")
        if "note" in annotation:
            note_text = annotation["note"].strip()
            meta_lines.append(f"\n{note_text}")
        if meta_lines:
            lines.append("## Session metadata")
            lines.append("")
            lines.extend(meta_lines)
            lines.append("")

        # Inputs section (from YAML)
        if "inputs" in annotation and annotation["inputs"]:
            lines.append("## Inputs received")
            lines.append("")
            for inp in annotation["inputs"]:
                lines.append(f"- {inp}")
            if "inputs_note" in annotation:
                lines.append("")
                lines.append(f"> {annotation['inputs_note'].strip()}")
            lines.append("")

    # Artifacts section (always from scan)
    lines.append("## Artifacts produced")
    lines.append("")
    for n in notes_sorted:
        lines.append(f"- {_safe_wikilink(n.stem)}")

    # YAML-declared artifacts not found in scan
    if annotation and "artifacts_produced" in annotation:
        scanned_stems = {n.stem for n in notes_sorted}
        yaml_artifacts = annotation["artifacts_produced"]
        for art in yaml_artifacts:
            art_stem = Path(art).stem if isinstance(art, str) else str(art)
            if art_stem not in scanned_stems:
                lines.append(f"- {art} *(declared in YAML, not found in scan)*")
        if "artifacts_note" in annotation:
            lines.append("")
            lines.append(f"> {annotation['artifacts_note'].strip()}")

    lines.append("")
    return "\n".join(lines)


def _build_verification_queue(
    entries: List[Dict[str, Any]],
    vault: Path,
) -> str:
    """Build VERIFICATION_QUEUE.md content."""
    now = _dt.datetime.now().isoformat(timespec="seconds")
    lines = [
        "---",
        f"generated_at: {now}",
        "purpose: Manual hub content found during rebuild that needs verification",
        "action: For each entry, decide whether to migrate content to hub_annotations.yaml or discard",
        "---",
        "",
        "# Hub Verification Queue",
        "",
        f"Generated: {now}",
        "",
        f"**{len(entries)} hubs** had manual content not covered by YAML annotations.",
        "For each, check the backup file and decide: migrate to `hub_annotations.yaml`, or discard.",
        "",
        "| Hub | Backup | Manual content preview |",
        "|-----|--------|-----------------------|",
    ]
    for e in entries:
        hub_rel = e["hub_path"].relative_to(vault)
        bak_rel = e["backup_path"].relative_to(vault)
        # First 120 chars of manual content, single line
        preview = e["manual_content"].replace("\n", " ").replace("|", "\\|")[:120]
        if len(e["manual_content"]) > 120:
            preview += "…"
        lines.append(f"| `{hub_rel}` | `{bak_rel}` | {preview} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Full manual content per hub")
    lines.append("")

    for e in entries:
        hub_rel = e["hub_path"].relative_to(vault)
        lines.append(f"### `{hub_rel}`")
        lines.append("")
        lines.append("```markdown")
        lines.append(e["manual_content"])
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Generate Obsidian chat hubs + per-note Connections (auto) for a chat-skeleton system."
    )
    ap.add_argument("vault", type=str, help="Path to Obsidian vault (root folder).")
    ap.add_argument("--hubs-folder", type=str, default="_HUBS", help="Folder (under vault) where chat hubs are written.")
    ap.add_argument("--yaml", type=str, default=None,
                    help="Path to hub_annotations.yaml. Default: <vault>/../SCRIPTS/hub_annotations.yaml")
    ap.add_argument("--no-hubs", action="store_true", help="Do not create/update hub notes; only update connections.")
    ap.add_argument("--dry-run", action="store_true", help="Print what would change without writing files.")
    ap.add_argument("--max-siblings", type=int, default=10, help="Max sibling links per note (use -1 for unlimited).")
    ap.add_argument("--exclude-dir", action="append", default=[], help="Folder name to exclude (can be repeated).")
    ap.add_argument("--scope", action="append", default=[], help="Relative subfolder under vault to scan (repeatable). If omitted, scans entire vault.")
    ap.add_argument("--include-relations", action="store_true", help="Also render Inputs/Outputs/Related from YAML into Connections.")
    ap.add_argument("--backup", action="store_true", help="Before modifying a note, create a .bak copy next to it.")
    args = ap.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    hubs_folder = vault / args.hubs_folder

    if not vault.exists() or not vault.is_dir():
        print(f"ERROR: vault path does not exist or is not a directory: {vault}", file=sys.stderr)
        return 2

    # Load YAML annotations
    if args.yaml:
        yaml_path = Path(args.yaml).expanduser().resolve()
    else:
        yaml_path = vault.parent / "SCRIPTS" / "hub_annotations.yaml"
    annotations = _load_hub_annotations(yaml_path)
    if annotations:
        print(f"Loaded {len(annotations)} session annotations from: {yaml_path}")
    else:
        print(f"No annotations loaded (looked at: {yaml_path})")

    exclude_dirs = list(args.exclude_dir)
    exclude_dirs.append(args.hubs_folder)  # don't scan generated hubs by default

    scan_roots = [vault]
    if args.scope:
        scan_roots = [(vault / s).resolve() for s in args.scope]
        missing_roots = [r for r in scan_roots if not r.exists() or not r.is_dir()]
        if missing_roots:
            for r in missing_roots:
                print(f"ERROR: scope path does not exist or is not a directory: {r}", file=sys.stderr)
            return 2

    md_files = list(_iter_md_files(scan_roots, exclude_dirs))
    notes: List[NoteInfo] = []
    for p in md_files:
        txt = _read_text(p)
        fm, body = _split_frontmatter(txt)
        stem = p.stem
        doc_id = _extract_doc_id(stem, fm)
        notes.append(NoteInfo(path=p, stem=stem, frontmatter=fm, body=body, doc_id=doc_id))

    id_index: Dict[str, str] = {}
    stem_index: Dict[str, str] = {}
    for n in notes:
        stem_index[n.stem] = n.stem
        if n.doc_id:
            id_index[n.doc_id] = n.stem

    chat_index: Dict[str, List[NoteInfo]] = {}
    chat_name_by_id: Dict[str, str] = {}

    for n in notes:
        chat_id = n.frontmatter.get("source_chat_id")
        if isinstance(chat_id, str) and chat_id.strip():
            chat_id = chat_id.strip()
            chat_index.setdefault(chat_id, []).append(n)

            chat_name = n.frontmatter.get("source_chat_name")
            if isinstance(chat_name, str) and chat_name.strip():
                chat_name_by_id.setdefault(chat_id, chat_name.strip())

    # Also include YAML-only sessions (sessions in YAML but no artifacts found in scan)
    for session_id, ann in annotations.items():
        session_key = str(session_id)
        if session_key not in chat_index:
            # YAML-only session — create hub even without scanned artifacts
            chat_index[session_key] = []
            if "title" in ann:
                chat_name_by_id[session_key] = ann["title"]

    unique_chats = len(chat_index)
    notes_with_chat = sum(len(v) for v in chat_index.values())

    # Build hubs
    hubs_to_write: List[Tuple[Path, str]] = []
    verification_entries: List[Dict[str, Any]] = []
    hubs_yaml_count = 0
    hubs_auto_count = 0

    if not args.no_hubs:
        for chat_id, group in chat_index.items():
            chat_name = chat_name_by_id.get(chat_id, f"(unknown chat name) {chat_id}")
            hub_path = hubs_folder / f"CHAT_{chat_id}.md"
            annotation = annotations.get(chat_id)

            # Extract manual content from existing hub before overwriting
            manual = _extract_manual_content(hub_path)

            if annotation:
                hubs_yaml_count += 1
            else:
                hubs_auto_count += 1

            # If manual content exists and no YAML annotation, add to verification queue
            if manual and not annotation:
                backup_path = hub_path.with_suffix(".md.bak")
                verification_entries.append({
                    "hub_path": hub_path,
                    "backup_path": backup_path,
                    "manual_content": manual,
                    "chat_id": chat_id,
                })

            content = _build_hub_content(chat_id, chat_name, group, annotation)
            hubs_to_write.append((hub_path, content))

    notes_to_write: List[Tuple[Path, str]] = []
    for chat_id, group in chat_index.items():
        hub_rel = f"{args.hubs_folder}/CHAT_{chat_id}"
        for n in group:
            siblings = [x for x in group if x.path != n.path]
            siblings_sorted = sorted(siblings, key=_sort_key_for_note)
            hub_link = None if args.no_hubs else _safe_wikilink(hub_rel, "chat")
            new_auto = _render_connections_block(
                note=n,
                hub_link=hub_link,
                siblings=siblings_sorted,
                id_index=id_index,
                stem_index=stem_index,
                max_siblings=args.max_siblings,
                include_relations=args.include_relations,
            )

            full_text = _read_text(n.path)
            updated = _upsert_connections_section(full_text, new_auto)

            if updated != full_text:
                notes_to_write.append((n.path, updated))

    # Report
    print(f"Scanned: {len(md_files)} markdown files")
    print(f"Found: {notes_with_chat} files with source_chat_id across {unique_chats} unique chats")
    if not args.no_hubs:
        print(f"{'Would write' if args.dry_run else 'Will write'} {len(hubs_to_write)} chat hubs "
              f"({hubs_yaml_count} YAML-enriched, {hubs_auto_count} auto-only) in: {hubs_folder}")
    print(f"{'Would modify' if args.dry_run else 'Will modify'} {len(notes_to_write)} notes with Connections (auto)")
    if verification_entries:
        print(f"{'Would generate' if args.dry_run else 'Will generate'} VERIFICATION_QUEUE.md "
              f"with {len(verification_entries)} hubs needing manual review")

    if args.dry_run:
        for p, _ in hubs_to_write[:10]:
            print(f"[hub] {p.relative_to(vault)}")
        if len(hubs_to_write) > 10:
            print(f"... ({len(hubs_to_write) - 10} more hubs)")
        for p, _ in notes_to_write[:10]:
            print(f"[note] {p.relative_to(vault)}")
        if len(notes_to_write) > 10:
            print(f"... ({len(notes_to_write) - 10} more notes)")
        if verification_entries:
            print(f"\nVerification queue entries:")
            for e in verification_entries:
                print(f"  - {e['hub_path'].relative_to(vault)}: {e['manual_content'][:80]}...")
        return 0

    # Write hubs (always back up existing hubs before overwriting)
    if not args.no_hubs and hubs_to_write:
        hubs_folder.mkdir(parents=True, exist_ok=True)
        backed_up = 0
        for p, content in hubs_to_write:
            p.parent.mkdir(parents=True, exist_ok=True)
            if p.exists():
                bak = p.with_suffix(".md.bak")
                shutil.copy2(p, bak)
                backed_up += 1
            p.write_text(content, encoding="utf-8")
        if backed_up:
            print(f"Backed up {backed_up} existing hub files (.md.bak)")

    # Write verification queue
    if verification_entries:
        vq_path = hubs_folder / "VERIFICATION_QUEUE.md"
        vq_content = _build_verification_queue(verification_entries, vault)
        vq_path.write_text(vq_content, encoding="utf-8")
        print(f"Wrote VERIFICATION_QUEUE.md with {len(verification_entries)} entries")

    # Write note updates
    for p, updated in notes_to_write:
        if args.backup:
            bak = p.with_suffix(p.suffix + ".bak")
            shutil.copy2(p, bak)
        p.write_text(updated, encoding="utf-8")

    print("Done.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
