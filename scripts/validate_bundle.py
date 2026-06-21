#!/usr/bin/env python3
"""Validate the plugin marketplace bundle.

Runs in CI and locally (no third-party deps). Checks:
  1. marketplace.json is valid JSON with the required shape.
  2. Every declared skill path exists and has a SKILL.md.
  3. Every SKILL.md has YAML frontmatter with non-empty `name` and `description`.
  4. Each skill's frontmatter `name` matches its directory name.
  5. No private/local-only files are present (private-defaults.md, _planning/).

Exit code 0 = all good; non-zero = one or more failures (printed).
"""
from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def parse_frontmatter(text: str) -> dict[str, str]:
    """Minimal YAML frontmatter parser for flat `key: value` pairs."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end].strip("\n")
    out: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            out[key.strip()] = val.strip()
    return out


def check_marketplace() -> list[str]:
    path = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
    if not os.path.isfile(path):
        fail(".claude-plugin/marketplace.json is missing")
        return []
    try:
        data = json.load(open(path))
    except json.JSONDecodeError as e:
        fail(f"marketplace.json is invalid JSON: {e}")
        return []

    for field in ("name", "plugins"):
        if field not in data:
            fail(f"marketplace.json missing top-level '{field}'")

    skill_paths: list[str] = []
    for i, plugin in enumerate(data.get("plugins", [])):
        if not plugin.get("name"):
            fail(f"plugin[{i}] missing 'name'")
        if not plugin.get("description"):
            fail(f"plugin[{i}] ({plugin.get('name','?')}) missing 'description'")
        for sp in plugin.get("skills", []):
            skill_paths.append(sp)
    return skill_paths


def check_skill(rel_path: str) -> None:
    skill_dir = os.path.join(ROOT, rel_path)
    if not os.path.isdir(skill_dir):
        fail(f"declared skill path does not exist: {rel_path}")
        return
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(skill_md):
        fail(f"{rel_path} has no SKILL.md")
        return
    fm = parse_frontmatter(open(skill_md, encoding="utf-8").read())
    if not fm.get("name"):
        fail(f"{rel_path}/SKILL.md frontmatter missing 'name'")
    if not fm.get("description"):
        fail(f"{rel_path}/SKILL.md frontmatter missing 'description'")
    expected = os.path.basename(rel_path.rstrip("/"))
    if fm.get("name") and fm["name"] != expected:
        fail(f"{rel_path}/SKILL.md name '{fm['name']}' != directory '{expected}'")


def check_no_private_files() -> None:
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if ".git" in dirpath.split(os.sep):
            continue
        if "_planning" in dirnames:
            fail(f"local-only '_planning/' present at {os.path.relpath(dirpath, ROOT)}")
        for fn in filenames:
            if fn == "private-defaults.md":
                rel = os.path.relpath(os.path.join(dirpath, fn), ROOT)
                fail(f"private file must not be published: {rel}")


def main() -> int:
    skill_paths = check_marketplace()
    if not skill_paths:
        fail("no skills declared in marketplace.json")
    for sp in skill_paths:
        check_skill(sp)
    check_no_private_files()

    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK — {len(skill_paths)} skill(s) validated, no private files present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
