// Smoke-test harness for the engine — run with `node`.
//   node prototypes/toon-forge-engine-test.js

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const sandbox = { window: {}, console: console };
vm.createContext(sandbox);

function loadInto(file) {
  const src = fs.readFileSync(path.join(__dirname, file), "utf-8");
  vm.runInContext(src, sandbox);
}

loadInto("toon-forge-stats.js");
loadInto("toon-forge-engine.js");

const E = sandbox.window.TOON_FORGE_ENGINE;

let passes = 0, fails = 0;
function assertEq(actual, expected, label) {
  if (actual === expected) { passes++; console.log(`  PASS ${label}: ${actual}`); }
  else { fails++; console.error(`  FAIL ${label}: expected ${expected}, got ${actual}`); }
}
function assertClose(actual, expected, eps, label) {
  if (Math.abs(actual - expected) <= eps) { passes++; console.log(`  PASS ${label}: ${actual.toFixed(2)} (~${expected})`); }
  else { fails++; console.error(`  FAIL ${label}: expected ~${expected}, got ${actual}`); }
}

// =============================================================
// Test 1: rating aggregation
// =============================================================
console.log("\n--- Test 1: rating aggregation ---");
{
  const character = {
    totalItemLevel: 89000,
    gear: {
      "Head":  { name: "Hood", ratingStats: { "Critical Severity": 3483, "Outgoing Healing": 2838 } },
      "Armor": { name: "Robe", ratingStats: { "Power": 5000, "Critical Strike": 2500 } }
    },
    artifacts: {
      primary:   { name: "Primary",     ratingStats: { "Power": 1000, "Combat Advantage": 500 } },
      secondary: [{ name: "Secondary",  ratingStats: { "Power": 300 } }]
    },
    companionGear: {
      "Neck": { name: "Talisman", ratingStats: { "Combat Advantage": 1950, "Critical Strike": 1740 } }
    }
  };
  const r = E.computeStats(character);
  assertEq(r.stats["Power"].ratingTotal, 6300, "Power rating total");
  assertEq(r.stats["Combat Advantage"].ratingTotal, 2450, "CA rating total");
  assertEq(r.stats["Critical Strike"].ratingTotal, 4240, "CritStrike rating total");
  assertEq(r.stats["Power"].contributors.length, 3, "Power contributor count");
  assertEq(r.stats["Class Resource Max"].flat, 1000, "CR Max base");
}

// =============================================================
// Test 2: rating-to-% formula at canonical points
// =============================================================
console.log("\n--- Test 2: rating-to-% formula ---");
{
  // At rating == TIL → 50%
  const r1 = E.computeStats({
    totalItemLevel: 89000,
    gear: { "Head": { name: "T", ratingStats: { "Power": 89000 } } }
  });
  assertClose(r1.stats["Power"].ratingContribPct, 50, 0.01, "rating == TIL → 50%");
  assertClose(r1.stats["Power"].finalPct, 50, 0.01, "Power finalPct = 50% (no bonuses)");

  // At rating == TIL + 10000 → 60% (rating cap for 120% stats)
  const r2 = E.computeStats({
    totalItemLevel: 89000,
    gear: { "Head": { name: "T", ratingStats: { "Power": 99000 } } }
  });
  assertClose(r2.stats["Power"].ratingContribPct, 60, 0.01, "rating == TIL+10k → 60%");

  // At rating > TIL + 10000 → still 60%, with overcap warning
  const r3 = E.computeStats({
    totalItemLevel: 89000,
    gear: { "Head": { name: "T", ratingStats: { "Power": 105000 } } }
  });
  assertClose(r3.stats["Power"].ratingContribPct, 60, 0.01, "Power overcap clamped to 60");
  let hasOvercapWarn = r3.warnings.some(w => /overcap on Power/.test(w));
  assertEq(hasOvercapWarn, true, "overcap warning emitted");
}

