"""Rogue gear batch 46 — Boots of the Thayan Servitor, Twisted Set weapons (Makhaira MH 4 tiers + Misericorde OH 2 tiers)."""
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

# Boots of the Thayan Servitor
src_dr = "Dread Ring Store"
add("Boots of the Thayan Servitor", "Feet", 800,
    {"Accuracy": 210, "Critical Strike": 88, "Critical Severity": 210, "Defense": 600, "Critical Avoidance": 89}, 720, src_dr, "Thayan Servitor Armor", ["Bard", "Rogue"], set_size=4)

# Twisted Set (Set 1/6) — Demonic Artifacts and Gear — Mod 6 Underdark
src_ud = "Underdark / Demogorgon (Master) / Mantol-Derith"
tw_eb = [{"type": "Set", "scope": "self", "stat": "Defense", "amount": 160,
          "setName": "Duality", "pieces": 2,
          "description": "2 of Set: Paranoia — +160 Defense per stack when struck (max 24, min 1). Bloodlust — +160 Power per stack when striking (max 24, min 1)."}]

# Twisted Makhaira MH — 4 tiers (300/400/500/600)
TIERS_TW = [(300,270,112,225,112),(400,360,150,300,150),(500,450,188,375,188),(600,540,225,450,225)]
for il, cr, accu, ca, cs in TIERS_TW:
    name = "Twisted Makhaira" if il == 300 else f"Twisted Makhaira (IL {il})"
    add(name, "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ud, "Duality", ["Rogue"], tw_eb)

# Twisted Misericorde OH — 2 tiers (300/400)
for il, cr, accu, ca, cs in TIERS_TW[:2]:
    name = "Twisted Misericorde" if il == 300 else f"Twisted Misericorde (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ud, "Duality", ["Rogue"], tw_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
