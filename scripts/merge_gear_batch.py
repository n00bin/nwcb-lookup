#!/usr/bin/env python3
"""Merge a batch of new gear entries into data/gear.json.

Reads scripts/gear_batch1_items.json (structured intake from screenshots),
matches each entry against the existing gear.json by name, and either:
  - Updates an existing entry (replacing stats with fresh values), or
  - Adds a new entry with the next available id.

Variants of items that share a display name (e.g. multiple
"Arcane Conduit Seal" with different equipBonus) are stored under
their fully-qualified name (e.g. "Arcane Conduit Seal — Pressured Muse")
and can use displayName for UI rendering.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEAR_PATH = ROOT / "data" / "gear.json"
BATCH_PATH = Path(__file__).resolve().parent / "gear_batch1_items.json"


def main():
    gear = json.loads(GEAR_PATH.read_text(encoding="utf-8"))
    batch = json.loads(BATCH_PATH.read_text(encoding="utf-8"))

    # Build index by name
    by_name = {item["name"]: i for i, item in enumerate(gear)}
    next_id = max((g.get("id", 0) for g in gear), default=0) + 1

    added, updated = [], []
    for entry in batch:
        name = entry["name"]
        # Required schema defaults
        entry.setdefault("ratingStats", {})
        entry.setdefault("percentStats", {})
        entry.setdefault("abilityBonuses", {})
        entry.setdefault("equipBonuses", [])
        entry.setdefault("notes", "")

        if name in by_name:
            idx = by_name[name]
            entry["id"] = gear[idx].get("id")
            gear[idx] = entry
            updated.append(name)
        else:
            entry["id"] = next_id
            next_id += 1
            gear.append(entry)
            added.append(name)

    GEAR_PATH.write_text(json.dumps(gear, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Merge complete:")
    print(f"  Added:   {len(added)}")
    for n in added: print(f"    + {n}")
    print(f"  Updated: {len(updated)}")
    for n in updated: print(f"    ~ {n}")
    print(f"  Total in gear.json: {len(gear)}")


if __name__ == "__main__":
    main()
