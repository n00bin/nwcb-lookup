"""Rogue gear batch 5 — Dark Matter (MH + +1 variants), Peer Into the Void (Imperial Citadel),
Meteoric Fury (Adventures in Wildspace), start of Ultraviolet Armor."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Rogue gear — screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes, equip=None, percent=None, set_size=2, abilities=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": percent or {}, "abilityBonuses": abilities or {},
        "allowedClasses": classes, "notes": INTAKE}
    data.append(entry)

# ---- Dark Matter Weapons — MH + +1 variants
dm_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 5.5,
          "setName": "Dark Matter", "pieces": 2,
          "description": "2 of Set: Deal or heal up to 5.5% additional damage based on HP difference. Role: DPS +1% Base Damage Boost, Tank +5% Incoming Damage, Healer +6% Overall Outgoing Healing. Doubled in Wildspace, +10% Movement Speed."}]
add("Solarium Kris", "Main Hand", 2500,
    {"Critical Strike": 1875, "Critical Severity": 1875}, 2250,
    "Defense of the Moondancer (Advanced)", "Dark Matter", ["Rogue"], dm_eb)
add("Starcore Stiletto +1", "Off Hand", 2700,
    {"Combat Advantage": 2025, "Forte": 2025}, 2430,
    "Defense of the Moondancer (Master)", "Dark Matter", ["Rogue"], dm_eb)
add("Solarium Kris +1", "Main Hand", 2700,
    {"Critical Strike": 2025, "Critical Severity": 2025}, 2430,
    "Defense of the Moondancer (Master)", "Dark Matter", ["Rogue"], dm_eb, {"Damage Bonus": 2.5})

# ---- Peer Into the Void Weapons (Imperial Citadel)
piv_eb = [{"type": "Set", "scope": "self", "stat": "Overall Outgoing Healing", "amount": 5,
           "setName": "Peer Into the Void", "pieces": 2,
           "description": "2 of Set: Gain 5% Overall Outgoing Healing and -5% Incoming Damage. In Wildspace, Movement Speed +12%. Every 2s in combat with a single opponent, gain stack of Darklight. Every 2s with 4+ opponents, lose 1 stack. Each Darklight stack: DPS +0.6% Base Damage Boost, Tank -0.6% Incoming Damage, Healer +0.6% Overall Outgoing Healing. Max 10 stacks. Bonuses doubled in Wildspace."}]
add("Xaryxian Sickle", "Off Hand", 2750,
    {"Accuracy": 2062, "Forte": 2062}, 2475,
    "The Imperial Citadel (Advanced)", "Peer Into the Void", ["Rogue"], piv_eb)
add("Xaryxian Scythe", "Main Hand", 2750,
    {"Critical Strike": 2062, "Critical Severity": 2062}, 2475,
    "The Imperial Citadel (Advanced)", "Peer Into the Void", ["Rogue"], piv_eb, {"Damage Bonus": 2.5})
add("Voidtouched Sickle", "Off Hand", 3000,
    {"Accuracy": 2250, "Forte": 2250}, 2700,
    "The Imperial Citadel (Master)", "Peer Into the Void", ["Rogue"], piv_eb)
add("Voidtouched Scythe", "Main Hand", 3000,
    {"Critical Strike": 2250, "Critical Severity": 2250}, 2700,
    "The Imperial Citadel (Master)", "Peer Into the Void", ["Rogue"], piv_eb, {"Damage Bonus": 2.75})

# ---- Meteoric Fury Weapons (Adventures in Wildspace Campaign)
mf_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 3,
          "setName": "Meteoric Fury", "pieces": 2,
          "description": "2 of Set: Deal or heal up to 3% additional damage based on HP difference. Role: DPS +2% Base Damage Boost, Tank -4% Incoming Damage, Healer +4% Overall Outgoing Healing. Doubled in Wildspace, +10% Movement Speed."}]
add("Meteoric Iron Blade", "Off Hand", 2450,
    {"Accuracy": 919, "Combat Advantage": 1838, "Forte": 919}, 2205,
    "Adventures in Wildspace Campaign", "Meteoric Fury", ["Rogue"], mf_eb)
add("Meteoric Iron Dagger", "Main Hand", 2450,
    {"Critical Strike": 1838, "Forte": 1838}, 2205,
    "Adventures in Wildspace Campaign", "Meteoric Fury", ["Rogue"], mf_eb)

# ---- Ultraviolet Armor (Set 2/17, IL 2900) — Imperial Citadel (Master) / Doomspace
cls_all = ["Rogue", "Cleric", "Bard", "Ranger"]
add("Ultraviolet Elven Hat", "Head", 2900,
    {"Combat Advantage": 2175, "Critical Severity": 2175}, 2610,
    "The Imperial Citadel (Master) / Doomspace", "Ultraviolet Armor", cls_all,
    [{"name": "Combatant's Advantage",
      "description": "For every 5 seconds you are in combat, you gain 1% Combat Advantage. Max Stacks: 10."}],
    None, 4)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
