"""Rogue gear batch 76 — Dragonflight Assault 3 more pieces, Elemental Dragonflight Raid 4-pc + Assault Mask start."""
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
src_dr = "The Greed of the Dragonflight (Stronghold)"
src_ei = "Elemental Infusion"
df_eb = [{"type": "Set", "scope": "self", "stat": "Max HP", "amount": 3000,
          "setName": "Dragonflight", "pieces": 2,
          "description": "2 of Set: +3,000 Maximum Hit Points. 3 of Set: +500 Power."}]

# Dragonflight Assault (IL 588) — 3 more pieces
SET_DA = "Dragonflight Assault"
add("Dragonflight Assault Mask",   "Head",  588,
    {"Accuracy": 265, "Critical Severity": 176, "Defense": 441}, 529, src_dr, SET_DA, cls_br, df_eb)
add("Dragonflight Assault Gloves", "Arms",  588,
    {"Critical Strike": 265, "Critical Severity": 176, "Defense": 441}, 529, src_dr, SET_DA, cls_br, df_eb)
add("Dragonflight Assault Boots",  "Feet",  588,
    {"Combat Advantage": 265, "Critical Severity": 176, "Defense": 441}, 529, src_dr, SET_DA, cls_br, df_eb)

# Elemental Dragonflight Raid 4-pc (IL 596)
SET_EDR = "Elemental Dragonflight Raid"
add("Elemental Dragonflight Raid Mask",   "Head",  596,
    {"Accuracy": 179, "Critical Strike": 268, "Defense": 447}, 536, src_ei, SET_EDR, cls_br, df_eb)
add("Elemental Dragonflight Raid Vest",   "Armor", 596,
    {"Accuracy": 268, "Combat Advantage": 179, "Defense": 447}, 536, src_ei, SET_EDR, cls_br, df_eb)
add("Elemental Dragonflight Raid Gloves", "Arms",  596,
    {"Combat Advantage": 179, "Critical Strike": 268, "Defense": 447}, 536, src_ei, SET_EDR, cls_br, df_eb)
add("Elemental Dragonflight Raid Boots",  "Feet",  596,
    {"Combat Advantage": 268, "Critical Strike": 179, "Defense": 447}, 536, src_ei, SET_EDR, cls_br, df_eb)

# Elemental Dragonflight Assault Mask start
SET_EDA = "Elemental Dragonflight Assault"
add("Elemental Dragonflight Assault Mask", "Head", 596,
    {"Accuracy": 268, "Critical Severity": 179, "Defense": 447}, 536, src_ei, SET_EDA, cls_br, df_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
