# Webapp mobile topbar geometry QA

Use this reference when modifying mobile/tablet top navigation, sticky headers, hamburger menus, or theme defaults in a static React/Vite webapp.

## Session-proven lessons

- Separate three acceptance targets that can sound similar in user language:
  1. **Topbar/background full-bleed**: the header surface reaches viewport edges.
  2. **Menu/nav row full-bleed**: the tab row reaches viewport left/right edges.
  3. **Tab buttons at viewport top**: the actual first tab/button starts at `top: 0`.
- Do not assume the user wants all three. If the user says the background should touch the edges, preserve the prior visual hierarchy unless they explicitly ask to move the menu/buttons.
- In a topbar containing `brand`, `theme`, `hamburger`, and `nav`, avoid moving `nav` above the title via `order: -1` or `grid-template-areas` unless that exact hierarchy change is requested.
- If the desired state is “background attached to top, title centered, menu below title,” verify:
  - `topbar.getBoundingClientRect().top === 0`
  - brand/title center is aligned to viewport center
  - `nav.top >= brand.bottom`
  - nav left/right insets match requested full-bleed behavior, often `0 / 0` on mobile/tablet
  - `documentElement.scrollWidth - clientWidth === 0`
- When multiple dark-mode selectors exist, include `:root[data-theme='dark'] ...` in final overrides if specificity otherwise resurrects old margins/padding.
- If the user asks for **mobile only**, do not broaden the change to tablet/desktop. Make the breakpoint explicit (for this webapp, `max-width: 560px`) and verify only the mobile viewport unless the user asks otherwise.

## Mobile hamburger tab containment

When Chris says mobile top tabs should be “inside the hamburger,” treat it as a state + CSS requirement, not just a visual restyle:

1. **Initialize state by viewport.** If React state defaults `isMenuOpen` to `true`, the mobile menu will appear open even if collapsed CSS exists. Use a viewport-aware initializer such as mobile closed / larger screens open when preserving desktop behavior.
2. **Close after selection on mobile.** In the tab selection handler, close the menu for the mobile breakpoint so the page content returns immediately after navigation.
3. **Use an unambiguous closed state.** For the mobile closed menu, prefer `.tab-nav:not(.open) { display: none; }` plus hidden/zero-height styles. This prevents invisible tab buttons from retaining boxes, focus/click surfaces, or extra vertical spacing.
4. **Verify three states.** Probe initial closed state, hamburger-open state, and after-select state. Required evidence: `aria-expanded`, nav class, `display`, `visibility`, `opacity`, pointer-events, first-tab bounding box, `navBelowBrand`, tab count, and `overflowX`.

## Mobile page-title margin alignment

When Chris says mobile page titles look stuck to the edges, compare the title/description to the **card body text inset**, not simply the viewport edge or the outer `.content-card` border.

- In this webapp, mobile `.workspace` and `.content-card` can both sit near viewport edges while card text has about a 20px inner inset. Align `.workspace-header h2` and description to that inner text rhythm with mobile-only `padding-inline`, and verify the left/right deltas against the first visible card.
- Also check section-level intro blocks that are not `.content-card`. In the OBD tab, `.obd-subtab-intro` renders the visible “About OBD” title/description outside the card body, so mobile title-margin fixes must include mobile-only `.obd-subtab-intro { padding-inline: 20px; }` and verify its kicker/h3/p deltas too.
- Report the measured relationship clearly, e.g. “title/description are 20px inside the card edge, matching card body margin,” instead of saying only “aligned.”

## Theme default changes

- Changing the default theme should not overwrite a stored user choice unless explicitly requested.
- Test two states:
  1. Clear/empty `localStorage` → default theme is the requested value.
  2. Existing `localStorage['august-dashboard-theme'] = 'dark' | 'light'` → stored value is still respected.

## Useful browser probe fields

For mobile/tablet/desktop, capture:

- `document.documentElement.dataset.theme`
- `getComputedStyle(document.documentElement).colorScheme`
- `topbar`, `brand`, `brandButton`, `themeButton`, `hamburgerButton`, `nav`, and first tab bounding boxes
- `brandCenterDelta = abs(brand.center - viewportWidth / 2)`
- `navBelowBrand = nav.top >= brand.bottom`
- `navInsetLeft`, `navInsetRight`, `navInsetTop`, `firstInsetTop`
- `overflowX`
- exact served JS/CSS asset names (local preview and live host) so geometry probes are attached to the current build, not a stale preview process
- console and page errors

## Preview and hosted-build verification pitfalls

- Before trusting a local preview probe, fetch the served HTML and confirm its hashed JS/CSS asset names match the freshly built `dist/index.html`. Old `vite preview` processes on common ports can silently serve a different worktree or previous build.
- If a fixed port is busy, do not assume your new preview started. Use `--strictPort`, inspect the background process log, then pick a truly free high port and point the probe at that port.
- For live GitHub Pages or other static hosts, poll the live HTML until the expected hashed JS/CSS appears. Then run the mobile browser probe against the live URL. For pages with large image/video assets, use `domcontentloaded` + wait for a required selector rather than `networkidle`, which can hang even after the relevant DOM/CSS is ready.

## Reporting nuance

When reporting geometry fixes, distinguish clearly between:

- “header/background is attached to the viewport top,” and
- “the menu row/button itself starts at viewport top.”

This prevents a future agent from over-correcting layout hierarchy when the user only wanted edge alignment.