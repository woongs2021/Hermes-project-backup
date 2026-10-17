# GoYJ Slack handoff to Design DNA webapp publication

Use when Chris says Go Youn-jung sent/saved additional Design DNA assets through Slack or a specialist DM and asks Karina to reflect them in the webapp.

## Core lesson

A Slack message ID alone is not enough proof that Karina/default can access the assets. The message may exist in Slack while the actual image files/paths are not present in Karina's local session DB, GoYJ daily log, selected manifest, or public asset tree. Do not claim publication until the actual image binaries or stable `MEDIA:/...`/filesystem paths are available and verified.

## Intake workflow

1. Resolve the handoff source:
   - Search current/default sessions for the Slack message ID and keywords.
   - Check GoYJ daily log under `/opt/data/agent-team-work-log/goyounjung/daily/`.
   - Check `/opt/data/dna-archive/candidates/YYYY-MM-DD/`, `/opt/data/dna-archive/selected/YYYY-MM-DD/`, and the webapp public asset folder.
   - Check GoYJ profile sessions/logs only for non-secret public paths or `MEDIA:` handles; never expose raw tokens or private IDs.
2. If only a Slack message ID is found and no paths/images are accessible, tell Chris plainly that the handoff is not materialized in Karina/default storage yet. Ask for the three images, `MEDIA:` handles, or for GoYJ to save/copy them into the selected DNA archive path.
3. Once files are accessible:
   - Copy only Chris/GoYJ-selected items into `/opt/data/dna-archive/selected/YYYY-MM-DD/images/` and the webapp `public/assets/dna-archive/YYYY-MM-DD/`.
   - Append `public/data/dna-archive.json` with unique IDs, `chris_selected` status, public-safe title/analysis, dimensions, SHA-256 `assetHash`, and `midjourneyPrompt` where applicable.
   - Preserve source candidate paths in local selected manifest; keep provider logs/raw credentials out of public assets.
4. Verify beyond manifest:
   - `npm run build:public`.
   - Live `dna-archive.json` count and exact new IDs.
   - Direct image URLs return `200 image/*`, expected dimensions, hash match.
   - Browser/Playwright navigation to `Corporate AX → Design DNA → DNA Dashboard` shows the tiles; report exact item numbers/navigation because new assets may appear lower in the grid.

## Reporting pattern

- If accessible and published: report count, item numbers/titles, commit, live URL, exact navigation, and direct URL/hash verification.
- If not accessible: say which stores were checked and what is missing. Do not imply Slack attachments were published if the image files never reached the archive/webapp filesystem.
