"""Check if Protégé's Hood specifically has duplicates, and summarize duplicate
quality: stub-vs-full so we know which to keep."""
import json
from collections import defaultdict
d = json.loads(open('G:/ai_projects/nwcb/data/gear.json', encoding='utf-8').read())

# Check Protégé's Hood
print("=== Protégé / Protege items ===")
for it in d:
    if 'rot' in it.get('name','') and 'g' in it.get('name','') and 'Hood' in it.get('name',''):
        print(f"  id {it['id']:>5} slot={it['slot']!r} set={it.get('set')!r} IL={it.get('item_level')} classes={it.get('allowedClasses')}")

# Classify duplicates
dups = defaultdict(list)
for it in d:
    if it.get('name') and it.get('slot'):
        dups[(it['slot'], it['name'])].append(it)

stub_old_count = 0
populated_new_count = 0
mixed_pairs = []
for (slot, name), items in dups.items():
    if len(items) < 2: continue
    # Sort by id
    items.sort(key=lambda x: x.get('id', 0))
    stub = [i for i in items if not i.get('set') and not i.get('source')]
    full = [i for i in items if i.get('set') or i.get('source')]
    if stub and full:
        mixed_pairs.append((slot, name, stub, full))

print(f"\n=== Duplicate quality summary ===")
print(f"Mixed pairs (stub + fully-populated): {len(mixed_pairs)}")
print(f"\nFirst 10 mixed pairs:")
for slot, name, stub, full in mixed_pairs[:10]:
    print(f"  slot={slot!r} name={name!r}")
    for s in stub:
        print(f"    STUB id={s['id']} (no set/source)")
    for f in full:
        print(f"    FULL id={f['id']} set={f.get('set')!r}")
