import json
d = json.loads(open('G:/ai_projects/nwcb/data/gear.json', encoding='utf-8').read())
for it in d:
    if it.get("name") == "Echo of the Damned" and it.get("slot") == "Off Hand":
        print(f"--- id {it['id']} ---")
        print(f"  set: {it.get('set')}")
        print(f"  IL: {it.get('item_level')}")
        print(f"  classes: {it.get('allowedClasses')}")
        print(f"  ratingStats: {it.get('ratingStats')}")
        print(f"  source: {it.get('source')}")
        print(f"  notes: {it.get('notes')}")

# Also find item missing id
missing = [it for it in d if not it.get("id")]
print(f"\n--- {len(missing)} item(s) missing id ---")
for m in missing:
    print(json.dumps(m, indent=2, ensure_ascii=False))
