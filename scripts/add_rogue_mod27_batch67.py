"""Rogue gear batch 67 — Manticore Executioner Boots + Manticore Duelist 4-pc,
Scintillant Amulet (Masterwork II Neck) 2 tiers."""
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

# Manticore Executioner Boots
add("Manticore Executioner Boots", "Feet", 756,
    {"Combat Advantage": 170, "Critical Strike": 227, "Deflection": 170, "Defense": 567}, 680, src_sos, "Manticore Executioner", cls_br,
    [{"name": "Gladiator's Focus",
      "description": "Every 5s in combat, gain 100 Critical Strike. After 2 minutes, ability no longer active."}])

# Manticore Duelist (Tank/Awareness variant, IL 756)
SET_MD = "Manticore Duelist"
add("Manticore Duelist Mask",   "Head",  756,
    {"Accuracy": 227, "Critical Strike": 170, "Defense": 547, "Awareness": 170}, 680, src_sos, SET_MD, cls_br,
    [{"name": "Gladiator's Accuracy",
      "description": "Every 5s in combat, gain 100 Accuracy. After 2 minutes, ability no longer active."}])
add("Manticore Duelist Vest",   "Armor", 756,
    {"Accuracy": 170, "Combat Advantage": 170, "Defense": 567, "Deflection": 227}, 680, src_sos, SET_MD, cls_br,
    [{"name": "Challenger's Might",
      "description": "When in combat with only one enemy, Power +1500."}])
add("Manticore Duelist Gloves", "Arms",  756,
    {"Critical Strike": 170, "Defense": 567, "Critical Avoidance": 170, "Deflection": 227}, 680, src_sos, SET_MD, cls_br,
    [{"name": "Survivor's Parry",
      "description": "Gain 25 Deflect for each percent of health you are missing."}])
add("Manticore Duelist Boots",  "Feet",  756,
    {"Accuracy": 244, "Defense": 567, "Deflection": 323}, 680, src_sos, SET_MD, cls_br,
    [{"name": "Gladiator's Focus",
      "description": "Every 5s in combat, gain 100 Critical Strike. After 2 minutes, ability no longer active."}])

# Scintillant Amulet (Neck) — Masterwork II Equipment Set
src_mw2_eq = "Masterwork Crafting (Mod 11)"
mw2_eq_eb = [{"type": "Set", "scope": "self", "stat": "Accuracy", "amount": 500,
              "setName": "Masterwork II Equipment Set", "pieces": 2,
              "description": "2 of Set: Encounter triggers Alacrity stack — 500 Accuracy and 1000 Movement for 5s. Max 3 stacks."}]
add("Scintillant Amulet (Mod 11)",          "Neck", 350,
    {"Accuracy": 175, "Combat Advantage": 175, "Critical Strike": 175}, 315, src_mw2_eq, "Masterwork II Equipment Set", ["Rogue"], mw2_eq_eb, set_size=2,
    abilities={"CON": 1})
add("Scintillant Amulet (Mod 11, IL 500)",  "Neck", 500,
    {"Accuracy": 250, "Combat Advantage": 250, "Critical Strike": 250}, 450, src_mw2_eq, "Masterwork II Equipment Set", ["Rogue"], mw2_eq_eb, set_size=2,
    abilities={"CON": 2})

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
