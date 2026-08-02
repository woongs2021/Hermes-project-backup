# Adding a specialist profile and splitting an existing agent lane

Use this when Chris adds a new named specialist to share work with an existing Hermes profile.

## Proven pattern

1. Define the split as routing lanes, not just a persona.
   - Existing agent: what remains in their ownership.
   - New agent: what becomes their ownership.
   - Overlap rule: when both should coordinate.

2. Create the new profile with a role-level description.
   - Example shape: `hermes profile create <profile> --description "<class-level capability summary>"`
   - Prefer lowercase ASCII profile names for CLI and gateway stability, while preserving the public display name in `SOUL.md`.

3. Configure the new profile consistently with the current team.
   - Match the team's current provider/model pattern unless Chris asked for a different model.
   - Do not copy credentials blindly between profiles; messaging bots require distinct tokens/apps.

4. Write the new profile `SOUL.md`.
   - Include primary mission, core responsibilities, working style, deliverables, collaboration rules, quality bar, Slack team-channel rules, and daily work-log protocol.
   - State that Karina is coordination lead/final synthesizer.
   - State tone boundaries, e.g. specialists use 존댓말 if that is the team convention.

5. Patch the existing profile whose lane changed.
   - Narrow its primary mission and deliverables.
   - Add an explicit coordination rule with the new specialist.
   - Update Slack/team-channel rules so future answers do not duplicate roles.

6. Patch Karina/default orchestration rules.
   - Add the new agent to the roster.
   - Add routing rules for both the new specialist and the narrowed existing specialist.
   - Update shared-channel decomposition guidance.

7. Update team work-log structure if the team uses daily agent logs.
   - Add the new agent to `/opt/data/agent-team-work-log/SCHEMA.md`.
   - Create the new agent's folder, usually `<agent>/daily/`.
   - Do not create placeholder daily notes for the new agent unless it actually performed substantive work.

8. Smoke test the profile.
   - Use a one-shot profile run asking for a short role self-introduction.
   - Verify the response matches role, language, and tone.
   - `hermes profile list` should show the profile and alias. Gateway may remain stopped until credentials are configured.

9. Record compact work context.
   - Update Karina's daily work log for substantive orchestration/config work.
   - Save only stable routing facts to memory; do not save transient profile status, session IDs, or task-completion narratives.

## Pitfalls

- Do not treat the new agent as only a name/persona. The useful artifact is the routing contract.
- Do not leave the old agent's SOUL broad; otherwise both agents will answer the same class of research.
- Do not start or promise messaging availability until a distinct Slack/Telegram credential exists for that profile.
- Do not paste raw tokens or private IDs into SOUL, logs, references, or final summaries.
