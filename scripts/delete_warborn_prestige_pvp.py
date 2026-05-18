"""Delete 8 confirmed PvP items (Warborn + Prestige Gladiator armor)."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

DELETE_IDS = {
    # Warborn Gladiator (PvP per n00b)
    2038, 2039, 2040, 2041,
    # Prestige Gladiator (PvP per n00b)
    2022, 2023, 2024, 2025,
}
before = len(data)

for it in data:
    if it["id"] in DELETE_IDS:
        print(f"  id={it['id']:>5}  {it.get('slot'):>6}  {it.get('name')!r}")

data = [it for it in data if it["id"] not in DELETE_IDS]
PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nBefore: {before} items; After: {len(data)} items (removed {before-len(data)}).")
