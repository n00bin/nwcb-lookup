"""Backfill 4 confident Warlock old weapon orphans based on sibling matches."""
import json
from pathlib import Path

PATH = Path("G:/ai_projects/nwcb/data/gear.json")
data = json.loads(PATH.read_text(encoding="utf-8"))

# (id, set, source, note)
TARGETS = {
    192: ("Stronghold Unity", "Stronghold Guild Marketplace",
          "Set classified 2026-05-17 — sibling Stronghold Mace IL 600 (id 2533) in Stronghold Unity; n00b ack."),
    174: ("Weapons of the Hexweaver", "Sea of Moving Ice (Module 10) / Royal Allies",
          "Set classified 2026-05-17 — 8 Hexweaver siblings (Pact Blade + Grimoire, Uncommon-Legendary tiers) all in Weapons of the Hexweaver; n00b ack."),
    183: ("Masterwork III Weapon Set", "Masterwork Crafting (Module 13) / Stronghold",
          "Set classified 2026-05-17 — Obsidian Tecpatl Legendary IL 800 (id 3729) in Masterwork III Weapon Set; n00b ack. IL 775 is intermediate tier."),
    197: ("Vistani", "Ravenloft Campaign / Vistani Camp",
          "Set classified 2026-05-17 — 8 Vistani Mace+Shield siblings (IL 350/500/650/800) in Vistani set; n00b ack."),
}

for it in data:
    if it["id"] in TARGETS:
        set_name, source, note = TARGETS[it["id"]]
        it["set"] = set_name
        it["setSize"] = 2
        it["source"] = source
        it["notes"] = note
        print(f"  Backfilled id={it['id']:>5}  {it.get('name')!r:42} -> set: {set_name!r}")

PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nTotal items: {len(data)}.")
