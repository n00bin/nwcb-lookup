"""Rogue gear batch 48 — Dusk Assault 3 more pieces, Drowcraft Armor 4-pc (IL 567),
Elemental Drowcraft Raid Mask start (IL 588)."""
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

# Dusk Assault remaining 3 pieces (IL 1175)
src_sh = "Trade Bar Merchant / Underdark (Module 8)"
SET_DA = "Dusk Armor (Assault)"
dusk_eb = [{"type": "Set", "scope": "self", "stat": "Max HP", "amount": 5000,
            "setName": "Dusk", "pieces": 2,
            "description": "2 of Set: +5,000 Max HP, +1% Power, +1% Defense. Wanderer's Vigor: not in party, regenerate 2000 HP every 3s."}]
add("Dusk Assault Vest",   "Armor", 1175,
    {"Critical Strike": 529, "Critical Severity": 352, "Defense": 881}, 1058, src_sh, SET_DA, cls_br, dusk_eb)
add("Dusk Assault Gloves", "Arms",  1175,
    {"Critical Strike": 529, "Critical Severity": 352, "Defense": 881}, 1058, src_sh, SET_DA, cls_br, dusk_eb)
add("Dusk Assault Boots",  "Feet",  1175,
    {"Combat Advantage": 529, "Critical Severity": 352, "Defense": 881}, 1058, src_sh, SET_DA, cls_br, dusk_eb)

# Drowcraft Armor (Set 4/6, IL 567) — Mantol-Derith Armor Dealer
src_md = "Mantol-Derith Armor Dealer (Module 6)"
SET_DC = "Drowcraft Armor"
add("Drowcraft Mask",   "Head",  567,
    {"Accuracy": 255, "Critical Strike": 170, "Defense": 425}, 510, src_md, SET_DC, cls_br)
add("Drowcraft Vest",   "Armor", 567,
    {"Accuracy": 170, "Combat Advantage": 255, "Defense": 425}, 510, src_md, SET_DC, cls_br)
add("Drowcraft Gloves", "Arms",  567,
    {"Combat Advantage": 255, "Critical Severity": 170, "Defense": 425}, 510, src_md, SET_DC, cls_br)
add("Drowcraft Boots",  "Feet",  567,
    {"Critical Strike": 255, "Critical Severity": 170, "Defense": 425}, 510, src_md, SET_DC, cls_br)

# Elemental Drowcraft Raid Mask (Elemental Infusion, IL 588)
src_ei = "Elemental Infusion"
SET_EDR = "Elemental Drowcraft Raid"
add("Elemental Drowcraft Raid Mask", "Head", 588,
    {"Accuracy": 265, "Critical Strike": 176, "Defense": 441}, 529, src_ei, SET_EDR, cls_br)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
