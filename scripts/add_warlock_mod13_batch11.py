"""Mod 13 Lost City of Omu — Dinohide armor finish + Masterwork III Stronghold weapons."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name=None, classes=None, equip=None, set_size=4, notes=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": {}, "abilityBonuses": {},
        "notes": notes or INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

# Dinohide armor — remainder pieces (Raid Viatus + Assault full set)
src_dh = "Masterwork Crafting (Module 11 The Lost City of Omu)"
add("Dinohide Raid Viatus",      "Feet",  784, {"Combat Advantage": 235, "Critical Strike": 353, "Defense": 588}, 706, src_dh, "Dinohide Set", ["Warlock"])
add("Dinohide Assault Barakoa",  "Head",  784, {"Combat Advantage": 353, "Critical Severity": 235, "Defense": 588}, 706, src_dh, "Dinohide Set", ["Warlock"])
add("Dinohide Assault Kiuno",    "Armor", 784, {"Critical Strike": 353, "Critical Severity": 235, "Defense": 588}, 706, src_dh, "Dinohide Set", ["Warlock"])
add("Dinohide Assault Shabas",   "Arms",  784, {"Combat Advantage": 353, "Critical Severity": 215, "Defense": 588}, 706, src_dh, "Dinohide Set", ["Warlock"])
add("Dinohide Assault Viatus",   "Feet",  784, {"Critical Strike": 353, "Critical Severity": 215, "Defense": 588}, 706, src_dh, "Dinohide Set", ["Warlock"])

# Masterwork III Stronghold Weapons (Module 13 Lost City of Omu)
# - Obsidian Tecpatl (Pact Blade)
# - Dinohide Temicamatl (Grimoire)
# - Exalted Obsidian Tecpatl (Pact Blade variant)
src_msw = "Masterwork Crafting (Module 13) / Stronghold"
mw3_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Masterwork III Weapon Set", "pieces": 2,
           "description": "2 of Set: You and nearby allies are granted the following: +2% Base Damage Boost, +2% Overall Outgoing Healing, -2% Incoming Damage. This effect may stack up to 5 times when allies are equipped with a set of Stronghold weapons."}]
TIERS = [
    ("Uncommon",  350, 131, 262, 131, 315),
    ("Rare",      500, 188, 375, 188, 450),
    ("Epic",      650, 244, 488, 244, 585),
    ("Legendary", 800, 300, 600, 300, 720),
]
for rarity, il, acc, ca, crit, cr in TIERS:
    add(f"Obsidian Tecpatl ({rarity})",         "Main Hand", il, {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr, src_msw, "Masterwork III Weapon Set", ["Warlock"], mw3_eb, 2)
    add(f"Dinohide Temicamatl ({rarity})",      "Off Hand",  il, {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr, src_msw, "Masterwork III Weapon Set", ["Warlock"], mw3_eb, 2)

# Exalted variant (Mod 13 PvP upgrade)
add("Exalted Obsidian Tecpatl", "Main Hand", 400, {"Accuracy": 150, "Combat Advantage": 300, "Critical Strike": 150}, 360, src_msw, "Masterwork III Weapon Set", ["Warlock"], mw3_eb, 2)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
