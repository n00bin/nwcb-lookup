"""Masterwork II Waist Sets II — Scintillant, Silverspruce, Sphene, Rubellite sashes."""
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

src_mw2 = "Masterwork Crafting (Module 11)"
SET = "Masterwork II Equipment Set"
TIERS = [(350, 175, 175, 315), (500, 250, 250, 450), (650, 325, 326, 585), (800, 400, 401, 720)]
RARITY = {350: "Uncommon", 500: "Rare", 650: "Epic", 800: "Legendary"}

# Scintillant Sash — DPS focus
for il, base, cd, cr in TIERS:
    ab = {"STR": il // 350, "DEX": il // 350}
    add(f"Scintillant Sash ({RARITY[il]})", "Belt", il,
        {"Combat Advantage": base, "Critical Strike": base, "Critical Severity": cd}, cr,
        src_mw2, SET, ["Warlock"], 2, ab)

# Silverspruce Belt/Sash — Tank focus
for il, base, cd, cr in TIERS:
    ab = {"CON": il // 350 + 1}
    add(f"Silverspruce Belt ({RARITY[il]})", "Belt", il,
        {"Critical Avoidance": base * 2, "Deflection": cd}, cr,
        src_mw2, SET, ["Warlock"], 2, ab)

# Sphene Sash — DPS Accuracy
for il, base, cd, cr in TIERS:
    ab = {"WIS": il // 350, "CHA": il // 350}
    add(f"Sphene Sash ({RARITY[il]})", "Belt", il,
        {"Accuracy": base, "Combat Advantage": base, "Critical Strike": cd}, cr,
        src_mw2, SET, ["Warlock"], 2, ab)

# Rubellite Sash — Crit Sev/Crit Strike
for il, base, cd, cr in TIERS:
    ab = {"INT": il // 350, "CHA": il // 350}
    add(f"Rubellite Sash ({RARITY[il]})", "Belt", il,
        {"Accuracy": base, "Combat Advantage": base, "Critical Strike": cd}, cr,
        src_mw2, SET, ["Warlock"], 2, ab)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
