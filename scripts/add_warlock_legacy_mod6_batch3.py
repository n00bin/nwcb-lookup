"""Module 3-7 legacy Warlock gear — Black Ice, Hammerstone, Elk Tribe."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear (Mod 3-7 era) — screenshot intake 2026-05-14."

def add(name, slot, il, rs, cr, source, set_name=None, classes=None, equip=None, notes=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": 0,
        "source": source, "percentStats": {}, "abilityBonuses": {},
        "notes": notes or INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

# Black Ice Gear (Module 6 Tyranny of Dragons — Icewind Dale Black Ice Forge)
src_bi = "Black Ice Forge (Icewind Pass / Module 6)"
add("Black Ice Mask",   "Head",  512, {"Combat Advantage": 131, "Critical Strike": 60, "Defense": 384, "Critical Avoidance": 60, "Deflection": 60}, 461, src_bi, "Black Ice Gear", ["Warlock"])
add("Black Ice Armor",  "Armor", 512, {"Accuracy": 74, "Combat Advantage": 163, "Defense": 384, "Critical Avoidance": 147}, 461, src_bi, "Black Ice Gear", ["Warlock"])
add("Black Ice Gloves", "Arms",  512, {"Accuracy": 60, "Combat Advantage": 60, "Defense": 384, "Critical Avoidance": 132, "Deflection": 132}, 461, src_bi, "Black Ice Gear", ["Warlock"])
add("Black Ice Boots",  "Feet",  512, {"Accuracy": 163, "Defense": 384, "Awareness": 74, "Critical Avoidance": 147}, 461, src_bi, "Black Ice Gear", ["Warlock"])

# Hammerstone Armor (Module 3-4 — Dwarven Valley, Warlock leather)
src_hm = "Dwarven Valley (Module 3-4)"
add("Hammerstone Mask",      "Head",  352, {"Combat Advantage": 92, "Critical Severity": 40, "Defense": 264, "Critical Avoidance": 92, "Deflection": 40}, 317, src_hm, "Hammerstone Armor", ["Warlock"])
add("Hammerstone Tunic",     "Armor", 352, {"Combat Advantage": 92, "Critical Severity": 40, "Defense": 264, "Critical Avoidance": 92, "Deflection": 40}, 317, src_hm, "Hammerstone Armor", ["Warlock"])
add("Hammerstone Gloves",    "Arms",  352, {"Combat Advantage": 92, "Critical Severity": 40, "Defense": 264, "Critical Avoidance": 92, "Deflection": 40}, 317, src_hm, "Hammerstone Armor", ["Warlock"])
add("Hammerstone Boots",     "Feet",  352, {"Combat Advantage": 92, "Critical Severity": 40, "Defense": 264, "Critical Avoidance": 92, "Deflection": 40}, 317, src_hm, "Hammerstone Armor", ["Warlock"])
add("Hammerstone Pact Blade","Main Hand", 352, {"Combat Advantage": 185, "Critical Strike": 185, "Awareness": 80, "Critical Avoidance": 80}, 317, src_hm, "Hammerstone Armor", ["Warlock"])
add("Hammerstone Grimoire",  "Off Hand",  352, {"Combat Advantage": 185, "Critical Strike": 185, "Awareness": 80, "Critical Avoidance": 80}, 317, src_hm, "Hammerstone Armor", ["Warlock"])

# Elk Tribe Chiefs (Module 4-ish — Icewind Pass, follows Hammerstone)
src_elk = "Icewind Pass (Module 4)"
add("Elk Tribe Noble's Grimoire", "Off Hand", 399, {"Accuracy": 98, "Combat Advantage": 202, "Critical Strike": 202, "Critical Avoidance": 98}, 359, src_elk, "Weapons of the Elk Tribe Chiefs", ["Warlock"])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
