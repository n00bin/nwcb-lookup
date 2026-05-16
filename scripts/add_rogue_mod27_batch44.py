"""Rogue gear batch 44 — Black Ice Gear 4-pc (IL 512, Mod 4 Black Ice Forge),
Hammerstone Armor 4-pc (IL 352, Dwarven Valley)."""
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

# Black Ice Gear (IL 512) — Black Ice Forge
src_bif = "Black Ice Forge (Module 4 Icewind Dale)"
SET_BI = "Black Ice Gear"
add("Black Ice Mask",   "Head",  512,
    {"Combat Advantage": 131, "Critical Strike": 60, "Defense": 384, "Awareness": 59, "Deflection": 131}, 461, src_bif, SET_BI, cls_br)
add("Black Ice Armor",  "Armor", 512,
    {"Accuracy": 59, "Combat Advantage": 131, "Defense": 384, "Critical Avoidance": 60, "Deflection": 131}, 461, src_bif, SET_BI, cls_br)
add("Black Ice Gloves", "Arms",  512,
    {"Accuracy": 59, "Critical Severity": 131, "Defense": 384, "Critical Avoidance": 60, "Deflection": 131}, 461, src_bif, SET_BI, cls_br)
add("Black Ice Boots",  "Feet",  512,
    {"Accuracy": 132, "Critical Severity": 60, "Defense": 384, "Awareness": 60, "Critical Avoidance": 131}, 461, src_bif, SET_BI, cls_br)

# Hammerstone Armor (IL 352) — Dwarven Valley
src_dv = "Dwarven Valley (Module 5)"
SET_HS = "Hammerstone Armor"
add("Hammerstone Mask",   "Head",  352,
    {"Combat Advantage": 92, "Critical Severity": 39, "Defense": 264, "Critical Avoidance": 40, "Deflection": 92}, 317, src_dv, SET_HS, ["Rogue"])
add("Hammerstone Tunic",  "Armor", 352,
    {"Combat Advantage": 92, "Critical Severity": 39, "Defense": 264, "Critical Avoidance": 40, "Deflection": 92}, 317, src_dv, SET_HS, ["Rogue"])
add("Hammerstone Gloves", "Arms",  352,
    {"Combat Advantage": 92, "Critical Severity": 39, "Defense": 264, "Critical Avoidance": 40, "Deflection": 92}, 317, src_dv, SET_HS, ["Rogue"])
add("Hammerstone Boots",  "Feet",  352,
    {"Combat Advantage": 92, "Critical Severity": 39, "Defense": 264, "Critical Avoidance": 40, "Deflection": 92}, 317, src_dv, SET_HS, ["Rogue"])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
