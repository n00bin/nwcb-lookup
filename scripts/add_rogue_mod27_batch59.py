"""Rogue gear batch 59 — Obsidian Omihuictli MH IL 800, Obsidian Itecpayo OH + Obsidian Mekatl tiers,
Exalted Obsidian Omihuictli 2 tiers."""
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
           "description": "2 of Set: You and nearby allies: +2% BDB, +2% OOH, -2% Incoming Damage. Stacks up to 5x."}]

# Obsidian Omihuictli MH IL 800
add("Obsidian Omihuictli (IL 800)", "Main Hand", 800,
    {"Accuracy": 300, "Combat Advantage": 600, "Critical Strike": 300}, 720, src_omu, "Masterwork III Weapon Set", ["Rogue"], mw3_eb)

# Obsidian Itecpayo OH IL 350 + 800
add("Obsidian Itecpayo",          "Off Hand", 350,
    {"Accuracy": 131, "Combat Advantage": 262, "Critical Strike": 131}, 315, src_omu, "Masterwork III Weapon Set", ["Rogue"], mw3_eb)
add("Obsidian Itecpayo (IL 800)", "Off Hand", 800,
    {"Accuracy": 300, "Combat Advantage": 600, "Critical Strike": 300}, 720, src_omu, "Masterwork III Weapon Set", ["Rogue"], mw3_eb)

# Obsidian Mekatl (mid-tier OH variant) IL 500 + 650
add("Obsidian Mekatl (IL 500)", "Off Hand", 500,
    {"Accuracy": 188, "Combat Advantage": 375, "Critical Strike": 188}, 450, src_omu, "Masterwork III Weapon Set", ["Rogue"], mw3_eb)
add("Obsidian Mekatl (IL 650)", "Off Hand", 650,
    {"Accuracy": 244, "Combat Advantage": 488, "Critical Strike": 244}, 585, src_omu, "Masterwork III Weapon Set", ["Rogue"], mw3_eb)

# Exalted Obsidian Omihuictli (MH) — IL 400 + 550
add("Exalted Obsidian Omihuictli (IL 400)", "Main Hand", 400,
    {"Accuracy": 150, "Combat Advantage": 300, "Critical Strike": 150}, 360, src_omu, "Masterwork III Weapon Set", ["Rogue"], mw3_eb)
add("Exalted Obsidian Omihuictli (IL 550)", "Main Hand", 550,
    {"Accuracy": 206, "Combat Advantage": 412, "Critical Strike": 206}, 495, src_omu, "Masterwork III Weapon Set", ["Rogue"], mw3_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
