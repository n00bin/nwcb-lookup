#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKING = ROOT / "gear_batch1_items.json"

NEW_ITEMS = [
    # Graveveil rings continued
    {"name": "Graveveil Coil of Silence", "slot": "Ring", "item_level": 4050, "ratingStats": {"Accuracy": 7898, "Critical Strike": 7290}, "percentStats": {"Action Point Gain": 1.5}, "combinedRating": 3240, "equipBonuses": [{"name": "Heroic Tactics", "description": "When your Stamina is over 75%, your Power is increased by 12,450."}], "set": "Doomvault Remains", "setSize": 8, "source": "Doomvault Remains"},
    {"name": "Graveveil Band of Unlife", "slot": "Ring", "item_level": 4050, "ratingStats": {"Critical Strike": 4252, "Forte": 5468}, "percentStats": {"Recharge Speed": 1.5}, "combinedRating": 3240, "equipBonuses": [{"name": "The Ol' Switcheroo", "description": "+11,325 Outgoing Healing, +3,775 Defense."}], "set": "Doomvault Remains", "setSize": 8, "source": "Doomvault Remains"},
    {"name": "Graveveil Hoop of Decay", "slot": "Ring", "item_level": 4050, "ratingStats": {"Defense": 4252, "Awareness": 4860}, "percentStats": {"Stamina Regeneration": 1.5}, "combinedRating": 3240, "equipBonuses": [{"name": "Survivor's Reflexes", "description": "Gain up to 12,450 Awareness based on your missing health. The max bonus is achieved at 25% or less health."}], "set": "Doomvault Remains", "setSize": 8, "source": "Doomvault Remains"},

    # Mark of the... clothing — Tyrators IL 2600
    {"name": "Mark of the Convert", "slot": "Shirt", "item_level": 2600, "ratingStats": {"Defense": 819, "Critical Avoidance": 1716, "Deflect Severity": 1756}, "percentStats": {"Stamina Regeneration": 1.5}, "combinedRating": 2340, "equipBonuses": [{"name": "Precision Tactics", "description": "When your Stamina is over 75%, your Critical Avoidance is increased by 7,275."}], "set": "Enchanted Awareness", "setSize": 2, "notes": "Glorious Undead Defence Shirt"},
    {"name": "Mark of the Adept", "slot": "Shirt", "item_level": 2600, "ratingStats": {"Critical Severity": 1404, "Deflection": 1755, "Outgoing Healing": 1248}, "percentStats": {"Stamina Regeneration": 1.5}, "combinedRating": 2340, "equipBonuses": [{"name": "Challenger's Forte", "description": "When in combat with 3 or more enemies, your Forte is increased by 1,455 every 2 seconds. Every 2 seconds you are in combat with 1 or less enemies, lose 1 stack. Max Stacks: 5 — 7,275 Forte."}], "set": "Enchanted Forte", "setSize": 2, "notes": "Glorious Undead Healer Shirt"},
    {"name": "Mark of the Fledgling", "slot": "Shirt", "item_level": 2600, "ratingStats": {"Critical Strike": 1872, "Incoming Healing": 1404, "Outgoing Healing": 936}, "percentStats": {"Stamina Regeneration": 1.5}, "combinedRating": 2340, "equipBonuses": [{"name": "Challenger's Forte", "description": "When in combat with 3 or more enemies, your Forte is increased by 1,455 every 2 seconds. Every 2 seconds you are in combat with 1 or less enemies, lose 1 stack. Max Stacks: 5 — 7,275 Forte."}], "set": "Enchanted Forte", "setSize": 2, "notes": "Glorious Undead Healer Shirt variant"},
]


def main():
    items = json.loads(WORKING.read_text(encoding="utf-8"))
    existing_names = {it["name"] for it in items}
    added = 0
    for new in NEW_ITEMS:
        if new["name"] in existing_names:
            continue
        items.append(new)
        existing_names.add(new["name"])
        added += 1
    WORKING.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Appended {added} new items. Working file now has {len(items)} total.")


if __name__ == "__main__":
    main()
