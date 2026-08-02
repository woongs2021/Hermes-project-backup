# Team Asset Handoff and Manifest Pattern

Use when Chris shares or renames profile images, homepage assets, agent portraits, logos, or other files that later need to be handed to Faker/Go Youn-jung.

## Pattern

1. Treat user-edited filenames as the source of truth.
   - If Chris says they renamed files manually, re-list/re-audit the target folder before updating manifests or memories.
   - Do not rely on earlier cache filenames or a previous inferred mapping.
2. Normalize the handoff location.
   - Prefer a stable folder such as `/opt/data/agent-team-assets/<asset-class>/`.
   - Keep product-facing filenames stable and readable.
3. Write or update a `MANIFEST.md` in the asset folder.
   - Include final filenames, intended owner/use, brief visual/semantic notes, size/format if verified, and any user correction such as role-to-image mapping.
   - Avoid raw Telegram/Slack cache IDs unless needed as private provenance; product code should use normalized names.
4. Log substantive asset handoff work in Karina's daily team work log.
5. If the asset set is likely to be used in future implementation, save only a compact durable pointer in memory or an existing project handoff note; avoid storing large file inventories in memory.

## Verification

- Confirm every expected final file exists.
- Confirm format/dimensions when the downstream use needs it.
- Read back the manifest or use a targeted check before telling Chris it is updated.

## Current Chris pattern

For the agent-team homepage, profile images are stored under `/opt/data/agent-team-assets/profile-images/` with a `MANIFEST.md`. Chris may manually rename files in that folder; always re-check the folder before handing it to Faker.
