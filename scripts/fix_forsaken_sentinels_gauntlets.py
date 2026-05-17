"""Fix Forsaken Sentinel's Gauntlets (id 1501) with verified in-game data."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

for it in data:
    if it["id"] == 1501:
        it["ratingStats"] = {"Accuracy": 459, "Defense": 919, "Deflection": 459}
        it["set"] = "Antiquities of Avernus"
        it["setSize"] = 2
        it["source"] = "Avernus Adventure Zone"
        it["equipBonuses"] = [{
            "type": "Equip",
            "scope": "self",
            "name": "Survivor's Might",
            "description": "Gain 45 Power for each percent of health you are missing.",
        }]
        it["notes"] = "Verified in-game 2026-05-17 — n00b confirmed. Shares equip power 'Survivor's Might' with Mender's Braces (id 1502)."
        print(f"  Fixed id={it['id']:>5}  {it.get('name')!r}")

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nTotal items: {len(data)}.")
