# Son SNS Marketer + Weekly Summary Pattern

Use when Chris wants Son to act not only as PM/growth-dialogue agent but also as a practical SNS marketer for Instagram, Facebook, LinkedIn, and Threads.

## Ownership split

- Karina owns the full weekly report and final synthesis.
- Muyeol owns validation rigor: final best-3 selection, risk/caution, evidence level, and a local validation summary for Son.
- Son owns the user-facing short weekly summary DM after Karina/Muyeol. Son translates validation into PM/marketing/action framing.
- Go Youn-jung owns the weekly abstract image, prompt, and “why this image” rationale.

## Friday cron chain

1. Karina final weekly report job delivers full report to Chris/Slack.
2. Muyeol downstream job uses `context_from` Karina final report and delivers `local` only. It should include:
   - core theme,
   - final best-3,
   - one sentence explaining why those 3 were selected,
   - validation caution/limitation,
   - selected-paper Korean translated title + original title + link.
3. Son downstream job uses `context_from` Karina final report + Muyeol local summary and delivers the user-facing Telegram DM from Son's own Telegram bot/profile, not Karina/default. If the cron job lives in the default/Karina cron store, keep `deliver=local` and have the Son-profile run send directly via Son's Telegram Bot API token without exposing credentials.

## Son weekly DM format

- Title: `손 주간보고 요약 — YYYY-MM-DD`
- Korean `~다` declarative style.
- Every summary bullet/sentence line starts with an emoji.
- 6–8 compact bullets:
  - weekly core theme,
  - why these 3 were selected,
  - compact final best-3,
  - Muyeol's main caution,
  - practical implication for Chris as OBD/design leader,
  - SNS/marketing angle for Instagram/Facebook/LinkedIn/Threads,
  - closing line that Karina handles the full report.
- Final section `선정 논문 3개`:
  - exactly 3 emoji-led lines,
  - Korean translated title,
  - original title in parentheses,
  - Telegram-compatible Markdown hyperlink when available,
  - if missing, write `링크 확인 필요다`; never fabricate links.

## Daily growth question addition

When Son's daily growth-question loop is active, add exactly one `SNS 마케팅 팁` line after the questions:

```markdown
오늘의 성장 질문
1. ...
2. ... (optional)

SNS 마케팅 팁
- ...

짧게 한두 문장만 답해주셔도 충분합니다.
```

Tips should be channel-aware but lightweight: for example LinkedIn = design-leadership framing, Threads = question/hook, Instagram = visual metaphor or carousel seed, Facebook = reflective narrative. Avoid generic growth-hack tone, unsupported claims, and AI-startup hype.
