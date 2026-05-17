"""Show the 259 orphans organized for review — broken out by slot, then by IL bucket."""
import json
from collections import defaultdict, Counter
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

orphans = [it for it in data if not it.get("set") and not it.get("source")]

# Slot breakdown
by_slot = defaultdict(list)
for o in orphans:
    by_slot[o.get("slot", "(none)")].append(o)

print(f"=== 259 ORPHANS BY SLOT ===\n")
slot_order = ["Main Hand", "Off Hand", "Head", "Armor", "Arms", "Feet",
              "Shirt", "Pants", "Belt", "Neck", "Ring"]
for slot in slot_order:
    items = by_slot.get(slot, [])
    if not items:
        continue
    print(f"--- {slot} ({len(items)} orphans) ---")
    # Sort by IL ascending
    items.sort(key=lambda x: (x.get("item_level") or 0, x.get("id", 0)))
    for o in items:
        il = o.get("item_level", "?")
        rs = list((o.get("ratingStats") or {}).keys())
        cls = o.get("allowedClasses") or "[]"
        cls_str = ",".join(cls) if isinstance(cls, list) and cls else "(none)"
        rs_str = "/".join(rs)
        print(f"  id={o['id']:>5}  IL={il!s:>5}  {o.get('name')!r:55}  ratings={rs_str:55}  classes={cls_str}")
    print()
