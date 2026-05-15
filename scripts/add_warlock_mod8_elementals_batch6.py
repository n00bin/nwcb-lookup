"""Module 8 Elemental Evil — Weapons of the Elements (13 sub-sets, partial).
Captured here: Drowcraft remainder, Howling, Earthen, Burning starts.
"""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Module 8 Elemental Evil — screenshot intake 2026-05-14."

def add(name, slot, il, rs, cr, source, set_name=None, classes=None, equip=None, set_size=2):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": {}, "abilityBonuses": {},
        "notes": INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

# Elemental Drowcraft remainder
src_ed = "Elemental Infusion (Czer-Konig / Module 8)"
drow_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Drowcraft", "pieces": 4,
            "description": "1 of Set: -10% Incoming Damage against Demon-type enemies. 2 of Set: Reduces amount of Madness inflicted by Maddening Aura. 3 of Set: -30% Incoming Damage against Paranoid Delusions."}]
add("Elemental Drowcraft Raid Longcoat",     "Armor", 588, {"Combat Advantage": 265, "Critical Strike": 176, "Defense": 441}, 529, src_ed, "Drowcraft", ["Warlock"], drow_eb, set_size=4)
add("Elemental Drowcraft Assault Wristguards","Arms", 588, {"Combat Advantage": 265, "Critical Severity": 176, "Defense": 441}, 529, src_ed, "Drowcraft", ["Warlock"], drow_eb, set_size=4)
add("Elemental Drowcraft Assault Pigaches",  "Feet",  588, {"Combat Advantage": 265, "Critical Severity": 176, "Defense": 441}, 529, src_ed, "Drowcraft", ["Warlock"], drow_eb, set_size=4)

# Elemental sub-sets — Weapons of the Elements (Module 8 Underdark + Elemental Evil Mod 4)
# Each has Pact Blade (Main Hand) + Grimoire (Off Hand) at 4 IL tiers.
src_elem = "Weapons of the Elements (Module 8 / Elemental Evil)"

TIERS = [
    ("Uncommon",  300, 112, 225, 112, 270),
    ("Rare",      400, 150, 300, 150, 360),
    ("Epic",      500, 188, 375, 188, 450),
    ("Legendary", 600, 225, 450, 225, 540),
]

def elem_set(name, set_name, eb_desc):
    eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": set_name, "pieces": 2,
           "description": eb_desc}]
    for rarity, il, acc, ca, crit, cr in TIERS:
        add(f"{name} Pact Blade ({rarity})", "Main Hand", il,
            {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr,
            src_elem, set_name, ["Warlock"], eb, set_size=2)
        add(f"{name} Grimoire ({rarity})", "Off Hand", il,
            {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr,
            src_elem, set_name, ["Warlock"], eb, set_size=2)

elem_set("Howling", "Howling Heart",
         "2 of Set: When you dodge, block, sprint, or shadow slip your Movement Speed is increased by 50% for 2 seconds. This effect may only occur once every 10 seconds.")
elem_set("Earthen", "Earthen Heart",
         "2 of Set: When you stand still for 3 seconds, incoming damage is reduced by 5%. This effect stacks up to 5 times and is removed upon moving.")
elem_set("Burning", "Burning Heart",
         "2 of Set: When using a daily power, there is a chance 25% of your AP will be immediately restored.")

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
