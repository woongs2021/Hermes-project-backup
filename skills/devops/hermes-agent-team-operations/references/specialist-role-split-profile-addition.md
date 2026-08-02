# Specialist role split + new profile addition pattern

Use when Chris wants to add a new specialist agent that takes over part of an existing specialist's lane.

## Durable pattern

1. Clarify the role split as explicit routing lanes, not just a new persona.
   - Example: keep one agent on AI technology / LLM / agent-framework / paper / startup / future-scenario research.
   - Move UX research / interview analysis / competitive service / design benchmark / IA journey / Persona-JTBD / design insight to the new agent.
2. Create the profile with a stable lowercase ID and role-based description:
   - `hermes profile create <profile_id> --description "..."`
3. Write the new profile `SOUL.md` with:
   - primary mission
   - core responsibilities
   - collaboration rules with Karina and adjacent agents
   - Slack/team-channel behavior
   - daily work-log protocol
   - explicit tone rule if relevant, e.g. specialists use 존댓말; Karina alone may use banmal with Chris.
4. Update the original specialist's `SOUL.md` to narrow its lane and reference the new specialist as the handoff partner.
5. Update Karina/default `SOUL.md` roster and routing rules so the orchestrator sends future tasks to the right owner.
6. Create/update work-log support:
   - add the new agent to `/opt/data/agent-team-work-log/SCHEMA.md`
   - create `/opt/data/agent-team-work-log/<profile_id>/daily/`
7. Prepare independent messaging credentials without exposing secrets:
   - create `/opt/data/profiles/<profile_id>/.env`
   - include empty token slots only, never copied real tokens
   - include distinct-token reminder
   - set mode `0600`
   - for shared Slack channels, default specialists to `SLACK_REQUIRE_MENTION=true`
8. Smoke test the profile with a harmless one-shot command:
   - `hermes -p <profile_id> chat -q "한 문장으로 본인 역할을 한국어 존댓말로 소개해 주세요." -Q`
9. Verify with `hermes profile list`; gateway may remain stopped until real Telegram/Slack credentials are added.

## Independent bot env template

Use this shape and leave secrets blank:

```env
# <Display Name> independent bot credentials
# Fill in one distinct bot/app token per platform. Do not reuse another profile's token.
# Keep this file private; never paste real tokens into chat/logs.

# Telegram 1:1 bot
TELEGRAM_BOT_TOKEN=
TELEGRAM_ALLOWED_USERS=

# Slack Socket Mode bot
SLACK_BOT_TOKEN=
SLACK_APP_TOKEN=
SLACK_ALLOWED_USERS=
SLACK_HOME_CHANNEL=
SLACK_REQUIRE_MENTION=true
```

## Pitfalls

- Do not only create the new profile; update the old specialist and Karina routing too, or the team will keep sending work to the old owner.
- Do not clone another profile's real `.env`; create a clean template with blank token values.
- Do not start the gateway before credentials are supplied unless the user explicitly wants a local-only check.
- Do not log or echo token values when verifying env files; print key names and value lengths only if needed.
