# Manifest-to-UI Reflection QA

Use this when a static/Vite dashboard is manifest-backed and the user says a newly published asset “is not reflected yet.” A manifest/direct-URL pass is not enough; prove the item is reachable in the rendered UI path the user will use.

## Proven loop

1. **Check live manifests and direct assets first.**
   - Fetch the live JSON with a cache-busting query for the latest commit.
   - Assert the new IDs/titles/status/image paths exist.
   - Fetch each direct image URL and verify status, content type, dimensions, and hash when available.

2. **Navigate to the actual UI lane.**
   - Do not inspect only the initial page DOM. Many dashboard sections are conditionally rendered after tab clicks.
   - Click the parent group and body-local tab path the user will use, e.g. `Corporate AX → Design DNA → DNA Dashboard`.
   - Capture the visible text, active tab labels, and URL/hash after navigation.

3. **Verify rendered cards, not only source data.**
   - Assert the new titles are present in `document.body.innerText` after the correct tab path.
   - Query the actual tile/button elements by title or accessible name.
   - Record visible order numbers when the item is lower in a list; tell the user where to find it.

4. **Image loading caveat for lazy thumbnails.**
   - Off-screen or lazy thumbnails may show `img.complete === false` and `naturalWidth === 0` in Playwright even when the network response is `200 image/png`.
   - Scroll target tiles into view and wait, but if `naturalWidth` still stays `0`, add request/response logging and a browser decode check:
     - `fetch(imageUrl) → blob → createImageBitmap(blob)` should return expected dimensions.
   - Report the distinction clearly: “card text is rendered; image requests return 200 and decode to 1024×1024; lazy `<img>` state may not have completed in the probe.”

5. **Final user report should include the navigation path.**
   - If the item is reflected but not on the first screen, say exactly where it appears, e.g. `Corporate AX → Design DNA → DNA Dashboard`, items `34–36`.
   - Avoid saying “reflected” based only on manifest/direct URL checks.

## Common pitfall

A false negative happens when the probe looks only at the initial route (e.g. Team home). A false positive happens when the agent checks only JSON/direct URLs and never confirms the rendered UI lane. Do both.