"""Rogue gear batch 61 — Bronzewood Sash 3 more tiers, Lichstone Sash 3 tiers (Masterwork III belts)."""
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

# Bronzewood Sash (Belt) — IL 500/650/800
add("Bronzewood Sash (IL 500)", "Belt", 500,
    {"Combat Advantage": 250, "Critical Strike": 250, "Critical Severity": 250}, 450, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"STR": 1, "DEX": 1})
add("Bronzewood Sash (IL 650)", "Belt", 650,
    {"Combat Advantage": 325, "Critical Strike": 326, "Critical Severity": 325}, 585, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"STR": 1, "DEX": 2})
add("Bronzewood Sash (IL 800)", "Belt", 800,
    {"Combat Advantage": 400, "Critical Strike": 401, "Critical Severity": 400}, 720, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"STR": 2, "DEX": 2})

# Lichstone Sash (Belt) — tank variant — IL 500/650/800
add("Lichstone Sash (IL 500)", "Belt", 500,
    {"Critical Avoidance": 500, "Deflection": 250}, 450, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"CON": 2})
add("Lichstone Sash (IL 650)", "Belt", 650,
    {"Critical Avoidance": 649, "Deflection": 325}, 585, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"CON": 3})
add("Lichstone Sash (IL 800)", "Belt", 800,
    {"Critical Avoidance": 799, "Deflection": 400}, 720, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
    abilities={"CON": 4})

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
