"""Find what items use Antiquities of X set names — look for Avernus variant."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

print("=== Items with 'Antiquities' in set field ===")
for it in data:
    s = it.get("set", "")
    if "Antiquities" in s:
        print(f"  id={it['id']:>5}  IL={it.get('item_level'):>4}  {it.get('slot'):>6}  {it.get('name')!r:50}  set={s!r:30}  src={(it.get('source','') or '')[:50]!r}")

print("\n=== Items with 'Antiquities' in source field ===")
hits = 0
for it in data:
    src = it.get("source", "") or ""
    if "Antiquities" in src and "Antiquities" not in (it.get("set", "") or ""):
        hits += 1
        if hits > 15:
            continue
        print(f"  id={it['id']:>5}  IL={it.get('item_level'):>4}  {it.get('slot'):>6}  {it.get('name')!r:50}  set={it.get('set','')!r:30}  src={src[:50]!r}")
if hits > 15:
    print(f"  ... and {hits-15} more")

print("\n=== Executioner's Might items in data ===")
for it in data:
    ebs = it.get("equipBonuses") or []
    for eb in ebs:
        if "Executioner" in (eb.get("name") or ""):
            print(f"  id={it['id']:>5}  IL={it.get('item_level'):>4}  {it.get('slot'):>6}  {it.get('name')!r:50}  set={it.get('set','')!r:30}  src={(it.get('source','') or '')[:50]!r}")
            break
