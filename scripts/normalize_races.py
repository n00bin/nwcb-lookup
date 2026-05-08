#!/usr/bin/env python3
"""Normalize data/races.json schema:

- fixedBonuses / choiceBonuses: always list of {stat, amount} objects.
  stat can be a string (single stat) or list (multi-choice / "any").
- premium: boolean (None -> false).
- traits: always list of objects with at least {name}. String traits
  become {name: "X"}. Rich traits keep description/percentStats.

Idempotent.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RACES = ROOT / "data" / "races.json"


def normalize_bonuses(b):
    """Accepts:
      - dict like {"DEX": 2, "STR": 1}
      - list of {stat, amount} objects
      - empty / None
    Returns list of {stat, amount} objects (stat can be str or list)."""
    if not b:
        return []
    if isinstance(b, dict):
        return [{"stat": k, "amount": v} for k, v in b.items()]
    if isinstance(b, list):
        out = []
        for item in b:
            if isinstance(item, dict):
                out.append({"stat": item["stat"], "amount": item["amount"]})
        return out
    return []


def normalize_traits(t):
    if not t:
        return []
    out = []
    for item in t:
        if isinstance(item, str):
            out.append({"name": item})
        elif isinstance(item, dict):
            entry = {"name": item.get("name", "")}
            if "description" in item:
                entry["description"] = item["description"]
            if item.get("percentStats"):
                entry["percentStats"] = item["percentStats"]
            if "notes" in item:
                entry["notes"] = item["notes"]
            out.append(entry)
    return out


def main():
    races = json.loads(RACES.read_text(encoding="utf-8"))
    for r in races:
        r["fixedBonuses"] = normalize_bonuses(r.get("fixedBonuses"))
        r["choiceBonuses"] = normalize_bonuses(r.get("choiceBonuses"))
        r["premium"] = bool(r.get("premium")) if r.get("premium") is not None else False
        r["traits"] = normalize_traits(r.get("traits"))

    RACES.write_text(json.dumps(races, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Normalized {len(races)} races.")
    # Quick sanity print
    for r in races:
        n = len(r["fixedBonuses"]) + len(r["choiceBonuses"])
        t = len(r["traits"])
        prem = " [premium]" if r["premium"] else ""
        print(f"  {r['name']:25s}{prem}  bonuses: {n}  traits: {t}")


if __name__ == "__main__":
    main()
