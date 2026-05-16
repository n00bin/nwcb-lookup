"""Populate Rogue powers in classes.json from 388 power-screen screenshots (2026-05-15 intake).

Covers:
- Base shared powers (atWill/encounter/daily/mechanic)
- Whisperknife paragon: 2 atWills, 5 encounters, 2 dailies, paragon class features, paragon feats
- Assassin paragon: 2 atWills, 5 encounters, 2 dailies, paragon class features, paragon feats

Magnitudes/cooldowns that differ per paragon use byParagon dicts (mirroring Bard pattern).
"""
import json
from pathlib import Path

CLASSES = Path("G:/ai_projects/nwcb/data/classes.json")
data = json.loads(CLASSES.read_text(encoding="utf-8"))

rogue = next(c for c in data if c["name"] == "Rogue")

# ---- Base shared Rogue powers (apply to both paragons unless overridden)
rogue["powers"] = {
    "atWill": [
        {
            "name": "Cloud of Steel",
            "type": "atWill",
            "magnitudeByParagon": {"Whisperknife": 60, "Assassin": 45},
            "castSeconds": 0.4,
            "range": 50,
            "durationSeconds": 5,
            "notes": "Toss blades at target dealing physical damage. Each strike that hits increases damage they take from Cloud of Steel by 5% (Whisperknife) / 2.5% (Assassin), stacking up to 10 times."
        },
        {
            "name": "Sly Flourish",
            "type": "atWill",
            "magnitude": 40,
            "castSeconds": 0.26,
            "rangeMelee": True,
            "notes": "A distracting flourish of your blades deal damage to your target with increasing magnitude throughout the combo."
        }
    ],
    "encounter": [
        {
            "name": "Blade Flurry",
            "type": "encounter",
            "magnitude": 330,
            "castSeconds": 0.45,
            "cooldownSeconds": 11,
            "radius": 15,
            "notes": "Spin and lash out with your weapons. Stealth: Radius +10' and power doesn't go on cooldown."
        },
        {
            "name": "Lashing Blade",
            "type": "encounter",
            "magnitude": 715,
            "castSeconds": 1.0,
            "cooldownSeconds": 11,
            "rangeMelee": True,
            "notes": "Focus your strength into one furious attack. Stealth: Adds another 300 Magnitude hit."
        },
        {
            "name": "Path of the Blade",
            "type": "encounter",
            "magnitude": "140x4",
            "castSeconds": 0.8,
            "cooldownSeconds": 14.7,
            "range": "Self",
            "durationSeconds": 6,
            "notes": "Summon an upheaval of blades around you. Stealth: Pulses twice as fast for half duration."
        },
        {
            "name": "Smoke Bomb",
            "type": "encounter",
            "magnitude": "120x4",
            "castSeconds": 0.5,
            "cooldownByParagon": {"Whisperknife": 14.1, "Assassin": 13.4},
            "rangeMelee": True,
            "radius": 20,
            "addedEffect": "Daze 4s",
            "notes": "Poison damage + Daze. Stealth: You and allies gain Combat Advantage against enemies inside the bomb."
        },
        {
            "name": "Bait and Switch",
            "type": "encounter",
            "castSeconds": 0.65,
            "cooldownByParagon": {"Whisperknife": 22.6, "Assassin": 21.4},
            "range": "Self",
            "notes": "Jump back, dropping a decoy with 50% Max HP. Decoy taunts enemies within 20'. Gain Action Points when decoy is hit. Bosses cannot be tricked. Stealth: Refills Stealth, no jump back, no stealth removal."
        }
    ],
    "daily": [
        {
            "name": "Hateful Knives",
            "type": "daily",
            "magnitude": 2000,
            "castSeconds": 1.8,
            "actionPointCost": 1000,
            "range": 82,
            "addedEffect": "Prone + Combat Advantage 6s",
            "notes": "Dash, knock Prone with upward strike, hurl two daggers before landing."
        },
        {
            "name": "Whirlwind of Blades",
            "type": "daily",
            "magnitude": 450,
            "castSeconds": 1.5,
            "actionPointCost": 1000,
            "radius": 30,
            "durationSeconds": 10,
            "addedEffect": "Increases damage by 3% per enemy hit (up to 5)",
            "notes": "Whip daggers around you dealing damage to nearby enemies."
        },
        {
            "name": "Courage Breaker",
            "type": "daily",
            "magnitude": 1800,
            "castSeconds": 2.0,
            "actionPointCost": 1000,
            "range": 45,
            "durationSeconds": 8,
            "addedEffect": "Lower target attack damage 15%. Slow 70% (ignores control immunity).",
            "notes": "Teleport to target and shatter their courage with a series of powerful attacks."
        }
    ],
    "mechanic": [
        {
            "name": "Roll",
            "type": "mechanic",
            "tactical": True,
            "castSeconds": 0,
            "notes": "Quickly dodge in running direction, briefly immune to damage and control. Activated while moving."
        },
        {
            "name": "Stealth",
            "type": "mechanic",
            "castSeconds": 0,
            "cooldownSeconds": 0.4,
            "durationSeconds": 6,
            "notes": "Enter Stealth to move undetected. Combat Advantage vs unaware targets. Encounter powers gain new effects."
        },
        {
            "name": "Forte",
            "type": "mechanic",
            "addedEffect": "Power increase + excels at Combat Advantage and Deflect Severity",
            "notes": "Paragon-specific increase. Works automatically, not slotted in HUD."
        }
    ]
}

