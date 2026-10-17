# Webapp body-tab indicator and Weekly metrics QA

Use this reference for Chris's Hermes Project Webapp when tuning body-local tabs under `Personal AX` / `Corporate AX`, or when integrating Weekly data counts into the existing Weekly synthesis metric grid.

## Body-local tab styling pattern

Relevant body tabs:
- Personal AX: `OBD Map`, `Research`, `Visual Archive`
- Corporate AX: `Chris Archive`, `Design DNA`

When Chris asks for an active underline with natural movement:
1. Keep the underline on body-local tabs only, not the parent topbar tabs.
2. Prefer one shared indicator element inside `.workspace-tab-nav` over per-button borders/pseudo-elements. This prevents layout height shifts and makes movement smoother.
3. Add a `ref` to the nav and compute the active button's bounding box after each active-tab change:
   - `--workspace-tab-indicator-left`
   - `--workspace-tab-indicator-width`
   - `--workspace-tab-indicator-opacity`
4. Render `<span className="workspace-tab-indicator" aria-hidden="true" />` after the tab buttons.
5. Position the indicator absolutely at nav bottom and animate `left`, `width`, and `opacity`.
6. Add `prefers-reduced-motion: reduce` to disable the transition.

Session-proven CSS values after Chris correction:
- `.workspace-tab-button span { font-size: 17px; }`
- `.workspace-tab-nav { margin: 6px 0 18px; padding: 0 0 10px; }`
- `.workspace-tab-indicator { height: 2px; transition: left 260ms cubic-bezier(0.22, 1, 0.36, 1), width 260ms cubic-bezier(0.22, 1, 0.36, 1), opacity 160ms ease; }`

Pitfall: Chris may like the underline animation but still tune font/spacing afterward. Preserve the animation behavior unless explicitly asked to remove it; adjust font and margins independently.

## Weekly metrics integration pattern

When Chris asks to show total counts in Weekly:
- Do not add a separate standalone `Weekly count · Research / Archive / Design DNA` card if he asks to keep the existing Weekly synthesis structure.
- Integrate counts into the existing `monthly-metric-grid` / `metric-card monthly-metric` style.
- Keep the hero title: `매주 리서치 후보 수와 신호를 업데이트하는 결산 화면` when Chris explicitly references that style.
- Include separate metric cards for:
  - Weekly papers
  - Total papers
  - Chris Archive
  - Design DNA
  - Visual Archive
  - Indexed total
  - optional existing weekly stats such as Lane balance and Avg relevance
- Compute counts from public manifests rather than hardcoding UI copy:
  - `research-board.json`
  - `chris-archive.json`
  - `dna-archive.json`
  - `midjourney-dna-archive.json`
  - `brand-mockup-assets.json`
  - `home-visual-set.json`

## Verification probe checklist

For desktop/tablet/mobile, verify with browser computed values:
- Body tab font size equals the requested pixel value (e.g. `17px`).
- Nav margin top/bottom equals requested values (e.g. `6px` / `18px`).
- Exactly one `.workspace-tab-indicator` is present.
- Indicator width and left match the active tab button within ~1px.
- Indicator transition includes `left`, `width`, and `opacity`.
- Horizontal overflow is zero.
- No console/page errors.

For Weekly metrics:
- Removed standalone count-card copy is absent when requested.
- Required metric labels are present.
- Metric count is sufficient for the requested data categories.
- Build with `npm run build:public`, then verify live GitHub Pages assets and browser behavior before reporting completion.
