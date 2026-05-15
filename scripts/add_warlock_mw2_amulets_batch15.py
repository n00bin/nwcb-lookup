"""Masterwork II Neck Sets II — Silverspruce, Sphene, Rubellite amulets."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Legacy Warlock gear screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes=None, set_size=2, ab=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": {}, "abilityBonuses": ab or {},
        "notes": INTAKE}
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

src_mw2n = "Masterwork Crafting (Module 11)"
SET = "Masterwork II Equipment Set"

# Silverspruce Amulet (Tank — Accuracy/Critical Avoidance/Deflection + CON)
for rarity, il, base, cd, cr, ab in [
    ("Uncommon",  350, 175, 175, 315, {"CON": 1}),
    ("Rare",      500, 250, 250, 450, {"CON": 2}),
    ("Epic",      650, 325, 325, 585, {"CON": 3}),
    ("Legendary", 800, 400, 400, 720, {"CON": 4}),
]:
    add(f"Silverspruce Amulet ({rarity})", "Neck", il,
        {"Accuracy": base, "Critical Avoidance": base, "Deflection": cd}, cr,
        src_mw2n, SET, ["Warlock"], 2, ab)

# Sphene Amulet (DPS — Accuracy/CA/Crit Strike + CON)
for rarity, il, base, cd, cr, ab in [
    ("Uncommon",  350, 175, 175, 315, {"CON": 1}),
    ("Rare",      500, 250, 250, 450, {"CON": 2}),
    ("Epic",      650, 325, 326, 585, {"CON": 3}),
    ("Legendary", 800, 400, 401, 720, {"CON": 4}),
]:
    add(f"Sphene Amulet ({rarity})", "Neck", il,
        {"Accuracy": base, "Combat Advantage": base, "Critical Strike": cd}, cr,
        src_mw2n, SET, ["Warlock"], 2, ab)

# Rubellite Amulet (DPS — CA/Crit Strike/Crit Sev + CON)
for rarity, il, base, cd, cr, ab in [
    ("Uncommon",  350, 175, 175, 315, {"CON": 1}),
    ("Rare",      500, 250, 250, 450, {"CON": 2}),
    ("Epic",      650, 325, 326, 585, {"CON": 3}),
    ("Legendary", 800, 400, 401, 720, {"CON": 4}),
]:
    add(f"Rubellite Amulet ({rarity})", "Neck", il,
        {"Combat Advantage": base, "Critical Strike": base, "Critical Severity": cd}, cr,
        src_mw2n, SET, ["Warlock"], 2, ab)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
