"""Rogue gear batch 65 — Titansteel Dagger IL 800, Titansteel Stiletto OH 4 tiers,
Manticore Raid Mask/Vest/Gloves start (Masterwork Armor II, Mod 11 Shroud of Souls)."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Rogue gear — screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes, equip=None, percent=None, set_size=2, abilities=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": percent or {}, "abilityBonuses": abilities or {},
        "allowedClasses": classes, "notes": INTAKE}
    data.append(entry)

src_sos = "Masterwork Crafting / The Shroud of Souls (Module 11)"
mw2_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 2,
           "setName": "Masterwork II Weapon Set", "pieces": 2,
           "description": "2 of Set: +2% BDB, +2% OOH, -2% Incoming Damage. Stacks up to 5x with allies in Stronghold weapons."}]

# Titansteel Dagger MH IL 800
add("Titansteel Dagger (IL 800)", "Main Hand", 800, {"Accuracy": 300, "Combat Advantage": 600, "Critical Strike": 300}, 720, src_sos, "Masterwork II Weapon Set", ["Rogue"], mw2_eb)

# Titansteel Stiletto OH — 4 tiers
TIERS = [(350,315,131,262,131),(500,450,188,375,188),(650,585,244,488,244),(800,720,300,600,300)]
for il, cr, accu, ca, cs in TIERS:
    name = "Titansteel Stiletto" if il == 350 else f"Titansteel Stiletto (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_sos, "Masterwork II Weapon Set", ["Rogue"], mw2_eb)

# Manticore Raid (Set 7/20, IL 756) — Masterwork Armor II — Bard/Rogue
SET_MR = "Manticore Raid"
cls_br = ["Bard", "Rogue"]
add("Manticore Raid Mask",   "Head",  756,
    {"Combat Advantage": 227, "Critical Strike": 340, "Defense": 567}, 680, src_sos, SET_MR, cls_br,
    [{"name": "Gladiator's Accuracy",
      "description": "Every 5s in combat, gain 100 Accuracy. After 2 minutes, ability no longer active."}], set_size=4)
add("Manticore Raid Vest",   "Armor", 756,
    {"Combat Advantage": 227, "Critical Strike": 340, "Defense": 567}, 680, src_sos, SET_MR, cls_br,
    [{"name": "Challenger's Might",
      "description": "When in combat with only one enemy, Power +1500."}], set_size=4)
add("Manticore Raid Gloves", "Arms",  756,
    {"Combat Advantage": 227, "Critical Strike": 340, "Defense": 567}, 680, src_sos, SET_MR, cls_br,
    [{"name": "Survivor's Parry",
      "description": "Gain 25 Deflect for each percent of health you are missing."}], set_size=4)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
