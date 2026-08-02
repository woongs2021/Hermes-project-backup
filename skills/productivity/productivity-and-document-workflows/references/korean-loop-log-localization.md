# Korean loop/log localization

Use this when Chris asks to Koreanize existing loop folders, schemas, Markdown logs, or future saved loop data while preserving operational stability.

## Safe localization scope

Translate human-facing content first:

- Markdown headings and prose
- TXT message drafts
- Schema explanations and field descriptions
- JSON/JSONL values meant for humans, such as titles, summaries, rationales, themes, notes, guardrails, and questions

Preserve parsing/execution-critical strings:

- YAML frontmatter keys
- JSON keys and schema field names
- enum/status values if any job or parser may match them
- IDs, timestamps, paths, URLs, route paths, component names, command names, code identifiers
- Python/shell scripts and prompt snippets required by an executor

## Recommended workflow

1. Inventory candidate files with `search_files(target="files")`; avoid broad edits in `skills/`, `profiles/`, `memories/`, `node_modules/`, `.git/`, and third-party packages unless Chris explicitly asks.
2. For Markdown, translate headings/labels/prose outside code fences and frontmatter. Keep links, paths, and inline code stable.
3. For JSON/JSONL, parse first and only translate selected human-facing values. Re-serialize with `ensure_ascii=False`; for JSONL keep one valid object per line.
4. For future cron loops, add a compact instruction to the prompt: “저장 로그는 가능한 한 한국어로, 단 keys/paths/IDs/status/code는 보존.”
5. Verify after edits:
   - all targeted Markdown files read as UTF-8
   - frontmatter delimiter balance is intact
   - JSON/JSONL parses successfully
   - no path-like strings were accidentally translated, e.g. `/final/`, `/pending/`, `current-home-visual-set`, `finalizer-status`

## Pitfalls

- Do not translate directory names inside path strings just because they are English words.
- Do not translate enum-like values if a downstream parser could compare them literally.
- Do not edit bundled/hub skills for this preference; update local umbrella skills or prompt rules instead.
- Avoid a one-size-fits-all regex pass over all of `/opt/data`; first exclude operational and third-party areas, then repair any path-like over-translation before reporting success.
