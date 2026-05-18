"""Bulk-backfill source for 70 confident ring orphan families.
Leaves 17 IL 1400/1650 class-themed rings flagged for verification."""
import json
import re
from collections import defaultdict
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

# (regex pattern, source, note tag)
FAMILIES = [
    (r"^Drowcraft",
     "Underdark Mount & Companion Affinity",
     "Drowcraft family (Mod 8 Underdark PvE per n00b)"),
    (r"^Dragonflight",
     "Stronghold Guild Marketplace (Rank 3)",
     "Dragonflight ring family (PvE)"),
    (r"^Lionsmane",
     "Stronghold Guild Marketplace",
     "Lionsmane Rings/Necklace (PvE per n00b — distinct from PvP Lionsmane armor set)"),
    (r"^Ring of Bel",
     "Avernus Campaign Store",
     "Ring of Bel +N (Avernus campaign)"),
    (r"^(Defending|Guiding|Leading|Striking|Piercing) Ring of",
     "Stronghold Guild Marketplace",
     "Stronghold 'Ring of the X' series (PvE)"),
    (r"^(Decaying|Withering|Sprouting|Moss|Vine|Prickly) Ring",
     "Underdark Adventure Zone",
     "Underdark plant/decay ring family"),
    (r"^(Pinched|Tapered|Split|Lead-plated|Copper-plated|Tin-plated|Nickel-plated|Gold-plated)",
     "Underdark Adventure Zone",
     "Underdark metal/coin ring family"),
    (r"^(Fish|Kuo-Toa|Merrow) Scale Ring",
     "Underdark Adventure Zone",
     "Underdark scale ring family"),
    (r"^(Stolen|Snatched|Taken) Ring",
     "Underdark Adventure Zone",
     "Underdark thief-themed ring family"),
    (r"^Tanner's",
     "Underdark Adventure Zone",
     "Tanner's Ring family (Underdark)"),
    (r"^(Rubellite|Sphene|Silverspruce|Scintillant)",
     "Sea of Moving Ice (Module 10)",
     "SoMI gemstone ring family"),
    (r"^(Beaded|Bronzewood|Lichstone)",
     "Tomb of the Nine Gods (Master)",
     "Tomb of 9 Gods crafted ring family"),
]

orphans = [it for it in data
           if not it.get("set") and not it.get("source")
           and it.get("slot") == "Ring"]

count_by_family = defaultdict(int)
updated = 0
for it in orphans:
    n = it.get("name", "")
    for pat, source, note in FAMILIES:
        if re.search(pat, n):
            it["source"] = source
            it["notes"] = f"Source classified 2026-05-18 — {note}; n00b ack bulk backfill."
            count_by_family[note] += 1
            updated += 1
            break

print(f"=== Backfill summary ===")
for fam, n in count_by_family.items():
    print(f"  {fam}: {n} items")
print(f"\nTotal updated: {updated} of {len(orphans)} ring orphans")

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
