"""v2 update — fill in all remaining Fighter powers/encounters/dailies/class features/feats."""
import json
from pathlib import Path

CLASSES = Path("G:/ai_projects/nwcb/data/classes.json")
data = json.loads(CLASSES.read_text(encoding="utf-8"))
fighter = next(c for c in data if c["name"] == "Fighter")

# Expand base shared powers
fighter["powers"]["atWill"].append(
    {"name": "Cleave", "type": "atWill", "magnitude": 55, "castSeconds": 0.5, "rangeMelee": True, "arc": 200, "notes": "Threefold attack to enemies in cone before you."}
)
fighter["powers"]["encounter"].extend([
    {"name": "Shield Slam", "type": "encounter", "magnitude": 350, "castSeconds": 0.7, "cooldownByParagon": {"Vanguard": 12.9, "Dreadnought": 13.0}, "range": 30, "radius": 10, "addedEffect": "Knock Down", "notes": "Deal physical damage to enemies in a line."},
    {"name": "Knee Breaker", "type": "encounter", "magnitude": 700, "castSeconds": 0.55, "cooldownSeconds": 14.8, "rangeMelee": True, "durationSeconds": 8, "addedEffect": "Slow", "notes": "Deal physical damage to target."},
    {"name": "Bull Charge", "type": "encounter", "magnitude": 520, "castSeconds": 0.65, "cooldownSeconds": 11.1, "range": 60, "addedEffect": "Knock Back", "notes": "Lunge at target dealing physical damage."}
])
# Update Shield Throw to reflect Dreadnought bounce variant
for e in fighter["powers"]["encounter"]:
    if e["name"] == "Shield Throw":
        e["notes"] = "Projectile to target enemy. Stuns target for 3s. Bounces to up to 3 nearby enemies (Dreadnought variant)."
        e["durationSeconds"] = 3
        e["cooldownByParagon"] = {"Vanguard": 5.5, "Dreadnought": 11.1}

# Update mechanics (rename Forge Ahead from base to Block, add Dig In)
fighter["powers"]["mechanic"] = [
    {"name": "Block", "type": "mechanic", "tactical": True, "castSeconds": 0, "range": "Self", "notes": "Raise shield, absorbs damage from front (40% Max HP). Drains stamina. Immunity to Control Effects. Ends when stamina depleted."},
    {"name": "Forge Ahead", "type": "mechanic", "tactical": True, "castSeconds": 0, "range": "Self", "notes": "Raise shield from front (10% Max HP absorb). First 1s: immune to most damage + 50% Movement Speed (3s CD). Ends when stamina depleted."},
    {"name": "Dig In", "type": "mechanic", "castSeconds": 0.1, "range": "Self", "addedEffect": "+15% Awareness + Immune to Control Effects", "notes": "Defensive position, absorbs 60% Max HP from all directions. Drains stamina. Does not end when stamina depleted."},
    {"name": "Seethe", "type": "mechanic", "castSeconds": 0.1, "range": "Self", "staminaCost": 1, "addedEffect": "Immune to Control + drains stamina + fills Vengeance Gauge", "notes": "Seethe with rage behind shield (50% Max HP absorb). May not move/attack."}
]

# Extend shared class features
fighter["classFeatures"] = [
    {"name": "Vigorous Strikes", "description": "Critical Strike +5% when stamina is full. Effect decreases as stamina decreases."},
    {"name": "Greater Endurance", "description": "Movement speed +10% whenever stamina gauge is full. Effect decreases as remaining stamina decreases."},
    {"name": "Shield Talent", "description": "Increases stamina regeneration.", "active": True},
    {"name": "Combat Superiority", "description": "Whenever you activate an encounter or daily, increase damage of at-will attacks by 10% for 10s.", "active": True}
]

# Extend general/skill feats
fighter["feats"] = [
    {"name": "Marathon Runner", "description": "Movement speed +10% when out of combat.", "type": "skill"},
    {"name": "Dungeoneering", "description": "Detect doors/triggers/traps, collect treasure from objects.", "type": "skill"},
    {"name": "Unshakable Shieldarm", "description": "Critical avoidance +10% while blocking.", "type": "skill"},
    {"name": "Tactician's Edge", "description": "Combat Advantage + Critical Strike +10% when stamina is full, +5% when stamina is empty. Effects decrease as stamina decreases.", "type": "skill"}
]

