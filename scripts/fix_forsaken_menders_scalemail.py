"""Fix Forsaken Mender's Scalemail (id 1498) with verified in-game data."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

for it in data:
    if it["id"] == 1498:
        it["ratingStats"] = {"Defense": 919, "Deflection": 919}
        it["combinedRating"] = 1102
        it["set"] = "Antiquities of Avernus"
        it["setSize"] = 2
        it["source"] = "Avernus Adventure Zone"
        it["equipBonuses"] = [{
            "type": "Equip",
            "scope": "self",
            "name": "Survivor's Remedy",
            "description": "Whenever you deflect an attack you have a 10% chance to restore 5% of your maximum hit points. This effect may only occur once every 5 seconds.",
        }]
        it["notes"] = "Verified in-game 2026-05-17 — n00b confirmed."
        print(f"  Fixed id={it['id']:>5}  {it.get('name')!r}")

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nTotal items: {len(data)}.")
