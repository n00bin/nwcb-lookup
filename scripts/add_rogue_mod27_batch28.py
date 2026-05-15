"""Rogue gear batch 28 — Pilgrim Weapons completion (Fleshtearer MH + Fleshskewer OH +
Exalted Fleshtearer MH + Exalted Fleshskewer OH, all 4 IL tiers each)."""
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

src_shar = "Sharandar"
pil_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 1,
           "setName": "Pilgrim", "pieces": 2,
           "description": "2 of Set: At start of combat, BDB and OOH +1% per enemy faced. If facing only 1 enemy, BDB and OOH +3% for 1 minute. Refreshes on kill."}]

# Standard weapon tier stats
TIERS = [(350, 315, 131, 262, 131), (500, 450, 188, 375, 188),
         (650, 585, 244, 488, 244), (800, 720, 300, 600, 300)]

# Fleshtearer MH remaining tiers (650, 800)
for il, cr, accu, ca, cs in TIERS[2:]:
    add(f"Fleshtearer (IL {il})", "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_shar, "Pilgrim", ["Rogue"], pil_eb)

# Fleshskewer OH — 4 tiers
for il, cr, accu, ca, cs in TIERS:
    name = "Fleshskewer" if il == 350 else f"Fleshskewer (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_shar, "Pilgrim", ["Rogue"], pil_eb)

# Exalted Fleshtearer MH — 4 tiers
for il, cr, accu, ca, cs in TIERS:
    name = "Exalted Fleshtearer" if il == 350 else f"Exalted Fleshtearer (IL {il})"
    add(name, "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_shar, "Pilgrim", ["Rogue"], pil_eb)

# Exalted Fleshskewer OH — IL 350 (start)
add("Exalted Fleshskewer", "Off Hand", 350, {"Accuracy": 131, "Combat Advantage": 262, "Critical Strike": 131}, 315, src_shar, "Pilgrim", ["Rogue"], pil_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
