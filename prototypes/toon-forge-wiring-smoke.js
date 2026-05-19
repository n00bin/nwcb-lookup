// Smoke-test the prototype's adapter + score + quick-stats wiring
// by loading all dependencies in a Node sandbox and calling them.
//
//   node prototypes/toon-forge-wiring-smoke.js

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const sandbox = { window: {}, console: console };
vm.createContext(sandbox);

function loadInto(rel) {
  const src = fs.readFileSync(path.join(__dirname, "..", rel), "utf-8");
  vm.runInContext(src, sandbox);
}
function loadHere(file) {
  const src = fs.readFileSync(path.join(__dirname, file), "utf-8");
  vm.runInContext(src, sandbox);
}

loadInto("data/classes.js");
loadInto("data/races.js");
loadInto("data/gear.js");
loadInto("data/artifacts.js");
loadInto("data/companion-gear.js");
loadInto("data/campaign-boons.js");
loadInto("data/guild-boons.js");
loadInto("toon-forge-stats.js");
loadInto("toon-forge-engine.js");

// Probe loaded data via inside-the-sandbox length checks.
const counts = vm.runInContext(`({
  classes:   typeof CLASSES_DATA === "undefined"   ? -1 : CLASSES_DATA.length,
  races:     typeof RACES_DATA === "undefined"     ? -1 : RACES_DATA.length,
  gear:      typeof GEAR_DATA === "undefined"      ? -1 : GEAR_DATA.length,
  artifacts: typeof ARTIFACTS_DATA === "undefined" ? -1 : ARTIFACTS_DATA.length,
  companionGear: typeof COMPANION_GEAR_DATA === "undefined" ? -1 : COMPANION_GEAR_DATA.length,
})`, sandbox);
console.log("Loaded:");
console.log("  CLASSES_DATA classes:    ", counts.classes);
console.log("  RACES_DATA races:        ", counts.races);
console.log("  GEAR_DATA items:         ", counts.gear);
console.log("  ARTIFACTS_DATA artifacts:", counts.artifacts);
console.log("  COMPANION_GEAR entries:  ", counts.companionGear);

// ----- replicate the prototype's adapter + score logic -----
const adapterScript = `
function findClass(name) {
  if (!name || typeof CLASSES_DATA === "undefined") return null;
  for (var i = 0; i < CLASSES_DATA.length; i++) {
    if (CLASSES_DATA[i].name === name) return CLASSES_DATA[i];
  }
  return null;
}
function findParagon(className, paragonName) {
  var cls = findClass(className);
  if (!cls || !paragonName) return null;
  for (var i = 0; i < cls.paragonPaths.length; i++) {
    if (cls.paragonPaths[i].name === paragonName) return cls.paragonPaths[i];
  }
  return null;
}
function findRace(name) {
  if (!name || typeof RACES_DATA === "undefined") return null;
  for (var i = 0; i < RACES_DATA.length; i++) {
    if (RACES_DATA[i].name === name) return RACES_DATA[i];
  }
  return null;
}
function buildEngineCharacter(s) {
  return {
    totalItemLevel: Number(s.il) || 0,
    class:    s.class    || "",
    paragon:  s.paragon  || "",
    paragonDef: findParagon(s.class, s.paragon),
    role:     s.role     || "",
    race:     findRace(s.race),
    abilityScores: s.abil,
    gear: {}, artifacts: {}, companionGear: {},
    campaignBoons: {}, guildBoons: [], buffs: []
  };
}
this.buildEngineCharacter = buildEngineCharacter;
this.findRace = findRace;
this.findParagon = findParagon;
`;
vm.runInContext(adapterScript, sandbox);

// ----- scenarios -----
function run(label, state) {
  const ec = sandbox.buildEngineCharacter(state);
  const r = sandbox.window.TOON_FORGE_ENGINE.computeStats(ec);
  console.log(`\n[${label}]`);
  console.log("  TIL:", ec.totalItemLevel, "race:", state.race || "(none)", "paragon:", state.paragon || "(none)");
  const interesting = ["Power", "Combat Advantage", "Critical Severity", "Action Point Gain", "Control Resist", "Forte", "Class Resource Regen"];
  for (const n of interesting) {
    const s = r.stats[n];
    if (!s) continue;
    if (s.finalPct === 0 && s.flat === 0) continue;
    console.log(`  ${n.padEnd(22)} finalPct=${s.finalPct.toFixed(1).padStart(6)} (rating=${s.ratingContribPct.toFixed(1)} + pct=${s.percentTotal.toFixed(1)})`);
  }
  if (r.warnings.length) {
    console.log("  warnings:", r.warnings);
  }
}

run("empty character", { il: "", class: null, paragon: "", race: "", role: null, abil: {} });
run("Sun Elf only", { il: "89000", class: "Wizard", paragon: "", race: "Sun Elf", role: "dps", abil: {} });
run("Sun Elf + Arcanist (forte kicks in)",
  { il: "89000", class: "Wizard", paragon: "Arcanist", race: "Sun Elf", role: "dps", abil: {} });
run("Bard Minstrel + Half-Elf (alias routing)",
  { il: "89000", class: "Bard", paragon: "Minstrel", race: "Half-Elf", role: "heal", abil: {} });

console.log("\nWiring smoke test passed (no exceptions thrown).");
