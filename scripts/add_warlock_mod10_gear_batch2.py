"""Module 10 Hexweaver's Relic Set (Storm King's Thunder Royal Allies) + Cloaked Ascendancy artifact armor."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)

INTAKE = "Legacy Warlock gear screenshot intake 2026-05-14."

def add(name, slot, il, rs, cr, source, set_name, equip, classes=None, percent=None, notes=None):
    global max_id
    max_id += 1
    entry = {
        "id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": 2 if set_name else 0,
        "source": source, "percentStats": percent or {}, "abilityBonuses": {},
        "notes": notes or INTAKE
    }
    if classes: entry["allowedClasses"] = classes
    data.append(entry)

# Morlanth's Shroud — Module 11 River District artifact armor (companion-tier)
add("Morlanth's Shroud", "Armor", 610,
    {"Accuracy": 284, "Combat Advantage": 189, "Defense": 472}, 567,
    "Shard of Night (River District / Module 11)", None, None,
    classes=["Warlock"],
    notes="Companion / armor artifact. When you have less than 10% health and you kill an enemy, you gain 25% of your health back. " + INTAKE)

# Hexweaver's Set (Storm King's Thunder Module 10) — Pact Blade + Grimoire × 4 IL tiers
hex_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 0,
           "setName": "Weapons of the Hexweaver", "pieces": 2,
           "description": "2 of Set: If you dodge, block, sprint or shadow slip, you gain Overcharge: Defense — decreases your incoming damage by 15% for 10s. May only activate Overcharge once every 30s. If you use an encounter power, you gain Overcharge: Attack — increases your outgoing damage by 10% and heals you 15% of your health over 10s. May only activate an Overcharge power once every 30s."}]
TIERS = [
    ("Uncommon",  350, 131, 262, 131, 315),
    ("Rare",      500, 188, 375, 188, 450),
    ("Epic",      650, 244, 488, 244, 585),
    ("Legendary", 800, 300, 600, 300, 720),
]
for rarity, il, acc, ca, crit, cr in TIERS:
    add(f"Hexweaver's Pact Blade ({rarity})", "Main Hand", il,
        {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr,
        "Sea of Moving Ice (Module 10) / Royal Allies",
        "Weapons of the Hexweaver", hex_eb, classes=["Warlock"])
    add(f"Hexweaver's Grimoire ({rarity})", "Off Hand", il,
        {"Accuracy": acc, "Combat Advantage": ca, "Critical Strike": crit}, cr,
        "Sea of Moving Ice (Module 10) / Royal Allies",
        "Weapons of the Hexweaver", hex_eb, classes=["Warlock"])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
