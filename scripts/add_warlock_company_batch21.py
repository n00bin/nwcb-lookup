"""Sets 15+19: Company PVE Armor remainder + Stronghold Company Gear (belts + cloaks)."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes=None, set_size=2, ab=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": {}, "abilityBonuses": ab or {},
        "notes": INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

# Company Belts (Set 19/20 Stronghold Company Gear) — multiple variants
src_co = "Guild Marks / Stronghold Marketplace"
SET = "Company"

# Company Assault Belt — 4 IL tiers
for il, base, cd, cr, ab in [
    (300, 150, 150, 270, {"STR": 1}),
    (500, 250, 250, 450, {"STR": 2, "CHA": 1}),
    (600, 300, 300, 540, {"STR": 2, "CHA": 1}),
]:
    add(f"Company Assault Belt ({['Uncommon','Rare','Epic','Legendary'][[300,500,600].index(il)]})",
        "Belt", il, {"Combat Advantage": base, "Critical Strike": base, "Critical Severity": cd}, cr,
        src_co, SET, ["Warlock"], 2, ab)

# Company Gladiator Belt — 4 IL tiers
for il, base, cd, cr, ab in [(400, 200, 200, 360, {"CON": 2})]:
    add("Company Gladiator Belt", "Belt", il, {"Combat Advantage": base, "Critical Strike": base, "Critical Avoidance": cd}, cr, src_co, SET, ["Warlock"], 2, ab)

# Company Ward Belt
for il, base, cd, cr, ab in [(500, 250, 250, 450, {"CON": 1, "WIS": 2})]:
    add("Company Ward Belt", "Belt", il, {"Combat Advantage": base, "Critical Avoidance": base, "Deflection": cd}, cr, src_co, SET, ["Warlock"], 2, ab)

# Company Cloaks (artifact accessories, Set 19/20)
add("Company Executioner Cloak", "Neck", 500, {"Accuracy": 250, "Combat Advantage": 250, "Critical Avoidance": 250}, 450, src_co, SET, ["Warlock"], 2, {"DEX": 1, "CHA": 2})
add("Company Duelist Cloak",     "Neck", 500, {"Combat Advantage": 250, "Critical Avoidance": 250, "Deflection": 250}, 450, src_co, SET, ["Warlock"], 2, {"DEX": 2, "WIS": 1})
add("Company Raider's Cloak Uncommon", "Neck", 300, {"Accuracy": 150, "Combat Advantage": 150, "Critical Severity": 150}, 270, src_co, SET, ["Warlock"], 2, {"INT": 1})
add("Company Raider Cloak Rare",       "Neck", 500, {"Accuracy": 250, "Combat Advantage": 250, "Critical Severity": 250}, 450, src_co, SET, ["Warlock"], 2, {"STR": 1, "INT": 2})
add("Company Raider Cloak Epic",       "Neck", 600, {"Accuracy": 301, "Combat Advantage": 300, "Critical Severity": 300}, 540, src_co, SET, ["Warlock"], 2, {"STR": 1, "INT": 2})

# Company PVE Armor finish (Set 15/20)
add("Company Assault Longcoat", "Armor", 588, {"Combat Advantage": 265, "Critical Severity": 176, "Defense": 441}, 529, "Guild Marks", "Company PVE Armor", ["Warlock"], 4)
add("Company Assault Pigaches", "Feet",  588, {"Critical Strike": 265, "Critical Severity": 176, "Defense": 441}, 529, "Guild Marks", "Company PVE Armor", ["Warlock"], 4)
add("Company Assault Wristguards","Arms", 588, {"Combat Advantage": 176, "Critical Strike": 265, "Defense": 441}, 529, "Guild Marks", "Company PVE Armor", ["Warlock"], 4)
add("Company Assault Cowl",       "Head", 588, {"Combat Advantage": 265, "Critical Severity": 176, "Defense": 441}, 529, "Guild Marks", "Company PVE Armor", ["Warlock"], 4)
add("Company Raid Wristguards",   "Arms", 588, {"Combat Advantage": 176, "Critical Strike": 265, "Defense": 441}, 529, "Guild Marks", "Company PVE Armor", ["Warlock"], 4)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
