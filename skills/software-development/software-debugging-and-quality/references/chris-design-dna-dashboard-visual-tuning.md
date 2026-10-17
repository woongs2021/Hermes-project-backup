# Chris Design DNA Dashboard Visual Tuning

Use when editing Chris's Hermes webapp Design DNA / DNA Dashboard / Chris Archive visual surfaces.

## Proven workflow

1. Treat Design DNA visual edits as production UI polish, not content-only work.
2. Make the smallest CSS/manifest change, then run `npm run build:public`.
3. Verify both local preview and hosted GitHub Pages when the change is visible to Chris.
4. For GitHub Pages, poll the live HTML for the current hashed CSS/JS asset and fetch that CSS before claiming deployment. Cache-busted query strings on the page are not enough if the HTML still points at an older hash.
5. Use Playwright computed-style probes across desktop/tablet/mobile instead of relying on screenshots.

## Design DNA image sizing pattern

For the three Design DNA images (hero, Core DNA, Expression Layer), keep the same responsive image-card sizing as other dashboard tabs:

- wrapper width: `100%`
- wrapper height: `clamp(220px, 34vw, 420px)`
- image width/height: `100%`
- `object-fit: cover`
- `object-position: center`

Verify all three rendered wrappers have identical heights at representative breakpoints:

- desktop around 1440px
- tablet around 834px
- mobile around 390px

## Typography and copy-block alignment pattern

When Chris says Design DNA title/body type should match other tabs, avoid special oversized hero typography. Prefer measuring the nearest accepted section rather than guessing. In this session the reference was Chris Archive overview.

Chris Archive overview metrics to mirror for Design DNA hero and DNA Dashboard overview:

- title width: `760px` at desktop
- body width: `760px` at desktop
- title/body vertical gap: `12px`
- title margin-bottom: `0.75rem`
- title font-size: `clamp(1.7rem, 2.6vw, 3rem)`
- title `font-weight: 420`, `line-height: 0.98`, `letter-spacing: -0.07em`
- body copy baseline: 16px / 25.28px line-height unless the app's global typography changes

Verify by probing title/body bounding boxes for both the reference tab and the edited Design DNA sections. If hosted CSS looks stale, create a fresh browser context/no-cache route and confirm the live stylesheet hash first.

## Public-facing Design DNA copy tone

Chris rejected overly direct/internal text and awkward AI-brand phrasing. For Design DNA / DNA Dashboard copy:

- Avoid terms like `조용한 지능` when it sounds like AI jargon rather than human language.
- Avoid internal workflow phrases in public UI copy: `저장해줘`, `썸네일을 클릭하면 생성 프롬프트와 분석 결과`, raw prompt/analysis plumbing.
- Prefer human product/design language: understanding a person's situation/intention, supporting better design judgment, selected graphic materials, future use in brand surfaces/package/UI/signal graphics.
- When a visual implies a conceptual count (e.g. a split-circle image implying two expression axes), adjust the heading and card count to match the visual instead of preserving stale copy.

## Flat image-surface preference

For Design DNA image cards, Chris preferred less decoration after size alignment:

- remove stroke/border from all three image wrappers
- remove box shadows
- remove surrounding gradient washes from the Core DNA and Expression Layer content-card wrappers
- keep sizing intact after removing decoration

Computed-style checks to run:

- `.design-dna-hero-image`, `.design-dna-section-hero-image`: `borderTopWidth === "0px"`, `boxShadow === "none"`
- `.design-dna-axis-map`, `.expression-layer-map`: `backgroundImage === "none"`
- no horizontal overflow on desktop/mobile

## Markdown principles modal pattern

For Design DNA system principles, mirror Chris Archive's document pattern:

- put the `.md` in `public/docs/`
- expose a view button that opens a modal with fetched markdown text
- expose an `<a download>` button for the same file
- verify the modal text contains the updated principle keywords and the download href points to the doc

## Common pitfalls

- Do not claim the hosted page is updated after only `git push`; wait for the live hashed asset to change or fetch the current CSS and confirm the new rules are present.
- Do not confuse manifest/data correctness with visual acceptance. For visual changes, probe actual DOM geometry and computed CSS.
- Do not leave one hero image using a max-width/aspect-ratio path while the other two use fixed responsive height; Chris notices cross-section inconsistency.
- If a Playwright lazy image check returns `naturalWidth = 0`, scroll/decode the images or verify the asset URLs directly before treating it as a broken image.
