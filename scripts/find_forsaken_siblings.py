"""Find Forsaken Mender's / Sentinel's family items and any siblings with set/source."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

print("=== All Forsaken Mender's / Sentinel's items ===")
for it in data:
    n = it.get("name", "")
    if "Forsaken" in n and ("Mender" in n or "Sentinel" in n):
        s = it.get("set", "")
        src = it.get("source", "")
        cls = it.get("allowedClasses") or []
        print(f"  id={it['id']:>5}  IL={it.get('item_level'):>4}  {it.get('slot'):>6}  {n!r:50}  set={s!r:25}  src={src[:40]!r}  classes={cls}")

print("\n=== Other 'Forsaken' items in data ===")
for it in data:
    n = it.get("name", "")
    if "Forsaken" in n and "Mender" not in n and "Sentinel" not in n:
        s = it.get("set", "")
        src = it.get("source", "")
        print(f"  id={it['id']:>5}  IL={it.get('item_level'):>4}  {it.get('slot'):>6}  {n!r:50}  set={s!r:25}  src={src[:40]!r}")

print("\n=== Other IL 1225 Head/Armor/Arms/Feet items with set names (era context) ===")
hits = 0
for it in data:
    if it.get("item_level") == 1225 and it.get("slot") in ("Head", "Armor", "Arms", "Feet") and it.get("set"):
        hits += 1
        if hits > 12:
            continue
        print(f"  id={it['id']:>5}  {it.get('slot'):>6}  {it.get('name')!r:50}  set={it.get('set','')!r:30}  src={(it.get('source','') or '')[:40]!r}")
print(f"\n(Total: {hits} items)")
