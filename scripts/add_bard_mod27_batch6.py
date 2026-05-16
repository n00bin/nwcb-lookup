"""Bard Mod 27 gear batch 6 — Vistani Lute, Tyrant (Skinstripper/Soulsilencer + Exalted), Primal (Primal Mekatl + Exalted),
Pilgrim (Fleshtaker MH + Exalted), Pioneer (Bard variants)."""
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

TIERS = [(350,315,131,262,131),(500,450,188,375,188),(650,585,244,488,244),(800,720,300,600,300)]
TIERS_EX = [(400,360,150,300,150),(550,495,206,412,206),(700,630,262,525,262),(850,765,319,638,319)]

# Vistani (Ravenloft Mod 14) — Vistani Lute (Bard OH) 4 tiers
src_rv = "Ravenloft (Module 14)"
vis_eb = [{"type": "Set", "scope": "self", "stat": "Defense", "amount": 500,
           "setName": "Vistani", "pieces": 2,
           "description": "2 of Set: +500 Defense, +5% Movement Speed."}]
for il, cr, accu, ca, cs in TIERS:
    name = "Vistani Lute" if il == 350 else f"Vistani Lute (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Critical Strike": cs}, cr, src_rv, "Vistani", ["Bard"], vis_eb)
# Note: At IL 650 image had +488 Accuracy, +488 CritStrike — matches pattern

# Tyrant (Lost City of Omu Mod 13) — Skinstripper (Bard MH) + Soulsilencer (Bard OH) + Exalted variants
src_omu = "Tier 3 Hunt in Omu / Port Nyanzaru (Module 13)"
tyr_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 1,
           "setName": "Tyrant", "pieces": 2,
           "description": "2 of Set: Start of combat: BDB, OOH, Damage Resistance +1%. Every 5s in combat: +1%. Doubled by Trophy Hunter buff. (Max 10%)"}]
# Skinstripper MH 4 tiers
for il, cr, accu, ca, cs in TIERS:
    name = "Skinstripper" if il == 350 else f"Skinstripper (IL {il})"
    add(name, "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_omu, "Tyrant", ["Bard"], tyr_eb)
# Soulsilencer OH 4 tiers
for il, cr, accu, ca, cs in TIERS:
    name = "Soulsilencer" if il == 350 else f"Soulsilencer (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_omu, "Tyrant", ["Bard"], tyr_eb)
# Exalted Skinstripper MH 4 tiers
for il, cr, accu, ca, cs in TIERS:
    name = "Exalted Skinstripper" if il == 350 else f"Exalted Skinstripper (IL {il})"
    add(name, "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_omu, "Tyrant", ["Bard"], tyr_eb)
# Exalted Soulsilencer OH 4 tiers
for il, cr, accu, ca, cs in TIERS:
    name = "Exalted Soulsilencer" if il == 350 else f"Exalted Soulsilencer (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_omu, "Tyrant", ["Bard"], tyr_eb)

# Primal (Sharandar/Chult Mod 11) — Primal Mekatl OH + Exalted Primal Mekatl OH for Bard
src_ch = "Chult Hunts / Sharandar (Module 11)"
prim_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 10,
            "setName": "Primal", "pieces": 2,
            "description": "2 of Set: Primal Recipuyo. If hit/healed for more than 10% of Max HP in a single blow, BDB and OOH +10% for 10s."}]
for il, cr, accu, ca, cs in TIERS:
    name = "Primal Mekatl" if il == 350 else f"Primal Mekatl (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ch, "Primal", ["Bard"], prim_eb)
for il, cr, accu, ca, cs in TIERS:
    name = "Exalted Primal Mekatl" if il == 350 else f"Exalted Primal Mekatl (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_ch, "Primal", ["Bard"], prim_eb)

# Pilgrim (Sharandar) — Fleshtaker MH (Bard) + Exalted Fleshtaker
src_shar = "Sharandar"
pil_eb = [{"type": "Set", "scope": "self", "stat": "Damage Bonus", "amount": 1,
           "setName": "Pilgrim", "pieces": 2,
           "description": "2 of Set: Start of combat: BDB and OOH +1% per enemy faced. If facing only 1 enemy, BDB and OOH +3% for 1 minute."}]
for il, cr, accu, ca, cs in TIERS:
    name = "Fleshtaker" if il == 350 else f"Fleshtaker (IL {il})"
    add(name, "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_shar, "Pilgrim", ["Bard"], pil_eb)
for il, cr, accu, ca, cs in TIERS:
    name = "Exalted Fleshtaker" if il == 350 else f"Exalted Fleshtaker (IL {il})"
    add(name, "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_shar, "Pilgrim", ["Bard"], pil_eb)

# Pioneer Bard — Pioneer Jambiya MH + Pioneer Lute OH + Exalted variants
src_pi = "Other Miscellaneous Sources"
pio_eb = [{"type": "Set", "scope": "self", "stat": "Power", "amount": 200,
           "setName": "Pioneer", "pieces": 2,
           "description": "2 of Set: Increased stat per party member: Party 1 = +200 Power; Party 2-5 progressively adds Defense/Accuracy/CS/CritSev."}]
for il, cr, accu, ca, cs in TIERS:
    name = "Pioneer Jambiya (Bard)" if il == 350 else f"Pioneer Jambiya (Bard, IL {il})"
    add(name, "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_pi, "Pioneer", ["Bard"], pio_eb)
for il, cr, accu, ca, cs in TIERS:
    name = "Pioneer Lute" if il == 350 else f"Pioneer Lute (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_pi, "Pioneer", ["Bard"], pio_eb)
for il, cr, accu, ca, cs in TIERS:
    name = "Exalted Pioneer Jamibya" if il == 350 else f"Exalted Pioneer Jamibya (IL {il})"
    add(name, "Main Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_pi, "Pioneer", ["Bard"], pio_eb)
for il, cr, accu, ca, cs in TIERS:
    name = "Exalted Pioneer Lute" if il == 350 else f"Exalted Pioneer Lute (IL {il})"
    add(name, "Off Hand", il, {"Accuracy": accu, "Combat Advantage": ca, "Critical Strike": cs}, cr, src_pi, "Pioneer", ["Bard"], pio_eb)

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Added items. Max id now: {max_id}, Total items: {len(data)}")
