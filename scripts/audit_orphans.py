"""Audit the 259 orphan gear items (no set + no source).

Classify each as:
  A. Has a fully-populated duplicate (same slot+name) — safe to delete (stub)
  B. Has rich data anyway (ratingStats, equipBonuses, item_level) — just needs set/source backfill
  C. Has nothing useful at all (no ratings, no IL, no equipBonuses) — true stub, may need delete
  D. Unique item, partial data — needs in-game verification
"""
import json
from collections import defaultdict, Counter
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

orphans = [it for it in data if not it.get("set") and not it.get("source")]
print(f"Total orphans (no set + no source): {len(orphans)}\n")

# Group all items by (slot, name) for duplicate lookup
groups = defaultdict(list)
for it in data:
    if it.get("name") and it.get("slot"):
        groups[(it["slot"], it["name"])].append(it)

cat_A = []  # has full duplicate
cat_B = []  # has rich data, just needs set/source backfill
cat_C = []  # nothing useful
cat_D = []  # partial data, unique

for orph in orphans:
    key = (orph["slot"], orph["name"])
    siblings = [i for i in groups[key] if i["id"] != orph["id"]]
    full_siblings = [s for s in siblings if s.get("set") or s.get("source")]
    has_ratings = bool(orph.get("ratingStats"))
    has_il = bool(orph.get("item_level"))
    has_equip = bool(orph.get("equipBonuses"))
    rich = has_ratings and has_il
    empty = not (has_ratings or has_il or has_equip)
    if full_siblings:
        cat_A.append((orph, full_siblings))
    elif rich:
        cat_B.append(orph)
    elif empty:
        cat_C.append(orph)
    else:
        cat_D.append(orph)

print(f"A. Has fully-populated duplicate (safe to delete): {len(cat_A)}")
print(f"B. Has rich data, needs set/source backfill:       {len(cat_B)}")
print(f"C. Truly empty stub (nothing to keep):             {len(cat_C)}")
print(f"D. Partial data, no duplicate (needs verification): {len(cat_D)}")
print()

if cat_A:
    print(f"=== Category A: stubs with full duplicates (delete candidates) ===")
    for orph, fulls in cat_A[:25]:
        fids = [f["id"] for f in fulls]
        print(f"  drop id={orph['id']:>5}  {orph.get('slot'):>8}  {orph.get('name')!r:55}  -> keep id(s) {fids}")
    if len(cat_A) > 25:
        print(f"  ... and {len(cat_A)-25} more")
    print()

if cat_C:
    print(f"=== Category C: truly empty stubs (no ratings, no IL, no equip) ===")
    for orph in cat_C[:25]:
        print(f"  id={orph['id']:>5}  {orph.get('slot'):>8}  {orph.get('name')!r:55}  classes={orph.get('allowedClasses')}")
    if len(cat_C) > 25:
        print(f"  ... and {len(cat_C)-25} more")
    print()

if cat_B:
    print(f"=== Category B: rich-data orphans (backfill set/source) — sample ===")
    for orph in cat_B[:15]:
        rs = list((orph.get("ratingStats") or {}).keys())
        print(f"  id={orph['id']:>5}  {orph.get('slot'):>8}  IL={orph.get('item_level'):>4}  {orph.get('name')!r:55}  ratings={rs}")
    if len(cat_B) > 15:
        print(f"  ... and {len(cat_B)-15} more")
    print()

if cat_D:
    print(f"=== Category D: partial-data orphans — sample ===")
    for orph in cat_D[:15]:
        print(f"  id={orph['id']:>5}  {orph.get('slot'):>8}  IL={orph.get('item_level')}  {orph.get('name')!r:55}  has_ratings={bool(orph.get('ratingStats'))}  has_equip={bool(orph.get('equipBonuses'))}")
    if len(cat_D) > 15:
        print(f"  ... and {len(cat_D)-15} more")
