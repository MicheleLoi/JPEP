"""
JPEP graph visualizer — builds an interactive HTML graph from SP-4/SP-5 frontmatter.
Mirrors the Obsidian graph view: hub nodes (sessions) + artifact nodes + directed edges.

Usage:
    python3 build_graph.py [--vault <path-to-Canonical_MD>] [--output <path.html>]

Defaults:
    --vault:  ../Canonical_MD  (relative to this script in transparency/SCRIPTS/)
    --output: <vault>/_GRAPHS/jpep_graph.html

Output: a single self-contained HTML file. Open in any browser.
"""

import re
import argparse
import yaml
from pathlib import Path
from pyvis.network import Network
import networkx as nx

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPTS_DIR = Path(__file__).parent
# Default: if script is in SCRIPTS/, vault is ../Canonical_MD; if run from Canonical_MD, use cwd
_default_vault = SCRIPTS_DIR / "../Canonical_MD" if (SCRIPTS_DIR / "../Canonical_MD").is_dir() else SCRIPTS_DIR

# Relational fields to extract directed edges from (CFP/III standard names)
REL_FIELDS = [
    "feeds_into", "derived_from", "output_completed", "inputs",
    "source_guidance", "source_file", "influenced_artifacts",
    "related_documents", "source_conversations",
    "related", "related_epistemic_trace_artifact",
]
# Multi-valued variants
REL_FIELDS_NUMBERED = [
    "output_completed1", "output_completed2", "output_completed3",
]

# V1/V2 field name variants → canonical name (v1/v2 used Title Case / mixed naming)
V1V2_FIELD_MAP = {
    "Input Artifacts":       "inputs",
    "Inputs":                "inputs",
    "input_artifacts":       "inputs",
    "phase1_inputs":         "inputs",
    "phase2_inputs":         "inputs",
    "phase3_inputs":         "inputs",
    "phase4_inputs":         "inputs",
    "phase5_inputs":         "inputs",
    "Output":                "output_completed",
    "Outputs":               "output_completed",
    "outputs":               "output_completed",
    "derived_from_artifact": "derived_from",
    "influenced_by":         "inputs",
    "Source":                "source_file",
    "conversion_source":     "source_file",
    "input_to":              "feeds_into",
}

# Node colours by artifact type
TYPE_COLORS = {
    "hub":              "#F4A300",   # amber — session hubs
    "section_draft":    "#4A90D9",   # blue
    "modification_log": "#27AE60",   # green
    "epistemic_trace":  "#8E44AD",   # purple
    "pdl":              "#16A085",   # teal
    "note":             "#7F8C8D",   # grey
    "reference":        "#BDC3C7",   # light grey
    "other":            "#E67E22",   # orange fallback
}

