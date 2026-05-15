"""Rogue gear batch 3 — Doomed Reaver Arms/Head, Dread March Arms/Head, Crystal/Bloodbrass weapons.
Also corrects Bismuth Dagger stats (batch 2 had wrong rating stats)."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Mod 27 Rogue gear — screenshot intake 2026-05-15."

def add(name, slot, il, rs, cr, source, set_name, classes, equip=None, percent=None, set_size=2, abilities=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": percent or {}, "abilityBonuses": abilities or {},
        "allowedClasses": classes, "notes": INTAKE}
    data.append(entry)

# ---- Doomed Reaver Armor (Set 4/21, IL 5000) — additional pieces (Cuirass + Greaves already in batch 2)
src_dr = "Soul Harvest (Master) (Module 27)"
dra_classes = ["Rogue", "Cleric", "Bard", "Ranger"]
add("Helm of the Scarlet Arcanum",      "Head", 5000,
    {"Accuracy": 3218, "Combat Advantage": 1980, "Forte": 2228}, 4500, src_dr,
    "Doomed Reaver Armor", dra_classes,
    [{"name": "Steady Precision",
      "description": "Every 8 seconds you are in combat, gain +1% Accuracy and +0.3% Recharge Speed. Max 7 Stacks: +7% Accuracy and +2.1% Recharge Speed."}],
    None, 4)
add("Gauntlets of the Scarlet Arcanum", "Arms", 5000,
    {"Combat Advantage": 3300, "Critical Severity": 4050}, 4500, src_dr,
    "Doomed Reaver Armor", dra_classes,
    [{"name": "Devastating Precision",
      "description": "When you damage your target for more than 20% of your Maximum Hit Points in a single blow, your enemy suffers +4% Critical Severity, while you gain +8% Critical Severity for 8 seconds (10 second cooldown)."}],
    None, 4)

# ---- Dread March Armor (Set 5/21, IL 4700) — additional pieces (Hauberk + Greaves already in batch 2)
src_dm = "Soul Harvest (Advanced) (Module 27)"
add("Diadem of the Crimson Gale",   "Head", 4700,
    {"Combat Advantage": 3102, "Forte": 2855}, 4230, src_dm,
    "Dread March Armor", dra_classes,
    [{"name": "Advantageous Strike",
      "description": "Whenever you deal Combat Advantage damage with your Powers, gain +3% Combat Advantage and +2.5% Power for 8 seconds. (10 second cooldown)"}],
    None, 4)
add("Vambraces of the Crimson Gale", "Arms", 4700,
    {"Critical Strike": 3807, "Forte": 3490}, 4230, src_dm,
    "Dread March Armor", dra_classes,
    [{"name": "Precision Against Odds",
      "description": "Each enemy you are in combat with increases your Critical Strike by 1.8%. Max 5 targets: 9% Critical Strike."}],
    None, 4)

# ---- Crystalline Weapons (Prismatic Defier of Dread) — additional Off-Hands
prismatic_eb = [{"type": "Set", "scope": "self", "stat": "Movement Speed", "amount": 12,
                 "setName": "Prismatic Defier of Dread", "pieces": 2,
                 "description": "2 of Set: While in the Pirates' Skyhold or Dread Sanctum, your Movement Speed is increased by 12%. Every 3s in combat, gain a stack of Prismatic Force. Each stack: General +0.35% Power, DPS +0.5% Critical Severity, Healer +0.4% Overall Outgoing Healing, Tank +0.4% Awareness. Max 10 stacks."}]
add("Crystal Dirk", "Off Hand", 3100,
    {"Accuracy": 3022, "Forte": 2790}, 2790,
    "Pirates' Skyhold / Dread Sanctum", "Prismatic Defier of Dread", ["Rogue"],
    prismatic_eb, {"Damage Bonus": 1.0})

# ---- Bloodbrass Weapons (Skyhold Arms, IL 2750)
skyhold_eb = [{"type": "Set", "scope": "self", "stat": "Movement Speed", "amount": 12,
               "setName": "Skyhold Arms", "pieces": 2,
               "description": "2 of Set: While in the Pirates' Skyhold, your Movement Speed is increased by 12%. Every 3s in combat, gain a stack of Freebooter's Will. Each stack: General +0.20% Power, DPS +0.35% Critical Severity, Healer +0.3% Overall Outgoing Healing, Tank +0.3% Awareness. Max 10 stacks."}]
add("Bloodbrass Dagger", "Main Hand", 2750,
    {"Critical Strike": 2475, "Critical Severity": 2475}, 2475,
    "Pirates' Skyhold Campaign Store", "Skyhold Arms", ["Rogue"], skyhold_eb)
add("Bloodbrass Dirk",   "Off Hand",  2750,
    {"Accuracy": 2681, "Forte": 1856}, 2475,
    "Pirates' Skyhold Campaign Store", "Skyhold Arms", ["Rogue"], skyhold_eb)

# ---- Corrections: fix Bismuth Dagger rating stats from batch 2 (had wrong Accuracy/Forte)
for it in data:
    if it.get("name") == "Bismuth Dagger" and it.get("item_level") == 3400 and it.get("slot") == "Main Hand":
        it["ratingStats"] = {"Critical Strike": 3060, "Critical Severity": 3060, "Combat Advantage": 3060}
        it["notes"] = INTAKE + " (corrected: batch 2 stats were wrong)"

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
