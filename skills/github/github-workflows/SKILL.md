---
name: github-workflows
description: "Use when managing GitHub authentication, repositories, issues, pull requests, code review, CI troubleshooting, or repository inspection through git and gh."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [github, git, gh, pull-requests, issues, code-review, repository-management]
    related_skills: []
---

# GitHub Workflows

## Overview

This umbrella covers GitHub work from Hermes: authentication, repository management, issue triage, PR lifecycle, code review, CI troubleshooting, releases, and codebase inspection. Prefer `gh` and `git` for actions, verify every side effect, and report exact URLs/IDs produced by the tools.

## When to Use

- Setting up or diagnosing GitHub auth with HTTPS tokens, SSH keys, or `gh auth`.
- Cloning, forking, creating, archiving, or configuring repositories.
- Creating, searching, labeling, assigning, or triaging issues.
- Opening, updating, reviewing, merging, or troubleshooting pull requests.
- Inspecting codebase size/language composition before planning or review.

## Auth and Environment

- Check `gh auth status` and `git remote -v` before assuming credentials.
- Respect the repo's existing protocol (SSH vs HTTPS) unless the user asks to change it.
- Use the helper script under `scripts/github-auth-gh-env.sh` if environment normalization is needed.

## Repository Management

- Use `gh repo` for create/fork/clone settings and `git` for local state.
- Verify remotes, default branch, branch protection, and permissions before destructive operations.
- Keep a record of URLs returned by `gh` after creating repos, releases, or PRs.
- For Hermes data/profile/runtime exports, never copy the whole data directory. Use an allowlist export, redact delivery IDs, scan staged files, and follow `references/hermes-data-export-security.md`.
- For local data-folder exports, especially Hermes/profile/cron data, use an allowlist export plus staged-file secret scan rather than copying whole runtime directories. See `references/github-curated-data-export.md`.
- For Chris's Faker/homepage + Karina/Hermes agent-system backups, keep two private repo-shaped export sets and preserve the implementation boundary while coding new data producers; see `references/chris-split-github-backup-sets.md`.
- For data/artifact uploads, prefer a safety-first curated export workflow: deny broad source-tree copies, create an allowlisted `data/` export, write `.gitignore` first, stage only selected files, run a staged-file secret scan, and only then commit/push. See `references/github-curated-data-export.md`.
- For Chris's monthly Hermes/Faker/Karina backups, keep homepage data and Karina agent-system backups as two private repo-shaped export sets with allowlist copying and independent secret scans. See `references/monthly-curated-hermes-backup-sets.md`.

## Data / Asset Uploads to GitHub

When the user asks to push local data files or assets into a GitHub repo:
- Do **not** copy broad runtime roots such as `/opt/data` wholesale. Treat them as high-risk because they may contain logs, databases, sessions, memories, profile state, and credentials.
- Ask for or infer the narrowest explicit allowlist of files/folders to upload, then copy only those into the repo.
- Add or verify `.gitignore` entries for `.env`, `.env.*`, credential/key material, token/secret naming patterns, logs, state DBs, cache folders, and session stores before staging.
- Run a pre-commit secret/sensitive-file review using `git status`, `git diff --cached --name-only`, and targeted content scans for common secret markers before pushing.
- Prefer branch → PR/merge flow for user-visible uploads, and verify the target branch/merge result with live git/GitHub output before reporting success.

## Issues

- Search first to avoid duplicates.
- Use labels, assignees, milestones, and templates deliberately.
- For bug reports or feature requests, adapt migrated templates such as `templates/github-issues-bug-report.md` and `templates/github-issues-feature-request.md` rather than inventing structure.

## Pull Requests and CI

- Branch from the correct base, make focused commits, and use conventional commit language when appropriate.
- Generate PR bodies from the feature/bugfix templates when they fit.
- After opening a PR, watch checks with `gh pr checks` and inspect failing logs before summarizing.

## Code Review

- Review the diff, not just the PR title.
- Separate blocking correctness/security issues from nits.
- Use the migrated review output template in `references/github-code-review-review-output-template.md` for structured summaries.
- If posting comments, verify the GitHub API/`gh` command succeeded.

## Codebase Inspection

- Use language/LOC tooling before estimating project size or refactor scope.
- Exclude generated, vendored, dependency, build, and cache directories.
- Use inspection results as planning input, not as a substitute for reading critical files.

## Common Pitfalls

1. **Acting without auth verification.** `gh` may target the wrong account or no account.
2. **Wrong repository or branch.** Always print/inspect current repo and branch before PR actions.
3. **Duplicate issues.** Search existing issues first.
4. **Claiming CI status from memory.** Query checks live.
5. **Posting unverified review comments.** Confirm API status or resulting URL.

## Verification Checklist

- [ ] `gh auth status` or equivalent verified when needed.
- [ ] Target owner/repo and branch confirmed.
- [ ] Side-effect commands returned success and durable handles.
- [ ] PR/issue/repo URLs captured.
- [ ] CI/test/review claims backed by real output.
