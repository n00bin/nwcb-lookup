"""v3 update — Barbarian: add shared Sprint/Battlerage mechanics, Adamantine Strike daily,
all remaining Blademaster class features + feats."""
import json
from pathlib import Path

CLASSES = Path("G:/ai_projects/nwcb/data/classes.json")
data = json.loads(CLASSES.read_text(encoding="utf-8"))
barb = next(c for c in data if c["name"] == "Barbarian")

# Add Sprint mechanic + Battlerage to shared base
barb["powers"]["mechanic"] = [
    {"name": "Sprint", "type": "mechanic", "tactical": True, "castSeconds": 0, "range": "Self", "addedEffect": "Control Immunity; first 1s grants immunity to most damage (3s CD)", "notes": "Movement speed +100%, drains stamina. Ends when Sprint ends or stamina depleted."},
    {"name": "Block", "type": "mechanic", "tactical": True, "castSeconds": 0, "range": "Self", "addedEffect": "Immune to Control Effects + Gain 15% Critical Avoidance under Unstoppable", "notes": "Raise weapon, absorbs 40% Max HP from front. Drains stamina."},
    {"name": "Unstoppable", "type": "mechanic", "castSeconds": 0, "range": "Self", "addedEffect": "Absorbs up to 60% Max HP + Immune to Control", "notes": "Generates Rage from damage and kills. At 50% Rage, activate Unstoppable. Increases at-will speed, drains Rage."},
    {"name": "Battlerage", "type": "mechanic", "castSeconds": 0, "range": "Self", "addedEffect": "Control Immunity + Damage dealt +25% + Damage taken -15%", "notes": "Generates Rage from damage and kills. At 50% Rage, activate Battlerage. Increases at-will speed, drains Rage over time."}
]

# ---- Blademaster paragon — add daily, class features, more feats
bm = next(p for p in barb["paragonPaths"] if p["name"] == "Blademaster")
bm["daily"] = [
    {"name": "Avalanche of Steel", "type": "daily", "paragon": True, "magnitude": 1400, "castSeconds": 5.0, "actionPointCost": 1000, "range": 30, "addedEffect": "Knock Down + Immune to most damage and control for 5s pre-impact", "notes": "Leap into the air, slam to ground."},
    {"name": "Adamantine Strike", "type": "daily", "paragon": True, "magnitude": 1200, "castSeconds": 1.3, "actionPointCost": 1000, "range": 30, "arc": 180, "durationSeconds": 10, "addedEffect": "Increases target's damage taken by 5%", "notes": "Cone damage in front of you."}
]
bm["classFeatures"] = [
    {"name": "Barbed Strikes", "description": "Critical Strike + Critical Severity +5% when stamina is full. Decreases as stamina decreases.", "paragon": True},
    {"name": "Steel Blitz", "description": "Your at-will attacks have a 20% chance to strike the target twice.", "paragon": True, "active": True},
    {"name": "Raging Strikes", "description": "Rage increases the damage your attacks deal, up to a maximum of 15%.", "paragon": True},
    {"name": "Impatience", "description": "Entering Battlerage reduces all of your cooldowns by 2 seconds.", "paragon": True}
]
bm["feats"] = [
    {"name": "Unstoppable Spin", "description": "Spinning Strike with <50 Rage sets Rage to 50. Battlerage activates automatically, duration +6s, damage bonus +50%. Does not stack with or activate Rampage.", "paragon": True},
    {"name": "Raging Criticals", "description": "Critical severity +10% when under Battlerage or Unstoppable.", "paragon": True},
    {"name": "Relentless Speed", "description": "Relentless Slash has 15% chance to grant Relentless Speed (6s): use Not So Fast regardless of cooldown and without triggering one.", "paragon": True},
    {"name": "Bloodspiller", "description": "Bloodletter magnitude increased to 950, recovers from cooldown 3s faster, causes Bloodletter to deal damage to you.", "paragon": True},
    {"name": "Overpenetration", "description": "Powers deal up to 10% more damage based on Critical Strike + Critical Severity proximity to rating cap.", "paragon": True},
    {"name": "Steel Slam", "description": "Avalanche of Steel creates a circle of unstable ground on landing (200 mag x3, 12s, Slow 3s).", "paragon": True},
    {"name": "Relentless Battlerage", "description": "Build 2x as much Rage from At-Will, Encounter, damage taken, and kills.", "paragon": True},
    {"name": "Escalating Rage", "description": "Deal critical damage to gain Escalating Rage stacks. At 5 stacks, gain Rampage (20s): extends Battlerage by 8s, +25% damage bonus. Cannot build Escalating Rage during Battlerage.", "paragon": True},
    {"name": "Brutal Critical", "description": "Whenever attacks deal critical damage, increase Rage by 3.", "paragon": True},
    {"name": "Indomitable Rage", "description": "Indomitable Battle Strike's magnitude increases to 1200 at max Rage, decreases to 800 with no Rage.", "paragon": True},
    {"name": "Mightier Leap", "description": "Mighty Leap hitting no enemies grants Mightier Leap (6s): magnitude 780 and allows immediate reuse. Cannot trigger consecutively.", "paragon": True}
]

CLASSES.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print("Barbarian v3 — Sprint/Battlerage mechanics, Adamantine Strike, full Blademaster class features and feats.")
