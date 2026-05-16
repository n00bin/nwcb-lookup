"""Rogue gear batch 58 — Dinohide Assault 4-pc + Masterwork III Obsidian Omihuictli MH 3 tiers."""
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

# Dinohide Assault 4-pc (IL 784)
src_omu = "Masterwork Armor III / The Lost City of Omu (Module 13)"
SET_DAS = "Dinohide Assault"
add("Dinohide Assault Chinibili",   "Head",  784,
    {"Combat Advantage": 353, "Critical Severity": 235, "Defense": 588}, 706, src_omu, SET_DAS, cls_br,
    [{"name": "Gladiator's Accuracy",
      "description": "Every 5s in combat, gain 100 Accuracy. After 2 minutes, ability no longer active."}])
add("Dinohide Assault Mederebiya",  "Armor", 784,
    {"Critical Strike": 353, "Critical Severity": 235, "Defense": 588}, 706, src_omu, SET_DAS, cls_br,
    [{"name": "Challenger's Might",
      "description": "When in combat with only one enemy, Power +1500."}])
add("Dinohide Assault Amibari",     "Arms",  784,
    {"Combat Advantage": 353, "Critical Strike": 235, "Defense": 588}, 706, src_omu, SET_DAS, cls_br,
    [{"name": "Survivor's Parry",
      "description": "Gain 25 Deflect for each percent of health you are missing."}])
add("Dinohide Assault Butisi",      "Feet",  784,
    {"Critical Strike": 353, "Critical Severity": 235, "Defense": 588}, 706, src_omu, SET_DAS, cls_br,
    [{"name": "Gladiator's Focus",
      "description": "Every 5s in combat, gain 100 Critical Strike. After 2 minutes, ability no longer active."}])

# Masterwork III Weapon Set — Obsidian Omihuictli MH 3 tiers (350/500/650)
mw3_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 2,
           "setName": "Masterwork III Weapon Set", "pieces": 2,
           "description": "2 of Set: You and nearby allies: +2% Base Damage Boost, +2% Overall Outgoing Healing, -2% Incoming Damage. Stacks up to 5 times when allies have similar weapons."}]
TIERS = [(350,315,131,262,131),(500,450,188,375,188),(650,585,244,488,244)]
for il, cr, accu, ca, cs in TIERS:
    name = "Obsidian Omihuictli" if il == 350 else f"Obsidian Omihuictli (IL {il})"
    add(name, "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_omu, "Masterwork III Weapon Set", ["Rogue"], mw3_eb, set_size=2)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
