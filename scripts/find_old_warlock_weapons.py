"""Find context for the 11 old Warlock weapon orphans by looking at similar items."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

# Look for related items by name keywords
keywords = ["Corpseslayer", "Deathbringer", "Pioneer Khaniar", "Tecpatl",
            "Pact Blade", "Hexweaver", "Stronghold", "Vistani", "Exalted"]
for kw in keywords:
    print(f"\n=== '{kw}' items (excluding our orphans) ===")
    orphan_ids = {149, 153, 161, 162, 165, 166, 174, 183, 187, 192, 197}
    hits = 0
    for it in data:
        n = it.get("name", "")
        if kw in n and it["id"] not in orphan_ids:
            hits += 1
            if hits > 8:
                continue
            s = it.get("set", "")
            src = it.get("source", "")
            print(f"  id={it['id']:>5}  IL={it.get('item_level'):>4}  {it.get('slot'):>9}  {n!r:50}  set={s!r:25}  src={src[:50]!r}")
    if hits > 8:
        print(f"  ... and {hits-8} more")
    if hits == 0:
        print(f"  (no other items)")
