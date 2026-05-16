"""Rogue gear batch 78 — Umbral Duelist 4-pc, Umbral Executioner Boots+Gloves, Company Raid Mask+Vest start."""
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
src_mw = "Masterwork Armor (Stronghold)"

# Umbral Duelist (Tank/Awareness, IL 728)
SET_UD = "Umbral Duelist"
add("Umbral Duelist Mask",   "Head",  728,
    {"Accuracy": 218, "Critical Strike": 164, "Defense": 546, "Awareness": 164}, 655, src_mw, SET_UD, cls_br,
    [{"name": "Gladiator's Accuracy",
      "description": "Every 5s in combat, gain 100 Accuracy. After 2 minutes, ability no longer active."}])
add("Umbral Duelist Vest",   "Armor", 728,
    {"Accuracy": 164, "Combat Advantage": 164, "Defense": 546, "Awareness": 218}, 655, src_mw, SET_UD, cls_br,
    [{"name": "Challenger's Might",
      "description": "When in combat with only one enemy, Power +1500."}])
add("Umbral Duelist Gloves", "Arms",  728,
    {"Critical Strike": 164, "Defense": 546, "Critical Avoidance": 164, "Deflection": 218}, 655, src_mw, SET_UD, cls_br,
    [{"name": "Survivor's Parry",
      "description": "Gain 25 Deflect for each percent of health you are missing."}])
add("Umbral Duelist Boots",  "Feet",  728,
    {"Accuracy": 235, "Defense": 546, "Deflection": 311}, 655, src_mw, SET_UD, cls_br,
    [{"name": "Gladiator's Focus",
      "description": "Every 5s in combat, gain 100 Critical Strike. After 2 minutes, ability no longer active."}])

# Umbral Executioner remaining 2 pieces
SET_UE = "Umbral Executioner"
add("Umbral Executioner Boots",  "Feet", 728,
    {"Combat Advantage": 164, "Critical Strike": 218, "Defense": 546, "Deflection": 164}, 655, src_mw, SET_UE, cls_br,
    [{"name": "Gladiator's Focus",
      "description": "Every 5s in combat, gain 100 Critical Strike. After 2 minutes, ability no longer active."}])
add("Umbral Executioner Gloves", "Arms", 728,
    {"Combat Advantage": 164, "Critical Strike": 218, "Critical Severity": 164, "Defense": 546}, 655, src_mw, SET_UE, cls_br,
    [{"name": "Survivor's Parry",
      "description": "Gain 25 Deflect for each percent of health you are missing."}])

# Company Raid (Set 15/20, IL 588) — Guild Marks
src_gm = "Guild Marks (Stronghold)"
SET_CR = "Company Raid"
add("Company Raid Mask", "Head",  588,
    {"Accuracy": 265, "Combat Advantage": 176, "Defense": 441}, 529, src_gm, SET_CR, cls_br)
add("Company Raid Vest", "Armor", 588,
    {"Accuracy": 265, "Combat Advantage": 176, "Defense": 441}, 529, src_gm, SET_CR, cls_br)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
