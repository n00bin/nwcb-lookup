"""Rogue gear batch 57 — Reinforced Dragonflight Assault 4-pc + Dinohide Raid 4-pc."""
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

# Reinforced Dragonflight Assault 4-pc (IL 1400)
src_mw3 = "Masterwork Armor III"
SET_RDA = "Reinforced Dragonflight Assault"
rd_eb = [{"type": "Set", "scope": "self", "stat": "Max HP", "amount": 3000,
          "setName": "Dragonflight", "pieces": 2,
          "description": "2 of Set: +3,000 Maximum Hit Points. 3 of Set: +1,000 Power."}]
add("Reinforced Dragonflight Assault Mask",   "Head",  1400,
    {"Accuracy": 630, "Critical Severity": 420, "Defense": 1050}, 1260, src_mw3, SET_RDA, cls_br, rd_eb)
add("Reinforced Dragonflight Assault Vest",   "Armor", 1400,
    {"Accuracy": 630, "Critical Severity": 420, "Defense": 1050}, 1260, src_mw3, SET_RDA, cls_br, rd_eb)
add("Reinforced Dragonflight Assault Gloves", "Arms",  1400,
    {"Critical Strike": 630, "Critical Severity": 420, "Defense": 1050}, 1260, src_mw3, SET_RDA, cls_br, rd_eb)
add("Reinforced Dragonflight Assault Boots",  "Feet",  1400,
    {"Combat Advantage": 630, "Critical Severity": 420, "Defense": 1050}, 1260, src_mw3, SET_RDA, cls_br, rd_eb)

# Dinohide Raid Set (Set 2/20, IL 784) — Masterwork III / Mod 13 Lost City of Omu
src_omu = "Masterwork Armor III / The Lost City of Omu (Module 13)"
SET_DR = "Dinohide Raid"
add("Dinohide Raid Chinibili",   "Head",  784,
    {"Combat Advantage": 235, "Critical Strike": 353, "Defense": 588}, 706, src_omu, SET_DR, cls_br,
    [{"name": "Gladiator's Accuracy",
      "description": "Every 5s in combat, gain 100 Accuracy. After 2 minutes, ability no longer active."}])
add("Dinohide Raid Mederebiya",  "Armor", 784,
    {"Combat Advantage": 235, "Critical Strike": 353, "Defense": 588}, 706, src_omu, SET_DR, cls_br,
    [{"name": "Challenger's Might",
      "description": "When in combat with only one enemy, Power +1500."}])
add("Dinohide Raid Amibari",     "Arms",  784,
    {"Combat Advantage": 235, "Critical Strike": 353, "Defense": 588}, 706, src_omu, SET_DR, cls_br,
    [{"name": "Survivor's Parry",
      "description": "Gain 25 Deflect for each percent of health you are missing."}])
add("Dinohide Raid Butisi",      "Feet",  784,
    {"Combat Advantage": 353, "Critical Strike": 235, "Defense": 588}, 706, src_omu, SET_DR, cls_br,
    [{"name": "Gladiator's Focus",
      "description": "Every 5s in combat, gain 100 Critical Strike. After 2 minutes, ability no longer active."}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
