"""Find remaining 'Gladiator' items in data (after Warborn/Prestige/Lionsmane deletions)
to identify the final ambiguous candidates."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

# Already confirmed delete (Warborn + Prestige - not yet deleted but pending)
PENDING_PVP = {2022, 2023, 2024, 2025, 2038, 2039, 2040, 2041}

# Already confirmed PvE (Masterwork crafted)
CONFIRMED_PVE = {
    2479, 2480, 2484, 2485,  # Titansteel
    2596, 2597, 2601, 2602,  # Adamant
    2612, 2616, 2624,         # Electrum/Rosegold/Samite
    2672, 2673, 2674, 2675,   # Company belts
}

# False positives (equip-power name only)
FALSE_POSITIVES = {513, 521, 533}

print("=== Remaining 'Gladiator' items (need classification) ===")
for it in data:
    n = it.get("name", "")
    if "Gladiator" not in n:
        continue
    iid = it["id"]
    if iid in PENDING_PVP or iid in CONFIRMED_PVE or iid in FALSE_POSITIVES:
        continue
    s = it.get("set", "") or ""
    src = it.get("source", "") or ""
    print(f"  id={iid:>5}  IL={it.get('item_level')!s:>5}  {it.get('slot'):>6}  {n!r:50}  set={s!r:25}  src={src[:50]!r}")