# ---- Class Features (shared)
rogue["classFeatures"] = [
    {"name": "Thievery", "description": "You can see and disarm traps, preventing damage or getting stuck. Collect and sell treasure from special thievery objects.", "notes": "Auto-applied skill."},
    {"name": "Skillful Infiltrator", "description": "Increases Movement Speed by 10%. Adds 2.5% Deflect and Critical Strike.", "type": "classFeature"},
    {"name": "Sneak Attack", "description": "Increases Movement Speed by 15% and increases cooldown rate of powers by 10% while Stealthed.", "type": "classFeature", "active": True},
    {"name": "Tenacious Concealment", "description": "Increases Stealth regeneration by +50%.", "type": "classFeature"},
    {"name": "Tactics", "description": "Increases Action Point Gain by 10%.", "type": "classFeature"}
]

# ---- General Feats (skill/racial)
rogue["feats"] = [
    {"name": "Swift Footwork", "description": "Your Stamina regenerates 5% faster.", "type": "skill"},
    {"name": "Cunning Ambusher", "description": "You deal 10% more damage for 5 seconds after leaving Stealth.", "type": "skill"},
    {"name": "Scoundrel Training", "description": "You gain 2% Combat Advantage.", "type": "skill"}
]

# ---- Whisperknife paragon
whisper = next(p for p in rogue["paragonPaths"] if p["name"] == "Whisperknife")
whisper["atWill"] = [
    {
        "name": "Disheartening Strike",
        "type": "atWill",
        "paragon": True,
        "magnitude": 75,
        "castSeconds": 0.9,
        "range": 50,
        "addedEffect": "DoT magnitude 450 over 10s + increases target's damage taken from projectile and physical attacks by 5% for 10s",
        "notes": "Fling a dagger at target with extreme precision."
    },
    {
        "name": "Shuriken Toss",
        "type": "atWill",
        "paragon": True,
        "magnitude": 60,
        "castSeconds": 0.53,
        "range": 50,
        "notes": "Throw a shuriken that ricochets to 2 additional targets."
    }
]
whisper["encounter"] = [
    {"name": "Vengeance's Pursuit", "type": "encounter", "paragon": True, "magnitudeInitial": 200, "magnitudeFollowUp": 250, "castSeconds": 0.7, "cooldownSeconds": 9.4, "range": 50, "durationSeconds": 8, "addedEffect": "Vengeance: target outgoing damage -5%", "notes": "Designate target. Re-activate to break control and teleport. Stealth: doesn't break Stealth; follow-up becomes single-target 715 mag + Stun 1s."},
    {"name": "Blitz", "type": "encounter", "paragon": True, "magnitude": 450, "castSeconds": 0.9, "cooldownSeconds": 13.2, "range": 50, "arc": 90, "notes": "Throw a fan of blades in front. Stealth: Recharges encounter cooldowns by 2s."},
    {"name": "Impact Shot", "type": "encounter", "paragon": True, "magnitude": 600, "castSeconds": 0.9, "cooldownSeconds": 9.4, "range": 50, "notes": "Strike opponent with extreme force. Stealth: Stuns target for 2s."},
    {"name": "Shadow Strike", "type": "encounter", "paragon": True, "magnitude": 775, "castSeconds": 1.0, "cooldownSeconds": 13.2, "range": 50, "durationSeconds": 10, "addedEffect": "Refills 20% Stealth on hit + target takes +5% damage from projectile/physical for 10s", "notes": "Whip a shadowy dagger. Stealth: doesn't remove Stealth, Dazes 3s."},
    {"name": "Shadowy Disappearance", "type": "encounter", "paragon": True, "magnitude": "300x2", "castSeconds": 0.6, "cooldownSeconds": 13.2, "range": 50, "radius": 10, "addedEffect": "Stealth 1.5s", "notes": "Vanish and teleport. Foes near exit and entry take damage. Stealth: doesn't remove Stealth."}
]
whisper["daily"] = [
    {"name": "Killing Storm", "type": "daily", "paragon": True, "magnitude": "200x12", "castSeconds": 0.2, "actionPointCost": 1000, "range": "Self", "durationSeconds": 10, "addedEffect": "-5% Awareness to target", "notes": "Vanish then perform a series of dash attacks in a small area."},
    {"name": "Lurker's Assault", "type": "daily", "paragon": True, "castSeconds": 0.5, "actionPointCost": 1000, "range": 80, "durationSeconds": 10, "addedEffect": "+40% Damage Boost", "notes": "Lurk through the shadows. Stealth meter regenerates very quickly. Teleport to target if targeting a foe."}
]
whisper["classFeatures"] = [
    {"name": "Dagger Threat", "description": "Your ranged attacks deal up to 10% more damage based on how close you are. Maximum benefit within 20'.", "paragon": True, "active": True},
    {"name": "Razor Action", "description": "When you activate a daily power you fling daggers up to 30' doing 300 magnitude damage and increasing your speed by 2% per target hit (max 10%).", "paragon": True},
    {"name": "Advantageous Position", "description": "For 2 seconds after leaving Stealth, maintain Combat Advantage and take 20% reduced damage from AoE/ranged.", "paragon": True},
    {"name": "Talisman of Shadows", "description": "When you enter stealth, Daze and Slow all foes in a 20' area for 1 second.", "paragon": True}
]
whisper["feats"] = [
    {"name": "Last Moments", "description": "Your at-will, encounter, and daily powers deal up to 10% more damage to foes as their health diminishes. Doubled in Stealth.", "paragon": True},
    {"name": "Dark Reimbursement", "description": "When you use an encounter power to leave stealth, you regain 25% Stealth.", "paragon": True},
    {"name": "One with the Shadows", "description": "Every 12s gain One with the Shadows: next Encounter refills half your Stealth Meter.", "paragon": True},
    {"name": "Shadow of Demise", "description": "While in Stealth, encounter powers add Shadow of Demise (5s) — 40% of damage you deal to target is dealt again when it expires.", "paragon": True},
    {"name": "Ambusher's Haste", "description": "While Stealthed, powers deal up to 40% more damage based on how full your Stealth meter is.", "paragon": True},
    {"name": "Gutterborn's Touch", "description": "Using an At-Will/Encounter/Daily on a target with Combat Advantage grants Gutterborn (5s): ranged powers deal 10% more damage.", "paragon": True},
    {"name": "Shadowy Opportunity", "description": "When leaving Stealth, gain Shadowy Opportunity (5s): each hit deals an additional 130 magnitude damage.", "paragon": True},
    {"name": "Return to Shadows", "description": "When activating an encounter, refill 7.5% Stealth per target hit (10% behind target). Cannot gain Stealth while stealthed.", "paragon": True},
    {"name": "Hidden Attacks", "description": "At-Will powers now drain 10% Stealth meter (down from 15%), Stealth regeneration +50%.", "paragon": True},
    {"name": "Shady Preparations", "description": "Entering Stealth reduces all your cooldowns by 2 seconds.", "paragon": True}
]

