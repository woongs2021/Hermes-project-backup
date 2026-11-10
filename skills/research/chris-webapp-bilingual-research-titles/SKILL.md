---
name: chris-webapp-bilingual-research-titles
description: "Maintain Chris's Hermes webapp research board with an English original title and Korean title for every public research record."
version: 1.0.0
author: Karina
license: MIT
metadata:
  hermes:
    tags: [chris, webapp, research-board, bilingual, korean, titles]
    related_skills: [research-intelligence-workflows, software-debugging-and-quality]
---

# Chris Webapp Research: Bilingual-title contract

## Use when

Use for any discovery, migration, correction, scheduled-loop, manifest, or UI change that creates or updates a public Yuna / Go Youn-jung research item in Chris's Hermes webapp.

## Non-negotiable display contract

Every public research item, including daily candidates and Friday validated picks, must show two separate title lines:

1. **English original title** — `title_en` in canonical JSONL and `title` in the public manifest.
2. **Korean title** — `title_ko` in canonical JSONL and `titleKo` in the public manifest.

Do not limit Korean titles to selected or validated items. Do not merge the two languages into a slash-separated single line. Render Korean as a visually quieter second line in cards, lists, marquees, and detail headers.

## Source and publishing flow

1. Update the canonical source: `/opt/data/agent-team-work-log/paper-candidates/all-research-items.jsonl`.
2. Preserve an authoritative official Korean title when available; otherwise add a conservative Korean translation that adds no claims beyond the original title.
3. Keep stable selection and matching keyed to the original English title / existing stable ID. Never use a display translation as a matching key.
4. Regenerate the public manifest in `/opt/data/projects/Hermes-project-webapp/august-dashboard/` with `npm run generate:research-board`.
5. Ensure the public output at `public/data/research-board.json` supplies non-empty `title` and `titleKo` for every eligible item.

## Legacy-data cleanup

- Preserve existing authoritative bilingual values before translating anything.
- Split legacy mixed `Korean / English` strings into their dedicated fields.
- Remove trailing metadata labels that are not title text (for example `원문보기`, `KCI`, or `인용`).
- Before bulk changes, create a reviewable backup/cache. Do not overwrite original source wording.

## UI and validation requirements

- Render both title fields in lane cards, More/modal listings, detail headers, and validated/featured treatments.
- The schema, TypeScript type, adapter, and manifest validator must reject missing `titleKo`.
- Keep records using `agent` as well as `lane` / `owner` eligible for normalization; Go Youn-jung records may otherwise be dropped.

## Release verification

Run, as applicable:

```bash
npm run generate:research-board
npm run validate:data
npm run lint
npm run build:public
git diff --check
```

After deployment, fetch the live Pages manifest with a cache-busting query and prove:

- public item count is as expected;
- every item has a non-empty English `title`;
- every item has a non-empty Korean `titleKo`.

If browser QA is available, also confirm paired titles appear in the rendered user-facing card and detail flow. Do not call a deployment visually verified if only manifest/bundle readback was possible.

## Report format

Tell Chris only the practical outcome: total updated records, bilingual coverage, what validation passed, and whether live UI was browser-verified or content/deployment-verified. Never expose private source paths, raw logs, credentials, or internal prompts.
