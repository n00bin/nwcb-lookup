"""Rogue gear batch 34 — Pilgrim Raid + Pilgrim Assault 4-pc (IL 644), League's Raid start (IL 588)."""
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
src_tb = "Trade Bar Merchant / Zen Market"

# ---- Pilgrim Raid (IL 644) — remaining pieces
SET_PILR = "Pilgrim Raid"
add("Pilgrim Raid Qafaz",   "Arms",  644,
    {"Combat Advantage": 193, "Critical Strike": 290, "Defense": 483}, 580, src_tb, SET_PILR, cls_br,
    [{"name": "Death Defier's Might",
      "description": "Gain 100 Power for each enemy engaged in battle. (Max 15)"}])
add("Pilgrim Raid Khaftan", "Armor", 644,
    {"Accuracy": 290, "Combat Advantage": 193, "Defense": 483}, 580, src_tb, SET_PILR, cls_br,
    [{"name": "Death Defier's Guard",
      "description": "Gain 100 Defense for each enemy engaged in battle. (Max 15)"}])
add("Pilgrim Raid Soqs",    "Feet",  644,
    {"Accuracy": 290, "Combat Advantage": 193, "Defense": 483}, 580, src_tb, SET_PILR, cls_br,
    [{"name": "Wanderer's Vigor",
      "description": "When not in a party, regenerate 3% of Max HP (up to 3000) every 3s."}])

# ---- Pilgrim Assault (IL 644) — 4 pieces
SET_PILA = "Pilgrim Assault"
add("Pilgrim Assault Keffiyeh", "Head",  644,
    {"Accuracy": 290, "Critical Severity": 193, "Defense": 483}, 580, src_tb, SET_PILA, cls_br,
    [{"name": "Chultan Hunter",
      "description": "+1% Damage in all of Chult."}])
add("Pilgrim Assault Khaftan",  "Armor", 644,
    {"Critical Strike": 290, "Critical Severity": 193, "Defense": 483}, 580, src_tb, SET_PILA, cls_br,
    [{"name": "Death Defier's Guard",
      "description": "Gain 100 Defense for each enemy in battle. (Max 15)"}])
add("Pilgrim Assault Qafaz",    "Arms",  644,
    {"Critical Strike": 290, "Critical Severity": 193, "Defense": 483}, 580, src_tb, SET_PILA, cls_br,
    [{"name": "Death Defier's Might",
      "description": "Gain 100 Power for each enemy in battle. (Max 15)"}])
add("Pilgrim Assault Soqs",     "Feet",  644,
    {"Combat Advantage": 290, "Critical Severity": 193, "Defense": 483}, 580, src_tb, SET_PILA, cls_br,
    [{"name": "Wanderer's Vigor",
      "description": "When not in a party, regenerate 3% of Max HP (up to 3000) every 3s."}])

# ---- League's Raid (Port Nyanzaru, IL 588)
src_pn = "Port Nyanzaru — Chultan Riches Vendor / Chultan Bazaar Vendor"
SET_LR = "League's Raid"
add("League's Raid Keffiyeh", "Head", 588,
    {"Combat Advantage": 176, "Critical Strike": 265, "Defense": 441}, 529, src_pn, SET_LR, cls_br,
    [{"name": "Warden's Defense",
      "description": "When damaged for more than 15% of Max HP in a single blow, gain 5% Defense for 10s."}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
