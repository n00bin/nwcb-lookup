"""Rogue gear batch 6 — Ultraviolet/Radiant Elven Armor, Cosmic Corsair's (Starhide),
Pulsar Armor, Astral Raider's Armor, Lolthian Gear, Abyssal weapons (Perfect Edge of Lolth)."""
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

# ---- Ultraviolet Armor (IL 2900) — remaining pieces
src_uv = "The Imperial Citadel (Master) / Doomspace"
SET_UV = "Ultraviolet Armor"
add("Ultraviolet Elven Vest", "Armor", 2900,
    {"Critical Strike": 2175, "Forte": 2175}, 2610, src_uv, SET_UV, cls_all,
    [{"name": "Focused Daily",
      "description": "When you use a Daily power, your next encounter power will deal 20% more damage. (10 second cooldown). Additionally, when Focused Daily triggers, you gain 2.5% Critical Severity for 10s."}])
add("Ultraviolet Elven Wristguards", "Arms", 2900,
    {"Accuracy": 1088, "Combat Advantage": 2175, "Forte": 1088}, 2610, src_uv, SET_UV, cls_all,
    [{"name": "Challenger's Precision",
      "description": "When in combat with only 1 enemy, your Critical Strike is increased by 1.5% every 2 seconds. Max 5 stacks: 7.5% Critical Strike."}])
add("Ultraviolet Elven Jackboots", "Feet", 2900,
    {"Critical Strike": 2175, "Critical Severity": 2175}, 2610, src_uv, SET_UV, cls_all,
    [{"name": "Wildspace Predator",
      "description": "+7% Damage in Wildspace. +2% Damage in non-Wildspace."}])

# ---- Radiant Elven Armor (Set 3/17, IL 2800)
src_rev = "The Imperial Citadel (Advanced) / Doomspace"
SET_REV = "Radiant Elven Armor"
add("Radiant Elven Cap",     "Head",  2800,
    {"Combat Advantage": 2100, "Critical Severity": 2100}, 2520, src_rev, SET_REV, cls_all,
    [{"name": "Spelljammer's Grace",
      "description": "For every 5 seconds you are in combat in Wildspace, you gain 0.85% Forte. Max Stacks: 7 (10 in Wildspace)."}])
add("Radiant Elven Jerkin",  "Armor", 2800,
    {"Critical Strike": 2100, "Forte": 2100}, 2520, src_rev, SET_REV, cls_all,
    [{"name": "Shielded Strength",
      "description": "When you have a Shield or Temp HP in Wildspace, gain 5% Damage and 2.5% Critical Severity. In non-Wildspace, the Damage bonus is reduced to 2%."}])
add("Radiant Elven Armband", "Arms",  2800,
    {"Accuracy": 1050, "Combat Advantage": 2100, "Forte": 1050}, 2520, src_rev, SET_REV, cls_all,
    [{"name": "Challenger's Presence",
      "description": "When in combat with only 1 enemy, every 2 seconds you gain 875 Power and 0.5% Critical Strike. Max 5 stacks: 4,375 Power and 2.5% Critical Strike."}])
add("Radiant Elven Boots",   "Feet",  2800,
    {"Critical Strike": 2100, "Critical Severity": 2100}, 2520, src_rev, SET_REV, cls_all,
    [{"name": "Wildspace Precision",
      "description": "+7.5% Critical Strike in Wildspace. +3% Critical Strike in non-Wildspace."}])

# ---- Cosmic Corsair's Armor (Set 5/17, IL 2700) — Starhide pieces
src_cc = "Defense of the Moondancer (Master)"
SET_CC = "Cosmic Corsair's Armor"
add("Starhide Cap",     "Head",  2700,
    {"Critical Severity": 2025, "Forte": 2025}, 2430, src_cc, SET_CC, cls_all,
    [{"name": "Maximized Opportunity",
      "description": "When in combat with only one enemy, your Combat Advantage is increased by 7%."}])
add("Starhide Jerkin",  "Armor", 2700,
    {"Critical Strike": 2025, "Critical Severity": 2025}, 2430, src_cc, SET_CC, cls_all,
    [{"name": "Focused Daily",
      "description": "When you deal damage with a Daily power, your next encounter power will deal 20% more damage. (30 second cooldown)"}])
add("Starhide Armband", "Arms",  2700,
    {"Accuracy": 2025, "Combat Advantage": 2025}, 2430, src_cc, SET_CC, cls_all,
    [{"name": "Butcher's Zeal",
      "description": "When you damage or heal your target for more than 15% of your Maximum Hit Points in a single blow, you gain 10 Action Points. Can only occur once every 5 seconds."}])
add("Starhide Boots",   "Feet",  2700,
    {"Combat Advantage": 2025, "Critical Strike": 2025}, 2430, src_cc, SET_CC, cls_all,
    [{"name": "Wildspace Hunter",
      "description": "+5% Damage in Wildspace."}])

# ---- Pulsar Armor (Set 6/17, IL 2600)
src_pa = "Defense of the Moondancer (Advanced)"
SET_PA = "Pulsar Armor"
add("Pulsar Hat",         "Head",  2600,
    {"Critical Strike": 1950, "Critical Severity": 1170, "Defense": 780}, 2340, src_pa, SET_PA, cls_all,
    [{"name": "Executioner's Grace",
      "description": "When you kill an enemy, your Forte increases by 7.5% for 10 seconds."}])
