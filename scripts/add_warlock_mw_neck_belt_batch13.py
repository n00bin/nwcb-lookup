"""Masterwork Waist + Neck Sets III — Fanged + Beaded belts, Beaded + Lichstone amulets."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes=None, set_size=2, abilities=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": {}, "abilityBonuses": abilities or {},
        "notes": INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

src_mw = "Masterwork Crafting (Module 13)"
SET = "Masterwork III Equipment Set"

# Fanged Sash (Belt) — Accuracy/CA/Crit Strike with WIS/CHA bonus
for rarity, il, base, cd, cr, ab in [
    ("Uncommon",  350, 175, 175, 315, {"WIS": 1, "CHA": 1}),
    ("Rare",      500, 250, 250, 450, {"WIS": 1, "CHA": 1}),
    ("Epic",      650, 325, 326, 585, {"WIS": 2, "CHA": 1}),
    ("Legendary", 800, 400, 401, 720, {"WIS": 2, "CHA": 2}),
]:
    add(f"Fanged Sash ({rarity})", "Belt", il,
        {"Accuracy": base, "Combat Advantage": base, "Critical Strike": cd}, cr,
        src_mw, SET, ["Warlock"], 2, ab)

# Beaded Sash (Belt) — Accuracy/CA/Crit Strike with INT/CHA bonus
for rarity, il, base, cd, cr, ab in [
    ("Uncommon",  350, 175, 175, 315, {"INT": 1, "CHA": 1}),
    ("Rare",      500, 250, 250, 450, {"INT": 1, "CHA": 1}),
    ("Epic",      650, 325, 326, 585, {"INT": 2, "CHA": 1}),
    ("Legendary", 800, 400, 401, 720, {"INT": 2, "CHA": 2}),
]:
    add(f"Beaded Sash ({rarity})", "Belt", il,
        {"Accuracy": base, "Combat Advantage": base, "Critical Strike": cd}, cr,
        src_mw, SET, ["Warlock"], 2, ab)

# Beaded Amulet (Neck) — CA/Crit Strike/Crit Sev with CON
for rarity, il, base, cd, cr, ab in [
    ("Uncommon",  350, 175, 175, 315, {"CON": 1}),
    ("Rare",      500, 250, 250, 450, {"CON": 2}),
    ("Epic",      650, 325, 326, 585, {"CON": 3}),
    ("Legendary", 800, 400, 401, 720, {"CON": 4}),
]:
    add(f"Beaded Amulet ({rarity})", "Neck", il,
        {"Combat Advantage": base, "Critical Strike": base, "Critical Severity": cd}, cr,
        src_mw, SET, ["Warlock"], 2, ab)

# Lichstone Amulet (Neck) — Accuracy/Critical Avoidance/Deflection with CON
for rarity, il, base, cd, cr, ab in [
    ("Uncommon",  350, 175, 175, 315, {"CON": 1}),
    ("Rare",      500, 250, 250, 450, {"CON": 2}),
    ("Epic",      650, 325, 326, 585, {"CON": 3}),
    ("Legendary", 800, 400, 401, 720, {"CON": 4}),
]:
    add(f"Lichstone Amulet ({rarity})", "Neck", il,
        {"Accuracy": base, "Critical Avoidance": base, "Deflection": cd}, cr,
        src_mw, SET, ["Warlock"], 2, ab)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
