"""Rogue gear batch 8 — Menzoberranzan Bregan D'aerthe (remaining), Exalted Dark Maiden's,
Dark Maiden's Assault, Dragonsteel/Dragonhide."""
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

cls_all = ["Rogue", "Cleric", "Bard", "Ranger"]

# ---- Menzoberranzan Gear (remaining Bregan D'aerthe pieces)
src_mz = "Menzoberranzan Campaign Store"
SET_MZ = "Menzoberranzan Gear"
add("Bregan D'aerthe Assassin's Band",      "Arms",  2000,
    {"Accuracy": 1500, "Critical Strike": 900, "Awareness": 600}, 1800, src_mz, SET_MZ, cls_all,
    [{"name": "Escalating Torrent",
      "description": "Gain 375 Power for 10s when you strike an enemy, lose a stack when struck. Stacks 20 times."}])
add("Bregan D'aerthe Assassin's Longboots", "Feet",  2000,
    {"Combat Advantage": 900, "Critical Severity": 1500, "Defense": 600}, 1800, src_mz, SET_MZ, cls_all,
    [{"name": "Brute's Expertise",
      "description": "When 20' or closer to target, Critical Severity +5%. When 20'+ away, Forte +5%."}])

# ---- Exalted Dark Maiden's Gear (Set 7/19, IL 2050) — Master
src_edm = "Menzoberranzan Campaign Store (Master)"
SET_EDM = "Exalted Dark Maiden's Gear"
add("Exalted Maiden's Assault Shroud",  "Head",  2050,
    {"Accuracy": 1538, "Defense": 1538}, 1845, src_edm, SET_EDM, cls_all,
    [{"name": "Executioner's Zeal",
      "description": "When you kill an enemy, you gain 3% Action Points."}])
add("Exalted Maiden's Assault Hide",    "Armor", 2050,
    {"Critical Strike": 1230, "Critical Severity": 923, "Defense": 923}, 1845, src_edm, SET_EDM, cls_all,
    [{"name": "Maiden's Blade",
      "description": "You do 6% more damage to enemies that are not facing you. This bonus doubles in the Underdark."}])
add("Exalted Maiden's Assault Gloves",  "Arms",  2050,
    {"Critical Strike": 1538, "Defense": 1538}, 1845, src_edm, SET_EDM, cls_all,
    [{"name": "Critical Force",
      "description": "Whenever you Critically Strike with your Powers, you have a 15% chance to deal 175 magnitude damage around you. This effect may only occur once every 15 seconds."}])
add("Exalted Maiden's Assault Gaiters", "Feet",  2050,
    {"Combat Advantage": 1230, "Critical Severity": 923, "Defense": 923}, 1845, src_edm, SET_EDM, cls_all,
    [{"name": "Spider's Bane",
      "description": "Gain 5,000 Power and more role effectiveness in Temple of the Spider. DPS +6% Base Damage Boost, Tank -6% Incoming Damage, Healer +6% Overall Outgoing Healing."}])

# ---- Dark Maiden's Gear (Set 8/19, IL 2000)
src_dm = "Northdark Reaches Campaign Store"
SET_DM = "Dark Maiden's Gear"
add("The Dark Maiden's Assault Shroud",  "Head",  2000,
    {"Accuracy": 1500, "Defense": 1500}, 1800, src_dm, SET_DM, cls_all,
    [{"name": "Executioner's Zeal",
      "description": "When you kill an enemy, you gain 1% Action Points."}])
add("The Dark Maiden's Assault Hide",    "Armor", 2000,
    {"Critical Strike": 1200, "Critical Severity": 900, "Defense": 900}, 1800, src_dm, SET_DM, cls_all,
    [{"name": "Maiden's Blade",
      "description": "You do 5% more damage to enemies that are not facing you. This bonus doubles in the Underdark."}])
add("The Dark Maiden's Assault Gloves",  "Arms",  2000,
    {"Critical Strike": 1500, "Defense": 1500}, 1800, src_dm, SET_DM, cls_all,
    [{"name": "Critical Force",
      "description": "Whenever you Critically Strike with your Powers, you have a 10% chance to deal 150 magnitude damage around you. This effect may only occur once every 15 seconds."}])
add("The Dark Maiden's Assault Gaiters", "Feet",  2000,
    {"Combat Advantage": 1200, "Critical Severity": 900, "Defense": 900}, 1800, src_dm, SET_DM, cls_all,
    [{"name": "Spider's Bane",
      "description": "Gain 4,500 Power in the Underdark. DPS +5% Base Damage Boost, Tank -5% Incoming Damage, Healer +5% Overall Outgoing Healing in Temple of the Spider."}])

# ---- Dragonsteel Gear (Set 9/19, IL 1900) — Dragonhide (Module 24)
src_dh = "Northdark Reaches Seals Store / Module 24"
SET_DH = "Dragonsteel Gear"
add("Dragonhide Shroud", "Head",  1900,
    {"Accuracy": 1140, "Critical Severity": 855, "Defense": 855}, 1710, src_dh, SET_DH, cls_all,
    [{"name": "Dragon Hunter's Might",
      "description": "+5% Damage against Dragons. When health is below 50%, Awareness is increased by 8,000."}])
add("Dragonhide Jacket", "Armor", 1900,
    {"Critical Severity": 1140, "Defense": 855, "Control Bonus": 855}, 1710, src_dh, SET_DH, cls_all,
    [{"name": "Leader's Power",
      "description": "Gain 1000 Power and Critical Strike for each player in your team."}])
add("Dragonhide Band",   "Arms",  1900,
    {"Critical Strike": 1425, "Defense": 1425}, 1710, src_dh, SET_DH, cls_all,
    [{"name": "Charged At-Will",
      "description": "Whenever you activate a Daily power, increase damage of your at-will attacks by 15% for 10s. (20s cooldown)"}])
add("Dragonhide Pikes",  "Feet",  1900,
    {"Combat Advantage": 1140, "Defense": 855, "Critical Avoidance": 855}, 1710, src_dh, SET_DH, cls_all,
    [{"name": "This or That",
      "description": "When not in a party, gain 3,000 Defense. When in a party, gain 10,000 Accuracy."}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
