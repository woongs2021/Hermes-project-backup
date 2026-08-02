# Chris weekly paper-report abstract visual

Use this reference when Go Youn-jung turns Muyeol's weekly best-3 paper report into the single visual follow-up artifact.

## Trigger

Runs after the Friday paper loop:

1. Daily Yuna + Go Youn-jung discovery remains 3+3.
2. Karina compiles the weekly candidate pool.
3. Muyeol selects and validates the final best 3.
4. Karina delivers the weekly report.
5. Go Youn-jung creates one abstract visual artifact from Muyeol's final report.

## Current Chris preference

Chris explicitly changed the weekly visual follow-up:

- Remove SNS / Instagram carousel prompt packages.
- Do **not** produce Midjourney prompts for carousel slides.
- Do **not** create a 4-slide information carousel, carousel IA, or SNS prompt/caption set.
- Instead, publish **one standalone abstract metaphor image** and leave the exact prompt used to generate it.

## Required outputs

Create exactly this package:

1. **One generated 1:1 abstract metaphor image** based on the week's final best-3 theme.
2. **The exact generation prompt used** for that image.
3. **A `왜 이 그림인가` rationale**: 2-4 concise Korean bullets explaining what weekly theme / selected papers / Muyeol caution the image represents, why the metaphor was chosen, and how Chris should read it.
4. **A `이번 주 스타일 선택` line** explaining how this week's visual style differs from the previous/typical output.
5. If generation fails: report the exact blocker and provide the ready-to-run prompt. Never fabricate a generated image.

## Source of truth

- Primary: Muyeol's finalized weekly best-3 report injected from Karina's delivery job.
- Supporting: `/opt/data/agent-team-work-log/paper-candidates/weekly-selected-papers.md`.
- Production notes/output folder: `/opt/data/agent-team-work-log/visuals/YYYY-WW/`.

## Abstract image direction

Chris's quality bar is **AI티가 안 나는 것**.

- Keep the image abstract and artistic.
- Do not show the metaphor too literally; avoid obvious objects unless heavily abstracted.
- Let the theme emerge through composition, material, rhythm, texture, light, negative space, and spatial tension.
- Use minimal/no text. Avoid Korean text in the raster image unless the brief truly requires it.
- Use `/opt/data/profiles/faker/design-systems/woongdesignv2.md` only as a quiet restraint/material/editorial reference: warm off-white `#FCFCFF`, ink `#010102`, restrained color planes, hairline/card/surface logic, strong whitespace, tactile paper grain, and human editorial/material composition. Do not force UI slides.
- Reference broad movements/material sensibilities, not living artists' exact styles:
  - Bauhaus grid discipline,
  - Korean monochrome / Dansaekhwa material restraint,
  - editorial photogram,
  - abstract cartography,
  - constructivist composition,
  - ink-wash atmosphere,
  - material minimalism,
  - quiet archival design.
- Negative guidance: no neon AI-startup look, no glassmorphism, no fake 3D UI, no pseudo text, no stock AI icons, no uncanny symbols, no oversaturated gradients, no synthetic glow, no glossy prompt-art finish.

## Style variation rule

Do not make the weekly abstract image look the same every week. Before writing the new prompt, check the latest previous visual production notes under `/opt/data/agent-team-work-log/visuals/` when available and identify the prior metaphor/style in one local note. Then deliberately vary at least a few of these: dominant metaphor, composition logic, material texture, color temperature, art/reference movement, density, lighting, and spatial depth.

Useful rotating palette examples:

- Bauhaus grid discipline + paper grain,
- Korean monochrome / Dansaekhwa material restraint,
- editorial photogram,
- abstract cartography,
- constructivist composition,
- ink-wash atmosphere,
- archival index-card / field-note aesthetic,
- quiet ceramic or glaze texture,
- architectural section drawing,
- botanical / organic diagram,
- astronomical plate,
- textile / loom structure,
- muted risograph print,
- low-relief paper sculpture.

If repeating a previous style is genuinely necessary, state the reason in the production note.

## Higgsfield CLI pattern

```bash
export PATH="/opt/data/.npm-global/bin:$PATH"
higgsfield version
higgsfield workspace status
higgsfield generate create gpt_image_2 \
  --aspect_ratio 1:1 \
  --quality high \
  --resolution 2k \
  --prompt "<prompt>" \
  --wait --json
```

For specialist-owned cron jobs, check the target profile's Higgsfield state, not only the default shell:

```bash
HOME=/opt/data/profiles/goyounjung/home \
PATH="/opt/data/.npm-global/bin:$PATH" \
higgsfield workspace status
```

If the specialist profile says no workspace/auth while the default profile works, and Chris intends shared Higgsfield usage, copy only the Higgsfield config/credentials files into that profile's home with restrictive permissions (`0600`) and do not print tokens or raw credential JSON.

Robustness rule: vision/image-review tools accept raster image formats only (PNG/JPEG/GIF/WEBP). Never pass SVG, JSON, text, empty files, or URL text files into a vision/image input; deliver a fallback file with caveat or skip vision review for that artifact.

## Production note

Write `/opt/data/agent-team-work-log/visuals/YYYY-WW/README.md` with:

- source report date/week,
- final 3 items,
- woongdesignv2 principles used,
- previous visual style checked,
- new style variation decision,
- metaphor choice and abstraction strategy,
- why this image was made / how it connects to the weekly report,
- exact Higgsfield prompt,
- output path/URL,
- quality notes and anti-AI-artifact review,
- limitations/blockers.

## Delivery

Final response should include:

- short Korean note,
- `MEDIA:/absolute/path` for the generated image or URL if returned by Higgsfield,
- `왜 이 그림인가` section with 2-4 concise bullets,
- `이번 주 스타일 선택` line,
- the exact image prompt used, clearly labeled,
- blocker + ready-to-run prompt if generation failed.
