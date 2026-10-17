# Codex usage based Faker coding scope

Use this when Chris wants to keep research/visual/growth loops stable while varying only Faker's coding workload based on monthly/current OpenAI Codex usage.

## Intent

Chris wants the rest of the agent team loops to remain unchanged. Only Faker's daily coding scope should expand or shrink so Codex/GPT usage does not sit unused or get exhausted too early.

## Usage source

Hermes can fetch Codex usage through the existing OpenAI Codex OAuth runtime, using `agent.account_usage._fetch_codex_account_usage()` rather than scraping the ChatGPT analytics web page. The web analytics URL is login/session-bound and may return 403 from the agent host.

Session-proven script location:

- `/opt/data/scripts/codex_usage_policy.py`

Output files:

- Current policy: `/opt/data/faker-coding-budget/codex-usage-policy.json`
- History: `/opt/data/faker-coding-budget/codex-usage-history.jsonl`

Recommended local scheduler:

- KST 09:35, before Faker's daily coding cron.
- Script-only/no-agent local cron is enough; do not DM Chris unless there is a real blocker.

## Policy bands

Use remaining percentage from the primary Codex usage window:

- `expanded` — remaining >= 80%: one coherent visible improvement, about 60–120 minutes, 2–4 related files/areas allowed, no broad rewrites.
- `normal` — remaining >= 55%: default Faker scope, about 30–90 minutes, 1–3 files/areas.
- `light` — remaining >= 30%: smaller task, about 15–45 minutes, 1–2 files, small UI/data/refactor improvement.
- `minimal` — remaining < 30%: avoid larger implementation; build verification, docs/data cleanup, or one tiny safe fix only.

## Faker cron prompt rule

Patch Faker coding cron prompts to:

1. Read `/opt/data/faker-coding-budget/codex-usage-policy.json` before choosing the daily coding task.
2. If the policy is missing or older than 24 hours, run `/opt/hermes/.venv/bin/python /opt/data/scripts/codex_usage_policy.py` once and reread it.
3. Follow `coding_mode` for task size only.
4. Keep all non-Faker loops unchanged: Karina, Yuna, Go Youn-jung, Son, Muyeol, visual, paper, and growth loops should not expand because Codex has spare usage.
5. In Faker's daily DM, include a short line like `📊 Codex 사용량 기준 — <coding_mode>; <remaining_percent>% remaining` when available.

## Pitfalls

- Do not scrape or rely on the visible ChatGPT analytics page when the backend usage API is available through Hermes OAuth.
- Do not confuse `cronjob(action='run')`/cron `ok` with user delivery. For Faker direct-DM jobs, verify the delivery path separately when relevant.
- Do not make additional coding jobs or expand non-Faker loops just because Codex has headroom.
- If usage fetch fails, default to `normal` rather than stopping the daily coding loop.
