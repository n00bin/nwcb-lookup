"""Fix Forsaken Mender's Cuisses (id 1496) with verified in-game data."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

for it in data:
    if it["id"] == 1496:
        it["ratingStats"] = {"Critical Strike": 459, "Defense": 919, "Critical Avoidance": 459}
        it["set"] = "Antiquities of Avernus"
        it["setSize"] = 2
        it["source"] = "Avernus Adventure Zone"
        it["equipBonuses"] = [{
            "type": "Equip",
            "scope": "self",
            "name": "Contender's Might",
            "description": "At the start of combat, your Power is increased by 3000 for 10 seconds.",
        }]
        it["notes"] = "Verified in-game 2026-05-17 — n00b confirmed."
        print(f"  Fixed id={it['id']:>5}  {it.get('name')!r}")

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nTotal items: {len(data)}.")
