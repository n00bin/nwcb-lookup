"""Fix all 12 'Mark of the X (Equip Power)' Ring orphans.

For each Ring entry (ids 350-361):
- Determine correct slot: Shirt for Convert/Adept/Fledgling/Recruit, Pants for Novice/Initiate
- Find the matching Shirt/Pants twin by base name + equip power
- Merge richer Ring data (full equipBonuses, allowedClasses) into the twin
- Add source: Red Harvest Heroic Encounters + Red Harvest Campaign Store
- Delete the Ring entry
- If no twin exists: re-slot the Ring entry to Shirt/Pants and backfill set
"""
import json
import re
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

PANTS_BASES = {"Novice", "Initiate"}
SHIRT_BASES = {"Convert", "Adept", "Fledgling", "Recruit"}

# Map base name -> set
BASE_TO_SET = {
    "Convert":   "Enchanted Awareness",
    "Adept":     "Enchanted Forte",
    "Fledgling": "Enchanted Forte",
    "Recruit":   "Enchanted Advantage",
    "Novice":    "Enchanted Advantage",
    "Initiate":  "Enchanted Advantage",
}

SOURCE = "Red Harvest Heroic Encounters / Red Harvest Campaign Store"
VERIFY_NOTE = "Verified in-game 2026-05-17 — n00b confirmed slot Shirt/Pants and Red Harvest source."

ring_ids = list(range(350, 362))
ring_entries = {it["id"]: it for it in data if it["id"] in ring_ids}

def parse_ring_name(name):
    """Parse e.g. 'Mark of the Convert (Survivor's Remedy)' into (base, equip_power)."""
    m = re.match(r"Mark of the (\w+)\s*\((.+)\)$", name)
    if m:
        return m.group(1), m.group(2)
    return None, None

def find_twin(base, equip_power, target_slot):
    """Find a Shirt/Pants entry that matches base name + equip power."""
    eq_lower = equip_power.lower()
    for it in data:
        if it.get("slot") != target_slot:
            continue
        n = it.get("name", "")
        if not n.startswith(f"Mark of the {base}"):
            continue
        # Match if name has the equip power, OR if equipBonuses lists it
        if eq_lower in n.lower():
            return it
        for eb in it.get("equipBonuses") or []:
            if eq_lower in (eb.get("name", "") or "").lower():
                return it
    return None

actions = []
to_delete = set()
for rid, ring in ring_entries.items():
    base, equip_power = parse_ring_name(ring.get("name", ""))
    if not base:
        actions.append(f"  SKIP id={rid}: name doesn't parse")
        continue
    target_slot = "Pants" if base in PANTS_BASES else "Shirt"
    twin = find_twin(base, equip_power, target_slot)
    if twin:
        # Migrate rich data to twin
        actions.append(f"  MERGE Ring id={rid} ({base}/{equip_power}) -> {target_slot} id={twin['id']}")
        # Pull set-bonus equipBonus from ring (it has the full set details)
        ring_ebs = ring.get("equipBonuses") or []
        twin_ebs = twin.get("equipBonuses") or []
        twin_eb_names = {(eb.get("name") or "").lower() for eb in twin_ebs}
        for eb in ring_ebs:
            ebn = (eb.get("name") or "").lower()
            if ebn and ebn not in twin_eb_names:
                twin_ebs.append(eb)
        twin["equipBonuses"] = twin_ebs
        # Pull allowedClasses if twin is missing it
        if not twin.get("allowedClasses") and ring.get("allowedClasses"):
            twin["allowedClasses"] = ring["allowedClasses"]
        # Backfill source on twin
        if not twin.get("source"):
            twin["source"] = SOURCE
        twin["notes"] = VERIFY_NOTE
        to_delete.add(rid)
    else:
        # No twin — re-slot the Ring entry to Shirt/Pants
        actions.append(f"  RE-SLOT Ring id={rid} ({base}/{equip_power}) -> become {target_slot}")
        ring["slot"] = target_slot
        if not ring.get("set"):
            ring["set"] = BASE_TO_SET.get(base, "")
        if not ring.get("source"):
            ring["source"] = SOURCE
        ring["notes"] = VERIFY_NOTE

# Apply deletions
before = len(data)
data = [it for it in data if it["id"] not in to_delete]
after = len(data)

print("=== Actions taken ===")
for a in actions:
    print(a)
print()
print(f"Deleted {len(to_delete)} duplicate Ring entries; {len(actions)-len(to_delete)} re-slotted in place")
print(f"Before: {before} items; After: {after} items")

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print("gear.json written.")
