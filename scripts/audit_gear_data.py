"""Audit gear.json for issues that could cause items to be hidden in Toon Forge UI."""
import json
from collections import Counter
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

# 1. Slot name distribution — any unexpected variants?
slots = Counter(it.get("slot", "<missing>") for it in data)
print("=== Slot names (count) ===")
for slot, count in slots.most_common():
    print(f"  {count:>5}  {slot!r}")

# 2. Items with no allowedClasses (universal) vs class-restricted
no_classes = [it for it in data if not it.get("allowedClasses")]
print(f"\n=== Class restrictions ===")
print(f"  Items without allowedClasses (universal): {len(no_classes)}")

cls_counts = Counter()
for it in data:
    for c in it.get("allowedClasses", []) or []:
        cls_counts[c] += 1
print(f"  Items per allowed class:")
for cls, count in cls_counts.most_common():
    print(f"    {count:>5}  {cls}")

# 3. Items missing required fields
missing_name = [it for it in data if not it.get("name")]
missing_slot = [it for it in data if not it.get("slot")]
missing_id = [it for it in data if not it.get("id")]
print(f"\n=== Missing fields ===")
print(f"  Missing name: {len(missing_name)}")
print(f"  Missing slot: {len(missing_slot)}")
print(f"  Missing id: {len(missing_id)}")

# 4. Items where the slot value contains typos or whitespace
suspicious_slots = [it for it in data if it.get("slot") and (
    it["slot"] != it["slot"].strip() or
    "  " in it["slot"]
)]
print(f"\n=== Slots with leading/trailing/double spaces: {len(suspicious_slots)} ===")
for it in suspicious_slots[:10]:
    print(f"    {it.get('id')}  slot={it['slot']!r}  name={it.get('name')!r}")

# 5. Items with allowedClasses containing unknown class names
known_classes = {"Bard", "Barbarian", "Cleric", "Fighter", "Paladin", "Ranger", "Rogue", "Warlock", "Wizard"}
bad_classes = [(it, [c for c in it.get("allowedClasses", []) or [] if c not in known_classes]) for it in data]
bad_classes = [(it, bad) for it, bad in bad_classes if bad]
print(f"\n=== Items with unknown allowedClasses: {len(bad_classes)} ===")
for it, bad in bad_classes[:10]:
    print(f"    {it.get('id')}  bad={bad}  name={it.get('name')!r}")

# 6. Duplicate names within the same slot (could mean items shadow each other in pickers)
from collections import defaultdict
dup_check = defaultdict(list)
for it in data:
    if it.get("name") and it.get("slot"):
        dup_check[(it["slot"], it["name"])].append(it.get("id"))
dups = {k: v for k, v in dup_check.items() if len(v) > 1}
print(f"\n=== Duplicate (slot, name) pairs: {len(dups)} ===")
for (slot, name), ids in list(dups.items())[:15]:
    print(f"    slot={slot!r}  name={name!r}  ids={ids}")
