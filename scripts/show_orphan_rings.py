"""Detailed view of the 99 orphan rings — grouped by IL bucket / family."""
import json
import re
from collections import defaultdict
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

orphan_rings = [it for it in data if not it.get("set") and not it.get("source") and it.get("slot") == "Ring"]
print(f"Total orphan rings: {len(orphan_rings)}\n")

# Group by IL bucket
buckets = defaultdict(list)
for r in orphan_rings:
    il = r.get("item_level") or 0
    if il < 750:
        b = f"IL <750 (early)"
    elif il < 1000:
        b = "IL 750-999"
    elif il < 1500:
        b = "IL 1000-1499"
    elif il < 2000:
        b = "IL 1500-1999"
    elif il < 2500:
        b = "IL 2000-2499"
    else:
        b = "IL 2500+"
    buckets[b].append(r)

order = ["IL <750 (early)", "IL 750-999", "IL 1000-1499", "IL 1500-1999",
         "IL 2000-2499", "IL 2500+"]

for bucket in order:
    items = buckets.get(bucket, [])
    if not items:
        continue
    print(f"=== {bucket} ({len(items)} rings) ===")
    items.sort(key=lambda x: (x.get("item_level") or 0, x.get("name", "")))
    for r in items:
        il = r.get("item_level", "?")
        rs = list((r.get("ratingStats") or {}).keys())
        cls = r.get("allowedClasses") or []
        cls_str = ",".join(cls) if cls else "univ"
        rs_str = "/".join(rs)
        print(f"  id={r['id']:>5}  IL={il!s:>5}  {r.get('name')!r:55}  ratings={rs_str:50}  {cls_str}")
    print()
