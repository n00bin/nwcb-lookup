"""Rogue gear batch 79 (FINAL) — Company Raid 2 more pieces + Company Assault 4-pc."""
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

cls_br = ["Bard", "Rogue"]
src_gm = "Guild Marks (Stronghold)"

# Company Raid remaining
SET_CR = "Company Raid"
add("Company Raid Gloves", "Arms", 588,
    {"Combat Advantage": 176, "Critical Strike": 265, "Defense": 441}, 529, src_gm, SET_CR, cls_br)
add("Company Raid Boots",  "Feet", 588,
    {"Combat Advantage": 176, "Critical Strike": 265, "Defense": 441}, 529, src_gm, SET_CR, cls_br)

# Company Assault 4-pc (IL 588) — Guild Marks
SET_CA = "Company Assault"
add("Company Assault Mask",   "Head",  588,
    {"Combat Advantage": 265, "Critical Severity": 176, "Defense": 441}, 529, src_gm, SET_CA, cls_br)
add("Company Assault Vest",   "Armor", 588,
    {"Critical Strike": 265, "Critical Severity": 176, "Defense": 441}, 529, src_gm, SET_CA, cls_br)
add("Company Assault Gloves", "Arms",  588,
    {"Combat Advantage": 265, "Critical Severity": 176, "Defense": 441}, 529, src_gm, SET_CA, cls_br)
add("Company Assault Boots",  "Feet",  588,
    {"Critical Strike": 265, "Critical Severity": 176, "Defense": 441}, 529, src_gm, SET_CA, cls_br)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
