"""Rogue gear batch 21 — Sunset Weapons (Sun Set) IL tier expansion:
Sunset Dagger MH IL 650/800, Sunset Stiletto OH IL 350/500/650/800."""
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

src_rv = "Ravenloft (Module 14) — Bonvia"
sun_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 5,
           "setName": "Sun Set", "pieces": 2,
           "description": "2 of Set: Base Damage Boost and OOH +5%. In Bonvia during nightfall, BDB/Damage Resistance/OOH/Movement Speed +10%."}]

# Sunset Dagger MH IL 650 + 800
add("Sunset Dagger (IL 650)", "Main Hand", 650,
    {"Accuracy": 244, "Combat Advantage": 488, "Critical Strike": 244}, 585, src_rv, "Sun Set", ["Rogue"], sun_eb)
add("Sunset Dagger (IL 800)", "Main Hand", 800,
    {"Accuracy": 300, "Combat Advantage": 600, "Critical Strike": 300}, 720, src_rv, "Sun Set", ["Rogue"], sun_eb)

# Sunset Stiletto OH — 4 tiers
add("Sunset Stiletto",          "Off Hand", 350,
    {"Accuracy": 131, "Combat Advantage": 262, "Critical Strike": 188}, 315, src_rv, "Sun Set", ["Rogue"], sun_eb)
add("Sunset Stiletto (IL 500)", "Off Hand", 500,
    {"Accuracy": 188, "Combat Advantage": 375, "Critical Strike": 188}, 450, src_rv, "Sun Set", ["Rogue"], sun_eb)
add("Sunset Stiletto (IL 650)", "Off Hand", 650,
    {"Accuracy": 244, "Combat Advantage": 488, "Critical Strike": 244}, 585, src_rv, "Sun Set", ["Rogue"], sun_eb)
add("Sunset Stiletto (IL 800)", "Off Hand", 800,
    {"Accuracy": 300, "Combat Advantage": 600, "Critical Strike": 300}, 720, src_rv, "Sun Set", ["Rogue"], sun_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
