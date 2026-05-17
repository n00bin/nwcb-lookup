"""Classify the remaining (slot, name) duplicates where ALL entries are fully populated.

A pair is 'legit' if the entries genuinely differ on substantive fields (IL, ratings,
set, source). A pair is a 'true duplicate' if the entries are functionally identical
(same IL, same ratingStats, same CR, same set, similar source).
"""
import json
from collections import defaultdict
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

groups = defaultdict(list)
for it in data:
    if it.get("name") and it.get("slot"):
        groups[(it["slot"], it["name"])].append(it)

legit_diff_il = []           # different IL -> different tier
legit_diff_set = []          # different set name -> different bonus
legit_diff_source = []       # same IL/set/CR but different source (multi-source same item)
legit_diff_classes = []      # different allowedClasses
legit_diff_stats = []        # same IL but different ratingStats (likely role variant)
true_dups = []               # functionally identical -> deletion candidates
unclassified = []

def sig(it):
    return (
        it.get("item_level"),
        tuple(sorted((it.get("ratingStats") or {}).items())),
        it.get("combinedRating"),
        it.get("set", ""),
        tuple(sorted(it.get("allowedClasses") or [])),
    )

for (slot, name), items in groups.items():
    if len(items) < 2:
        continue
    if any(not (i.get("set") or i.get("source")) for i in items):
        continue  # already-handled stub case (shouldn't be any left)
    ils = {i.get("item_level") for i in items}
    sets = {i.get("set", "") for i in items}
    classes = {tuple(sorted(i.get("allowedClasses") or [])) for i in items}
    sigs = {sig(i) for i in items}
    rstats = {tuple(sorted((i.get("ratingStats") or {}).items())) for i in items}
    sources = {i.get("source", "") for i in items}

    if len(ils) > 1:
        legit_diff_il.append((slot, name, items))
    elif len(sets) > 1:
        legit_diff_set.append((slot, name, items))
    elif len(classes) > 1:
        legit_diff_classes.append((slot, name, items))
    elif len(rstats) > 1:
        legit_diff_stats.append((slot, name, items))
    elif len(sigs) == 1:
        # All key fields match -> true duplicate
        true_dups.append((slot, name, items))
    elif len(sources) > 1:
        legit_diff_source.append((slot, name, items))
    else:
        unclassified.append((slot, name, items))

print(f"=== Duplicate classification (full+full pairs only) ===\n")
print(f"Legit — different IL tier:      {len(legit_diff_il):>4}")
print(f"Legit — different set name:     {len(legit_diff_set):>4}")
print(f"Legit — different allowedClass: {len(legit_diff_classes):>4}")
print(f"Legit — same IL diff ratings:   {len(legit_diff_stats):>4}")
print(f"Legit — multi-source same item: {len(legit_diff_source):>4}")
print(f"TRUE DUPLICATES (identical):    {len(true_dups):>4}")
print(f"Unclassified:                   {len(unclassified):>4}")

print(f"\n=== TRUE DUPLICATES (deletion candidates) ===")
for slot, name, items in true_dups:
    items.sort(key=lambda x: x.get("id", 0))
    ids = [i["id"] for i in items]
    print(f"  {slot!r:>16} {name!r} -> ids {ids} (IL {items[0].get('item_level')}, set {items[0].get('set','')!r})")

print(f"\n=== Unclassified (need eyeballs) ===")
for slot, name, items in unclassified[:10]:
    items.sort(key=lambda x: x.get("id", 0))
    print(f"  {slot!r} {name!r}:")
    for i in items:
        print(f"    id={i['id']} IL={i.get('item_level')} CR={i.get('combinedRating')} set={i.get('set','')!r} src={i.get('source','')[:50]!r}")

print(f"\n=== Sample 'same IL diff ratings' (top 5) ===")
for slot, name, items in legit_diff_stats[:5]:
    items.sort(key=lambda x: x.get("id", 0))
    print(f"  {slot!r} {name!r}:")
    for i in items:
        print(f"    id={i['id']} IL={i.get('item_level')} ratings={i.get('ratingStats')}")
