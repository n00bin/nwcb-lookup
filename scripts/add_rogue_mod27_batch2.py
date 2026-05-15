"""Mod 27 Rogue continued — Forsaken/Dirge weapons, Doomed Reaver/Dread March armor, Crystalline weapons."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Mod 27 Rogue gear — screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes, equip=None, percent=None, set_size=2, abilities=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": percent or {}, "abilityBonuses": abilities or {},
        "allowedClasses": classes, "notes": INTAKE}
    data.append(entry)

# Essence Reap (Greater) — Shadepiercer's Cull (OH) + Venomshade Talon (MH), IL 4000
er_greater_eb = [{"type": "Set", "scope": "self", "stat": "Movement Speed", "amount": 14,
                  "setName": "Essence Reap (Greater)", "pieces": 2,
                  "description": "2 of Set: While in Thay, your Movement Speed is increased by 14% and your Damage is increased by 2.5%. Whenever you deal Combat Advantage damage with your powers, you have a 10% chance to deal an additional 4% of the following stats by 4.2% for 10 seconds: Accuracy, Combat Advantage. (10 second cooldown)"}]
add("Shadepiercer's Cull",  "Off Hand",  4000, {"Critical Severity": 3960, "Defense": 2700}, 3600, "Shackles of Divinity (Master)", "Essence Reap (Greater)", ["Rogue"], er_greater_eb)
add("Venomshade Talon",     "Main Hand", 4000, {"Combat Advantage": 2160, "Critical Strike": 3960}, 3600, "Shackles of Divinity (Master)", "Essence Reap (Greater)", ["Rogue"], er_greater_eb, {"Damage Bonus": 1.0})

# Essence Reap (base) — Shadepiercer's Fang (OH) + Venomshade Knife (MH), IL 3800
er_eb = [{"type": "Set", "scope": "self", "stat": "Movement Speed", "amount": 10,
          "setName": "Essence Reap", "pieces": 2,
          "description": "2 of Set: While in Thay, your Movement Speed is increased by 10%. Whenever you deal Combat Advantage damage with your powers, you have one of the following stats by 4.2% for 10 seconds: Accuracy, Combat Advantage. (15 second cooldown)"}]
add("Shadepiercer's Fang", "Off Hand",  3800, {"Critical Severity": 3762, "Defense": 2565}, 3420, "Shackles of Divinity (Advanced)", "Essence Reap", ["Rogue"], er_eb)
add("Venomshade Knife",    "Main Hand", 3800, {"Combat Advantage": 2052, "Critical Strike": 3762}, 3420, "Shackles of Divinity (Advanced)", "Essence Reap", ["Rogue"], er_eb, {"Damage Bonus": 0.5})

# Umbral Stride (Thayan Zealot weapons, IL 3300 — paralleling Warlock Profaned Pact Blade / Doomscript Grimoire)
us_eb = [{"type": "Set", "scope": "self", "stat": "Movement Speed", "amount": 10,
          "setName": "Umbral Stride", "pieces": 2,
          "description": "2 of Set: While in Thay, Movement Speed +10%. Every 3s in combat, gain Umbral Stride stack: General +0.35% Power, DPS +0.5% Critical Severity, Healer +0.4% Outgoing Healing, Tank +0.4% Awareness. Max 10 stacks."}]
add("Withering Stiletto of the Thayan Zealot",  "Main Hand", 3300, {"Accuracy": 3539, "Forte": 2005}, 2970, "Adventures in Thay", "Umbral Stride", ["Rogue"], us_eb)
add("Nightpiercer Dagger of the Thayan Zealot", "Main Hand", 3300, {"Critical Strike": 2673, "Critical Severity": 3267}, 2970, "Adventures in Thay", "Umbral Stride", ["Rogue"], us_eb)

# Doomed Reaver Armor (Set 4/21, IL 5000) — leather class set, shared Rogue/Cleric/Bard/Ranger
src_dr = "Soul Harvest (Master) (Module 27)"
dra_classes = ["Rogue", "Cleric", "Bard", "Ranger"]
add("Cuirass of the Scarlet Arcanum",   "Armor", 5000, {"Accuracy": 3218, "Combat Advantage": 1980, "Forte": 2228}, 4500, src_dr, "Doomed Reaver Armor", dra_classes, [{"name": "Focused Burst", "description": "When you use a Daily power, for the next 30 seconds your next Encounter Power deals +75% more Damage."}], None, 4)
add("Greaves of the Scarlet Arcanum",   "Feet",  5000, {"Combat Advantage": 3300, "Critical Severity": 4050}, 4500, src_dr, "Doomed Reaver Armor", dra_classes, [{"name": "Momentum's Edge", "description": "While moving, gain +0.5% Power and +0.6% Combat Advantage. If you stand still for more than 3 seconds, you lose all stacks. Max 5 Stacks: +2.5% Power and +3% Combat Advantage."}], None, 4)

# Dread March Armor (Set 5/21, IL 4700) — shared leather class set
src_dm = "Soul Harvest (Advanced) (Module 27)"
add("Hauberk of the Crimson Gale",  "Armor", 4700, {"Critical Strike": 3807, "Forte": 3490}, 4230, src_dm, "Dread March Armor", dra_classes, [{"name": "Lethal Focus", "description": "When you damage your target for more than 15% of your Maximum Hit Points in a single blow, you gain +3% Power and +4% Accuracy for 7 seconds (5 second cooldown)."}], None, 4)
add("Greaves of the Crimson Gale",  "Feet",  4700, {"Combat Advantage": 3102, "Forte": 2855}, 4230, src_dm, "Dread March Armor", dra_classes, [{"name": "Kinetic Precision", "description": "While moving, gain +1% Power and +0.7% Combat Advantage. If you stand still for more than 4 seconds, you lose all stacks. Max 5 Stacks: +5% Power and +3.5% Combat Advantage."}], None, 4)

# Crystalline Weapons (Set 1/11 Pirate's Skyhold / Dread Sanctum) — Bismuth + Crystal Dagger/Dirk
prismatic_eb = [{"type": "Set", "scope": "self", "stat": "Movement Speed", "amount": 12,
                 "setName": "Prismatic Defier of Dread", "pieces": 2,
                 "description": "2 of Set: While in the Pirates' Skyhold or Dread Sanctum, your Movement Speed is increased by 12%. Every 3s in combat, gain a stack of Prismatic Force. Each stack: General +0.35% Power, DPS +0.5% Critical Severity, Healer +0.4% Overall Outgoing Healing, Tank +0.4% Awareness. Max 10 stacks."}]
add("Bismuth Dagger", "Main Hand", 3400, {"Accuracy": 3315, "Forte": 2295}, 3060, "Pirates' Skyhold / Dread Sanctum", "Prismatic Defier of Dread", ["Rogue"], prismatic_eb, {"Damage Bonus": 1.0})
add("Bismuth Dirk",   "Off Hand",  3400, {"Accuracy": 3315, "Forte": 2295}, 3060, "Pirates' Skyhold / Dread Sanctum", "Prismatic Defier of Dread", ["Rogue"], prismatic_eb, {"Damage Bonus": 1.0})
add("Crystal Dagger", "Main Hand", 3100, {"Critical Strike": 2790, "Critical Severity": 2790}, 2790, "Pirates' Skyhold / Dread Sanctum", "Prismatic Defier of Dread", ["Rogue"], prismatic_eb, {"Damage Bonus": 1.0})

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
