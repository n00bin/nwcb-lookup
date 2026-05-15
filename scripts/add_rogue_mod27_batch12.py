"""Rogue gear batch 12 — Blessed Blade IL 1150/1400, Sure Edge (all 4 tiers),
Celestial Point of Praise (4 tiers), Celestial Stylet of Mercy (4 tiers),
Legion Guard's Barbed Blade IL 600 (Devil's Legion start)."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Rogue gear — screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes, equip=None, percent=None, set_size=2, abilities=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": percent or {}, "abilityBonuses": abilities or {},
        "allowedClasses": classes, "notes": INTAKE}
    data.append(entry)

src_rc = "The Redeemed Citadel"
src_zc = "Trial: Zariel's Challenge"
src_av = "Avernus Adventure Zone"

# ---- Blessed Blade (Module 19) — Oathkeeper additional tiers IL 1150 + 1400
bb_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 3,
          "setName": "Blessed Blade", "pieces": 2,
          "description": "2 of Set: Sure Edge of the Blessed Blade. When you use an encounter power, your weapons become Blessed: +3% Power/Accuracy/CA + random buff (Blessed Guidance: +5% Critical Strike, Blessed Insight: +7.5% Action Point gain) for 10s. (30s CD)"}]
add("Oathkeeper of the Blessed Blade (IL 1150)", "Main Hand", 1150,
    {"Accuracy": 862, "Critical Severity": 862}, 1015, src_rc, "Blessed Blade", ["Rogue"], bb_eb)
add("Oathkeeper of the Blessed Blade (IL 1400)", "Main Hand", 1400,
    {"Accuracy": 1050, "Critical Severity": 1050}, 1260, src_rc, "Blessed Blade", ["Rogue"], bb_eb)

# ---- Sure Edge of the Blessed Blade (Off Hand) — 4 tiers
add("Sure Edge of the Blessed Blade",          "Off Hand", 650,
    {"Combat Advantage": 488, "Critical Strike": 488}, 585, src_rc, "Blessed Blade", ["Rogue"], bb_eb)
add("Sure Edge of the Blessed Blade (IL 900)", "Off Hand", 900,
    {"Combat Advantage": 675, "Critical Strike": 675}, 810, src_rc, "Blessed Blade", ["Rogue"], bb_eb)
add("Sure Edge of the Blessed Blade (IL 1150)", "Off Hand", 1150,
    {"Combat Advantage": 862, "Critical Strike": 862}, 1015, src_rc, "Blessed Blade", ["Rogue"], bb_eb)
add("Sure Edge of the Blessed Blade (IL 1400)", "Off Hand", 1400,
    {"Combat Advantage": 1050, "Critical Strike": 1050}, 1260, src_rc, "Blessed Blade", ["Rogue"], bb_eb)

# ---- Celestial Set (Trial: Zariel's Challenge) — Celestial Point of Praise (MH) + Celestial Stylet of Mercy (OH)
cel_eb = [{"type": "Set", "scope": "self", "stat": "Base Damage Boost", "amount": 7.5,
           "setName": "Celestial", "pieces": 2,
           "description": "2 of Set: Use encounter/daily during combat to gain Divine Charge stacks (15s each). 5 stacks consume and grant Divine Fury for 30s: +7.5% Base Damage Boost, +7.5% Overall Outgoing Healing. Refreshable."}]
add("Celestial Point of Praise",          "Main Hand", 650,
    {"Accuracy": 488, "Critical Severity": 488}, 585, src_zc, "Celestial", ["Rogue"], cel_eb)
add("Celestial Point of Praise (IL 900)", "Main Hand", 900,
    {"Accuracy": 675, "Critical Severity": 675}, 810, src_zc, "Celestial", ["Rogue"], cel_eb)
add("Celestial Point of Praise (IL 1150)", "Main Hand", 1150,
    {"Accuracy": 862, "Critical Severity": 862}, 1015, src_zc, "Celestial", ["Rogue"], cel_eb)
add("Celestial Point of Praise (IL 1400)", "Main Hand", 1400,
    {"Accuracy": 1050, "Critical Severity": 1050}, 1260, src_zc, "Celestial", ["Rogue"], cel_eb)

add("Celestial Stylet of Mercy",          "Off Hand", 650,
    {"Combat Advantage": 488, "Critical Strike": 488}, 585, src_zc, "Celestial", ["Rogue"], cel_eb)
add("Celestial Stylet of Mercy (IL 900)", "Off Hand", 900,
    {"Combat Advantage": 675, "Critical Strike": 675}, 810, src_zc, "Celestial", ["Rogue"], cel_eb)
add("Celestial Stylet of Mercy (IL 1150)", "Off Hand", 1150,
    {"Combat Advantage": 862, "Critical Strike": 862}, 1015, src_zc, "Celestial", ["Rogue"], cel_eb)
add("Celestial Stylet of Mercy (IL 1400)", "Off Hand", 1400,
    {"Combat Advantage": 1050, "Critical Strike": 1050}, 1260, src_zc, "Celestial", ["Rogue"], cel_eb)

# ---- Devil's Legion (Legion Guard's, IL 600) — Avernus Adventure Zone
dl_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 1500,
          "setName": "Devil's Legion", "pieces": 2,
          "description": "2 of Set: You and nearby allies are granted: +1500 Power, +1500 Combat Advantage, +1500 Defense, +1500 Critical Avoidance. Stacks up to 5 times when allies are equipped with full Legion Guard's weapons."}]
add("The Legion Guard's Barbed Blade", "Main Hand", 600,
    {"Accuracy": 450, "Critical Severity": 450}, 540, src_av, "Devil's Legion", ["Rogue"], dl_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
