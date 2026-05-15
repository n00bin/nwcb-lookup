"""Rogue gear batch 4 — Prismatic Crystalline Armor (3700), Crystalline Armor (3350),
Enchanted Depths Armor (3200), Depths Armor (3000), Living Magma weapons (2700), Dark Matter weapons (2500)."""
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

cls_all = ["Rogue", "Cleric", "Bard", "Ranger"]

# ---- Prismatic Crystalline Armor (Set 3/11, IL 3700) — Dread Sanctum (Master)
src_pca = "Dread Sanctum (Master)"
SET_PCA = "Prismatic Crystalline Armor"
add("Prismatic Bismuth Mail", "Armor", 3700,
    {"Critical Strike": 3530, "Critical Severity": 3530}, 3330, src_pca, SET_PCA, cls_all,
    [{"name": "Tactical Daily (Greater)",
      "description": "When you deal damage with a Daily power, your next encounter power will deal 20% more damage. (30 second cooldown). You gain 5% Combat Advantage."}])
add("Prismatic Crystalflex Bracers", "Arms", 3700,
    {"Combat Advantage": 2220, "Critical Severity": 3530}, 3330, src_pca, SET_PCA, cls_all,
    [{"name": "Enveloped Rage (Greater)",
      "description": "When in combat with 3 or more enemies, your Critical Severity is increased 1.8% every 2 seconds. Every 2 seconds you are in combat with 1 or fewer enemies, lose 1 stack. Max 5 stacks: 9% Critical Severity."}])
add("Prismatic Luminstep Greaves", "Feet", 3700,
    {"Critical Strike": 3530, "Forte": 2498}, 3330, src_pca, SET_PCA, cls_all,
    [{"name": "Discharged Precision (Lesser)",
      "description": "When Action Points are less than 80%, your Accuracy is increased. +5% while outside of the Pirates' Skyhold or Dread Sanctum. +10% while inside."}])
add("Prismatic Fractal Barbut", "Head", 3700,
    {"Accuracy": 1804, "Combat Advantage": 2220, "Forte": 1249}, 3330, src_pca, SET_PCA, cls_all,
    [{"name": "Critical Spiker (Greater)",
      "description": "For every 5 seconds you are in combat, you gain 1.8% Critical Strike. Max Stacks: 5."}])

# ---- Crystalline Armor (Set 4/11, IL 3350) — Dread Sanctum (Advanced)
src_ca = "Dread Sanctum (Advanced)"
SET_CA = "Crystalline Armor"
add("Bismuth Mail", "Armor", 3350,
    {"Combat Advantage": 2010, "Critical Severity": 3015}, 3015, src_ca, SET_CA, cls_all,
    [{"name": "Tactical Daily (Greater)",
      "description": "When you deal damage with a Daily power, your next encounter power will deal 20% more damage. (30 second cooldown). You gain 5% Combat Advantage."}])
add("Crystalflex Bracers", "Arms", 3350,
    {"Critical Strike": 3015, "Critical Severity": 3015}, 3015, src_ca, SET_CA, cls_all,
    [{"name": "Enveloped Rage (Greater)",
      "description": "When in combat with 3 or more enemies, your Critical Severity is increased 1.8% every 2 seconds. Max 5 stacks: 9% Critical Severity."}])
add("Luminstep Greaves", "Feet", 3350,
    {"Accuracy": 1633, "Combat Advantage": 2010, "Forte": 1131}, 3015, src_ca, SET_CA, cls_all,
    [{"name": "Discharged Precision (Lesser)",
      "description": "When Action Points are less than 80%, your Accuracy is increased. +5% outside of / +10% inside the Pirates' Skyhold or Dread Sanctum."}])
add("Fractal Barbut", "Head", 3350,
    {"Critical Strike": 3015, "Forte": 3265}, 3015, src_ca, SET_CA, cls_all,
    [{"name": "Critical Spiker (Greater)",
      "description": "For every 5 seconds you are in combat, you gain 1.8% Critical Strike. Max Stacks: 5."}])

# ---- Enchanted Depths Armor (Set 2/11, IL 3200) — Lair of the Mad Dragon (Master)
src_eda = "Lair of the Mad Dragon (Master)"
SET_EDA = "Enchanted Depths Armor"
add("Enchanted Depthcured Hat", "Head", 3200,
    {"Critical Strike": 2400, "Forte": 2400}, 2880, src_eda, SET_EDA, cls_all,
    [{"name": "Combatant's Advantage",
      "description": "For every 5 seconds you are in combat, you gain 1% Combat Advantage. Max Stacks: 10."}])
