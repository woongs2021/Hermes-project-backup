# Webapp OBD Signal Loop card consolidation

Use when Chris asks to simplify or reorganize the Hermes webapp OBD Map / Signal Loop section.

## User preference signal

Chris prefers the Signal Loop to avoid duplicated structures such as:

- a separate 5-step arrow summary, followed by
- another 5-card/detail timeline repeating the same stages.

Instead, merge the loop into one readable 5-card flow where each card contains the summary and detail together.

Updated preference from the 2026-09-03 iteration:

- Keep the five cards connected by visible arrows.
- Prefer a vertical sequence for this Signal Loop section, even on desktop, because it reads as a process rather than a gallery.
- Use distinct card accent colors so the five steps feel differentiated.
- Do **not** over-emphasize the numbering. Avoid circular number badges, gradient-filled number chips, heavy shadows, or button-like number treatments. Use colored number text only.

## Implementation pattern

1. Find the OBD Map / Signal Loop component, usually `ObdGrowthTimelinePanel` and `SignalLoopInfographic` in `extendedPanels.tsx`.
2. Identify whether the same source array, such as `obdMilestones`, is rendered twice.
3. Replace the duplicate views with a single vertical card flow:
   - one card per milestone,
   - step number as plain colored text,
   - lens/kicker,
   - title,
   - short output/summary,
   - detail paragraph,
   - a small downward arrow between cards.
4. Remove the repeated timeline/rail DOM rather than hiding it with CSS.
5. For this section, do not use a cramped 5-column desktop layout or even a 3+2 layout if Chris asks for process clarity. Prefer:
   - desktop: one vertical column with a comfortable max width,
   - tablet: one vertical column,
   - mobile: one vertical column.
6. Card differentiation should come from subtle background tint, border color, and accent text color. Numbering should be restrained: text only, no circle/gradient/shadow.

## Verification pattern

Run normal data/build checks, then a browser DOM/geometry/style probe:

- exactly 5 merged cards, e.g. `.signal-loop-detail-card` count is 5,
- exactly 4 connector arrows, e.g. `.signal-loop-card-arrow` count is 4,
- old timeline cards count is 0,
- old signal-loop node count is 0,
- each card has both output and detail text,
- card rectangles are vertically ordered and left-aligned,
- desktop/tablet/mobile horizontal overflow is 0,
- number text colors are differentiated,
- number text has no badge treatment: background `none`, border radius `0px`, box shadow `none`.

If the user says not to capture screenshots, do not create or send screenshots. Use DOM/computed-style checks and live URL confirmation instead.

If using Vite dev server, confirm the served page is fresh dev output rather than an old static `dist` bundle by checking HTML module paths (`/@vite/client` and `/src/main.tsx`).
