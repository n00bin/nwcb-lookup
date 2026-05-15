"""Masterwork Armor III — Reinforced Dragonflight + Dinohide Raid start."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name=None, classes=None, equip=None, set_size=4, notes=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": {}, "abilityBonuses": {},
        "notes": notes or INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

# Reinforced Dragonflight Gear (Masterwork Armor III, IL 1400) — Raid + Assault × 4 pieces
src_rd = "Masterwork Crafting (Masterwork Armor III)"
df_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Dragonflight", "pieces": 4,
          "description": "2 of Set: +5,000 Maximum Hit Points, +1,000 Power. 3 of Set: +5,000 Maximum Hit Points, +1,000 Power."}]
for variant, stats_h, stats_b, stats_a, stats_f in [
    ("Raid",    {"Combat Advantage": 420, "Critical Strike": 630, "Defense": 1050},
                {"Accuracy": 630, "Combat Advantage": 420, "Defense": 1050},
                {"Combat Advantage": 420, "Critical Strike": 630, "Defense": 1050},
                {"Accuracy": 630, "Combat Advantage": 420, "Defense": 1050}),
    ("Assault", {"Critical Strike": 630, "Defense": 1050, "Incoming Healing": 420},
                {"Critical Strike": 630, "Critical Severity": 420, "Defense": 1050},
                {"Critical Strike": 630, "Critical Severity": 420, "Defense": 1050},
                {"Critical Severity": 630, "Defense": 1050, "Outgoing Healing": 420}),
]:
    add(f"Reinforced Dragonflight {variant} Cowl",       "Head",  1400, stats_h, 1260, src_rd, "Dragonflight", ["Warlock"], df_eb)
    add(f"Reinforced Dragonflight {variant} Longcoat",   "Armor", 1400, stats_b, 1260, src_rd, "Dragonflight", ["Warlock"], df_eb)
    add(f"Reinforced Dragonflight {variant} Wristguards","Arms",  1400, stats_a, 1260, src_rd, "Dragonflight", ["Warlock"], df_eb)
    add(f"Reinforced Dragonflight {variant} Pigaches",   "Feet",  1400, stats_f, 1260, src_rd, "Dragonflight", ["Warlock"], df_eb)

# Dinohide Raid Set (Masterwork Armor III, IL 784, Mod 11) — start
src_dh = "Masterwork Crafting (Module 11 The Lost City of Omu)"
add("Dinohide Raid Barakoa", "Head",  784, {"Combat Advantage": 235, "Critical Strike": 353, "Defense": 588}, 706, src_dh, "Dinohide Set", ["Warlock"], None, 4,
    "Gladiator's Accuracy: every 5 seconds in combat, gain 100 Accuracy. Max 2 min. " + INTAKE)
add("Dinohide Raid Kiuno",   "Armor", 784, {"Combat Advantage": 235, "Critical Strike": 353, "Defense": 588}, 706, src_dh, "Dinohide Set", ["Warlock"], None, 4,
    "Challenger's Might: when in combat with only one enemy, +1500 Power. " + INTAKE)
add("Dinohide Raid Shabas",  "Arms",  784, {"Combat Advantage": 235, "Critical Strike": 353, "Defense": 588}, 706, src_dh, "Dinohide Set", ["Warlock"], None, 4,
    "Survivor's Party: gain 25 Deflect for each percent of health you are missing. " + INTAKE)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
