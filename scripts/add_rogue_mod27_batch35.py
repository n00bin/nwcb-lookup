"""Rogue gear batch 35 — League's Raid 3 more, League's Assault 4-pc, League's Elite Raid Keffiyeh."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Rogue gear — screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes, equip=None, percent=None, set_size=4, abilities=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": percent or {}, "abilityBonuses": abilities or {},
        "allowedClasses": classes, "notes": INTAKE}
    data.append(entry)

cls_br = ["Bard", "Rogue"]
src_pn = "Port Nyanzaru — Chultan Riches/Bazaar Vendor"

# League's Raid (IL 588) — remaining 3 pieces
SET_LR = "League's Raid"
add("League's Raid Khaftan", "Armor", 588,
    {"Accuracy": 265, "Combat Advantage": 176, "Defense": 441}, 529, src_pn, SET_LR, cls_br,
    [{"name": "Survivor's Guard",
      "description": "Gain 10 Defense for each percent of health you are missing."}])
add("League's Raid Qafaz",   "Arms",  588,
    {"Combat Advantage": 176, "Critical Strike": 265, "Defense": 441}, 529, src_pn, SET_LR, cls_br,
    [{"name": "Survivor's Might",
      "description": "Gain 10 Power for each percent of health you are missing."}])
add("League's Raid Soqs",    "Feet",  588,
    {"Accuracy": 265, "Combat Advantage": 176, "Defense": 441}, 529, src_pn, SET_LR, cls_br,
    [{"name": "Warden's Haste",
      "description": "When damaged for more than 15% of Max HP in a single blow, Movement Speed +5% for 10s."}])

# League's Assault (IL 588) — 4 pieces
src_pn_pro = "Professions / Port Nyanzaru"
SET_LA = "League's Assault"
add("League's Assault Keffiyeh", "Head",  588,
    {"Accuracy": 265, "Critical Severity": 176, "Defense": 441}, 529, src_pn_pro, SET_LA, cls_br,
    [{"name": "Warden's Defense",
      "description": "When damaged for more than 15% of Max HP in a single blow, gain 5% Defense for 10s."}])
add("League's Assault Khaftan",  "Armor", 588,
    {"Critical Strike": 265, "Critical Severity": 176, "Defense": 441}, 529, src_pn_pro, SET_LA, cls_br,
    [{"name": "Survivor's Guard",
      "description": "Gain 10 Defense for each percent of health missing."}])
add("League's Assault Qafaz",    "Arms",  588,
    {"Critical Strike": 265, "Critical Severity": 176, "Defense": 441}, 529, src_pn_pro, SET_LA, cls_br,
    [{"name": "Survivor's Might",
      "description": "Gain 10 Power for each percent of health missing."}])
add("League's Assault Soqs",     "Feet",  588,
    {"Combat Advantage": 265, "Critical Severity": 176, "Defense": 441}, 529, src_pn_pro, SET_LA, cls_br,
    [{"name": "Warden's Haste",
      "description": "When damaged for more than 15% of Max HP, Movement Speed +5% for 10s."}])

# League's Elite Raid Keffiyeh (Head, IL 602)
SET_LER = "League's Elite Raid"
add("League's Elite Raid Keffiyeh", "Head", 602,
    {"Combat Advantage": 361, "Critical Strike": 542, "Defense": 452}, 1355, "Professions", SET_LER, cls_br,
    [{"name": "Warden's Defense",
      "description": "When damaged for more than 10% of Max HP in a single blow, gain 5% Defense for 10s."}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
