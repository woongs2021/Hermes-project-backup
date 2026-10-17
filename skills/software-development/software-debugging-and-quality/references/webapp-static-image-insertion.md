# Webapp static image insertion pattern

Use this when a user asks to place an attached/generated image into a specific section of a React/Vite/static webapp and deploy it.

## Durable workflow

1. **Preserve the requested placement language.** Identify the exact existing card/section the user named (for example, “OBD definition 다음”, “Research loop archive 밑”, “Monthly synthesis 밑”) and insert the image immediately after that DOM node, not merely somewhere in the same tab. When the user says “다른 탭들과 동일하게 타이틀 내용 밑에 배치,” treat the placement as: after the subtab’s hero/title-description card and before the next diagram/infographic/timeline/list. When names overlap across tabs or panels, verify which component is actually rendered for the requested route before editing; do not assume a similarly named imported/extended panel is the live page.
2. **Copy into a stable public asset path.** Use a page/section-specific path such as `public/assets/<page>/<semantic-name>.jpg`. If replacing an image, prefer keeping the public path stable and overwrite the asset so existing markup/URLs stay simple.
3. **Record intrinsic dimensions in markup.** Determine the image width/height and set the `<img width height>` attributes to match the actual file. If image libraries are unavailable, a small stdlib JPEG SOF parser is enough; avoid depending on local-only tools like `identify` being present.
4. **Use a shared wide-image card class.** For hero/section imagery, use a class that spans the grid (`grid-column: 1 / -1`), removes padding, hides overflow, and applies `object-fit: cover; object-position: center;`. When `.content-card` media queries reapply padding, add specific later overrides for every new image-card class.
5. **Verify placement by DOM order, not screenshots alone.** Browser probes should assert: the preceding card kicker/text, image card is the expected child index, next sibling class/kicker, image `complete`, `naturalWidth`, `naturalHeight`, `objectFit`, `overflow`, theme, and console/page errors across mobile/tablet/desktop. If the inserted selector is missing (`childIndex: -1` or `null`), treat it as a placement/component-routing failure, not a Playwright failure: re-check the app's active tab/render tree and remove any mistaken insertion from non-rendered or wrong-route panels before continuing.
6. **Verify static-host propagation.** After push, poll live HTML for new hashed assets; fetch the image URL and compare status/hash/length. Then run the same browser probe against the live URL before claiming deployment success.

## Image artifact cleanup before redeploy

When the user accepts an inserted image but asks to remove a visible line/band/artifact:

1. **Separate image pixels from CSS/frame artifacts.** Inspect whether the line is in the image itself, the figure background, border, shadow, or object-fit crop. If browser QA is unavailable, compare source pixels or use vision on the public asset before editing.
2. **Prefer stable-path replacement for small visual fixes.** Keep the existing public asset path and overwrite the image so JSX stays unchanged and the live URL can be hash-verified.
3. **Use the least destructive edit.** If the artifact is internal (for example a thin black line inside an object), avoid cropping the whole hero unless composition demands it. Patch only the affected rectangle with a nearby sampled tone or crop only the offending edge band.
4. **Verify the edit quantitatively and visually.** For line removal, measure the target rows/columns before and after (for example dark-pixel ratio), confirm dimensions still match the JSX intrinsic width/height, run build/lint, and verify the live URL returns the new byte length/hash.
5. **Report the verification honestly.** If no browser screenshot/geometry probe was possible, say the proof is asset-level/live readback rather than visual layout QA.

## Profile/avatar image insertion

When the image is a profile/avatar rather than a wide hero:

1. Reuse a canonical public asset path (`public/assets/team/<name>_profile.png|jpg`) instead of embedding Telegram cache names or generation URLs.
2. If the same person appears in multiple panels, wire all appearances to the same canonical asset so future refinements propagate consistently.
3. Match the local component pattern: rounded-square for profile explanation cards; existing circular `.obd-agent-face` for Operating Map node faces.
4. Set `width`, `height`, `loading`, and `decoding` in JSX, but verify the rendered CSS box. If CSS should make the avatar square and a fixed HTML height stretches it, add `height: auto` or an explicit CSS height.
5. For Operating Map-style node arrays, check data definitions as well as JSX; a missing face may be `faces: []` in the node data, not a rendering bug.
6. Browser QA should assert count, `src`, `alt`, `complete`, `naturalWidth/naturalHeight`, rendered rect, `object-fit`, border radius, and overflow on desktop/mobile.

## Common pitfalls

- A later `.content-card` mobile rule can silently reintroduce padding around full-bleed image cards. Add breakpoint-specific overrides for each image-card class and re-check actual `imgWidth` vs `imageCardWidth`.
- If a user says “same logic” or “same pattern” for another sibling tab/subtab, do not create a bespoke layout. Reuse the existing wide-image figure pattern, but add the new class in both places: the shared figure selector (`.<section>-image-card { ... }`) and the shared image selector (`.<section>-image-card img { ... }`). Missing the second selector leaves object-fit/height behavior inconsistent.
- For OBD subtabs in this webapp, the recurring accepted placement is: subtab hero/title-description card → inserted image card → infographic/diagram/list. Signal Loop and Operating Map both use `public/assets/obd/<semantic-name>.jpg`, intrinsic `1280 × 640`, and the shared full-width image-card styling.
- For the Visual Archive top-level tab in this webapp, distinguish the top workspace header from the internal carousel hero. If Chris says the image belongs under `Home visual system`, place `visual-archive-image-card` immediately after the workspace header and before `<HomeVisualHeroPanel />`, not inside `HomeVisualHeroPanel` after `home-visual-carousel-system`. Store these tab-level assets under `public/assets/visuals/<semantic-name>.jpg` and add the new class to both shared figure and shared `img` selectors.
- When browser QA is unavailable, still verify the deployed static artifact by polling live HTML for the new hashed JS/CSS assets, fetching the live image URL, and comparing status, byte length, and hash prefix. Phrase this as content/deployment verification, not a visual geometry claim.
- Do not confuse tab routing or page location with image placement; the acceptance criterion is the exact section order inside the page.
