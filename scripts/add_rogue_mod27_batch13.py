"""Rogue gear batch 13 — Devil's Legion (Legion Guard's MH+OH 4 tiers each),
Hellfire Engine Tow Hook MH IL 600."""
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

src_av = "Avernus Adventure Zone"
src_bw = "Blood War Campaign Store"

# Devil's Legion (Module 19 Avernus)
dl_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 1500,
          "setName": "Devil's Legion", "pieces": 2,
          "description": "2 of Set: You and nearby allies are granted: +1500 Power, +1500 Combat Advantage, +1500 Defense, +1500 Critical Avoidance. Stacks up to 5 times when allies are equipped with full Legion Guard's weapons."}]

# Barbed Blade (MH) — IL 800/1000/1200 (IL 600 in batch 12)
add("The Legion Guard's Barbed Blade (IL 800)",  "Main Hand", 800,
    {"Accuracy": 600, "Critical Severity": 600}, 720, src_av, "Devil's Legion", ["Rogue"], dl_eb)
add("The Legion Guard's Barbed Blade (IL 1000)", "Main Hand", 1000,
    {"Accuracy": 750, "Critical Severity": 750}, 900, src_av, "Devil's Legion", ["Rogue"], dl_eb)
add("The Legion Guard's Barbed Blade (IL 1200)", "Main Hand", 1200,
    {"Accuracy": 900, "Critical Severity": 900}, 1080, src_av, "Devil's Legion", ["Rogue"], dl_eb)

# Twisted Blade (OH) — 4 tiers
add("The Legion Guard's Twisted Blade",          "Off Hand", 600,
    {"Combat Advantage": 450, "Critical Strike": 450}, 540, src_av, "Devil's Legion", ["Rogue"], dl_eb)
add("The Legion Guard's Twisted Blade (IL 800)", "Off Hand", 800,
    {"Combat Advantage": 600, "Critical Strike": 600}, 720, src_av, "Devil's Legion", ["Rogue"], dl_eb)
add("The Legion Guard's Twisted Blade (IL 1000)", "Off Hand", 1000,
    {"Combat Advantage": 750, "Critical Strike": 750}, 900, src_av, "Devil's Legion", ["Rogue"], dl_eb)
add("The Legion Guard's Twisted Blade (IL 1200)", "Off Hand", 1200,
    {"Combat Advantage": 900, "Critical Strike": 900}, 1080, src_av, "Devil's Legion", ["Rogue"], dl_eb)

# Hellfire Engine Remains (Set 5/11) — Tow Hook MH IL 600
he_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 1500,
          "setName": "Hellfire Engine Remains", "pieces": 2,
          "description": "2 of Set: Hellfire Engine weapon set — bonus TBD from in-game popup."}]
add("Hellfire Engine Tow Hook", "Main Hand", 600,
    {"Accuracy": 450, "Critical Severity": 450}, 540, src_bw, "Hellfire Engine Remains", ["Rogue"], he_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
