# Docker specialist gateway watchdog pattern

Use this when Chris wants specialist profile gateways (Yuna, Go Youn-jung, Son, Faker, Muyeol, etc.) to stay alive for profile-local cron delivery, but `hermes --profile <name> gateway install` reports that service installation is not needed because Hermes is running inside Docker.

## Problem shape

- Specialist recurring loops must deliver from the owning specialist profile/bot, not Karina/default.
- Profile-local cron jobs only fire reliably when the corresponding profile gateway is running.
- In Docker deployments, `hermes gateway install` may be a no-op because the container runtime is the service manager.
- The agent may not have permission to edit `/entrypoint.sh` or access the Docker daemon socket from inside the container.

## Preferred durable fix when host/root access exists

1. Set the container restart policy at the Docker host layer, e.g. `unless-stopped`.
2. Add profile gateway startup to the container entrypoint or service supervisor.
3. Use duplicate guards before launching each profile gateway:

```bash
pgrep -f "hermes --profile yuna gateway run" >/dev/null || nohup hermes --profile yuna gateway run >>/opt/data/logs/gateway-yuna.log 2>&1 </dev/null &
```

## In-container fallback when host/root access is unavailable

Create a local script under `/opt/data/scripts/ensure-specialist-gateways.sh` that checks every required profile and starts any missing gateway. Keep it silent on success so a no-agent cron does not deliver routine noise.

```bash
#!/usr/bin/env bash
set -euo pipefail
LOG_DIR="/opt/data/logs"
mkdir -p "$LOG_DIR"

for profile in yuna goyounjung son faker muyeol; do
  [[ -d "/opt/data/profiles/${profile}" ]] || continue
  if ! pgrep -f "hermes --profile ${profile} gateway run" >/dev/null 2>&1; then
    nohup hermes --profile "${profile}" gateway run >>"${LOG_DIR}/gateway-${profile}.log" 2>&1 </dev/null &
    printf '%s started profile=%s pid=%s\n' "$(date -u +%FT%TZ)" "$profile" "$!" >>"${LOG_DIR}/specialist-gateway-watchdog.log"
  fi
done
```

Then schedule it from a gateway that is already automatically started by the container, usually default/Karina:

```text
schedule: every 5m
deliver: local
no_agent: true
script: ensure-specialist-gateways.sh
profile: default
```

## Verification

- Run the script once manually and confirm it exits `0`.
- Run/tick the watchdog cron once and confirm `last_status=ok`.
- Check each profile:

```bash
hermes --profile yuna gateway status
hermes --profile goyounjung gateway status
hermes --profile son gateway status
hermes --profile faker gateway status
hermes --profile muyeol gateway status
```

- Check profile-local cron status:

```bash
hermes --profile <profile> cron status
```

## Reporting to Chris

Keep it concise:

- Say whether true service install was possible.
- If Docker blocked service install, say that the container runtime owns persistence.
- Report the fallback watchdog job ID, script path, and running status.
- Do not print raw Telegram/Slack tokens or long logs.

## Pitfalls

- Do not launch duplicate gateways for the same profile/bot; always use `pgrep` guards.
- Do not call the fallback watchdog a full host-level restart policy. It is an in-container resilience layer that depends on the default gateway/container coming back.
- Do not route specialist user-facing content through the default watchdog cron. The watchdog should be `local` and `no_agent` only.