add("Enchanted Depthcured Boots", "Feet", 3200,
    {"Combat Advantage": 2400, "Critical Severity": 2400}, 2880, src_eda, SET_EDA, cls_all,
    [{"name": "Fiery Predator",
      "description": "+4% Damage on fire-themed maps. +1% Damage on other maps."}])
add("Enchanted Depthcured Vest", "Armor", 3200,
    {"Accuracy": 1200, "Combat Advantage": 2400, "Forte": 1200}, 2880, src_eda, SET_EDA, cls_all,
    [{"name": "Ruthless Advantage",
      "description": "When you damage or heal your target for more than 10% of your Maximum Hit Points in a single blow, you gain 1.5% Accuracy and Combat Advantage for 15 seconds. (Max stack 5)"}])
add("Enchanted Depthcured Wristguards", "Arms", 3200,
    {"Critical Strike": 2400, "Critical Severity": 2400}, 2880, src_eda, SET_EDA, cls_all,
    [{"name": "Enveloped Precision",
      "description": "When in combat with 3 or more enemies, your Critical Strike is increased 1.5% every 2 seconds. Max 5 Stacks: 7.5% Critical Strike."}])

# ---- Depths Armor (Set 3/11, IL 3000) — Lair of the Mad Dragon (Advanced)
src_da = "Lair of the Mad Dragon (Advanced)"
SET_DA = "Depths Armor"
add("Depthcured Cap", "Head", 3000,
    {"Critical Strike": 2250, "Forte": 2250}, 2700, src_da, SET_DA, cls_all,
    [{"name": "Combatant's Advantage",
      "description": "For every 5 seconds you are in combat, you gain 0.8% Combat Advantage. Max 10 Stacks: 8% Combat Advantage."}])
add("Depthcured Boots", "Feet", 3000,
    {"Combat Advantage": 2250, "Critical Severity": 2250}, 2700, src_da, SET_DA, cls_all,
    [{"name": "Fiery Predator",
      "description": "+3.5% Damage on fire-themed maps. +1% Damage on other maps."}])
add("Depthcured Jerkin", "Armor", 3000,
    {"Accuracy": 1125, "Combat Advantage": 2250, "Forte": 1125}, 2700, src_da, SET_DA, cls_all,
    [{"name": "Ruthless Might",
      "description": "When you damage or heal your target for more than 10% of your Maximum Hit Points in a single blow, you gain 1.5% Critical Strike and Critical Severity for 15 seconds. Max 5 Stacks: 7.5% CS/CritSev."}])
add("Depthcured Armband", "Arms", 3000,
    {"Critical Strike": 2250, "Critical Severity": 2250}, 2700, src_da, SET_DA, cls_all,
    [{"name": "Enveloped Precision",
      "description": "When in combat with 3 or more enemies, your Critical Strike is increased 1.3% every 2 seconds. Max 5 Stacks: 6.5% Critical Strike."}])

# ---- Living Magma Weapons (Set 1/11, IL 2700) — Mount Hotenow / Mountain of Flame
src_lm = "Mountain of Flame Campaign Store"
SET_LM = "Living Magma"
lm_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 7.5,
          "setName": "Living Magma", "pieces": 2,
          "description": "2 of Set: Gain 7.5% Power while at full health. Decreases relative to missing health. Role bonus: DPS +2.5% Combat Advantage, Tank +2.5% Defense, Healer +2.5% Outgoing Healing. Does not stack. On fire-themed maps, role bonus is doubled and Movement Speed is increased 10%."}]
add("Encased Magma Khanjar", "Main Hand", 2700,
    {"Critical Strike": 1012, "Defense": 1012, "Forte": 2025}, 2430, src_lm, SET_LM, ["Rogue"], lm_eb, {"Damage Bonus": 87.5/100})
add("Encased Magma Jambiya", "Off Hand",  2700,
    {"Accuracy": 1012, "Combat Advantage": 2025, "Forte": 1012}, 2430, src_lm, SET_LM, ["Rogue"], lm_eb, {"Damage Bonus": 87.5/100})

# ---- Dark Matter Weapons (Set 1/17, IL 2500) — Wildspace / Defense of the Moondancer (Advanced)
src_dm = "Defense of the Moondancer (Advanced)"
SET_DM = "Dark Matter"
dm_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 5.5,
          "setName": "Dark Matter", "pieces": 2,
          "description": "2 of Set: Deal or heal up to 5.5% additional damage based on the difference in HP between you and your target. Role bonus: DPS +1% Base Damage Boost, Tank +5% Incoming Damage, Healer +6% Overall Outgoing Healing. Does not stack. When in Wildspace, role bonus is doubled and Movement Speed is increased 10%."}]
add("Starcore Stiletto", "Off Hand", 2500,
    {"Combat Advantage": 1875, "Forte": 1875}, 2250, src_dm, SET_DM, ["Rogue"], dm_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
