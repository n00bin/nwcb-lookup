"""Masterwork Waist Sets III — Bronzewood + Lichstone sashes (4 IL tiers each)."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes=None, equip=None, set_size=2, abilities=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": {}, "abilityBonuses": abilities or {},
        "notes": INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

src_mw = "Masterwork Crafting (Module 13)"
mw_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Masterwork III Equipment Set", "pieces": 2,
          "description": "2 of Set: When you use an encounter power, you gain a stack of Alacrity, granting 1% Accuracy and 5% Movement Speed for 5 seconds. Stacks up to 3 times."}]

# Bronzewood Sash — Belt, 4 IL tiers, DPS/Combat Advantage focus
for rarity, il, ca, crit, cr, ab in [
    ("Uncommon",  350, 175, 175, 315, {"STR": 1, "DEX": 1}),
    ("Rare",      500, 250, 250, 450, {"STR": 1, "DEX": 1}),
    ("Epic",      650, 325, 326, 585, {"STR": 1, "DEX": 2}),
    ("Legendary", 800, 400, 401, 720, {"STR": 2, "DEX": 2}),
]:
    add(f"Bronzewood Sash ({rarity})", "Belt", il,
        {"Combat Advantage": ca, "Critical Strike": ca, "Critical Severity": crit}, cr,
        src_mw, "Masterwork III Equipment Set", ["Warlock"], mw_eb, 2, ab)

# Lichstone Sash — Belt, 4 IL tiers, Defense/Tank focus
for rarity, il, ca, cd, cr, ab in [
    ("Uncommon",  350, 350, 175, 315, {"CON": 2}),
    ("Rare",      500, 500, 250, 450, {"CON": 2}),
    ("Epic",      650, 649, 325, 585, {"CON": 3}),
    ("Legendary", 800, 799, 400, 720, {"CON": 4}),
]:
    add(f"Lichstone Sash ({rarity})", "Belt", il,
        {"Critical Avoidance": ca, "Deflection": cd}, cr,
        src_mw, "Masterwork III Equipment Set", ["Warlock"], mw_eb, 2, ab)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
