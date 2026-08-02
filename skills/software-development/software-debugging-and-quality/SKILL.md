---
name: software-debugging-and-quality
description: "Use when diagnosing software defects, validating implementation plans, debugging Python/Node processes, running TDD, requesting review, or simplifying recent code changes."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [debugging, tdd, code-review, refactoring, quality, python, node]
    related_skills: []
---

# Software Debugging and Quality

## Overview

This umbrella covers the class-level loop for understanding, testing, fixing, reviewing, and simplifying code. Use it to avoid the common failure mode of patching symptoms before proving the root cause.

## When to Use

- A bug, failing test, regression, or flaky behavior needs diagnosis.
- You need debugger-level inspection in Python or Node.js.
- The user asks for TDD, a spike, a code review, or cleanup of recent changes.
- A change should be verified before commit/PR.

## Core Loop

1. **Understand before editing**: reproduce the symptom and identify the responsible path.
2. **Make the failure executable**: add or run the smallest test/probe that captures the issue.
3. **Change the minimum code**: fix the root cause, not adjacent symptoms.
4. **Verify broadly enough**: run the targeted test plus relevant adjacent tests/linters.
5. **Review and simplify**: inspect the diff for security, maintainability, and unnecessary complexity.

## Systematic Debugging

- Use the four-phase pattern: root-cause investigation, pattern analysis, hypothesis/testing, implementation.
- Collect evidence from logs, stack traces, tests, source reading, and runtime probes.
- Do not edit until you can explain why the current behavior happens.

## Test-Driven Development

- Enforce RED → GREEN → REFACTOR when adding behavior or fixing a bug.
- RED: write or identify a failing test that proves the desired behavior.
- GREEN: implement the smallest fix.
- REFACTOR: simplify while keeping tests green.
- If you changed production code before a failing test existed, stop and add the test before continuing.

## Spikes

- Use throwaway experiments to validate uncertain libraries, APIs, performance assumptions, or architecture choices.
- Time-box the spike and produce a verdict: VALIDATED, PARTIAL, or INVALIDATED.
- Do not merge spike code directly; translate learnings into production-quality code.

## Python Debugging

- Use `pdb` for local breakpoints, post-mortem debugging, and quick pytest inspection.
- Use `debugpy` when a running process needs DAP/remote attach behavior.
- Prefer no-source-edit launch modes for quick probes; remove any temporary breakpoints before finalizing.

## Node.js Debugging

- Use `node inspect` or `--inspect` with the Chrome DevTools Protocol for Node processes.
- Attach to running processes when restarting would hide the bug.
- For performance/memory issues, capture heap snapshots or CPU profiles rather than guessing.

## Node/npm CLI setup and OAuth connection

Use this lane when installing or connecting a Node-based CLI tool before validation, especially CLIs that authenticate through a browser and `localhost` callback.

- Check package metadata first with `npm view <package> version description bin --json` so you know the expected binary names.
- If global install fails because `/usr/local` is not writable, use a user-owned npm prefix (for this environment, `/opt/data/.npm-global`) and export that `bin` directory into `PATH`; avoid sudo unless the user explicitly wants a system-wide install.
- Verify install by running the CLI help/version commands before attempting real workflows.
- For browser OAuth from a remote/container Hermes host, start the auth command in a tracked background process on a fixed port, send the user the auth URL, then if their browser lands on `localhost:<port>/callback?...` and fails, ask them for the full callback URL and replay it from the Hermes host with `curl`.
- Confirm authentication with a read-only command such as model/workspace/account listing. Never print access tokens.
- Session-proven details, including the Higgsfield CLI pattern, are in `references/node-cli-loopback-oauth-setup.md`.

## Node/CLI Tool Setup and Authentication

When validating whether a Node-based CLI can be connected, make the check executable and finish with a real verification command.

1. Check `node -v`, `npm -v`, global npm prefix, and package metadata with `npm view <pkg> version description bin --json` before installing.
2. Try the requested install path first if low-risk. If global install fails with `EACCES` under `/usr/local`, do not escalate to root by default; set a user-owned prefix such as `npm config set prefix /opt/data/.npm-global`, install again, and run commands with `PATH="/opt/data/.npm-global/bin:$PATH"`.
3. Verify the installed CLI with `--help`, `version`, or an equivalent read-only command; report exact aliases/binaries discovered from package metadata.
4. For browser/OAuth CLI logins, start the login in a tracked background process when the tool waits for callback approval, share only the generated authorization URL, and keep the process alive for the user's callback.
5. After the user approves, verify with a non-secret command such as `auth status`, `account`, `model list`, or another read-only endpoint. Never print raw access tokens from commands like `auth token`.

## Code Review and Simplification

- Before handoff, get the diff, run static/security checks, run relevant tests, self-review, and if useful ask an independent reviewer subagent.
- For cleanup, consider parallel review perspectives: complexity, correctness, and deletion/simplification opportunities.
- Keep only fixes that are supported by failing tests, clear evidence, or measurable simplification.

## Exploratory Web-App QA / Dogfooding

Use this lane when the target is a running web app rather than a code diff: the same quality loop applies, but the executable evidence is browser interaction, console output, screenshots, and a structured bug report.

1. **Plan scope and sitemap.** Identify target URL, user flows, navigation areas, forms, edge cases, and an output directory for screenshots/report.
2. **Explore systematically.** For each page/flow, use browser navigation, DOM snapshots, screenshots, and interaction tests; check browser console after every navigation and significant interaction.
3. **Exercise edges.** Test keyboard navigation, empty/invalid form submissions, long/special-character inputs, scroll states, and rapid/repeated interactions.
4. **Collect evidence.** For every issue, record URL, reproduction steps, expected vs actual behavior, console errors, severity/category, and screenshot path.
5. **Report clearly.** De-duplicate, sort by severity, and write a report from `templates/web-dogfood-report-template.md`; classify with `references/web-dogfood-issue-taxonomy.md`.

## Common Pitfalls

1. **Skipping reproduction.** You cannot verify a fix for a bug you never reproduced.
2. **Debugger leftovers.** Remove breakpoints, debug ports, print spam, and temporary probes.
3. **Overfitting tests.** A test that mirrors the implementation does not protect behavior.
4. **Review without running code.** A textual review is not a substitute for execution.

## Verification Checklist

- [ ] Failure or need reproduced/confirmed.
- [ ] Root cause explained in concrete code paths.
- [ ] Test/probe added or selected before changing behavior where practical.
- [ ] Targeted and adjacent verification commands run.
- [ ] Diff reviewed for security, complexity, and accidental artifacts.
