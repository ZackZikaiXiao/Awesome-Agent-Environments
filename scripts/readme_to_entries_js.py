#!/usr/bin/env python3

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
OUTPUT = ROOT / "docs" / "entries.js"

ENTRY_RE = re.compile(
    r"^- \[(?P<name>[^\]]+)\]\((?P<url>[^)]+)\)"
    r"(?: !\[stars\]\((?P<badge>[^)]+)\))?"
    r" - (?P<rest>.+)$"
)

TAG_RE = re.compile(r"`([^`]+)`")

SKIP_SECTIONS = {
    "Contents",
    "Scope",
    "Taxonomy",
    "Contributing",
}


def anchorize(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug


def parse_entries() -> list[dict]:
    current_section = None
    entries = []

    for raw_line in README.read_text().splitlines():
        line = raw_line.rstrip()

        if line.startswith("## "):
            current_section = line[3:].strip()
            continue

        if not current_section or current_section in SKIP_SECTIONS:
            continue

        match = ENTRY_RE.match(line)
        if not match:
            continue

        rest = match.group("rest")
        if " Tags: " in rest:
            description, tag_blob = rest.rsplit(" Tags: ", 1)
            tags = TAG_RE.findall(tag_blob)
        else:
            description = rest
            tags = []

        entries.append(
            {
                "name": match.group("name"),
                "url": match.group("url"),
                "badge": match.group("badge"),
                "description": description.strip(),
                "tags": tags,
                "section": current_section,
                "section_anchor": anchorize(current_section),
            }
        )

    return entries


def main() -> None:
    entries = parse_entries()
    payload = "window.AGENT_ENV_ENTRIES = " + json.dumps(
        entries,
        ensure_ascii=False,
        indent=2,
    ) + ";\n"
    OUTPUT.write_text(payload)
    print(f"Wrote {len(entries)} entries to {OUTPUT}")


if __name__ == "__main__":
    main()
