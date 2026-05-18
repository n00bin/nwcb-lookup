"""Show remaining orphan rings after PvP deletions, grouped by family."""
import json
import re
from collections import defaultdict
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

orphans = [it for it in data
           if not it.get("set") and not it.get("source")
           and it.get("slot") == "Ring"]
print(f"Total remaining orphan rings: {len(orphans)}\n")

# Family detection
FAMILIES = [
    ("Drowcraft", r"^Drowcraft"),
    ("Dragonflight", r"^Dragonflight"),
    ("Lionsmane", r"^Lionsmane"),
    ("Rubellite/Sphene/Silverspruce/Scintillant (SoMI gemstones)",
     r"^(Rubellite|Sphene|Silverspruce|Scintillant)"),
    ("Beaded/Bronzewood/Lichstone (Tomb of 9 Gods crafted)",
     r"^(Beaded|Bronzewood|Lichstone)"),
    ("'Ring of the X' series (Stronghold PvE)",
     r"^(Defending|Guiding|Leading|Striking|Piercing) Ring of"),
    ("'Ring of the Forest/Rose/Ivy' (Underdark)",
     r"Ring of (the Forest|the Rose|Ivy|the Soldier|the Squire|the Knight|the Sentry|the Guard|the Warden|the Scout|the Mentor|the Herald|the Archer|the Travel|the Squire|the Urchin|the Thief|the Criminal|the Bandit)"),
    ("Underdark gemstone-style rings (Pinched/Tapered/Split/Plated)",
     r"^(Pinched|Tapered|Split|Lead-plated|Copper-plated|Tin-plated|Nickel-plated|Gold-plated)"),
    ("Underdark thief-themed (Stolen/Snatched/Taken)",
     r"^(Stolen|Snatched|Taken) Ring"),
    ("Underdark plant/decay (Decaying/Withering/Sprouting/Moss/Vine/Prickly)",
     r"^(Decaying|Withering|Sprouting|Moss|Vine|Prickly|Fish|Kuo-Toa|Merrow) "),
    ("Tanner's Ring family", r"^Tanner's "),
    ("Ring of Bel +N (Avernus campaign)", r"^Ring of Bel"),
]

by_family = defaultdict(list)
for o in orphans:
    n = o.get("name", "")
    matched = False
    for family, pat in FAMILIES:
        if re.search(pat, n):
            by_family[family].append(o)
            matched = True
            break
    if not matched:
        by_family["(unmatched)"].append(o)

for family, items in by_family.items():
    items.sort(key=lambda x: (x.get("item_level") or 0, x.get("name", "")))
    print(f"\n=== {family} ({len(items)} items) ===")
    for it in items:
        print(f"  id={it['id']:>5}  IL={it.get('item_level'):>4}  {it.get('name')!r:50}  classes={it.get('allowedClasses')}")
