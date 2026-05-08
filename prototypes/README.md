# Toon Forge — Roadmap

The character builder we're working toward. Prototype is locked in:
visual identity, UX flow, and feel.

## What's here now

- **`toon-forge.html`** — interactive wizard prototype. 6 steps, mock data,
  live Build Score gauge. This is the visual + UX target.
- **`character-editor.html`** — earlier dense-form prototype. Kept for
  reference but **not** the target (looked too much like NW Hub).

Open `toon-forge.html` directly in a browser via `file://` to play with it.
Not deployed, not in nav, won't show on the live site.

## How it differs from NW Hub (deliberate)

| Aspect | NW Hub | Toon Forge |
|---|---|---|
| Layout | 3-column dense form-dump | Single-column 6-step wizard |
| Heading font | Sans-serif | Georgia serif (subtle fantasy feel) |
| Brand color | Blue-first | Amber-first throughout |
| Role picker | Dropdown | Big tappable tiles with blurbs |
| Class picker | Dropdown list | Visual 9-card grid |
| Stat panel | Always-visible right column, 30+ rows | Sticky footer with Build Score gauge + 5 hero stats |
| Tone | Terse, technical | Friendly explanations, plain English |
| Progress | Single giant scroll | Numbered steps with done-checkmarks |
| Help | None | Hint icons + tooltips on every stat |
| Audience | Theorycrafters | n00b's audience (casual / mid-core) |
| Headline | Stat percentage walls | Single 0–100 score with tier label |

## Build phases (rough estimate)

### Phase 1 — Data foundation (1–2 weeks)
The biggest gap. We have companions/mounts/insignias/artifacts but
**no gear database**.
- [ ] Gear database (12 slots × multiple tiers × class restrictions)
      — schema, source data, build pipeline integration
- [ ] Class + paragon path data (stat distribution per role; some
      already in mekaniks.html Forte table)
- [ ] Race data (ability score modifiers)
- [ ] Boon trees (Stronghold, Guild, Master)
- [ ] Buff catalog (food, scrolls, potions, masterworks)

### Phase 2 — Stat aggregation engine (3–4 days)
- [ ] Pure JS module that takes the full character state and outputs
      every final stat percentage
- [ ] Source breakdown per stat (so users can see "50% from rating,
      20% from companions, 12% from boons")
- [ ] Cap awareness (rating cap vs total cap per the Mekaniks page)
- [ ] Forte distribution applied per paragon

### Phase 3 — Live stat panel hooked up (2–3 days)
- [ ] Replace prototype's mock numbers with engine output
- [ ] Cap progress bars actually compute
- [ ] Build Score formula refined (probably weighted toward role-
      relevant caps reached)

### Phase 4 — Magnitude calculator + hit scenarios (2–3 days)
- [ ] Use the Full Damage Formula already documented in mekaniks.html
- [ ] CR / FL / DF probability matrix
- [ ] Expected weighted average

### Phase 5 — Wiring all sections (1 week)
- [ ] Companion picker → real summoned + 4-active + 12-stable bolster
- [ ] Mount picker → 1-active + 9-stable bolster + insignia bonuses
- [ ] Boon checkboxes → real percentage contributions
- [ ] Buff checkboxes → real stat contributions

### Phase 6 — Save / load / share (3–4 days)
- [ ] localStorage profiles (multi-character)
- [ ] Export to JSON / share-link compress
- [ ] Import from JSON or share link

### Phase 7 — Build optimizer (1–2 weeks; the moonshot)
- [ ] Given owned items, search for best stat distribution
- [ ] Respect slot rules, set bonuses, unique-equip
- [ ] Output explainability (top contributors, biggest tradeoffs)

### Phase 8 — Polish + integrate into site (3–4 days)
- [ ] Add to top nav
- [ ] Mobile responsive
- [ ] Onboarding tour (first-time visitor walkthrough)

**Total rough estimate: 5–8 weeks of focused work.**

## Constraints to honor

- Per `CLAUDE.md`: no fabricated stats. All gear/boon/buff values must
  come from in-game screenshots or community references.
- Site identity: this is for **n00b's audience** — casual to mid-core.
  When in doubt, choose the friendlier label and the less dense layout.
- Mobile-first matters: many viewers will be on a phone.
