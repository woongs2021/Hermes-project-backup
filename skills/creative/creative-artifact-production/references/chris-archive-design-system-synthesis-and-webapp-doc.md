# Chris Archive design-system synthesis + webapp document pattern

Use when Chris asks to turn a matured Chris Archive batch into a design-system Markdown document and expose it in the GitHub Pages webapp.

## Trigger

- Chris says the archive has reached a target count (e.g. 60 unique references) and asks to start Design DNA analysis.
- Chris asks for a named Markdown file such as `헤르메스디자인시스템.md` and wants it viewable/downloadable from the webapp.

## Workflow

1. Verify the current archive count from the public manifest and/or archive entries.
2. Synthesize at cluster level, not image-by-image:
   - one-sentence definition
   - 8–10 repeated DNA clusters
   - color, typography, metaphor, layout, component, motion, brand-safety sections
   - Do / Don't
   - asset generation principles
   - initial tokens
3. Treat single references as evidence, not final rules. Write final language as repeated-pattern guidance.
4. Ask/route Go Youn-jung only when aesthetic judgment materially improves synthesis. For a first draft, Karina can draft and mark GoYJ review pending.
5. Save the canonical archive document under the requested Korean filename, e.g. `/opt/data/chris-archive/헤르메스디자인시스템.md`.
6. For GitHub Pages public access, copy the same Markdown to an ASCII-safe URL path such as `public/docs/hermes-design-system.md`, while keeping the browser download filename as the Korean name using `download="헤르메스디자인시스템.md"`.
7. In the Chris Archive tab, add:
   - a primary button: `헤르메스디자인시스템 보기`
   - a popup/modal that fetches and displays the Markdown text
   - an `MD 다운로드` link
8. Verify locally and live:
   - document URL returns HTTP 200 and contains expected section text
   - button opens the modal
   - download link href works and download attr is the Korean filename
   - desktop/tablet/mobile modal containment remains valid
   - existing archive grid counts and assets still pass

## Content stance

Core positioning used for the first Hermes system draft:

> 차가운 AI 기능을 따뜻한 인간 맥락 안에 안전하게 담는 OS-native visual language

Recurring clusters to consider:

- Soft Ambient Intelligence
- Protected Luminous Container
- Warm-Cool Equilibrium
- Orb / Orbit / Feedback Field
- Modular Soft System
- Human-Scale Interaction
- Quiet Editorial System
- Analog Archive Object
- Signal / Dot / Rhythm
- Human-System Editorial Contrast

## Pitfalls

- Do not dump all 60 entries into the system document. The deliverable is synthesis, not a raw archive mirror.
- Do not copy third-party brand names, campaign wording, logos, poster layouts, or exact icon silhouettes from the references.
- Do not serve the public doc only at a Korean/non-ASCII path on GitHub Pages; it may be harder to verify and can 404 depending on encoding/deployment. Use an ASCII-safe public path and a Korean download filename.
- Do not stop at local build success. Verify the actual Pages URL and the modal/download behavior with browser-computed checks.