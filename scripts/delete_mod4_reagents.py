"""Delete the 10 Mod 4 Tyranny of Dragons artifact-weapon refining reagents.
These are NOT equippable gear — they're crafting/refining materials used to
upgrade artifact weapons. IL 435, no ratings, no equipBonuses."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

DELETE_IDS = {1953, 1958, 1963, 1968, 1973, 1978, 1983, 1988, 1995, 2000}
before = len(data)

for it in data:
    if it["id"] in DELETE_IDS:
        print(f"  id={it['id']:>5}  {it.get('slot'):>9}  {it.get('name')!r}")

data = [it for it in data if it["id"] not in DELETE_IDS]
PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nBefore: {before} items; After: {len(data)} items (removed {before-len(data)}).")
