"""Rogue gear batch 73 — Elemental Lionsmane Duelist Gloves+Boots, Lionsmane Duelist Boots+Gloves start."""
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

# Elemental Lionsmane Duelist remaining 2 pieces (IL 574)
src_ei = "Elemental Infusion"
SET_ELD = "Elemental Lionsmane Duelist"
add("Elemental Lionsmane Duelist Gloves", "Arms", 574,
    {"Critical Strike": 129, "Defense": 430, "Critical Avoidance": 129, "Deflection": 172}, 517, src_ei, SET_ELD, cls_br)
add("Elemental Lionsmane Duelist Boots",  "Feet", 574,
    {"Accuracy": 185, "Defense": 430, "Deflection": 245}, 517, src_ei, SET_ELD, cls_br)

# Lionsmane Duelist (base, IL 560) — Stronghold Siege
src_ss = "Stronghold Siege"
SET_LD = "Lionsmane Duelist"
add("Lionsmane Duelist Gloves", "Arms", 560,
    {"Critical Strike": 126, "Defense": 420, "Critical Avoidance": 168, "Deflection": 168}, 504, src_ss, SET_LD, cls_br)
add("Lionsmane Duelist Boots",  "Feet", 560,
    {"Accuracy": 181, "Defense": 420, "Deflection": 219}, 504, src_ss, SET_LD, cls_br)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
