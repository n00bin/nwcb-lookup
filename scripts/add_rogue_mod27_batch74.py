"""Rogue gear batch 74 — Lionsmane Duelist Vest+Mask, Elemental Lionsmane Executioner 3 pieces,
Lionsmane Executioner 3 pieces."""
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

# Lionsmane Duelist Vest+Mask (IL 560)
src_ss = "Stronghold Siege"
SET_LD = "Lionsmane Duelist"
add("Lionsmane Duelist Vest", "Armor", 560,
    {"Accuracy": 126, "Combat Advantage": 126, "Defense": 420, "Awareness": 168}, 504, src_ss, SET_LD, cls_br)
add("Lionsmane Duelist Mask", "Head",  560,
    {"Accuracy": 168, "Critical Strike": 126, "Defense": 420, "Awareness": 126}, 504, src_ss, SET_LD, cls_br)

# Elemental Lionsmane Executioner (IL 574) — Elemental Infusion
src_ei = "Elemental Infusion"
SET_ELE = "Elemental Lionsmane Executioner"
add("Elemental Lionsmane Executioner Mask",   "Head",  574,
    {"Combat Advantage": 129, "Critical Strike": 129, "Critical Severity": 172, "Defense": 430}, 517, src_ei, SET_ELE, cls_br)
add("Elemental Lionsmane Executioner Vest",   "Armor", 574,
    {"Combat Advantage": 129, "Critical Strike": 172, "Critical Avoidance": 129, "Defense": 430}, 517, src_ei, SET_ELE, cls_br)
add("Elemental Lionsmane Executioner Gloves", "Arms",  574,
    {"Combat Advantage": 129, "Critical Strike": 172, "Critical Severity": 129, "Defense": 430}, 517, src_ei, SET_ELE, cls_br)

# Lionsmane Executioner (base, IL 560) — Stronghold Siege
SET_LE = "Lionsmane Executioner"
add("Lionsmane Executioner Vest",   "Armor", 560,
    {"Combat Advantage": 126, "Critical Strike": 168, "Critical Avoidance": 126, "Defense": 420}, 504, src_ss, SET_LE, cls_br)
add("Lionsmane Executioner Gloves", "Arms",  560,
    {"Combat Advantage": 126, "Critical Strike": 168, "Critical Severity": 126, "Defense": 420}, 504, src_ss, SET_LE, cls_br)
add("Lionsmane Executioner Boots",  "Feet",  560,
    {"Combat Advantage": 126, "Critical Strike": 168, "Defense": 420, "Deflection": 126}, 504, src_ss, SET_LE, cls_br)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
