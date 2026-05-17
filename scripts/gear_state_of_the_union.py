"""Comprehensive audit of where the gear database stands.

Reports: total count, slot breakdown, class coverage, IL/era distribution,
missing-data hotspots, set completeness, and quick win opportunities."""
import json
from collections import Counter, defaultdict
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

n = len(data)
print(f"=== TOTAL GEAR: {n} items ===\n")

# --- Slot distribution ---
slot_counts = Counter(it.get("slot", "(none)") for it in data)
print("=== Slot distribution ===")
for slot, c in slot_counts.most_common():
    print(f"  {slot:>12}  {c:>4}")
print()

# --- Class coverage ---
class_counts = Counter()
no_class = 0
for it in data:
    classes = it.get("allowedClasses")
    if not classes:
        no_class += 1
    else:
        for cls in classes:
            class_counts[cls] += 1
print("=== Class coverage ===")
print(f"  (no allowedClasses set):    {no_class:>4} items (universal or unclassified)")
for cls, c in sorted(class_counts.items(), key=lambda x: -x[1]):
    print(f"  {cls:>12}  {c:>4}")
print()

# --- IL / era distribution ---
il_buckets = Counter()
for it in data:
    il = it.get("item_level") or 0
    if il == 0:
        il_buckets["(no IL)"] += 1
    elif il < 500:
        il_buckets["<500"] += 1
    elif il < 1000:
        il_buckets["500-999 (legacy)"] += 1
    elif il < 1500:
        il_buckets["1000-1499 (Mod 6-15)"] += 1
    elif il < 2500:
        il_buckets["1500-2499 (Mod 16-18)"] += 1
    elif il < 3500:
        il_buckets["2500-3499 (Mod 19-23)"] += 1
    elif il < 4500:
        il_buckets["3500-4499 (Mod 24-26)"] += 1
    else:
        il_buckets["4500+ (Mod 27+)"] += 1
print("=== Item Level distribution (era buckets) ===")
order = ["<500", "500-999 (legacy)", "1000-1499 (Mod 6-15)", "1500-2499 (Mod 16-18)",
         "2500-3499 (Mod 19-23)", "3500-4499 (Mod 24-26)", "4500+ (Mod 27+)", "(no IL)"]
for k in order:
    if il_buckets[k]:
        print(f"  {k:>30}  {il_buckets[k]:>4}")
print()

# --- Missing data hotspots ---
no_set = sum(1 for it in data if not it.get("set"))
no_source = sum(1 for it in data if not it.get("source"))
no_ratings = sum(1 for it in data if not it.get("ratingStats"))
no_il = sum(1 for it in data if not it.get("item_level"))
no_equip = sum(1 for it in data if not it.get("equipBonuses"))
no_classes = sum(1 for it in data if not it.get("allowedClasses"))
print("=== Missing-data hotspots ===")
print(f"  No set name:        {no_set:>4} ({100*no_set/n:.1f}%)")
print(f"  No source:          {no_source:>4} ({100*no_source/n:.1f}%)")
print(f"  No ratingStats:     {no_ratings:>4} ({100*no_ratings/n:.1f}%)")
print(f"  No item_level:      {no_il:>4} ({100*no_il/n:.1f}%)")
print(f"  No equipBonuses:    {no_equip:>4} ({100*no_equip/n:.1f}%) (many are intentional — non-set gear)")
print(f"  No allowedClasses:  {no_classes:>4} ({100*no_classes/n:.1f}%)")
print()

# --- Set completeness ---
sets = defaultdict(lambda: defaultdict(list))  # set_name -> slot -> [ids]
for it in data:
    s = it.get("set")
    if not s:
        continue
    sets[s][it.get("slot", "(none)")].append(it["id"])

print(f"=== Sets in data: {len(sets)} unique set names ===")
print(f"\nSets with only 1 slot covered (incomplete):")
incomplete = []
for set_name, slots in sets.items():
    if len(slots) == 1:
        incomplete.append((set_name, list(slots.keys())[0], len(list(slots.values())[0])))
incomplete.sort(key=lambda x: -x[2])
for set_name, slot, c in incomplete[:20]:
    print(f"  {set_name!r:50}  only {slot}  ({c} items)")
print(f"  ... {len(incomplete)} total sets with only one slot covered")
print()

# --- Sets that look complete (4-piece armor sets) ---
complete_armor_sets = []
armor_slots = {"Head", "Armor", "Arms", "Feet"}
for set_name, slots in sets.items():
    if armor_slots.issubset(slots.keys()):
        complete_armor_sets.append(set_name)
print(f"=== Complete 4-piece armor sets (Head+Armor+Arms+Feet): {len(complete_armor_sets)} ===")
for s in sorted(complete_armor_sets)[:25]:
    cnt = sum(len(v) for v in sets[s].values())
    print(f"  {s!r:50}  {cnt} pieces total")
if len(complete_armor_sets) > 25:
    print(f"  ... and {len(complete_armor_sets)-25} more")
print()

# --- Items missing both set AND source (probably needs deletion or attention) ---
suspicious = [it for it in data if not it.get("set") and not it.get("source")]
print(f"=== Suspicious entries (no set AND no source): {len(suspicious)} ===")
for it in suspicious[:15]:
    print(f"  id={it['id']:>5}  {it.get('slot'):>8}  {it.get('name')!r:60}  IL={it.get('item_level')}")
if len(suspicious) > 15:
    print(f"  ... and {len(suspicious)-15} more")
