"""Sets 11-13: Lionsmane finish + Dragonflight Armor + Elemental Dragonflight."""
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

# Lionsmane Executioner Cowl finish
add("Lionsmane Executioner Cowl", "Head", 560, {"Combat Advantage": 126, "Critical Strike": 168, "Critical Severity": 126, "Defense": 420}, 504, "Stronghold Siege", "Lionsmane Set", ["Warlock"])

# Dragonflight Armor (Set 12/20, IL 588) — The Greed of the Dragonflight, Stronghold
src_df = "The Greed of the Dragonflight (Stronghold)"
for variant, stats_h, stats_b, stats_a, stats_f in [
    ("Raid",    {"Combat Advantage": 176, "Critical Strike": 265, "Defense": 441},
                {"Accuracy": 265, "Combat Advantage": 176, "Defense": 441},
                {"Combat Advantage": 176, "Critical Strike": 265, "Defense": 441},
                {"Combat Advantage": 176, "Critical Strike": 265, "Defense": 441}),
    ("Assault", {"Critical Strike": 265, "Critical Severity": 176, "Defense": 441},
                {"Critical Strike": 265, "Critical Severity": 176, "Defense": 441},
                {"Critical Strike": 265, "Critical Severity": 176, "Defense": 441},
                {"Combat Advantage": 176, "Critical Severity": 265, "Defense": 441}),
]:
    add(f"Dragonflight {variant} Cowl",       "Head",  588, stats_h, 529, src_df, "Dragonflight", ["Warlock"])
    add(f"Dragonflight {variant} Longcoat",   "Armor", 588, stats_b, 529, src_df, "Dragonflight", ["Warlock"])
    add(f"Dragonflight {variant} Wristguards","Arms",  588, stats_a, 529, src_df, "Dragonflight", ["Warlock"])
    add(f"Dragonflight {variant} Pigaches",   "Feet",  588, stats_f, 529, src_df, "Dragonflight", ["Warlock"])

# Elemental Dragonflight Armor (Set 13/20, IL 596) — Elemental Infusion
src_edf = "Elemental Infusion (Czer-Konig)"
for variant, stats_h, stats_b, stats_a, stats_f in [
    ("Raid",    {"Combat Advantage": 179, "Critical Strike": 268, "Defense": 447},
                {"Accuracy": 268, "Combat Advantage": 179, "Defense": 447},
                {"Combat Advantage": 179, "Critical Strike": 268, "Defense": 447},
                {"Accuracy": 179, "Combat Advantage": 268, "Defense": 447}),
    ("Assault", {"Combat Advantage": 179, "Critical Severity": 268, "Defense": 447},
                {"Critical Strike": 268, "Critical Severity": 179, "Defense": 447},
                {"Critical Strike": 268, "Critical Severity": 179, "Defense": 447},
                {"Combat Advantage": 179, "Critical Severity": 268, "Defense": 447}),
]:
    add(f"Elemental Dragonflight {variant} Cowl",       "Head",  596, stats_h, 536, src_edf, "Dragonflight", ["Warlock"])
    add(f"Elemental Dragonflight {variant} Longcoat",   "Armor", 596, stats_b, 536, src_edf, "Dragonflight", ["Warlock"])
    add(f"Elemental Dragonflight {variant} Wristguards","Arms",  596, stats_a, 536, src_edf, "Dragonflight", ["Warlock"])
    add(f"Elemental Dragonflight {variant} Pigaches",   "Feet",  596, stats_f, 536, src_edf, "Dragonflight", ["Warlock"])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
