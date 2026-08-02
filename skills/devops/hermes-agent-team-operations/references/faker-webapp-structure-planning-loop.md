# Faker Webapp Structure Planning Loop

Use this reference when Chris wants Faker to prepare a future webapp/dashboard/homepage but delay actual coding until a later phase.

## Current proven pattern

- Owner: Faker profile.
- Delivery: Telegram DM from Faker's own Telegram bot/profile. If the job lives in the default/Karina cron store, keep cron `deliver=local` and have Faker send the user-facing DM directly via `/opt/data/profiles/faker/.env` `TELEGRAM_BOT_TOKEN`; never expose tokens and never fall back to Karina/default delivery.
- Schedule: daily 09:45 KST, within Chris's preferred 09:00–10:00 KST work-loop window.
- July mode: planning-only until the end of July.
- August 1 checkpoint: Karina/Faker creates a phase-by-phase Markdown development plan, saves it under `/opt/data/hermes-webapp-build-loop/plans/`, and shares it to Slack for Chris confirmation. Chris wants the plan broken down for daily incremental coding; Faker recommends ~10 phases, each with 3–7 daily tasks.
- August coding mode: implementation may begin only after Chris/Karina confirms the August 1 phase plan, repo/workdir, public/private scope, data exposure rules, and implementation priority.
- Daily coding-task rule after approval: each task should fit roughly 30–90 minutes, touch 1–3 files/areas, have visible output, completion criteria, verification method, and next-day handoff. Prefer a small end-to-end slice early over perfect architecture.
- Data root: `/opt/data/hermes-webapp-build-loop/`.
- Go Youn-jung daily graphics should drive the future home screen first, not only a secondary gallery: finalized 3-image set → `HomeVisualHero` on `/` with 1 lead + 2 supporting cards. The same final assets also feed the Pinterest-like Image Gallery / Visual Archive tab under `/visuals`. Assets live under `/opt/data/hermes-webapp-build-loop/assets/image-gallery/`; metadata under `/opt/data/hermes-webapp-build-loop/data/image-gallery/`. Daily images are pending-review first: do not mirror them to Faker's final feed until Chris says a final-save phrase such as “오늘 최종본 저장해줘”/“이걸로 저장해줘,” or the end-of-day no-feedback finalizer saves the unchanged set.

## Phase rules

### July planning-only

Until `2026-07-31` KST, Faker should not:

- modify an app repository,
- create a deployable app,
- write production application code,
- run build/deploy commands,
- present speculative code as implemented work.

- Allowed July outputs:

- data model candidates,
- IA/route candidates,
- component-system candidates,
- implementation backlog candidates,
- source adapter ideas,
- privacy/public-vs-private boundaries,
- OBD/Hermes-growth reuse notes,
- Go Youn-jung visual-archive tab/data adapter notes,
- Harness / Loop / Graph Engineering project-framing notes,
- graph MVP candidates such as `nodes.jsonl`, `edges.jsonl`, graph `schema.md`, node/edge definitions, and relation breadcrumb UI ideas,
- coding risks and dependencies.

### August implementation-ready

From `2026-08-01` KST, Faker can shift toward implementation only when the repository/workdir and public/private scope are confirmed. If not confirmed, the DM should ask for that decision rather than starting code.

## Local data structure

Root: `/opt/data/hermes-webapp-build-loop/`

Recommended files:

- `SCHEMA.md` — loop rules and schema.
- `daily/YYYY-MM-DD.md` — daily webapp structure brief.
- `events.jsonl` — one compact JSON object per daily planning event.
- `candidates/data-model.md`
- `candidates/ia-and-routes.md`
- `candidates/component-system.md`
- `candidates/home-screen-layout.md` — homepage composition sourced from the latest Go Youn-jung visual loop (`HomeVisualHero`, 1 lead + 2 supporting cards).
- `candidates/image-gallery-tab.md` — Pinterest-like visual archive tab candidate sourced from Go Youn-jung daily graphics.
- `candidates/graph-engineering.md` — Harness / Loop / Graph Engineering project framing, graph node/edge MVP candidates, and relation breadcrumb UI notes.
- `candidates/implementation-backlog.md`
- `data/image-gallery/items.jsonl` — normalized image-card feed; each item includes title, theme, metaphor, image path, and `why` rationale bullets for click reveal.
- `assets/image-gallery/YYYY-MM-DD/*.png` — webapp-ready mirrored image assets.
- `august-readiness.md` — later synthesis before coding starts.

