# Paper 후보s Logging Contract

목적:local research log for Chris's daily 3+3 paper discovery, Friday best-3 selection, monthly synthesis, and future Faker 대시보드/search UI.

## Files

- `yuna-YYYY-WW.md`: weekly Yuna lane 후보s. Daily Yuna job appends/merges exactly 3 selected AI/AI×design 후보s per day.
- `goyounjung-YYYY-WW.md`: weekly Go Youn-jung lane 후보s. Daily Go Youn-jung job appends/merges exactly 3 selected UX/HCI/design/brand 후보s per day.
- `all-research-items.jsonl`: append-friendly local index of daily 3+3 후보 items for future 대시보드 search. Each line should be one compact JSON object.
- `friday-shortlist-YYYY-WW.md`: Karina's Friday provisional best-3 shortlist plus reserves for Muyeol.
- `weekly-selected-papers.md`: 기준 소스 for Muyeol-finalized Friday best-3 selections and monthly synthesis hooks.

## JSONL fields for `all-research-items.jsonl`

Recommended compact object:

```json
{
  "date_kst": "YYYY-MM-DD",
  "iso_week": "YYYY-WW",
  "lane": "yuna|goyounjung",
  "title": "paper title",
  "url_or_id": "https://... or DOI/arXiv/ACM ID",
  "source_venue": "venue/source",
  "publication_date": "YYYY-MM-DD or source date",
  "core_claim": "one-line evidence claim",
  "chris_relevance": "short note",
  "korean_source_status": "yes|no|unclear + note",
  "source_access": "full|abstract|metadata|snippet|paywalled|unclear",
  "initial_score_5": 0,
  "duplicate_key": "normalized title/doi/url key",
  "duplicate_repeat_signal": "new|repeat|merged + note",
  "owner": "yuna|goyounjung"
}
```

## 규칙

- Keep daily Slack output capped at 3 items per lane, but log those selected daily 후보s locally.
- Preserve direct source URLs/DOIs/IDs so future cards can open the original source.
- 저장하지 않는다 비밀값, private IDs, raw chat logs, or 자격 증명.
- De-duplicate visible outputs; in logs, repeated appearances may be recorded as repeat/confidence signals.
- Friday report shows exactly 3 최종 items total, finalized by Muyeol, and appends them to `weekly-selected-papers.md`.
