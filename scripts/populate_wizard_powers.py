"""Populate Wizard powers in classes.json from 2026-05-16 power-screen screenshots.

Covers:
- Base shared powers (atWill/encounter/daily/mechanic) — Magic Missile, Ray of Frost,
  Entangling Force, Repel, Ray of Enfeeblement, Icy Terrain, Shield, Arcane Singularity,
  Ice Knife, Oppressive Force, Teleport, Spell Mastery, Arcane Mastery, Chill, Control Mastery
- Class features shared: Orb of Imposition, Chilling Presence, Evocation, Arcane Presence
- Thaumaturge paragon: 2 atWills (Scorching Burst, Chilling Cloud), 3 encounters (Fanning the Flame,
  Icy Rays, Chill Strike, Conduit of Ice, Fireball), 2 dailies (Furious Immolation, Ice Storm),
  class features (Frost Wave, Combustive Action, Swath of Destruction, Critical Conflagration),
  Smolder mechanic + Forte
- Arcanist paragon: 2 atWills (Storm Pillar, Arcane Bolt), encounters (Lightning Bolt, Disintegrate,
  Steal Time, Arcane Tempest, Arcane Conduit), dailies (Maelstrom of Chaos, Arcane Empowerment),
  class features (Eye of the Storm, Storm Spell, Storm Fury, Arcane Power Field), Forte
"""
import json
from pathlib import Path

CLASSES = Path("G:/ai_projects/nwcb/data/classes.json")
data = json.loads(CLASSES.read_text(encoding="utf-8"))

wizard = next(c for c in data if c["name"] == "Wizard")

# ---- Base shared Wizard powers
wizard["powers"] = {
    "atWill": [
        {"name": "Magic Missile", "type": "atWill", "magnitude": 60, "castSeconds": 0.35, "range": 80, "addedEffect": "Third cast strikes 3 times. Adds a stack of Arcane Mastery.", "notes": "Blast your enemy with arcane damage."},
        {"name": "Ray of Frost", "type": "atWill", "magnitude": 65, "castSeconds": 0.5, "range": 80, "addedEffect": "Adds a chill stack with each damage hit. Freezes the target at 6 chill stacks.", "notes": "Channel a powerful beam of frost at your target."}
    ],
    "encounter": [
        {"name": "Entangling Force", "type": "encounter", "magnitude": 600, "castSeconds": 0.4, "cooldownByParagon": {"Thaumaturge": 13.6, "Arcanist": 13.8}, "range": 80, "durationSeconds": 2, "addedEffect": "Hold", "notes": "Pull your enemy into the air and choke them. Each stack of Arcane Mastery increases duration by 0.1s."},
        {"name": "Repel", "type": "encounter", "magnitude": 580, "castSeconds": 0.05, "cooldownByParagon": {"Thaumaturge": 9.3, "Arcanist": 9.5}, "range": 80, "addedEffect": "Push", "notes": "Send a forceful blast pushing target away. Distance increased by Arcane Mastery stacks. Spell Mastery: Affects multiple targets with 300 magnitude damage."},
        {"name": "Ray of Enfeeblement", "type": "encounter", "magnitude": 520, "castSeconds": 0.34, "cooldownByParagon": {"Thaumaturge": 15.3, "Arcanist": 15.5}, "range": 80, "durationSeconds": 10, "addedEffect": "Decreases target's outgoing damage by 10%", "notes": "DoT to enemy. Spell Mastery: Increases target's damage taken from magical/projectile by 10% for 10s."},
        {"name": "Icy Terrain", "type": "encounter", "magnitude": 400, "castSeconds": 0.8, "cooldownByParagon": {"Thaumaturge": 16.2, "Arcanist": 16.4}, "radius": 15, "durationSeconds": 1.5, "addedEffect": "Roots targets initially + Chill stacks on ice", "notes": "Freeze the ground around you. Spell Mastery: Can cast at target location."},
        {"name": "Shield", "type": "encounter", "magnitude": 350, "castSeconds": 0.53, "cooldownByParagon": {"Thaumaturge": 15.3, "Arcanist": 15.1}, "range": "Self", "addedEffect": "Shield 30% Max HP. Push when depleted/recast. Pulse improved by Arcane Mastery.", "notes": "Spell Mastery: 40% Max HP shield, stronger pulse."}
    ],
    "daily": [
        {"name": "Arcane Singularity", "type": "daily", "magnitude": 1200, "castSeconds": 1.8, "actionPointCost": 1000, "range": 80, "radius": 42, "addedEffect": "Gain a stack of Arcane Mastery", "notes": "Create a powerful singularity that sucks in all enemies."},
        {"name": "Ice Knife", "type": "daily", "magnitude": 2300, "castSeconds": 1.0, "actionPointCost": 1000, "range": 80, "durationSeconds": 1.5, "addedEffect": "Knockdown + 3 stacks of chill to target", "notes": "Summon and slam down a huge blade of ice."},
        {"name": "Oppressive Force", "type": "daily", "magnitude": "200x2", "castSeconds": 0.9, "actionPointCost": 1000, "radius": 25, "durationSeconds": 1, "addedEffect": "Daze + Grants stack of Arcane Mastery. Additional Action: Explode (500 mag + Repel).", "notes": "Magnetic force that disables and explodes after delay."}
    ],
    "mechanic": [
        {"name": "Teleport", "type": "mechanic", "tactical": True, "castSeconds": 0, "range": "Self", "notes": "Quickly dodge the direction you are running, immune to damage and control. Activated while moving."},
        {"name": "Spell Mastery", "type": "mechanic", "notes": "Place an additional Encounter power into your R1 slot. Encounter powers in that slot deal increased damage and may have additional modifications. Auto-applied."},
        {"name": "Arcane Mastery", "type": "mechanic", "notes": "Always active. Casting Arcane spells builds stacks of Arcane Mastery (max 5), +0.5% Arcane damage per stack. Stacks last 8s. Grants additional effects on many Arcane powers."},
        {"name": "Chill", "type": "mechanic", "notes": "Always active. Cold spells Chill targets, Slowing them (max 6 stacks). Some Cold powers freeze max-stacked targets (Stun). Frozen targets recover sooner if they take enough damage."},
        {"name": "Control Mastery", "type": "mechanic", "notes": "Always active. Control effects (Stun/Root/Hold/Daze) are 2.5x as effective against non-player enemies."}
    ]
}