add("Pulsar Vest",        "Armor", 2600,
    {"Combat Advantage": 1950, "Critical Strike": 1170, "Forte": 780}, 2340, src_pa, SET_PA, cls_all,
    [{"name": "Defender Strike",
      "description": "Gain -1% Incoming Damage when you strike an enemy. Stacks 5 times. When you are struck, the stacks are consumed and you gain 1% Base Damage Boost per stack consumed for 10 seconds. Stacks cannot be applied at the same time."}])
add("Pulsar Wristguards", "Arms",  2600,
    {"Accuracy": 1950, "Combat Advantage": 1170, "Critical Severity": 780}, 2340, src_pa, SET_PA, cls_all,
    [{"name": "Escalating Torrent",
      "description": "Gain 400 Power for 10 seconds when you strike an enemy, lose a stack when you are struck. Stacks 20 times."}])
add("Pulsar Half-Boots",  "Feet",  2600,
    {"Accuracy": 780, "Combat Advantage": 1170, "Critical Severity": 1950}, 2340, src_pa, SET_PA, cls_all,
    [{"name": "Tenacious Luck",
      "description": "When in combat with only one enemy, your Critical Strike is increased by 7%."}])

# ---- Astral Raider's Armor (Set 7/17, IL 2200) — Xaryxian Invasions
src_ar = "Xaryxian Invasions"
SET_AR = "Astral Raider's Armor"
add("Astral Raider's Hat",          "Head",  2200,
    {"Critical Strike": 1320, "Outgoing Healing": 990}, 1980, src_ar, SET_AR, cls_all,
    [{"name": "Reckless Brutality",
      "description": "Whenever you deal damage to an enemy gain a stack of Reckless Brutality, increasing your Power by 2000 but increasing your damage taken by 2% for 5 seconds. (Max 5 stacks)"}])
add("Astral Raider's Vest",         "Armor", 2200,
    {"Defense": 990, "Deflection": 1320, "Incoming Healing": 990}, 1980, src_ar, SET_AR, cls_all,
    [{"name": "Death Defying Advantage",
      "description": "Gain 2% Combat Advantage for each enemy you are engaged in battle within 100'. (Max of 10 targets)"}])
add("Astral Raider's Wristguards",  "Arms",  2200,
    {"Combat Advantage": 1320, "Defense": 990, "Control Resistance": 990}, 1980, src_ar, SET_AR, cls_all,
    [{"name": "Scaled Power",
      "description": "Grants up to 70% bonus Damage when your total item level is being scaled down. Disabled in Thay Arena PvP."}])
add("Astral Raider's Jackboots",    "Feet",  2200,
    {"Defense": 990, "Awareness": 1320, "Critical Avoidance": 990}, 1980, src_ar, SET_AR, cls_all,
    [{"name": "Scaled Disdain",
      "description": "Grants up to -70% Incoming Damage when your total item level is being scaled down."}])

# ---- Lolthian Gear (Set 8/17, IL 2050) — Seals Store / Module 27 launch (Light of Xaryxis)
src_lo = "Seals Store (Seals of the Spider God) / Module 27 launch"
SET_LO = "Lolthian Gear"
add("Lolthian Shroud", "Head",  2050,
    {"Accuracy": 1230, "Critical Severity": 923, "Defense": 923}, 1845, src_lo, SET_LO, cls_all,
    [{"name": "Skirmisher's Might",
      "description": "Whenever you deal Combat Advantage damage with your powers, you have a 10% chance to gain 7500 Power for 10 seconds. (20 second cooldown)"}])
add("Lolthian Jacket", "Armor", 2050,
    {"Critical Severity": 1230, "Defense": 923, "Control Bonus": 923}, 1845, src_lo, SET_LO, cls_all,
    [{"name": "Charged Focus",
      "description": "When Action Points are full, your Critical Severity is increased by 5000."}])
add("Lolthian Band",   "Arms",  2050,
    {"Critical Strike": 1538, "Defense": 1538}, 1845, src_lo, SET_LO, cls_all,
    [{"name": "Executioner's Ferocity",
      "description": "When you kill an enemy, your Critical Severity increases by 5% for 10 seconds."}])
add("Lolthian Pikes",  "Feet",  2050,
    {"Combat Advantage": 1230, "Defense": 923, "Critical Avoidance": 923}, 1845, src_lo, SET_LO, cls_all,
    [{"name": "Gladiator's Advantage",
      "description": "For every 5 seconds you are in combat, you gain 650 Combat Advantage, to the max of 7800."}])

# ---- Abyssal (Master) Gear weapons — Demonweb Empowerment set
de_eb = [{"type": "Set", "scope": "self", "stat": "Movement Speed", "amount": 10,
          "setName": "Demonweb Empowerment", "pieces": 2,
          "description": "2 of Set: +10% Movement Speed in the Demonweb. Bonus combat synergy with Lolthian gear."}]
add("Perfect Edge of Lolth", "Main Hand", 2475,
    {"Combat Advantage": 1856, "Critical Strike": 1856}, 2228,
    "The Demonweb Pits (Master)", "Demonweb Empowerment", ["Rogue"], de_eb,
    {"Damage Bonus": 1.25}, 2)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
