"""Rogue gear batch 10 — Scintillant Amulet, Weapons of the Vale, Scalebreaker's Gear,
Grand Alliance, Crimson/Ancient Scalebreaker's armor, Shield of the North (Enclave Scout's)."""
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

# ---- Scintillant Amulet (Masterwork of Menzoberranzan) — IL 1700 (final amulet)
SET_MoM = "Masterwork of Menzoberranzan Equipment Set"
mom_eb = [{"type": "Set", "scope": "self", "stat": "Accuracy", "amount": 2.5,
           "setName": SET_MoM, "pieces": 2,
           "description": "2 of Set: When you use an encounter power, gain a stack of Speedy Anointing, granting 2.5% Accuracy and 25% Recharge Speed for 5 seconds. Stacks up to 3 times."}]
add("Scintillant Amulet", "Neck", 1700,
    {"Combat Advantage": 849, "Critical Strike": 852, "Critical Severity": 849}, 1530,
    "Menzoberranzan Masterwork crafting", SET_MoM, cls_all, mom_eb,
    abilities={"INT": 6}, set_size=2)

# ---- Scalebreaker's Wrath weapons (Set 1/11, IL 1850)
sw_eb = [{"type": "Set", "scope": "self", "stat": "Recharge Speed", "amount": 1,
          "setName": "Scalebreaker's Wrath", "pieces": 2,
          "description": "2 of Set: Use encounter/daily during combat to gain Scalebreaker's Wrath stacks. Each stack 20s: DPS +1% Recharge Speed and Action Point Gain, Tank +1% Stamina Regen and Action Point Gain, Healer +1% Movement Speed and Action Point Gain. 6 stacks empower 30s: DPS +7.5% BDB, Tank -7.5% Incoming Damage, Healer +7.5% OOH."}]
src_kk = "The Crown of Keldegonn"
add("Durgarn Thord Dagger",   "Main Hand", 1850,
    {"Critical Strike": 1388, "Critical Severity": 1388}, 1665, src_kk, "Scalebreaker's Wrath", ["Rogue"], sw_eb, set_size=2)
add("Durgarn Thord Stiletto", "Off Hand",  1850,
    {"Accuracy": 1388, "Forte": 1388}, 1665, src_kk, "Scalebreaker's Wrath", ["Rogue"], sw_eb, set_size=2)

# ---- Vale weapons (IL 1700)
v_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 5,
         "setName": "Vale", "pieces": 2,
         "description": "2 of Set: Adventurer's Might. When you use an encounter power, 10% chance to increase a Boost by 4% for 10s based on role: DPS Recharge Speed, Tank Stamina Regeneration, Healer Action Point Gain."}]
src_shar = "Sharandar"
add("Antique Handaxe of the Vale",  "Main Hand", 1700,
    {"Critical Strike": 1275, "Critical Severity": 1275}, 1530, src_shar, "Vale", ["Rogue"], v_eb, set_size=2)
add("Antique Stiletto of the Vale", "Off Hand",  1700,
    {"Accuracy": 1275, "Deflection": 1275}, 1530, src_shar, "Vale", ["Rogue"], v_eb, set_size=2)

# ---- Fortified Vale weapons (IL 1800)
fv_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 5,
          "setName": "Fortified Vale", "pieces": 2,
          "description": "2 of Set: Adventurer's Might. DPS +5% Power, Tank +5% Defense, Healer +5% Outgoing Healing. 15% chance per encounter power to gain 7.5% Boost based on role for 10s."}]
add("Fortified Handaxe of the Vale",  "Main Hand", 1800,
    {"Critical Strike": 1350, "Critical Severity": 1350}, 1620, src_shar, "Fortified Vale", ["Rogue"], fv_eb, set_size=2)
add("Fortified Stiletto of the Vale", "Off Hand",  1800,
    {"Accuracy": 1350, "Deflection": 1350}, 1620, src_shar, "Fortified Vale", ["Rogue"], fv_eb, set_size=2)

# ---- Grand Alliance weapons (IL 1700)
ga_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 3,
          "setName": "Grand Alliance", "pieces": 2,
          "description": "2 of Set: Brute's Expertise. When 20' or closer, a role stat and Forte +3%: DPS Power, Tank Awareness, Healer Outgoing Healing."}]
src_dv = "Dragonbone Vale"
add("Grand Alliance Dagger",   "Main Hand", 1700,
    {"Critical Severity": 1275, "Critical Avoidance": 1275}, 1530, src_dv, "Grand Alliance", ["Rogue"], ga_eb, set_size=2)
add("Grand Alliance Stiletto", "Off Hand",  1700,
    {"Critical Strike": 1275, "Deflect Severity": 1275}, 1530, src_dv, "Grand Alliance", ["Rogue"], ga_eb, set_size=2)

