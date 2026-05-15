"""Rogue gear batch 25 — Exalted Skinpeeler OH remaining tiers (3),
Primal Weapons (Primal Omihuictli MH 4 tiers, Mod 11 Chult)."""
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

# Exalted Skinpeeler OH remaining tiers
src_omu = "Tier 3 Hunt in Omu / Port Nyanzaru (Module 13)"
tyr_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 1,
           "setName": "Tyrant", "pieces": 2,
           "description": "2 of Set: At the start of combat, your Base Damage Boost, OOH, and Damage Resistance are increased by 1%. Every 5s in combat, these increase by 1%. (Max 10%)"}]
add("Exalted Skinpeeler (IL 500)", "Off Hand", 500,
    {"Accuracy": 188, "Combat Advantage": 375, "Critical Strike": 188}, 450, src_omu, "Tyrant", ["Rogue"], tyr_eb)
add("Exalted Skinpeeler (IL 650)", "Off Hand", 650,
    {"Accuracy": 244, "Combat Advantage": 488, "Critical Strike": 244}, 585, src_omu, "Tyrant", ["Rogue"], tyr_eb)
add("Exalted Skinpeeler (IL 800)", "Off Hand", 800,
    {"Accuracy": 300, "Combat Advantage": 600, "Critical Strike": 300}, 720, src_omu, "Tyrant", ["Rogue"], tyr_eb)

# ---- Primal Weapons (Set 2/18, Module 11 — Chult)
src_ch = "Chult Hunts / Sharandar (Module 11)"
prim_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 10,
            "setName": "Primal", "pieces": 2,
            "description": "2 of Set: Primal Recipuyo. If you are hit or healed for more than 10% of your Maximum HP in a single blow, your Base Damage Boost and Overall Outgoing Healing are increased by 10% for 10s."}]

# Primal Omihuictli MH — 4 tiers
add("Primal Omihuictli",          "Main Hand", 350,
    {"Accuracy": 131, "Combat Advantage": 262, "Critical Strike": 131}, 315, src_ch, "Primal", ["Rogue"], prim_eb)
add("Primal Omihuictli (IL 500)", "Main Hand", 500,
    {"Accuracy": 188, "Combat Advantage": 375, "Critical Strike": 188}, 450, src_ch, "Primal", ["Rogue"], prim_eb)
add("Primal Omihuictli (IL 650)", "Main Hand", 650,
    {"Accuracy": 244, "Combat Advantage": 488, "Critical Strike": 244}, 585, src_ch, "Primal", ["Rogue"], prim_eb)
add("Primal Omihuictli (IL 800)", "Main Hand", 800,
    {"Accuracy": 300, "Combat Advantage": 600, "Critical Strike": 300}, 720, src_ch, "Primal", ["Rogue"], prim_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
