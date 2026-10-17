---
name: github-workflows
description: "Use when managing GitHub authentication, repositories, issues, pull requests, code review, CI troubleshooting, GitHub Pages waiting deploys (see references/github-pages-waiting-deploy.md), or repository inspection through git and gh."
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
- For Chris's Hermes backups, keep two curated repo-shaped export sets and preserve the implementation boundary while coding new data producers; backup pushes are **command-triggered, not recurring loops** unless Chris explicitly asks. Current remotes are `https://github.com/woongs2021/Hermes-project-backup.git` for Karina/Hermes agent-system backup and `https://github.com/woongs2021/Hermes-project-webapp.git` for the webapp/Pages repo. For the webapp repo, configure Vite for `base: '/Hermes-project-webapp/'` and GitHub Pages at `https://woongs2021.github.io/Hermes-project-webapp/`; see `references/chris-split-github-backup-sets.md`. If pushing `.github/workflows/*` through `gh`/OAuth, ensure the token has `workflow` scope (use `gh auth refresh -h github.com -s workflow`) before pushing.
- For Chris's command-triggered Hermes backup/webapp pushes, keep the two current remotes and Pages target in sync with `references/chris-split-github-backup-sets.md`: backup/private agent-system repo `Hermes-project-backup`, webapp repo `Hermes-project-webapp`, Vite base `/Hermes-project-webapp/`, and Pages target `https://woongs2021.github.io/Hermes-project-webapp/`. Run curated export + safety scan before branch/commit/push; ensure scanners skip `.git/` after repo initialization.
- For Chris's Hermes backup/webapp repositories, use the curated split workflow and Pages troubleshooting checklist in `references/chris-split-github-backup-sets.md`. The private backup repo remains command-triggered, not recurring. The webapp repo can have a coding loop, but publishing is approval-gated: daily coding stays local, the Saturday weekly candidate prepares build/safety evidence and asks Chris for explicit approval, and only after approval should an agent push the weekly branch, fast-forward/merge main, run GitHub Pages, and verify HTTP 200.
- For data/artifact uploads, prefer a safety-first curated export workflow: deny broad source-tree copies, create an allowlisted `data/` export, write `.gitignore` first, stage only selected files, run a staged-file secret scan, and only then commit/push. See `references/github-curated-data-export.md`.
- For Chris's webapp repo GitHub Pages deployment, use the Pages workflow/Vite-base/auth-scope troubleshooting pattern in `references/github-pages-curated-webapp-deploy.md`: add `workflow` scope when pushing workflow files, enable Pages with `build_type=workflow`, allow `main` in the `github-pages` environment branch policy when needed, remove `node_modules/`/`dist/` before staging, and verify the final URL with HTTP 200. If a pushed Pages update does not appear and the latest Actions run has `build` success but `deploy` stuck in `waiting`, use `references/github-pages-waiting-deploy-recovery.md` and `references/github-pages-waiting-deploy-concurrency.md`: check for a stuck Pages concurrency run, change Pages workflow concurrency to `cancel-in-progress: true` when appropriate, retrigger, then verify the live manifest/asset rather than assuming browser cache.
- For splitting Chris's webapp 4K/HQ originals out of the Pages repo while preserving download buttons, use `references/webapp-asset-repo-split-for-4k-downloads.md`: keep previews/thumbnails in `Hermes-project-webapp`, upload 4K/HQ originals to a public asset repo GitHub Release, point manifest `downloadSrc` at release asset URLs, and do not rewrite history or force-push without explicit approval. For the complete inventory → resumable upload → manifest conversion → live Pages verification sequence, use `references/github-release-asset-externalization-runbook.md`. When Chris explicitly approves post-migration cleanup, delete **only** the inventory-derived originals after comparing each local file's byte size with the Release asset and confirming every manifest item has a local display preview plus external download URL. Stage-check the exact deletion count before push. Update both repositories' root `README.md` files in the same delivery: document the phase-by-phase implementation state, current Release/tag/count, display-versus-download contract, verification status, and clearly distinguish current-tree cleanup from a separate history rewrite.
- For Chris's iterative webapp UI/copy polish on GitHub Pages, use `references/github-pages-webapp-ui-polish.md`: preserve marketing/product-intro tone rather than changelog-like copy, avoid overclaiming Chris's personal growth, verify desktop and mobile separately with computed styles, guard Vite base-path image helpers against double-prefixing, and live-smoke the final Pages URL.
- If a GitHub Pages build succeeds but the deploy job stays `waiting`, check workflow concurrency. A stuck Pages deploy can block later updates when `concurrency.cancel-in-progress: false`; switch it to `true`, push a small workflow commit to cancel/replace the stuck run, then verify live manifest plus live DOM/image hash rather than trusting push success.
- For Chris Archive dashboard/modal work specifically, use `references/chris-archive-webapp-dashboard-qa.md`: verify desktop/tablet/mobile grid counts, modal viewport containment, all archive image assets, and avoid scroll-jank by reserving scrollbar gutter while toggling only scrollbar color during scroll.
- For Chris Archive image ingestion and Design DNA milestones, use `references/chris-archive-image-ingestion-and-dna-workflow.md`: `추가해줘` means archive without extra confirmation, check exact duplicate hashes before adding, write a reusable analysis note, sync the webapp manifest/public asset, verify the new tile by title/id rather than relying on visual last position, and treat counts like 60 references as a DNA-analysis threshold. Keep GoYJ-generated selected assets separate from Chris Archive references: they belong under the webapp `Design DNA → DNA Dashboard` sub-tab, backed by `public/data/dna-archive.json` and `public/assets/dna-archive/...`, and are added only after Chris says `저장해줘`.
- For Vite public assets on Chris's Pages webapp, guard against `/assets/...` root-path breaks and double-prefixing with `import.meta.env.BASE_URL`. Use the idempotent helper and live smoke checklist in `references/vite-pages-public-assets-and-live-smoke.md`, especially browser checks for image `complete/naturalWidth` and computed CSS/layout values after deployment.
- For Vite public assets on Chris's Pages webapp, guard against `/assets/...` root-path breaks and double-prefixing with `import.meta.env.BASE_URL`. Use the idempotent helper and live smoke checklist in `references/vite-pages-public-assets-and-live-smoke.md`, especially browser checks for image `complete/naturalWidth` and computed CSS/layout values after deployment. Also verify that public asset filenames are not accidentally excluded by broad `.gitignore` patterns such as `*token*`; if a manifest item 404s on Pages while it exists locally, check `git check-ignore -v <asset>` and rename the public asset/manifest path rather than forcing ignored secret-like filenames into git.
- When Chris's Pages webapp grows from 4K/HQ generated images or mockups, separate display assets from download originals: keep lightweight previews in the webapp repo, store 4K/HQ originals in a public asset repo release or object storage, and point manifest `downloadSrc` at the external URL. Measure actual repo/public asset size first, do not rewrite history without explicit approval, and see `references/webapp-large-asset-externalization.md`.
- If a push succeeds but GitHub Pages keeps serving an old manifest/image, do not assume browser cache. Check the Pages workflow status: the build job can succeed while the deploy job remains `waiting`. For Chris's Pages repo, changing workflow concurrency from `cancel-in-progress: false` to `true` can cancel a stuck waiting deploy and allow the new deploy to proceed. See `references/github-pages-deploy-waiting-and-asset-verification.md`.
- For replacing the Visual Archive hero/camera image, keep the existing public asset path stable, update alt text, avoid screenshots if Chris requested that review mode, and verify by source/live SHA-256 plus browser `img.complete && naturalWidth > 0`; see `references/chris-webapp-visual-archive-asset-replacement.md`.
- If deploying from a Git worktree where `main` is already checked out in another worktree, do not stop at `fatal: 'main' is already used by worktree ...`. After validation and commit on the active feature branch, push the feature branch normally, then, if Chris approved direct deployment, update remote `main` with a refspec such as `git push origin <feature-branch>:main`; verify `refs/heads/main` and the feature branch point to the same commit, then perform the usual GitHub Pages live smoke. See `references/git-worktree-branch-conflict-pages-deploy.md`.
- For Chris's monthly Hermes/Faker/Karina backups, keep homepage data and Karina agent-system backups as two private repo-shaped export sets with allowlist copying and independent secret scans. See `references/monthly-curated-hermes-backup-sets.md`.

