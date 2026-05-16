"""Rogue gear batch 41 — Lifeforged Stiletto OH 3 more tiers (500/650/800),
Aboleth Weapons (Aboleth Dagger MH 3 tiers 350/500/650)."""
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

src_ca = "Cloaked Ascendancy Campaign Vendor / River District (Module 15)"

# Lifeforged Stiletto OH — 3 more tiers
lf_eb = [{"type": "Set", "scope": "self", "stat": "Defense", "amount": 5,
          "setName": "Lifeforged", "pieces": 2,
          "description": "2 of Set: Encounter power triggers Fortified: Defense +5%, 10% of Defense added to Power for 10s. (30s CD)"}]
add("Lifeforged Stiletto (IL 500)", "Off Hand", 500, {"Accuracy": 188, "Combat Advantage": 375, "Critical Strike": 188}, 450, src_ca, "Lifeforged", ["Rogue"], lf_eb)
add("Lifeforged Stiletto (IL 650)", "Off Hand", 650, {"Accuracy": 244, "Combat Advantage": 488, "Critical Strike": 244}, 585, src_ca, "Lifeforged", ["Rogue"], lf_eb)
add("Lifeforged Stiletto (IL 800)", "Off Hand", 800, {"Accuracy": 300, "Combat Advantage": 600, "Critical Strike": 300}, 720, src_ca, "Lifeforged", ["Rogue"], lf_eb)

# Aboleth Weapons (Storm King's Thunder, Mod 12)
src_sk = "Sea of Moving Ice / Storm King's Thunder (Module 12)"
ab_eb = [{"type": "Set", "scope": "self", "stat": "Outgoing Damage", "amount": 4,
          "setName": "Aboleth", "pieces": 2,
          "description": "2 of Set: Encounter power triggers Far-Influenced: Outgoing Damage +4% + random buff (Relentless +2500 CritStrike, Tainted Attack DoT, Impeding Thought death explosion) for 10s. (30s CD)"}]

# Aboleth Dagger MH — 3 tiers (350/500/650)
TIERS = [(350,315,131,262,131),(500,450,188,375,188),(650,585,244,488,244)]
for il, cr, accu, ca, cs in TIERS:
    name = "Aboleth Dagger" if il == 350 else f"Aboleth Dagger (IL {il})"
    add(name, "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_sk, "Aboleth", ["Rogue"], ab_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
