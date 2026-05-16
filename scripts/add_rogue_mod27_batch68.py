"""Rogue gear batch 68 — Scintillant Amulet 2 more tiers, Silverspruce Amulet 4 tiers,
Sphene Amulet 4 tiers (Masterwork II Neck Sets)."""
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
           "description": "2 of Set: Encounter triggers Alacrity stack — 500 Accuracy + 1000 Movement for 5s. Max 3 stacks."}]

# Scintillant Amulet (Mod 11) — 2 more tiers
add("Scintillant Amulet (Mod 11, IL 650)", "Neck", 650,
    {"Accuracy": 325, "Combat Advantage": 325, "Critical Strike": 326}, 585, src_mw2, "Masterwork II Equipment Set", ["Rogue"], mw2_eb,
    abilities={"CON": 3})
add("Scintillant Amulet (Mod 11, IL 800)", "Neck", 800,
    {"Accuracy": 400, "Combat Advantage": 400, "Critical Strike": 401}, 720, src_mw2, "Masterwork II Equipment Set", ["Rogue"], mw2_eb,
    abilities={"CON": 4})

# Silverspruce Amulet (Neck) — tank — 4 tiers
SS = [(350,315,175,175,175,1),(500,450,250,250,250,2),(650,585,325,325,325,3),(800,720,400,400,400,4)]
for il, cr, accu, ca, defl, con in SS:
    name = "Silverspruce Amulet" if il == 350 else f"Silverspruce Amulet (IL {il})"
    add(name, "Neck", il, {"Accuracy": accu, "Critical Avoidance": ca, "Deflection": defl}, cr, src_mw2, "Masterwork II Equipment Set", ["Rogue"], mw2_eb,
        abilities={"CON": con})

# Sphene Amulet (Neck) — 4 tiers
SP = [(350,315,175,175,175,1),(500,450,250,250,250,2),(650,585,325,325,326,3),(800,720,400,400,401,4)]
for il, cr, accu, ca, cs, con in SP:
    name = "Sphene Amulet" if il == 350 else f"Sphene Amulet (IL {il})"
    add(name, "Neck", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_mw2, "Masterwork II Equipment Set", ["Rogue"], mw2_eb,
        abilities={"CON": con})

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
