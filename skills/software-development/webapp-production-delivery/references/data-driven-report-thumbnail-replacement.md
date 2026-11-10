# Data-driven report thumbnail replacement

Use when a user supplies an image for one research/dissertation/report idea in a static React app.

1. Copy the source into a stable, public path such as `public/assets/<section>/<idea>-hero.jpg`; do not overwrite a shared hero if sibling ideas use it.
2. Find the data record selected by that subtab and change only its `heroImage`/image field and accessible alt text.
3. Build and lint before browser QA.
4. In Playwright, navigate to the target route, click the named subtab, and assert:
   - active tab text is the target idea;
   - rendered hero `src` includes the new filename;
   - `img.complete` is true and natural dimensions are nonzero;
   - `document.documentElement.scrollWidth === window.innerWidth` at the relevant narrow viewport.
5. Commit the new binary and data-reference change together. Push, then confirm the static-host workflow is successful and fetch/check the deployed asset before saying it is live. If the workflow is still running, report local verification and the pending deployment distinctly.
