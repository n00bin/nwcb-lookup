"""Compare Mark of the Convert variants — Ring id 350 vs Shirt id 500."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

target_ids = {350, 494, 500, 356}  # convert ring, convert shirt base, convert shirt SR, convert ring precision
for it in data:
    if it["id"] in target_ids:
        print(f"--- id={it['id']}  slot={it.get('slot')}  ---")
        print(f"  name: {it.get('name')!r}")
        print(f"  IL={it.get('item_level')}  CR={it.get('combinedRating')}")
        print(f"  ratings={it.get('ratingStats')}")
        print(f"  percentStats={it.get('percentStats')}")
        print(f"  equipBonuses={it.get('equipBonuses')}")
        print(f"  set={it.get('set','')!r}")
        print(f"  source={it.get('source','')!r}")
        print(f"  classes={it.get('allowedClasses')}")
        print()
