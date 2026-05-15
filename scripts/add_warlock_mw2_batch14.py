"""Module 11 Masterwork II — Manticore armor + Stronghold II weapons + Neck Sets II."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes=None, equip=None, set_size=2, ab=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": {}, "abilityBonuses": ab or {},
        "notes": INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

# Masterwork II Stronghold weapons (Mod 11 Shroud of Souls): Fartouched Pact Blade + Manticore Grimoire
src_mw2w = "Masterwork Crafting (Module 11 Shroud of Souls)"
mw2w_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Masterwork II Weapon Set", "pieces": 2,
            "description": "2 of Set: You and nearby allies are granted bonuses when equipped with a full set of Stronghold II weapons."}]
TIERS_W = [
    ("Uncommon",  350, 131, 262, 131, 315),
    ("Rare",      500, 188, 375, 188, 450),
    ("Epic",      650, 244, 488, 244, 585),
    ("Legendary", 800, 300, 600, 300, 720),
]
for rarity, il, acc, ca, crit, cr in TIERS_W:
    add(f"Fartouched Pact Blade ({rarity})", "Main Hand", il, {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr, src_mw2w, "Masterwork II Weapon Set", ["Warlock"], mw2w_eb, 2)
    add(f"Manticore Grimoire ({rarity})",    "Off Hand",  il, {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr, src_mw2w, "Masterwork II Weapon Set", ["Warlock"], mw2w_eb, 2)

# Manticore Armor (Masterwork II) — Raid + Assault + Executioner + Duelist variants, IL 756
src_mw2a = "Masterwork Crafting (Module 11 Shroud of Souls)"
for variant, stats_pattern, ability_label in [
    ("Raid",       {"Combat Advantage": 227, "Critical Strike": 340, "Defense": 567}, "Gladiator's Accuracy"),
    ("Assault",    {"Critical Strike": 340, "Critical Severity": 227, "Defense": 567}, "Gladiator's Focus"),
    ("Executioner",{"Combat Advantage": 170, "Critical Strike": 227, "Critical Severity": 170, "Awareness": 170, "Defense": 547}, "Survivor's Parry"),
    ("Duelist",    {"Accuracy": 227, "Combat Advantage": 170, "Critical Strike": 170, "Defense": 567}, "Survivor's Parry"),
]:
    for slot_name, slot in [("Cowl", "Head"), ("Longcoat", "Armor"), ("Wristguards", "Arms"), ("Pigaches", "Feet")]:
        add(f"Manticore {variant} {slot_name}", slot, 756, stats_pattern, 680, src_mw2a, "Manticore Set", ["Warlock"], None, 4)

# Scintillant Amulet (Masterwork II Neck) — 4 IL tiers
src_mw2n = "Masterwork Crafting (Module 11)"
mw2_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Masterwork II Equipment Set", "pieces": 2,
           "description": "2 of Set: When you use an encounter power, you gain a stack of Alacrity, granting 500 Accuracy and 1000 Movement for 5 seconds. Stacks up to 3 times."}]
for rarity, il, base, cd, cr, ab in [
    ("Uncommon",  350, 175, 175, 315, {"CON": 1}),
    ("Rare",      500, 250, 250, 450, {"CON": 2}),
    ("Epic",      650, 325, 326, 585, {"CON": 3}),
    ("Legendary", 800, 400, 401, 720, {"CON": 4}),
]:
    add(f"Scintillant Amulet ({rarity})", "Neck", il,
        {"Accuracy": base, "Combat Advantage": base, "Critical Strike": cd}, cr,
        src_mw2n, "Masterwork II Equipment Set", ["Warlock"], mw2_eb, 2, ab)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
