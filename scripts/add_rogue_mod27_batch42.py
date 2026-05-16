"""Rogue gear batch 42 — Aboleth Dagger MH IL 800, Aboleth Stiletto OH 4 tiers,
Shadewalker's Relic Set start (Module 10)."""
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

src_sk = "Sea of Moving Ice / Storm King's Thunder (Module 12)"
ab_eb = [{"type": "Set", "scope": "self", "stat": "Outgoing Damage", "amount": 4,
          "setName": "Aboleth", "pieces": 2,
          "description": "2 of Set: Encounter power triggers Far-Influenced: Outgoing Damage +4% + random buff for 10s. (30s CD)"}]

# Aboleth Dagger MH IL 800
add("Aboleth Dagger (IL 800)", "Main Hand", 800, {"Accuracy": 300, "Combat Advantage": 600, "Critical Strike": 300}, 720, src_sk, "Aboleth", ["Rogue"], ab_eb)

# Aboleth Stiletto OH — 4 tiers
TIERS = [(350,315,131,262,131),(500,450,188,375,188),(650,585,244,488,244),(800,720,300,600,300)]
for il, cr, accu, ca, cs in TIERS:
    name = "Aboleth Stiletto" if il == 350 else f"Aboleth Stiletto (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_sk, "Aboleth", ["Rogue"], ab_eb)

# Shadewalker's Relic Set (Mod 10 Sea of Moving Ice / Royal Allies) — start
src_smi = "Sea of Moving Ice / Royal Allies Campaign (Module 10)"
sw_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 500,
          "setName": "Weapons of the Shadewalker", "pieces": 2,
          "description": "2 of Set: A set of relic weapons from Module 10. Restore through Royal Allies campaign."}]
add("Shadewalker's Dagger", "Main Hand", 350, {"Accuracy": 131, "Combat Advantage": 262, "Critical Strike": 131}, 315, src_smi, "Weapons of the Shadewalker", ["Rogue"], sw_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
