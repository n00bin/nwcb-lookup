"""Rogue gear batch 27 — Exalted Primal Itecpayo OH 4 tiers + Pilgrim Weapons (Fleshtearer MH 2 tiers)."""
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

src_ch = "Chult Hunts / Sharandar (Module 11)"
prim_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 10,
            "setName": "Primal", "pieces": 2,
            "description": "2 of Set: Primal Recipuyo. If hit/healed for more than 10% of Max HP in a single blow, BDB and OOH +10% for 10s."}]

# Exalted Primal Itecpayo OH — 4 tiers
for il, cr, accu, ca, cs in [(350,315,131,262,131),(500,450,188,375,188),(650,585,244,488,244),(800,720,300,600,300)]:
    name = "Exalted Primal Itecpayo" if il == 350 else f"Exalted Primal Itecpayo (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ch, "Primal", ["Rogue"], prim_eb)

# Pilgrim Weapons (Sharandar) — Fleshtearer MH 2 tiers (350, 500)
src_shar = "Sharandar"
pil_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 1,
           "setName": "Pilgrim", "pieces": 2,
           "description": "2 of Set: At start of combat, BDB and OOH +1% per enemy faced (max for 10s). If facing only 1 enemy, BDB and OOH +3% for 1 minute. Refreshes on kill."}]
add("Fleshtearer",          "Main Hand", 350,
    {"Accuracy": 131, "Combat Advantage": 262, "Critical Strike": 131}, 315, src_shar, "Pilgrim", ["Rogue"], pil_eb)
add("Fleshtearer (IL 500)", "Main Hand", 500,
    {"Accuracy": 188, "Combat Advantage": 375, "Critical Strike": 188}, 450, src_shar, "Pilgrim", ["Rogue"], pil_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
