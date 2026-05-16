"""Rogue gear batch 62 — Beaded Sash 3 tiers + Beaded Amulet 4 tiers (Masterwork III equip set)."""
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

src_mw = "Masterwork Crafting (Mod 13)"
mwn_eb = [{"type": "Set", "scope": "self", "stat": "Accuracy", "amount": 1,
           "setName": "Masterwork III Equipment Set", "pieces": 2,
           "description": "2 of Set: Encounter triggers Alacrity — 1% Accuracy + 5% Movement Speed for 3s. Max 3 stacks."}]

# Beaded Sash (Belt) — IL 350/500/650
add("Beaded Sash", "Belt", 350,
    {"Accuracy": 175, "Combat Advantage": 175, "Critical Strike": 175}, 315, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"INT": 1, "CHA": 1})
add("Beaded Sash (IL 500)", "Belt", 500,
    {"Accuracy": 250, "Combat Advantage": 250, "Critical Strike": 250}, 450, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"INT": 1, "CHA": 1})
add("Beaded Sash (IL 650)", "Belt", 650,
    {"Accuracy": 325, "Combat Advantage": 325, "Critical Strike": 326}, 585, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"INT": 2, "CHA": 1})

# Beaded Amulet (Neck) — IL 350/500/650/800
add("Beaded Amulet", "Neck", 350,
    {"Combat Advantage": 175, "Critical Strike": 175, "Critical Severity": 175}, 315, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"CON": 1})
add("Beaded Amulet (IL 500)", "Neck", 500,
    {"Combat Advantage": 250, "Critical Strike": 250, "Critical Severity": 250}, 450, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"CON": 2})
add("Beaded Amulet (IL 650)", "Neck", 650,
    {"Combat Advantage": 325, "Critical Strike": 326, "Critical Severity": 325}, 585, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"CON": 3})
add("Beaded Amulet (IL 800)", "Neck", 800,
    {"Combat Advantage": 400, "Critical Strike": 401, "Critical Severity": 400}, 720, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"CON": 4})

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
