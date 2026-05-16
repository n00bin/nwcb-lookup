"""Rogue gear batch 64 — Bronzewood Amulet 4 tiers + Titansteel Dagger MH 3 tiers (Masterwork II)."""
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

src_mw = "Masterwork Crafting (Mod 13)"
mwn_eb = [{"type": "Set", "scope": "self", "stat": "Accuracy", "amount": 1,
           "setName": "Masterwork III Equipment Set", "pieces": 2,
           "description": "2 of Set: Encounter triggers Alacrity — 1% Accuracy + 5% Movement Speed for 3s. Max 3 stacks."}]

# Bronzewood Amulet (Neck) — 4 tiers — Accuracy/CA/CritStrike rating combo
BW = [(350,315,175,175,175,1),(500,450,250,250,250,2),(650,585,325,325,326,3),(800,720,400,400,401,4)]
for il, cr, accu, ca, cs, con in BW:
    name = "Bronzewood Amulet" if il == 350 else f"Bronzewood Amulet (IL {il})"
    add(name, "Neck", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
        abilities={"CON": con})

# Masterwork II Weapon Set (Mod 11 Shroud of Souls) — Titansteel Dagger MH 3 tiers
src_sos = "Masterwork Crafting / The Shroud of Souls (Module 11)"
mw2_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 2,
           "setName": "Masterwork II Weapon Set", "pieces": 2,
           "description": "2 of Set: You and nearby allies: +2% BDB, +2% OOH, -2% Incoming Damage. Stacks up to 5x with allies in Stronghold weapons."}]
TIERS = [(350,315,131,262,131),(500,450,188,375,188),(650,585,244,488,244)]
for il, cr, accu, ca, cs in TIERS:
    name = "Titansteel Dagger" if il == 350 else f"Titansteel Dagger (IL {il})"
    add(name, "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_sos, "Masterwork II Weapon Set", ["Rogue"], mw2_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
