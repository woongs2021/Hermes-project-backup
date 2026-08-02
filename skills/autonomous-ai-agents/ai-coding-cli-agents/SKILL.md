---
name: ai-coding-cli-agents
description: "Use when delegating coding, PR review, or repository work to autonomous coding CLIs such as Claude Code, Codex, or OpenCode."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [autonomous-agents, coding-agents, claude-code, codex, opencode, delegation]
    related_skills: [autonomous-ai-agents]
---

# AI Coding CLI Agents

## Overview

This umbrella covers class-level orchestration of external autonomous coding CLIs. Treat each CLI as a worker process with its own strengths, flags, and interaction modes. The invariant is the same: provide a bounded goal, isolate work when needed, capture real output, verify changes yourself, and never claim success from the agent's self-report alone.

## When to Use

- Delegating feature implementation, bug fixes, refactors, or PR review to an installed coding-agent CLI.
- Running one-shot autonomous coding tasks from Hermes.
- Starting interactive or background agent sessions that may need PTY handling.
- Running multiple agents in parallel on separate worktrees.

## General Workflow

1. Inspect repository state and define the smallest useful goal.
2. Choose the CLI that is installed and authenticated.
3. Prefer non-interactive/print mode for bounded tasks; use PTY interactive mode only when the workflow requires dialogs.
4. For long tasks, start the process in background with notification on completion.
5. Read the produced diff, run tests/linters, and verify claims before reporting success.
6. If multiple agents operate in one repo, use separate worktrees/branches to avoid clobbering.

## Claude Code

- Best for feature work and PR-oriented coding when `claude` CLI is installed.
- Pay attention to PTY dialog handling for interactive mode; many prompts require an actual pseudo-terminal.
- Use print/non-interactive mode for repeatable automation and capture stdout/stderr.
- Review settings, allowed tools, and slash-command behavior before giving it broad repo authority.

## Codex

- Best for OpenAI Codex CLI delegation, one-shot fixes, and parallel issue handling.
- Use explicit flags for sandbox/approval/model behavior rather than relying on defaults.
- Be aware of Hermes Gateway caveats: background agent subprocesses may not inherit exactly the same interactive context.
- For PR reviews, give Codex the exact diff/range and require actionable findings.

## OpenCode

- Best for OpenCode CLI feature work, review, and interactive sessions.
- Resolve the binary path before starting; installations may expose different command names.
- Use background sessions for long interactive work and poll/log them deliberately.
- Keep the prompt narrow and include verification requirements.

## Common Pitfalls

1. **Trusting self-reports.** Always inspect files, diffs, and test output after an agent finishes.
2. **No branch/worktree isolation.** Parallel agents can overwrite each other in a shared checkout.
3. **Forgetting PTY mode.** Interactive CLIs can hang or misbehave without `pty=true`.
4. **Unbounded prompts.** Large vague goals create sprawling diffs and unverifiable outcomes.

## Verification Checklist

- [ ] CLI installed/authenticated and command path resolved.
- [ ] Goal, files, branch/worktree, and allowed scope are explicit.
- [ ] Agent output/logs captured.
- [ ] Diff reviewed by Hermes, not just the delegated agent.
- [ ] Relevant tests/linters/builds run with real output.
