#!/usr/bin/env python3
from pathlib import Path

def has_yaml_frontmatter(text: str) -> bool:
    if not text.startswith("---"):
        return False
    # find closing frontmatter delimiter on its own line
    end = text.find("\n---", 3)
    return end != -1

def main(root: str = ".") -> None:
    root_path = Path(root).resolve()
    missing = []

    for p in root_path.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8")
        except Exception:
            missing.append(p)
            continue

        if not has_yaml_frontmatter(txt):
            missing.append(p)

    print(f"Scanned: {root_path}")
    print(f"Markdown files without YAML frontmatter: {len(missing)}\n")
    for p in sorted(missing):
        print(p)

if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
