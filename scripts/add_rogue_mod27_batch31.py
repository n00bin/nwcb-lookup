"""Rogue gear batch 31 — Exalted Pioneer Sakin OH 4 tiers + Chultan Armor (Primal Raid + Primal Assault
+ Huntsman Raid) — Bard/Rogue, IL 672-700."""
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

# ---- Exalted Pioneer Sakin OH — 4 tiers
src_pi = "Other Miscellaneous Sources"
pio_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 200,
           "setName": "Pioneer", "pieces": 2,
           "description": "2 of Set: Increased stat per party member."}]
TIERS = [(350,315,131,262,131),(500,450,188,375,188),(650,585,244,488,244),(800,720,300,600,300)]
for il, cr, accu, ca, cs in TIERS:
    name = "Exalted Pioneer Sakin" if il == 350 else f"Exalted Pioneer Sakin (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_pi, "Pioneer", ["Rogue"], pio_eb, set_size=2)

# ---- Primal Raid (Chultan Armor, IL 700)
src_cs = "Chult Seals Store"
SET_PR = "Primal Raid"
add("Primal Raid Chinibili",   "Head",  700,
    {"Combat Advantage": 210, "Critical Strike": 315, "Defense": 525}, 630, src_cs, SET_PR, cls_br,
    [{"name": "Butcher's Remedy",
      "description": "When you damage or heal your target for more than 15% of your Max HP in a single blow, you gain 1% of your health back."}])
add("Primal Raid Mederebiya",  "Armor", 700,
    {"Combat Advantage": 315, "Critical Strike": 210, "Defense": 525}, 630, src_cs, SET_PR, cls_br,
    [{"name": "Butcher's Guard",
      "description": "When you damage or heal your target for more than 15% of Max HP in a single blow, you gain 1% Defense for 10s. (Max stack 5)"}])
add("Primal Raid Amibari",     "Arms",  700,
    {"Combat Advantage": 315, "Critical Strike": 210, "Defense": 525}, 630, src_cs, SET_PR, cls_br,
    [{"name": "Butcher's Might",
      "description": "When you damage or heal your target for more than 15% of Max HP in a single blow, you gain 1% Power for 10s. (Max stack 5)"}])
add("Primal Raid Butisi",      "Feet",  700,
    {"Accuracy": 315, "Combat Advantage": 210, "Defense": 525}, 630, src_cs, SET_PR, cls_br,
    [{"name": "Executioner's Zeal",
      "description": "When you kill an enemy, you gain 3% Action Points."}])

# ---- Primal Assault (alt Chultan, IL 700) — Crit-Severity focus
SET_PA = "Primal Assault"
add("Primal Assault Chinibili",  "Head",  700,
    {"Combat Advantage": 210, "Critical Severity": 315, "Defense": 525}, 630, src_cs, SET_PA, cls_br,
    [{"name": "Butcher's Remedy",
      "description": "When you damage or heal target for more than 15% of Max HP, gain 1% of health back."}])
add("Primal Assault Mederebiya", "Armor", 700,
    {"Combat Advantage": 315, "Critical Strike": 210, "Defense": 525}, 630, src_cs, SET_PA, cls_br,
    [{"name": "Butcher's Guard",
      "description": "Damage/heal for more than 15% of Max HP, gain 1% Defense for 10s. Max 5 stacks."}])
add("Primal Assault Amibari",    "Arms",  700,
    {"Combat Advantage": 315, "Critical Severity": 210, "Defense": 525}, 630, src_cs, SET_PA, cls_br,
    [{"name": "Butcher's Might",
      "description": "Damage/heal for more than 15% of Max HP, gain 1% Power for 10s. Max 5 stacks."}])
add("Primal Assault Butisi",     "Feet",  700,
    {"Combat Advantage": 315, "Critical Severity": 210, "Defense": 525}, 630, src_cs, SET_PA, cls_br,
    [{"name": "Executioner's Zeal",
      "description": "When you kill an enemy, you gain 3% Action Points."}])

# ---- Huntsman Raid (Tomb of the Nine Gods, IL 672)
src_t9g = "Tomb of the Nine Gods (Master)"
SET_HR = "Huntsman Raid"
add("Huntsman Raid Mask",   "Head",  672,
    {"Combat Advantage": 202, "Critical Strike": 302, "Defense": 504}, 605, src_t9g, SET_HR, cls_br,
    [{"name": "Great Hunter",
      "description": "+1% Damage against Hunts in Chult."}])
add("Huntsman Raid Vest",   "Armor", 672,
    {"Accuracy": 302, "Combat Advantage": 202, "Defense": 504}, 605, src_t9g, SET_HR, cls_br,
    [{"name": "Challenger's Guard",
      "description": "When in combat with only one enemy, your Defense is increased by 1000."}])
add("Huntsman Raid Gloves", "Arms",  672,
    {"Combat Advantage": 202, "Critical Strike": 302, "Defense": 504}, 605, src_t9g, SET_HR, cls_br,
    [{"name": "Challenger's Might",
      "description": "When in combat with only one enemy, your Power is increased by 1000."}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
