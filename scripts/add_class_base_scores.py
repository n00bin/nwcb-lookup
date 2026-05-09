#!/usr/bin/env python3
"""Add verified `baseAbilityScores` to each class in data/classes.json.

Source: NW Hub character editor screenshots from n00b 2026-05-08.
Order: STR / CON / DEX / INT / WIS / CHA. Sum = 74 for all classes.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data" / "classes.json"

BASE_SCORES = {
    "Barbarian": {"str": 18, "con": 14, "dex": 14, "int":  8, "wis": 10, "cha": 10},
    "Bard":      {"str": 10, "con": 12, "dex": 14, "int": 12, "wis": 10, "cha": 16},
    "Cleric":    {"str": 10, "con": 10, "dex": 10, "int": 15, "wis": 16, "cha": 13},
    "Fighter":   {"str": 16, "con": 16, "dex": 14, "int":  8, "wis": 10, "cha": 10},
    "Paladin":   {"str":  8, "con": 12, "dex": 10, "int": 12, "wis": 14, "cha": 18},
    "Ranger":    {"str": 16, "con": 12, "dex": 16, "int": 10, "wis":  8, "cha": 12},
    "Rogue":     {"str": 13, "con": 13, "dex": 18, "int":  8, "wis": 10, "cha": 12},
    "Warlock":   {"str":  8, "con": 14, "dex": 12, "int": 16, "wis":  8, "cha": 16},
    "Wizard":    {"str":  8, "con": 10, "dex": 12, "int": 18, "wis": 14, "cha": 12},
}


def main():
    data = json.loads(PATH.read_text(encoding="utf-8"))
    for cls in data:
        scores = BASE_SCORES.get(cls["name"])
        if not scores:
            print(f"  WARN: no base scores for {cls['name']}")
            continue
        cls["baseAbilityScores"] = scores
    PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Updated {len(BASE_SCORES)} classes with baseAbilityScores.")
    for name, s in BASE_SCORES.items():
        total = sum(s.values())
        print(f"  {name:10s} {s['str']:>2}/{s['con']:>2}/{s['dex']:>2}/{s['int']:>2}/{s['wis']:>2}/{s['cha']:>2}  = {total}")


if __name__ == "__main__":
    main()
