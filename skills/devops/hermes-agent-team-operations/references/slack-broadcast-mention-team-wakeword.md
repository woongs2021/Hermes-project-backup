# Slack broadcast mentions as team-wide wake words

Session learning: in a shared Slack team channel with one Slack app/bot per Hermes profile, users may want `@everyone`, `@channel`, or `@here` to wake all specialist agents instead of manually mentioning each bot.

Implementation pattern:
- Keep `SLACK_REQUIRE_MENTION=true` for specialist profiles so ordinary channel chatter remains quiet.
- In the Slack adapter mention-gating logic, treat Slack broadcast tokens as equivalent to a bot mention for routing only:
  - `<!everyone>`
  - `<!channel>`
  - `<!here>`
- Preserve normal individual bot mention behavior: `<@BOT_USER_ID>` still works.
- Do not disable mention gating globally just to get team-wide wakeups; that makes every channel message noisy.

Verification pattern:
- Add/extend Slack mention-gating tests so messages containing each broadcast token pass when `require_mention=true`.
- Restart every running profile gateway after adapter/code changes; profile gateways cache running code until restart.
- Verify each profile gateway reconnects to Slack Socket Mode and any other active platform.

Operational notes:
- Slack display text may show `@everyone`, `@channel`, or `@here`, but the event text routed to the adapter uses the token forms above.
- This is best for explicit team summons. Karina should still synthesize final answers so parallel specialist voices do not replace orchestration.
