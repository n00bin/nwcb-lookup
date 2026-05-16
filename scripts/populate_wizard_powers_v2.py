"""v2 update — add remaining Thaumaturge feats and Wizard racial general powers."""
import json
from pathlib import Path

CLASSES = Path("G:/ai_projects/nwcb/data/classes.json")
data = json.loads(CLASSES.read_text(encoding="utf-8"))

wizard = next(c for c in data if c["name"] == "Wizard")
thaum = next(p for p in wizard["paragonPaths"] if p["name"] == "Thaumaturge")

# Add Thaumaturge feats (was only Relative Haste)
thaum["feats"] = [
    {"name": "Relative Haste", "description": "Powers recharge 5% faster per Chilled enemy nearby. Max 20% speedup.", "paragon": True},
    {"name": "Glowing Flames", "description": "Smolder's flames radiate, dealing 30% normal damage to afflicted enemies within 15' of primary target.", "paragon": True},
    {"name": "Chilling Advantage", "description": "Cold-based at-will/encounter/daily that apply Chill now also directly apply Rimefire Smolder.", "paragon": True},
    {"name": "Critical Burn", "description": "Critical severity +10% and Smolder deals 25% more critical damage.", "paragon": True},
    {"name": "Directed Flames", "description": "Smolder and Rimefire Smolder deal 25% of total damage on apply/reapply (no longer DoT). 1s CD.", "paragon": True},
    {"name": "Rimefire Weaving", "description": "Smolder/Chill on target reduces its Damage Resistance to your damage by 5%. Rimefire increases this to 10%. Rimefire bonus doesn't stack with chill or smolder.", "paragon": True},
    {"name": "Icy Veins", "description": "Activating an Encounter Power applies 1 stack of Chill to all foes within 20'.", "paragon": True},
    {"name": "Smoldering Recovery", "description": "Whenever Smolder deals damage, you gain 0.3% of Action Points. With Directed Flames, 0.3% of Action Points.", "paragon": True}
]

# Note: Wizard's racial/general skills are character-specific (Dragonborn here). Documented separately
# but not added to wizard.feats since those are character traits, not class properties.

CLASSES.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print("Thaumaturge feats updated with full set.")
