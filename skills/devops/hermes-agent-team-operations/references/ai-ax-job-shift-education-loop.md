# AI/AX 일자리 변화 교육 루프

## Trigger
Use this pattern when Chris wants a recurring team loop that tracks AI/AX-driven job-market changes for education, design-career, and business-market learning.

## Session-proven structure
- Store under a dedicated loop root such as `/opt/data/ai-ax-job-shift-loop/`.
- Use Korean for human-readable Markdown/TXT/summary/JSON values, while preserving JSON keys, enum/status values, IDs, paths, URLs, code identifiers, route names, commands, and original source titles.
- Keep the loop local-first for intermediate work by default. If Chris explicitly asks for per-agent DM delivery, each owner should send a concise specialist DM from that specialist's own Telegram bot/window after its lane completes, while still saving the local Markdown/JSONL/graph artifacts.
- For per-agent DM delivery, do not route user-facing specialist messages through Karina/default. Use the specialist profile's gateway/home target when verified, or explicit specialist direct-send pattern from `references/direct-specialist-telegram-delivery.md`.

## Owner sequence
1. **Yuna** — AI/AX impact on jobs overall.
   - Runs Wed/Fri morning.
   - Splits Korea and global.
   - Uses credible reports/articles: government, OECD/WEF/ILO, consulting firms, labor/economics institutes, universities, reputable media, and major platform/company research.
   - Covers jobs at risk, jobs augmented, new roles, reskilling/education implications, uncertainty.
2. **Go Youn-jung** — design-role impact from Yuna’s result.
   - Runs after Yuna with `context_from` Yuna.
   - Splits Korea and global.
   - Focuses on UX/Product design, brand/design management, content/design ops, design education, hiring signals, junior-designer risk, senior design-leadership opportunity.
3. **Son** — business-market shift from Yuna + Go Youn-jung.
   - Runs after both with `context_from` Yuna and Go Youn-jung.
   - Splits Korea and global.
   - Tracks AX adoption, education/reskilling markets, HR tech, productivity tooling, creative/design services, outsourcing/automation, SMB vs enterprise differences, who pays, adoption blockers.
4. **Faker** — consolidates the three lanes into one tab/log structure.
   - Runs after all research lanes with `context_from` all three.
   - Does not build a full UI unless Chris explicitly approves; creates dashboard/webapp-ready tab logs and JSONL.
   - Marks missing upstream inputs instead of fabricating.
5. **Muyeol** — Friday-only validation.
   - Runs after Faker with `context_from` all four jobs.
   - Checks source legitimacy, Korea/global balance, duplicate claims, causal leaps, overclaiming, context separation, and JSONL/log parse/accumulation.
   - Sends concise Telegram validation with GO/WATCH/HOLD.

## Suggested folder contract
```text
/opt/data/ai-ax-job-shift-loop/
  README.md
  raw/yuna/YYYY-MM-DD.md
  raw/goyounjung/YYYY-MM-DD.md
  raw/son/YYYY-MM-DD.md
  tabs/overview/YYYY-MM-DD.md
  tabs/yuna-ai-ax/YYYY-MM-DD.md
  tabs/goyoungjung-design/YYYY-MM-DD.md
  tabs/son-business/YYYY-MM-DD.md
  tabs/graph/YYYY-MM-DD.md
  tabs/muyeol-validation/YYYY-MM-DD.md
  data/events.jsonl
  data/consolidated-index.jsonl
  data/graph-nodes.jsonl
  data/graph-edges.jsonl
  data/validation.jsonl
  weekly/YYYY-WW-validation.md
```

## Scheduling pattern
- Wed/Fri KST morning research/consolidation sequence:
  - 09:15 Yuna
  - 09:25 Go Youn-jung
  - 09:35 Son
  - 09:45 Faker
- Friday-only validation:
  - 09:55 Muyeol

Use UTC cron equivalents when creating jobs in Hermes (`15 0 * * 3,5`, etc.) because KST is UTC+9.

## Prompt requirements
- Require current source retrieval for factual claims.
- Require Korea/global separation.
- Require source URLs/IDs and source-access caveats.
- Distinguish evidence from interpretation.
- Append compact JSONL events with stable keys for future dashboards.
- For graph-engineering mode, require Faker to extract claim-graph nodes/edges rather than only narrative tabs: nodes such as `source`, `claim`, `job_role`, `task`, `skill`, `market`, `education_signal`, `risk`, `stakeholder`, `region`; relations such as `supports`, `affects`, `automates`, `augments`, `creates_role`, `requires_skill`, `creates_market`, `risks`, `needs_validation`, `weights_paper_loop`, `weights_obd_loop`.
- Require lightweight verification for Faker: file existence and JSONL parse.
- Avoid generic AI-startup hype and do not frame every signal as One UI unless Chris asks.

## Cross-loop weighting
- Chris wants high-quality findings from this loop to influence other loops when evidence is strong.
- Require each lane to record `paper_loop_weight_ko` when a source/theme should raise the priority of related paper discovery topics, source classes, keywords, or evaluation lenses.
- Require each lane to record `obd_loop_weight_ko` when a source/theme should raise the priority of OBD learning around market/category framing, job/capability shifts, education, stakeholder change, value exchange, or business-design leadership.
- Use `WATCH` for uncertain but important signals and `LOW` for weak evidence. Do not let one article over-steer the paper or OBD loops without repeat/source-quality support.

## Pitfalls
- Do not ask the same broad research question to every agent. Chain the work: Yuna gives job-market base, Go Youn-jung narrows to design jobs, Son translates into business markets, Faker structures logs, Muyeol validates.
- Do not send every intermediate report to Chris by default; it becomes noisy. Prefer local accumulation plus Friday validation/synthesis unless Chris explicitly asks for per-agent DMs. If he asks, send compact lane-owner DMs from the actual specialist bot/window, not Karina, and verify real Telegram message IDs before reporting success.
- Do not fabricate sources or upstream outputs. Missing inputs should be explicitly logged in `missing_inputs`.
- Do not let Faker start implementation/UI work just because a tab structure exists; tab logs are data preparation unless Chris approves UI build scope.
