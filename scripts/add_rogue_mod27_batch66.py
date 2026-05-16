"""Rogue gear batch 66 — Manticore Raid Boots, Manticore Executioner 3 pieces,
Manticore Assault 4-pc (Masterwork Armor II, Mod 11)."""
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

src_sos = "Masterwork Crafting / The Shroud of Souls (Module 11)"
cls_br = ["Bard", "Rogue"]

# Manticore Raid Boots
add("Manticore Raid Boots", "Feet", 756,
    {"Combat Advantage": 340, "Critical Strike": 227, "Defense": 567}, 680, src_sos, "Manticore Raid", cls_br,
    [{"name": "Gladiator's Focus",
      "description": "Every 5s in combat, gain 100 Critical Strike. After 2 minutes, ability no longer active."}])

# Manticore Executioner — 3 pieces
SET_ME = "Manticore Executioner"
add("Manticore Executioner Mask",   "Head",  756,
    {"Combat Advantage": 170, "Critical Strike": 170, "Critical Severity": 227, "Defense": 567}, 680, src_sos, SET_ME, cls_br,
    [{"name": "Gladiator's Accuracy",
      "description": "Every 5s in combat, gain 100 Accuracy. After 2 minutes, ability no longer active."}])
add("Manticore Executioner Vest",   "Armor", 756,
    {"Combat Advantage": 170, "Critical Strike": 227, "Critical Avoidance": 170, "Defense": 567}, 680, src_sos, SET_ME, cls_br,
    [{"name": "Challenger's Might",
      "description": "When in combat with only one enemy, Power +1500."}])
add("Manticore Executioner Gloves", "Arms",  756,
    {"Combat Advantage": 170, "Critical Strike": 227, "Critical Severity": 170, "Defense": 567}, 680, src_sos, SET_ME, cls_br,
    [{"name": "Survivor's Parry",
      "description": "Gain 25 Deflect for each percent of health you are missing."}])

# Manticore Assault — 4-pc
SET_MA = "Manticore Assault"
add("Manticore Assault Mask",   "Head",  756,
    {"Combat Advantage": 340, "Critical Severity": 227, "Defense": 567}, 680, src_sos, SET_MA, cls_br,
    [{"name": "Gladiator's Accuracy",
      "description": "Every 5s in combat, gain 100 Accuracy. After 2 minutes, ability no longer active."}])
add("Manticore Assault Vest",   "Armor", 756,
    {"Critical Strike": 340, "Critical Severity": 227, "Defense": 567}, 680, src_sos, SET_MA, cls_br,
    [{"name": "Challenger's Might",
      "description": "When in combat with only one enemy, Power +1500."}])
add("Manticore Assault Gloves", "Arms",  756,
    {"Combat Advantage": 340, "Critical Severity": 227, "Defense": 567}, 680, src_sos, SET_MA, cls_br,
    [{"name": "Survivor's Parry",
      "description": "Gain 25 Deflect for each percent of health you are missing."}])
add("Manticore Assault Boots",  "Feet",  756,
    {"Critical Strike": 340, "Critical Severity": 227, "Defense": 567}, 680, src_sos, SET_MA, cls_br,
    [{"name": "Gladiator's Focus",
      "description": "Every 5s in combat, gain 100 Critical Strike. After 2 minutes, ability no longer active."}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
