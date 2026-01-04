#!/usr/bin/env python3
"""
Obsidian Chat-Skeleton generator:
- builds chat hubs: _HUBS/CHAT_<source_chat_id>.md
- updates each note that has `source_chat_id` in YAML frontmatter with a
  "## Connections (auto)" section linking to its chat hub + sibling artifacts.

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

def _build_hub_content(
    chat_id: str,
    chat_name: str,
    notes: List[NoteInfo],
) -> str:
    notes_sorted = sorted(notes, key=_sort_key_for_note)
    now = _dt.datetime.now().isoformat(timespec="seconds")
    fm = {
        "source_chat_name": chat_name,
        "source_chat_id": chat_id,
        "artifacts_count": len(notes),
        "generated_at": now,
    }
    fm_text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    lines = [
        "---",
        fm_text,
        "---",
        "",
        f"# Chat Hub: {chat_name}",
        "",
        "## Artifacts generati",
    ]
    for n in notes_sorted:
        lines.append(f"- {_safe_wikilink(n.stem)}")
    lines.append("")
    return "\n".join(lines)

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Generate Obsidian chat hubs + per-note Connections (auto) for a chat-skeleton system (optionally scoped to subfolders)."
    )
    ap.add_argument("vault", type=str, help="Path to Obsidian vault (root folder).")
    ap.add_argument("--hubs-folder", type=str, default="_HUBS", help="Folder (under vault) where chat hubs are written.")
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

    unique_chats = len(chat_index)
    notes_with_chat = sum(len(v) for v in chat_index.values())

    hubs_to_write: List[Tuple[Path, str]] = []
    if not args.no_hubs:
        for chat_id, group in chat_index.items():
            chat_name = chat_name_by_id.get(chat_id, f"(unknown chat name) {chat_id}")
            hub_path = hubs_folder / f"CHAT_{chat_id}.md"
            hubs_to_write.append((hub_path, _build_hub_content(chat_id, chat_name, group)))

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

    print(f"Scanned: {len(md_files)} markdown files")
    print(f"Found: {notes_with_chat} files with source_chat_id across {unique_chats} unique chats")
    if not args.no_hubs:
        print(f"{'Would write' if args.dry_run else 'Will write'} {len(hubs_to_write)} chat hubs in: {hubs_folder}")
    print(f"{'Would modify' if args.dry_run else 'Will modify'} {len(notes_to_write)} notes with Connections (auto)")

    if args.dry_run:
        for p, _ in hubs_to_write[:10]:
            print(f"[hub] {p.relative_to(vault)}")
        if len(hubs_to_write) > 10:
            print(f"... ({len(hubs_to_write) - 10} more hubs)")
        for p, _ in notes_to_write[:10]:
            print(f"[note] {p.relative_to(vault)}")
        if len(notes_to_write) > 10:
            print(f"... ({len(notes_to_write) - 10} more notes)")
        return 0

    if not args.no_hubs and hubs_to_write:
        hubs_folder.mkdir(parents=True, exist_ok=True)
        for p, content in hubs_to_write:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")

    for p, updated in notes_to_write:
        if args.backup:
            bak = p.with_suffix(p.suffix + ".bak")
            shutil.copy2(p, bak)
        p.write_text(updated, encoding="utf-8")

    print("Done.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
