# Evidence-first research card enrichment

Use this when upgrading a research board from headline-level cards to useful detail cards.

## Card contract

- `summary`: explain **research gap → method/data/sample → core finding or framework**. Prefer concrete study facts only when present in an official abstract, publisher page, DOI metadata, or validated source record.
- `chrisRelevance`: interpret the finding for AX, OBD, One UI, design leadership, education, research practice, or governance. Keep interpretation distinct from study evidence.
- Include scope limits when they materially affect interpretation (e.g., student sample, exploratory workshop, one domain, qualitative study).

## Evidence order

1. Publisher/DOI landing page and official abstract/full text.
2. Crossref metadata for title, venue, DOI, dates, and abstract when present.
3. Canonical repository record (ACL Anthology, arXiv, conference library).
4. Existing validated source record and Muyeol review notes.

Never invent sample sizes, effect sizes, methods, or claims to make cards richer. If the abstract is unavailable, write a clearly bounded description from the verified title/venue/validation record rather than implying a full-paper reading.

## Update workflow

1. Identify the exact inclusion set (`friday_final_pick` and/or validated `GO`/`WATCH`/`HOLD`) and deduplicate only if the product explicitly wants one card per paper; otherwise preserve each dated card while keeping its explanation consistent.
2. Enrich source records first so generated public JSON remains reproducible.
3. Regenerate the public manifest; do not hand-edit generated output as the sole source of truth.
4. Verify every selected card has substantive evidence and relevance text, then run schema validation, lint, production build, and live JSON/DOM checks.
5. Report the selected-card count separately from the total board count, so “weekly 1-pick” is never confused with broader candidate updates.