## Data / Asset Uploads to GitHub

When the user asks to push local data files or assets into a GitHub repo:
- Do **not** copy broad runtime roots such as `/opt/data` wholesale. Treat them as high-risk because they may contain logs, databases, sessions, memories, profile state, and credentials.
- Ask for or infer the narrowest explicit allowlist of files/folders to upload, then copy only those into the repo.
- Add or verify `.gitignore` entries for `.env`, `.env.*`, credential/key material, token/secret naming patterns, logs, state DBs, cache folders, and session stores before staging.
- Run a pre-commit secret/sensitive-file review using `git status`, `git diff --cached --name-only`, and targeted content scans for common secret markers before pushing.
- Prefer branch → PR/merge flow for user-visible uploads, and verify the target branch/merge result with live git/GitHub output before reporting success.

## GitHub Pages deploy waiting pitfall

For Chris's webapp Pages repo, a push can build successfully while the `deploy` job remains `waiting`, leaving the live site on an older manifest even though `git push` succeeded. When this happens:
- Query recent workflow runs/jobs/deployments if possible, but avoid over-polling GitHub API into rate limits.
- Check the live `data/brand-mockup-assets.json` and asset hash directly; live manifest/hash is the user-visible source of truth.
- If an old Pages deployment is stuck, set the Pages workflow concurrency to cancel stale runs, e.g. `concurrency: group: pages` with `cancel-in-progress: true`, then trigger a fresh commit/deploy.
- Do not report deployment complete until the live manifest references the new revision filename, the live image URL returns `200 image/*`, and a browser smoke test shows the new `imageSrc` in the DOM.

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
4. **Claiming CI/status or deploy completion from memory/push output.** Query checks live; for GitHub Pages waiting deploy recovery, see `references/github-pages-waiting-deploy.md`.
5. **Posting unverified review comments.** Confirm API status or resulting URL.

## Verification Checklist

- [ ] `gh auth status` or equivalent verified when needed.
- [ ] Target owner/repo and branch confirmed.
- [ ] Side-effect commands returned success and durable handles.
- [ ] PR/issue/repo URLs captured.
- [ ] CI/test/review claims backed by real output.
