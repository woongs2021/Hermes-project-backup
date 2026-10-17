# Son data-backed webapp graph handoff

Use this pattern when Chris asks Karina to check Slack/Faker requests and make the webapp graph reflect Son's **actual data/interpretation**, not Faker's provisional Son-like copy.

## Trigger

- Chris says variants of: `슬랙의 페이커 요청사항 확인해서 손의 실제 데이터 기반으로 웹앱 그래프 적용하게 해줘`.
- Faker has reported or requested in Slack that a graph/copy/UI element needs Son's growth/business/PM framing.
- Son has not yet answered in the Slack thread, or the visible Slack reply is insufficient, but Son's local loop data exists.

## Operating pattern

1. **Check Slack thread first.** Confirm what Faker asked, what Chris corrected, and whether Son actually replied. Do not claim Slack contains Son's answer if the thread only contains Faker's request.
2. **Use Son's actual local sources to unblock.** Prefer stored Son-owned data over invented “Son-style” copy:
   - `/opt/data/hermes-growth-sns-loop/events.jsonl`
   - `/opt/data/hermes-growth-sns-loop/insights.md`
   - `/opt/data/hermes-growth-sns-loop/daily/*.md`
   - `/opt/data/hermes-growth-sns-loop/son-prep/*.md`
   - relevant Son daily work logs under `/opt/data/agent-team-work-log/son/daily/`
3. **Separate data layers clearly.** Public-safe dashboard/research/visual/final-pick counts may support the graph, but Son-derived axes/questions/judgment criteria must come from actual Son logs.
4. **Patch the webapp locally first unless Chris explicitly asks to publish.** Typical target: `august-dashboard/src/App.tsx` and adjacent CSS. Preserve GitHub deploy boundary: no commit/push/deploy until Chris says so.
5. **Make the graph read as Son's judgment model.** Good axis examples from the session:
   - Role ontology
   - Public-safe decision log
   - Artifact relationship
   - Delegation boundary
   - Control & adoption map
   - Evaluation validity
6. **Verify with real commands.** Run the local app checks used by the repo, typically:
   - `npm run validate:data`
   - `npm run lint`
   - `npm run build:public`
   - `git diff --check`
7. **Close the Slack loop.** Reply in the original thread with changed files, data sources, verification output summary, and deploy status. Tell Faker/Son what remains.
8. **Record Karina's daily team work log** when this affects multi-agent continuity.

## Pitfalls

- Do not treat Faker's provisional “Son-like” wording as Son's actual data.
- Do not wait indefinitely for a Slack reply if Son's persisted data already answers the task.
- Do not overstate delivery: distinguish local patch, verified build, commit, push, and live deploy.
- Do not expose raw Slack/Telegram tokens, private IDs, or copied private logs in the work log or Chris-facing summary.
