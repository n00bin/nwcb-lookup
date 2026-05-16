"""Bard Mod 27 gear batch 8 — Weapons of the Elements Bard variants (Howling/Earthen/Burning/Drowned Rapier+Lute),
Twisted Set Bard (Twisted Makhaira), Elk Tribe Noble's Lute."""
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

src_ue = "Weapons of the Elements (Module 8)"
ELEM_TIERS = [(300,270,112,225,112),(400,360,150,300,150),(500,450,188,375,188),(600,540,225,450,225)]

# Howling Heart
hw_eb = [{"type": "Set", "scope": "self", "stat": "Movement Speed", "amount": 30,
          "setName": "Howling Heart", "pieces": 2,
          "description": "2 of Set: Dodge/block/sprint/shadow slip Movement Speed +30% for 2s. (10s CD)"}]
for il, cr, accu, ca, cs in ELEM_TIERS:
    add(f"Howling Rapier{' (IL '+str(il)+')' if il!=300 else ''}", "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ue, "Howling Heart", ["Bard"], hw_eb)
    add(f"Howling Lute{' (IL '+str(il)+')' if il!=300 else ''}", "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ue, "Howling Heart", ["Bard"], hw_eb)

# Earthen Heart
eh_eb = [{"type": "Set", "scope": "self", "stat": "Incoming Damage", "amount": -5,
          "setName": "Earthen Heart", "pieces": 2,
          "description": "2 of Set: Stand still 3s — Incoming Damage -5%. Stacks 3 times. Removed on move."}]
for il, cr, accu, ca, cs in ELEM_TIERS:
    add(f"Earthen Rapier{' (IL '+str(il)+')' if il!=300 else ''}", "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ue, "Earthen Heart", ["Bard"], eh_eb)
    add(f"Earthen Lute{' (IL '+str(il)+')' if il!=300 else ''}",   "Off Hand",  il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ue, "Earthen Heart", ["Bard"], eh_eb)

# Burning Heart
bh_eb = [{"type": "Set", "scope": "self", "stat": "Action Points", "amount": 25,
          "setName": "Burning Heart", "pieces": 2,
          "description": "2 of Set: Daily power 25% chance to immediately restore AP."}]
for il, cr, accu, ca, cs in ELEM_TIERS:
    add(f"Burning Rapier{' (IL '+str(il)+')' if il!=300 else ''}", "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ue, "Burning Heart", ["Bard"], bh_eb)
    add(f"Burning Lute{' (IL '+str(il)+')' if il!=300 else ''}",   "Off Hand",  il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ue, "Burning Heart", ["Bard"], bh_eb)

# Drowned Heart
dh_eb = [{"type": "Set", "scope": "self", "stat": "Heal Self", "amount": 50,
          "setName": "Drowned Heart", "pieces": 2,
          "description": "2 of Set: When struck, Heal for 50% of Max HP over 30s. (30s CD)"}]
for il, cr, accu, ca, cs in ELEM_TIERS:
    add(f"Drowned Rapier{' (IL '+str(il)+')' if il!=300 else ''}", "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ue, "Drowned Heart", ["Bard"], dh_eb)
    add(f"Drowned Lute{' (IL '+str(il)+')' if il!=300 else ''}",   "Off Hand",  il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ue, "Drowned Heart", ["Bard"], dh_eb)

# Twisted Set (Mod 6 Underdark/Duality)
src_ud = "Underdark / Demogorgon (Master) / Mantol-Derith"
tw_eb = [{"type": "Set", "scope": "self", "stat": "Defense", "amount": 160,
          "setName": "Duality", "pieces": 2,
          "description": "2 of Set: Paranoia stacks (max 24): +160 Defense per stack when struck. Bloodlust stacks: +160 Power per stack when striking."}]
TWIST_TIERS = [(300,270,112,225,112),(400,360,150,300,150),(500,450,188,375,188),(600,540,225,450,225)]
for il, cr, accu, ca, cs in TWIST_TIERS:
    name = "Twisted Makhaira" if il == 300 else f"Twisted Makhaira (IL {il})"
    add(name + " (Bard)", "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ud, "Duality", ["Bard"], tw_eb)
for il, cr, accu, ca, cs in TWIST_TIERS:
    name = "Twisted Misericorde" if il == 300 else f"Twisted Misericorde (IL {il})"
    add(name + " (Bard)", "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ud, "Duality", ["Bard"], tw_eb)

# Elk Tribe Noble's Lute (Bard OH) — Weapons of the Elk Tribe Chiefs
src_iwp = "Icewind Pass (Module 4)"
ET_eb = [{"type": "Set", "scope": "self", "stat": "Stat", "amount": 0,
          "setName": "Weapons of the Elk Tribe Chiefs", "pieces": 2,
          "description": "2 of Set: Elk Tribe weapon set bonus from Icewind Pass."}]
add("Elk Tribe Noble's Lute", "Off Hand", 399,
    {"Combat Advantage": 202, "Critical Strike": 202, "Critical Severity": 98, "Critical Avoidance": 98}, 359,
    src_iwp, "Weapons of the Elk Tribe Chiefs", ["Bard"], ET_eb, set_size=2)

# Elk Tribe Noble's Poniard variant for Bard (if shared)
add("Elk Tribe Noble's Poniard (Bard)", "Main Hand", 399,
    {"Combat Advantage": 202, "Critical Strike": 202, "Critical Severity": 98, "Critical Avoidance": 98}, 359,
    src_iwp, "Weapons of the Elk Tribe Chiefs", ["Bard"], ET_eb, set_size=2)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
