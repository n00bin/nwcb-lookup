#!/usr/bin/env python3
"""Backfill setBonus text for sets where I have the bonus from OCR memory
but didn't extract it into the schema during the gear batch processing.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEAR_PATH = ROOT / "data" / "gear.json"

# Map: set name -> setBonus text. Only applied to items missing setBonus.
SET_BONUSES = {
    "Impending Doom": (
        "2 of Set: Accumulate 10 Charges to consume them and become Unleashed. "
        "Charged by: 1 charge per Daily power (10s CD), 1 charge per Encounter power "
        "(7s CD), 1 charge per 7 seconds in combat. Unleashed grants Tank: -Incoming "
        "Damage / Heal: +Outgoing Healing (values scale with item level). Charges and "
        "Unleashed last 15 seconds and are refreshable. Leaving combat removes all Charges. "
        "Set also grants +Forte (scales with tier)."
    ),
    "Enchanted Advantage": "2 of Set: +3% Combat Advantage (some variants grant +25 Action Points or +7% Combat Advantage).",
    "Enchanted Healing": "2 of Set: +3% Outgoing Healing (lower-tier variants grant +2% Outgoing Healing).",
    "Enchanted Awareness": "2 of Set: +1,000 Awareness.",
}


def main():
    gear = json.loads(GEAR_PATH.read_text(encoding="utf-8"))
    updated = 0
    for g in gear:
        s = g.get("set")
        if not s or s not in SET_BONUSES:
            continue
        if g.get("setBonus"):
            continue  # Don't overwrite existing
        g["setBonus"] = SET_BONUSES[s]
        updated += 1
    GEAR_PATH.write_text(json.dumps(gear, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Backfilled setBonus on {updated} items across {len(SET_BONUSES)} sets.")


if __name__ == "__main__":
    main()
