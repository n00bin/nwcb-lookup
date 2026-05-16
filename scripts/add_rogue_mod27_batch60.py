"""Rogue gear batch 60 — Exalted Obsidian Omihuictli MH 2 more tiers + Exalted Obsidian Itecpayo OH 4 tiers,
Bronzewood Sash (Masterwork Waist Sets III)."""
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

src_omu = "Masterwork Armor III / The Lost City of Omu (Module 13)"
mw3_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 2,
           "setName": "Masterwork III Weapon Set", "pieces": 2,
           "description": "2 of Set: +2% BDB, +2% OOH, -2% Incoming Damage. Stacks up to 5x with similar weapons."}]

# Exalted Obsidian Omihuictli (MH) — IL 700, 850
add("Exalted Obsidian Omihuictli (IL 700)", "Main Hand", 700,
    {"Accuracy": 262, "Combat Advantage": 525, "Critical Strike": 262}, 630, src_omu, "Masterwork III Weapon Set", ["Rogue"], mw3_eb)
add("Exalted Obsidian Omihuictli (IL 850)", "Main Hand", 850,
    {"Accuracy": 319, "Combat Advantage": 638, "Critical Strike": 319}, 765, src_omu, "Masterwork III Weapon Set", ["Rogue"], mw3_eb)

# Exalted Obsidian Itecpayo (OH) — 4 tiers
for il, cr, accu, ca, cs in [(400,360,150,300,150),(550,495,206,412,206),(700,630,262,525,262),(850,765,319,638,319)]:
    add(f"Exalted Obsidian Itecpayo (IL {il})", "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_omu, "Masterwork III Weapon Set", ["Rogue"], mw3_eb)

# Bronzewood Sash (Masterwork III Equipment Set, IL 350) — Belt
src_mwn = "Masterwork Crafting (Mod 13)"
mwn_eb = [{"type": "Set", "scope": "self", "stat": "Accuracy", "amount": 1,
           "setName": "Masterwork III Equipment Set", "pieces": 2,
           "description": "2 of Set: Encounter power triggers Alacrity stack — 1% Accuracy + 5% Movement Speed for 3s. Max 3 stacks."}]
add("Bronzewood Sash", "Belt", 350,
    {"Combat Advantage": 175, "Critical Strike": 175, "Critical Severity": 175}, 315, src_mwn, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"STR": 1, "DEX": 1})

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
