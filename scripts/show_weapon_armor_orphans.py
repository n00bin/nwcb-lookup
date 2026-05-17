"""Show all remaining class-restricted weapon/armor orphans organized by class + family."""
import json
from collections import defaultdict
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

orphans = [it for it in data if not it.get("set") and not it.get("source")
           and it.get("slot") in ("Main Hand", "Off Hand", "Head", "Armor", "Arms", "Feet")]
print(f"Total weapon/armor orphans: {len(orphans)}\n")

by_slot = defaultdict(list)
for o in orphans:
    by_slot[o.get("slot", "(none)")].append(o)

for slot in ["Main Hand", "Off Hand", "Head", "Armor", "Arms", "Feet"]:
    items = by_slot.get(slot, [])
    if not items:
        continue
    items.sort(key=lambda x: (x.get("item_level") or 0, x.get("name", "")))
    print(f"=== {slot} ({len(items)}) ===")
    for o in items:
        rs = list((o.get("ratingStats") or {}).keys())
        cls = o.get("allowedClasses") or []
        cls_str = ",".join(cls) if cls else "(none)"
        print(f"  id={o['id']:>5}  IL={o.get('item_level')!s:>5}  {o.get('name')!r:55}  ratings={'/'.join(rs)[:45]:<45}  {cls_str}")
    print()
