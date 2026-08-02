---
name: productivity-and-document-workflows
description: "Use when operating productivity apps, documents, personal knowledge systems, maps, briefings, meeting pipelines, PDFs/OCR, presentations, email-like workspaces, Airtable, Google Workspace, Notion, and scheduled personal automation."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [productivity, documents, google-workspace, notion, airtable, pdf, ocr, powerpoint, briefings, meetings, knowledge]
    related_skills: [research-intelligence-workflows]
---

# Productivity and Document Workflows

## Overview

This umbrella covers user-facing productivity systems: office documents, knowledge bases, scheduled briefings, personal/persona calibration, map/location lookups, meeting pipelines, and SaaS workspaces such as Google Workspace, Notion, and Airtable. The common pattern is to authenticate safely, retrieve or mutate real external state, verify with a read-back, and return a durable link/path/record ID.

## When to Use

- The user asks for Google Drive/Docs/Sheets/Gmail/Calendar operations, Notion pages/databases, Airtable records, or similar productivity app work.
- The user asks to create/edit/read PowerPoint decks, PDFs, scanned documents, OCR output, or document conversions.
- The user asks for scheduled personal briefings, meeting summaries, Teams pipeline operation, daily work wikis, or Obsidian/vault updates.
- The user asks for geocoding, POIs, routes, time zones, or Telegram location-pin interpretation.
- The user asks to calibrate assistant persona/preferences in a durable but non-overfit way.

## Core Workflow

1. **Identify the system of record.** Google, Notion, Airtable, local vault, PDF/PPTX file, map API, cron job, or meeting pipeline.
2. **Check auth and prerequisites.** Do not invent tokens, IDs, or file paths; inspect config/env when needed.
3. **Perform the action with the narrowest tool.** Prefer CLI/API wrappers already configured for the workspace.
4. **Read back after writes.** Fetch the record/page/file/cron job again, or inspect generated output.
5. **Return a durable handle.** URL, document ID, file path, cron job ID, meeting ID, route summary, or extracted text path.

## Workflow Lanes

### SaaS workspaces and data apps

- Google Workspace: use gws/Google API helpers for Gmail, Calendar, Drive, Docs, and Sheets; respect OAuth setup and scopes.
- Notion: use ntn CLI or HTTP API; distinguish databases/data sources/pages and preserve property schemas.
- Airtable: handle field types carefully, paginate, use formulas for filters, and verify upserts by record ID.
- Social/email tools such as Himalaya or X/Yuanbao/OpenHue are usually separate integration lanes, but the same rule applies: act through the configured CLI/API and read back.

### Documents and presentations

- PowerPoint: inspect structure, edit XML or use helper scripts, then render/QA slides when possible.
- PDF/OCR: try remote extraction for accessible URLs, then local PyMuPDF for digital PDFs, then marker/OCR for scans.
- Nano-PDF: use for targeted text/title typo edits, not full redesigns.
- Personal profile/intro surfaces: when Chris asks to add his saved introduction/history into a deck, dashboard, portfolio, or slide-like web artifact, use the existing artifact as the system of record, add the content directly, and verify the rendered/buildable artifact rather than only drafting copy. For Chris’s current positioning, prefer `OBD: Ontology Business Designer` as the short external label and express AI context in supporting copy such as “for the AI era”; avoid expanding the acronym to `AOBD` unless Chris explicitly asks.
- Keep original files backed up before destructive edits.

### Personal knowledge, briefings, and meetings

- Scheduled personal briefings: use cron jobs with self-contained prompts; respect multi-profile delivery/ownership.
- Daily work wiki and Obsidian: write concise, dated notes with links back to sources or session references.
- Local loop/log localization: when Chris asks to Koreanize logs or future loop data, translate human-facing Markdown/TXT and JSON/JSONL values where safe, but preserve parsing-critical structure: frontmatter keys, JSON keys, enum/status values, IDs, file paths, URLs, route paths, component names, code identifiers, commands, and prompt/script strings needed for execution. See `references/korean-loop-log-localization.md` for the detailed workflow and verification checklist.
- Before broad localization, exclude protected/operational areas unless explicitly requested (skills, profiles, memories, node_modules, third-party packages), then verify UTF-8 readability, frontmatter delimiter balance, JSON/JSONL parseability, and that path-like strings were not accidentally translated.
- Persona calibration: save stable user preferences, not transient task outcomes; avoid overfitting to one chat.
- Teams meeting pipeline: inspect status, replay or summarize jobs, and remember Graph subscriptions expire quickly.

