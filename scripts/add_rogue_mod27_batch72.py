"""Rogue gear batch 72 — Stronghold Dagger MH 2 more tiers + Stronghold Stiletto OH 4 tiers,
Elemental Lionsmane Duelist 2 pieces start (IL 574)."""
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

# Stronghold Dagger MH 2 more tiers (500/600)
src_sh = "Stronghold Outfitter"
stronghold_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 2,
                  "setName": "Stronghold Unity", "pieces": 2,
                  "description": "2 of Set: +2% BDB, +2% OOH, -2% Incoming Damage. Stacks up to 5x with similar Stronghold weapons."}]
add("Stronghold Dagger (IL 500)", "Main Hand", 500, {"Accuracy": 188, "Combat Advantage": 375, "Critical Strike": 188}, 450, src_sh, "Stronghold Unity", ["Rogue"], stronghold_eb)
add("Stronghold Dagger (IL 600)", "Main Hand", 600, {"Accuracy": 225, "Combat Advantage": 450, "Critical Strike": 225}, 540, src_sh, "Stronghold Unity", ["Rogue"], stronghold_eb)

# Stronghold Stiletto OH 4 tiers (300/400/500/600)
TIERS = [(300,270,112,225,112),(400,360,150,300,150),(500,450,188,375,188),(600,540,225,450,225)]
for il, cr, accu, ca, cs in TIERS:
    name = "Stronghold Stiletto" if il == 300 else f"Stronghold Stiletto (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_sh, "Stronghold Unity", ["Rogue"], stronghold_eb)

# Elemental Lionsmane Duelist (Set 11/20, IL 574)
src_ei = "Elemental Infusion"
SET_ELD = "Elemental Lionsmane Duelist"
cls_br = ["Bard", "Rogue"]
add("Elemental Lionsmane Duelist Mask", "Head",  574,
    {"Accuracy": 172, "Critical Strike": 129, "Defense": 430, "Awareness": 129}, 517, src_ei, SET_ELD, cls_br, set_size=4)
add("Elemental Lionsmane Duelist Vest", "Armor", 574,
    {"Accuracy": 129, "Combat Advantage": 129, "Defense": 430, "Awareness": 172}, 517, src_ei, SET_ELD, cls_br, set_size=4)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
