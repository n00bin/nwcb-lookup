"""
Scan gear.json (and adjacent data files) for equipBonuses that are
narrative-only — i.e., have name/description but no structured stat
fields the engine can apply.

A structured equipBonus has at least:
  - stat (string)
  - amount (number)
  - [optional] type, scope, perStack, maxStacks, alwaysActive, condition

A "narrative-only" equipBonus has name/description (or effectText) but
lacks stat OR amount. Those can't be applied by the engine.

Set entries that exist only as markers (no stat/amount but with setName)
are intentional and should NOT be flagged. Skip those.
"""
import json
import os
from collections import defaultdict

REPO = os.path.join(os.path.dirname(__file__), '..', '..')
DATA = os.path.join(REPO, 'data')

FILES = [
    'gear.json',
    'artifacts.json',
    'companion_gear.json',
    'mount_collars.json',
    'mount_combat_powers.json',
    'mount_equip_powers.json',
    'mount_insignia_bonuses.json',
    'overloads.json',
    'kits.json',
]

def is_set_marker(eb):
    """Set entries with only setName and no stat are marker-only (intentional)."""
    return eb.get('type') == 'Set' and eb.get('setName') and not eb.get('stat')

def is_structured(eb):
    """Has the fields the engine can act on."""
    return bool(eb.get('stat')) and eb.get('amount') is not None

def is_narrative(eb):
    """Has narrative text but isn't structured and isn't a set marker."""
    has_narrative = bool(eb.get('description') or eb.get('effectText') or eb.get('notes'))
    return has_narrative and not is_structured(eb) and not is_set_marker(eb)

findings = defaultdict(list)
total_items = 0
total_bonuses = 0
narrative_count = 0

for filename in FILES:
    path = os.path.join(DATA, filename)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list):
        continue
    for item in data:
        if not isinstance(item, dict):
            continue
        total_items += 1
        bonuses = item.get('equipBonuses') or []
        if not isinstance(bonuses, list):
            continue
        for eb in bonuses:
            if not isinstance(eb, dict):
                continue
            total_bonuses += 1
            if is_narrative(eb):
                narrative_count += 1
                name = item.get('name', '?')
                slot = item.get('slot') or item.get('collarSlot') or 'unknown'
                il = item.get('item_level', '?')
                bname = eb.get('name', '(unnamed)')
                desc = eb.get('description') or eb.get('effectText') or eb.get('notes', '')
                findings[filename].append({
                    'item_name': name,
                    'item_slot': slot,
                    'item_il': il,
                    'item_id': item.get('id'),
                    'bonus_name': bname,
                    'description': desc[:200],
                })

print(f'Scanned {total_items} items across {len(FILES)} files.')
print(f'Total equipBonuses checked: {total_bonuses}')
print(f'Narrative-only equipBonuses: {narrative_count}')
print()

for filename, items in findings.items():
    print(f'=== {filename}: {len(items)} narrative-only ===')
    # Group by bonus name (often same bonus exists on multiple items)
    by_bonus = defaultdict(list)
    for item in items:
        by_bonus[item['bonus_name']].append(item)
    for bonus_name in sorted(by_bonus.keys()):
        instances = by_bonus[bonus_name]
        print(f'  "{bonus_name}" — {len(instances)} item(s)')
        for inst in instances[:3]:
            print(f'    id {inst["item_id"]}: {inst["item_name"]} (IL {inst["item_il"]}, {inst["item_slot"]})')
        if len(instances) > 3:
            print(f'    ... and {len(instances) - 3} more')
        sample_desc = instances[0]['description']
        print(f'    Desc: {sample_desc}')
        print()
