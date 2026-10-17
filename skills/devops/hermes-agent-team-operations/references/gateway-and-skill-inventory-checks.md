# Gateway and Skill Inventory Checks

Use this reference when Chris asks whether the Hermes gateway/team is connected, or asks what skills the current Karina profile has.

## Gateway status check style

- Keep the Chris-facing answer concise, warm, Korean banmal, and status-oriented.
- Do not mirror full diagnostics or raw logs.
- Never print raw Telegram, Slack, OAuth, bot, API, or app tokens. Sanitize tool output before summarizing.
- State only the actionable status: gateway running/not running, configured platforms, specialist profile processes, and any material warning.
- If the gateway is running manually/foreground/docker rather than installed as a persistent service, mention that plainly because reboot/process exit can stop it.
- Recent Slack Socket Mode reconnect warnings or Telegram transient network reconnects are usually worth describing as “자동 재연결 계열” unless there is an active fatal error.

## Minimal verification sequence

1. Check `hermes gateway status`.
2. Check `hermes status` for messaging platform configuration and managed tool status.
3. Inspect recent gateway warnings/errors only enough to detect active failures; sanitize secrets and do not paste long logs.
4. If configuration/running status is not enough, send short smoke-test messages to Telegram home and the intended Slack target, and verify real success handles/message IDs before saying delivery works.
5. Summarize in Korean with bullets: Gateway, Telegram, Slack, specialist profiles, caveat/next action.

## Restart recovery pattern

Use this when Chris reports Telegram/Slack disconnection and the default/Karina gateway appears stuck or down.

1. Load the Hermes Agent skill first for current gateway commands, but do not edit protected bundled skills.
2. Check `hermes gateway status`, `hermes status --all`, and `send_message(action='list')` to separate process state, platform configuration, and target-directory state.
3. When running shell commands that may expose platform secrets, sanitize output before it enters the user-facing summary. Do not paste raw logs to Chris.
4. Be careful with `hermes gateway restart` in a foreground tool call: it may time out after stopping the gateway, leaving default/Karina down. If this happens, immediately check status and recent logs.
5. If no managed service is available, relaunch with tracked background `hermes gateway run` rather than shell-level `nohup`/`&`; then verify logs include Telegram connected, Slack connected, and `Gateway running with 2 platform(s)`.
6. After reconnection, perform end-to-end smoke sends to both platforms when appropriate. Report “sent successfully” only from tool success/message ID or equivalent evidence.
7. If the gateway is still manual rather than installed as a service, mention the stability caveat and recommend service installation only if failures recur.
8. For substantive operational repair, update Karina's daily team work log with decisions, evidence, caveat, and no secrets.

## Skill inventory reporting

When Chris asks what skills are available:

1. Use `skills_list` for the active skill list and count.
2. If asked to distinguish “newly made / our skills,” inspect local skill metadata/path/update history enough to classify, but label uncertainty when no explicit `created_by` or provenance field exists.
3. Separate active skills from archived skills. Archived skills under `.archive/` are useful context but should not be counted as active.
4. Prefer grouping by class-level umbrella vs bundled/hub/community/default skill rather than dumping every path.
5. Mention overlaps or umbrella consolidation opportunities briefly; curator can handle broad consolidation later.

## Classification language

Good wording:

- “명시적인 created_by 필드는 없어서 author/최근 수정일/umbrella 구조 기준으로 보면…”
- “active 목록은 N개이고, archive에는 예전 좁은 스킬들이 더 있어.”
- “우리가 정리한 커스텀 umbrella로 보이는 건…”

Avoid:

- Claiming exact authorship when metadata does not prove it.
- Treating archived one-session skills as active capabilities.
- Printing full filesystem listings unless Chris asks for paths.
