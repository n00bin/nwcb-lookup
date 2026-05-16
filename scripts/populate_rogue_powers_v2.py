"""v2 update — adds Assassin paragon dailies, class features, feats."""
import json
from pathlib import Path

CLASSES = Path("G:/ai_projects/nwcb/data/classes.json")
data = json.loads(CLASSES.read_text(encoding="utf-8"))

rogue = next(c for c in data if c["name"] == "Rogue")
assassin = next(p for p in rogue["paragonPaths"] if p["name"] == "Assassin")

assassin["daily"] = [
    {"name": "Bloodbath", "type": "daily", "paragon": True, "magnitude": 2200, "castSeconds": 0.25, "actionPointCost": 1000, "range": 30, "radius": 30, "notes": "Flash around the battlefield, slashing into your foes so quickly that you cannot be targeted."},
    {"name": "Shocking Execution", "type": "daily", "paragon": True, "magnitude": 2200, "castSeconds": 1.5, "actionPointCost": 1000, "range": 30, "addedEffect": "If hit target below 20% HP, refill half of action points (20s CD). Enemy PvP players killed by this cannot be revived.", "notes": "Leap up and strike with a vicious attack."}
]

assassin["classFeatures"] = [
    {"name": "Invisible Infiltrator", "description": "When you use a Daily power, your Stealth meter is refilled. For 5 seconds afterward, your Damage is increased by 5%.", "paragon": True},
    {"name": "Infiltrator's Action", "description": "When you use a Daily power, you gain Combat Advantage for 10 seconds.", "paragon": True},
    {"name": "Oppressive Darkness", "description": "When you have Combat Advantage your powers deal an additional 20 magnitude damage to the target.", "paragon": True, "active": True},
    {"name": "First Strike", "description": "Your first attack in combat deals 15% more damage.", "paragon": True}
]

assassin["feats"] = [
    {"name": "Assassin's Target", "description": "Your at-will and daily power attacks apply a stack of 'targeted' to the first enemy hit. Stacks up to 5 times; increases damage of your next Encounter power that strikes the target by 1% per stack.", "paragon": True},
    {"name": "Knife's Edge", "description": "Activating a Daily power reduces your cooldowns by 4 seconds.", "paragon": True},
    {"name": "Duelist's Expertise", "description": "Gain 0.5% increased damage and deflect chance for each second you are in combat (max 15 stacks). At 16 stacks or when leaving combat, gain Master Duelist: consume all stacks for 15% Damage and Deflect chance, for 10s.", "paragon": True},
    {"name": "Back Alley Tactics", "description": "Deal up to 10% more damage based on how few Action Points you have.", "paragon": True},
    {"name": "Execution", "description": "When enemy is under 20% life, attacks have a 10% chance to execute the target dealing 200 magnitude damage.", "paragon": True},
    {"name": "Shadow's Flurry", "description": "Your attacks have a 5% chance to spawn a shadowy figure that uses the final combo of Duelist's Flurry on the target.", "paragon": True},
    {"name": "Hastily Sharpened Blades", "description": "Critical Strike is increased by a random amount on each attack from 5% to 10%.", "paragon": True},
    {"name": "Skullcracker", "description": "Every 15s gain 'skullcracker': next At-will or Encounter Dazes for 3s and marks target for 10s (mark duration +0.5s per damage hit, max +5s bonus). Marked enemies take 10% more damage from your powers.", "paragon": True},
    {"name": "Master of Shadows", "description": "Stealth regeneration +50%, Stealth duration +25%.", "paragon": True},
    {"name": "Toxic Blades", "description": "Encounter and Daily attacks apply a DoT: 20 magnitude weapon damage every 3s for 15s, stacks up to 5 times. Does not apply to players.", "paragon": True}
]

CLASSES.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print("Assassin paragon dailies, class features, and feats added.")
