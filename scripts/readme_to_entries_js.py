#!/usr/bin/env python3

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
OUTPUT = ROOT / "docs" / "entries.js"

ENTRY_RE = re.compile(r"^- \[(?P<name>[^\]]+)\]\((?P<url>[^)]+)\)(?P<after>.*)$")
WRAPPED_BADGE_RE = re.compile(
    r"\[!\[[^\]]*\]\((?P<badge>[^)]+)\)\]\((?P<badge_link>[^)]+)\)"
)
PLAIN_BADGE_RE = re.compile(r"!\[[^\]]*\]\((?P<badge>[^)]+)\)")

TAG_RE = re.compile(r"`([^`]+)`")
PREFIX = "window.AGENT_ENV_ENTRIES = "

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


def load_existing_entries() -> dict[tuple[str, str], dict]:
    if not OUTPUT.exists():
        return {}

    raw = OUTPUT.read_text().strip()
    if not raw.startswith(PREFIX) or not raw.endswith(";"):
        return {}

    payload = raw[len(PREFIX) : -1].strip()

    try:
        entries = json.loads(payload)
    except json.JSONDecodeError:
        return {}

    return {
        (entry.get("name", ""), entry.get("url", "")): entry
        for entry in entries
    }


def parse_entries() -> list[dict]:
    current_section = None
    lines = README.read_text().splitlines()
    use_h3_sections = any(line.startswith("### ") for line in lines)
    existing_entries = load_existing_entries()
    entries = []

    for raw_line in lines:
        line = raw_line.rstrip()

        if line.startswith("### "):
            if use_h3_sections:
                current_section = line[4:].strip()
            continue

        if line.startswith("## "):
            if use_h3_sections:
                current_section = None
            else:
                current_section = line[3:].strip()
            continue

        if not current_section or current_section in SKIP_SECTIONS:
            continue

        match = ENTRY_RE.match(line)
        if not match:
            continue

        after = match.group("after")
        if " - " not in after:
            continue

        prefix, rest = after.split(" - ", 1)

        wrapped_badge = WRAPPED_BADGE_RE.search(prefix)
        plain_badge = PLAIN_BADGE_RE.search(prefix)
        badge = None
        if wrapped_badge:
            badge = wrapped_badge.group("badge")
        elif plain_badge:
            badge = plain_badge.group("badge")

        if " Tags: " in rest:
            description, tag_blob = rest.rsplit(" Tags: ", 1)
            tags = TAG_RE.findall(tag_blob)
        else:
            description = rest
            existing_entry = existing_entries.get(
                (match.group("name"), match.group("url")),
                {},
            )
            tags = existing_entry.get("tags", [])

        entries.append(
            {
                "name": match.group("name"),
                "url": match.group("url"),
                "badge": badge,
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
