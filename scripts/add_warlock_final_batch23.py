"""Final batch — Umbral remaining + Elemental Dragonflight remaining + Company remaining."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes=None, set_size=4, ab=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": {}, "abilityBonuses": ab or {},
        "notes": INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

# Umbral remaining pieces (additional individual variants seen in screenshots)
src_um = "Masterwork Crafting (Stronghold)"
add("Umbral Duelist Longcoat",         "Armor", 728, {"Accuracy": 218, "Combat Advantage": 164, "Defense": 546, "Awareness": 164}, 655, src_um, "Umbral Set", ["Warlock"])
add("Umbral Executioner Longcoat",     "Armor", 728, {"Combat Advantage": 164, "Critical Strike": 218, "Defense": 546, "Critical Avoidance": 164}, 655, src_um, "Umbral Set", ["Warlock"])
add("Umbral Assault Pigaches",         "Feet",  728, {"Critical Strike": 328, "Critical Severity": 218, "Defense": 546}, 655, src_um, "Umbral Set", ["Warlock"])

# Elemental Dragonflight remaining
add("Elemental Dragonflight Raid Wristguards", "Arms", 596, {"Combat Advantage": 179, "Critical Strike": 268, "Defense": 447}, 536, "Elemental Infusion", "Dragonflight", ["Warlock"])

# Company Duelist Cloak — additional IL tiers (300, 400, 600 seen previously)
src_co = "Guild Marks"
add("Company Duelist Cloak (Uncommon)",  "Neck", 300, {"Combat Advantage": 150, "Critical Avoidance": 150, "Deflection": 150}, 270, src_co, "Company", ["Warlock"], 2, {"DEX": 1})
add("Company Duelist Cloak (Rare)",      "Neck", 400, {"Combat Advantage": 200, "Critical Avoidance": 200, "Deflection": 200}, 360, src_co, "Company", ["Warlock"], 2, {"DEX": 2})
add("Company Duelist Cloak (Legendary)", "Neck", 600, {"Combat Advantage": 300, "Critical Avoidance": 301, "Deflection": 300}, 540, src_co, "Company", ["Warlock"], 2, {"DEX": 2, "WIS": 2})

# Company Raider Cloak (Rare IL 400 additional)
add("Company Raider Cloak (Rare)", "Neck", 400, {"Accuracy": 200, "Combat Advantage": 200, "Critical Severity": 200}, 360, src_co, "Company", ["Warlock"], 2, {"INT": 2})

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
