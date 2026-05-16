"""Rogue gear batch 63 — Lichstone Amulet 4 tiers + Fanged Beaded Amulet 4 tiers (Masterwork Neck Sets III)."""
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

# Lichstone Amulet (Neck) — 4 tiers
LICH = [(350,315,175,175,175,1),(500,450,250,250,250,2),(650,585,325,325,325,3),(800,720,400,400,400,4)]
for il, cr, accu, ca, defl, con in LICH:
    name = "Lichstone Amulet" if il == 350 else f"Lichstone Amulet (IL {il})"
    add(name, "Neck", il, {"Accuracy": accu, "Critical Avoidance": ca, "Deflection": defl}, cr, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
        abilities={"CON": con})

# Fanged Beaded Amulet (Neck) — DPS variant — 4 tiers
FB = [(350,315,175,175,175,1),(500,450,250,250,250,2),(650,585,325,325,326,3),(800,720,400,400,401,4)]
for il, cr, accu, ca, cs, con in FB:
    name = "Fanged Beaded Amulet" if il == 350 else f"Fanged Beaded Amulet (IL {il})"
    add(name, "Neck", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_mw, "Masterwork III Equipment Set", ["Rogue"], mwn_eb,
        abilities={"CON": con})

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
