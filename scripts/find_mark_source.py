"""Find the source of 'Mark of the X' items by checking related items with same set
or any 'Mark' items elsewhere in data that DO have source info."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

# All Mark items
marks = [it for it in data if "Mark of" in it.get("name", "")]
print(f"=== All 'Mark of' items (any slot, any naming): {len(marks)} ===\n")
for it in sorted(marks, key=lambda x: (x.get("slot", ""), x["id"])):
    src = it.get("source", "")
    setn = it.get("set", "")
    notes = it.get("notes", "")
    print(f"  id={it['id']:>5}  {it.get('slot'):>6}  IL={it.get('item_level')!s:>5}  {it.get('name')!r:55}")
    print(f"          set={setn!r}  source={src!r}")
    if notes:
        print(f"          notes={notes[:120]!r}")

# Other IL 2600 items in data — see if any cluster around a known set
print(f"\n=== Other items at IL 2600 (to identify the era/source) ===\n")
il2600 = [it for it in data if it.get("item_level") == 2600 and "Mark of" not in it.get("name", "")]
print(f"Total IL 2600 items: {len(il2600)}")
# Show ones with set/source info
with_source = [it for it in il2600 if it.get("set") or it.get("source")]
print(f"Of those, with set/source: {len(with_source)}")
for it in with_source[:15]:
    print(f"  id={it['id']:>5}  {it.get('slot'):>6}  {it.get('name')!r:55}  set={it.get('set','')!r}  src={it.get('source','')!r}")
