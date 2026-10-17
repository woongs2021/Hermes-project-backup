# Slack cron/loop alert cleanup and delivery hygiene

Use when Chris asks to remove Hermes cron/loop stop/failure alerts from Slack while keeping Telegram delivery.

## Pattern

1. Treat loop stop/failure notifications as operational noise, not team-channel content. Chris wants these off Slack while Telegram delivery remains available.
2. Find all relevant cron `deliver` settings, not only the default profile. Specialist profile-local cron files can keep `slack,telegram:<id>` even after the default cron list is clean.
   - Default profile commonly uses `/opt/data/cron/jobs.json`.
   - Specialist profiles commonly use `/opt/data/profiles/<profile>/cron/jobs.json`.
3. Convert `slack,telegram:<target>` to `telegram:<target>` for user-facing specialist loops; convert Slack-only paused/legacy jobs to `local` when they should no longer speak to Slack.
4. Verify no remaining `deliver` value contains `slack` across default and specialist cron job stores.
5. If deleting already-posted Slack cron failure messages:
   - Do not print tokens or raw Slack credential values.
   - Slack `search.messages` may reject bot tokens with `not_allowed_token_type`; use `conversations.history` instead when needed.
   - Large Slack history responses can contain problematic JSON escapes or partial reads. A robust fallback is to fetch raw response text, scan locally for `Cronjob Response:` / `failed` / `To stop or manage this job`, extract message `ts`, then call `chat.delete`.
   - Messages posted by specialist bots often cannot be deleted by the default bot (`cant_delete_message`). Retry deletion with the owner profile's Slack bot token, still without printing credentials.
6. After cleanup, rescan recent Slack history for remaining cron failure/stop messages and report only counts/status, not raw internal messages.

## Safety

- Never expose Slack bot tokens, app tokens, channel IDs beyond non-secret target identifiers already visible in config, or raw private chat logs.
- Do not remove Telegram delivery when the user explicitly says Telegram should stay.
- Do not over-broaden: remove Slack from loop stop/failure delivery and scheduled loop outputs only when Chris asks; ordinary direct Slack team coordination can remain governed by the main Slack/team rules.