# ---- Vanguard paragon — expand
vang = next(p for p in fighter["paragonPaths"] if p["name"] == "Vanguard")
vang["daily"] = [
    {"name": "Bladed Rampart", "type": "daily", "paragon": True, "magnitude": 260, "castSeconds": 1.0, "actionPointCost": 1000, "range": "Self", "durationSeconds": 10, "addedEffect": "+30% Defense + deal physical damage to attackers when you take damage", "notes": "Defensive Daily."},
    {"name": "Phalanx", "type": "daily", "paragon": True, "castSeconds": 0.75, "actionPointCost": 1000, "radius": 16, "durationSeconds": 14, "addedEffect": "Immunity to most control + barrier around you reducing damage taken by allies within 20%", "notes": "Effect ends early upon guarding."}
]
vang["mechanic"] = [
    {"name": "Path of the Vanguard", "type": "mechanic", "paragon": True, "notes": "Threat generation greatly increased."},
    {"name": "Forte", "type": "mechanic", "paragon": True, "notes": "Paragon provides Defense increase, excels at Accuracy and Critical Avoidance."},
    {"name": "Retaliate", "type": "mechanic", "paragon": True, "magnitudeRange": [500, 800], "castSeconds": 1.0, "range": 20, "arc": 80, "notes": "When you release Dig In immediately after blocking, trigger Retaliate cone damage. Increased Threat. Once every 10s."}
]
vang["classFeatures"] = [
    {"name": "Ferocious Reaction", "description": "Deal physical damage (magnitude 25) to attackers whenever you deflect an attack.", "paragon": True},
    {"name": "Steel Recovery", "description": "Whenever you use an encounter or daily power, restore 5% of your stamina.", "paragon": True},
    {"name": "Anvil of Challenge", "description": "Anvil of Doom places you at top of target's threat list. May be charged; fully charged it will not place you at top.", "paragon": True, "active": True},
    {"name": "Enduring Warrior", "description": "Take 5% less damage when you are below 25% of Max HP.", "paragon": True}
]
vang["feats"] = [
    {"name": "Critical Deflection", "description": "Whenever you deflect, recover up to 10 stamina if Critical Strike rating matches/exceeds Deflect. Not while blocking. 3s CD.", "paragon": True},
    {"name": "Combat Balance", "description": "When not blocking, decrease damage taken by up to 10% if Critical Avoidance, Deflect, and Awareness ratings are equal.", "paragon": True},
    {"name": "Shieldthrower", "description": "Shield Throw generates additional threat, cooldown reduced to 6s, magnitude reduced to 325, no longer stuns targets.", "paragon": True},
    {"name": "Rising Tide", "description": "Tide of Iron grants Rising Tide: additional 25 magnitude physical damage on multi-enemy attacks for 3s.", "paragon": True},
    {"name": "Sharpened Senses", "description": "Bladed Rampart now grants 30% Awareness.", "paragon": True},
    {"name": "Shake It Off", "description": "Increases magnitude of Retaliate by up to 300 based on remaining stamina.", "paragon": True},
    {"name": "Deep Breathing", "description": "While under Dig In, every 3s gain Deep Breathing (10s): +4% damage and +4% healing received. Stacks up to 3 times.", "paragon": True},
    {"name": "Perfect Block", "description": "Determination allows blocking of most attacks without stamina, but 180s cooldown imposed on Determination.", "paragon": True},
    {"name": "Cleaving Bull", "description": "Bull Charge no longer knocks back targets; grants Cleaving Bull: +40 magnitude when attack strikes multiple enemies, 8s duration.", "paragon": True},
    {"name": "Staying Power", "description": "Enforced Threat now increases threat generation for 10 seconds.", "paragon": True}
]

