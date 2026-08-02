# Curated Data Export to GitHub

Use this when a user wants to push local `data/`-style folders to a GitHub repo while excluding `.env` and other sensitive runtime files.

## Recommended workflow

1. Clone the target repo into a scratch path, not inside the source data tree.
2. Create a dedicated branch, e.g. `data-curated-upload`.
3. Prefer an allowlist export over copying a whole home/profile/runtime directory.
4. Add `.gitignore` before copying files.
5. Copy only curated artifacts into a repository-local `data/` directory.
6. For Hermes/profile data, sanitize rather than blindly uploading:
   - Redact delivery destination fields such as `chat_id`, `thread_id`, `user_id`, `account_id`, `group_code`, and full platform targets.
   - Exclude run outputs/backups unless explicitly needed and reviewed.
7. Stage files and inspect `git diff --cached --name-only` before committing.
8. Run a staged-file secret scan before commit/push.
9. After push, use PR Files changed or `git ls-tree`/`git show --name-only` to verify the remote content before merge.

## Baseline exclude patterns

Always exclude, even for private repos unless the user explicitly accepts the risk:

- `.env`, `.env.*`, `*.env`
- `auth.json`, `auth.lock`, credential/key/token/password named files
- `config.yaml`, config backups, channel directories, Slack/Telegram manifests
- `*.db`, `*.db-wal`, `*.db-shm`, `state.db*`, `kanban.db*`
- `sessions/`, `logs/`, `cache/`, `image_cache/`, `audio_cache/`, `tmp/`, `pastes/`
- profile runtime internals: profile `.env`, auth/config/channel files, logs, sessions, DBs, caches, `home/`, `bin/`, `hooks/`, `sandboxes/`, `memories/`
- cron `output/` and `*.bak*` files unless separately reviewed

## Hermes profile/cron export guidance

If the user asks to include profiles and cron, do not treat that as permission to upload all profile runtime state. A safer class-level default is:

Include conditionally:
- root `cron/jobs.json` after redacting destination IDs/targets
- profile `SOUL.md`
- profile `profile.yaml`
- profile `cron/jobs.json` after redaction
- deliberately authored profile docs/plans/design-system files

Exclude by default:
- profile `.env`, auth/config/channel files
- profile `state.db*`, `sessions/`, `logs/`, caches
- profile `memories/` unless the user explicitly wants private memory exported
- profile `skills/` if a scan produces many credential/API examples; skills often contain code snippets and provider examples that create noisy or risky scans
- cron run `output/` and backups, which may contain private conversation or delivery context

## Staged-file high-confidence scan pattern

A practical scan should check staged text files for high-confidence patterns, not merely any appearance of words like `token` because code may use local variables named `token`.

Regex classes to include:
- assignments involving `api_key`, `client_secret`, `access_token`, `refresh_token`, `authorization`, `bearer`, `password`, `private_key`, `credential`
- common token prefixes: `github_pat_`, `ghp_`, `gho_`, `ghu_`, `ghs_`, `glpat-`, `xoxb-`, `xoxp-`, `xoxa-`, `xoxr-`, `sk-`
- private key headers such as `BEGIN RSA PRIVATE KEY` and `BEGIN OPENSSH PRIVATE KEY`

Also run a separate exact search for known raw destination IDs if the repo contains messaging/cron config.

## Pitfalls

- Do not upload a whole `/opt/data` or equivalent runtime directory; it commonly contains logs, SQLite state, sessions, memories, profile auth, and cache files.
- Do not equate private repo with safe repo. Private repos still should not receive raw tokens, auth files, DBs, sessions, or logs.
- A broad keyword scan can produce false positives from variable names like `token`. Confirm with high-confidence assignment/prefix patterns before blocking, but do not ignore real matches.
- If GitHub authentication is unavailable, finish the local branch/commit and report that push/merge is blocked by credentials rather than weakening the security workflow.