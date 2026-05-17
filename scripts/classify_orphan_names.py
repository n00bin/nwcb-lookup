"""Pattern-classify the 256 truly-unique orphans by name keyword to guess their set."""
import json
import re
from collections import defaultdict
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

def norm(s):
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return s

orphans = [it for it in data if not it.get("set") and not it.get("source")]
populated = [it for it in data if (it.get("set") or it.get("source"))]
pop_index = defaultdict(list)
for it in populated:
    pop_index[(it.get("slot"), norm(it.get("name", "")))].append(it)

unique_orphans = [o for o in orphans if not pop_index.get((o.get("slot"), norm(o.get("name", ""))))]

# Pattern-classify by name keyword
patterns = [
    (r"\bbloodwoven\b",                "Bloodwoven (Mod 27 Thay shirt/pants)"),
    (r"\bbloodwrought\b|\bbloodforged\b",  "Bloodforged / Crimson Gale (Mod 27)"),
    (r"\bcrimson march\b|\bzulkirs?\b|\benthraller\b", "Crimson March/Doomed Reaver (Mod 27)"),
    (r"\bdepthweave\b|\bdepthcured\b", "Enchanted Depths/Depthweave (Mod 14 Sea of Moving Ice)"),
    (r"\bvoidcaller\b",                 "Voidcaller's Gear"),
    (r"\bencased magma\b|\bmagma infused\b", "Living Magma (Mountain of Flame)"),
    (r"\bthayan zealot\b|\bumbral\b",  "Umbral Stride (Thay)"),
    (r"\brunes of the (avowed|pledged|sworn|oathbound|covenant|promised)\b",
                                        "Paladin Runes (campaign pants)"),
    (r"\bfaulty\b|\bcorrupted\b|\bpetrified\b|\bdefunct\b|\brusted\b",
                                        "Mod 4 Tyranny artifact weapon reagents"),
    (r"\bdoomscript\b|\bprofaned\b",   "Doom Cult / Profane (Mod 27 Thay weapons)"),
    (r"\bsoul collector\b|\bsoul harvest\b", "Soul Harvest / Soul Collector (Mod 27)"),
    (r"\bskyhold\b|\bbloodbrass\b",    "Pirates' Skyhold (Skyhold Arms)"),
    (r"\bperfect (nail|claws?) of lolth\b|\bdemonweb\b", "Demonweb Empowerment / Demonweb Pits"),
    (r"\bxaryxian\b|\bpeer into the void\b", "Peer Into the Void (Imperial Citadel)"),
    (r"\bstronghold\b|\bgrand alliance\b|\bcompany\b", "Stronghold / Guild gear"),
    (r"\bblack ice\b|\bdrake\b",        "Black Ice / Drake"),
    (r"\bcrystalline\b|\bbismuth\b|\bcrystal (rapier|lute)\b", "Crystalline / Prismatic Defier (Dread Sanctum)"),
    (r"\bnautili\b|\bsword coast\b",   "Sword Coast / Nautili"),
    (r"\barchmage\b|\bmage('s)? robe\b", "Archmage / Mage gear"),
    (r"\bbarovian\b|\bravenloft\b",    "Barovian (Ravenloft)"),
    (r"\bvistani\b",                    "Vistani"),
    (r"\baberration\b|\bxaryxis\b",    "Xaryxis Reach (Mod 26)"),
]

bucket_counts = defaultdict(list)
unmatched = []
for o in unique_orphans:
    n = norm(o.get("name", ""))
    matched = False
    for pat, label in patterns:
        if re.search(pat, n):
            bucket_counts[label].append(o)
            matched = True
            break
    if not matched:
        unmatched.append(o)

print(f"=== Pattern classification of {len(unique_orphans)} unique orphans ===\n")
total_matched = sum(len(v) for v in bucket_counts.values())
print(f"Matched a known pattern: {total_matched}  ({100*total_matched/len(unique_orphans):.0f}%)")
print(f"Unmatched (need manual review): {len(unmatched)}\n")

for label, items in sorted(bucket_counts.items(), key=lambda x: -len(x[1])):
    print(f"  {label}:  {len(items)} items")
print()

# Show sample of unmatched
print(f"=== Sample of unmatched orphans (first 30) ===")
for o in unmatched[:30]:
    print(f"  id={o['id']:>5}  {o.get('slot'):>8}  IL={o.get('item_level')!s:>5}  {o.get('name')!r:55}")
print(f"  ... and {len(unmatched)-30 if len(unmatched) > 30 else 0} more")
