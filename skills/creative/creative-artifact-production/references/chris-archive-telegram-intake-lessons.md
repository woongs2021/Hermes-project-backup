# Chris Archive Telegram intake lessons

Use this reference when Chris is repeatedly sending images to archive via Telegram with the phrase `추가해줘`.

## Session learning

Chris expects archive intake to feel calm and continuous, not like a stream of half-finished progress fragments. During one session, repeated interim messages such as “분석했어, 저장할게” made the experience feel like the assistant was “말을 하다 말어.”

## Preferred interaction pattern

- If the image includes `추가해줘`, proceed without asking for confirmation.
- Do the full storage/update/verification sequence quietly.
- Send one concise completion message after verification.
- Include only:
  - 저장 완료
  - asset path
  - entry path
  - index and `DESIGN_SYSTEM_DRAFT.md` updated
  - strongest 3–6 design-DNA signals
  - one relevant caution if needed
- Avoid repeated step-by-step progress commentary unless there is a real blocker or a long delay.

## Efficient execution pattern

For straightforward repeated intakes, prefer one consolidated `execute_code` call that:

1. Gets KST date.
2. Computes the source image hash before naming.
3. Checks whether the same hash already exists under `/opt/data/chris-archive/images/`.
   - If it is an exact duplicate and Chris still said `추가해줘`, do **not** create another duplicate asset file by default.
   - Reuse the existing asset path, create only a new entry if the image is a crop/detail/supporting reference, and mark `related_entries` / duplicate evidence clearly.
   - If the new upload is visually different but hash-collides in a short hash display, extend the hash length rather than overwriting.
4. Copies the source image to `/opt/data/chris-archive/images/YYYY/MM/` with `YYYY-MM-DD_<visual-slug>_<sha12>.jpg` only when it is not an exact duplicate.
5. Writes `/opt/data/chris-archive/entries/YYYY/YYYY-MM-DD_<visual-slug>.md`.
6. Appends to `index.md` idempotently.
7. Adds tentative class-level candidates to `DESIGN_SYSTEM_DRAFT.md` without promoting final rules.
8. Verifies both asset and entry exist and have nonzero size.

This reduces Telegram noise, avoids duplicated image binaries during rapid intake, and prevents the user from seeing fragmented work-in-progress messages.

## Analysis emphasis from the initial archive run

The initial archive run surfaced recurring candidate clusters:

- Ambient AI cards
- Luminous presence
- Directional manifesto graphics
- Soft modular intelligence
- Relational mesh fields
- Warm emotional mesh
- Bold manifesto typography + material overlay
- Looped warm intelligence core / soft looped core
- Orbital agent constellation
- Interface as cushion / pressure-absorbing AI layer
- Quiet symbolic core / context-to-signal axis
- Prismatic contact field / calm luminous boundary
- Light-theme gentle AI aura
- Human-scale circular navigation / biomorphic circular content system
- Calm AI processing UI / dot-matrix task generation
- Story-based product OS / rounded bento narrative
- Protected emotional orbit / privacy-safe emotional intelligence
- Living design-system board / token card collage
- Human perception identity poster / brand as lens
- Purple system pattern / phase-shift rhythm grid
- Mobility ambient media UI / motion-principle-to-product
- Calm AI state component / glass capsule progress

Treat these as candidate clusters only. Go Youn-jung review or repeated evidence is needed before final `DESIGN_SYSTEM.md` rules. When many similar images arrive in one session, explicitly classify each new image as either a new cluster, a stronger exemplar of an existing cluster, or supporting/detail evidence so the archive does not become a flat pile of unrelated entries.

## Recent batch additions to handle carefully

- **Design-system/token-board references:** these are useful not only as visual inspiration but as a way to present extracted tokens later. Capture card anatomy, bento/masonry organization, token specimen style, and the relationship between `DESIGN_SYSTEM.md` text and a companion visual board.
- **Human/lens/identity posters:** if third-party logos, faces, eyewear, product names, or wordmarks are visible, mark brand-safety explicitly. Extract perception/lens metaphor, monochrome identity field, human silhouette, gaze direction, and logo-placement tension only; never reuse literal marks or identities.
- **Pattern/rhythm grids:** treat repeating semi-circles, waves, dots, or glyphs as possible processing cadence / loop pulse / package-surface systems. Capture scale, density, phase shift, spacing, and motion direction candidates.
- **Mobility/media references:** when vehicle cockpit or in-car UI is visible, add safety and glanceability review items: driving distraction, motion speed, brightness, information density, and third-party UI/product isolation.
- **Component-level references:** when an image is a simple component such as a progress bar, analyze honest state semantics and accessibility, not only aesthetics. Do not imply precise progress unless the product can support it.
