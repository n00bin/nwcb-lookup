"""Backfill source for 14 Belt/Neck orphans (Dragonflight + Lionsmane families).
Flag 2 singletons (Celestial Sash + Divine Focus) for verification."""
import json
import re
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

DRAGONFLIGHT_IDS = {2582, 2580, 2578, 2570, 2584, 2579, 2576, 2569}
LIONSMANE_IDS = {2557, 2564, 2559, 2562, 2547, 2552}

count = 0
for it in data:
    iid = it["id"]
    if iid in DRAGONFLIGHT_IDS:
        it["source"] = "Stronghold Guild Marketplace (Rank 3)"
        it["notes"] = "Source classified 2026-05-18 — Dragonflight Belt/Neck family (PvE) matches ring siblings; n00b ack."
        count += 1
        print(f"  Dragonflight: id={iid:>5}  {it.get('slot'):>5}  {it.get('name')!r}")
    elif iid in LIONSMANE_IDS:
        it["source"] = "Stronghold Guild Marketplace"
        it["notes"] = "Source classified 2026-05-18 — Lionsmane Belt/Neck family (PvE, distinct from PvP Lionsmane armor set); n00b ack."
        count += 1
        print(f"  Lionsmane:    id={iid:>5}  {it.get('slot'):>5}  {it.get('name')!r}")

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nBackfilled {count} entries. Total items: {len(data)}.")