// =============================================================
// Test 3: percent aggregation (race + master boon)
// =============================================================
console.log("\n--- Test 3: percent aggregation ---");
{
  const character = {
    totalItemLevel: 89000,
    race: {
      name: "Sun Elf",
      traits: [
        { name: "Inner Calm",     percentStats: { "Action Point Gain": 5 } },
        { name: "Sun Elf Grace",  percentStats: { "Control Resist": 25 } }
      ]
    },
    campaignBoons: {
      master: [
        {
          ranks: 3,
          boon: {
            name: "Deathly Rage", maxRanks: 3,
            perRankEffects: [
              { stat: "Combat Advantage",  amount: 2, type: "percent" },
              { stat: "Power",             amount: 2, type: "percent" },
              { stat: "Critical Severity", amount: 2, type: "percent" }
            ]
          }
        },
        {
          ranks: 3,
          boon: {
            name: "Blood Lust", maxRanks: 3,
            perRankEffects: [
              { stat: "Defense",         amount: -1, type: "percent", scope: "enemy" }, // skipped
              { stat: "magnitude",       amount: 10, type: "flat" },                    // skipped (flat)
              { stat: "Action Point Gain", amount: 0.5, type: "percent" }
            ]
          }
        }
      ]
    }
  };
  const r = E.computeStats(character);
  assertClose(r.stats["Power"].percentTotal, 6, 0.001, "Power %total = +6 from Deathly Rage R3");
  assertClose(r.stats["Combat Advantage"].percentTotal, 6, 0.001, "CA %total = +6");
  assertClose(r.stats["Critical Severity"].percentTotal, 6, 0.001, "CritSev %total = +6");
  assertClose(r.stats["Action Point Gain"].percentTotal, 5 + 1.5, 0.001, "AP Gain %total = race(5) + bloodlust(1.5)");
  assertClose(r.stats["Control Resist"].percentTotal, 25, 0.001, "CtrlResist %total = 25 from Sun Elf Grace");
  // Defense should NOT have the enemy-scoped -1% applied
  assertEq(r.stats["Defense"].percentTotal, 0, "enemy-scoped boon effect skipped");
}

// =============================================================
// Test 4: rating + percent combined, cap clamping
// =============================================================
console.log("\n--- Test 4: combined finalPct + cap clamping ---");
{
  // Power: rating = TIL (50%) + master boon +6% = 56% finalPct
  const r1 = E.computeStats({
    totalItemLevel: 89000,
    gear: { "Head": { name: "T", ratingStats: { "Power": 89000 } } },
    campaignBoons: {
      master: [{
        ranks: 3,
        boon: {
          name: "Deathly Rage", maxRanks: 3,
          perRankEffects: [{ stat: "Power", amount: 2, type: "percent" }]
        }
      }]
    }
  });
  assertClose(r1.stats["Power"].finalPct, 56, 0.01, "Power = 50 (rating) + 6 (boon) = 56");
  assertEq(r1.stats["Power"].capReached, false, "Power not at cap");

  // Power overcap: rating(60%) + percent(70%) = 130 → clamped to 120, warning
  const r2 = E.computeStats({
    totalItemLevel: 89000,
    gear: { "Head": { name: "T", ratingStats: { "Power": 99000 } } },
    campaignBoons: {
      master: [{
        ranks: 3,
        boon: {
          name: "Big Buff", maxRanks: 3,
          perRankEffects: [{ stat: "Power", amount: 23.4, type: "percent" }]  // 3 × 23.4 = 70.2%
        }
      }]
    }
  });
  assertClose(r2.stats["Power"].finalPct, 120, 0.01, "Power clamped to 120 cap");
  assertEq(r2.stats["Power"].capReached, true, "Power capReached = true");
  let totalCapWarn = r2.warnings.some(w => /Total cap on Power/.test(w));
  assertEq(totalCapWarn, true, "total-cap warning emitted");
}

// =============================================================
// Test 5: fixed-ratio stats (AP Gain, Recharge Speed)
// =============================================================
console.log("\n--- Test 5: fixed-ratio stats ---");
{
  const character = {
    totalItemLevel: 89000,
    gear: {
      "Head": { name: "T", ratingStats: { "Action Point Gain": 800, "Recharge Speed": 1000 } }
    }
  };
  const r = E.computeStats(character);
  assertClose(r.stats["Action Point Gain"].ratingContribPct, 2, 0.01, "AP Gain: 800 / 400 = 2%");
  assertClose(r.stats["Recharge Speed"].ratingContribPct, 5, 0.01, "Recharge: 1000 / 200 = 5%");
}

// =============================================================
// Test 6: Class Resource Regen aliasing
// =============================================================
console.log("\n--- Test 6: Class Resource Regen aliasing ---");
{
  const character = {
    totalItemLevel: 89000,
    gear: {
      "Head": { name: "T", percentStats: { "Performance Regen": 3, "Divinity Regen": 2 } }
    }
  };
  const r = E.computeStats(character);
  assertClose(r.stats["Class Resource Regen"].percentTotal, 5, 0.001,
    "Performance Regen + Divinity Regen routed to Class Resource Regen");
}

