#!/usr/bin/env python3
"""Apply confirmed corrections to data/races.json based on the NW Hub
races page (verified by n00b 2026-05-08).

Targeted fixes only — most of our 15 races already matched. Updates:

- Aasimar: bonuses were wrong (+2 any/+2 any -> +2 WIS / +2 choose
  CON|CHA). Trait names changed (Celestial Superiority -> Celestial
  Legacy, Celestial Presence -> Healing Hands). Old percentStats
  were attached to the WRONG trait names; cleared with a
  "needs verification" note.
- Gith: trait names changed (Gith Endurance -> Decentralized Mind,
  Gith Advantage -> Githborn Discipline). Old percentStats cleared
  (verification needed).
- Dwarf: trait name fix (Cast-Iron -> Cast-Iron Stomach).
- Half-Elf, Half-Orc, Tiefling, Sun Elf: descriptions added from NW
  Hub where given. percentStats added for any explicit numbers.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RACES = ROOT / "data" / "races.json"


def find_race(races, name):
    for r in races:
        if r["name"] == name:
            return r
    raise KeyError(name)


def set_trait(race, old_name, new_name=None, description=None,
              percent_stats=None, notes=None):
    target = None
    for t in race["traits"]:
        if t.get("name") == old_name or (new_name and t.get("name") == new_name):
            target = t
            break
    if target is None:
        raise ValueError(f"Trait {old_name!r} not found on race {race['name']}")
    if new_name:
        target["name"] = new_name
    if description is not None:
        target["description"] = description
    if percent_stats is not None:
        if percent_stats:
            target["percentStats"] = percent_stats
        else:
            target.pop("percentStats", None)
    if notes is not None:
        target["notes"] = notes


def main():
    races = json.loads(RACES.read_text(encoding="utf-8"))

    # ---- Aasimar ----
    a = find_race(races, "Aasimar")
    a["fixedBonuses"]  = [{"stat": "WIS", "amount": 2}]
    a["choiceBonuses"] = [{"stat": "CON", "amount": 2},
                          {"stat": "CHA", "amount": 2}]
    set_trait(a, "Celestial Superiority", new_name="Celestial Legacy",
              percent_stats={},
              notes="Stats need in-game verification - old data was attached to a different trait name.")
    set_trait(a, "Celestial Presence", new_name="Healing Hands",
              percent_stats={},
              notes="Stats need in-game verification - old data was attached to a different trait name.")

    # ---- Gith ----
    g = find_race(races, "Gith")
    set_trait(g, "Gith Endurance", new_name="Decentralized Mind",
              description="Bonus to Control Resist.",
              percent_stats={},
              notes="Exact Control Resist amount needs in-game verification.")
    set_trait(g, "Gith Advantage", new_name="Githborn Discipline",
              percent_stats={},
              notes="Stats need in-game verification - old +5% Combat Advantage was attached to a different trait name.")

    # ---- Dwarf ----
    d = find_race(races, "Dwarf")
    set_trait(d, "Cast-Iron", new_name="Cast-Iron Stomach")

    # ---- Half-Elf ----
    he = find_race(races, "Half-Elf")
    set_trait(he, "Dilettante",
              description="Grants +2 Ability Score. This bonus is automatically determined by your class.")
    set_trait(he, "Knack for Success",
              description="+3% Critical Severity, +3% Deflect, and +3% Gold Bonus.",
              percent_stats={"Critical Severity": 3, "Deflect": 3, "Gold Bonus": 3})

    # ---- Half-Orc ----
    ho = find_race(races, "Half-Orc")
    set_trait(ho, "Furious Assault",
              description="Bonus Critical Severity on first hit of an encounter power.")

    # ---- Tiefling ----
    t = find_race(races, "Tiefling")
    set_trait(t, "Bloodhunt",
              description="+5% damage to targets below 50% HP.")
    set_trait(t, "Infernal Wrath",
              description="10% chance on taking damage to reduce attacker's damage by 5% for 5s.")

    # ---- Sun Elf ----
    s = find_race(races, "Sun Elf")
    set_trait(s, "Inner Calm",
              description="+5% Action Point Gain.",
              percent_stats={"Action Point Gain": 5})
    set_trait(s, "Sun Elf Grace",
              description="+25% Control Resist.",
              percent_stats={"Control Resist": 25})

    RACES.write_text(json.dumps(races, indent=2, ensure_ascii=False), encoding="utf-8")
    print("Applied NW Hub-verified updates to: Aasimar, Gith, Dwarf, Half-Elf, Half-Orc, Tiefling, Sun Elf")


if __name__ == "__main__":
    main()
