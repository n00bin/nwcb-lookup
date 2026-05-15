"""Module 4-6 armor sets — Elemental Elven, Elven, Elemental Alliance."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-14/15."

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

# Elemental Elven Armor (Mod 4 Elemental Evil) — IL 575 — Raid + Assault × 4 pieces
src_eea = "Elemental Infusion (Czer-Konig) / Module 4 Elemental Evil"
for variant, raid_stats in [
    ("Raid",    {"Accuracy": 172, "Critical Strike": 259, "Defense": 431}),
    ("Assault", {"Combat Advantage": 259, "Critical Severity": 172, "Defense": 431}),
]:
    add(f"Elemental Elven {variant} Longcoat",    "Armor", 575, raid_stats, 518, src_eea, "Elemental Elven Armor", ["Warlock"])
    add(f"Elemental Elven {variant} Wristguards", "Arms",  575, raid_stats, 518, src_eea, "Elemental Elven Armor", ["Warlock"])
    add(f"Elemental Elven {variant} Pigaches",    "Feet",  575, raid_stats, 518, src_eea, "Elemental Elven Armor", ["Warlock"])
add("Elemental Elven Assault Cowl", "Head", 575, {"Combat Advantage": 259, "Critical Severity": 172, "Defense": 431}, 518, src_eea, "Elemental Elven Armor", ["Warlock"])

# Elven Armor (Mod 4) — IL 547 — Raid + Assault × 4 pieces
src_ea = "Seal of the Protector (Module 4)"
for variant, stats in [
    ("Raid",    {"Accuracy": 170, "Critical Strike": 255, "Defense": 425}),
    ("Assault", {"Combat Advantage": 255, "Critical Severity": 170, "Defense": 425}),
]:
    for slot_name, slot in [("Cowl", "Head"), ("Longcoat", "Armor"), ("Wristguards", "Arms"), ("Pigaches", "Feet")]:
        add(f"Elven {variant} {slot_name}", slot, 547, stats, 510, src_ea, "Elven Armor", ["Warlock"])

# Elemental Alliance Armor (Mod 4 — Elemental Infusion) — IL 554 — Raid + Assault × 4 pieces
src_eaa = "Temple of Tiamat / Cragmire Crypt (Master) / Elemental Infusion"
for variant, stats in [
    ("Raid",    {"Accuracy": 166, "Combat Advantage": 249, "Defense": 416}),
    ("Assault", {"Accuracy": 249, "Critical Severity": 166, "Defense": 416}),
]:
    for slot_name, slot in [("Cowl", "Head"), ("Longcoat", "Armor"), ("Wristguards", "Arms"), ("Pigaches", "Feet")]:
        add(f"Elemental Alliance {variant} {slot_name}", slot, 554, stats, 499, src_eaa, "Elemental Alliance Armor", ["Warlock"])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
