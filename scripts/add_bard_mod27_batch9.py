"""Bard Mod 27 gear batch 9 — Mod 15 Cloaked Ascendancy (Mirage/Fey/Lifeforged/Aboleth Bard variants)
+ Shadewalker's (Mod 10) Bard variants + Sun Set (Ravenloft) Bard."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Mod 27 Bard gear — screenshot intake 2026-05-16."

def add(name, slot, il, rs, cr, source, set_name, classes, equip=None, percent=None, set_size=2, abilities=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": percent or {}, "abilityBonuses": abilities or {},
        "allowedClasses": classes, "notes": INTAKE}
    data.append(entry)

src_ca = "Cloaked Ascendancy Campaign Vendor / River District (Module 15)"
TIERS = [(350,315,131,262,131),(500,450,188,375,188),(650,585,244,488,244),(800,720,300,600,300)]

# Mirage (Bard) — Mirage Rapier MH + Mirage Lute OH
mir_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 3,
           "setName": "Mirage", "pieces": 2,
           "description": "2 of Set: Encounter triggers Master of Illusion (10s): illusion attacks enemies, +3% damage. (30s CD)"}]
for il, cr, accu, ca, cs in TIERS:
    add(f"Mirage Rapier{' (IL '+str(il)+')' if il!=350 else ''}", "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ca, "Mirage", ["Bard"], mir_eb)
    add(f"Mirage Lute{' (IL '+str(il)+')' if il!=350 else ''}",   "Off Hand",  il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ca, "Mirage", ["Bard"], mir_eb)

# Fey (Bard) — Fey Rapier MH + Fey Lute OH
fey_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 3,
           "setName": "Fey", "pieces": 2,
           "description": "2 of Set: Fey-Touched on encounter power: 10% AP + 3% BDB + 6% OOH for 10s. (30s CD)"}]
for il, cr, accu, ca, cs in TIERS:
    add(f"Fey Rapier{' (IL '+str(il)+')' if il!=350 else ''}", "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ca, "Fey", ["Bard"], fey_eb)
    add(f"Fey Lute{' (IL '+str(il)+')' if il!=350 else ''}",   "Off Hand",  il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ca, "Fey", ["Bard"], fey_eb)

# Lifeforged (Bard)
lf_eb = [{"type": "Set", "scope": "self", "stat": "Defense", "amount": 5,
          "setName": "Lifeforged", "pieces": 2,
          "description": "2 of Set: Encounter triggers Fortified: Defense +5%, 10% of Defense added to Power for 10s. (30s CD)"}]
for il, cr, accu, ca, cs in TIERS:
    add(f"Lifeforged Rapier{' (IL '+str(il)+')' if il!=350 else ''}", "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ca, "Lifeforged", ["Bard"], lf_eb)
    add(f"Lifeforged Lute{' (IL '+str(il)+')' if il!=350 else ''}",   "Off Hand",  il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ca, "Lifeforged", ["Bard"], lf_eb)

# Aboleth (Bard) — Sea of Moving Ice Mod 12
src_sk = "Sea of Moving Ice / Storm King's Thunder (Module 12)"
ab_eb = [{"type": "Set", "scope": "self", "stat": "Outgoing Damage", "amount": 4,
          "setName": "Aboleth", "pieces": 2,
          "description": "2 of Set: Encounter triggers Far-Influenced: Outgoing Damage +4% + random buff for 10s. (30s CD)"}]
for il, cr, accu, ca, cs in TIERS:
    add(f"Aboleth Rapier{' (IL '+str(il)+')' if il!=350 else ''}", "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_sk, "Aboleth", ["Bard"], ab_eb)
    add(f"Aboleth Lute{' (IL '+str(il)+')' if il!=350 else ''}",   "Off Hand",  il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_sk, "Aboleth", ["Bard"], ab_eb)

# Shadewalker's (Mod 10) Bard
src_smi = "Sea of Moving Ice / Royal Allies Campaign (Module 10)"
sw_eb = [{"type": "Set", "scope": "self", "stat": "Incoming Damage", "amount": -10,
          "setName": "Weapons of the Shadewalker", "pieces": 2,
          "description": "2 of Set: Dodge/block/sprint/shadow slip triggers Overcharge: Defense — Incoming Damage -10% and Movement Speed +5% for 10s. Encounter triggers Overcharge: Attack — Outgoing Damage +10% and heals 15% of health over 10s. (30s CD)"}]
for il, cr, accu, ca, cs in TIERS:
    add(f"Shadewalker's Rapier{' (IL '+str(il)+')' if il!=350 else ''}", "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_smi, "Weapons of the Shadewalker", ["Bard"], sw_eb)
    add(f"Shadewalker's Lute{' (IL '+str(il)+')' if il!=350 else ''}",   "Off Hand",  il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_smi, "Weapons of the Shadewalker", ["Bard"], sw_eb)

# Sun Set (Bard) — Ravenloft Mod 14
src_rv = "Ravenloft (Module 14) — Bonvia"
sun_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 5,
           "setName": "Sun Set", "pieces": 2,
           "description": "2 of Set: Base Damage Boost and OOH +5%. In Bonvia during nightfall, BDB/Damage Resistance/OOH/Movement Speed +10%."}]
SUN_TIERS = [(350,315,131,262,131),(500,450,188,375,188),(650,585,244,488,244),(800,720,300,600,300)]
for il, cr, accu, ca, cs in SUN_TIERS:
    add(f"Sunset Rapier{' (IL '+str(il)+')' if il!=350 else ''}", "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_rv, "Sun Set", ["Bard"], sun_eb)
    add(f"Sunset Lute{' (IL '+str(il)+')' if il!=350 else ''}",   "Off Hand",  il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_rv, "Sun Set", ["Bard"], sun_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
