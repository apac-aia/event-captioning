// Boundary tests for Zoom licensing advice in index.html.
// Run: node tests/zoom-plan.test.js
// Extracts the real functions/data from index.html (no build step, no deps).
const fs = require("fs");
const path = require("path");
const assert = require("assert");
const html = fs.readFileSync(path.join(__dirname, "..", "index.html"), "utf8");

// all inline scripts must parse
[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].forEach(m => new Function(m[1]));

// safe: evaluating our own repo's source, not untrusted input
const pick = re => {
  const m = html.match(re);
  assert(m, "pattern not found: " + re);
  return m[0];
};
// const declared inside eval stays in eval scope; var leaks to module scope
eval(pick(/const PLATFORMLABEL=\{[\s\S]*?\};/).replace(/^const /, "var "));
eval(pick(/const ZOOM_PLANS=\[[\s\S]*?\n\];/).replace(/^const /, "var "));
eval(pick(/function zoomPlanAdvice\(n\)\{[\s\S]*?\n\}/));
eval(pick(/function platformCapacityNote\(\)\{[\s\S]*?\n\}/));

const adviceText = n => {
  const a = zoomPlanAdvice(n);
  return [a.main, a.alt, a.extra].filter(Boolean).join("；");
};

// capacity boundaries (official: Basic/Pro 100, Business 300, Enterprise 500, LM 500/1000)
assert(adviceText(100).includes("Pro"), "100 -> Pro");
assert(!adviceText(100).includes("Business"), "100 must not need Business");
assert(adviceText(101).includes("Business（300 人）"), "101 -> Business preferred");
assert(adviceText(101).includes("Large Meeting 500"), "101 -> Pro+LM500 alternative shown");
assert(adviceText(150).includes("Business"), "150 -> Business");
assert(!/Pro（100 人）/.test(adviceText(150)), "150 must not recommend bare Pro");
assert(adviceText(300).includes("Business"), "300 -> Business");
assert(adviceText(301).includes("Large Meeting 500") && adviceText(301).includes("Enterprise"), "301 -> LM500 or Enterprise");
assert(adviceText(500).includes("Large Meeting 500") || adviceText(500).includes("Enterprise"), "500 stays in 301-500 band");
assert(/Webinar|Events/.test(adviceText(501)), "501 -> Webinar/Events tier");
assert(adviceText(501).includes("Zoom 確認"), "501 -> contact Zoom");

// 150 + all-day + translated captions end-to-end string
global.state = { format: "hybrid", platform: "zoom", onlinePeople: 150 };
let note = platformCapacityNote();
assert(note.includes("Business（300 人）"), "150 note recommends Business");
assert(note.includes("Translated Captions"), "150 note points to TC licensing");
assert(note.includes("30 小時"), "150 note covers all-day duration");
assert(note.includes("Large Meeting 500"), "150 note offers Pro+LM500 alternative");

// empty concurrent count -> ask to fill, never derive from event size
global.state = { format: "hybrid", platform: "zoom", onlinePeople: null };
note = platformCapacityNote();
assert(note.includes("同時連入"), "empty -> ask for concurrent count");
assert(note.includes("活動總人數不能拿來推定"), "empty -> forbids deriving from total attendance");

// translated captions discipline in plan data
const pro = ZOOM_PLANS.find(p => p.name === "Workplace Pro");
const biz = ZOOM_PLANS.find(p => p.name === "Workplace Business");
assert(pro.tc.startsWith("不含"), "Pro must not claim included TC");
assert(biz.tc.startsWith("不自動內含"), "plain Business must not claim auto-included TC");
const tcAddon = ZOOM_PLANS.find(p => p.name.includes("Translated Captions"));
assert(tcAddon.tc.includes("主持"), "TC add-on assigned to host account");
assert(tcAddon.use.includes("洽 Zoom 銷售"), "TC pricing deferred to Zoom sales");
ZOOM_PLANS.forEach(p => ["name", "cap", "dur", "tc", "rec", "use"].forEach(k => assert(p[k], `plan ${p.name} missing ${k}`)));
ZOOM_PLANS.forEach(p => assert(!/\$\s?\d/.test(p.tc + p.use), `no fixed price in plan ${p.name}`));

// plan card metadata: check date + all five official links wired on the Zoom tool object itself
assert(/plansChecked:ZOOM_CHECK_DATE/.test(html) && /const ZOOM_CHECK_DATE="\d{4}-\d{2}-\d{2}"/.test(html), "check date present");
const zoomAssign = pick(/Object\.assign\(TOOLS\.find\(t=>t\.name\.startsWith\("Zoom "\)\),\{[\s\S]*?\n\}\);/);
["KB0068002", "KB0067966", "KB0065116", "KB0059081", "KB0063899"].forEach(kb =>
  assert(zoomAssign.includes(kb), "official source not wired on Zoom tool object: " + kb));

console.log("zoom-plan tests OK");
