# Chris Daily Higgsfield Graphic Loop

Use this reference for Chris's recurring Go Youn-jung visual loop and similar daily generative-graphic tasks.

## Trigger

Chris wants Go Youn-jung to generate recurring visual inspiration, not one-off prompt packs: daily 1:1 graphics with rationale, storage, and delivery. Exact prompts are saved locally for traceability, but omitted from the recurring DM and shared only when Chris separately asks for them.

## Current loop shape

- Owner: Go Youn-jung, under Karina orchestration.
- Delivery: Telegram DM from Go Youn-jung's own Telegram bot/profile. Do not rely on default/Karina cron auto-delivery for this visual loop; if cron auto-delivery makes the message appear from Karina/default, set cron `deliver` to local and have the Go Youn-jung-profile job send directly via its Telegram bot token without exposing credentials.
- Cadence: daily 09:10 KST unless Chris changes it. Chris wants the main work loops to arrive between 09:00 and 10:00 KST.
- Output: two generated Higgsfield images per day, short Korean rationale, model used, and why that model was chosen. Exact prompts are saved locally but not included in the daily delivery unless Chris asks separately.
- Storage root: `/opt/data/agent-team-work-log/visuals/daily-graphics/`.
- Event log: `/opt/data/agent-team-work-log/visuals/daily-graphics/events.jsonl`.
- Webapp image-gallery mirror for Faker: copy final images to `/opt/data/hermes-webapp-build-loop/assets/image-gallery/YYYY-MM-DD/` and write metadata to `/opt/data/hermes-webapp-build-loop/data/image-gallery/` so the future webapp can show a Pinterest-like visual tab with click-to-reveal rationale.

## Visual direction Chris approved

- Premium illustration / soft-3D editorial graphics.
- Rounded, tactile, friendly forms with bevels, fillets, soft shadows, and calm depth.
- Simple theme-matched solid backgrounds; avoid busy scenes unless the concept truly needs one.
- Use `woongdesignv2` theme colors as palette restraint, not as UI-slide decoration.
- Avoid sharp, spiky, blade-like, needle-like, jagged, hazardous, aggressive, or painful-looking object silhouettes.
- Avoid excessive wave, ripple, fluid, water, swirl, or flowing-sheet motifs; Chris felt the wave feeling was too strong. Prefer calmer solid object, still-life, product-editorial, tactile artifact, plant/tool/furniture/book/material metaphors unless he explicitly asks for fluid motion.
- Avoid generic AI aesthetics: neon, glassmorphism, glowing brains, fake UI panels, pseudo-text, robots, cyberpunk defaults, plastic hands/faces, and over-smooth AI-startup gradients.
- Prefer text-free images.

## Daily variation rule

Before choosing the day's prompts, inspect recent daily-graphics notes/events when available. Vary at least these dimensions:

- Object/metaphor family: do not keep repeating vessels, looms, or orbit gardens.
- Metaphor mode: one abstract/systemic and one concrete; concrete can be person, animal, object, tool, fabric, plant, machine, furniture, book, landscape, etc.
- Silhouette: rounded is preferred, but shape language should still vary.
- Material: clay, felt, paper, ceramic, soft rubber, translucent resin, fabric, wood, matte metal, etc.
- Composition: centered object, diagonal arrangement, floating cluster, landscape field, product-still-life, poster icon, etc.
- Color theme: choose two non-overlapping `woongdesignv2` theme families or nuanced palette mixes each day. Across any 7-day rolling window, avoid repeating the same daily color pairing and metaphor family when possible, so the week reads as seven different color/metaphor chapters while preserving the same premium soft-3D/editorial style.

## Model selection and disclosure

- First inspect available Higgsfield image models/options when practical.
- Prefer the highest-quality text-to-image model with 1:1 and 2k support. As of the successful test on 2026-07-20, `seedream_v5_pro` worked well for 2k soft-3D illustration.
- In the DM, include:
  - `사용 모델`: actual model confirmed by command output.
  - `왜 이 모델인가`: short reason, e.g. 2k support, strong text-to-image quality, stable soft-3D/editorial object rendering.
- Never claim a model was used unless a real command result confirms it.

## Storage and delivery contract

For each run, save:

- `prompts.md` under `/opt/data/agent-team-work-log/visuals/daily-graphics/YYYY-MM-DD/`.
- Generated image files under a generated subfolder for that date.
- Append one JSON object per image to `events.jsonl` with:
  - `date_kst`
  - `agent`
  - `theme`
  - `metaphor_mode`
  - `metaphor_subject`
  - `prompt`
  - `model`
  - `model_reason`
  - `job_id` when available
  - `output_path_or_url`
  - `remote_url` when available
  - `quality_notes`
  - `limitations`

For the future Faker webapp image tab, also mirror final delivered assets into `/opt/data/hermes-webapp-build-loop/`:

- Copy each final PNG to `assets/image-gallery/YYYY-MM-DD/`.
- Write/update `data/image-gallery/YYYY-MM-DD.json`.
- Append normalized card records to `data/image-gallery/items.jsonl`.
- Include fields: `id`, `date_kst`, `agent`, `title`, `theme`, `metaphor`, `why`, `model`, `webapp_asset_path`, `source_path`, `display_mode`, `interaction`, and `prompt_policy`.
- The future webapp should use these as Pinterest-like masonry cards; clicking a card reveals the `why` rationale. Exact prompts remain hidden by default.

For Telegram delivery, the final response must attach each generated local image explicitly and omit exact prompt text:

```text
MEDIA:/opt/data/agent-team-work-log/visuals/daily-graphics/YYYY-MM-DD/generated/01-....png
MEDIA:/opt/data/agent-team-work-log/visuals/daily-graphics/YYYY-MM-DD/generated/02-....png
```

Include title, theme, metaphor, `왜 이 이미지인가`, `사용 모델`, and `왜 이 모델인가`. Do not include exact prompts in the recurring DM; tell Chris they are saved and can be shared separately if he asks.

Plain local file paths in prose may document storage but do not reliably become native Telegram media. If only a remote URL exists, include Markdown image syntax like `![title](https://...)`.

## Governance handoff

Muyeol should review recurring loop changes weekly before they become unquestioned defaults. For this visual loop, Muyeol should check:

- metaphor diversity and repetition;
- soft-3D/illustration fit;
- sharp-object avoidance;
- solid-background fit;
- model-choice transparency;
- Higgsfield credit/session risk;
- privacy or accidental disclosure risk in logs.

Muyeol records recommendations; Karina applies them unless Chris has explicitly directed otherwise.

## Higgsfield auth pattern

If a profile-local Higgsfield job is not authenticated, start `higgsfield auth login` in that profile's `HOME`, ask Chris to open the OAuth URL, and if the browser fails on `localhost/callback?...`, have Chris paste the full callback URL. Call it from the agent host while the login process is waiting, then verify `workspace status` and model access. Do not print tokens or credential files.