TYPE_SIZES = {
    "hub":              22,
    "section_draft":    14,
    "modification_log": 12,
    "epistemic_trace":  12,
    "pdl":              11,
    "note":             10,
    "reference":        8,
    "other":            10,
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

FILENAME_PREFIX_RE = re.compile(
    r"^(?:(?:II|III|CFP)_)?(?:SP)?(?P<id>\d+(?:\.\d+)*)"
)
ERA_ID_RE = re.compile(
    r"^(?P<era>(?:II|III|CFP)_)?(?:SP)?(?P<num>\d+(?:\.\d+)*)"
)

def stem_to_id(stem: str) -> str:
    """Normalise a filename stem to its dot-ID prefix (era stripped)."""
    m = FILENAME_PREFIX_RE.match(stem)
    return m.group("id") if m else stem

def stem_to_era_id(s: str):
    """Return (era, numeric_id) tuple from a stem or reference string.
    era is '' for bare artifacts, 'III', 'CFP', etc. for prefixed ones.
    Everything after the numeric code is treated as a description and ignored.
    abc_X.Y.Z and dfg_X.Y.Z are different; X.Y.Z_foo and X.Y.Z_bar are the same.
    """
    m = ERA_ID_RE.match(s.strip())
    if not m:
        return None
    era = (m.group("era") or "").rstrip("_")
    return (era, m.group("num"))

def classify(data: dict, filename: str) -> str:
    dtype = str(data.get("document_type", "") or data.get("artifact_type", "")).lower()
    fname = filename.lower()
    if "section draft" in dtype or "type 12" in dtype:
        return "section_draft"
    if "modification log" in dtype or "modlog" in dtype or "4.2_modificationlogs" in fname:
        return "modification_log"
    if "epistemic" in dtype or "trace" in dtype or "4.7_epistemictraces" in fname:
        return "epistemic_trace"
    if "pdl" in dtype or "pdl" in fname:
        return "pdl"
    if "steering" in dtype or "note" in dtype or "type 11" in dtype or "5.3_notes" in fname:
        return "note"
    if "reference" in fname or "bibliography" in fname or "citations" in fname:
        return "reference"
    return "other"

def extract_chat_ids(data: dict) -> list[str]:
    ids = []
    # Build a lowercase-key lookup for case-insensitive matching (v1/v2 used Title Case)
    lower_keys = {k.lower(): k for k in data.keys()}

    # UUID-style fields — standard snake_case and v1/v2 Title Case variants
    uuid_exact = {"source_chat_id", "chat_id", "upstream_chat_id"}
    uuid_exact_lower = {"source chat id", "chat id", "source_chat_id", "chat_id", "upstream_chat_id"}
    for k_lower, k_orig in lower_keys.items():
        # Exact match (case-insensitive)
        if k_lower in uuid_exact_lower:
            v = str(data[k_orig]).strip()
            if v and v not in ("", "null", "~"):
                ids.append(v)
        # Numbered variants: source_chat_id_1 / source_chat_id_2 (digit suffix)
        # or source_chat_1_id / source_chat_2_id (digit in middle — v1/v2 style)
        elif re.match(r"^(?:source.?chat.?id|chat.?id)_\d+$", k_lower) or \
             re.match(r"^source.?chat.?\d+.?id$", k_lower):
            v = str(data[k_orig]).strip()
            if v and v not in ("", "null", "~"):
                ids.append(v)
    # SID-style field
    sid = data.get("session_id", "")
    if sid:
        sid = str(sid).strip()
        if sid and sid not in ("", "null", "~"):
            ids.append(sid)
    # phase_N_chat_id — used in two-phase modlogs (e.g. 4.2.9)
    for k, v in data.items():
        if re.match(r"^phase\d+_chat_id$", str(k)):
            v = str(v).strip()
            if v and v not in ("", "null", "~"):
                ids.append(v)
    # Extract UUID from claude.ai chat URLs (e.g. source_chat_link: https://claude.ai/chat/<uuid>)
    _uuid_re = re.compile(r"claude\.ai/chat/([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})", re.IGNORECASE)
    for k, v in data.items():
        if "link" in str(k).lower() and isinstance(v, str):
            m = _uuid_re.search(v)
            if m:
                ids.append(m.group(1))
    return list(dict.fromkeys(ids))  # deduplicate while preserving order

def safe_node_id(raw: str) -> str:
    """Make a string safe for use as a vis.js node id."""
    return re.sub(r'[/\\:*?"<>|]', "_", raw)

def flatten_value(v) -> list[str]:
    """Return a list of string values from a frontmatter field."""
    if v is None:
        return []
    if isinstance(v, list):
        out = []
        for item in v:
            if isinstance(item, dict):
                # e.g. source_conversations list of {session: ..., exported_as: ...}
                for vv in item.values():
                    if vv:
                        out.extend(flatten_value(vv))
            else:
                out.extend(flatten_value(item))
        return out
    s = str(v).strip()
    # Split on semicolons (hub script concatenates with ;) or commas (v1/v2 inline lists)
    import re as _fv_re
    parts = [p.strip() for p in _fv_re.split(r"[;,]", s) if p.strip()]
    result = []
    for part in parts:
        # Strip annotation in parens: "CFP_5.3.1 (master work plan)" → "CFP_5.3.1"
        base = re.sub(r"\s*\(.*?\)\s*$", "", part).strip()
        # Strip leading prose words before an ID: "see 4.7.4" → "4.7.4"
        base = re.sub(r"^(?:see|cf\.?|from|ref\.?)\s+", "", base, flags=re.IGNORECASE)
        if base:
            result.append(base)
    return result

# ---------------------------------------------------------------------------
# Build graph
# ---------------------------------------------------------------------------

def build_graph(vault: Path) -> nx.DiGraph:
    G = nx.DiGraph()

    md_files = [
        f for f in vault.rglob("*.md")
        if "_HUBS" not in str(f) and "build_graph" not in str(f)
    ]

    # Map from dot-ID prefix → node id (for resolving reference targets)
    id_to_node: dict[str, str] = {}
    # Map from stem → node id
    stem_to_node: dict[str, str] = {}

    # --- Pass 1: create artifact nodes ---
    for f in md_files:
        text = f.read_text(errors="ignore")
        if not text.startswith("---"):
            continue
        end = text.find("---", 3)
        if end == -1:
            continue
        try:
            data = yaml.safe_load(text[3:end]) or {}
        except Exception:
            continue

        stem = f.stem
        node_id = safe_node_id(stem)
        atype = classify(data, str(f))
        label = data.get("label") or data.get("title") or stem
        # Label: keep era prefix (CFP_, III_) + numeric code; elide trailing name
        _m = re.match(r"^((?:II|III|CFP)_)?((?:SP)?\d+(?:\.\d+)*(?:\.\d+)?)", stem)
        short = ((_m.group(1) or "") + _m.group(2)) if _m else stem
        # Era for filtering
        _era_m = re.match(r"^(II|III|CFP)_", stem)
        era = _era_m.group(1) if _era_m else "v1v2"

        G.add_node(
            node_id,
            label=short,
            full_title=label,
            title=f"{stem}\n{data.get('document_type', atype)}\n{data.get('date_created') or data.get('date') or data.get('created', '')}",
            color=TYPE_COLORS[atype],
            size=TYPE_SIZES[atype],
            node_type=atype,
            stem=stem,
            era=era,
        )
        dot_id = stem_to_id(stem)
        era_key = stem_to_era_id(stem)   # (era, numeric) — unambiguous lookup key
        if era_key:
            id_to_node[era_key] = node_id
        stem_to_node[stem] = node_id

        # --- Add hub nodes for each session ID found ---
        # Collect chat name for tooltip enrichment (v1/v2: "source_chat_name"; v3+: may be absent)
        chat_name_hint = (
            data.get("source_chat_name")
            or data.get("chat_name")
            or data.get("Source chat name")
            or ""
        )
        for chat_id in extract_chat_ids(data):
            hub_id = safe_node_id(f"HUB_{chat_id}")
            if not G.has_node(hub_id):
                # Shorten hub label
                hub_label = chat_id
                if chat_id.startswith("SID-"):
                    hub_label = chat_id[4:]  # drop "SID-"
                elif len(chat_id) > 16:
                    hub_label = chat_id[:8] + "…"
                hub_title = f"Session: {chat_id}"
                if chat_name_hint:
                    hub_title += f"\n{chat_name_hint}"
                G.add_node(
                    hub_id,
                    label=hub_label,
                    title=hub_title,
                    color=TYPE_COLORS["hub"],
                    size=TYPE_SIZES["hub"],
                    node_type="hub",
                    stem=chat_id,
                )
            elif chat_name_hint:
                # Enrich existing hub tooltip if we now have a name
                existing_title = G.nodes[hub_id].get("title", "")
                if chat_name_hint not in existing_title:
                    G.nodes[hub_id]["title"] = existing_title + f"\n{chat_name_hint}"
            G.add_edge(hub_id, node_id, color="#F4A300", width=1, title="session")

    # --- Pass 2: add relational edges ---
    for f in md_files:
        text = f.read_text(errors="ignore")
        if not text.startswith("---"):
            continue
        end = text.find("---", 3)
        if end == -1:
            continue
        try:
            data = yaml.safe_load(text[3:end]) or {}
        except Exception:
            continue

        src_id = safe_node_id(f.stem)
        if not G.has_node(src_id):
            continue

        def _add_rel_edges(field: str, canonical: str):
            """Resolve a relational field and add directed edges."""
            raw = data.get(field)
            if not raw:
                return
            targets = flatten_value(raw)
            for target in targets:
                target_stem = Path(target).stem
                # 1. Exact stem match (most specific)
                target_node = stem_to_node.get(target_stem)
                if not target_node:
                    # 2. (era, numeric) from Path stem — works for file-style refs
                    era_key = stem_to_era_id(target_stem)
                    if era_key:
                        target_node = id_to_node.get(era_key)
                if not target_node:
                    # 3. (era, numeric) from raw target string — handles "X.Y.Z description"
                    #    where Path.stem truncates at the first decimal point
                    era_key = stem_to_era_id(target)
                    if era_key:
                        target_node = id_to_node.get(era_key)
                if target_node and target_node != src_id:
                    if canonical in ("feeds_into", "output_completed"):
                        ecol = "#E74C3C"   # red — output flow
                        G.add_edge(src_id, target_node, color=ecol, width=1.5, title=canonical)
                    elif canonical in ("inputs", "derived_from", "source_file"):
                        ecol = "#3498DB"   # blue — input flow (target feeds into src)
                        G.add_edge(target_node, src_id, color=ecol, width=1.5, title=canonical)
                    elif canonical == "source_guidance":
                        ecol = "#95A5A6"   # grey — guidance
                        G.add_edge(src_id, target_node, color=ecol, width=1.5, title=canonical)
                    else:
                        ecol = "#BDC3C7"   # light grey — lateral
                        G.add_edge(src_id, target_node, color=ecol, width=1.5, title=canonical)

        # Standard CFP/III fields
        for field in REL_FIELDS + REL_FIELDS_NUMBERED:
            _add_rel_edges(field, field)

        # V1/V2 field name variants
        for v1_field, canonical in V1V2_FIELD_MAP.items():
            _add_rel_edges(v1_field, canonical)

    return G

# ---------------------------------------------------------------------------
# Era filtering
# ---------------------------------------------------------------------------

def filter_era(G: nx.DiGraph, era: str) -> nx.DiGraph:
    """Return a subgraph containing only artifacts from `era` and the hub nodes
    that connect to at least one artifact in that era.
    era values: 'v1v2', 'III', 'CFP'
    """
    # Artifact nodes in this era
    art_nodes = {n for n in G.nodes if G.nodes[n].get("era") == era}
    # Hub nodes with at least one edge to an artifact in this era
    hub_nodes = {
        n for n in G.nodes
        if G.nodes[n].get("node_type") == "hub"
        and any(nbr in art_nodes for nbr in G.successors(n))
    }
    keep = art_nodes | hub_nodes
    return G.subgraph(keep).copy()

# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

def render(G: nx.DiGraph, output: Path):
    net = Network(
        height="95vh",
        width="100%",
        bgcolor="#1a1a2e",
        font_color="#e0e0e0",
        directed=True,
        notebook=False,
    )
    net.from_nx(G)

    # Physics: Barnes-Hut for performance with ~150 nodes
    net.set_options("""
    {
      "nodes": {
        "borderWidth": 1,
        "borderWidthSelected": 3,
        "font": { "size": 11, "face": "monospace" }
      },
      "edges": {
        "arrows": { "to": { "enabled": true, "scaleFactor": 0.5 } },
        "smooth": { "type": "dynamic" }
      },
      "physics": {
        "barnesHut": {
          "gravitationalConstant": -8000,
          "centralGravity": 0.3,
          "springLength": 120,
          "springConstant": 0.04,
          "damping": 0.09
        },
        "maxVelocity": 50,
        "minVelocity": 0.75,
        "stabilization": { "iterations": 200 }
      },
      "interaction": {
        "hover": true,
        "tooltipDelay": 200,
        "navigationButtons": true,
        "keyboard": true
      }
    }
    """)

    net.write_html(str(output))
    print(f"Graph written to: {output}")
    print(f"Nodes: {G.number_of_nodes()}  Edges: {G.number_of_edges()}")

    # Node type summary
    from collections import Counter
    counts = Counter(G.nodes[n]["node_type"] for n in G.nodes)
    for t, c in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {t:20s} {c}")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build JPEP graph visualization")
    parser.add_argument("--vault", default=str(_default_vault), help="Path to Canonical_MD vault")
    parser.add_argument("--output", default=None, help="Output HTML file (default: <vault>/_GRAPHS/jpep_graph.html)")
    args = parser.parse_args()

    vault = Path(args.vault).resolve()
    output = Path(args.output) if args.output else vault / "_GRAPHS" / "jpep_graph.html"
    output.parent.mkdir(parents=True, exist_ok=True)

    print(f"Scanning: {vault}")
    G = build_graph(vault)
    render(G, output)

    # Era-specific graphs
    graphs_dir = output.parent
    for era, fname in [("v1v2", "jpep_graph_v1v2.html"),
                       ("III",  "jpep_graph_III.html"),
                       ("CFP",  "jpep_graph_CFP.html")]:
        print(f"\n--- Era: {era} ---")
        G_era = filter_era(G, era)
        render(G_era, graphs_dir / fname)
