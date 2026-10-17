# Webapp grouped text navigation and collapsible sub-tab QA

Use this reference when tuning Chris's Hermes webapp top navigation, especially when introducing top-level group tabs over existing child tabs.

## Session-proven pattern

- Preserve existing child tabs unless the user explicitly asks to remove them. A top-level group row should not make child tabs inaccessible.
- If child tabs should remain discoverable, render the full child tab row (`Team / OBD Map / Research / Visual Archive / Chris Archive / Design DNA / Weekly`) and use the top row as a grouping/context control.
- If the top row is a toggle, keep separate state for sub-tab visibility (for example `areSubTabsVisible`) and apply an explicit collapsed class to the child tab row.
- Top-level group buttons can still switch the active group/default tab, but avoid closing the mobile menu when the user needs to choose a child tab next.
- If Chris says the two-row header still feels too complex, move child tabs out of the topbar and into the relevant workspace body. Keep only the four parent groups in the header (`Team / Personal AX / Corporate AX / Weekly`), render child tabs conditionally in the body for groups that need them, and let the hamburger collapse/expand the parent group row itself.
- For that workspace-child-tab structure, `Team` and `Weekly` can remain simple pages with no body child tabs; `Personal AX` should expose only its body tabs (for example `OBD Map / Research / Visual Archive`), and `Corporate AX` should expose only its body tabs (for example `Chris Archive / Design DNA`). Prefer `group intro → body tabs → selected child tab title/description → content` when Chris asks for group explanations.
- For text-only navigation requested by Chris, remove card treatments: no stroke, no filled active surface, no border radius; active state should be color-only unless a specific line/indicator is requested.

## CSS pitfalls

Large, iteratively tuned CSS files can contain old navigation overrides much later in the file. A change near the primary `.tab-nav` definition may be silently undone by later rules.

Check for and override all of these patterns when refactoring the topbar:

```css
.topbar .tab-nav:not(.open) { display: none; }
.topbar .tab-nav { max-height: 0; overflow: hidden; }
.topbar .tab-nav.open { max-height: ...; }
.topbar .tab-nav { background: ...; backdrop-filter: ...; }
```

If the new structure uses a wrapper like `.tab-menu` and the child row no longer receives `.open`, explicitly cover both `.tab-nav`, `.tab-nav.open`, and `.tab-nav:not(.open)` in the final override, including dark-mode selectors if they exist.

For a text-only grouped nav, a robust final override shape is:

```css
.topbar .tab-group-nav,
.topbar .tab-nav,
.topbar .tab-nav.open,
.topbar .tab-nav:not(.open),
:root[data-theme='dark'] .topbar .tab-group-nav,
:root[data-theme='dark'] .topbar .tab-nav,
:root[data-theme='dark'] .topbar .tab-nav.open,
:root[data-theme='dark'] .topbar .tab-nav:not(.open) {
  position: static;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-height: none;
  overflow: visible;
  border: 0;
  padding: 0;
  background: transparent;
  box-shadow: none;
  backdrop-filter: none;
  opacity: 1;
  pointer-events: auto;
  transform: none;
  visibility: visible;
}

.topbar .tab-nav.collapsed,
.topbar .tab-nav.collapsed:not(.open),
:root[data-theme='dark'] .topbar .tab-nav.collapsed,
:root[data-theme='dark'] .topbar .tab-nav.collapsed:not(.open) {
  display: none;
}
```

## QA checklist

Use Playwright/computed-style probes, not visual judgment only:

### Two-row header child tabs

- Top group labels are present and centered.
- Child labels are present before collapse.
- Description `<small>` elements are removed when requested (`.tab-group-button small` count is `0`).
- `justify-content` for both group and child nav is `center` when requested.
- Child row height is greater than zero when expanded on desktop/tablet/mobile.
- Clicking a top group toggles child row to `display: none` and `aria-hidden="true"` if hidden.
- Clicking the same/top group again restores child row to visible (`display: flex`, height > 0, `aria-hidden="false"`).
- Active group indicators such as a `0.5px` line are verified via `getComputedStyle(button, '::after').height`.
- Every child tab is clickable after expansion and updates `location.hash` plus active child/group labels.
- Menu controls remain text-only: active and inactive buttons have `border: 0px`, transparent background, and no card radius/fill.
- Check desktop, tablet, and mobile; mobile often has legacy `.tab-nav:not(.open)` hiding rules.

### Header parent tabs + workspace child tabs

When child tabs have been moved into the workspace body, verify:

- Header/topbar contains only the parent labels (`Team / Personal AX / Corporate AX / Weekly`).
- Header child tab count is zero (`.topbar .tab-nav .tab-button` should be absent).
- The hamburger toggles the parent group row itself: closed state has the topbar menu visually hidden (`display: none` or equivalent hidden geometry), and open state restores the four parent tabs.
- `Personal AX` renders only its workspace child tabs (for example `OBD Map / Research / Visual Archive`), and clicking one updates the hash and active body tab.
- `Corporate AX` renders only its workspace child tabs (for example `Chris Archive / Design DNA`), and clicking one updates the hash and active body tab.
- `Team` and `Weekly` do not render workspace child tabs unless explicitly requested.
- If group explanations are present, assert DOM order and geometry: `.workspace-group-intro` before `.workspace-tab-nav`, `.workspace-tab-nav` before `.workspace-header`; confirm the selected child tab title/description appears below the body tabs.
- Probe desktop/tablet/mobile for overflow after each state transition.
