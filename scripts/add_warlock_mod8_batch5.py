"""Module 8 Underdark — Drowcraft + Elemental Drowcraft sets."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-14."

def add(name, slot, il, rs, cr, source, set_name=None, classes=None, equip=None, set_size=0):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size,
        "source": source, "percentStats": {}, "abilityBonuses": {},
        "notes": INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

drow_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Drowcraft", "pieces": 4,
            "description": "1 of Set: -10% Incoming Damage against Demon-type enemies. 2 of Set: Reduces amount of Madness inflicted by Maddening Aura. 3 of Set: -30% Incoming Damage against Paranoid Delusions."}]

# Drowcraft (base) — IL 567 — Mantol-Derith Armor Dealer / Demogorgon Master
src_d = "Mantol-Derith Armor Dealer / Demogorgon (Master) (Module 8)"
add("Drowcraft Cowl",        "Head",  567, {"Combat Advantage": 255, "Critical Strike": 170, "Defense": 425}, 510, src_d, "Drowcraft", ["Warlock"], drow_eb, set_size=4)
add("Drowcraft Longcoat",    "Armor", 567, {"Combat Advantage": 255, "Critical Strike": 170, "Defense": 425}, 510, src_d, "Drowcraft", ["Warlock"], drow_eb, set_size=4)
add("Drowcraft Wristguards", "Arms",  567, {"Accuracy": 255, "Critical Severity": 170, "Defense": 425}, 510, src_d, "Drowcraft", ["Warlock"], drow_eb, set_size=4)
add("Drowcraft Pigaches",    "Feet",  567, {"Combat Advantage": 255, "Critical Severity": 170, "Defense": 425}, 510, src_d, "Drowcraft", ["Warlock"], drow_eb, set_size=4)

# Elemental Drowcraft (upgraded via Elemental Infusion) — IL 588
src_ed = "Elemental Infusion (Czer-Konig / Module 8)"
add("Elemental Drowcraft Raid Cowl",         "Head",  588, {"Combat Advantage": 265, "Critical Severity": 176, "Defense": 441}, 529, src_ed, "Drowcraft", ["Warlock"], drow_eb, set_size=4)
add("Elemental Drowcraft Raid Pigaches",     "Feet",  588, {"Combat Advantage": 265, "Critical Severity": 176, "Defense": 441}, 529, src_ed, "Drowcraft", ["Warlock"], drow_eb, set_size=4)
add("Elemental Drowcraft Raid Wristguards",  "Arms",  588, {"Combat Advantage": 176, "Critical Advantage": 265, "Defense": 441}, 529, src_ed, "Drowcraft", ["Warlock"], drow_eb, set_size=4)
add("Elemental Drowcraft Assault Cowl",      "Head",  588, {"Combat Advantage": 265, "Critical Severity": 176, "Defense": 441}, 529, src_ed, "Drowcraft", ["Warlock"], drow_eb, set_size=4)
add("Elemental Drowcraft Assault Longcoat",  "Armor", 588, {"Combat Advantage": 265, "Critical Severity": 176, "Defense": 441}, 529, src_ed, "Drowcraft", ["Warlock"], drow_eb, set_size=4)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
