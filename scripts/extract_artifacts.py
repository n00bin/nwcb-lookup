#!/usr/bin/env python3
"""Extract the inline artifacts array from js/artifacts-page.js into
data/artifacts.json with a unified gear-friendly schema.

Each artifact gets:
  - normalized field names (itemLevel -> item_level)
  - stats array converted to ratingStats dict (matches gear.json shape)
  - default allowedClasses (all 9 — most artifacts are universal)
  - empty percentStats / abilityBonuses / equipBonuses for now
  - sequential id starting at 1
  - all the rich gameplay fields kept (type, power, debuff, cooldown,
    set, source, image)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JS = ROOT / "js" / "artifacts-page.js"
OUT = ROOT.parent / "data" / "artifacts.json"

ALL_CLASSES = ["Barbarian", "Bard", "Cleric", "Fighter", "Paladin",
               "Ranger", "Rogue", "Warlock", "Wizard"]


def parse_artifacts(text: str):
    # Find the var artifacts = [ ... ]; block
    start = text.index("var artifacts = [")
    # walk forward bracket-balanced to find the matching ];
    i = text.index("[", start)
    depth = 0
    end = i
    while end < len(text):
        ch = text[end]
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                break
        end += 1
    block = text[i:end + 1]

    # Extract each top-level { ... } entry.
    # Each entry is on its own line — easy to grep.
    entries = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("{") or "name:" not in line:
            continue
        # strip trailing comma if present
        if line.endswith(","):
            line = line[:-1]
        # Convert JS object literal -> JSON.
        # Quote bare keys: name:, type:, power:, debuff:, cooldown:, set:,
        # source:, image:, itemLevel:, combinedRating:, stats:
        # The inner stats list is already JSON-quoted ("stat", "value").
        json_line = re.sub(
            r'(\b)(name|type|power|debuff|cooldown|set|source|image|itemLevel|combinedRating|stats)(\s*:)',
            r'\1"\2"\3',
            line,
        )
        try:
            entry = json.loads(json_line)
        except json.JSONDecodeError as e:
            print(f"  PARSE ERR: {e}\n    line: {line[:120]}...")
            continue
        entries.append(entry)
    return entries


def normalize(entry, idx):
    stats_list = entry.get("stats", [])
    rating_stats = {}
    for s in stats_list:
        rating_stats[s["stat"]] = s["value"]
    return {
        "id":             idx,
        "name":           entry["name"],
        "slot":           "Artifact",
        "type":           entry.get("type", ""),
        "item_level":     entry.get("itemLevel", 600),
        "combinedRating": entry.get("combinedRating", 0),
        "allowedClasses": list(ALL_CLASSES),  # default; refine later if any are class-locked
        "ratingStats":    rating_stats,
        "percentStats":   {},
        "abilityBonuses": {},
        "equipBonuses":   [],
        "power":          entry.get("power", ""),
        "debuff":         entry.get("debuff", ""),
        "cooldown":       entry.get("cooldown", 60),
        "set":            entry.get("set", "None"),
        "source":         entry.get("source", ""),
        "image":          entry.get("image", ""),
    }


def main():
    txt = JS.read_text(encoding="utf-8")
    raw = parse_artifacts(txt)
    print(f"Parsed {len(raw)} artifacts from artifacts-page.js")

    normalized = [normalize(e, i + 1) for i, e in enumerate(raw)]

    OUT.write_text(
        json.dumps(normalized, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    print(f"Wrote {len(normalized)} entries to {OUT.relative_to(ROOT.parent)}")

    # Sanity check
    print("\nSample first entry:")
    print(json.dumps(normalized[0], indent=2)[:500])


if __name__ == "__main__":
    main()
