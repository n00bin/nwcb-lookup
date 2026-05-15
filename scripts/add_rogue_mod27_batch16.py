"""Rogue gear batch 16 — Devil Forged remaining (Hide/Gaiters), Demon Forged remaining
(Hide/Bracers), Infernal Forged generic (IL 1200, Vallenhas Seals, all 4 pieces)."""
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

cls_all = ["Cleric", "Bard", "Rogue", "Ranger"]
src_ic = "Infernal Citadel Epic Dungeon"
src_vh = "Vallenhas Seals Store"

# ---- Devil Forged remaining pieces
SET_DEV = "Infernal Forged Armor (Devil Forged)"
add("Devil Forged Hide", "Armor", 1215,
    {"Critical Severity": 911, "Defense": 911}, 1094, src_ic, SET_DEV, cls_all,
    [{"name": "Leader's Guard",
      "description": "Gain 1000 Defense for each player in your team."},
     {"name": "Devil Hunter",
      "description": "+1% Damage against Demons."}])
add("Devil Forged Gaiters", "Feet", 1215,
    {"Combat Advantage": 364, "Critical Strike": 547, "Defense": 911}, 1094, src_ic, SET_DEV, cls_all,
    [{"name": "Gladiator's Might",
      "description": "Every 5s in combat, gain 200 Power. Max 24 Stacks: 4800 Power."},
     {"name": "Devil Hunter",
      "description": "+1% Damage against Demons."}])

# ---- Demon Forged remaining pieces
SET_DEM = "Infernal Forged Armor (Demon Forged)"
add("Demon Forged Hide",    "Armor", 1215,
    {"Critical Severity": 911, "Defense": 911}, 1094, src_ic, SET_DEM, cls_all,
    [{"name": "Leader's Guard",
      "description": "Gain 1000 Defense for each player in your team."},
     {"name": "Devil Hunter",
      "description": "+1% Damage against Devils."}])
add("Demon Forged Bracers", "Arms",  1215,
    {"Accuracy": 364, "Critical Severity": 547, "Defense": 911}, 1094, src_ic, SET_DEM, cls_all,
    [{"name": "Survivor's Might",
      "description": "When you Deflect, gain 1000 Power for 10s. Max 5 Stacks."},
     {"name": "Devil Hunter",
      "description": "+1% Damage against Devils."}])

# ---- Infernal Forged Armor (Generic IL 1200, Vallenhas Seals)
SET_IF = "Infernal Forged Armor"
add("Infernal Forged Hood",    "Head",  1200,
    {"Combat Advantage": 360, "Critical Strike": 540, "Defense": 900}, 1080, src_vh, SET_IF, cls_all,
    [{"name": "Skirmisher's Might",
      "description": "10% chance to gain 5000 Power for 10s on CA damage. (30s CD)"}])
add("Infernal Forged Hide",    "Armor", 1200,
    {"Critical Severity": 900, "Defense": 900}, 1080, src_vh, SET_IF, cls_all,
    [{"name": "Leader's Guard",
      "description": "Gain 1000 Defense for each player in your team."}])
add("Infernal Forged Bracers", "Arms",  1200,
    {"Accuracy": 360, "Critical Severity": 540, "Defense": 900}, 1080, src_vh, SET_IF, cls_all,
    [{"name": "Survivor's Might",
      "description": "When you Deflect, gain 1000 Power for 10s. Max 5 Stacks."}])
add("Infernal Forged Gaiters", "Feet",  1200,
    {"Combat Advantage": 360, "Critical Strike": 540, "Defense": 900}, 1080, src_vh, SET_IF, cls_all,
    [{"name": "Gladiator's Might",
      "description": "Every 5s in combat, gain 200 Power. Max 24 Stacks: 4800 Power."}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