# ---- Dreadnought paragon — expand
dread = next(p for p in fighter["paragonPaths"] if p["name"] == "Dreadnought")
dread["atWill"] = [
    {"name": "Heavy Slash", "type": "atWill", "paragon": True, "magnitude": 175, "castSeconds": 0.7, "rangeMelee": True, "durationSeconds": 12, "addedEffect": "+5% damage dealt", "notes": "Deal physical damage to target."},
    {"name": "Reave", "type": "atWill", "paragon": True, "magnitude": 60, "castSeconds": 0.4, "range": 45, "radius": 6, "notes": "Twofold ranged attack to enemies in a line."}
]
# Extend Dreadnought encounters with paragon-specific
dread["encounter"].extend([
    {"name": "Anvil of Doom (Dreadnought)", "type": "encounter", "paragon": True, "magnitude": 880, "enhancedMagnitude": 1360, "castSeconds": 0.86, "cooldownSeconds": 16.7, "rangeMelee": True, "notes": "Vengeance Gauge above 15: damage enhanced, cooldown -4s, consumes 15 vengeance."},
    {"name": "Commander's Strike", "type": "encounter", "paragon": True, "magnitude": 780, "castSeconds": 0.8, "cooldownSeconds": 16.7, "rangeMelee": True, "durationSeconds": 10, "addedEffect": "Increases target's vulnerability to physical damage by 10%", "notes": "Deal physical damage to target."},
    {"name": "Tremor", "type": "encounter", "paragon": True, "magnitude": 440, "castSeconds": 0.8, "cooldownSeconds": 14.8, "radius": 15, "notes": "Deal physical damage to nearby enemies."}
])
dread["classFeatures"] = [
    {"name": "Momentum", "description": "Bull Charge no longer knocks targets; +400 magnitude damage. Movement speed +20% after running for 2s. Effect ends when movement stops.", "paragon": True},
    {"name": "Plow the Road", "description": "Shield Slam deals an additional 200 magnitude damage and consumes 10 vengeance. No effect if Vengeance Gauge below 10.", "paragon": True},
    {"name": "Always Spiteful", "description": "At start of combat, if Vengeance Gauge is below 55, set to 55. (12s CD)", "paragon": True, "active": True},
    {"name": "Enduring Vengeance", "description": "Every 10s your Vengeance Gauge is above 50%, gain stack of Enduring Vengeance (+1% damage). Max 5 stacks. Ends when Vengeance below 50%.", "paragon": True}
]
dread["feats"] = [
    {"name": "Crushing Blows", "description": "20% chance on hit to deal a crushing blow consuming 5 vengeance for additional 150 magnitude damage. No effect if Vengeance below 5.", "paragon": True},
    {"name": "Ricochet", "description": "Shield Throw bounces to up to 3 nearby enemies (-10/-20/-30% damage). 10% chance on multi-target hit to allow Shield Throw without cooldown.", "paragon": True},
    {"name": "Landwaster", "description": "Earthshaker applies Landwaster when Vengeance Gauge > 50: allows executing Shockwave free by activating Earthshaker again, costs 50 vengeance. 3s duration.", "paragon": True},
    {"name": "Roiling Hatred", "description": "Whenever you critically strike, restore 2 vengeance.", "paragon": True},
    {"name": "Bloody Reprise", "description": "When Vengeance Gauge drops below 50%, gain Bloody Reprise (3s): next encounter sets Vengeance to 75.", "paragon": True},
    {"name": "Striker's Mark", "description": "Daily powers deal an additional 400 magnitude damage to targets affected by Commander's Strike or other Physical Vulnerability Up. Effect removed in this case.", "paragon": True},
    {"name": "Executioner's Cut", "description": "On using encounter, consume 5 vengeance to slice each target hit for 200 magnitude after 2s. Does not stack. No effect if Vengeance below 5.", "paragon": True},
    {"name": "Prepared Slam", "description": "Tremor gains effect of pulling nearby enemies towards you.", "paragon": True},
    {"name": "Weight of Vengeance", "description": "Anvil of Doom deals additional 480 magnitude damage, recovers 4s faster, consumes 15 vengeance. No effect if Vengeance below 15.", "paragon": True}
]

CLASSES.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print("Fighter powers v2 — comprehensive Vanguard + Dreadnought completion.")
