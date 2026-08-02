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
4. Summarize in Korean with bullets: Gateway, Telegram, Slack, specialist profiles, caveat/next action.

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
