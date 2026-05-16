"""Rogue gear batch 56 — Golden Dragon's Whisper, Dragon Bone Whirl/Swirl,
Reinforced Dragonflight Raid 4-pc (IL 1400)."""
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

# Golden Dragon's Whisper (Mod 1 ToD)
src_todc = "Tyranny of Dragons Campaign Tasks"
gd_eb = [{"type": "Set", "scope": "self", "stat": "Critical Strike", "amount": 0,
          "setName": "Golden Dragon", "pieces": 2,
          "description": "2 of Set: Golden Dragon Dagger + Golden Dragon Stiletto. Modification slot for class feature enhancement."}]
add("Golden Dragon's Whisper", "Main Hand", 300,
    {"Combat Advantage": 150, "Critical Strike": 150, "Critical Severity": 150}, 270, src_todc, "Golden Dragon", ["Rogue"],
    gd_eb + [{"name": "Disheartening Strike Damage", "description": "Increase the damage done by Disheartening Strike by 10%."}])

# Dragon Bone Weapons (Set 3/5, IL 800) — from various dragon hunts
src_drag = "Dragon Hunts (Neverdeath/Icespire Peak/Ebon Downs)"
add("Dragon Bone Whirl", "Main Hand", 800,
    {"Combat Advantage": 422, "Critical Strike": 422, "Critical Avoidance": 355}, 355, src_drag, "Dragon Bone Weapons", ["Rogue"])
add("Dragon Bone Swirl", "Off Hand",  800,
    {"Combat Advantage": 422, "Critical Strike": 427, "Deflection": 350}, 350, src_drag, "Dragon Bone Weapons", ["Rogue"])

# Reinforced Dragonflight Raid 4-pc (IL 1400) — Masterwork Armor III
src_mw3 = "Masterwork Armor III"
SET_RD = "Reinforced Dragonflight Raid"
rd_eb = [{"type": "Set", "scope": "self", "stat": "Max HP", "amount": 3000,
          "setName": "Dragonflight", "pieces": 2,
          "description": "2 of Set: +3,000 Maximum Hit Points. 3 of Set: +1,000 Power."}]
add("Reinforced Dragonflight Raid Mask",   "Head",  1400,
    {"Combat Advantage": 420, "Critical Strike": 630, "Defense": 1050}, 1260, src_mw3, SET_RD, cls_br, rd_eb, set_size=4)
add("Reinforced Dragonflight Raid Vest",   "Armor", 1400,
    {"Accuracy": 630, "Combat Advantage": 420, "Defense": 1050}, 1260, src_mw3, SET_RD, cls_br, rd_eb, set_size=4)
add("Reinforced Dragonflight Raid Gloves", "Arms",  1400,
    {"Combat Advantage": 420, "Critical Strike": 630, "Defense": 1050}, 1260, src_mw3, SET_RD, cls_br, rd_eb, set_size=4)
add("Reinforced Dragonflight Raid Boots",  "Feet",  1400,
    {"Accuracy": 630, "Combat Advantage": 420, "Defense": 1050}, 1260, src_mw3, SET_RD, cls_br, rd_eb, set_size=4)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
