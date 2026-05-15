"""Rogue gear batch 22 — Vistani Weapons set (Ravenloft Mod 14), 4 IL tiers MH + 3 tiers OH."""
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

src_rv = "Ravenloft (Module 14)"
vis_eb = [{"type": "Set", "scope": "self", "stat": "Defense", "amount": 500,
           "setName": "Vistani", "pieces": 2,
           "description": "2 of Set: +500 Defense, +5% Movement Speed."}]

# Vistani Dagger MH — 4 tiers
add("Vistani Dagger",          "Main Hand", 350,
    {"Accuracy": 262, "Critical Strike": 262}, 315, src_rv, "Vistani", ["Rogue"], vis_eb)
add("Vistani Dagger (IL 500)", "Main Hand", 500,
    {"Accuracy": 375, "Critical Strike": 375}, 450, src_rv, "Vistani", ["Rogue"], vis_eb)
add("Vistani Dagger (IL 650)", "Main Hand", 650,
    {"Accuracy": 488, "Critical Strike": 488}, 585, src_rv, "Vistani", ["Rogue"], vis_eb)
add("Vistani Dagger (IL 800)", "Main Hand", 800,
    {"Accuracy": 600, "Critical Strike": 600}, 720, src_rv, "Vistani", ["Rogue"], vis_eb)

# Vistani Stiletto OH — 3 tiers
add("Vistani Stiletto",          "Off Hand", 350,
    {"Accuracy": 262, "Critical Strike": 262}, 315, src_rv, "Vistani", ["Rogue"], vis_eb)
add("Vistani Stiletto (IL 500)", "Off Hand", 500,
    {"Accuracy": 375, "Critical Strike": 375}, 450, src_rv, "Vistani", ["Rogue"], vis_eb)
add("Vistani Stiletto (IL 650)", "Off Hand", 650,
    {"Accuracy": 488, "Critical Strike": 488}, 585, src_rv, "Vistani", ["Rogue"], vis_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
