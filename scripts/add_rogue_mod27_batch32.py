"""Rogue gear batch 32 — Huntsman Raid Boots, Huntsman Assault (3 pieces), Pioneer Raid (2 pieces start)."""
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
src_t9g = "Tomb of the Nine Gods (Master)"

# Huntsman Raid Boots
add("Huntsman Raid Boots", "Feet", 672,
    {"Accuracy": 302, "Combat Advantage": 202, "Defense": 504}, 605, src_t9g, "Huntsman Raid", cls_br,
    [{"name": "Executioner's Haste",
      "description": "When you kill an enemy, your Movement Speed increases by 1% for 10 seconds. (Max stack 5)"}])

# Huntsman Assault (alt set, IL 672) — Crit-Severity / Crit-Strike focus
SET_HA = "Huntsman Assault"
add("Huntsman Assault Mask",   "Head",  672,
    {"Accuracy": 302, "Critical Severity": 202, "Defense": 504}, 605, src_t9g, SET_HA, cls_br,
    [{"name": "Great Hunter",
      "description": "+1% Damage against Hunts in Chult."}])
add("Huntsman Assault Vest",   "Armor", 672,
    {"Critical Strike": 302, "Critical Severity": 202, "Defense": 504}, 605, src_t9g, SET_HA, cls_br,
    [{"name": "Challenger's Guard",
      "description": "When in combat with only one enemy, Defense is increased by 1000."}])
add("Huntsman Assault Gloves", "Arms",  672,
    {"Critical Strike": 302, "Critical Severity": 202, "Defense": 504}, 605, src_t9g, SET_HA, cls_br,
    [{"name": "Challenger's Might",
      "description": "When in combat with only one enemy, Power is increased by 1000."}])

# Pioneer Raid (Chultan, IL 616) — Campaign Rewards and Store
src_cr = "Campaign Rewards and Store"
SET_PR_LOW = "Pioneer Raid"
add("Pioneer Raid Soqs",  "Feet", 616,
    {"Combat Advantage": 277, "Critical Strike": 185, "Defense": 462}, 554, src_cr, SET_PR_LOW, cls_br,
    [{"name": "Leader's Dash",
      "description": "Your Movement Speed increases by 1% for each player in your team."}])
add("Pioneer Raid Qafaz", "Arms", 616,
    {"Combat Advantage": 277, "Critical Strike": 185, "Defense": 462}, 554, src_cr, SET_PR_LOW, cls_br,
    [{"name": "Leader's Might",
      "description": "Gain 200 Power for each player in your team."}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
