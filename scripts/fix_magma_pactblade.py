"""Add Living Magma set to id 160 Encased Magma Pactblade (had source but no set)."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

for it in data:
    if it["id"] == 160:
        it["set"] = "Living Magma"
        it["setSize"] = 2
        it["notes"] = "Set added 2026-05-17 — was missing set name despite having source. Matches all other Encased Magma weapons."
        print(f"  Updated id={it['id']:>5}  {it.get('name')!r} -> set: Living Magma")

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nTotal items: {len(data)}.")
