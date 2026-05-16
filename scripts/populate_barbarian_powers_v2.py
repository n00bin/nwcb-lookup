"""v2 update — comprehensive Barbarian powers from full screenshot review."""
import json
from pathlib import Path

CLASSES = Path("G:/ai_projects/nwcb/data/classes.json")
data = json.loads(CLASSES.read_text(encoding="utf-8"))
barb = next(c for c in data if c["name"] == "Barbarian")

# Base shared Barbarian powers
barb["powers"] = {
    "atWill": [
        {"name": "Sure Strike", "type": "atWill", "magnitude": 60, "castSeconds": 0.45, "rangeMelee": True, "notes": "Fourfold attack to target enemy."},
        {"name": "Bounding Slam", "type": "atWill", "magnitude": 80, "rageMagnitude": 120, "castSeconds": 1.0, "range": 30, "radius": 10, "notes": "Lunge at target, damage to them and nearby enemies. More damage under Battlerage or Unstoppable."}
    ],
    "encounter": [
        {"name": "Not So Fast", "type": "encounter", "magnitude": 300, "castSeconds": 0.7, "cooldownSeconds": 10.9, "radius": 15, "durationSeconds": 6, "addedEffect": "Slow", "notes": "Deal physical damage to nearby enemies."},
        {"name": "Mighty Leap", "type": "encounter", "magnitude": 380, "castSeconds": 0.4, "cooldownSeconds": 13.6, "range": 50, "radius": 12, "notes": "Leap to target location, damage nearby enemies."},
        {"name": "Punishing Charge", "type": "encounter", "magnitude": 650, "castSeconds": 0.25, "cooldownSeconds": 13.6, "range": 60, "durationSeconds": 3, "addedEffect": "Stun", "notes": "Lunge at target enemy."},
        {"name": "Indomitable Battle Strike", "type": "encounter", "magnitudeRange": [800, 1200], "castSeconds": 1.1, "cooldownSeconds": 10.9, "rangeMelee": True, "notes": "Deal physical damage to target. Damage increases as your rage increases."},
        {"name": "Bloodletter", "type": "encounter", "magnitude": 600, "castSeconds": 0.73, "cooldownSeconds": 13.6, "rangeMelee": True, "addedEffect": "Absorbs damage dealt as hit points", "notes": "Deal physical damage to target enemy."}
    ],
    "daily": [
        {"name": "Savage Advance", "type": "daily", "magnitude": 1800, "castSeconds": 1.0, "actionPointCost": 1000, "range": 82, "addedEffect": "Knocks back any nearby enemies", "notes": "Lunge at target enemy."},
        {"name": "Spinning Strike", "type": "daily", "magnitude": 1400, "castSeconds": 1.3, "actionPointCost": 1000, "radius": 15, "addedEffect": "Control Immunity + +100% Movement Speed", "notes": "Deal physical damage to nearby enemies over 3 seconds. Effects end when power completes."},
        {"name": "Crescendo", "type": "daily", "magnitude": 2800, "castSeconds": 0.25, "actionPointCost": 1000, "range": 30, "durationSeconds": 3, "addedEffect": "Stun. Immune to control effects while attacking.", "notes": "Multi-hit combo to target enemy."}
    ],
    "mechanic": [
        {"name": "Block", "type": "mechanic", "tactical": True, "castSeconds": 0, "range": "Self", "addedEffect": "Immune to Control Effects + Gain 15% Critical Avoidance under Unstoppable", "notes": "Raise weapon, absorbs 40% Max HP from front. Drains stamina. Ends when stamina depleted."},
        {"name": "Unstoppable", "type": "mechanic", "castSeconds": 0, "range": "Self", "addedEffect": "Absorbs all damage (up to 60% Max HP) + Immune to Control", "notes": "Generates Rage from dealing/taking damage and kills. At 50% Rage, activate Unstoppable. Increases at-will speed, drains Rage over time. Damage taken depletes stamina."}
    ]
}

# Shared class features (already correct from v1; will keep)
# Note: Persistent Rage is a skill feat, leave as is

