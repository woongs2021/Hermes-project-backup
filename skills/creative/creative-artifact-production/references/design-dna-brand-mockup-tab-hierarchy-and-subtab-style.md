# Design DNA Brand Mockup tab hierarchy and underline subtabs

Use when Chris asks to reorganize **Design DNA → DNA Brand Asset** mockup tabs, especially when multiple raw mockup collections accumulate.

## Preferred hierarchy

Keep raw/reference mockup collections grouped under one upper-level lane:

- `Brand Mockup Assets`
  - `Coffee Mockup Assets`
  - `Outdoor Mockup Assets 1`
  - `Outdoor Mockup Assets 2`
  - future raw mockup collections
- `Midjourney + Mockup`
  - synthesized / generated application examples from motifs + mockups

Do not leave Coffee/Outdoor collections as peers of `Midjourney + Mockup` once there are several raw mockup collections; group them under `Brand Mockup Assets` so the top-level split remains clear: raw mockup references vs synthesized outputs.

## React pattern

- Track an upper lane, e.g. `activeBrandAssetLane: 'brandMockup' | 'midjourneyMockup'`.
- Keep `activeBrandAssetSource` for the selected raw collection id from `brandMockupAssets.collections`.
- Render upper tabs with the existing card/chip style (`dna-dashboard-source-tabs` + `dna-dashboard-source-tab`).
- When `activeBrandAssetLane === 'brandMockup'`, render a second-level tab row from `collections[]`.
- Keep `Midjourney + Mockup` rendering from `examples[]` unchanged and at the same upper level as `Brand Mockup Assets`.

## Second-level visual style Chris requested

The raw collection tabs under `Brand Mockup Assets` should match the existing `Chris Archive` / `Design DNA` workspace-tab behavior, not just generic underline chips:

- transparent background
- no card border
- no border radius
- centered tab row (`justify-content: center`)
- generous spacing between tabs, similar to workspace tabs (`column-gap: clamp(32px, 4.6vw, 76px)` or equivalent)
- active tab color should use the same primary blue as workspace tabs (`var(--primary)`, currently `#4065f8`)
- use one movable underline indicator element whose `left` and `width` animate between tabs, rather than each tab drawing its own static underline
- remove the extra gray bottom rule under the underline (`border-bottom: 0` on the subtab group)
- horizontal overflow is allowed on mobile, but hide the scrollbar and account for `scrollLeft` when calculating indicator position
- keep text labels concise and counts as small metadata

Suggested class split:

```tsx
const brandMockupSubtabNavRef = useRef<HTMLDivElement | null>(null)

useEffect(() => {
  const nav = brandMockupSubtabNavRef.current
  if (!nav || activeBrandAssetLane !== 'brandMockup') return

  const updateBrandMockupIndicator = () => {
    const activeButton = nav.querySelector<HTMLButtonElement>('.brand-mockup-subtab.active')
    if (!activeButton) {
      nav.style.setProperty('--brand-mockup-subtab-indicator-opacity', '0')
      return
    }

    const navBox = nav.getBoundingClientRect()
    const buttonBox = activeButton.getBoundingClientRect()
    nav.style.setProperty('--brand-mockup-subtab-indicator-left', `${buttonBox.left - navBox.left + nav.scrollLeft}px`)
    nav.style.setProperty('--brand-mockup-subtab-indicator-width', `${buttonBox.width}px`)
    nav.style.setProperty('--brand-mockup-subtab-indicator-opacity', '1')
  }

  updateBrandMockupIndicator()
  const animationFrame = window.requestAnimationFrame(updateBrandMockupIndicator)
  window.addEventListener('resize', updateBrandMockupIndicator)
  nav.addEventListener('scroll', updateBrandMockupIndicator, { passive: true })

  return () => {
    window.cancelAnimationFrame(animationFrame)
    window.removeEventListener('resize', updateBrandMockupIndicator)
    nav.removeEventListener('scroll', updateBrandMockupIndicator)
  }
}, [activeDesignDnaSection, activeBrandAssetLane, activeBrandAssetSource, brandMockupCollections.length])

<div
  className="dna-dashboard-source-tabs brand-mockup-subtabs"
  aria-label="Brand Mockup Assets collections"
  ref={brandMockupSubtabNavRef}
>
  {brandMockupCollections.map((collection) => (
    <button
      type="button"
      className={activeBrandAssetSource === collection.id
        ? 'dna-dashboard-source-tab brand-mockup-subtab active'
        : 'dna-dashboard-source-tab brand-mockup-subtab'}
      aria-pressed={activeBrandAssetSource === collection.id}
      onClick={() => setActiveBrandAssetSource(collection.id)}
      key={collection.id}
    >
      <span>{collection.title}</span>
      <small>{collection.items.length} assets</small>
    </button>
  ))}
  <span className="brand-mockup-subtab-indicator" aria-hidden="true" />
</div>
```

CSS checks to verify:

- `.brand-mockup-subtabs` computed `display` is `flex`.
- `.brand-mockup-subtabs` computed `justify-content` is `center`.
- The visual union of the subtab buttons is centered in the group (`centerDelta` near 0 in DOM probes).
- The subtab group has no gray helper rule (`border-bottom-width: 0px`).
- `.brand-mockup-subtab` computed border widths are `0px`, radius is `0px`, background is transparent, and text-align is center.
- Active tab color equals workspace primary (`var(--primary)`, currently `#4065f8`).
- `.brand-mockup-subtab-indicator` is visible with opacity 1, primary color, and transition properties for `left`, `width`, and `opacity`.
- After clicking another subtab, the indicator's rendered left/width matches the active tab; include `nav.scrollLeft` in the calculation for mobile/horizontal-scroll layouts.
- `document.documentElement.scrollWidth - window.innerWidth` is `0`.

## QA

After build and deploy, verify desktop/tablet/mobile:

1. Top-level DNA Brand Asset tabs show `Brand Mockup Assets` and `Midjourney + Mockup`.
2. Inside `Brand Mockup Assets`, the raw collections appear as underline-style subtabs.
3. Coffee, Outdoor 1, Outdoor 2 each open their expected collection and image count.
4. `Midjourney + Mockup` remains a top-level peer and still renders the existing `examples[]` stack.
5. No horizontal overflow and no console errors.
