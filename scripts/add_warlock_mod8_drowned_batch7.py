"""Module 8 Drowned elemental set."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Module 8 Drowned elemental + Mod 4 Elemental Elven — screenshot intake 2026-05-14."

def add(name, slot, il, rs, cr, source, set_name, classes, equip=None, set_size=2):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": {}, "abilityBonuses": {},
        "notes": INTAKE, "allowedClasses": classes}
    data.append(entry)

src_elem = "Weapons of the Elements (Module 8 / Elemental Evil)"
TIERS = [
    ("Uncommon",  300, 112, 225, 112, 270),
    ("Rare",      400, 150, 300, 150, 360),
    ("Epic",      500, 188, 375, 188, 450),
    ("Legendary", 600, 225, 450, 225, 540),
]
drowned_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0, "setName": "Drowned Heart", "pieces": 2,
               "description": "2 of Set: When you are struck, Heal for 50% of your Maximum Hit Points over the next 30 seconds, this effect may only occur once every 60 seconds. Disabled in Thay Arena PvP."}]
for rarity, il, acc, ca, crit, cr in TIERS:
    add(f"Drowned Pact Blade ({rarity})", "Main Hand", il,
        {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr,
        src_elem, "Drowned Heart", ["Warlock"], drowned_eb)
    add(f"Drowned Grimoire ({rarity})", "Off Hand", il,
        {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr,
        src_elem, "Drowned Heart", ["Warlock"], drowned_eb)

# Elemental Elven Armor (Mod 4 Tyranny of Dragons era, infused) — start
src_ee = "Elemental Infusion (Czer-Konig)"
add("Elemental Elven Raid Cowl", "Head", 575, {"Accuracy": 259, "Combat Advantage": 172, "Defense": 431}, 518, src_ee, "Elemental Elven Armor", ["Warlock"], None, set_size=4)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
