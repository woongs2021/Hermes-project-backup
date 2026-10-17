# GoYJ Design DNA asset loop and webapp save gate

Use when Chris asks to operate or repair Go Youn-jung's recurring visual generation loop for Chris Archive / Design DNA assets.

## Current operating contract

- Owner/sender: Go Youn-jung profile and bot, not Karina/default.
- Schedule: Monday / Wednesday / Friday, KST 10:15 unless Chris changes it.
- Output per run: 5 square 1:1 graphic candidates.
- Generation model: always `gpt_image_2_5` through Higgsfield CLI. Do **not** substitute Seedream, Recraft, Kling, `image_auto`, or other image models. If `gpt_image_2_5` is unavailable, report the blocker rather than generating with another model.
- Source of inspiration: Chris Archive + `헤르메스디자인시스템.md` / Design DNA, but the output must be original and must not copy third-party logos, slogans, layouts, app icons, package labels, or readable fake UI text.
- Candidate status: temporary review only. Candidates live under `/opt/data/dna-archive/candidates/YYYY-MM-DD/` and should not be published to the webapp or final selected archive until Chris approves.
- Save gate: only when Chris explicitly says `저장해줘` for one or more candidates should the selected image(s) be copied into `/opt/data/dna-archive/selected/YYYY-MM-DD/`, reflected in `public/data/dna-archive.json`, and committed/pushed to the webapp.
- Webapp destination: saved GoYJ images belong in **Design DNA → DNA Dashboard**, not in Chris Archive and not as a loose section inside the main Design DNA narrative. Chris Archive remains for user-collected references/source material.

## Webapp implementation pattern

1. Keep top-level tabs separate:
   - `Chris Archive`: source/reference images only.
   - `Design DNA`: the design-system narrative.
2. Inside `Design DNA`, provide a small sub-tab switcher:
   - `Design DNA`: principles, archive evidence, prompt packages, guardrails.
   - `DNA Dashboard`: selected GoYJ-generated assets.
3. `DNA Dashboard` should mirror the Chris Archive dashboard interaction model:
   - square thumbnails
   - click-to-open detail modal
   - large image
   - GoYJ analysis
   - DNA clusters
   - generation prompt
   - source/save policy
4. Keep `public/data/dna-archive.json` as the public-safe manifest. It should contain only selected/published assets, not temporary review candidates.
5. Copy selected assets into `public/assets/dna-archive/YYYY-MM-DD/` and verify every manifest `imageSrc` returns HTTP 200 on GitHub Pages.

## Verification checklist

- Local build succeeds (`npm run build:public`).
- On the live Pages URL:
  - `#chrisArchive` shows only Chris Archive references and no DNA Dashboard/grid.
  - `#design-dna` shows a `Design DNA` / `DNA Dashboard` sub-tab switcher.
  - Opening `DNA Dashboard` shows all selected GoYJ assets, including the newly saved ones.
  - All DNA asset image URLs return HTTP 200.
  - Detail modal shows prompt and analysis.
  - Desktop/tablet/mobile have no horizontal overflow.

## Pitfalls

- Do not publish all generated candidates. Chris's `저장해줘` is the approval signal.
- Do not place GoYJ selected images inside Chris Archive; that confuses references with generated outputs.
- Do not add a loose DNA grid directly into the main Design DNA page body; use the Design DNA internal `DNA Dashboard` sub-tab.
- Do not switch image models silently. The durable preference is GPT Image 2.5 only for this loop.
- Do not commit unrelated manifest timestamp churn or unrelated research/home data diffs when only updating DNA assets.