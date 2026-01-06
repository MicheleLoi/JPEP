#!/usr/bin/env python3
"""
Obsidian Connections Generator (Strategy A) + Chat Hub (source_chat_id)

Usage:
  python obsidian_connections_with_chat_hubs.py /path/to/vault
  python obsidian_connections_with_chat_hubs.py /path/to/vault --dry-run
  python obsidian_connections_with_chat_hubs.py /path/to/vault --no-hubs
  python obsidian_connections_with_chat_hubs.py /path/to/vault --siblings max --max-siblings 20
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# HARD FAIL if PyYAML is missing - this script is useless without frontmatter parsing
try:
    import yaml  # PyYAML
except Exception:
    raise SystemExit(
        "ERROR: PyYAML is required to parse YAML frontmatter (--- ... ---).\n"
        "Install it with:\n"
        "  pip install pyyaml\n"
        "Then rerun the script.\n\n"
        "This script cannot function without YAML parsing - all connection data\n"
        "lives in frontmatter fields like source_chat_id, inputs, outputs, etc."
    )


# -------- Patterns --------
# Numeric dot IDs: 4.7.3, 5.2.4.1, 11.2, etc.
DOT_ID_RE = re.compile(r"\b\d+(?:\.\d+)+\b")

# SP-prefixed: SP5.1, SP-5, SP 2.1, proto-SP2.1
SP_ID_RE = re.compile(r"\b(?:proto-)?SP[-\s]?(?P<id>\d+(?:\.\d+)*)\b", re.IGNORECASE)

# Obsidian link with id inside: [[5.2.8]]
OBSIDIAN_ID_RE = re.compile(r"\[\[(?P<id>\d+(?:\.\d+)+)\]\]")

# Filename prefix: 4.7.3_..., 5.3.1_..., SP5.1_...
FILENAME_PREFIX_RE = re.compile(r"^(?:SP)?(?P<id>\d+(?:\.\d+)*)")

# Underscore IDs like 5_2_3_ -> 5.2.3
UNDERSCORE_ID_RE = re.compile(r"\b(?P<id>\d+(?:_\d+)+)\b")


# -------- Configuration defaults --------
DEFAULT_REL_FIELDS = [
    # strong / expected
    "inputs", "outputs",
    # seen in your corpus / inventory
    "input_artifacts", "influenced_artifacts",
    "one_to_many_influence",
    "continued_by", "continuation_of", "feeds_into",
    "related_documents",
    "cross_documented_as",
    "output_usage", "used_as_input",
    "inputs_see", "inputs_key_source", "inputs_summary",
    "relationship_note", "taxonomy_source_role",
    "salient_outputs", "salient_output_artifact",
]

CHAT_FIELDS = ["source_chat_id", "chat_id", "source_chat", "source_chatid"]  # allow variants
CHAT_NAME_FIELDS = ["source_chat_name", "chat_name"]


@dataclass
class FileEntry:
    path: Path
    stem: str  # filename without .md


# -------- Helpers --------
def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write_text(p: Path, s: str) -> None:
    p.write_text(s, encoding="utf-8")


def split_frontmatter(md: str) -> Tuple[Optional[str], str]:
    if not md.startswith("---"):
        return None, md
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", md, re.DOTALL)
    if not m:
        return None, md
    return m.group(1), m.group(2)


def parse_yaml(fm: str, filepath: Path) -> dict:
    """
    Parse YAML frontmatter. HARD FAIL on malformed YAML so broken 
    frontmatter is caught immediately, not silently ignored.
    """
    try:
        obj = yaml.safe_load(fm)
    except Exception as e:
        raise SystemExit(
            f"ERROR: Failed to parse YAML frontmatter in:\n"
            f"  {filepath}\n"
            f"YAML error: {e}\n\n"
            f"Fix the frontmatter syntax before running again."
        )
    return obj if isinstance(obj, dict) else {}


def normalize_list(v) -> List[str]:
    if v is None:
        return []
    if isinstance(v, str):
        return [v]
    if isinstance(v, (int, float, bool)):
        return [str(v)]
    if isinstance(v, list):
        out: List[str] = []
        for item in v:
            out.extend(normalize_list(item))
        return out
    if isinstance(v, dict):
        return [str(v)]
    return [str(v)]


def extract_ids_any(text: str) -> List[str]:
    """
    Extract IDs from arbitrary text.
    Supports:
      - dot IDs (4.7.3)
      - SP/proto-SP IDs (SP5.1 -> 5.1)
      - obsidian IDs ([[5.2.8]] -> 5.2.8)
      - underscore IDs (5_2_3 -> 5.2.3)
    """
    found: List[str] = []
    seen = set()

    # Obsidian IDs
    for m in OBSIDIAN_ID_RE.finditer(text):
        _id = m.group("id")
        if _id not in seen:
            seen.add(_id)
            found.append(_id)

    # SP/proto-SP
    for m in SP_ID_RE.finditer(text):
        _id = m.group("id")
        if _id and _id not in seen:
            seen.add(_id)
            found.append(_id)

    # Dot IDs
    for m in DOT_ID_RE.finditer(text):
        _id = m.group(0)
        if _id not in seen:
            seen.add(_id)
            found.append(_id)

    # Underscore IDs -> convert
    for m in UNDERSCORE_ID_RE.finditer(text):
        raw = m.group("id")
        if "_" in raw:
            conv = raw.replace("_", ".")
            if conv.count(".") >= 1 and conv not in seen:
                seen.add(conv)
                found.append(conv)

    return found


def build_id_index(vault: Path) -> Dict[str, FileEntry]:
    idx: Dict[str, FileEntry] = {}
    for p in vault.rglob("*.md"):
        m = FILENAME_PREFIX_RE.match(p.name)
        if m:
            key = m.group("id")
            idx[key] = FileEntry(path=p, stem=p.stem)
    return idx


def build_chat_index(vault: Path) -> Tuple[Dict[str, List[FileEntry]], Dict[Path, str], Dict[str, str]]:
    """
    Returns:
      chat_index: chat_id -> list of FileEntry
      file_to_chat: file_path -> chat_id
      chat_to_name: chat_id -> chat_name (best effort)
    """
    chat_index: Dict[str, List[FileEntry]] = {}
    file_to_chat: Dict[Path, str] = {}
    chat_to_name: Dict[str, str] = {}

    for p in vault.rglob("*.md"):
        txt = read_text(p)
        fm, _ = split_frontmatter(txt)
        if not fm:
            continue
        data = parse_yaml(fm, p)
        chat_id = None

        for k in CHAT_FIELDS:
            if k in data and data.get(k):
                # keep raw string; normalize whitespace
                chat_id = str(data.get(k)).strip()
                break

        if not chat_id:
            continue

        entry = FileEntry(path=p, stem=p.stem)
        chat_index.setdefault(chat_id, []).append(entry)
        file_to_chat[p] = chat_id

        # best effort: capture a name if present
        for nk in CHAT_NAME_FIELDS:
            if nk in data and data.get(nk):
                name = str(data.get(nk)).strip()
                if chat_id not in chat_to_name:
                    chat_to_name[chat_id] = name
                break

    # stable ordering by filename for determinism
    for cid in chat_index:
        chat_index[cid].sort(key=lambda e: e.stem.lower())

    return chat_index, file_to_chat, chat_to_name


def ensure_dir(p: Path) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)


def format_link(stem: str, display: str, alias_mode: str = "id") -> str:
    if alias_mode == "none":
        return f"[[{stem}]]"
    return f"[[{stem}|{display}]]"


def find_and_replace_auto_block(body: str, header: str, new_block: str) -> Tuple[str, bool]:
    """
    Replace existing block from header until next H2 or end; else append.
    """
    header_esc = re.escape(header.strip())
    pattern = re.compile(rf"(?ms)^\s*{header_esc}\s*$.*?(?=^\s*##\s|\Z)")
    if pattern.search(body):
        updated = pattern.sub(new_block.strip() + "\n\n", body)
        return updated, (updated != body)
    sep = "\n\n" if not body.endswith("\n\n") else ""
    return body + sep + new_block, True


def collect_rels(data: dict, rel_fields: List[str]) -> Dict[str, List[str]]:
    rels: Dict[str, List[str]] = {}
    for f in rel_fields:
        if f in data and data.get(f) is not None:
            vals = normalize_list(data.get(f))
            # ignore explicit null-like strings
            vals = [v for v in vals if str(v).strip().lower() not in ("null", "none", "")]
            if vals:
                rels[f] = vals
    return rels


def generate_connections_block(
    *,
    file_entry: FileEntry,
    id_index: Dict[str, FileEntry],
    chat_index: Dict[str, List[FileEntry]],
    file_to_chat: Dict[Path, str],
    chat_to_name: Dict[str, str],
    rels: Dict[str, List[str]],
    hubs_folder: str,
    alias_mode: str,
    siblings_mode: str,
    max_siblings: int,
) -> str:
    """
    Order: Chat skeleton first, then explicit rel fields.
    """
    lines: List[str] = []
    lines.append("## Connections (auto)")
    lines.append("")

    # --- 1) Source chat skeleton (primary) ---
    chat_id = file_to_chat.get(file_entry.path)
    if chat_id:
        hub_stem = f"{hubs_folder.rstrip('/').rstrip('\\')}/CHAT_{chat_id}"
        # Obsidian wants paths without extension; keep forward slash
        hub_stem = hub_stem.replace("\\", "/")
        chat_name = chat_to_name.get(chat_id, "")
        label = "chat" if not chat_name else f"chat: {chat_name}"
        lines.append("### Source chat (primary)")
        lines.append(f"- {format_link(hub_stem, label, alias_mode='none')}")
        # siblings
        sibs = [e for e in chat_index.get(chat_id, []) if e.path != file_entry.path]
        if sibs:
            lines.append("### Sibling artifacts (same chat)")
            if siblings_mode == "none":
                lines.append("- _(siblings hidden by config)_")
            else:
                shown = sibs[:max_siblings]
                sib_links = [format_link(s.stem, s.stem, alias_mode="none") for s in shown]
                lines.append("- " + "; ".join(sib_links))
                if len(sibs) > max_siblings:
                    lines.append(f"- _(and {len(sibs) - max_siblings} more...)_")
        lines.append("")

    # --- 2) Explicit relations (inputs/outputs/etc.) ---
    if rels:
        lines.append("### Explicit links (inputs/outputs/etc.)")
        for field, raw_items in rels.items():
            resolved: List[str] = []
            unresolved: List[str] = []

            for raw in raw_items:
                ids = extract_ids_any(str(raw))
                if not ids:
                    unresolved.append(str(raw).strip())
                    continue
                for _id in ids:
                    if _id in id_index:
                        resolved.append(format_link(id_index[_id].stem, _id, alias_mode=alias_mode))
                    else:
                        unresolved.append(_id)

            # dedupe preserving order
            def dedupe(seq: List[str]) -> List[str]:
                seen = set()
                out = []
                for x in seq:
                    if x not in seen:
                        seen.add(x)
                        out.append(x)
                return out

            resolved = dedupe(resolved)
            unresolved = dedupe(unresolved)

            if not resolved and not unresolved:
                continue

            lines.append(f"**{field}:**")
            if resolved:
                lines.append("- " + "; ".join(resolved))
            if unresolved:
                lines.append("- " + "; ".join([f"UNRESOLVED: {u}" for u in unresolved]))
            lines.append("")

    if len(lines) <= 3:
        lines.append("_No connections found._")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_chat_hubs(
    vault: Path,
    hubs_folder: str,
    chat_index: Dict[str, List[FileEntry]],
    chat_to_name: Dict[str, str],
    dry_run: bool,
) -> int:
    """
    Create/update hub notes: <vault>/<hubs_folder>/CHAT_<chat_id>.md
    """
    hubs_root = (vault / hubs_folder).resolve()
    ensure_dir(hubs_root / "dummy.txt")
    count = 0

    for chat_id, files in chat_index.items():
        hub_path = hubs_root / f"CHAT_{chat_id}.md"
        title = f"Chat hub: {chat_id}"
        chat_name = chat_to_name.get(chat_id, "")

        lines = []
        lines.append(f"# {title}")
        lines.append("")
        if chat_name:
            lines.append(f"- **Chat name:** {chat_name}")
        lines.append(f"- **Chat ID:** {chat_id}")
        lines.append(f"- **Artifacts:** {len(files)}")
        lines.append("")
        lines.append("## Artifacts")
        lines.append("")
        for fe in files:
            # link by stem (relative)
            lines.append(f"- [[{fe.stem}]]")
        lines.append("")

        content = "\n".join(lines)

        if not dry_run:
            write_text(hub_path, content)
        count += 1

    return count


def process_file(
    p: Path,
    *,
    id_index: Dict[str, FileEntry],
    chat_index: Dict[str, List[FileEntry]],
    file_to_chat: Dict[Path, str],
    chat_to_name: Dict[str, str],
    rel_fields: List[str],
    hubs_folder: str,
    alias_mode: str,
    siblings_mode: str,
    max_siblings: int,
    dry_run: bool,
) -> bool:
    txt = read_text(p)
    fm, body = split_frontmatter(txt)
    if not fm:
        return False
    data = parse_yaml(fm, p)

    rels = collect_rels(data, rel_fields)

    entry = FileEntry(path=p, stem=p.stem)
    block = generate_connections_block(
        file_entry=entry,
        id_index=id_index,
        chat_index=chat_index,
        file_to_chat=file_to_chat,
        chat_to_name=chat_to_name,
        rels=rels,
        hubs_folder=hubs_folder,
        alias_mode=alias_mode,
        siblings_mode=siblings_mode,
        max_siblings=max_siblings,
    )

    new_body, changed = find_and_replace_auto_block(body, "## Connections (auto)", block)
    if not changed:
        return False

    new_txt = "---\n" + fm.strip() + "\n---\n" + new_body.lstrip("\n")
    if not dry_run:
        write_text(p, new_txt)
    return True


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Generate Obsidian connection blocks and chat hubs from YAML frontmatter.",
        epilog="Requires PyYAML. Install with: pip install pyyaml"
    )
    ap.add_argument("vault", type=str, help="Path to Obsidian vault")
    ap.add_argument("--dry-run", action="store_true", help="Show what would change without modifying files")
    ap.add_argument("--no-hubs", action="store_true", help="Do not generate chat hub notes")
    ap.add_argument("--hubs-folder", type=str, default="_HUBS", help="Folder (inside vault) for CHAT hubs")
    ap.add_argument("--alias-mode", choices=["id", "none"], default="id", help="Link format for explicit IDs")
    ap.add_argument("--siblings", choices=["max", "none"], default="max", help="Show sibling list or hide")
    ap.add_argument("--max-siblings", type=int, default=30)
    ap.add_argument("--rel-fields", type=str, default=",".join(DEFAULT_REL_FIELDS),
                    help="Comma-separated list of frontmatter fields to scan for relationships")

    args = ap.parse_args()
    vault = Path(args.vault).expanduser().resolve()
    if not vault.exists() or not vault.is_dir():
        raise SystemExit(f"ERROR: Vault not found: {vault}")

    rel_fields = [s.strip() for s in args.rel_fields.split(",") if s.strip()]

    print(f"Scanning vault: {vault}")
    print(f"Relationship fields: {len(rel_fields)} configured")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE (will modify files)'}")
    print()

    # Pass 1 (logical): indices
    id_index = build_id_index(vault)
    print(f"Found {len(id_index)} files with numeric ID prefixes")

    chat_index, file_to_chat, chat_to_name = build_chat_index(vault)
    print(f"Found {len(chat_index)} unique source_chat_ids across {len(file_to_chat)} files")
    print()

    # Pass 2 (logical): write hubs + update files
    if not args.no_hubs:
        hubs_written = write_chat_hubs(
            vault=vault,
            hubs_folder=args.hubs_folder,
            chat_index=chat_index,
            chat_to_name=chat_to_name,
            dry_run=args.dry_run,
        )
        print(f"{'Would write' if args.dry_run else 'Wrote'} {hubs_written} chat hubs in {args.hubs_folder}/")

    modified = 0
    errors = 0
    for p in vault.rglob("*.md"):
        # skip hub notes themselves to avoid self-noise
        if args.hubs_folder in p.parts:
            continue
        try:
            if process_file(
                p,
                id_index=id_index,
                chat_index=chat_index,
                file_to_chat=file_to_chat,
                chat_to_name=chat_to_name,
                rel_fields=rel_fields,
                hubs_folder=args.hubs_folder,
                alias_mode=args.alias_mode,
                siblings_mode=args.siblings,
                max_siblings=args.max_siblings,
                dry_run=args.dry_run,
            ):
                modified += 1
        except SystemExit:
            # Re-raise YAML parse errors (these are fatal)
            raise
        except Exception as e:
            print(f"[ERROR] {p}: {e}")
            errors += 1

    print(f"{'Would modify' if args.dry_run else 'Modified'} {modified} files.")
    if errors:
        print(f"Encountered {errors} non-fatal errors (see above).")


if __name__ == "__main__":
    main()
