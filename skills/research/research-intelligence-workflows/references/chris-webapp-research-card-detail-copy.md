# Chris webapp research-card detail copy

Use when updating Hermes Project Webapp Research board cards for Chris, especially `friday_final_pick`, `GO`, `WATCH`, or other major/validated papers.

## Preferred card copy shape

Chris wants research details to reveal what the paper is actually about, not only why it matters. For each major paper:

- `summary`: evidence-first, abstract/metadata-based.
  - Start with the paper's problem/gap.
  - Mention method, sample, dataset, benchmark, review size, framework, or study context when available.
  - Include the core construct/findings in concrete terms.
  - Avoid generic “important for AI UX” phrasing unless the abstract supports it.
- `chrisRelevance`: interpretation-first for Chris.
  - Translate the evidence into AX / OBD / design-leadership / design-education implications.
  - Say what this helps Chris judge, teach, evaluate, or design.
  - Include caution when the study should not be overgeneralized.

## Source order

1. Prefer DOI/arXiv/official publisher metadata and abstract.
2. If full abstract is unavailable, use public metadata plus existing Muyeol/Yuna/GoYJ validation notes.
3. Label conclusions conservatively: do not imply full-paper review when only abstract/metadata was used.

## Webapp workflow

1. Update the source JSONL when the source record exists outside the webapp repo.
2. Regenerate `public/data/research-board.json` via the existing generator.
3. If validated items are missing, check adapter filters for `lane`, `owner`, and `agent`; GoYJ records may use `agent: goyounjung`.
4. Verify counts and representative card text before deploy.
5. Run `validate:data`, lint, build, deploy, and live JSON/DOM checks.

## Pitfalls

- Do not only write a relevance blurb; Chris explicitly asked for abstract-style detail so the content can be understood.
- Do not overclaim if only Crossref container/date metadata is available.
- Do not let `agent`-only records drop from public output when the adapter filters only `lane ?? owner`.
