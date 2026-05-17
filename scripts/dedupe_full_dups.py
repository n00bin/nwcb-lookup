"""Delete the 42 functionally-identical duplicate gear entries.

For each (slot, name) group whose entries all share identical (IL, ratingStats,
CR, set, allowedClasses), keep the lowest id and drop the rest."""
import json
from collections import defaultdict
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

groups = defaultdict(list)
for it in data:
    if it.get("name") and it.get("slot"):
        groups[(it["slot"], it["name"])].append(it)

def sig(it):
    return (
        it.get("item_level"),
        tuple(sorted((it.get("ratingStats") or {}).items())),
        it.get("combinedRating"),
        it.get("set", ""),
        tuple(sorted(it.get("allowedClasses") or [])),
    )

ids_to_delete = set()
deleted_summary = []
for (slot, name), items in groups.items():
    if len(items) < 2:
        continue
    sigs = {sig(i) for i in items}
    if len(sigs) != 1:
        continue
    # All entries identical -> keep lowest id, delete rest
    items.sort(key=lambda x: x.get("id", 0))
    keep = items[0]
    for drop in items[1:]:
        ids_to_delete.add(drop["id"])
        deleted_summary.append((drop["id"], slot, name, keep["id"]))

print(f"Will delete {len(ids_to_delete)} duplicate entries:")
for did, slot, name, kid in deleted_summary:
    print(f"  drop id={did} ({slot!r} {name!r}) — keeping id={kid}")

new_data = [it for it in data if it["id"] not in ids_to_delete]
print(f"\nBefore: {len(data)} items; After: {len(new_data)} items")
print(f"Removed: {len(data) - len(new_data)} items")

PATH.write_text(json.dumps(new_data, indent=2, ensure_ascii=False), encoding="utf-8")
print("\ngear.json written.")
