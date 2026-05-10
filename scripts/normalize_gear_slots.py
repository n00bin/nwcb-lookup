#!/usr/bin/env python3
"""Normalize gear.json slot values and dedupe duplicate-name entries.

Fixes:
1. Slot 'Pant' -> 'Pants' (NW uses 'Pants' consistently)
2. Slot 'Waist' -> 'Belt' (NW uses 'Belt' for the belt slot)
3. For items with duplicate 'name' values, keep the entry with the most
   complete data (most ratingStats keys + has equipBonuses) and drop the rest.
"""
import json
from pathlib import Path

GEAR_PATH = Path(__file__).resolve().parents[2] / "data" / "gear.json"


def completeness_score(item):
    """Higher score = more complete entry. Used to pick the winner among duplicates."""
    s = 0
    s += len(item.get("ratingStats") or {})
    s += len(item.get("percentStats") or {})
    s += len(item.get("equipBonuses") or []) * 3
    s += 1 if item.get("setBonus") else 0
    s += 1 if item.get("source") else 0
    s += 1 if item.get("item_level") else 0  # IL > 0
    s += 1 if item.get("combinedRating") else 0
    return s


def main():
    gear = json.loads(GEAR_PATH.read_text(encoding="utf-8"))
    original_count = len(gear)

    # Step 1: normalize slot names
    slot_renames = {"Pant": "Pants", "Waist": "Belt"}
    renamed = 0
    for g in gear:
        s = g.get("slot")
        if s in slot_renames:
            g["slot"] = slot_renames[s]
            renamed += 1

    # Step 2: dedup by name — keep the most complete entry per name
    by_name = {}
    for g in gear:
        n = g.get("name")
        if not n:
            continue
        if n not in by_name or completeness_score(g) > completeness_score(by_name[n]):
            by_name[n] = g

    deduped = list(by_name.values())
    dropped = original_count - len(deduped)

    GEAR_PATH.write_text(json.dumps(deduped, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Slot renames applied:        {renamed}")
    print(f"Duplicate entries dropped:   {dropped}")
    print(f"Final entry count: {original_count} -> {len(deduped)}")


if __name__ == "__main__":
    main()
