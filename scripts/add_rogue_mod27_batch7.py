"""Rogue gear batch 7 — Demonweb Abyssal weapons (Perfect Barb), Duergar set,
Beholder Slayer (Weaver), Stormforged/Blaspheme (Northdark Reaches),
Menzoberranzan Masterwork (Mastered Duergar), Enchanted/Menzoberranzan Bregan D'aerthe."""
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

# ---- Demonweb Empowerment — Perfect Barb of Lolth (OH) IL 2475
de_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 1,
          "setName": "Demonweb Empowerment", "pieces": 2,
          "description": "2 of Set: Your Base Damage Boost and Overall Outgoing Healing increase. Your incoming damage is reduced by up to 7.5% when your Stamina is empty. At start of Combat, Critical Strike and Critical Severity increase by 1%. Every 5s in combat, these increase by 1% (Max 5%)."}]
add("Perfect Barb of Lolth", "Off Hand", 2475,
    {"Critical Strike": 1856, "Critical Severity": 1856}, 2228,
    "The Demonweb Pits (Master)", "Demonweb Empowerment", ["Rogue"], de_eb,
    {"Damage Bonus": 1.25}, 2)

# ---- Duergar Weapon Set (IL 1900) — Northdark Reaches
duer_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 2,
            "setName": "Duergar Weapon Set", "pieces": 2,
            "description": "2 of Set: You and nearby allies are granted the following: +2% Base Damage Boost, +2% Overall Outgoing Healing, -2% Incoming Damage. This effect may stack up to 5 times when allies are equipped with a set of similar weapons."}]
add("Duergar Mercenary's Steel Dagger",   "Main Hand", 1900,
    {"Accuracy": 1425, "Critical Severity": 1425}, 1710,
    "Northdark Reaches Campaign", "Duergar Weapon Set", ["Rogue"], duer_eb, {"Damage Bonus": 1.0}, 2)
add("Duergar Mercenary's Steel Stiletto", "Off Hand",  1900,
    {"Critical Strike": 1425, "Critical Avoidance": 1425}, 1710,
    "Northdark Reaches Campaign", "Duergar Weapon Set", ["Rogue"], duer_eb, {"Damage Bonus": 1.0}, 2)

# ---- Beholder Slayer (IL 2050) — Gzemnid's Reliquary (Master)
bs_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 5,
          "setName": "Beholder Slayer", "pieces": 2,
          "description": "2 of Set: Deal or heal up to 5% additional damage based on HP percentage difference. Role: DPS +1% Base Damage Boost, Tank -2% Incoming Damage, Healer +2% Overall Outgoing Healing. Stacks up to 5 times with similarly-equipped allies. In Underdark, Damage increased 5%."}]
add("The Weaver's Knife",  "Main Hand", 2050,
    {"Critical Strike": 1538, "Critical Severity": 1538}, 1845,
    "Gzemnid's Reliquary (Master)", "Beholder Slayer", ["Rogue"], bs_eb, {"Damage Bonus": 1.25}, 2)
add("The Weaver's Dagger", "Off Hand",  2050,
    {"Accuracy": 1538, "Forte": 1538}, 1845,
    "Gzemnid's Reliquary (Master)", "Beholder Slayer", ["Rogue"], bs_eb, {"Damage Bonus": 1.25}, 2)

# ---- Stormforged (IL 2000) — Northdark Reaches Campaign
sf_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 2,
          "setName": "Stormforged", "pieces": 2,
          "description": "2 of Set: Gain 2% Base Damage Boost, -2% Incoming Damage, or 2% Overall Outgoing Healing depending on role, while in the Underdark. Additionally, gain 7.5% Base Damage Boost, -7.5% Incoming Damage, or 7.5% Overall Outgoing Healing for 15s when you dodge/block/sprint/shadow slip (30s CD)."}]
add("Stormforged Cleaver", "Main Hand", 2000,
    {"Combat Advantage": 600, "Critical Strike": 1500, "Critical Severity": 900}, 1800,
    "Northdark Reaches Campaign", "Stormforged", ["Rogue"], sf_eb, {"Damage Bonus": 1.0}, 2)
add("Stormforged Knife",   "Off Hand",  2000,
    {"Accuracy": 1500, "Deflection": 1500}, 1800,
    "Northdark Reaches Campaign", "Stormforged", ["Rogue"], sf_eb, {"Damage Bonus": 1.0}, 2)

# ---- Blaspheme (IL 1900) — Northdark Reaches Campaign
bl_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 7500,
          "setName": "Blaspheme", "pieces": 2,
          "description": "2 of Set: Gain 7500 Power/Defense/Outgoing Healing depending on role for 15s when you dodge/block/sprint/shadow slip (30s CD). When dealing CA damage, 10% chance to gain 5% Base Damage Boost/-5% Incoming Damage/5% OOH for 15s (30s CD)."}]
add("Blaspheme Cleaver", "Main Hand", 1900,
    {"Combat Advantage": 570, "Critical Strike": 1425, "Critical Severity": 855}, 1710,
    "Northdark Reaches Campaign", "Blaspheme", ["Rogue"], bl_eb, {"Damage Bonus": 0.5}, 2)
