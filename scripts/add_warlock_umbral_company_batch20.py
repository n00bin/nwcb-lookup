"""Sets 14-15: Masterwork Armor (Umbral variants) + Company PVE Armor."""
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

# Umbral Armor (Set 14/20 Masterwork I, IL 728) — 4 variants × 4 pieces
src_um = "Masterwork Crafting (Stronghold)"
for variant, base_stats in [
    ("Raid",       {"Combat Advantage": 218, "Critical Strike": 328, "Defense": 546}),
    ("Assault",    {"Critical Strike": 328, "Critical Severity": 218, "Defense": 546}),
    ("Duelist",    {"Accuracy": 218, "Combat Advantage": 164, "Critical Strike": 164, "Defense": 546}),
    ("Executioner",{"Combat Advantage": 164, "Critical Strike": 164, "Critical Severity": 218, "Defense": 546}),
]:
    for slot_name, slot in [("Cowl", "Head"), ("Longcoat", "Armor"), ("Wristguards", "Arms"), ("Pigaches", "Feet")]:
        add(f"Umbral {variant} {slot_name}", slot, 728, base_stats, 655, src_um, "Umbral Set", ["Warlock"], 4)

# Company PVE Armor (Set 15/20, IL 588) — Guild Marks
src_co = "Guild Marks / Stronghold Marketplace"
for variant, stats in [
    ("Raid",    {"Accuracy": 265, "Combat Advantage": 176, "Defense": 441}),
    ("Assault", {"Combat Advantage": 176, "Critical Strike": 265, "Defense": 441}),
]:
    for slot_name, slot in [("Cowl", "Head"), ("Longcoat", "Armor"), ("Wristguards", "Arms"), ("Pigaches", "Feet")]:
        add(f"Company {variant} {slot_name}", slot, 588, stats, 529, src_co, "Company PVE Armor", ["Warlock"], 4)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
