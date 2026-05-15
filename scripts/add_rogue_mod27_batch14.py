"""Rogue gear batch 14 — Hellfire Engine MH IL 800/1000/1200, OH all 4 tiers,
Divine Armor (Redeemed Citadel 4-pc), Lion Guard Armor (Vallenhas 4-pc start)."""
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

src_bw = "Blood War Campaign Store"
src_rc = "The Redeemed Citadel"
src_vh = "Vallenhas Campaign Rewards / Infernal Citadel"

# ---- Hellfire Engine Remains — Tow Hook (MH) 3 more tiers, Oil Stick (OH) 4 tiers
he_eb = [{"type": "Set", "scope": "self", "stat": "Stamina Regeneration", "amount": 15,
          "setName": "Hellfire Engine Remains", "pieces": 2,
          "description": "2 of Set: At the start of combat, your Stamina Regeneration is increased by 15%, and your Movement Speed is increased by 15% for 10s. When you kill an enemy, this buff will refresh. When you leave combat, this buff will expire."}]
add("Hellfire Engine Tow Hook (IL 800)",  "Main Hand", 800,
    {"Accuracy": 600, "Critical Severity": 600}, 720, src_bw, "Hellfire Engine Remains", ["Rogue"], he_eb, set_size=2)
add("Hellfire Engine Tow Hook (IL 1000)", "Main Hand", 1000,
    {"Accuracy": 750, "Critical Severity": 750}, 900, src_bw, "Hellfire Engine Remains", ["Rogue"], he_eb, set_size=2)
add("Hellfire Engine Tow Hook (IL 1200)", "Main Hand", 1200,
    {"Accuracy": 900, "Critical Severity": 900}, 1080, src_bw, "Hellfire Engine Remains", ["Rogue"], he_eb, set_size=2)

add("Hellfire Engine Oil Stick",          "Off Hand", 600,
    {"Combat Advantage": 450, "Critical Strike": 450}, 540, src_bw, "Hellfire Engine Remains", ["Rogue"], he_eb, set_size=2)
add("Hellfire Engine Oil Stick (IL 800)", "Off Hand", 800,
    {"Combat Advantage": 600, "Critical Strike": 600}, 720, src_bw, "Hellfire Engine Remains", ["Rogue"], he_eb, set_size=2)
add("Hellfire Engine Oil Stick (IL 1000)", "Off Hand", 1000,
    {"Combat Advantage": 750, "Critical Strike": 750}, 900, src_bw, "Hellfire Engine Remains", ["Rogue"], he_eb, set_size=2)
add("Hellfire Engine Oil Stick (IL 1200)", "Off Hand", 1200,
    {"Combat Advantage": 900, "Critical Strike": 900}, 1080, src_bw, "Hellfire Engine Remains", ["Rogue"], he_eb, set_size=2)

# ---- Divine Armor (Set 6/11, IL 1230) — Bard/Rogue/Ranger
SET_DA = "Divine Armor"
cls_brr = ["Bard", "Rogue", "Ranger"]
add("Divine Raid Helm",    "Head",  1230,
    {"Combat Advantage": 369, "Critical Strike": 554, "Defense": 922}, 1107, src_rc, SET_DA, cls_brr,
    [{"name": "Charged Might",
      "description": "When your Stamina is over 75%, your Power is increased by 5000."}])
add("Divine Raid Surcoat", "Armor", 1230,
    {"Critical Severity": 922, "Defense": 922}, 1107, src_rc, SET_DA, cls_brr,
    [{"name": "Critical Remedy",
      "description": "Whenever you Critically Strike with your Powers, you have a 10% chance to restore 5% of your Maximum Hit Points. (5s CD)"}])
add("Divine Raid Braces",  "Arms",  1230,
    {"Accuracy": 369, "Critical Severity": 554, "Defense": 922}, 1107, src_rc, SET_DA, cls_brr,
    [{"name": "Escalating Might",
      "description": "Gain 250 Power for 10 seconds when you strike an enemy, lose a stack when you are struck. Max 20 Stacks: 5000 Power."}])
add("Divine Raid Cuisses", "Feet",  1230,
    {"Combat Advantage": 369, "Critical Strike": 554, "Defense": 922}, 1107, src_rc, SET_DA, cls_brr,
    [{"name": "Death Defier's Might",
      "description": "Gain 300 Power for each enemy you are engaged in battle. (Max of 15 targets)"}])

# ---- Lion Guard Armor (Set 7/11, IL 1250) — Bard/Rogue/Ranger
SET_LG = "Lion Guard Armor"
add("Lion Guard's Raid Hat",       "Head",  1250,
    {"Combat Advantage": 375, "Critical Strike": 562, "Defense": 938}, 1125, src_vh, SET_LG, cls_brr,
    [{"name": "Charged Might",
      "description": "When your Stamina is over 75%, your Power is increased by 5000."}])
add("Lion Guard's Raid Leathers",  "Armor", 1250,
    {"Critical Severity": 938, "Defense": 938}, 1125, src_vh, SET_LG, cls_brr,
    [{"name": "Critical Remedy",
      "description": "Whenever you Critically Strike with your Powers, you have a 10% chance to restore 5% of your Maximum Hit Points. (5s CD)"}])
add("Lion Guard's Raid Gloves",    "Arms",  1250,
    {"Accuracy": 375, "Critical Strike": 562, "Defense": 938}, 1125, src_vh, SET_LG, cls_brr,
    [{"name": "Escalating Might",
      "description": "Gain 250 Power for 10 seconds when you strike an enemy, lose a stack when struck. Max 20 Stacks: 5000 Power."}])
add("Lion Guard's Raid Boots",     "Feet",  1250,
    {"Combat Advantage": 375, "Critical Strike": 562, "Defense": 938}, 1125, src_vh, SET_LG, cls_brr,
    [{"name": "Death Defier's Might",
      "description": "Gain 300 Power for each enemy you are engaged in battle. (Max of 15 targets)"}])

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
