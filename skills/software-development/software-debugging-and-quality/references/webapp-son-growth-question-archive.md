# Webapp Son growth-question archive expansion

Use when Chris asks to show more of Son's real questions in the Hermes Project Webapp, especially the OBD Map / growth graph area.

## Source of truth

- Prefer `/opt/data/agent-team-work-log/growth-question-sources/son-question-source-log.jsonl` for actual delivered Son questions.
- Use public-safe fields only: `date_kst`, `week_kst`, `question_text`, `obd_theme`, and high-level source tags.
- Do not expose raw Telegram/Slack logs, private IDs, profile tokens, internal credential paths, or long upstream refs in the public UI.

## Implementation pattern

1. Locate the rendered Son question section in the webapp, usually `src/App.tsx` around `sonWeeklyQuestionGroups`, `chrisGrowthGraphPoints`, and `ChrisGrowthGraphPanel`.
2. Compare UI counts against actual rendered arrays. Fix mismatches like a label saying `Son 질문 7개` while only 5 list items render.
3. Group questions by `week_kst` and theme, keeping the UI readable. For a large log, show a scrollable weekly archive rather than a flat wall of text.
4. Keep graph interpretation modest: Son's questions should be framed as a public-safe operating-language trail, not as a literal growth score or psychological measurement.
5. Update summary chips to reflect source-backed counts, e.g. `50 Son source-log questions`, `6 weekly groups`, `actual Son DM archive`.
6. Verify with browser/DOM probes, not source inspection alone:
   - expected group count
   - expected total question count
   - first/last week visible
   - scrollability of the question archive
   - desktop/tablet/mobile `overflowX === 0`
   - no console/page errors
7. If unrelated manifest/assets are dirty in the worktree, commit only files relevant to the user's request.

## Copy style

- Say “Son의 source-flow 로그에 남은 실제 질문” rather than implying invented or reconstructed questions.
- Use concise Korean public-facing question summaries; preserve meaning, but avoid raw prompt plumbing.
- If the source log contains multiple-choice questions, the public UI may shorten options into the core judgment axis when space is limited.
