# Webapp Dashboard Navigation IA Pattern

Use this reference when Chris asks to simplify or restructure the Hermes webapp dashboard navigation.

## Preferred IA when top navigation feels complex

- Keep the global header focused on broad parent groups only.
  - Example: `Team / Personal AX / Corporate AX / Weekly`.
- Move child tabs out of the global header and into the relevant workspace/body area.
  - `Personal AX`: `OBD Map / Research / Visual Archive`.
  - `Corporate AX`: `Chris Archive / Design DNA`.
  - `Team` and `Weekly`: no body child tabs unless Chris explicitly asks.
- Put contextual group explanation above body child tabs.
- Put the selected child tab title/description below the child tab row.
- Recommended reading order for grouped workspace pages:
  1. Group intro
  2. Body child tabs
  3. Active child tab title/description
  4. Actual content

## Interaction expectations

- The hamburger button should collapse/expand the parent header tabs as a group, not only child tabs.
- Preserve access to every existing child tab; moving tabs into the body must not make routes unreachable.
- Keep text-only tab treatment unless Chris asks for a stronger control style:
  - No card/stroke/background/radius treatment.
  - Active state primarily by text color.
  - Avoid active underline/line indicators if they create perceived layout jitter.

## Copy/documentation sync

When the navigation IA changes substantially:

- Update the app README with the current IA, child-tab placement, QA expectations, and deployment URL.
- If the app has a Weekly / changelog / update surface, add a concise in-app update summary there too.
- For nested app repos, verify the GitHub README URL at the actual app path (for example `.../blob/main/august-dashboard/README.md`) rather than assuming root `README.md` is the displayed project doc.

## QA probes to run

Use Playwright/computed-style probes, not only visual inspection:

- Header parent labels equal expected parent groups.
- Header child-tab count is `0` after moving child tabs into the body.
- Body child tabs appear only for the intended parent groups.
- Child tab clicks update the hash and active child state.
- Team/Weekly have no body child tabs unless requested.
- Hamburger closed state hides parent tabs (`display: none` or equivalent) and open state restores them.
- Topbar margin/gap values match the requested pixel tuning.
- Desktop/tablet/mobile overflow is false.
- If README/Weekly were updated, verify both live app DOM and GitHub/raw README content.
