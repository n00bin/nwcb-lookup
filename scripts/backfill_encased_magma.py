"""Backfill the 2 Encased Magma Lute/Tome orphans into Living Magma set."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

# First confirm siblings exist with Living Magma set
print("=== Living Magma siblings in data ===")
for it in data:
    if "Encased Magma" in it.get("name", "") or it.get("set") == "Living Magma":
        s = it.get("set", "")
        src = it.get("source", "")
        marker = " <-- ORPHAN" if it["id"] in (4, 27) else ""
        print(f"  id={it['id']:>5}  IL={it.get('item_level'):>4}  {it.get('slot'):>9}  {it.get('name')!r:50}  set={s!r}  src={src[:40]!r}{marker}")

TARGETS = {4, 27}
NOTE = "Set classified 2026-05-17 — matches existing Living Magma siblings (Encased Magma Saber, etc.) at IL 2700; n00b ack."

print("\n=== Backfill ===")
for it in data:
    if it["id"] in TARGETS:
        it["set"] = "Living Magma"
        it["setSize"] = 2
        it["source"] = "Mountain of Flame Campaign Store"
        it["notes"] = NOTE
        print(f"  Backfilled id={it['id']:>5}  {it.get('slot'):>9}  {it.get('name')!r}")

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nTotal items: {len(data)}.")
