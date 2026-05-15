"""Warlock Stronghold Set + Lionsmane Armor (Sets 10-11 of 20)."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes=None, equip=None, set_size=2):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": {}, "abilityBonuses": {},
        "notes": INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

# Warlock Stronghold Set — Stronghold Pact Blade + Stronghold Grimoire
src_sh = "Stronghold (The Outfitter)"
sh_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Stronghold Unity", "pieces": 2,
          "description": "2 of Set: You and nearby allies are granted bonuses when equipped with a Stronghold weapon set. Crafted via the Stronghold marketplace."}]
TIERS_W = [("Uncommon", 300, 112, 225, 112, 270), ("Rare", 400, 150, 300, 150, 360), ("Epic", 500, 188, 375, 188, 450), ("Legendary", 600, 225, 450, 225, 540)]
for rarity, il, acc, ca, crit, cr in TIERS_W:
    add(f"Stronghold Pact Blade ({rarity})", "Main Hand", il, {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr, src_sh, "Stronghold Unity", ["Warlock"], sh_eb, 2)
    add(f"Stronghold Grimoire ({rarity})", "Off Hand", il, {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr, src_sh, "Stronghold Unity", ["Warlock"], sh_eb, 2)

# Lionsmane Armor — multiple variants (Set 11/20). IL varies by variant.
src_ls = "Stronghold Siege / Elemental Infusion"
# Elemental Lionsmane Duelist (IL 574, PvP 634) — Combat Advantage/Defense/Awareness focus
add("Elemental Lionsmane Duelist Pigaches",    "Feet",  574, {"Combat Advantage": 215, "Defense": 410, "Awareness": 215}, 517, src_ls, "Lionsmane Set", ["Warlock"], None, 4)
add("Elemental Lionsmane Duelist Wristguards", "Arms",  574, {"Accuracy": 172, "Critical Strike": 129, "Defense": 430, "Critical Avoidance": 129}, 517, src_ls, "Lionsmane Set", ["Warlock"], None, 4)
add("Elemental Lionsmane Executioner Cowl",        "Head", 574, {"Combat Advantage": 129, "Critical Strike": 129, "Critical Severity": 172, "Defense": 430, "Awareness": 129}, 517, src_ls, "Lionsmane Set", ["Warlock"], None, 4)
add("Elemental Lionsmane Executioner Wristguards","Arms", 574, {"Critical Strike": 129, "Critical Severity": 172, "Defense": 430, "Awareness": 129}, 517, src_ls, "Lionsmane Set", ["Warlock"], None, 4)
# Lionsmane Duelist Longcoat / Medic Belt — non-infused
add("Lionsmane Duelist Longcoat", "Armor", 560, {"Accuracy": 168, "Combat Advantage": 126, "Defense": 420, "Awareness": 126}, 504, src_ls, "Lionsmane Set", ["Warlock"], None, 4)
add("Lionsmane Medic Belt",        "Belt",  588, {"Accuracy": 529, "Combat Advantage": 353}, 529, src_ls, "Lionsmane Set", ["Warlock"], None, 4)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
