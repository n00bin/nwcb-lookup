"""Lionsmane Armor remaining pieces (Set 11/20)."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes=None, set_size=4):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": {}, "abilityBonuses": {},
        "notes": INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

src = "Stronghold Siege / Elemental Infusion"
SET = "Lionsmane Set"

# Elemental Lionsmane (IL 574, infused)
add("Elemental Lionsmane Duelist Cowl",         "Head",  574, {"Combat Advantage": 129, "Critical Strike": 129, "Defense": 430, "Critical Avoidance": 172}, 517, src, SET, ["Warlock"])
add("Elemental Lionsmane Executioner Longcoat", "Armor", 574, {"Combat Advantage": 129, "Critical Strike": 172, "Critical Severity": 129, "Defense": 430}, 517, src, SET, ["Warlock"])

# Lionsmane (IL 560, base)
add("Lionsmane Duelist Cowl",         "Head",  560, {"Accuracy": 168, "Combat Advantage": 126, "Defense": 420, "Awareness": 168, "Critical Avoidance": 126}, 504, src, SET, ["Warlock"])
add("Lionsmane Duelist Wristguards",  "Arms",  560, {"Accuracy": 168, "Critical Strike": 126, "Defense": 420, "Critical Avoidance": 126}, 504, src, SET, ["Warlock"])
add("Lionsmane Duelist Pigaches",     "Feet",  560, {"Combat Advantage": 210, "Defense": 420, "Awareness": 210}, 504, src, SET, ["Warlock"])
add("Lionsmane Executioner Longcoat", "Armor", 560, {"Combat Advantage": 126, "Critical Strike": 168, "Critical Severity": 126, "Defense": 420}, 504, src, SET, ["Warlock"])
add("Lionsmane Executioner Pigaches", "Feet",  560, {"Combat Advantage": 126, "Critical Strike": 168, "Critical Severity": 126, "Defense": 420}, 504, src, SET, ["Warlock"])
add("Lionsmane Executioner Wristguards","Arms", 560, {"Critical Strike": 126, "Critical Severity": 168, "Defense": 420, "Awareness": 126}, 504, src, SET, ["Warlock"])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
