"""Rogue gear batch 30 — Pioneer Sakin OH (4 tiers) + Exalted Pioneer Jambiya MH (4 tiers)."""
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

src_pi = "Other Miscellaneous Sources"
pio_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 200,
           "setName": "Pioneer", "pieces": 2,
           "description": "2 of Set: Pioneer Jambiya + Pioneer Sakin. Increased stat per party member (1=+200 Power; 2=+400 P/Def; 3=+600 P/Def/Acc; 4=+800 P/Def/Acc/CS; 5=+1000 P/Def/Acc/CS/CritSev)."}]
TIERS = [(350,315,131,262,131),(500,450,188,375,188),(650,585,244,488,244),(800,720,300,600,300)]

# Pioneer Sakin OH — 4 tiers
for il, cr, accu, ca, cs in TIERS:
    name = "Pioneer Sakin" if il == 350 else f"Pioneer Sakin (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_pi, "Pioneer", ["Rogue"], pio_eb)

# Exalted Pioneer Jambiya MH — 4 tiers
for il, cr, accu, ca, cs in TIERS:
    name = "Exalted Pioneer Jambiya" if il == 350 else f"Exalted Pioneer Jambiya (IL {il})"
    add(name, "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_pi, "Pioneer", ["Rogue"], pio_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
