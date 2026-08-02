# Slack + Telegram multi-profile team orchestration pattern

Session-proven pattern for a Karina-led Hermes specialist team.

## Shape

- One main/default profile acts as the single front door and final synthesizer.
- Each specialist has its own Hermes profile, SOUL.md, Telegram bot token, Slack bot token, and Slack app token.
- Telegram is used for separate 1:1 specialist DMs.
- Slack is used as the shared team room where all bots coexist.
- `SLACK_REQUIRE_MENTION=true` is important in shared channels so only the mentioned agent responds.

## SOUL.md defaults

Put durable operating behavior in SOUL.md, not memory:

- Main profile: owns orchestration, task splitting, specialist routing, final synthesis, and calm user-facing decisions.
- Specialists: treat the main profile as coordination lead; answer within lane; produce handoff notes for final synthesis; do not take over other specialists' roles.
- Shared Slack rule: if the user directly mentions a specialist, the specialist may answer directly but should frame output so the main orchestrator can synthesize.

After SOUL.md edits, restart the affected gateway profiles. Existing gateway sessions may otherwise continue with cached defaults.

## Daily work logs

For agent self-continuity, use date-bound Markdown files rather than memory:

- Root example: `/opt/data/agent-team-work-log/`
- Per-agent folders: `<agent>/daily/YYYY-MM-DD.md`, `<agent>/index.md`, optional `<agent>/topics/`
- Create a daily file only when the agent performed substantive work.
- Do not create files for no-work days, greetings, `/start`, platform checks, or routine connection tests.
- Never write raw chat logs, bot tokens, OAuth/API keys, private IDs, or credential-like strings.
- End-of-day local-only cron jobs can inspect each profile's sessions with `session_search`; prompt must explicitly skip file creation when no substantive work occurred.

## Gateway verification

- Verify per profile with `hermes --profile <name> gateway status` and each profile's latest gateway log startup block.
- For Slack, confirm `Socket Mode connected`, `✓ slack connected`, and `Gateway running with 2 platform(s)` when Telegram is also enabled.
- Restart only the affected profile when a single profile's Socket Mode reconnect loop appears.

## Watch-pattern pitfall

Do not start long-lived gateways with broad watch patterns like `error`/`ERROR`; normal agent tool failures inside the gateway can trigger false alerts. Use connection success patterns and specific hard-failure strings instead.