add("Blaspheme Knife",   "Off Hand",  1900,
    {"Accuracy": 1425, "Deflection": 1425}, 1710,
    "Northdark Reaches Campaign", "Blaspheme", ["Rogue"], bl_eb, {"Damage Bonus": 0.5}, 2)

# ---- Menzoberranzan Masterwork Gear (Set 3/19, IL 1900) — Mastered Duergar Mercenary pieces
src_mmw = "Menzoberranzan Masterwork crafting"
SET_MMW = "Menzoberranzan Masterwork Gear"
add("Mastered Duergar Mercenary's Barbute",  "Head",  1900,
    {"Combat Advantage": 1425, "Critical Severity": 1425}, 1710, src_mmw, SET_MMW, cls_all,
    [{"name": "Survivor's Strike",
      "description": "When your health is 50% or more, your Critical Strike is increased by 10,000. When your health is below 50%, your Accuracy is increased by 10,000. When your health is below 50%, Recharge Speed is increased by 20%."}])
add("Mastered Duergar Mercenary's Harness",  "Armor", 1900,
    {"Critical Strike": 1425, "Critical Severity": 1425}, 1710, src_mmw, SET_MMW, cls_all,
    [{"name": "Survivor's Action",
      "description": "When health is 50% or more, your Action Point Gain is increased by 7.5%. When health is below 50%, Stamina Regeneration is increased by 15%."}])
add("Mastered Duergar Mercenary's Punchers", "Arms",  1900,
    {"Combat Advantage": 1425, "Critical Severity": 1425}, 1710, src_mmw, SET_MMW, cls_all,
    [{"name": "Survivor's Savagery",
      "description": "When health is 50% or more, your Critical Strike is increased by 10,000. When health is below 50%, Critical Avoidance is increased by 10,000."}])
add("Mastered Duergar Mercenary's Trodders", "Feet",  1900,
    {"Combat Advantage": 1425, "Critical Strike": 1425}, 1710, src_mmw, SET_MMW, cls_all,
    [{"name": "Survivor's Finesse",
      "description": "When health is 50% or more, your Critical Severity is increased by 10,000. When health is below 50%, Movement Speed is increased by 20%."}])

# ---- Enchanted Menzoberranzan Gear (Set 5/19, IL 2050) — Enchanted Bregan D'aerthe Assassin's
src_emz = "Demonweb Pits Campaign Store (Enchanted)"
SET_EMZ = "Enchanted Menzoberranzan Gear"
add("Enchanted Bregan D'aerthe Assassin's Hat",       "Head",  2050,
    {"Critical Strike": 1538, "Critical Severity": 1538}, 1845, src_emz, SET_EMZ, cls_all,
    [{"name": "Charged Precision",
      "description": "When your Stamina is over 75%, your Accuracy is increased by 10%."}])
add("Enchanted Bregan D'aerthe Assassin's Leathers",  "Armor", 2050,
    {"Accuracy": 1538, "Combat Advantage": 1538}, 1845, src_emz, SET_EMZ, cls_all,
    [{"name": "Liquid Luck",
      "description": "Gain 1.5% Critical Strike for each player in your team. When moving, gain 8% Critical Severity."}])
add("Enchanted Bregan D'aerthe Assassin's Band",      "Arms",  2050,
    {"Accuracy": 1538, "Critical Strike": 923, "Awareness": 615}, 1845, src_emz, SET_EMZ, cls_all,
    [{"name": "Escalating Torrent",
      "description": "Gain 400 Power for 10s when you strike an enemy, lose a stack when struck. Stacks 20 times."}])
add("Enchanted Bregan D'aerthe Assassin's Longboots", "Feet",  2050,
    {"Combat Advantage": 923, "Critical Severity": 1538, "Defense": 615}, 1845, src_emz, SET_EMZ, cls_all,
    [{"name": "Brute's Expertise",
      "description": "When 20' or closer to your target, Critical Severity is increased by 7.5%. When 20' or further away, Forte is increased by 7.5%."}])

# ---- Menzoberranzan Gear (Set 6/19, IL 2000) — Bregan D'aerthe Assassin's
src_mz = "Menzoberranzan Campaign Store"
SET_MZ = "Menzoberranzan Gear"
add("Bregan D'aerthe Assassin's Hat",      "Head",  2000,
    {"Critical Strike": 1500, "Critical Severity": 1500}, 1800, src_mz, SET_MZ, cls_all,
    [{"name": "Charged Precision",
      "description": "When Stamina is over 75%, Accuracy is increased by 7.5%."}])
add("Bregan D'aerthe Assassin's Leathers", "Armor", 2000,
    {"Accuracy": 1500, "Combat Advantage": 1500}, 1800, src_mz, SET_MZ, cls_all,
    [{"name": "Liquid Luck",
      "description": "Gain 1% Critical Strike for each player in your team. When moving, gain 5% Critical Severity."}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
