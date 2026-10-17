# Webapp research board weekly-pick update pattern

Use when Chris asks to update the Hermes webapp with Muyeol's weekly 1-pick, new Yuna/GoYJ papers, or clearer research-card descriptions.

## Source and manifest flow

- Source of truth for research items is usually `/opt/data/agent-team-work-log/paper-candidates/all-research-items.jsonl`.
- The public webapp manifest is `august-dashboard/public/data/research-board.json`.
- Regenerate it from the webapp repo with `npm run generate:research-board`, then validate with `npm run validate:data`.
- The source JSONL lives outside the webapp git repo; only commit the regenerated public manifest and any adapter/source-code changes in the webapp repo.

## Weekly 1-pick handling

- Verify Muyeol's 1-pick by DOI/title/status in the live/public manifest; do not infer solely from nearby newly-added candidates.
- The weekly 1-pick should carry `status: friday_final_pick` and `validationStatus: GO` when Muyeol marked it GO.
- Other newly-added papers in the same week are candidates, not the 1-pick; be explicit in the user-facing summary to avoid confusion.

## GoYJ/Yuna source normalization pitfall

- Some new GoYJ records may use `agent: goyounjung` rather than `lane` or `owner`.
- The research-board adapter/filter must treat `record.lane ?? record.owner ?? record.agent` as the lane candidate before normalization.
- If public item count is lower than JSONL source count, inspect recent JSONL keys; missing `lane/owner` with present `agent` is a common cause.

## Abstract-based description enrichment

When Chris asks to make a card's detailed description more understandable:

1. Fetch authoritative metadata/abstract from the DOI source when available (Crossref often works for DOI metadata).
2. Rewrite `core_claim` as a concise abstract summary: problem/gap, method, sample/evidence, key construct/factors, and result.
3. Rewrite `chris_relevance` as the practical AX/OBD/design-leadership implication, without overclaiming.
4. Regenerate `public/data/research-board.json` and verify the target item text includes the new abstract-derived details.

Example for an AI-literacy scale paper:

- Good summary: explains the gap, expert-informed item pool, EFA/CFA sample sizes, and final 23-item/five-factor scale.
- Good relevance: frames designer AI capability beyond prompt skill, including ethics, originality, design value judgment, and output evaluation.
- Avoid: claiming the scale proves real-world job performance, is a hiring KPI, or applies directly to all professional designers without caution.

## Verification checklist

- `npm run generate:research-board`
- `npm run validate:data`
- `npm run lint`
- `npm run build:public`
- `git diff --check`
- Local or live fetch confirms:
  - total research item count
  - the weekly 1-pick title/DOI/status/validationStatus
  - new Yuna/GoYJ candidate counts for the target date
  - updated summary/relevance strings
- After push, prove Pages served the new JSON by fetching `data/research-board.json?v=<commit>` and searching for the exact new text. Browser QA should also report console/page errors and horizontal overflow when practical.
