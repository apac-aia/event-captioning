// Placement tests for the tutorial highlight card in index.html.
// Run: node tests/tour-card.test.js
// Verifies the card never gets squeezed below viewport height and does not
// cover its highlighted target when there is room beside it.
const fs = require("fs");
const path = require("path");
const assert = require("assert");
const html = fs.readFileSync(path.join(__dirname, "..", "index.html"), "utf8");

// safe: evaluating our own repo's source, not untrusted input
const fn = html.match(/function placeTourCard\(target\)\{[\s\S]*?\n\}/)[0];
const clampSrc = html.match(/function clamp\(n,min,max\)\{[^\n]*\}/)[0];
const card = { style: {}, get offsetHeight() { return this._h; }, _h: 0 };
global.document = { querySelector: () => card };
eval(clampSrc + "\n" + fn);

const target = (top, left, width, height) => ({
  getBoundingClientRect: () => ({ top, left, width, height, bottom: top + height, right: left + width })
});
const px = v => parseInt(v, 10);

// desktop 1280x800: card below target, full-viewport max-height, no overlap
global.window = { innerWidth: 1280, innerHeight: 800 };
card._h = 320;
placeTourCard(target(80, 40, 120, 48));
assert.equal(px(card.style.maxHeight), 800 - 24, "maxHeight = viewport - margins");
assert.equal(px(card.style.top), 80 + 48 + 14, "placed below target");
assert(px(card.style.top) >= 80 + 48, "card does not cover target when below fits");

// desktop: target near bottom -> placed above, no overlap
card._h = 320;
placeTourCard(target(700, 40, 120, 48));
assert.equal(px(card.style.top), 700 - 14 - 320, "placed above target");
assert(px(card.style.top) + card._h <= 700, "card does not cover target when above fits");

// iPhone SE 375x667: long step text still fits below top target, buttons visible
global.window = { innerWidth: 375, innerHeight: 667 };
card._h = 480;
placeTourCard(target(60, 10, 140, 44));
assert.equal(px(card.style.width), 375 - 24, "card width fits SE viewport");
assert.equal(px(card.style.maxHeight), 667 - 24, "SE max-height uses full viewport");
assert.equal(px(card.style.top), 60 + 44 + 14, "SE: below target");
assert(px(card.style.top) + card._h <= 667 - 12, "SE: card bottom (buttons) inside viewport");

// 320px reflow width: card never wider than viewport
global.window = { innerWidth: 320, innerHeight: 568 };
card._h = 500;
placeTourCard(target(40, 8, 100, 40));
assert(px(card.style.width) <= 320 - 24, "320px: no horizontal overflow");
assert(px(card.style.left) >= 12, "320px: left margin kept");

// tiny viewport, card taller than either side -> pinned opposite target, capped to viewport
global.window = { innerWidth: 360, innerHeight: 640 };
card._h = 616;
placeTourCard(target(60, 10, 100, 40));
assert.equal(px(card.style.top), 640 - 12 - 616, "pinned opposite target half");

console.log("tour-card tests OK");
