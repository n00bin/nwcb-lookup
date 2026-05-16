"""Rogue gear batch 55 — Eternal Leather Armor + Helmet, Dragon Bone weapons (Mod 1 ToD)."""
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

cls_br = ["Bard", "Rogue"]
src_tod = "Tyranny of Dragons Epic Adventure"

# Eternal Armor (IL 1300) — remaining 2 pieces
SET_EA = "Eternal Armor Set"
add("Eternal Leather Armor", "Armor", 1300,
    {"Accuracy": 337, "Combat Advantage": 337, "Defense": 975, "Critical Avoidance": 296}, 1170, src_tod, SET_EA, cls_br, set_size=4)
add("Eternal Helmet",        "Head",  1300,
    {"Combat Advantage": 337, "Critical Severity": 339, "Defense": 975, "Deflection": 294}, 1170, src_tod, SET_EA, cls_br, set_size=4)

# Dragon Bone Weapons (Mod 1 Tyranny of Dragons)
src_todc = "Tyranny of Dragons Campaign Tasks"
ef_eb = [{"type": "Set", "scope": "self", "stat": "Critical Strike", "amount": 0,
          "setName": "Dagger of Elemental Fire", "pieces": 2,
          "description": "2 of Set: Dagger of Elemental Fire + Elemental Fire Stiletto. Augments artifact properties."}]
gd_eb = [{"type": "Set", "scope": "self", "stat": "Critical Strike", "amount": 0,
          "setName": "Golden Dragon", "pieces": 2,
          "description": "2 of Set: Any Golden Dragon Dagger + Golden Dragon Stiletto. Modification slot for class feature enhancement."}]

add("Dagger of Elemental Fire",    "Main Hand", 300,
    {"Combat Advantage": 150, "Critical Strike": 150, "Critical Severity": 150}, 270, src_todc, "Dagger of Elemental Fire", ["Rogue"], ef_eb)
add("Elemental Fire Stiletto",     "Off Hand",  300,
    {"Combat Advantage": 150, "Critical Strike": 150, "Critical Severity": 150}, 270, src_todc, "Dagger of Elemental Fire", ["Rogue"], ef_eb)
add("Golden Dragon Stiletto",      "Off Hand",  300,
    {"Combat Advantage": 150, "Critical Strike": 150, "Critical Severity": 150}, 270, src_todc, "Golden Dragon", ["Rogue"], gd_eb)
add("Infiltrator of the Golden Dragon", "Main Hand", 300,
    {"Combat Advantage": 150, "Critical Strike": 150, "Deflection": 150}, 270, src_todc, "Golden Dragon", ["Rogue"], gd_eb,
    None, 2,
    abilities=None)

# Add equip bonus for Infiltrator separately via manual entry
# Actually add() with equip parameter — but I already used equip for gd_eb above. Let me restructure
# The above isn't great — let me re-do Infiltrator with both set_eb and individual equip
data[-1]["equipBonuses"] = gd_eb + [{"name": "Gloaming Cut Damage",
                                      "description": "Increase the damage done by Gloaming Cut by 10%."}]

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
