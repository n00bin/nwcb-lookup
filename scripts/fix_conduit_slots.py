#!/usr/bin/env python3
"""Fix Conduit clothing slot mis-assignment from batch 1.

Variants like 'Arcane Conduit Seal -- Pressured Muse' were stored at
slot 'Ring' / 'Neck' instead of inheriting the base item's clothing
slot (Shirt / Pants). All Conduit Seals/Sigils/Marks/Inks/Crests/
Insignias are clothing pieces, never rings or necks.

Canonical slot per Conduit type (verified against the unsuffixed base
entries that came from later batches):

  Seal     -> Shirt
  Sigil    -> Pants
  Mark     -> Pants
  Ink      -> Shirt
  Crest    -> Shirt
  Insignia -> Pants

Applies the same correction to all Conduit lines (Arcane, Mystic, etc.).
Also strips trailing nulls from equipBonuses lists.
"""
import json
from pathlib import Path

GEAR_PATH = Path(__file__).resolve().parents[2] / "data" / "gear.json"

# Conduit type -> canonical slot
CONDUIT_SLOTS = {
    "Seal": "Shirt",
    "Sigil": "Pants",
    "Mark": "Pants",
    "Ink": "Shirt",
    "Crest": "Shirt",
    "Insignia": "Pants",
}


def detect_conduit_type(name):
    """Return the conduit type if this is a Conduit item, else None."""
    if "Conduit" not in name:
        return None
    # Split on em-dash for variant items
    base = name.split("—")[0].strip()
    for ctype in CONDUIT_SLOTS:
        if base.endswith(ctype):
            return ctype
    return None


def main():
    gear = json.loads(GEAR_PATH.read_text(encoding="utf-8"))
    fixed_slot = 0
    cleaned_bonuses = 0

    for g in gear:
        ctype = detect_conduit_type(g.get("name", ""))
        if ctype:
            correct_slot = CONDUIT_SLOTS[ctype]
            if g.get("slot") != correct_slot:
                g["slot"] = correct_slot
                fixed_slot += 1

        # Clean trailing/inline nulls in equipBonuses
        eb = g.get("equipBonuses")
        if isinstance(eb, list):
            cleaned = [e for e in eb if e]
            if len(cleaned) != len(eb):
                g["equipBonuses"] = cleaned
                cleaned_bonuses += 1

    GEAR_PATH.write_text(json.dumps(gear, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Slot corrections:          {fixed_slot} Conduit items moved to correct clothing slot")
    print(f"equipBonuses cleanups:     {cleaned_bonuses} entries had null entries stripped")
    print(f"Total entries in gear.json: {len(gear)}")


if __name__ == "__main__":
    main()
