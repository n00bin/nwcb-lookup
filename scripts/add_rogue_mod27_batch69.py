"""Rogue gear batch 69 — Rubellite Amulet 4 tiers + Scintillant Sash 3 tiers (Masterwork II)."""
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

# Rubellite Amulet (Neck) — 4 tiers
RB = [(350,315,175,175,175,1),(500,450,250,250,250,2),(650,585,325,326,325,3),(800,720,400,401,400,4)]
for il, cr, ca, cs, csev, con in RB:
    name = "Rubellite Amulet" if il == 350 else f"Rubellite Amulet (IL {il})"
    add(name, "Neck", il, {"Combat Advantage": ca, "Critical Strike": cs, "Critical Severity": csev}, cr, src_mw2, "Masterwork II Equipment Set", ["Rogue"], mw2_eb,
        abilities={"CON": con})

# Scintillant Sash (Belt) — 3 tiers (350/500/650 + 800 to come)
SC = [(350,315,175,175,175,1,1),(500,450,250,250,250,1,1),(650,585,325,326,325,1,2)]
for il, cr, ca, cs, csev, strv, dex in SC:
    name = "Scintillant Sash (Mod 11)" if il == 350 else f"Scintillant Sash (Mod 11, IL {il})"
    add(name, "Belt", il, {"Combat Advantage": ca, "Critical Strike": cs, "Critical Severity": csev}, cr, src_mw2, "Masterwork II Equipment Set", ["Rogue"], mw2_eb,
        abilities={"STR": strv, "DEX": dex})

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
