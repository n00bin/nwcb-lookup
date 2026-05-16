"""Remove the 29 stub gear entries (those with no 'set' and no 'source') that have
a fully-populated duplicate with the same (slot, name)."""
import json
from collections import defaultdict
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

# Group by (slot, name)
groups = defaultdict(list)
for it in data:
    if it.get("name") and it.get("slot"):
        groups[(it["slot"], it["name"])].append(it)

# Find stub+full pairs and identify stub ids to delete
stub_ids_to_delete = set()
deleted_summary = []
for (slot, name), items in groups.items():
    if len(items) < 2:
        continue
    stubs = [i for i in items if not i.get("set") and not i.get("source")]
    fulls = [i for i in items if i.get("set") or i.get("source")]
    if stubs and fulls:
        for s in stubs:
            stub_ids_to_delete.add(s["id"])
            deleted_summary.append((s["id"], slot, name, [f["id"] for f in fulls]))

print(f"Identified {len(stub_ids_to_delete)} stub entries to delete.")
print("\nDeletion plan:")
for sid, slot, name, full_ids in deleted_summary:
    print(f"  Delete id={sid} ({name!r} {slot!r}) — keeping full id(s) {full_ids}")

# Remove them
new_data = [it for it in data if it["id"] not in stub_ids_to_delete]
print(f"\nBefore: {len(data)} items; After: {len(new_data)} items")
print(f"Removed: {len(data) - len(new_data)} items")

PATH.write_text(json.dumps(new_data, indent=2, ensure_ascii=False), encoding="utf-8")
print("\ngear.json written.")
