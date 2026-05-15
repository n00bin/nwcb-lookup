"""Rogue gear batch 15 — Infernal Forged Armor variants:
Fiend Forged (Master, IL 1230) + Devil/Demon Forged (Advanced, IL 1215)."""
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

src_ic = "Infernal Citadel Epic Dungeon"
cls_all = ["Cleric", "Bard", "Rogue", "Ranger"]

# ---- Fiend Forged (Set 8/11 Master, IL 1230) — Cleric/Bard/Rogue/Ranger
SET_FF = "Infernal Forged Armor (Fiend Forged)"
add("Fiend Forged Hood",    "Head",  1230,
    {"Combat Advantage": 369, "Critical Strike": 554, "Defense": 922}, 1107, src_ic, SET_FF, cls_all,
    [{"name": "Skirmisher's Might",
      "description": "Whenever you deal Combat Advantage damage with your powers, you have a 10% chance to gain 5000 Power for 10 seconds. (30 second cooldown)"},
     {"name": "Fiend Hunter",
      "description": "+1% Damage against Demons, Devils, and Fiends."}])
add("Fiend Forged Hide",    "Armor", 1230,
    {"Critical Severity": 922, "Defense": 922}, 1107, src_ic, SET_FF, cls_all,
    [{"name": "Leader's Guard",
      "description": "Gain 1000 Defense for each player in your team."},
     {"name": "Fiend Hunter",
      "description": "+1% Damage against Demons, Devils, and Fiends."}])
add("Fiend Forged Bracers", "Arms",  1230,
    {"Accuracy": 369, "Critical Severity": 554, "Defense": 922}, 1107, src_ic, SET_FF, cls_all,
    [{"name": "Survivor's Might",
      "description": "Whenever you Deflect an attack, gain 1000 Power for 10 seconds. (Max 5 stacks)"},
     {"name": "Fiend Hunter",
      "description": "+1% Damage against Demons, Devils, and Fiends."}])
add("Fiend Forged Gaiters", "Feet",  1230,
    {"Combat Advantage": 369, "Critical Strike": 554, "Defense": 922}, 1107, src_ic, SET_FF, cls_all,
    [{"name": "Gladiator's Might",
      "description": "For every 5 seconds you are in combat, you gain 200 Power. Max 24 Stacks: 4800 Power."},
     {"name": "Fiend Hunter",
      "description": "+1% Damage against Demons, Devils, and Fiends."}])

# ---- Devil Forged (Advanced, IL 1215) — +1% Damage against Demons
SET_DEV = "Infernal Forged Armor (Devil Forged)"
add("Devil Forged Hood",    "Head",  1215,
    {"Combat Advantage": 364, "Critical Strike": 547, "Defense": 911}, 1094, src_ic, SET_DEV, cls_all,
    [{"name": "Skirmisher's Might",
      "description": "10% chance to gain 5000 Power for 10s on CA damage. (30s CD)"},
     {"name": "Devil Hunter",
      "description": "+1% Damage against Demons."}])
add("Devil Forged Bracers", "Arms",  1215,
    {"Accuracy": 364, "Critical Severity": 547, "Defense": 911}, 1094, src_ic, SET_DEV, cls_all,
    [{"name": "Survivor's Might",
      "description": "When you Deflect, gain 1000 Power for 10s. Max 5 Stacks."},
     {"name": "Devil Hunter",
      "description": "+1% Damage against Demons."}])

# ---- Demon Forged (Advanced, IL 1215) — +1% Damage against Devils
SET_DEM = "Infernal Forged Armor (Demon Forged)"
add("Demon Forged Hood",    "Head",  1215,
    {"Combat Advantage": 364, "Critical Strike": 547, "Defense": 911}, 1094, src_ic, SET_DEM, cls_all,
    [{"name": "Skirmisher's Might",
      "description": "10% chance to gain 5000 Power for 10s on CA damage. (30s CD)"},
     {"name": "Devil Hunter",
      "description": "+1% Damage against Devils."}])
add("Demon Forged Gaiters", "Feet",  1215,
    {"Combat Advantage": 364, "Critical Strike": 547, "Defense": 911}, 1094, src_ic, SET_DEM, cls_all,
    [{"name": "Gladiator's Might",
      "description": "Every 5s in combat, gain 200 Power. Max 24 Stacks: 4800 Power."},
     {"name": "Devil Hunter",
      "description": "+1% Damage against Devils."}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
