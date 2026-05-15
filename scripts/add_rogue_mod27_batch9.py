"""Rogue gear batch 9 — Rings of the Demonweb Pits (4 rings),
Masterwork of Menzoberranzan Equipment Set (3 amulets + 4 belts)."""
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

cls_all = ["Rogue", "Cleric", "Bard", "Ranger"]

# ---- Rings of the Demonweb Pits (Set 11/19, IL 1700) — rings
src_rdp = "Rings of the Demonweb Pits"
SET_RDP = "Rings of the Demonweb Pits"
add("Darklake Ward Ring",          "Ring", 1700,
    {"Deflection": 3825, "Critical Avoidance": 1275}, 1360, src_rdp, SET_RDP, cls_all,
    [{"name": "Charging Bull",
      "description": "When you have been running for 1 second, you generate threat around you every second as long as you continue running."}])
add("Scintillant Restoration Ring", "Ring", 1700,
    {"Critical Strike": 1275, "Outgoing Healing": 3825}, 1360, src_rdp, SET_RDP, cls_all,
    [{"name": "Survivor's Gift",
      "description": "Your current Hit Points increases your Outgoing Healing, up to a maximum of 6%."}])
add("Shroomwood Raid Ring",        "Ring", 1700,
    {"Combat Advantage": 1275, "Critical Strike": 3825}, 1360, src_rdp, SET_RDP, cls_all,
    [{"name": "Butcher's Precision",
      "description": "When you damage or heal your target for more than 15% of your Maximum Hit Points in a single blow, you gain 1.5% Critical Severity for 10 seconds. (Max stack 5)"}])
add("Scintillant Assault Ring",    "Ring", 1700,
    {"Critical Strike": 1275, "Critical Severity": 3825}, 1360, src_rdp, SET_RDP, cls_all,
    [{"name": "Enduring Critical",
      "description": "Your current Hit Points increases your Critical Strike, up to a maximum of 6%."}])

# ---- Masterwork of Menzoberranzan Equipment Set (Set 0/2, IL 1700) — amulets + belts
SET_MoM = "Masterwork of Menzoberranzan Equipment Set"
mom_eb = [{"type": "Set", "scope": "self", "stat": "Accuracy", "amount": 2.5,
           "setName": SET_MoM, "pieces": 2,
           "description": "2 of Set: When you use an encounter power, gain a stack of Speedy Anointing, granting 2.5% Accuracy and 25% Recharge Speed for 5 seconds. Stacks up to 3 times."}]
src_mw = "Menzoberranzan Masterwork crafting"
add("Goristroskin Soulbead Amulet", "Neck", 1700,
    {"Critical Avoidance": 852, "Deflection": 849, "Deflect Severity": 849}, 1530, src_mw, SET_MoM, cls_all, mom_eb,
    abilities={"CON": 6})
add("Spiked Amulet", "Neck", 1700,
    {"Accuracy": 849, "Combat Advantage": 849, "Critical Strike": 852}, 1530, src_mw, SET_MoM, cls_all, mom_eb,
    abilities={"WIS": 6})
add("Shroomwood Sash", "Belt", 1700,
    {"Combat Advantage": 849, "Critical Strike": 852, "Critical Severity": 849}, 1530, src_mw, SET_MoM, cls_all, mom_eb,
    abilities={"STR": 3, "DEX": 3})
add("Scintillant Sash", "Belt", 1700,
    {"Accuracy": 849, "Combat Advantage": 849, "Critical Strike": 852}, 1530, src_mw, SET_MoM, cls_all, mom_eb,
    abilities={"INT": 3, "CHA": 3})
add("Spiked Sash", "Belt", 1700,
    {"Critical Strike": 1701, "Outgoing Healing": 849}, 1530, src_mw, SET_MoM, cls_all, mom_eb,
    abilities={"DEX": 3, "CHA": 3})
add("Darklake Sash", "Belt", 1700,
    {"Critical Avoidance": 1698, "Deflection": 849}, 1530, src_mw, SET_MoM, cls_all, mom_eb,
    abilities={"CON": 6})

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