# ---- Crimson Scalebreaker's Rebel armor (Set 2/11, IL 1800)
src_csr = "Dragonbone Vale Campaign Store"
SET_CSR = "Crimson Scalebreaker's Rebel"
add("Crimson Scalebreaker's Rebel Shroud", "Head",  1800,
    {"Accuracy": 1000, "Defense": 810, "Awareness": 810}, 1620, src_csr, SET_CSR, cls_all,
    [{"name": "Executioner's Ferocity",
      "description": "When you kill an enemy, your Critical Severity increases by 5% for 10 seconds."}])
add("Crimson Scalebreaker's Rebel Hide",   "Armor", 1800,
    {"Critical Severity": 1080, "Defense": 810, "Control Resistance": 810}, 1620, src_csr, SET_CSR, cls_all,
    [{"name": "Skirmisher's Versatility",
      "description": "Whenever you deal Combat Advantage damage with your powers, you have a 10% chance to increase one of the following stats by 8% for 10 seconds: Accuracy, Combat Advantage, Critical Avoidance, or Deflect Severity. (30 second cooldown)"}])
add("Crimson Scalebreaker's Rebel Gloves", "Arms",  1800,
    {"Critical Strike": 1000, "Defense": 810, "Forte": 810}, 1620, src_csr, SET_CSR, cls_all,
    [{"name": "Herald's Cunning",
      "description": "When you have teammates within 10' of you, your Stamina Regeneration and Control Resistance is increased by 5%."}])
add("Crimson Scalebreaker's Rebel Pikes",  "Feet",  1800,
    {"Combat Advantage": 1000, "Defense": 810, "Critical Avoidance": 810}, 1620, src_csr, SET_CSR, cls_all,
    [{"name": "Renegade's Footwork",
      "description": "Whenever you Deflect an attack, gain 1% Movement Speed and Recharge Speed for 10 seconds. Max 5 Stacks: 5% Movement Speed and Recharge Speed."}])

# ---- Ancient Scalebreaker's armor (Set 2/11 Seals Store, IL 1700)
src_asc = "Dragonbone Vale Seals Store"
SET_ASC = "Ancient Scalebreaker's"
add("Ancient Scalebreaker's Shroud", "Head",  1700,
    {"Accuracy": 1020, "Defense": 765, "Awareness": 765}, 1530, src_asc, SET_ASC, cls_all,
    [{"name": "Executioner's Ferocity",
      "description": "When you kill an enemy, your Critical Severity increases by 5% for 10 seconds."}])
add("Ancient Scalebreaker's Hide",   "Armor", 1700,
    {"Critical Severity": 1020, "Defense": 765, "Control Resistance": 765}, 1530, src_asc, SET_ASC, cls_all,
    [{"name": "Skirmisher's Versatility",
      "description": "Whenever you deal CA damage with your powers, 10% chance to increase one of Accuracy/CA/Critical Avoidance/Deflect Severity by 8% for 10s. (30s CD)"}])
add("Ancient Scalebreaker's Gloves", "Arms",  1700,
    {"Critical Strike": 1020, "Defense": 765, "Forte": 765}, 1530, src_asc, SET_ASC, cls_all,
    [{"name": "Herald's Cunning",
      "description": "When you have teammates within 10' of you, your Stamina Regeneration and Control Resistance is increased by 5%."}])
add("Ancient Scalebreaker's Pikes",  "Feet",  1700,
    {"Combat Advantage": 1020, "Defense": 765, "Critical Avoidance": 765}, 1530, src_asc, SET_ASC, cls_all,
    [{"name": "Renegade's Footwork",
      "description": "Whenever you Deflect an attack, gain 1% Movement Speed and Recharge Speed for 10s. Max 5 Stacks: 5% Movement Speed and Recharge Speed."}])

# ---- Shield of the North Gear (Set 3/11, IL 1600) — Enclave Scout's
src_son = "Dragonbone Vale Seals Store / Module 22 launch"
SET_SON = "Shield of the North Gear"
add("Enclave Scout's Wristguards", "Arms",  1600,
    {"Combat Advantage": 960, "Defense": 720, "Control Resistance": 720}, 1440, src_son, SET_SON, cls_all,
    [{"name": "Leader's Ward",
      "description": "Gain 500 Deflect Severity for each player in your team."}])
add("Enclave Scout's Vest",        "Armor", 1600,
    {"Defense": 720, "Deflection": 960, "Incoming Healing": 720}, 1440, src_son, SET_SON, cls_all,
    [{"name": "Leader's Might",
      "description": "Gain 1500 Power for each player in your team."}])
add("Enclave Scout's Boots",       "Feet",  1600,
    {"Defense": 720, "Awareness": 960, "Critical Avoidance": 720}, 1440, src_son, SET_SON, cls_all,
    [{"name": "Death Defier's Focus",
      "description": "Gain 500 Critical Strike for each enemy you are engaged in battle with. (Max of 15 targets)"}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
