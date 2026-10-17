const { chromium } = require('playwright');

const target = process.env.QA_URL;
if (!target) {
  console.error('Set QA_URL to the page URL to probe, e.g. QA_URL=http://127.0.0.1:60269/Hermes-project-webapp/#visuals');
  process.exit(2);
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 390, height: 844 }, isMobile: true });
  const errors = [];
  page.on('console', (msg) => {
    if (msg.type() === 'error') errors.push(msg.text());
  });
  page.on('pageerror', (err) => errors.push(err.message));

  await page.goto(target, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForSelector('.workspace-header h2', { timeout: 60000 });
  await page.waitForTimeout(800);

  const measure = async (label) => page.evaluate((stateLabel) => {
    const box = (el) => {
      if (!el) return null;
      const r = el.getBoundingClientRect();
      return { left: r.left, right: r.right, top: r.top, bottom: r.bottom, width: r.width, height: r.height };
    };
    const brand = document.querySelector('.brand-block');
    const h2 = document.querySelector('.workspace-header h2');
    const desc = document.querySelector('.workspace-header p:not(.eyebrow)');
    const firstCard = document.querySelector('.workspace .content-card');
    const nav = document.querySelector('.topbar .tab-nav');
    const hamburger = document.querySelector('.hamburger-button');
    const firstTab = document.querySelector('.topbar .tab-button');
    const ns = nav ? getComputedStyle(nav) : null;
    return {
      label: stateLabel,
      hash: location.hash,
      viewport: { width: innerWidth, height: innerHeight },
      overflowX: document.documentElement.scrollWidth - document.documentElement.clientWidth,
      hamburgerExpanded: hamburger?.getAttribute('aria-expanded') ?? null,
      navClass: nav?.className ?? null,
      nav: box(nav),
      firstTab: box(firstTab),
      navDisplay: ns?.display ?? null,
      navVisibility: ns?.visibility ?? null,
      navOpacity: ns?.opacity ?? null,
      navPointerEvents: ns?.pointerEvents ?? null,
      navMaxHeight: ns?.maxHeight ?? null,
      navBelowBrand: nav && brand ? nav.getBoundingClientRect().top >= brand.getBoundingClientRect().bottom : null,
      h2: box(h2),
      desc: box(desc),
      firstCard: box(firstCard),
      h2LeftDeltaVsCard: h2 && firstCard ? Math.round((h2.getBoundingClientRect().left - firstCard.getBoundingClientRect().left) * 10) / 10 : null,
      descLeftDeltaVsCard: desc && firstCard ? Math.round((desc.getBoundingClientRect().left - firstCard.getBoundingClientRect().left) * 10) / 10 : null,
      h2RightDeltaVsCard: h2 && firstCard ? Math.round((firstCard.getBoundingClientRect().right - h2.getBoundingClientRect().right) * 10) / 10 : null,
      tabCount: document.querySelectorAll('.topbar .tab-button').length,
    };
  }, label);

  const closed = await measure('closed');
  await page.click('.hamburger-button', { force: true });
  await page.waitForTimeout(300);
  const open = await measure('open-after-hamburger');

  const secondTab = page.locator('.topbar .tab-button').nth(1);
  if (await secondTab.count()) {
    await secondTab.click({ force: true });
    await page.waitForTimeout(300);
  }
  const afterSelect = await measure('after-select');

  await browser.close();
  console.log(JSON.stringify({ closed, open, afterSelect, errors }, null, 2));
})();
