"""Module 2-8 legacy Warlock gear — Thayan Servitor, Twisted set, Dusk Armor, Elk Tribe."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-14."

def add(name, slot, il, rs, cr, source, set_name=None, classes=None, equip=None, set_size=0, notes=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size,
        "source": source, "percentStats": {}, "abilityBonuses": {},
        "notes": notes or INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

# Elk Tribe Pact Blade (Module 4)
add("Elk Tribe Noble's Pact Blade", "Main Hand", 399,
    {"Accuracy": 98, "Combat Advantage": 202, "Critical Strike": 202, "Critical Avoidance": 98}, 359,
    "Icewind Pass (Module 4)", "Weapons of the Elk Tribe Chiefs", ["Warlock"])

# Thayan Servitor Armor (Module 2 Dread Ring) — IL 800
src_th = "Dread Ring Store (Module 2)"
add("Hood of the Thayan Servitor",   "Head",  800, {"Combat Advantage": 89, "Critical Strike": 211, "Defense": 600, "Critical Avoidance": 211, "Deflection": 89}, 720, src_th, "Thayan Servitor Armor", ["Warlock"], set_size=4)
add("Tunic of the Thayan Servitor",  "Armor", 800, {"Combat Advantage": 97, "Critical Strike": 203, "Defense": 600, "Critical Avoidance": 203}, 720, src_th, "Thayan Servitor Armor", ["Warlock"], set_size=4)
add("Gloves of the Thayan Servitor", "Arms",  800, {"Combat Advantage": 89, "Critical Strike": 211, "Defense": 600, "Critical Avoidance": 211, "Deflection": 89}, 720, src_th, "Thayan Servitor Armor", ["Warlock"], set_size=4)
add("Boots of the Thayan Servitor",  "Feet",  800, {"Combat Advantage": 89, "Critical Strike": 211, "Defense": 600, "Critical Avoidance": 211, "Deflection": 89}, 720, src_th, "Thayan Servitor Armor", ["Warlock"], set_size=4)

# Twisted Set (Module 8 — Demogorgon Master / Mantol-Derith) — 2pc artifact weapons
twisted_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Duality", "pieces": 2,
               "description": "2 of Set: Gain the effect of Paranoia (when struck, lose 100 Defense, lose stack when strike) and Bloodlust (when striking, gain 100 Power, lose stack when struck). Neither Paranoia nor Bloodlust may exceed 24 stacks or be reduced below 1 stack."}]
src_tw = "Demogorgon (Master) / Mantol-Derith (Module 8)"
for rarity, il, acc, ca, crit, cr in [("Uncommon", 300, 112, 225, 112, 270), ("Rare", 400, 150, 300, 150, 360), ("Epic", 500, 188, 375, 188, 450), ("Legendary", 600, 225, 450, 225, 540)]:
    add(f"Twisted Akinakes ({rarity})", "Main Hand", il, {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr, src_tw, "Duality", ["Warlock"], twisted_eb, set_size=2)
    add(f"Twisted Grimoire ({rarity})", "Off Hand",  il, {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr, src_tw, "Duality", ["Warlock"], twisted_eb, set_size=2)

# Dusk Armor (Module 8 Underdark Stronghold gear) — Raid (DPS) + Assault variants, IL 1175
src_du = "Trade Bar Merchant / Stronghold (Module 8 Underdark)"
dusk_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Dusk", "pieces": 4,
            "description": "1 of Set: Wanderer's Vigor — when not in a party, regenerate 2000 HP every 3s. 2 of Set: When in a party, +5,000 Max HP, +1% Power, +1% Defense. 3 of Set: When on the Stronghold map, you and your allies gain 5 Movement Speed (no effect in Stronghold Siege)."}]
for label, head_rs, body_rs, arms_rs, feet_rs in [
    ("Raid",    {"Combat Advantage": 352, "Critical Strike": 529, "Defense": 881}, {"Accuracy": 352, "Combat Advantage": 352, "Defense": 881}, {"Combat Advantage": 352, "Critical Strike": 529, "Defense": 881}, {"Combat Advantage": 352, "Critical Strike": 529, "Defense": 881}),
    ("Assault", {"Accuracy": 352, "Critical Severity": 529, "Defense": 881}, {"Accuracy": 352, "Critical Severity": 529, "Defense": 881}, {"Accuracy": 352, "Critical Severity": 529, "Defense": 881}, {"Combat Advantage": 352, "Critical Severity": 529, "Defense": 881}),
]:
    add(f"Dusk {label} Cowl",       "Head",  1175, head_rs, 1058, src_du, "Dusk", ["Warlock"], dusk_eb, set_size=4)
    add(f"Dusk {label} Longcoat",   "Armor", 1175, body_rs, 1058, src_du, "Dusk", ["Warlock"], dusk_eb, set_size=4)
    add(f"Dusk {label} Wristguards","Arms",  1175, arms_rs, 1058, src_du, "Dusk", ["Warlock"], dusk_eb, set_size=4)
    add(f"Dusk {label} Pigaches",   "Feet",  1175, feet_rs, 1058, src_du, "Dusk", ["Warlock"], dusk_eb, set_size=4)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