# ---- Assassin paragon
assassin = next(p for p in rogue["paragonPaths"] if p["name"] == "Assassin")
assassin["atWill"] = [
    {"name": "Duelist's Flurry", "type": "atWill", "paragon": True, "magnitude": 35, "castSeconds": 0.15, "rangeMelee": True, "durationSeconds": 9, "addedEffect": "Each flurry hit has a chance to apply Bleed (stacks up to 10)", "notes": "Strike with two slashes followed by a flurry of attacks."},
    {"name": "Gloaming Cut", "type": "atWill", "paragon": True, "magnitude": 150, "castSeconds": 1.1, "range": 20, "durationSeconds": 8, "addedEffect": "+50% Stealth regeneration", "notes": "Dash forward with shadowy cross slash. Up to 100% more damage based on target's missing health. Kills grant 20% Stealth bar."}
]
assassin["encounter"] = [
    {"name": "Impossible to Catch", "type": "encounter", "paragon": True, "castSeconds": 0, "cooldownSeconds": 17.8, "range": "Self", "durationSeconds": 4, "addedEffect": "Control Immunity + 10% Deflect", "notes": "Break free of most control. Stealth: +25% Movement Speed and +10% Defense for the duration."},
    {"name": "Deft Strike", "type": "encounter", "paragon": True, "magnitude": 800, "castSeconds": 0.9, "cooldownSeconds": 12.5, "range": 60, "durationSeconds": 3, "addedEffect": "Slow", "notes": "Dash behind enemy and stab. Stealth: Range to 60' + teleport to friendly targets."},
    {"name": "Wicked Reminder", "type": "encounter", "paragon": True, "magnitude": 800, "castSeconds": 0.5, "cooldownSeconds": 16.1, "rangeMelee": True, "durationSeconds": 10, "addedEffect": "Target takes +10% damage from physical attacks", "notes": "Pierce enemy's armor. Stealth: Also reduces target's Critical Avoidance by 5% for 10s."},
    {"name": "Dazing Strike", "type": "encounter", "paragon": True, "magnitude": 350, "castSeconds": 0.45, "cooldownSeconds": 8.9, "rangeMelee": True, "arc": 130, "durationSeconds": 4, "addedEffect": "Combat Advantage + Daze + Interrupt", "notes": "Snap into the air with crushing head blow. Stealth: Magnitude 500."},
    {"name": "Assassinate", "type": "encounter", "paragon": True, "magnitude": 845, "castSeconds": 0.95, "cooldownSeconds": 13.7, "rangeMelee": True, "notes": "Quickly strike, dealing physical damage and interrupting. 25% stronger from behind. Stealth: 25% stronger from any direction."}
]

CLASSES.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Updated Rogue powers in classes.json — base + Whisperknife + Assassin (partial). Both paragons need daily review.")
