"""Rogue gear batch 29 — Pilgrim Exalted Fleshskewer OH 3 tiers + Pioneer Weapons (Jambiya MH 4 tiers)."""
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

TIERS = [(350,315,131,262,131),(500,450,188,375,188),(650,585,244,488,244),(800,720,300,600,300)]

# Pilgrim Exalted Fleshskewer OH remaining tiers (500/650/800)
src_shar = "Sharandar"
pil_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 1,
           "setName": "Pilgrim", "pieces": 2,
           "description": "2 of Set: At start of combat, BDB and OOH +1% per enemy faced. If facing only 1 enemy, BDB and OOH +3% for 1 minute."}]
for il, cr, accu, ca, cs in TIERS[1:]:
    add(f"Exalted Fleshskewer (IL {il})", "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_shar, "Pilgrim", ["Rogue"], pil_eb)

# Pioneer Weapons (Other Miscellaneous Sources)
src_pi = "Other Miscellaneous Sources"
pio_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 200,
           "setName": "Pioneer", "pieces": 2,
           "description": "2 of Set: Pioneer Jambiya + Pioneer Sakin. Increased stat for each party member: Party 1 = +200 Power; Party 2 = +400 Power and Defense; Party 3 = +600 Power, Defense, Accuracy; Party 4 = +800 Power, Defense, Accuracy, CS; Party 5 = +1000 Power, Defense, Accuracy, CS, CritSev."}]

# Pioneer Jambiya MH — 4 tiers
for il, cr, accu, ca, cs in TIERS:
    name = "Pioneer Jambiya" if il == 350 else f"Pioneer Jambiya (IL {il})"
    add(name, "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_pi, "Pioneer", ["Rogue"], pio_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
