"""Compact summary: orphans grouped by slot, with IL range and class breakdown."""
import json
from collections import defaultdict, Counter
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
orphans = [it for it in data if not it.get("set") and not it.get("source")]
by_slot = defaultdict(list)
for o in orphans:
    by_slot[o.get("slot", "(none)")].append(o)

slot_order = ["Main Hand", "Off Hand", "Head", "Armor", "Arms", "Feet",
              "Shirt", "Pants", "Belt", "Neck", "Ring"]

print(f"=== Orphan summary by slot ===\n")
print(f"{'Slot':<12} {'Count':>6}  {'IL range':<14}  Class breakdown")
print(f"{'-'*12} {'-'*6}  {'-'*14}  {'-'*40}")
for slot in slot_order:
    items = by_slot.get(slot, [])
    if not items:
        continue
    ils = [i.get("item_level") or 0 for i in items]
    il_range = f"{min(ils)}-{max(ils)}"
    cls_counter = Counter()
    for i in items:
        cs = i.get("allowedClasses") or []
        if not cs:
            cls_counter["(none)"] += 1
        else:
            for c in cs:
                cls_counter[c] += 1
    cls_str = ", ".join(f"{c}:{n}" for c, n in cls_counter.most_common(4))
    print(f"{slot:<12} {len(items):>6}  {il_range:<14}  {cls_str}")
