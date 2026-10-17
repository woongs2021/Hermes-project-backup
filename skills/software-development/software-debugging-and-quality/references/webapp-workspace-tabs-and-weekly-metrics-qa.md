# Webapp workspace tabs and Weekly metrics QA

Use this reference for Chris's Hermes Project Webapp when tuning body-local tabs, Design DNA internal section tabs, or Weekly metric-card counts.

## Body-local workspace tabs

Scope: Personal AX and Corporate AX body tabs such as `OBD Map`, `Research`, `Visual Archive`, `Chris Archive`, and `Design DNA`.

Session-proven implementation pattern:
- Keep the parent topbar unchanged; apply changes only to `.workspace-tab-nav` / `.workspace-tab-button` unless Chris asks for global nav changes.
- If Chris wants an animated underline, prefer a single `.workspace-tab-indicator` element inside the nav rather than per-button pseudo-elements. This avoids layout jitter and gives one underline that moves by updating CSS variables.
- In React, keep a `useRef<HTMLElement | null>` for the nav, then on `activeTab.id` and body-tab count changes:
  - find `.workspace-tab-button.active`;
  - compute active button rect relative to nav rect;
  - set `--workspace-tab-indicator-left`, `--workspace-tab-indicator-width`, and opacity on the nav;
  - update again on `requestAnimationFrame` and on `resize`.
- CSS indicator baseline:
  - `position: absolute; bottom: 0; height: 2px; border-radius: 999px; background/currentColor: var(--primary);`
  - transition `left`, `width`, and `opacity` with a gentle cubic-bezier;
  - include `@media (prefers-reduced-motion: reduce) { transition: none; }`.
- When Chris asks for exact size/spacing, verify computed pixels rather than relying on CSS text. Example checks: active tab font-size, nav margin-top/bottom, indicator width/left vs active button width/left, transition property, overflow.
- Current proven body-local tab spacing baseline after Chris feedback: `.workspace-tab-nav { margin: 0 0 12px; padding: 0 0 10px; }`. If Chris asks to tighten/loosen the Personal AX / Corporate AX subtab vertical spacing, patch the nav margin rather than changing button padding or topbar/global nav. Verify both groups because Personal AX and Corporate AX share the same selector.

## Design DNA internal section tabs

Scope: the three internal tabs inside the Design DNA tab: `Design DNA`, `DNA Dashboard`, and `DNA Brand Asset` (`.design-dna-section-tabs`, `.design-dna-section-tab`).

Chris preference from this session:
- Remove wrapper/card-like stroke around these three tabs when it feels boxed-in.
- Remove per-button and active-tab stroke/background when asked for a flatter treatment.
- Reduce overly bold section tab titles to semi-bold; verified target was `font-weight: 650`.
- Remember dark-mode overrides may reintroduce background or active surfaces; explicitly verify both light and dark computed styles.
- Mobile overrides can re-add padding/radius; check mobile computed padding/radius as well.

Verification probe fields:
- labels exactly: `Design DNA | DNA Dashboard | DNA Brand Asset`.
- `.design-dna-section-tabs`: border width `0px`, transparent background, padding `0px`, radius `0px` when flattened.
- `.design-dna-section-tab`: border width `0px`.
- `.design-dna-section-tab.active`: border width `0px`, transparent background.
- title span `font-weight: 650` for semi-bold treatment.
- test desktop and mobile, light and dark.

## DNA Dashboard selected-asset deletion / pruning

When Chris says a specific DNA Dashboard item can be deleted, remove it by stable title/id across all persistence layers, not just the visible tile:
- Delete the entry from `public/data/dna-archive.json` and verify the item count decreases.
- Delete the matching `public/assets/dna-archive/<date>/<file>` asset so the URL returns 404/HTTPError after deploy.
- If the item came from a selected archive batch, delete it from `/opt/data/dna-archive/selected/<date>/selected-manifest.json` and remove the selected image file there too.
- If the item was included in a public method card or public Markdown method document, update those axis lists so the deleted style no longer appears as an active/public axis; if useful, keep only a short deletion note in the doc.
- Build, deploy, then verify live: deleted title absent from body text/DNA Dashboard, same-day tile count updated, public asset URL no longer resolves, remaining tiles still render, and desktop/mobile overflow remains zero.

## DNA Dashboard Midjourney rail additions

When adding Chris-attached manual Midjourney images to the `DNA Dashboard > Midjourney` rail:
- Update `public/data/midjourney-dna-archive.json`, not `public/data/dna-archive.json`.
- Continue the visible numbering sequence from the existing Midjourney rail. The UI sorts by `created` then `title`, so title prefixes such as `Midjourney 17 — ...` keep same-day additions ordered.
- Copy images into `public/assets/dna-archive/midjourney/YYYY-MM-DD/` and ensure the manifest `imageSrc` points there.
- If preserving original archives, mirror them under `/opt/data/dna-archive/midjourney/YYYY-MM-DD/images/` plus an archive-side manifest.
- Verify dimensions and hashes before claiming saved; 1:1 images should remain square.
- Build and then test both desktop and mobile live UI by navigating: `Corporate AX → Design DNA → DNA Dashboard → Midjourney`.
- QA assertions: total saved asset count increased, today’s new tiles have expected titles and numbers, all tile images decode, one detail modal shows `sourceTool: Midjourney`, prompt and analysis text, console/page errors are empty, and overflow is zero.

## Weekly metric-card counts

When Chris asks to show data-counting in Weekly:
- Prefer integrating counts into the existing Weekly metric grid (`monthly-metric-grid` / `metric-card monthly-metric`) instead of creating a separate standalone count card if he wants the lower Weekly content simplified.
- Count from public manifests rather than hardcoding UI values:
  - `research-board.json`: total papers, latest-week weekly papers, GO signals.
  - `chris-archive.json`: Chris Archive references.
  - `dna-archive.json` + `midjourney-dna-archive.json` + `brand-mockup-assets.json`: Design DNA outputs.
  - `home-visual-set.json`: Visual Archive.
  - Indexed total = total papers + Chris Archive + Design DNA + Visual Archive.
- Verify the removed standalone copy is absent if replacing it: `Weekly count · Research / Archive / Design DNA`.
- Verify metric labels render across desktop/tablet/mobile and overflow is zero.
