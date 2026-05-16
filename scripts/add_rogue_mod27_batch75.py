"""Rogue gear batch 75 — Lionsmane Executioner Mask, Elemental Lionsmane Executioner Boots,
Dragonflight Raid 4-pc (IL 588), Dragonflight Assault Vest start."""
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

# Lionsmane Executioner Mask (IL 560)
src_ss = "Stronghold Siege"
add("Lionsmane Executioner Mask", "Head", 560,
    {"Combat Advantage": 126, "Critical Strike": 126, "Critical Severity": 126, "Defense": 420}, 504, src_ss, "Lionsmane Executioner", cls_br)

# Elemental Lionsmane Executioner Boots (IL 574)
src_ei = "Elemental Infusion"
add("Elemental Lionsmane Executioner Boots", "Feet", 574,
    {"Combat Advantage": 129, "Critical Strike": 172, "Defense": 430, "Deflection": 129}, 517, src_ei, "Elemental Lionsmane Executioner", cls_br)

# Dragonflight Raid 4-pc (IL 588) — Greed of the Dragonflight
src_dr = "The Greed of the Dragonflight (Stronghold)"
SET_DR = "Dragonflight Raid"
df_eb = [{"type": "Set", "scope": "self", "stat": "Max HP", "amount": 3000,
          "setName": "Dragonflight", "pieces": 2,
          "description": "2 of Set: +3,000 Maximum Hit Points. 3 of Set: +500 Power."}]
add("Dragonflight Raid Mask",   "Head",  588,
    {"Combat Advantage": 176, "Critical Strike": 265, "Defense": 441}, 529, src_dr, SET_DR, cls_br, df_eb)
add("Dragonflight Raid Vest",   "Armor", 588,
    {"Accuracy": 265, "Combat Advantage": 176, "Defense": 441}, 529, src_dr, SET_DR, cls_br, df_eb)
add("Dragonflight Raid Gloves", "Arms",  588,
    {"Combat Advantage": 176, "Critical Strike": 265, "Defense": 441}, 529, src_dr, SET_DR, cls_br, df_eb)
add("Dragonflight Raid Boots",  "Feet",  588,
    {"Accuracy": 265, "Combat Advantage": 176, "Defense": 441}, 529, src_dr, SET_DR, cls_br, df_eb)

# Dragonflight Assault Vest (IL 588) — alt set start
SET_DA = "Dragonflight Assault"
add("Dragonflight Assault Vest", "Armor", 588,
    {"Accuracy": 265, "Critical Severity": 176, "Defense": 441}, 529, src_dr, SET_DA, cls_br, df_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
