"""Rogue gear batch 47 — Twisted Misericorde OH 2 more tiers (500/600),
Dusk Armor 4-pc Raid + Dusk Assault Mask (Set 3/6, IL 1175, Stronghold)."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Rogue gear — screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes, equip=None, percent=None, set_size=4, abilities=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": percent or {}, "abilityBonuses": abilities or {},
        "allowedClasses": classes, "notes": INTAKE}
    data.append(entry)

# Twisted Misericorde OH — 2 more tiers (500/600)
src_ud = "Underdark / Demogorgon (Master) / Mantol-Derith"
tw_eb = [{"type": "Set", "scope": "self", "stat": "Defense", "amount": 160,
          "setName": "Duality", "pieces": 2,
          "description": "2 of Set: Paranoia stacks (max 24): +160 Defense per stack when struck. Bloodlust stacks: +160 Power per stack when striking."}]
add("Twisted Misericorde (IL 500)", "Off Hand", 500, {"Accuracy": 188, "Combat Advantage": 375, "Critical Strike": 188}, 450, src_ud, "Duality", ["Rogue"], tw_eb, set_size=2)
add("Twisted Misericorde (IL 600)", "Off Hand", 600, {"Accuracy": 225, "Combat Advantage": 450, "Critical Strike": 225}, 540, src_ud, "Duality", ["Rogue"], tw_eb, set_size=2)

# Dusk Armor — Raid 4-pc (IL 1175)
src_sh = "Trade Bar Merchant / Underdark (Module 8)"
SET_DR = "Dusk Armor (Raid)"
cls_br = ["Bard", "Rogue"]
dusk_eb = [{"type": "Set", "scope": "self", "stat": "Max HP", "amount": 5000,
            "setName": "Dusk", "pieces": 2,
            "description": "2 of Set: +5,000 Max HP, +1% Power, +1% Defense. Wanderer's Vigor: when not in a party, regenerate 2000 HP every 3s. 4 of Set: On Stronghold map, you and allies gain +5 Movement Speed."}]
add("Dusk Raid Mask",   "Head",  1175,
    {"Combat Advantage": 352, "Critical Strike": 529, "Defense": 881}, 1058, src_sh, SET_DR, cls_br, dusk_eb)
add("Dusk Raid Vest",   "Armor", 1175,
    {"Accuracy": 529, "Combat Advantage": 352, "Defense": 881}, 1058, src_sh, SET_DR, cls_br, dusk_eb)
add("Dusk Raid Gloves", "Arms",  1175,
    {"Combat Advantage": 352, "Critical Strike": 529, "Defense": 881}, 1058, src_sh, SET_DR, cls_br, dusk_eb)
add("Dusk Raid Boots",  "Feet",  1175,
    {"Accuracy": 529, "Combat Advantage": 352, "Defense": 881}, 1058, src_sh, SET_DR, cls_br, dusk_eb)

# Dusk Assault Mask — alt set start
SET_DA = "Dusk Armor (Assault)"
add("Dusk Assault Mask", "Head", 1175,
    {"Accuracy": 529, "Critical Severity": 352, "Defense": 881}, 1058, src_sh, SET_DA, cls_br, dusk_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
