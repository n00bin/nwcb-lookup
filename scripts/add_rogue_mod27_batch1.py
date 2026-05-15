"""Mod 27 Soul Collector / Adventures in Thay — Rogue artifact weapons.
Scream Seeker (Main Hand) + Dread Confessor (Off-Hand) at 6 IL tiers each.
Sets: Whisper of Power (lower IL) → Impending Doom (higher IL)."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Mod 27 Rogue Adventures in Thay — screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes, equip=None, percent=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name, "setSize": 2,
        "source": source, "percentStats": percent or {}, "abilityBonuses": {},
        "allowedClasses": classes, "notes": INTAKE}
    data.append(entry)

# Whisper of Power 2pc set (lower IL tiers)
wp_eb = [{"type": "Set", "scope": "self", "stat": "Movement Speed", "amount": 10,
          "setName": "Whisper of Power", "pieces": 2,
          "description": "2 of Set: +10% Movement Speed in Thay."}]

# Impending Doom 2pc set (higher IL tiers — Soul Harvest dungeons)
id_eb = [{"type": "Set", "scope": "self", "stat": "Critical Severity", "amount": 2.5,
          "setName": "Impending Doom", "pieces": 2,
          "description": "2 of Set: Accumulate 18 Charges to consume them and become Unleashed. Charged by: 1 charge per Daily power (10s CD), 1 charge per Encounter power (1s CD), 1 charge per 5s in combat. Unleashed grants: DPS +4% Base Damage Boost, Heal +4% Outgoing Healing. Charges and Unleashed last 20s and are refreshable. Leaving combat removes all Charges."},
         {"type": "Set", "scope": "self", "stat": "Power", "amount": 2.5,
          "setName": "Impending Doom", "pieces": 2}]

src_zone = "The Soul Collector Zone Mechanic / Adventures in Thay (Module 27)"
src_adv  = "Soul Harvest (Advanced) (Module 27)"
src_mst  = "Soul Harvest (Master) (Module 27)"

# Scream Seeker (Main Hand) — 6 IL tiers
add("Scream Seeker (IL 3400)", "Main Hand", 3400, {"Critical Strike": 1060, "Critical Severity": 1060}, 3060, src_zone, "Whisper of Power", ["Rogue"], wp_eb)
add("Scream Seeker (IL 3750)", "Main Hand", 3750, {"Critical Strike": 3375, "Critical Severity": 3375}, 3375, src_zone, "Whisper of Power", ["Rogue"], wp_eb)
add("Scream Seeker (IL 4100)", "Main Hand", 4100, {"Critical Strike": 3690, "Critical Severity": 3690}, 3690, src_zone, "Impending Doom", ["Rogue"], id_eb)
add("Scream Seeker (IL 4450)", "Main Hand", 4450, {"Accuracy": 2892, "Critical Strike": 2670, "Critical Severity": 2670}, 4005, src_adv, "Impending Doom", ["Rogue"], id_eb, {"Damage Bonus": 0.5})
add("Scream Seeker (IL 4800)", "Main Hand", 4800, {"Accuracy": 3120, "Critical Strike": 2880, "Critical Severity": 2880}, 4320, src_adv, "Impending Doom", ["Rogue"], id_eb, {"Damage Bonus": 1.0})
add("Scream Seeker (IL 5250)", "Main Hand", 5250, {"Accuracy": 3412, "Critical Strike": 3150, "Critical Severity": 3150}, 4725, src_mst, "Impending Doom", ["Rogue"], id_eb, {"Damage Bonus": 2.0})

# Dread Confessor (Off-Hand) — 6 IL tiers
add("Dread Confessor (IL 3400)", "Off Hand", 3400, {"Accuracy": 3315, "Combat Advantage": 2040}, 3060, src_zone, "Whisper of Power", ["Rogue"], wp_eb)
add("Dread Confessor (IL 3750)", "Off Hand", 3750, {"Accuracy": 3656, "Combat Advantage": 2250}, 3375, src_zone, "Whisper of Power", ["Rogue"], wp_eb)
add("Dread Confessor (IL 4100)", "Off Hand", 4100, {"Accuracy": 3997, "Combat Advantage": 2460}, 3690, src_zone, "Impending Doom", ["Rogue"], id_eb)
add("Dread Confessor (IL 4450)", "Off Hand", 4450, {"Accuracy": 4339, "Combat Advantage": 2670}, 4005, src_adv, "Impending Doom", ["Rogue"], id_eb)
add("Dread Confessor (IL 4800)", "Off Hand", 4800, {"Accuracy": 3120, "Combat Advantage": 1920, "Power": 1680}, 4320, src_adv, "Impending Doom", ["Rogue"], id_eb, {"Damage Bonus": 1.0})
add("Dread Confessor (IL 5250)", "Off Hand", 5250, {"Accuracy": 3412, "Combat Advantage": 2100, "Power": 1837}, 4725, src_mst, "Impending Doom", ["Rogue"], id_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