wizard["classFeatures"] = [
    {"name": "Orb of Imposition", "description": "Increase the duration of your control powers by 25%. Your control powers do 5% more damage against control immune targets."},
    {"name": "Chilling Presence", "description": "Increase the damage you deal by 0.5% for each stack of Chill on your target. This damage bonus is doubled on Frozen targets."},
    {"name": "Evocation", "description": "Increase the damage of your Area of Effect powers by 10%."},
    {"name": "Arcane Presence", "description": "Arcane Mastery increases the damage of your Cold, Fire, and Lightning based attacks by 1% per stack.", "active": True}
]

# General/Skill feats
wizard["feats"] = [
    {"name": "Arcana", "description": "Innate understanding of arcane forces and magical objects.", "type": "skill"},
    {"name": "Brisk Transport", "description": "When you Teleport, Movement Speed +10 for 2s.", "type": "skill"},
    {"name": "Controlled Momentum", "description": "After using a Control Encounter, allies within 30' deal 2% more damage for 6s. Does not stack.", "type": "skill"},
    {"name": "Improved Technique", "description": "Adds 5% Control Bonus.", "type": "skill"}
]

# ---- Thaumaturge paragon
thaum = next(p for p in wizard["paragonPaths"] if p["name"] == "Thaumaturge")
thaum["atWill"] = [
    {"name": "Scorching Burst", "type": "atWill", "paragon": True, "magnitude": "60-110", "castSeconds": 1.7, "range": 80, "radius": 1, "addedEffect": "Adds Smolder to targets", "notes": "Column of fire at target location. Size and damage increase the longer it's channeled."},
    {"name": "Chilling Cloud", "type": "atWill", "paragon": True, "magnitude": 90, "castSeconds": 0.4, "range": 80, "addedEffect": "Adds Chill stack. Third hit also damages enemies near target; final attack adds Chill to all targets.", "notes": "Swarm of ice crystals."}
]
thaum["encounter"] = [
    {"name": "Fanning the Flame", "type": "encounter", "paragon": True, "magnitude": 500, "castSeconds": 0.6, "cooldownSeconds": 15.3, "range": 80, "durationSeconds": 6, "addedEffect": "Smolder. Enemies within 15' affected by Smolder take 100 mag dmg and deal 100 mag dmg to the burning target.", "notes": "Set enemy ablaze with hard-to-extinguish burn."},
    {"name": "Icy Rays", "type": "encounter", "paragon": True, "magnitude": "600-850", "castSeconds": 0, "cooldownSeconds": 15.3, "range": 80, "durationSeconds": 1, "addedEffect": "Stun + Adds Chill stack. Two-cast: rune mark + dual fire if both at one target.", "notes": "First cast marks; second cast hits marked + current target."},
    {"name": "Chill Strike", "type": "encounter", "paragon": True, "magnitude": 660, "castSeconds": 0.4, "cooldownSeconds": 12.7, "range": 80, "durationSeconds": 0.5, "addedEffect": "Stun + Adds Chill stack", "notes": "Hurl powerful icicle. Spell Mastery: Reduced damage but damages nearby enemies (300 mag)."},
    {"name": "Conduit of Ice", "type": "encounter", "paragon": True, "magnitude": 350, "castSeconds": 0.8, "cooldownSeconds": 11.0, "range": 80, "addedEffect": "Adds chill stack to all targets hit", "notes": "Enemy becomes conduit for icy storm, damaging surrounding foes."},
    {"name": "Fireball", "type": "encounter", "paragon": True, "magnitude": 350, "castSeconds": 0.6, "cooldownSeconds": 10.2, "range": 80, "radius": 15, "addedEffect": "Adds Smolder to all targets hit", "notes": "Fire damage to target and nearby. Spell Mastery: Single target, magnitude 700."}
]
thaum["daily"] = [
    {"name": "Furious Immolation", "type": "daily", "paragon": True, "magnitude": 900, "castSeconds": 2.0, "actionPointCost": 1000, "range": 80, "radius": 35, "durationSeconds": 1, "addedEffect": "Pull + Adds Smolder", "notes": "Titanic column of flame that pulls enemies in and blasts upward."},
    {"name": "Ice Storm", "type": "daily", "paragon": True, "magnitude": 1200, "castSeconds": 1.9, "actionPointCost": 1000, "radius": 40, "durationSeconds": 5, "addedEffect": "Slow + Knockdown + Adds 1 stack of Chill", "notes": "Massive wave of ice."}
]
thaum["mechanic"] = [
    {"name": "Smolder", "type": "mechanic", "paragon": True, "notes": "Your fire powers add Smolder DoT. If target is Chilled, gains Rimefire aspect allowing duration refresh by Chill effects."},
    {"name": "Forte", "type": "mechanic", "paragon": True, "notes": "Paragon provides Power increase + excels at Combat Advantage and Critical Avoidance."}
]
thaum["classFeatures"] = [
    {"name": "Frost Wave", "description": "When you activate a Daily power, apply 6 stacks of Chill and Freeze foes within 30'.", "paragon": True},
    {"name": "Combustive Action", "description": "When a target affected by Smolder dies, you gain 5% of max Action Points. 1s cooldown.", "paragon": True},
    {"name": "Swath of Destruction", "description": "Increases Smolder damage by 10%; targets affected by Smolder take 3% more damage.", "paragon": True, "active": True},
    {"name": "Critical Conflagration", "description": "Whenever you critically strike with one of your powers, add Smolder to target (if not already burning).", "paragon": True, "active": True}
]
thaum["feats"] = [
    {"name": "Relative Haste", "description": "Powers recharge 5% faster per Chilled enemy nearby. Max 20% speedup.", "paragon": True}
    # More Thaumaturge feats to be added in v2 as I capture them
]

