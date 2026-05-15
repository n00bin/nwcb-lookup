"""Company belts and cloaks — additional IL tiers."""
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

src_co = "Guild Marks / Stronghold Marketplace"
SET = "Company"

# Company Assault Belt — IL 400 + 600 (additional)
add("Company Assault Belt (Rare)",      "Belt", 400, {"Combat Advantage": 200, "Critical Strike": 200, "Critical Severity": 200}, 360, src_co, SET, ["Warlock"], 2, {"STR": 2})
add("Company Assault Belt (Legendary)", "Belt", 600, {"Combat Advantage": 300, "Critical Strike": 301, "Critical Severity": 300}, 540, src_co, SET, ["Warlock"], 2, {"STR": 2, "CHA": 2})

# Company Gladiator Belt — IL 600 (additional)
add("Company Gladiator Belt (Legendary)", "Belt", 600, {"Combat Advantage": 300, "Critical Strike": 300, "Critical Avoidance": 301}, 540, src_co, SET, ["Warlock"], 2, {"CON": 2, "INT": 2})

# Company Ward Belt — IL 400 (additional)
add("Company Ward Belt (Rare)", "Belt", 400, {"Combat Advantage": 200, "Critical Avoidance": 200, "Deflection": 200}, 360, src_co, SET, ["Warlock"], 2, {"WIS": 2})

# Company Executioner Cloak — IL 300 + 600 (additional)
add("Company Executioner Cloak (Uncommon)",  "Neck", 300, {"Accuracy": 150, "Combat Advantage": 150, "Critical Avoidance": 150}, 270, src_co, SET, ["Warlock"], 2, {"CHA": 1})
add("Company Executioner Cloak (Legendary)", "Neck", 600, {"Accuracy": 300, "Combat Advantage": 300, "Critical Avoidance": 301}, 540, src_co, SET, ["Warlock"], 2, {"DEX": 2, "CHA": 2})

# Company Raider Cloak — IL 600 (additional, Maximum Quality)
add("Company Raider Cloak (Legendary)", "Neck", 600, {"Accuracy": 301, "Combat Advantage": 300, "Critical Severity": 300}, 540, src_co, SET, ["Warlock"], 2, {"STR": 1, "INT": 2})

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
