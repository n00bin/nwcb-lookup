"""Rogue gear batch 23 — Barovian Lord's Armor (Banditlord's Raid + Assault, IL 770) — Ravenloft Mod 14."""
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
src_bv = "Barovia Seals Store / Ravenloft (Module 14)"

# ---- Barovian Lord's Armor — Banditlord's Raid (Crit-Severity focus, IL 770)
SET_RAID = "Barovian Lord's Armor (Raid)"
add("Banditlord's Raid Hat",     "Head",  770,
    {"Combat Advantage": 247, "Critical Strike": 330, "Defense": 578}, 693, src_bv, SET_RAID, cls_br,
    [{"name": "Survivor's Savagery",
      "description": "When health is 50% or more, your Critical Strike is increased by 1500. When health is below 50%, Critical Avoidance is increased by 2000."}])
add("Banditlord's Raid Jerkin",  "Armor", 770,
    {"Combat Advantage": 329, "Critical Strike": 248, "Defense": 578}, 693, src_bv, SET_RAID, cls_br,
    [{"name": "Warden's Balance",
      "description": "When health is 50% or more, your Power is increased by 1500. When health is below 50%, Defense is increased by 2000."}])
add("Banditlord's Raid Bracers", "Arms",  770,
    {"Combat Advantage": 329, "Critical Strike": 248, "Defense": 578}, 693, src_bv, SET_RAID, cls_br,
    [{"name": "Survivor's Finesse",
      "description": "When health is 50% or more, your Critical Severity is increased by 1500. When health is below 50%, Deflect is increased by 2000."}])
add("Banditlord's Raid Boots",   "Feet",  770,
    {"Accuracy": 330, "Combat Advantage": 247, "Defense": 578}, 693, src_bv, SET_RAID, cls_br,
    [{"name": "Survivor's Strike",
      "description": "When health is 50% or more, your Accuracy is increased by 1500. When health is below 50%, Movement Speed is increased by 10%."}])

# ---- Barovian Lord's Armor — Banditlord's Assault (Crit-Strike focus, IL 770)
SET_ASLT = "Barovian Lord's Armor (Assault)"
add("Banditlord's Assault Hat",     "Head",  770,
    {"Combat Advantage": 247, "Critical Severity": 330, "Defense": 578}, 693, src_bv, SET_ASLT, cls_br,
    [{"name": "Survivor's Savagery",
      "description": "When health is 50% or more, your Critical Strike is increased by 1500. When health is below 50%, Critical Avoidance is increased by 2000."}])
add("Banditlord's Assault Bracers", "Arms",  770,
    {"Combat Advantage": 329, "Critical Severity": 248, "Defense": 578}, 693, src_bv, SET_ASLT, cls_br,
    [{"name": "Survivor's Finesse",
      "description": "When health is 50% or more, your Critical Severity is increased by 1500. When health is below 50%, Deflect is increased by 2000."}])
add("Banditlord's Assault Boots",   "Feet",  770,
    {"Accuracy": 329, "Combat Advantage": 248, "Defense": 578}, 693, src_bv, SET_ASLT, cls_br,
    [{"name": "Survivor's Strike",
      "description": "When health is 50% or more, your Accuracy is increased by 1500. When health is below 50%, Movement Speed is increased by 10%."}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
