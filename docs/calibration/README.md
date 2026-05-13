# Calibration Screenshots

This folder stores in-game screenshots used during Toon Forge stat calibration.

## Naming convention

```
YYYY-MM-DD_class-paragon_what-it-shows.png
```

Examples:
- `2026-05-13_ranger-warden_stat-panel.png` — full character stat sheet
- `2026-05-13_ranger-warden_thayan-talisman-tooltip.png` — hover tooltip of one item
- `2026-05-13_ranger-warden_executioners-covenant-bonus.png` — insignia bonus tooltip

## What to capture

When auditing a stat or verifying a fix, save the following:
- **Full stat panel** — the headline numbers we're trying to match
- **Item tooltips** for any item we're questioning — proves the direct stats
- **Insignia bonus panels** — verifies which bonuses are active per mount
- **Class skill tab** — confirms which class skills the character has
- **Buff/boon screens** — confirms which buffs are active

## Linking to patterns

Each entry in `../calibration_patterns.md` should cite its supporting screenshot when one exists:

```
**Evidence**: 2026-05-13_ranger-warden_rotsteel-tooltip.png
```

That lets a future session re-verify the pattern by reading the actual screenshot, not relying on chat memory.

## Notes

- PNG is preferred (lossless, exact stat values are readable)
- Crop to just the relevant panel if possible — easier to skim later
- Don't worry about file size; this is a personal project, repo size doesn't matter
