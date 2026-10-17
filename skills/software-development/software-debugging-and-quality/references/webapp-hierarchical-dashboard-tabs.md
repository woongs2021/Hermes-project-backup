# Webapp hierarchical dashboard tabs

Use this reference when Chris asks to simplify grouped/top dashboard navigation.

## Session-proven pattern

When a two-row header nav feels visually complex, move child/leaf tabs out of the global header and into the relevant page body.

Preferred structure:
- Header/topbar keeps only parent groups, e.g. `Team / Personal AX / Corporate AX / Weekly`.
- Do not render leaf tabs in the header.
- Render body-local tabs only for parent groups that genuinely need them:
  - `Personal AX`: `OBD Map / Research / Visual Archive`
  - `Corporate AX`: `Chris Archive / Design DNA`
  - `Team` and `Weekly`: no body subtab row unless explicitly requested.
- The top-right hamburger should collapse/expand the parent topbar tabs themselves, not only child tabs.
- Keep text-only styling unless Chris asks otherwise: no stroke/card/background/radius; active state by text color.

## Implementation checklist

1. Compute the active parent group from the active leaf tab.
2. Header JSX should map only parent groups (`tabGroups`) to topbar buttons.
3. Body JSX should compute `bodyTabs` only for parent groups with children that belong in content.
4. Body tab click should switch active leaf tab without closing the hamburger/topbar unexpectedly.
5. Hamburger state should apply to the parent tab container:
   - closed: parent menu not visible, e.g. `display: none`, no pointer events.
   - open: parent menu visible, e.g. `display: grid` or flex container.
6. Remove stale header child-tab DOM or verify it is not rendered; hiding stale DOM is not enough.

## Playwright verification fields

For desktop/tablet/mobile, verify:
- Header parent labels exactly: `Team`, `Personal AX`, `Corporate AX`, `Weekly`.
- Header child tab count is `0`.
- `Personal AX` shows body tabs: `OBD Map`, `Research`, `Visual Archive`.
- Body child click updates hash and active child, e.g. `Research` -> `#research`.
- `Corporate AX` shows body tabs: `Chris Archive`, `Design DNA`.
- `Team` and `Weekly` have `workspaceTabCount === 0`.
- Hamburger closed state hides parent tab menu; reopening restores parent labels.
- `document.documentElement.scrollWidth <= innerWidth` to catch overflow.

## Pitfalls

- A two-row header can still feel too complex even if it is technically usable. If Chris says it is complex, simplify information architecture rather than tweaking spacing again.
- Do not leave old `.tab-nav` header selectors controlling visibility after moving tabs into body; late CSS overrides can make the body/header relationship confusing.
- Do not use active underline/pseudo-lines for collapsing tab controls; they can create perceived layout jitter.
