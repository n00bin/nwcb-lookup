"""Rogue gear batch 71 — Rubellite Sash 4 tiers + Stronghold Dagger MH 2 tiers (Rogue Stronghold Set)."""
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

src_mw2 = "Masterwork Crafting (Mod 11)"
mw2_eb = [{"type": "Set", "scope": "self", "stat": "Accuracy", "amount": 500,
           "setName": "Masterwork II Equipment Set", "pieces": 2,
           "description": "2 of Set: Encounter triggers Alacrity — 500 Accuracy + 1000 Movement for 5s. Max 3 stacks."}]

# Rubellite Sash (Belt) — 4 tiers
RB = [(350,315,175,175,175,1,1),(500,450,250,250,250,1,1),(650,585,325,325,326,2,1),(800,720,400,400,401,2,2)]
for il, cr, accu, ca, cs, intel, cha in RB:
    name = "Rubellite Sash" if il == 350 else f"Rubellite Sash (IL {il})"
    add(name, "Belt", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_mw2, "Masterwork II Equipment Set", ["Rogue"], mw2_eb,
        abilities={"INT": intel, "CHA": cha})

# Stronghold Dagger MH — 2 tiers (Set 10/20)
src_sh = "Stronghold Outfitter"
stronghold_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 2,
                  "setName": "Stronghold Unity", "pieces": 2,
                  "description": "2 of Set: You and nearby allies: +2% BDB, +2% OOH, -2% Incoming Damage. Stacks up to 5x with similar Stronghold weapons."}]
add("Stronghold Dagger",          "Main Hand", 300, {"Accuracy": 112, "Combat Advantage": 225, "Critical Strike": 112}, 270, src_sh, "Stronghold Unity", ["Rogue"], stronghold_eb)
add("Stronghold Dagger (IL 400)", "Main Hand", 400, {"Accuracy": 150, "Combat Advantage": 300, "Critical Strike": 150}, 360, src_sh, "Stronghold Unity", ["Rogue"], stronghold_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
