"""Find anchor items for unmatched ring families."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

keywords = ["Wayseeker", "Waywatcher", "Mightbreaker", "Soothsayer", "Soulfire",
            "Stalwartneedle", "Medic's Ring", "Mercenary's Ring", "Officer's Ring",
            "Physician's Ring", "Scout's Ring", "Soldier's Ring", "Lionsmane Ring"]

for kw in keywords:
    print(f"\n=== '{kw}' related items (with set/source) ===")
    hits = 0
    for it in data:
        n = it.get("name", "")
        if kw not in n: continue
        s = it.get("set", "") or ""
        src = it.get("source", "") or ""
        if s or src:
            hits += 1
            if hits > 5: continue
            print(f"  id={it['id']:>5}  IL={it.get('item_level'):>4}  {n!r:45}  set={s!r:30}  src={src[:50]!r}")
    if hits == 0:
        print(f"  (no anchors)")
    elif hits > 5:
        print(f"  ... and {hits-5} more")
