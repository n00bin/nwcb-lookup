#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKING = ROOT / "gear_batch1_items.json"

NEW_ITEMS = [
    # Paladin Main Hand — Blood Bargain set (paired with Ebon Crusader's Aegis)
    {"name": "Oathbreaker's Judgment", "slot": "Main Hand", "subSlot": "Blade", "item_level": 4000, "allowedClasses": ["Paladin"], "weaponDamage": 100, "ratingStats": {"Awareness": 2640, "Forte": 2430}, "combinedRating": 3600, "equipBonuses": [{"name": "Blood Bargain Equip", "description": "Whenever you are struck by a Critical Strike, you have a 10% chance to increase your Critical Avoidance by 10% and gain 5% Power for 10 seconds."}], "set": "Blood Bargain", "setSize": 2, "setBonus": "While in Thay, your Movement Speed is increased by 12% and your Forte is increased by 8%.", "setPartners": ["Ebon Crusader's Aegis"], "notes": "Blade, Weapon"},

    # Bloodwoven enchanted clothing — Shackles of Divinity (IL 3,150)
    {"name": "Bloodwoven Brands", "slot": "Shirt", "item_level": 3150, "ratingStats": {"Defense": 1323, "Critical Avoidance": 1701, "Combat Resistance": 1418, "Control Bonus": 1418}, "combinedRating": 2835, "equipBonuses": [{"name": "Warden's Defense", "description": "Whenever you are damaged for more than 15% of your Maximum Hit Points in a single blow, you gain 3% Defense for 10 seconds."}], "set": "Enchanted Awareness", "setSize": 2, "notes": "Defense Shirt"},
    {"name": "Bloodwoven Symbols", "slot": "Shirt", "item_level": 3150, "ratingStats": {"Critical Strike": 1701, "Forte": 1701, "Outgoing Healing": 1134}, "combinedRating": 2835, "equipBonuses": [{"name": "Medic's Haste", "description": "Whenever you heal an ally you have a chance to gain +3% Recharge speed for 5 seconds. (7 second cooldown)"}], "set": "Enchanted Healing", "setSize": 2, "notes": "Healer Shirt"},
    {"name": "Bloodwoven Signs", "slot": "Shirt", "item_level": 3150, "ratingStats": {"Combat Advantage": 1512, "Critical Severity": 2268, "Awareness": 1134}, "combinedRating": 2835, "equipBonuses": [{"name": "Occult Advantage", "description": "+5% Combat Advantage, -5% Accuracy."}], "set": "Enchanted Advantage", "setSize": 2, "notes": "Offense Shirt"},
    {"name": "Bloodwoven Sigils", "slot": "Pants", "item_level": 3150, "ratingStats": {"Combat Advantage": 1134, "Critical Strike": 2268, "Defense": 992}, "combinedRating": 2835, "equipBonuses": [{"name": "Reckless Advantage", "description": "Whenever you deal damage to an enemy, gain a stack of Reckless Advantage, increasing your Combat Advantage by 2% but decreasing your Critical Avoidance by 1.5% for 5 seconds. (Max 3 stacks)"}], "set": "Enchanted Advantage", "setSize": 2, "notes": "Offense Pants (paired with Bloodwoven Signs)"},
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
