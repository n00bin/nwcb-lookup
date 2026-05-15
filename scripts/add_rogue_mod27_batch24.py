"""Rogue gear batch 24 — Banditlord's Assault Jerkin, Tyrant Weapons (Skinstealer/Skinpeeler)
4 IL tiers each, Exalted Tyrant Weapons (Exalted Skinstealer 4 tiers, Exalted Skinpeeler start)."""
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

# ---- Banditlord's Assault Jerkin (was missing from batch 23)
src_bv = "Barovia Seals Store / Ravenloft (Module 14)"
SET_ASLT = "Barovian Lord's Armor (Assault)"
cls_br = ["Bard", "Rogue"]
add("Banditlord's Assault Jerkin", "Armor", 770,
    {"Combat Advantage": 329, "Critical Strike": 248, "Defense": 578}, 693, src_bv, SET_ASLT, cls_br,
    [{"name": "Warden's Balance",
      "description": "When health is 50% or more, your Power is increased by 1500. When health is below 50%, Defense is increased by 2000."}], set_size=4)

# ---- Tyrant Weapons (Module 13 — Lost City of Omu) — Tier 3 Hunt
src_omu = "Tier 3 Hunt in Omu / Port Nyanzaru (Module 13)"
tyr_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 1,
           "setName": "Tyrant", "pieces": 2,
           "description": "2 of Set: At the start of combat, your Base Damage Boost, OOH, and Damage Resistance are increased by 1%. Every 5s in combat, these increase by 1%. Doubled by a Trophy Hunter buff. (Max 10%)"}]

# Skinstealer MH — 4 tiers
add("Skinstealer",          "Main Hand", 350,
    {"Accuracy": 131, "Combat Advantage": 262, "Critical Strike": 131}, 315, src_omu, "Tyrant", ["Rogue"], tyr_eb)
add("Skinstealer (IL 500)", "Main Hand", 500,
    {"Accuracy": 188, "Combat Advantage": 375, "Critical Strike": 188}, 450, src_omu, "Tyrant", ["Rogue"], tyr_eb)
add("Skinstealer (IL 650)", "Main Hand", 650,
    {"Accuracy": 244, "Combat Advantage": 488, "Critical Strike": 244}, 585, src_omu, "Tyrant", ["Rogue"], tyr_eb)
add("Skinstealer (IL 800)", "Main Hand", 800,
    {"Accuracy": 300, "Combat Advantage": 600, "Critical Strike": 300}, 720, src_omu, "Tyrant", ["Rogue"], tyr_eb)

# Skinpeeler OH — 4 tiers
add("Skinpeeler",          "Off Hand", 350,
    {"Accuracy": 131, "Combat Advantage": 262, "Critical Strike": 131}, 315, src_omu, "Tyrant", ["Rogue"], tyr_eb)
add("Skinpeeler (IL 500)", "Off Hand", 500,
    {"Accuracy": 188, "Combat Advantage": 375, "Critical Strike": 188}, 450, src_omu, "Tyrant", ["Rogue"], tyr_eb)
add("Skinpeeler (IL 650)", "Off Hand", 650,
    {"Accuracy": 244, "Combat Advantage": 488, "Critical Strike": 244}, 585, src_omu, "Tyrant", ["Rogue"], tyr_eb)
add("Skinpeeler (IL 800)", "Off Hand", 800,
    {"Accuracy": 300, "Combat Advantage": 600, "Critical Strike": 300}, 720, src_omu, "Tyrant", ["Rogue"], tyr_eb)

# Exalted Skinstealer MH — 4 tiers
add("Exalted Skinstealer",          "Main Hand", 350,
    {"Accuracy": 131, "Combat Advantage": 262, "Critical Strike": 131}, 315, src_omu, "Tyrant", ["Rogue"], tyr_eb)
add("Exalted Skinstealer (IL 500)", "Main Hand", 500,
    {"Accuracy": 188, "Combat Advantage": 375, "Critical Strike": 188}, 450, src_omu, "Tyrant", ["Rogue"], tyr_eb)
add("Exalted Skinstealer (IL 650)", "Main Hand", 650,
    {"Accuracy": 244, "Combat Advantage": 488, "Critical Strike": 244}, 585, src_omu, "Tyrant", ["Rogue"], tyr_eb)
add("Exalted Skinstealer (IL 800)", "Main Hand", 800,
    {"Accuracy": 300, "Combat Advantage": 600, "Critical Strike": 300}, 720, src_omu, "Tyrant", ["Rogue"], tyr_eb)

# Exalted Skinpeeler OH — start tier
add("Exalted Skinpeeler", "Off Hand", 350,
    {"Accuracy": 131, "Combat Advantage": 262, "Critical Strike": 131}, 315, src_omu, "Tyrant", ["Rogue"], tyr_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
