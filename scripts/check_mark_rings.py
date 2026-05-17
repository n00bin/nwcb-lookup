"""Investigate the 12 'Mark of the X' Ring entries (ids 350-361).
Compare to all other 'Mark of the X' items in data to see what slot they
'should' be."""
import json
from collections import defaultdict, Counter
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

# Find all "Mark of" items, grouped by slot
mark_items = [it for it in data if "Mark of the" in it.get("name", "")]
print(f"=== Total 'Mark of the X' items in data: {len(mark_items)} ===\n")

slot_counts = Counter(it.get("slot") for it in mark_items)
print("Slot distribution of all Mark items:")
for slot, c in slot_counts.most_common():
    print(f"  {slot}: {c}")
print()

# The 12 disputed Ring entries
print("=== The 12 disputed RING entries (ids 350-361) ===")
for it in sorted(mark_items, key=lambda x: x["id"]):
    if it.get("slot") == "Ring":
        print(f"  id={it['id']}  {it.get('name')!r}  IL={it.get('item_level')}  CR={it.get('combinedRating')}")
        print(f"    ratings={it.get('ratingStats')}")
print()

# What slot do the SAME Marks live in for Shirt/Pants?
print("=== Same Mark names in Shirt/Pants slots ===")
ring_names = {it.get("name") for it in mark_items if it.get("slot") == "Ring"}
for it in mark_items:
    if it.get("slot") in ("Shirt", "Pants") and it.get("name") in ring_names:
        print(f"  id={it['id']:>5}  {it.get('slot'):>5}  {it.get('name')!r}  IL={it.get('item_level')}")
        print(f"        ratings={it.get('ratingStats')}")
        print(f"        set={it.get('set','')!r}")
print()

# What about Marks WITHOUT the parenthetical (base names)?
print("=== Base Mark names — sample by slot ===")
base_marks = {}  # name without parens -> list of slots
for it in mark_items:
    n = it.get("name", "")
    base = n.split(" (")[0] if " (" in n else n
    base_marks.setdefault(base, []).append((it.get("slot"), it["id"]))

# Show distribution for each base name
for base, items in sorted(base_marks.items()):
    slots = Counter(s for s, _ in items)
    if len(slots) > 1 or "Ring" in slots:
        print(f"  {base!r}:")
        for s, c in slots.most_common():
            ids = [i for sl, i in items if sl == s]
            print(f"    {s}: {c} entries (ids: {ids[:8]}{'...' if len(ids)>8 else ''})")
