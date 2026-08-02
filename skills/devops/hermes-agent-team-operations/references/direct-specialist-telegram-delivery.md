# Direct specialist Telegram delivery

Use this when Chris wants scheduled/user-facing specialist messages to appear from the specialist's own Telegram DM (Son, Faker, Go Youn-jung, etc.) rather than Karina/default.

## Why this pattern exists

A cron job stored in the default/Karina cron store can run with `profile: son` or `profile: faker` while cron auto-delivery still uses the default/Karina delivery path. The result can look like Karina sent the specialist's message. For Chris's specialist DM loops, this is the wrong UX.

## Required pattern

Preferred durable setup:

1. Put the scheduled job in the specialist profile's own cron context when possible, and set an explicit delivery target such as `telegram:<Chris chat id>` rather than bare `telegram` if the profile does not have a reliable Telegram home/origin.
2. Trigger or wait for one run and verify a real Telegram delivery result/message ID before telling Chris the specialist DM loop is fixed. A successful `cronjob(action='run')` only queues the job for a scheduler tick; it is not proof that the DM was delivered.

Fallback/direct-send setup when default/Karina cron ownership or duplicate auto-delivery would make the message appear from Karina:

1. Keep the user-facing specialist job owned by the correct profile in the prompt and metadata.
2. Set cron `deliver` to `local` so cron does not auto-send the final response via Karina/default.
3. In the prompt, require the specialist to send the user-facing DM directly through that profile's Telegram bot token:
   - Son: `/opt/data/profiles/son/.env`
   - Faker: `/opt/data/profiles/faker/.env`
   - Go Youn-jung: `/opt/data/profiles/goyounjung/.env`
4. Use Chris's approved Telegram chat ID only when already part of the user's configured profile setup.
5. Never print or log bot tokens, `.env` contents, raw credentials, or private platform IDs beyond the approved chat ID.
6. If direct send fails, write a local blocker status and do **not** fall back to Karina/default delivery.

## Toolset requirement

If the job will send directly via Telegram Bot API from the prompt, the cron job must include a toolset capable of local HTTP execution, normally `terminal` along with any required `file` / `session_search` toolsets. Without `terminal` or an equivalent HTTP-capable tool, the specialist run may prepare local files but be unable to send the DM.

Recommended `enabled_toolsets` examples:

- Son daily/weekly DM: `["file", "session_search", "terminal"]`
- Faker daily webapp DM: `["file", "session_search", "terminal"]`
- Go Youn-jung generated-image DM: `["terminal", "file", "vision", "web", "session_search"]`

## Prompt block template

```text
<Specialist> Telegram direct-delivery requirement:
- Do NOT rely on cron auto-delivery for the user-facing DM, because default/Karina cron delivery can make the message appear from Karina/default even when the run profile is `<profile>`.
- This cron job's `deliver` target must remain `local` only.
- After preparing the concise user-facing DM and saving required local files, send the DM directly from the `<profile>` Telegram bot using the Telegram Bot API with `TELEGRAM_BOT_TOKEN` from `/opt/data/profiles/<profile>/.env` and Chris's authorized chat ID.
- Start the user-facing DM with `<Specialist>입니다.` so Chris can clearly tell which specialist sent it.
- Use a local Python helper or curl. Never print or log the bot token, raw credentials, private IDs beyond the approved Chris chat ID, or full .env contents.
- If direct Telegram sending fails, write a short local blocker status without exposing credentials; do not fall back to Karina/default delivery.
- The final cron output should be a short local status only, not the full user-facing DM.
```

## Verification

- Check whether the relevant job is using the preferred specialist-profile explicit delivery (`deliver=telegram:<Chris chat id>`) or the fallback direct-send pattern (`deliver=local` plus Telegram Bot API from the specialist token). Do not mix the two unless you understand the delivery path.
- Check the job prompt contains the direct-delivery block when using the fallback pattern.
- Check `enabled_toolsets` includes `terminal` or an equivalent direct-send capability when using Bot API fallback.
- After `cronjob(action='run')`, re-check `last_run_at`, `last_status`, output files, and delivery errors; the `run` call itself only schedules the next tick and can appear successful even when no DM has arrived yet.
- If profile-local `send_message(target='telegram')` fails because no home channel is set, either configure/set the profile's home target or use explicit `telegram:<Chris chat id>` / Bot API direct send.
- If a spawned specialist Hermes process reports `cron_auto_delivery_duplicate_target` or similar duplicate auto-delivery skip, do not assume the DM was sent. Use the profile's own Telegram Bot API token for a one-shot resend, or reconfigure the scheduled job's delivery path, then verify real Telegram message IDs.
- For a user-requested smoke test, trigger the job or send a short direct message from the specialist token and report only success/message IDs, never tokens.
