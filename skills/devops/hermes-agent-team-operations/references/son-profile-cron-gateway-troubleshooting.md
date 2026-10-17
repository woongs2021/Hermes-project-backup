# Son profile cron/gateway troubleshooting

Use when Chris reports that Son did not answer, sent a fallback-looking reply, or a Son recurring loop produced an error.

## Quick triage

1. Check Son profile status and gateway, not Karina/default:
   - `hermes --profile son status --all`
   - `hermes --profile son gateway status`
2. Check Son profile cron jobs:
   - `hermes --profile son cron list`
   - Inspect recent outputs under `/opt/data/profiles/son/cron/output/<job_id>/`.
3. Inspect recent sanitized logs only; never print tokens:
   - `/opt/data/profiles/son/logs/agent.log`
   - `/opt/data/profiles/son/logs/gateway.log`

## Known durable failure modes

### Missing Son-local skill

If Son's final SNS cron says a skill such as `ai-ax-sns-market-summary-format` was “not found and skipped,” the skill exists in default but not Son's profile-local skill store. Copy the skill directory into Son's profile, preserving references:

```bash
mkdir -p /opt/data/profiles/son/skills/social-media
cp -a /opt/data/skills/social-media/ai-ax-sns-market-summary-format \
  /opt/data/profiles/son/skills/social-media/
```

Then re-run or wait for the next Son cron; verify the prompt no longer reports the skill as skipped.

### Slack `Session is closed` loop

If Son's Slack adapter repeats `Session is closed` / `Failed to connect`, restart only Son's gateway:

```bash
pgrep -af '[h]ermes --profile son gateway run'
# stop the Son gateway process carefully, avoiding killing the current shell command
hermes --profile son gateway run  # run as tracked background in Hermes when using tools
```

Verify logs show:

- `✓ telegram connected`
- `✓ slack connected`
- `Gateway running with 2 platform(s)`

### Primary provider auth failure

If logs say `Primary provider auth failed` or `Codex auth is missing access_token`, Son may still answer through fallback, but quality/reliability is degraded. This usually requires Son profile auth refresh (`hermes auth` / model re-auth) rather than prompt changes. Report it separately from gateway health.

## Reporting to Chris

Keep it concise:

- what was broken: gateway session, missing skill, or provider auth
- what was fixed now
- what remains user/auth-dependent
- next scheduled run time if relevant