// =============================================================
// Test 7: flat stats (Max HP, Class Resource Max)
// =============================================================
console.log("\n--- Test 7: flat-kind stats ---");
{
  const character = {
    totalItemLevel: 89000,
    gear: {
      "Head":  { name: "T1", ratingStats: { "Maximum Hit Points": 5000 } },
      "Armor": { name: "T2", ratingStats: { "Maximum Hit Points": 12000 } }
    }
  };
  const r = E.computeStats(character);
  assertEq(r.stats["Maximum Hit Points"].flat, 17000, "Max HP flat = 5000 + 12000");
  assertEq(r.stats["Maximum Hit Points"].ratingContribPct, 0, "Max HP ratingContribPct = 0 (flat)");
  assertEq(r.stats["Class Resource Max"].flat, 1000, "CR Max base = 1000 (no gear adds)");
}

// =============================================================
// Test 8: forte distribution
// =============================================================
console.log("\n--- Test 8: forte distribution ---");
{
  // Wizard Arcanist: Power 50% / Critical Severity 25% / Awareness 25%
  // Forte rating = TIL → Forte % = 50% → distributed:
  //   Power: 50 × 0.50 = +25%
  //   CritSev: 50 × 0.25 = +12.5%
  //   Awareness: 50 × 0.25 = +12.5%
  const r = E.computeStats({
    totalItemLevel: 89000,
    paragonDef: {
      name: "Arcanist",
      percentStats: { "Power": 50, "Critical Severity": 25, "Awareness": 25 }
    },
    gear: { "Head": { name: "T", ratingStats: { "Forte": 89000 } } }
  });
  assertClose(r.stats["Forte"].ratingContribPct, 50, 0.01, "Forte itself = 50% (rating=TIL)");
  assertClose(r.stats["Power"].percentTotal, 25, 0.01, "Forte → Power +25%");
  assertClose(r.stats["Critical Severity"].percentTotal, 12.5, 0.01, "Forte → CritSev +12.5%");
  assertClose(r.stats["Awareness"].percentTotal, 12.5, 0.01, "Forte → Awareness +12.5%");
}

// =============================================================
// Test 9: forte bypasses rating cap
// =============================================================
console.log("\n--- Test 9: forte bypasses fed-stat rating cap ---");
{
  // Power has rating capped at 60% (rating == TIL+10000).
  // With Forte at TIL → Forte +25% to Power's percentTotal.
  // Final Power = 60 (rating cap) + 25 (forte) + ... = 85%
  // This ONLY works if Forte's contribution flows through percentTotal,
  // bypassing Power's rating cap. If it went through ratingContribPct,
  // Power would be clamped at 60%.
  const r = E.computeStats({
    totalItemLevel: 89000,
    paragonDef: {
      name: "Arcanist",
      percentStats: { "Power": 50, "Critical Severity": 25, "Awareness": 25 }
    },
    gear: {
      "Head":  { name: "T", ratingStats: { "Forte": 89000, "Power": 99000 } }
    }
  });
  assertClose(r.stats["Power"].ratingContribPct, 60, 0.01, "Power rating clamped at 60");
  assertClose(r.stats["Power"].percentTotal, 25, 0.01, "Power %total has +25 from forte");
  assertClose(r.stats["Power"].finalPct, 85, 0.01, "Power final = 60 (rating) + 25 (forte) = 85");
}

// =============================================================
// Test 10: forte healer paragon — Class Resource Regen alias
// =============================================================
console.log("\n--- Test 10: forte healer alias routing ---");
{
  // Bard Minstrel: "Performance Regen" 50% / Crit Sev 25% / Deflect Sev 25%
  // Forte primary "Performance Regen" should route to "Class Resource Regen"
  const r = E.computeStats({
    totalItemLevel: 89000,
    paragonDef: {
      name: "Minstrel",
      percentStats: { "Performance Regen": 50, "Critical Severity": 25, "Deflect Severity": 25 }
    },
    gear: { "Head": { name: "T", ratingStats: { "Forte": 89000 } } }
  });
  assertClose(r.stats["Class Resource Regen"].percentTotal, 25, 0.01,
    "Performance Regen routed to Class Resource Regen → +25");
  // Make sure no warning was emitted for an unknown stat
  assertEq(r.warnings.some(w => /Performance Regen/.test(w)), false,
    "no unknown-stat warning for Performance Regen");
}

// =============================================================
console.log(`\n${passes} pass, ${fails} fail`);
if (fails > 0) process.exit(1);
