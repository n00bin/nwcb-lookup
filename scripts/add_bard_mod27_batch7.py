"""Bard Mod 27 gear batch 7 — Chultan (Wootz Jambiya shared with Rogue + new Wootz Lute OH for Bard),
plus a few more Bard weapon set variants."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
max_id = max((i.get('id', 0) for i in data), default=0)
INTAKE = "Mod 27 Bard gear — screenshot intake 2026-05-16."

def add(name, slot, il, rs, cr, source, set_name, classes, equip=None, percent=None, set_size=2, abilities=None):
    global max_id
    max_id += 1
    entry = {"id": max_id, "name": name, "slot": slot, "item_level": il,
        "ratingStats": rs, "combinedRating": cr,
        "equipBonuses": equip or [], "set": set_name or "", "setSize": set_size if set_name else 0,
        "source": source, "percentStats": percent or {}, "abilityBonuses": abilities or {},
        "allowedClasses": classes, "notes": INTAKE}
    data.append(entry)

# Update existing Wootz Jambiya entries to also allow Bard
for it in data:
    if it.get("name", "").startswith("Wootz Jambiya"):
        cls = it.get("allowedClasses", [])
        if "Bard" not in cls:
            cls.append("Bard")
            it["allowedClasses"] = cls

# Add Wootz Lute (Bard OH) at 4 tiers — Chultan set
src_chc = "Professions / Tomb of Annihilation (Module 12)"
ch_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 2000,
          "setName": "Chultan", "pieces": 2,
          "description": "2 of Set: Commander's Surprise. At the start of combat, a random stat is increased by 2000 for 10 seconds."}]
TIERS = [(350,315,131,262,131),(500,450,188,375,188),(650,585,244,488,244),(800,720,300,600,300)]
for il, cr, accu, ca, cs in TIERS:
    name = "Wootz Lute" if il == 350 else f"Wootz Lute (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_chc, "Chultan", ["Bard"], ch_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
