# Docker profile gateway watchdog pattern

Use this when Chris needs multiple specialist Hermes profile gateways (Yuna, Go Youn-jung, Son, Faker, Muyeol, etc.) to stay alive in a Docker-based Hermes deployment.

## Why this exists

In Docker deployments, `hermes --profile <name> gateway install` can correctly report that service installation is unnecessary because the container runtime is the service manager. If the container entrypoint only starts the default/Karina gateway, specialist profile gateways may not come back automatically after restart.

## Preferred durable fix

If Docker host / image control is available:

1. Set the container restart policy at the host/runtime layer, e.g. `unless-stopped`.
2. Update the container entrypoint or supervisor to start every intended profile gateway.
3. Include duplicate guards so the same Telegram/Slack bot does not run multiple polling/socket processes.

## In-container fallback when host/root control is unavailable

If the agent cannot edit `/entrypoint.sh` or access the Docker daemon socket, use a local no-agent watchdog cron owned by the default gateway:

1. Create a script under `/opt/data/scripts/`, for example `ensure-specialist-gateways.sh`.
2. The script should loop over intended profile names, check `pgrep -f "hermes --profile <profile> gateway run"`, and start missing gateways with `nohup hermes --profile "<profile>" gateway run >>/opt/data/logs/gateway-<profile>.log 2>&1 </dev/null &`.
3. The script should stay silent on stdout so `no_agent` cron with `deliver=local` does not message Chris.
4. Create a default-profile cron job, e.g. every 5 minutes, with `script=<script>`, `no_agent=true`, `deliver=local`.
5. Run one scheduler tick and verify the watchdog job status is `ok` and every specialist `hermes --profile <profile> gateway status` reports running.

## Safety notes

- This is an operations watchdog, not a user-facing specialist proxy. It must not send specialist content as Karina/default.
- Do not print or log Telegram/Slack tokens. Check only configured/running status and delivery handles.
- Avoid duplicate gateways for the same profile/bot. Always use a process guard before starting a profile gateway.
- Treat this as a fallback. The cleanest durable fix remains Docker host restart policy plus entrypoint/supervisor startup for each profile.

## Evidence to report

- Watchdog cron job id and schedule.
- Script path.
- `last_status=ok` for watchdog tick.
- Per-profile gateway running status.
- Any remaining limitation, e.g. Docker daemon inaccessible or root-owned entrypoint not editable.
