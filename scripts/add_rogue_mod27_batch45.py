"""Rogue gear batch 45 — Hammerstone Mace, Elk Tribe Noble weapons, Thayan Servitor Armor start."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Rogue gear — screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes, equip=None, percent=None, set_size=4, abilities=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": percent or {}, "abilityBonuses": abilities or {},
        "allowedClasses": classes, "notes": INTAKE}
    data.append(entry)

# Hammerstone Mace (Mod 5, IL 352) — Dwarven Valley
src_dv = "Dwarven Valley (Module 5)"
add("Hammerstone Mace", "Main Hand", 352,
    {"Combat Advantage": 185, "Critical Severity": 79, "Critical Avoidance": 79, "Deflection": 185}, 317, src_dv, "Hammerstone Armor", ["Rogue"], set_size=4)

# Elk Tribe Noble Weapons (Set 5/9, IL 399) — Icewind Pass
src_iwp = "Icewind Pass (Module 4)"
SET_ET = "Weapons of the Elk Tribe Chiefs"
add("Elk Tribe Noble's Poniard", "Main Hand", 399,
    {"Combat Advantage": 202, "Critical Strike": 202, "Critical Severity": 98, "Critical Avoidance": 98}, 359, src_iwp, SET_ET, ["Rogue"], set_size=2)
add("Elk Tribe Noble's Dirk",    "Off Hand",  399,
    {"Combat Advantage": 202, "Critical Strike": 202, "Critical Severity": 98, "Critical Avoidance": 98}, 359, src_iwp, SET_ET, ["Rogue"], set_size=2)

# Thayan Servitor Armor (Set 1/6, IL 800) — Dread Ring Store
src_dr = "Dread Ring Store"
SET_TS = "Thayan Servitor Armor"
cls_br = ["Bard", "Rogue"]
add("Hood of the Thayan Servitor",   "Head",  800,
    {"Accuracy": 210, "Critical Strike": 88, "Critical Severity": 210, "Defense": 600, "Critical Avoidance": 89}, 720, src_dr, SET_TS, cls_br)
add("Tunic of the Thayan Servitor",  "Armor", 800,
    {"Accuracy": 203, "Critical Strike": 97, "Critical Severity": 203, "Defense": 600, "Critical Avoidance": 97}, 720, src_dr, SET_TS, cls_br)
add("Gloves of the Thayan Servitor", "Arms",  800,
    {"Accuracy": 210, "Critical Strike": 88, "Critical Severity": 210, "Defense": 600, "Critical Avoidance": 89}, 720, src_dr, SET_TS, cls_br)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
