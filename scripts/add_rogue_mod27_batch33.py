"""Rogue gear batch 33 — Pioneer Raid Khaftan/Keffiyeh, Huntsman Assault Boots,
Pioneer Assault 4-pc, Pilgrim Raid Keffiyeh start."""
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

cls_br = ["Bard", "Rogue"]

# ---- Pioneer Raid (Campaign Rewards, IL 616) — remaining 2 pieces
src_cr = "Campaign Rewards and Store"
SET_PR = "Pioneer Raid"
add("Pioneer Raid Keffiyeh", "Head",  616,
    {"Combat Advantage": 277, "Critical Strike": 185, "Defense": 462}, 554, src_cr, SET_PR, cls_br,
    [{"name": "Leader's Vitality",
      "description": "Gain 1000 Maximum Hit Points for each player in your team."}])
add("Pioneer Raid Khaftan",  "Armor", 616,
    {"Combat Advantage": 277, "Critical Strike": 185, "Defense": 462}, 554, src_cr, SET_PR, cls_br,
    [{"name": "Leader's Guard",
      "description": "Gain 200 Defense for each player in your team."}])

# ---- Huntsman Assault Boots (Tomb of the Nine Gods)
src_t9g = "Tomb of the Nine Gods (Master)"
add("Huntsman Assault Boots", "Feet", 672,
    {"Combat Advantage": 302, "Critical Severity": 202, "Defense": 504}, 605, src_t9g, "Huntsman Assault", cls_br,
    [{"name": "Executioner's Haste",
      "description": "When you kill an enemy, Movement Speed +1% for 10s. Max 5 stacks."}])

# ---- Pioneer Assault (IL 616) — full 4-pc
SET_PASA = "Pioneer Assault"
add("Pioneer Assault Keffiyeh", "Head",  616,
    {"Combat Advantage": 277, "Critical Severity": 185, "Defense": 462}, 554, src_cr, SET_PASA, cls_br,
    [{"name": "Leader's Vitality",
      "description": "Gain 1000 Maximum HP per team player."}])
add("Pioneer Assault Khaftan",  "Armor", 616,
    {"Critical Strike": 277, "Critical Severity": 185, "Defense": 462}, 554, src_cr, SET_PASA, cls_br,
    [{"name": "Leader's Guard",
      "description": "Gain 200 Defense per team player."}])
add("Pioneer Assault Qafaz",    "Arms",  616,
    {"Critical Strike": 277, "Critical Severity": 185, "Defense": 462}, 554, src_cr, SET_PASA, cls_br,
    [{"name": "Leader's Might",
      "description": "Gain 200 Power per team player."}])
add("Pioneer Assault Soqs",     "Feet",  616,
    {"Combat Advantage": 277, "Critical Severity": 185, "Defense": 462}, 554, src_cr, SET_PASA, cls_br,
    [{"name": "Leader's Dash",
      "description": "Movement Speed +1% per team player."}])

# ---- Pilgrim Raid (Zen Market, IL 644)
src_zen = "Zen Market"
SET_PILR = "Pilgrim Raid"
add("Pilgrim Raid Keffiyeh", "Head", 644,
    {"Combat Advantage": 193, "Critical Strike": 290, "Defense": 483}, 580, src_zen, SET_PILR, cls_br,
    [{"name": "Chultan Hunter",
      "description": "+1% Damage in all of Chult."}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
