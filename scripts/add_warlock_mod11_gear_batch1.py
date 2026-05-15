"""Module 11 Ascended Weapon Sets — Warlock — batch 1 of N.
Sets covered: Mirage, Aboleth, Fey, Lifeforged.
Each set has Pact Blade (Main Hand) + Grimoire (Off Hand) at 4 IL tiers (350/500/650/800).
Source: The Cloaked Ascendancy campaign vendor (River District) — Module 11.
"""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)

INTAKE = "Module 11 Ascended Weapon Sets of the Warlock — screenshot intake 2026-05-14."

def add(name, slot, il, rs, cr, source, set_name, equip):
    global max_id
    max_id += 1
    data.append({
        "id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name, "setSize": 2,
        "source": source, "percentStats": {}, "abilityBonuses": {},
        "allowedClasses": ["Warlock"], "notes": INTAKE
    })

TIERS = [
    ("Uncommon",  350, 131, 262, 131, 315),
    ("Rare",      500, 188, 375, 188, 450),
    ("Epic",      650, 244, 488, 244, 585),
    ("Legendary", 800, 300, 600, 300, 720),
]

SETS = [
    # set_name, source_loc, pact_eb, grim_eb
    ("Mirage", "The Cloaked Ascendancy (Module 11)",
     [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Mirage", "pieces": 2,
       "description": "2 of Set: When you use an encounter power, you become a Master of Illusion for 10 seconds. As a Master of Illusion you summon an illusion of yourself to fight for you, attacking your enemies. The summoned illusion deals up to 4% more damage, which increases by 10% against enemies with Shields and Temp HP. You can only be a Master of Illusion once every 30 seconds."}]),
    ("Aboleth", "The Cloaked Ascendancy (Module 11)",
     [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Aboleth", "pieces": 2,
       "description": "2 of Set: When you use an encounter power, you will become Aboleth Influenced, which increases your Outgoing Damage by 4% and grants you a random buff for 10 seconds. Relentless: increases Critical Strike by 2500. Tainted Attack: enemies you attack take additional damage over time. Impeding Death: enemies you attack will explode on death, doing damage to other foes. You can only be Aboleth-influenced once every 30 seconds."}]),
    ("Fey", "The Cloaked Ascendancy (Module 11)",
     [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Fey", "pieces": 2,
       "description": "2 of Set: When you use an encounter power, you become Fey-Touched, which restores 10% of your AP, as well as increases your Base Damage Boost by 3% and Overall Outgoing Healing by 6% for 10 seconds. You can only be Fey-Touched once every 30 seconds."}]),
    ("Lifeforged", "The Cloaked Ascendancy (Module 11)",
     [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Lifeforged", "pieces": 2,
       "description": "2 of Set: When you use an encounter power, you become Fortified, which increases your Defense by 5% and adds 10% of your Defense to your Power for 10 seconds. You can only be Fortified once every 30 seconds."}]),
]

for set_name, source, eb in SETS:
    for rarity, il, acc, ca, crit, cr in TIERS:
        add(f"{set_name} Pact Blade ({rarity})", "Main Hand", il,
            {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr,
            source, set_name, eb)
        add(f"{set_name} Grimoire ({rarity})", "Off Hand", il,
            {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr,
            source, set_name, eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
