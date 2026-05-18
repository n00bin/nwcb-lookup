"""Show all Belt/Neck orphan items grouped by family."""
import json
from collections import defaultdict
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

orphans = [it for it in data
           if not it.get("set") and not it.get("source")
           and it.get("slot") in ("Belt", "Neck")]

print(f"Total Belt/Neck orphans: {len(orphans)}\n")

by_slot = defaultdict(list)
for o in orphans:
    by_slot[o.get("slot")].append(o)

for slot in ["Belt", "Neck"]:
    items = by_slot.get(slot, [])
    if not items:
        continue
    items.sort(key=lambda x: (x.get("item_level") or 0, x.get("name", "")))
    print(f"=== {slot} ({len(items)}) ===")
    for o in items:
        rs = list((o.get("ratingStats") or {}).keys())
        print(f"  id={o['id']:>5}  IL={o.get('item_level')!s:>4}  {o.get('name')!r:55}  ratings={'/'.join(rs)}")
    print()
