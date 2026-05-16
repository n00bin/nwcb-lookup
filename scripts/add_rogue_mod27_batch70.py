"""Rogue gear batch 70 — Scintillant Sash IL 800 + Silverspruce Belt 4 tiers + Sphene Sash 4 tiers."""
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

src_mw2 = "Masterwork Crafting (Mod 11)"
mw2_eb = [{"type": "Set", "scope": "self", "stat": "Accuracy", "amount": 500,
           "setName": "Masterwork II Equipment Set", "pieces": 2,
           "description": "2 of Set: Encounter triggers Alacrity — 500 Accuracy + 1000 Movement for 5s. Max 3 stacks."}]

# Scintillant Sash IL 800
add("Scintillant Sash (Mod 11, IL 800)", "Belt", 800,
    {"Combat Advantage": 400, "Critical Strike": 401, "Critical Severity": 400}, 720, src_mw2, "Masterwork II Equipment Set", ["Rogue"], mw2_eb,
    abilities={"STR": 2, "DEX": 2})

# Silverspruce Belt — 4 tiers (tank)
SS = [(350,315,350,175,2),(500,450,500,250,2),(650,585,649,325,3),(800,720,799,400,4)]
for il, cr, cav, defl, con in SS:
    name = "Silverspruce Belt" if il == 350 else f"Silverspruce Belt (IL {il})"
    add(name, "Belt", il, {"Critical Avoidance": cav, "Deflection": defl}, cr, src_mw2, "Masterwork II Equipment Set", ["Rogue"], mw2_eb,
        abilities={"CON": con})

# Sphene Sash — 4 tiers
SP = [(350,315,175,175,175,1,1),(500,450,250,250,250,1,1),(650,585,325,325,325,2,1),(800,720,400,400,401,2,2)]
for il, cr, accu, ca, cs, wis, cha in SP:
    name = "Sphene Sash" if il == 350 else f"Sphene Sash (IL {il})"
    add(name, "Belt", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_mw2, "Masterwork II Equipment Set", ["Rogue"], mw2_eb,
        abilities={"WIS": wis, "CHA": cha})

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