Each `events.jsonl` object should include:

- `date_kst`
- `phase`
- `structure_brief`
- `data_candidate`
- `implementation_candidate`
- `obd_reuse_note`
- `risk_or_dependency`
- `chris_question`

## Home screen from Go Youn-jung visual loop

Chris's current direction: use Go Youn-jung's newly established daily visual loop as the basis for the future webapp home screen. Faker should treat the latest 3-image set as a curated editorial hero, not just archive content.

- Route candidate: `/`.
- Component: `HomeVisualHero`.
- Layout: 1 lead visual card + 2 supporting visual cards.
- Data source: canonical current set `/opt/data/hermes-webapp-build-loop/data/image-gallery/final/current-home-visual-set.json`; archive/feed support `/opt/data/hermes-webapp-build-loop/data/image-gallery/items.jsonl`.
- Card behavior: static 1080 still on home; click opens shared `WhyThisImageDrawer` with rationale/model/date/source and optional turntable video.
- Prompt policy: exact prompts hidden by default, private/admin only after Chris asks or approves.
- `/visuals` remains the full Pinterest-like archive.

## Image Gallery / Visual Archive tab

Go Youn-jung's daily Higgsfield graphics should be a first-class future webapp axis, not just a folder of images. Faker should plan a Pinterest-like visual archive tab:

- Data source: `/opt/data/hermes-webapp-build-loop/data/image-gallery/items.jsonl`.
- Asset root: `/opt/data/hermes-webapp-build-loop/assets/image-gallery/YYYY-MM-DD/`.
- Route candidate: `/visuals`.
- Layout: responsive masonry/Pinterest-style image cards.
- Card default: image, title, date, theme, metaphor, source agent.
- Click behavior: open drawer/modal with larger image and `왜 이 이미지인가` rationale bullets, plus model/date/source metadata.
- Prompt policy: exact prompts hidden by default; expose only in private/admin mode after Chris approves or explicitly asks.

## Daily DM format

Faker should use respectful concise Korean and start with `Chris님,` or, for direct profile-owned Telegram delivery, `Faker입니다.`.

Sections:

- `🧱 오늘의 웹앱 구조 브리프`
- `🗂️ 오늘 쌓아둘 데이터/구현 후보`
- `🧩 OBD/Hermes 성장기 반영 포인트`
- `✅ Chris님께 드리는 10분 체크`

When Chris requests the project framing, explicitly separate:

- **Harness** — the safe execution/permission/routing/tooling base for the agent team.
- **Loop** — recurring research, growth, visual, planning, and validation rhythms.
- **Graph Engineering** — converting loop outputs into node/edge relationships such as `ResearchItem → Insight → GrowthQuestion → Decision → Artifact`.

During July, explicitly mention: `7월은 구현하지 않고 후보만 쌓겠습니다.`

## Integration with Son SNS loop

If Son’s Hermes-growth SNS loop exists, use its latest output as upstream context. The webapp planning loop should convert Son’s public narrative/subscriber-acquisition signals into future data structures such as:

- `DecisionMoment`
- `GrowthSignal`
- `SubscriberHypothesis`
- `OBDInsight`
- `AgentWorkflowEvent`

Keep public storytelling separate from private operational detail. Public pages may show polished narrative proof; private dashboard can keep richer logs, metrics, risks, and source references.

## Cron setup notes

- Use the Faker profile for the job.
- Prefer explicit Telegram delivery when profile-local home resolution is uncertain.
- The prompt must be self-contained because cron jobs run without current chat context.
- If Chris asks to run it today too, call `cronjob(action='run')`, then verify with `last_run_at`/`last_status` or created loop artifacts before claiming delivery.
- Use `context_from` with the Son daily SNS loop when available.

## First useful seed candidate

A strong first candidate is `DecisionMoment`: one moment where Hermes reduced Chris’s decision burden. It can later power a `/growth` public Before/After card and a private `/dashboard` operational card.

Suggested fields:

- `date_kst`
- `source_lane`
- `before_state`
- `agent_intervention`
- `after_state`
- `share_angle`
- `privacy_level`
- `metrics_later`

## Pitfalls

- Do not let “coding loop” imply immediate coding when Chris requested a delayed implementation phase.
- Do not store secrets, raw tokens, private IDs, or raw copied chat logs.
- Do not blend public homepage content with private dashboard data; define the boundary early.
- Do not report a scheduler-triggered job as delivered until run status or local artifacts confirm it.