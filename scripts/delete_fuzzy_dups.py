"""Delete the 3 fuzzy duplicate orphans. First migrate any richer data from
the orphan to the kept entry (ratings, equipBonuses, percentStats, classes)
since orphans sometimes have data the populated entry is missing."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))
by_id = {it["id"]: it for it in data}

# (orphan_id, keep_id, reason)
pairs = [
    (24, 298, "lowercase 'c' in 'covenant'"),
    (70, 473, "typo 'PAct' instead of 'Pact'"),
    (129, 195, "leading asterisks '***'"),
]

def merge(orphan, keep):
    """Bring over any field on orphan that's missing/empty on keep."""
    changed = []
    for field in ("item_level", "ratingStats", "combinedRating", "percentStats",
                  "abilityBonuses", "allowedClasses", "set", "source"):
        ov = orphan.get(field)
        kv = keep.get(field)
        # Treat empty containers as missing
        is_empty = kv in (None, "", 0, [], {})
        if ov and is_empty:
            keep[field] = ov
            changed.append(field)
    # equipBonuses: merge by name to avoid duplicates
    ok_ebs = keep.get("equipBonuses") or []
    ok_names = {(eb.get("name") or "").lower() for eb in ok_ebs}
    for eb in orphan.get("equipBonuses") or []:
        n = (eb.get("name") or "").lower()
        if n and n not in ok_names:
            ok_ebs.append(eb)
            changed.append(f"equipBonus({eb.get('name')})")
    keep["equipBonuses"] = ok_ebs
    return changed

to_delete = set()
for oid, kid, reason in pairs:
    orph = by_id.get(oid)
    keep = by_id.get(kid)
    if not orph or not keep:
        print(f"  SKIP id={oid}->id={kid}: missing")
        continue
    changes = merge(orph, keep)
    print(f"  DELETE id={oid} ({reason}) -> keep id={kid}")
    if changes:
        print(f"    migrated to id={kid}: {changes}")
    to_delete.add(oid)

before = len(data)
data = [it for it in data if it["id"] not in to_delete]
PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nBefore: {before} items; After: {len(data)} items (removed {before-len(data)}).")
