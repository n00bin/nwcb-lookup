"""Rogue gear batch 43 — Shadewalker's Relic Set: Dagger MH 3 more tiers (500/650/800) + Stiletto OH 4 tiers."""
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

src_smi = "Sea of Moving Ice / Royal Allies Campaign (Module 10)"
# Updated set bonus from popup
sw_eb = [{"type": "Set", "scope": "self", "stat": "Incoming Damage", "amount": -10,
          "setName": "Weapons of the Shadewalker", "pieces": 2,
          "description": "2 of Set: Dodge/block/sprint/shadow slip triggers Overcharge: Defense — Incoming Damage -10% and Movement Speed +5% for 10s. Encounter power triggers Overcharge: Attack — Outgoing Damage +10% and heals 15% of health over 10s. (30s CD)"}]

TIERS = [(500,450,188,375,188),(650,585,244,488,244),(800,720,300,600,300)]
# Shadewalker's Dagger MH — 3 more tiers
for il, cr, accu, ca, cs in TIERS:
    add(f"Shadewalker's Dagger (IL {il})", "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_smi, "Weapons of the Shadewalker", ["Rogue"], sw_eb)

# Shadewalker's Stiletto OH — 4 tiers
TIERS_FULL = [(350,315,131,262,131)] + TIERS
for il, cr, accu, ca, cs in TIERS_FULL:
    name = "Shadewalker's Stiletto" if il == 350 else f"Shadewalker's Stiletto (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_smi, "Weapons of the Shadewalker", ["Rogue"], sw_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