### Safe localization / Koreanization of document repositories

When the user asks to Koreanize Markdown/schema/log folders while preserving operation:

1. Inventory Markdown files first, but exclude operational/protected areas unless explicitly requested: `skills/`, `profiles/*/skills/`, `memories/`, `.git/`, `node_modules/`, and generated/vendor package docs.
2. Treat headings, labels, prose, status summaries, and human-facing explanations as safe translation targets.
3. Preserve parser-sensitive tokens exactly: YAML frontmatter keys, JSON/JSONL keys, enum/status values, code blocks, file paths, route paths, component/function/class names, IDs, URLs, and shell/Python snippets.
4. If doing broad find/replace, repair over-translation in path-like or identifier-like text immediately (e.g. keep `final/`, `pending/`, `current-home-visual-set`, `finalizer-status`, not translated variants).
5. Verify after mutation with at least: UTF-8 read of all targeted Markdown, frontmatter delimiter sanity for files starting with `---`, and a search for common accidental path/identifier translations.
6. If JSON/JSONL adjacent files are also localized, translate only human-facing values and re-parse every JSON file and every JSONL row before reporting success.

### Local loop/document localization without breaking automation

When the user asks to translate local loop folders, schemas, or operational notes into Korean (or another human language), treat it as a documentation-localization task, not a refactor:

- Localize human-facing prose first: Markdown headings/body, DM drafts, titles, rationale bullets, event summaries, guardrail descriptions, and explanatory notes.
- Preserve machine-facing identifiers unless the user explicitly asks for a schema migration: file/folder names, JSON keys, enum/status strings, IDs, routes, component names, script code, URLs, and absolute paths.
- For JSON/JSONL, translate only values that are clearly display text or notes; keep objects parse-compatible and line-delimited JSONL one object per line.
- After mutation, verify by reading back or parsing every touched JSON file and every JSONL line. Report the validation result, not just that files were written.
- If scripts may depend on English section headings or phrases, search the relevant project/loop folder for those phrases before changing them; keep a compatibility alias or preserve the phrase if needed.


### Maps and location

- Geocode, route, and timezone through OpenStreetMap/OSRM-style APIs or configured map scripts.
- Include coordinates, timestamp/source, and assumptions about travel mode.
- For chat location pins, parse the platform metadata rather than asking the user to retype coordinates when available.

## Consolidated Legacy Knowledge

- `airtable`: REST CRUD, filters, field shapes, pagination, and upserts.
- `google-workspace`: Gmail/Calendar/Drive/Docs/Sheets via gws CLI and Python bridge.
- `notion`: Notion API, ntn CLI, database/data-source changes, and markdown conversion.
- `powerpoint`: PPTX creation, reading, targeted editing, helper scripts, and QA.
- `nano-pdf`: natural-language PDF typo/title edits.
- `ocr-and-documents`: PDF/scanned document extraction with PyMuPDF/marker and arXiv handling.
- `maps`: geocoding, POIs, routes, timezones, and Telegram location pins.
- `scheduled-personal-briefings`: cron prompts, delivery routing, morning/evening/daily digest patterns.
- `teams-meeting-pipeline`: Teams meeting summary pipeline operation and Graph subscription pitfalls.
- `daily-work-wiki`: durable daily work/conversation wiki architecture.
- `obsidian`: vault read/search/write/edit patterns and wikilinks.
- `persona-calibration`: onboarding questions and stable preference memory hygiene.
- `himalaya`: terminal IMAP/SMTP operations when email work is document/productivity adjacent.

## Common Pitfalls

1. **No read-back after mutation.** External writes must be verified before reporting success.
2. **Confusing transient logs with durable memory.** Save only stable preferences; put task logs in notes/wiki/session search.
3. **Flattening documents.** PPTX/PDF/Notion blocks have structure; preserve it rather than dumping plain text unless asked.
4. **Credential leakage.** Never echo OAuth tokens/API keys; use configured tools and redact secrets.
5. **Wrong profile ownership.** Scheduled briefings and meeting pipelines may belong to specialist profiles; inspect before editing.

## Verification Checklist

- [ ] System of record and target object identified.
- [ ] Auth/prerequisites checked.
- [ ] Operation executed with configured CLI/API/file tool.
- [ ] Mutation read back or generated file inspected.
- [ ] Durable URL/path/ID and caveats returned.
