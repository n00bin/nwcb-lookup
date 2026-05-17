"""Fuzzy-match the 249 rich-data orphans against fully-populated entries
to find duplicates that the exact-match audit missed (casing/punctuation diffs)."""
import json
import re
from collections import defaultdict
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

def norm(s):
    """Aggressive normalization for fuzzy match."""
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return s

orphans = [it for it in data if not it.get("set") and not it.get("source")]
populated = [it for it in data if (it.get("set") or it.get("source"))]

# Index populated items by (slot, normalized_name)
pop_index = defaultdict(list)
for it in populated:
    key = (it.get("slot"), norm(it.get("name", "")))
    pop_index[key].append(it)

fuzzy_dups = []
no_match = []
for orph in orphans:
    key = (orph.get("slot"), norm(orph.get("name", "")))
    matches = pop_index.get(key, [])
    if matches:
        fuzzy_dups.append((orph, matches))
    else:
        no_match.append(orph)

print(f"=== Fuzzy duplicate audit of 259 orphans ===\n")
print(f"Fuzzy-matched to a populated entry:  {len(fuzzy_dups)}")
print(f"No fuzzy match (truly unique orphan): {len(no_match)}")
print()

if fuzzy_dups:
    print(f"=== Fuzzy duplicates (deletion candidates) ===")
    # Show breakdown of why they fuzzy-matched
    diff_types = {"casing only": 0, "punctuation": 0, "spacing": 0, "exact-after-norm": 0}
    for orph, matches in fuzzy_dups:
        on = orph.get("name", "")
        mn = matches[0].get("name", "")
        if on == mn:
            diff_types["exact-after-norm"] += 1
        elif on.lower() == mn.lower():
            diff_types["casing only"] += 1
        else:
            diff_types["punctuation"] += 1
    for k, v in diff_types.items():
        print(f"  {k}: {v}")
    print()
    print(f"First 30 fuzzy-dup examples:")
    for orph, matches in fuzzy_dups[:30]:
        on = orph.get("name", "")
        mids = [(m["id"], m.get("name", "")) for m in matches]
        print(f"  orph id={orph['id']:>5}  IL={orph.get('item_level')!s:>5}  {on!r:55}")
        for mid, mn in mids:
            print(f"      -> full id={mid}  {mn!r}")

print()
print(f"=== Sample of truly unique orphans (no fuzzy match) ===")
for orph in no_match[:25]:
    print(f"  id={orph['id']:>5}  {orph.get('slot'):>8}  IL={orph.get('item_level')!s:>5}  {orph.get('name')!r:55}  ratings={list((orph.get('ratingStats') or {}).keys())}")
if len(no_match) > 25:
    print(f"  ... and {len(no_match)-25} more")