# ---- Arcanist paragon
arc = next(p for p in wizard["paragonPaths"] if p["name"] == "Arcanist")
arc["atWill"] = [
    {"name": "Storm Pillar", "type": "atWill", "paragon": True, "magnitude": "40-100", "castSeconds": 1.6, "range": 80, "radius": 8, "addedEffect": "Refreshes Arcane Mastery and Chill stacks if >50% charge. Max charge: pillar of lightning attacks nearby targets (50 mag, 3s).", "notes": "Charge up blast of lightning. If no target, hits your location."},
    {"name": "Arcane Bolt", "type": "atWill", "paragon": True, "magnitude": 120, "castSeconds": 0.7, "range": 80, "addedEffect": "Grants stack of Arcane Mastery", "notes": "Summon Arcane Bolts from the sky."}
]
arc["encounter"] = [
    {"name": "Lightning Bolt", "type": "encounter", "paragon": True, "magnitude": 350, "castSeconds": 0.72, "cooldownSeconds": 10.3, "range": 30, "radius": 5, "addedEffect": "Refreshes Arcane Mastery and Chill stacks", "notes": "Call down Spell Storm, releasing powerful bolts of lightning in front."},
    {"name": "Disintegrate", "type": "encounter", "paragon": True, "magnitude": "500 or 750", "castSeconds": 0.35, "cooldownSeconds": 6.9, "range": 80, "addedEffect": "If target below 20% HP, attempt to Disintegrate (+50% damage).", "notes": "Deal arcane damage to enemy."},
    {"name": "Steal Time", "type": "encounter", "paragon": True, "magnitude": 350, "castSeconds": 0.6, "cooldownSeconds": 11.2, "radius": 30, "durationSeconds": 4, "addedEffect": "Slow. Additional Action: Stun 1s. Arcane Mastery increases Stun/Slow by 0.2s per stack.", "notes": "Steal time from enemies around you, then shatter to stun."},
    {"name": "Arcane Tempest", "type": "encounter", "paragon": True, "magnitude": 400, "castSeconds": 0.35, "cooldownSeconds": 11.2, "range": 80, "radius": 10, "addedEffect": "Knockdown", "notes": "Fury of arcane energy at target. Spell Mastery: Around yourself, mag 440."},
    {"name": "Arcane Conduit", "type": "encounter", "paragon": True, "magnitude": 300, "castSeconds": 0.4, "cooldownSeconds": 10.3, "range": 80, "durationSeconds": 5, "addedEffect": "Target takes 15% increased damage from arcane powers. Grants 1 stack of Arcane Mastery.", "notes": "Spell Mastery: Bonus to 20%, magnitude 330."}
]
arc["daily"] = [
    {"name": "Maelstrom of Chaos", "type": "daily", "paragon": True, "magnitude": 1400, "castSeconds": 2.13, "actionPointCost": 1000, "range": 80, "radius": 8, "durationSeconds": 1, "addedEffect": "Knockdown + Refreshes Arcane Mastery and Chill stacks", "notes": "Unleash bolt of spell storm chaos. Immune to control during cast."},
    {"name": "Arcane Empowerment", "type": "daily", "paragon": True, "castSeconds": 1.3, "actionPointCost": 1000, "range": 80, "durationSeconds": 10, "addedEffect": "Encounter powers +20% damage and recharge faster. Gain 5 stacks of Arcane Mastery.", "notes": "Empower yourself with arcane magic, entering transcendent state."}
]
arc["mechanic"] = [
    {"name": "Forte", "type": "mechanic", "paragon": True, "notes": "Paragon provides Power increase + excels at Combat Advantage and Critical Avoidance."}
]
arc["classFeatures"] = [
    {"name": "Eye of the Storm", "description": "Using an Encounter/Daily grants Eye of the Storm for 5s — 10% Critical Strike. (10s CD)", "paragon": True},
    {"name": "Storm Spell", "description": "Shock target for 120 magnitude 20% of the time on critical attacks.", "paragon": True},
    {"name": "Storm Fury", "description": "When attacked, enemies shocked for 200 magnitude. Once per enemy per 3s.", "paragon": True},
    {"name": "Arcane Power Field", "description": "When you activate a Daily, gain Arcane Power Field for 8s: doubles Arcane Mastery damage bonus, foes within 30' take 60 mag damage every 2s.", "paragon": True}
]
arc["feats"] = [
    {"name": "Alacrity", "description": "Whenever you use a daily power against an enemy, reduce Encounter cooldowns by 5s.", "paragon": True},
    {"name": "Assailing Force", "description": "Encounter powers have a 10% chance of applying Assailing Force. Next Encounter power deals double initial damage.", "paragon": True},
    {"name": "Chaos Magic", "description": "Encounter/Daily powers have 7% chance to apply one of 3 buffs: Power Surge (+100% at-will damage 5s), Rapid Recovery (+100% Cooldown Recovery 5s), Quick Action (+20% AP over 5s).", "paragon": True},
    {"name": "Nightmare Wizardry", "description": "Critical Strikes have 10% chance to grant Combat Advantage for 10s.", "paragon": True},
    {"name": "A Step Above Mastery", "description": "Arcane Mastery stacks up to 10, +0.5% damage per stack, lasts 10s.", "paragon": True},
    {"name": "Elemental Reinforcement", "description": "Casting Arcane/Cold/Lightning spell grants 7% damage for 10s. Doubled if you don't cast same element twice in a row.", "paragon": True},
    {"name": "Striking Advantage", "description": "Dealing Combat Advantage damage with At-Will/Encounter/Daily grants 25% chance of 120 magnitude lightning damage. 1s cooldown.", "paragon": True},
    {"name": "Iced Lightning", "description": "Storm Pillar, Lightning Bolt, Storm Spell, Storm Fury and Striking Advantage deal 30% increased base damage versus chilled targets.", "paragon": True},
    {"name": "Snap Freeze", "description": "Chill deals 70 magnitude damage each time a stack is applied to an enemy.", "paragon": True},
    {"name": "Spell Twisting", "description": "Encounter powers grant Spell Twisting stack (max 4). Casting At-will consumes 1 stack; consuming grants 1% total AP.", "paragon": True}
]

CLASSES.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print("Wizard powers populated (Thaumaturge + Arcanist paragons).")
