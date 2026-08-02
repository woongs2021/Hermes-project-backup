# Session reference: Karina specialist team setup

This reference captures a reusable example, not a full transcript.

## Scenario

The user wanted a main orchestrator persona, Karina, to manage four new Hermes specialist profiles:

- `yuna`: research agent for market research, paper search, benchmarking, and insight synthesis
- `son`: PM agent for planning, prioritization, roadmap, task breakdown, and coordination
- `faker`: coding agent for implementation, debugging, prototyping, automation, and technical review
- `muyeol`: validation/security agent for fact-checking, QA, risk, security review, and final audit

The user also wanted the existing 09:30 KST AI/design briefing that Karina had been doing to be delegated to `yuna`.

## Concrete steps used

1. Create profiles:
   - `hermes profile create yuna --description "Research agent. Handles market research, paper search, benchmarking, and insight synthesis."`
   - `hermes profile create son --description "PM agent. Handles planning, prioritization, roadmap, task breakdown, and project coordination."`
   - `hermes profile create faker --description "Coding agent. Handles implementation, debugging, prototyping, automation, and technical review."`
   - `hermes profile create muyeol --description "Validation and security agent. Handles fact-checking, QA, risk analysis, security review, and final audit."`

2. Non-interactive setup was insufficient by itself, so profile config was set explicitly:
   - `hermes --profile <name> config set model.provider openai-codex`
   - `hermes --profile <name> config set model.default gpt-5.5`
   - `hermes --profile <name> config set model.base_url https://chatgpt.com/backend-api/codex`
   - `hermes --profile <name> config set terminal.backend local`
   - `hermes --profile <name> config set agent.max_turns 90`

3. Smoke test each profile:
   - `hermes --profile <name> chat -Q -q "Smoke test: reply with exactly OK-<name>"`

4. Check actual SOUL path. In the container, the real files were:
   - `/opt/data/SOUL.md`
   - `/opt/data/profiles/yuna/SOUL.md`
   - `/opt/data/profiles/son/SOUL.md`
   - `/opt/data/profiles/faker/SOUL.md`
   - `/opt/data/profiles/muyeol/SOUL.md`

5. Write Karina/default `SOUL.md` as the main orchestrator with routing rules.

6. Patch each specialist `SOUL.md` to say the specialist is managed by Karina and should treat Karina as coordination lead.

7. Update the 09:30 KST briefing cron job:
   - list cron jobs
   - find the AI/design briefing job
   - update it with `profile='yuna'`, a self-contained Yuna prompt, `deliver='origin'`, and the same KST schedule (`30 0 * * *`)

8. Initialize and verify Kanban:
   - `hermes kanban init`
   - `hermes kanban assignees`
   - `hermes kanban stats`

## Verification observed

- `hermes profile list` showed all four specialists with model `gpt-5.5`.
- Smoke tests returned `OK-yuna`, `OK-son`, `OK-faker`, `OK-muyeol`.
- Cron listing showed the 09:30 briefing with `profile: yuna`.
- Kanban assignees listed `default`, `yuna`, `son`, `faker`, and `muyeol`.

## Durable lesson

For profile teams, the durable configuration spans several layers: profile config, SOUL files, cron job profile ownership, and Kanban assignees. Updating only one layer leaves the team concept incomplete.
