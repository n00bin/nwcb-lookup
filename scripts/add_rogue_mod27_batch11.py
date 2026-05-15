"""Rogue gear batch 11 — Enclave Scout's Hat, Forest Guardian's Raid (Vault of Stars 4-pc),
Weathered Wood Gear (Module 20 4-pc), The Crone's Gear (Module 20 Seals 4-pc),
Oathkeeper of the Blessed Blade (Module 19, 2 IL tiers)."""
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

# ---- Enclave Scout's Hat (Shield of the North) IL 1600 — final piece
src_son = "Dragonbone Vale Seals Store / Module 22 launch"
SET_SON = "Shield of the North Gear"
add("Enclave Scout's Hat", "Head", 1600,
    {"Critical Strike": 960, "Defense": 720, "Incoming Healing": 720}, 1440, src_son, SET_SON, cls_all,
    [{"name": "Charged Precision",
      "description": "When Stamina is over 75%, Accuracy is increased by 7.5%."}])

# ---- Forest Guardian's Gear (Set 1/10, IL 1500) — Vault of Stars
src_fg = "Vault of Stars Epic Dungeon"
SET_FG = "Forest Guardian's Gear"
add("Forest Guardian's Raid Coif",     "Head",  1500,
    {"Combat Advantage": 675, "Defense": 1125, "Control Bonus": 450}, 1350, src_fg, SET_FG, cls_all,
    [{"name": "Fey Hunter",
      "description": "+3% Damage in all of Sharandar."}])
add("Forest Guardian's Raid Leathers", "Armor", 1500,
    {"Accuracy": 1125, "Defense": 1125}, 1350, src_fg, SET_FG, cls_all,
    [{"name": "Leader's Awareness",
      "description": "Gain 1500 Awareness for each player in your team."}])
add("Forest Guardian's Raid Braces",   "Arms",  1500,
    {"Accuracy": 450, "Critical Severity": 675, "Defense": 1125}, 1350, src_fg, SET_FG, cls_all,
    [{"name": "Death Defier's Accuracy",
      "description": "Gain 500 Accuracy for each enemy you are engaged in battle with. (Max of 15 targets)"}])
add("Forest Guardian's Raid Cuisses",  "Feet",  1500,
    {"Combat Advantage": 450, "Critical Strike": 675, "Defense": 1125}, 1350, src_fg, SET_FG, cls_all,
    [{"name": "Charged Mastery",
      "description": "When your Stamina is over 75%, your Combat Advantage is increased by 7500."}])

# ---- Weathered Wood Gear (Set 2/10, IL 1300) — Module 20 Seals
src_ww = "Sharandar Seals Store / Module 20 launch"
SET_WW = "Weathered Wood Gear"
add("Weathered Wood Hood",    "Head",  1300,
    {"Combat Advantage": 585, "Defense": 975, "Control Bonus": 390}, 1170, src_ww, SET_WW, cls_all,
    [{"name": "Skirmisher's Might",
      "description": "Whenever you deal Combat Advantage damage with your powers, you have a 10% chance to gain 5000 Power for 10 seconds. (30 second cooldown)"}])
add("Weathered Wood Hide",    "Armor", 1300,
    {"Accuracy": 975, "Defense": 975}, 1170, src_ww, SET_WW, cls_all,
    [{"name": "Leader's Guard",
      "description": "Gain 1000 Defense for each player in your team."}])
add("Weathered Wood Bracers", "Arms",  1300,
    {"Accuracy": 390, "Critical Severity": 585, "Defense": 975}, 1170, src_ww, SET_WW, cls_all,
    [{"name": "Survivor's Might",
      "description": "Whenever you Deflect an attack, gain 1000 Power for 10 seconds. (Max 5 stacks)"}])
add("Weathered Wood Gaiters", "Feet",  1300,
    {"Combat Advantage": 390, "Critical Strike": 585, "Defense": 975}, 1170, src_ww, SET_WW, cls_all,
    [{"name": "Gladiator's Might",
      "description": "For every 5 seconds you are in combat, you gain 200 Power. Max 24 Stacks: 4800 Power."}])

# ---- The Crone's Gear (Set 3/10, IL 1225) — Module 20 Seals of the Fallen
src_cr = "Sharandar Seals Store / Module 20 (Seals of the Fallen)"
SET_CR = "The Crone's Gear"
add("Crone's Hood",    "Head",  1225,
    {"Combat Advantage": 551, "Defense": 919, "Control Bonus": 368}, 1102, src_cr, SET_CR, cls_all,
    [{"name": "Executioner's Might",
      "description": "When you kill an enemy, your Power increases by 5000 for 10 seconds. (30 second cooldowns)"}])
add("Crone's Hide",    "Armor", 1225,
    {"Accuracy": 919, "Defense": 919}, 1102, src_cr, SET_CR, cls_all,
    [{"name": "Survivor's Remedy",
      "description": "Whenever you Deflect an attack, you have a 10% chance to restore 5% of your Maximum Hit Points. (5s CD)"}])
add("Crone's Bracers", "Arms",  1225,
    {"Accuracy": 368, "Critical Severity": 551, "Defense": 919}, 1102, src_cr, SET_CR, cls_all,
    [{"name": "Survivor's Might",
      "description": "Gain 45 Power for each percent of health you are missing."}])
add("Crone's Gaiters", "Feet",  1225,
    {"Combat Advantage": 368, "Critical Strike": 551, "Defense": 919}, 1102, src_cr, SET_CR, cls_all,
    [{"name": "Contender's Might",
      "description": "At the start of combat, your Power is increased by 3000 for 10 seconds."}])

# ---- Blessed Blade (Module 19 — The Redeemed Citadel) — 2 IL tiers
bb_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 3,
          "setName": "Blessed Blade", "pieces": 2,
          "description": "2 of Set: Sure Edge of the Blessed Blade. When you use an encounter power, your weapons become Blessed: +3% Power/Accuracy/CA + random buff (Blessed Guidance: +5% Critical Strike, Blessed Insight: +7.5% Action Point gain) for 10s. (30s CD)"}]
src_rc = "The Redeemed Citadel"
add("Oathkeeper of the Blessed Blade",         "Main Hand", 650,
    {"Accuracy": 488, "Critical Severity": 488}, 585, src_rc, "Blessed Blade", ["Rogue"], bb_eb, set_size=2)
add("Oathkeeper of the Blessed Blade (IL 900)", "Main Hand", 900,
    {"Accuracy": 675, "Critical Severity": 675}, 810, src_rc, "Blessed Blade", ["Rogue"], bb_eb, set_size=2)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
