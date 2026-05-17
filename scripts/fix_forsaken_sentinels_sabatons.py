"""Fix Forsaken Sentinel's Sabatons (id 1497) with verified in-game data."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

for it in data:
    if it["id"] == 1497:
        it["ratingStats"] = {"Combat Advantage": 459, "Defense": 919, "Awareness": 459}
        it["set"] = "Antiquities of Avernus"
        it["setSize"] = 2
        it["source"] = "Avernus Adventure Zone"
        it["equipBonuses"] = [{
            "type": "Equip",
            "scope": "self",
            "name": "Contender's Might",
            "description": "At the start of combat, your Power is increased by 3000 for 10 seconds.",
        }]
        it["notes"] = "Verified in-game 2026-05-17 — n00b confirmed. Shares equip power 'Contender's Might' with Mender's Cuisses (id 1496)."
        print(f"  Fixed id={it['id']:>5}  {it.get('name')!r}")

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nTotal items: {len(data)}.")
