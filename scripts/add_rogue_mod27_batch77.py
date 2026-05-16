"""Rogue gear batch 77 — Elemental Dragonflight Assault 3 pieces, Umbral Assault 3 pieces, Umbral Executioner Mask+Vest."""
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

# Elemental Dragonflight Assault (IL 596) — 3 more pieces
src_ei = "Elemental Infusion"
SET_EDA = "Elemental Dragonflight Assault"
df_eb = [{"type": "Set", "scope": "self", "stat": "Max HP", "amount": 3000,
          "setName": "Dragonflight", "pieces": 2,
          "description": "2 of Set: +3,000 Maximum Hit Points. 3 of Set: +500 Power."}]
add("Elemental Dragonflight Assault Vest",   "Armor", 596,
    {"Accuracy": 268, "Critical Severity": 179, "Defense": 447}, 536, src_ei, SET_EDA, cls_br, df_eb)
add("Elemental Dragonflight Assault Gloves", "Arms",  596,
    {"Critical Strike": 268, "Critical Severity": 179, "Defense": 447}, 536, src_ei, SET_EDA, cls_br, df_eb)
add("Elemental Dragonflight Assault Boots",  "Feet",  596,
    {"Combat Advantage": 268, "Critical Severity": 179, "Defense": 447}, 536, src_ei, SET_EDA, cls_br, df_eb)

# Umbral Assault (Set 14/20, IL 728)
src_mw = "Masterwork Armor (Stronghold)"
SET_UA = "Umbral Assault"
add("Umbral Assault Vest",   "Armor", 728,
    {"Critical Strike": 328, "Critical Severity": 218, "Defense": 546}, 655, src_mw, SET_UA, cls_br,
    [{"name": "Challenger's Might",
      "description": "When in combat with only one enemy, Power +1500."}])
add("Umbral Assault Gloves", "Arms",  728,
    {"Combat Advantage": 328, "Critical Severity": 218, "Defense": 546}, 655, src_mw, SET_UA, cls_br,
    [{"name": "Survivor's Parry",
      "description": "Gain 25 Deflect for each percent of health you are missing."}])
add("Umbral Assault Boots",  "Feet",  728,
    {"Critical Strike": 328, "Critical Severity": 218, "Defense": 546}, 655, src_mw, SET_UA, cls_br,
    [{"name": "Gladiator's Focus",
      "description": "Every 5s in combat, gain 100 Critical Strike. After 2 minutes, ability no longer active."}])

# Umbral Executioner (Set 14/20, IL 728) — Mask + Vest start
SET_UE = "Umbral Executioner"
add("Umbral Executioner Mask", "Head",  728,
    {"Combat Advantage": 164, "Critical Strike": 164, "Critical Severity": 218, "Defense": 546}, 655, src_mw, SET_UE, cls_br,
    [{"name": "Gladiator's Accuracy",
      "description": "Every 5s in combat, gain 100 Accuracy. After 2 minutes, ability no longer active."}])
add("Umbral Executioner Vest", "Armor", 728,
    {"Combat Advantage": 164, "Critical Strike": 218, "Critical Avoidance": 164, "Defense": 546}, 655, src_mw, SET_UE, cls_br,
    [{"name": "Challenger's Might",
      "description": "When in combat with only one enemy, Power +1500."}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
