# Approval-gated weekly webapp Pages loop

Use this pattern when Chris wants ongoing webapp coding but does **not** want daily GitHub pushes or daily Pages deploys.

## Operating shape

- Daily coding job:
  - Runs from the specialist coding profile (usually Faker).
  - Works in a concrete repo/workdir, e.g. `/opt/data/projects/Hermes-project-webapp`.
  - Performs one small local coding task.
  - Runs local verification such as `cd august-dashboard && npm run build`.
  - Runs the repo safety scan before committing, e.g. `python3 scripts/scan_export_safety.py .`.
  - Commits locally to a weekly work branch if there are substantive changes.
  - Does **not** push, merge to `main`, or trigger Pages.
  - DMs Chris with a concise local status and reminds him that raw `localhost` is not directly reachable from Telegram unless a deliberate tunnel is configured.

- Weekly approval job:
  - Schedule the approval gate on Chris's requested day/time. Current proven pattern: Saturday 10:30 KST.
  - Prepare a local release candidate only.
  - Run build and safety scan.
  - Create or update a local weekly branch such as `webapp-weekly-YYYYMMDD`.
  - Save a local approval note with changed-file summary, branch, local commit SHA, build result, safety result, and proposed publish action.
  - Send Chris an approval request DM.
  - Stop before any remote side effect.

- After explicit approval:
  - Only after Chris approves the specific weekly candidate, push the weekly branch.
  - Merge/fast-forward `main`.
  - Push `main`.
  - Watch the GitHub Pages workflow.
  - Verify the Pages URL returns HTTP 200.
  - Report branch, main commit, workflow status, and preview URL.

## Guardrails

- Silence or prior approval is not approval. Approval must be explicit after the weekly candidate request.
- Do not push just because the loop is scheduled; the scheduled job is an approval request, not a deploy.
- Telegram cannot view this machine's raw `localhost`. Use GitHub Pages as the default user-checkable preview, or set up an explicit tunnel only after a separate security/scope decision.
- Avoid committing build-only timestamp churn. For Vite/dashboard projects, `npm run build` may update generated files such as `public/data/dashboard-manifest.json` only by `generatedAt`. If that is the only diff, reset it before committing/reporting. Keep generated manifest changes only when paired with substantive source/data/schema changes.
- Keep `deliver=local` for specialist-owned cron jobs that direct-send through the specialist bot; otherwise messages can appear from Karina/default.

## Suggested Saturday approval DM shape

Start with `Faker입니다.` and include:

1. 이번 주 로컬 반영 후보 요약
2. local branch name
3. local commit short SHA if any
4. build/safety scan result
5. current Pages URL as the last deployed baseline
6. explicit request: `승인해주시면 GitHub branch push → main 반영 → Pages 확인을 진행하겠습니다.`

If there are no substantive changes, say that nothing needs publishing and no approval is needed.