# ---- Sentinel paragon (Tank)
sent = next(p for p in barb["paragonPaths"] if p["name"] == "Sentinel")
sent["daily"] = [
    {"name": "Primal Instinct", "type": "daily", "paragon": True, "castSeconds": 1.0, "actionPointCost": 1000, "range": "Self", "durationSeconds": 10, "addedEffect": "+30% Awareness + 90% Critical Avoidance + Generate rage over time", "notes": "Defensive Daily."},
    {"name": "Battle High", "type": "daily", "paragon": True, "castSeconds": 1.0, "actionPointCost": 1000, "radius": 80, "durationSeconds": 10, "addedEffect": "+35% Max HP self (restore amount increased) + +15% Max HP nearby allies", "notes": "HP buff."}
]
sent["mechanic"] = [
    {"name": "Path of the Sentinel", "type": "mechanic", "paragon": True, "notes": "Threat generation greatly increased."},
    {"name": "Forte", "type": "mechanic", "paragon": True, "notes": "Paragon provides Defense increase, excels at Critical Severity and Awareness."}
]
sent["feats"].extend([
    {"name": "Disarming Takedown", "description": "Takedown increases target's damage taken from physical attacks by 5% for 10 seconds.", "paragon": True},
    {"name": "Crushing Advance", "description": "Savage Advance no longer knocks back, but reduces target's damage dealt by 12% for 12s.", "paragon": True},
    {"name": "Rage and Rally", "description": "Unstoppable now increases threat. When Unstoppable ends, restores up to 40% of max stamina based on duration.", "paragon": True},
    {"name": "Blood Fury", "description": "Primal Fury's Rage cost reduced to 30. While Unstoppable, Rage cost is 0 and it now restores HP equal to damage dealt.", "paragon": True},
    {"name": "Inspiring Bravado", "description": "Battle High now increases max HP of nearby allies by 15% for 10s.", "paragon": True},
    {"name": "Boasting Takedown", "description": "Takedown generates increased threat.", "paragon": True},
    {"name": "Leap into Action", "description": "Mighty Leap increases your threat generation for 10s.", "paragon": True}
])

# ---- Blademaster paragon (DPS)
bm = next(p for p in barb["paragonPaths"] if p["name"] == "Blademaster")
bm["atWill"] = [
    {"name": "Relentless Slash", "type": "atWill", "paragon": True, "magnitude": 55, "castSeconds": 0.8, "rangeMelee": True, "arc": 240, "durationSeconds": 12, "addedEffect": "Increases damage dealt by 5%", "notes": "Twofold attack to enemies in cone before you."},
    {"name": "Brash Strike", "type": "atWill", "paragon": True, "magnitude": 140, "castSeconds": 0.65, "rangeMelee": True, "notes": "Threefold attack to target enemy."}
]
bm["encounter"].extend([
    {"name": "Hidden Daggers", "type": "encounter", "paragon": True, "magnitude": 100, "castSeconds": 0.8, "cooldownSeconds": 7.2, "range": 40, "charges": 2, "addedEffect": "Surprise Attack: deals additional 150 magnitude on next attack that is not Hidden Daggers", "notes": "Slide backwards and deal projectile damage in a cone."},
    {"name": "Roar", "type": "encounter", "paragon": True, "magnitude": 290, "castSeconds": 0.61, "cooldownSeconds": 11.8, "range": 30, "arc": 45, "durationSeconds": 2, "addedEffect": "Stun + builds Rage per target hit", "notes": "Battle roar that interrupts enemies."},
    {"name": "Frenzy", "type": "encounter", "paragon": True, "magnitude": 1275, "castSeconds": 1.1, "cooldownSeconds": 14.5, "range": 17, "notes": "Deal physical damage to target enemy."},
    {"name": "Axestorm", "type": "encounter", "paragon": True, "magnitude": 450, "castSeconds": 1.4, "cooldownSeconds": 13.6, "range": 50, "radius": 10, "notes": "Deal projectile damage to enemies in a line."}
])
bm["mechanic"] = [
    {"name": "Forte", "type": "mechanic", "paragon": True, "notes": "Paragon provides Power increase, excels at Critical Severity and Awareness."}
]

# Skill feat
barb["feats"] = [
    {"name": "Persistent Rage", "description": "Increases the rate at which you generate Rage.", "type": "skill"},
    {"name": "Dungeoneering", "description": "Detect doors/triggers/traps, collect treasure.", "type": "skill"},
    {"name": "Marathon Runner", "description": "Movement speed +10% out of combat.", "type": "skill"}
]

CLASSES.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print("Barbarian powers v2 — comprehensive Sentinel + Blademaster completion.")
