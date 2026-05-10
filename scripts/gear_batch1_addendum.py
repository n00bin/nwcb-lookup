#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORKING = ROOT / "gear_batch1_items.json"

NEW_ITEMS = [
    {"name": "Veil of the Last Oath", "slot": "Head", "item_level": 3550, "ratingStats": {"Critical Severity": 1917, "Control Resist": 1598, "Outgoing Healing": 1704}, "combinedRating": 3195, "equipBonuses": [{"name": "Medic's Grace", "description": "For every 5 seconds you are in combat, you gain 990 Critical Severity and 0.5% Outgoing Healing. Max Stacks: 5 — 4,950 Critical Severity and 2.5% Outgoing Healing."}], "set": "Vanguard's Vow Armor", "setSize": 2},
    {"name": "Raiment of the Bonekeeper", "slot": "Armor", "item_level": 3550, "ratingStats": {"Critical Strike": 2556, "Incoming Healing": 1917, "Outgoing Healing": 1278}, "combinedRating": 3195, "equipBonuses": [{"name": "Thayan Harmony", "description": "You gain 4,950 Critical Strike. Teammates who are 25' or closer to you gain 1% Defense."}], "set": "Vanguard's Vow Armor", "setSize": 2},
    {"name": "Helm of the Eternal Gaze", "slot": "Head", "item_level": 3550, "ratingStats": {"Defense": 1118, "Critical Avoidance": 2343, "Deflect Severity": 2396}, "combinedRating": 3195, "equipBonuses": [{"name": "Occult Defence", "description": "You gain 9,925 Defence. And when in Thay you gain -1.2% Incoming Damage."}], "set": "Vanguard's Vow Armor", "setSize": 2},
    {"name": "Sabatons of the Silent Passage", "slot": "Feet", "item_level": 3550, "ratingStats": {"Critical Strike": 1917, "Defense": 1118, "Forte": 1917}, "combinedRating": 3195, "equipBonuses": [{"name": "Challenger's Recovery", "description": "When in combat with only 1 enemy, your Recharge Speed is increased by 0.2% every 2 seconds. Every 2 seconds you are in combat with 4 or more enemies, lose 1 stack. Max Stacks: 10 — 2% Recharge Speed."}], "set": "Vanguard's Vow Armor", "setSize": 2},
    {"name": "Gauntlets of the Anointed", "slot": "Arms", "item_level": 3550, "ratingStats": {"Critical Severity": 1917, "Deflection": 2396, "Outgoing Healing": 1704}, "combinedRating": 3195, "equipBonuses": [{"name": "Controlled Divinity", "description": "Gain a stack of 0.6% Divinity/Performance/Soulweave regeneration for 15 seconds when you heal an ally, lose a stack when you are struck. Max Stacks: 10 — 6% Regen."}], "set": "Vanguard's Vow Armor", "setSize": 2},
    {"name": "Bulwark of the Deathless Tyrant", "slot": "Armor", "item_level": 3550, "ratingStats": {"Combat Advantage": 1278, "Forte": 1438, "Incoming Healing": 2556}, "combinedRating": 3195, "equipBonuses": [{"name": "Overwhelming Parry", "description": "When in combat with multiple enemies, gain 9,925 Awareness. This bonus is at full power when in combat with 7 or more enemies."}], "set": "Vanguard's Vow Armor", "setSize": 2},
    {"name": "Grasp of the Silent Sentinel", "slot": "Arms", "item_level": 3550, "ratingStats": {"Defense": 1491, "Critical Avoidance": 1757, "Combat Resistance": 1598}, "combinedRating": 3195, "equipBonuses": [{"name": "Enveloped Aegis", "description": "When in combat with 3 or more enemies, your Deflect Severity is increased by 1,983 every 2 seconds. Every 2 seconds you are in combat with 1 or fewer enemies, lose 1 stack. Max Stacks: 5 — 9,925 Deflect Severity."}], "set": "Vanguard's Vow Armor", "setSize": 2},
    {"name": "Stalkers of the Undying Legions", "slot": "Feet", "item_level": 3550, "ratingStats": {"Accuracy": 2077, "Awareness": 1704, "Deflection": 2396}, "combinedRating": 3195, "equipBonuses": [{"name": "Rising Reflexes", "description": "For every 5 seconds you are in combat, you gain 992 Deflect and Critical Avoidance. Max Stacks: 5 — 4,962 Deflect and Critical Avoidance."}], "set": "Vanguard's Vow Armor", "setSize": 2},
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
