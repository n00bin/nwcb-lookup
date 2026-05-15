"""Mod 4 Tyranny of Dragons — Alliance Armor finish + Eternal Armor + ToD artifact weapons."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name=None, classes=None, equip=None, set_size=2, notes=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": {}, "abilityBonuses": {},
        "notes": notes or INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

# Alliance Armor finish (IL 546)
src_aa = "Seal of the Elements / Valindra's Tower / Malabog's Castle / Lair of Lostmauth"
for variant, stats in [
    ("Raid",    {"Accuracy": 164, "Critical Strike": 246, "Defense": 410}),
    ("Assault", {"Critical Strike": 164, "Critical Severity": 246, "Defense": 410}),
]:
    for slot_name, slot in [("Cowl", "Head"), ("Longcoat", "Armor"), ("Wristguards", "Arms"), ("Pigaches", "Feet")]:
        add(f"Alliance {variant} {slot_name}", slot, 546, stats, 491, src_aa, "Alliance Armor", ["Warlock"], None, 4)

# Eternal Armor Set (Tyranny of Dragons Epic Adventure) — IL 1300
src_ea = "Tyranny of Dragons Epic Adventure"
eternal_stats_head = {"Accuracy": 294, "Combat Advantage": 337, "Defense": 975, "Critical Avoidance": 339}
eternal_stats_body = {"Accuracy": 294, "Combat Advantage": 337, "Defense": 975, "Critical Avoidance": 339}
eternal_stats_arms = {"Accuracy": 337, "Critical Strike": 337, "Defense": 975, "Critical Avoidance": 296}
eternal_stats_feet = {"Accuracy": 294, "Combat Advantage": 337, "Defense": 975, "Critical Avoidance": 339}
add("Eternal Helmet",       "Head",  1300, eternal_stats_head, 1170, src_ea, "Eternal Armor Set", ["Warlock"], None, 4)
add("Eternal Leather Armor","Armor", 1300, eternal_stats_body, 1170, src_ea, "Eternal Armor Set", ["Warlock"], None, 4)
add("Eternal Gloves",       "Arms",  1300, eternal_stats_arms, 1170, src_ea, "Eternal Armor Set", ["Warlock"], None, 4)
add("Eternal Boots",        "Feet",  1300, eternal_stats_feet, 1170, src_ea, "Eternal Armor Set", ["Warlock"], None, 4)

# Tyranny of Dragons artifact weapons — IL 300 single tier
src_tod = "Tyranny of Dragons Campaign Tasks (Module 4)"
tod_stats_mh = {"Combat Advantage": 150, "Critical Strike": 150, "Critical Avoidance": 150}
tod_stats_oh = {"Accuracy": 150, "Combat Advantage": 150, "Critical Avoidance": 150}

# Elemental Fire / Air / Earth / Water — Pact Blade + Grimoire (Module 4 Cult of the Dragon)
add("Pact Blade of Elemental Fire", "Main Hand", 300, tod_stats_mh, 270, src_tod, "Pact Blade of Elemental Fire", ["Warlock"], None, 2,
    )
add("Elemental Fire Grimoire", "Off Hand", 300, {"Accuracy": 150, "Combat Advantage": 150, "Critical Avoidance": 150}, 270, src_tod, "Pact Blade of Elemental Fire", ["Warlock"], None, 2)

# Golden Dragon Pact Blade variants (Tyranny of Dragons artifact weapons)
add("Golden Dragon's Hellbringer", "Main Hand", 300, {"Accuracy": 150, "Combat Advantage": 150, "Critical Strike": 150}, 270, src_tod, "Golden Dragon", ["Warlock"], None, 2,
    notes="Increase the damage done by Hellish Rebuke by 10%. " + INTAKE)
add("Soulbinder of the Golden Dragon", "Main Hand", 300, {"Combat Advantage": 150, "Critical Strike": 150, "Critical Avoidance": 150}, 270, src_tod, "Golden Dragon", ["Warlock"], None, 2,
    notes="Increase the damage done by Essence Defiler by 10%. " + INTAKE)
add("Golden Dragon Grimoire", "Off Hand", 300, {"Accuracy": 150, "Combat Advantage": 150, "Critical Avoidance": 150}, 270, src_tod, "Golden Dragon", ["Warlock"], None, 2)
add("Sovereigner of the Golden Dragon", "Off Hand", 300, {"Combat Advantage": 150, "Critical Strike": 150, "Critical Avoidance": 150}, 270, src_tod, "Golden Dragon", ["Warlock"], None, 2,
    notes="Increase the damage done by Essence Defiler by 10%. " + INTAKE)

# Dragon Bone Weapons (Set 3/5 ToD) — IL 800 high-rarity artifact weapons
src_db = "Cult of the Dragon (Tyranny of Dragons)"
add("Dragon Bone Pact Blade", "Main Hand", 800, {"Combat Advantage": 350, "Critical Strike": 422, "Critical Avoidance": 427}, 720, src_db, "Dragon Bone Weapons", ["Warlock"], None, 2)
add("Dragon Bone Grimoire",   "Off Hand",  800, {"Combat Advantage": 350, "Critical Strike": 422, "Critical Avoidance": 427}, 720, src_db, "Dragon Bone Weapons", ["Warlock"], None, 2)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
