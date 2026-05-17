"""Fix Forsaken Mender's Coif (id 1494) with verified in-game data."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

for it in data:
    if it["id"] == 1494:
        # Correct the wrong ratings
        it["ratingStats"] = {
            "Critical Strike": 643,
            "Defense": 919,
            "Critical Avoidance": 276,
        }
        it["set"] = "Antiquities of Avernus"
        it["setSize"] = 2
        it["source"] = "Avernus Adventure Zone"
        it["equipBonuses"] = [{
            "type": "Equip",
            "scope": "self",
            "name": "Executioner's Might",
            "description": "When you kill an enemy, your Power increases by 5000 for 10 seconds. 30 second cooldown.",
        }]
        it["notes"] = "Verified in-game 2026-05-17 — n00b confirmed set, source, stats, and Executioner's Might equip power. No 2pc set bonus."
        print(f"  Fixed id={it['id']:>5}  {it.get('name')!r}")
        print(f"    set: {it.get('set')}")
        print(f"    source: {it.get('source')}")
        print(f"    stats: {it.get('ratingStats')}")
        print(f"    equipBonuses[0].name: {it['equipBonuses'][0]['name']}")

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nTotal items: {len(data)}.")
