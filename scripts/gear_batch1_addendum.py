#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKING = ROOT / "gear_batch1_items.json"

NEW_ITEMS = [
    {"name": "Sabatons of the Vital Sigil", "slot": "Feet", "item_level": 4700, "allowedClasses": ["Paladin", "Cleric"], "ratingStats": {"Power": 1974, "Outgoing Healing": 2538}, "combinedRating": 4230, "equipBonuses": [{"name": "Sustained Vitality", "description": "Per 5s in combat: +0.5% OH and +0.6% Forte. Max 6 stacks (3% OH, 3.6% Forte)"}], "set": "Dread March Armor", "setSize": 2, "source": "Soul Harvest (Advanced)"},
    {"name": "Vambraces of the Vital Sigil", "slot": "Arms", "item_level": 4700, "allowedClasses": ["Paladin", "Cleric"], "ratingStats": {"Forte": 3490, "Outgoing Healing": 2538}, "combinedRating": 4230, "equipBonuses": [{"name": "Divine Ascendance", "description": "Divinity maximum increased by 20%"}], "set": "Dread March Armor", "setSize": 2, "source": "Soul Harvest (Advanced)"},
    {"name": "Breastplate of the Vital Sigil", "slot": "Armor", "item_level": 4700, "allowedClasses": ["Paladin", "Cleric"], "ratingStats": {"Forte": 3490, "Outgoing Healing": 2538}, "combinedRating": 4230, "equipBonuses": [{"name": "Protective Embrace", "description": "Heal ally grants them +1% Defense for 6s. Max 5 stacks (5%)"}], "set": "Dread March Armor", "setSize": 2, "source": "Soul Harvest (Advanced)"},
    {"name": "Crown of the Iron Bulwark", "slot": "Head", "item_level": 4700, "allowedClasses": ["Paladin", "Barbarian", "Fighter"], "ratingStats": {"Defense": 2221, "Awareness": 3102}, "combinedRating": 4230, "equipBonuses": [{"name": "Shared Resilience", "description": "On encounter use: 40% chance for self + lowest-HP ally in 25' to gain +5% Forte and +3.5% Defense 8s (15s cd)"}], "set": "Dread March Armor", "setSize": 2, "source": "Soul Harvest (Advanced)"},
    {"name": "Cuirass of the Iron Bulwark", "slot": "Armor", "item_level": 4700, "allowedClasses": ["Paladin", "Barbarian", "Fighter"], "ratingStats": {"Awareness": 2538, "Critical Avoidance": 4265}, "combinedRating": 4230, "equipBonuses": [{"name": "Reactive Shielding", "description": "On dmg > 15% MaxHP: 20' aura gives allies +1% Defense and +2.5% IH 8s (15s cd)"}], "set": "Dread March Armor", "setSize": 2, "source": "Soul Harvest (Advanced)"},
    {"name": "Vambraces of the Iron Bulwark", "slot": "Arms", "item_level": 4700, "allowedClasses": ["Paladin", "Barbarian", "Fighter"], "ratingStats": {"Awareness": 2538, "Critical Avoidance": 4265}, "combinedRating": 4230, "equipBonuses": [{"name": "Tactical Insight", "description": "Per 6s in combat: +0.4% Awareness, +0.1% Power to allies in 20'. Max 8 (3.2% / 0.8% per ally)"}], "set": "Dread March Armor", "setSize": 2, "source": "Soul Harvest (Advanced)"},
    {"name": "Aegis of the Condemned · IL 4800", "displayName": "Aegis of the Condemned", "slot": "Off Hand", "subSlot": "Shield", "item_level": 4800, "allowedClasses": ["Paladin"], "ratingStats": {"Critical Strike": 2880, "Awareness": 1920, "Outgoing Healing": 1920}, "combinedRating": 4320, "equipBonuses": [{"name": "Impending Doom set bonus", "description": "Set Impending Doom (0/2) — Charges by daily/encounter/in-combat. Unleashed: Tank −1% Incoming dmg, Heal −1% OH; +x% Forte; +x% Defense"}], "set": "Impending Doom", "setSize": 2, "source": "Soul Harvest (Advanced)", "tier": "Advanced"},
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
