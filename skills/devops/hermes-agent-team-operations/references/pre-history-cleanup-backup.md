# Pre-history-cleanup backup pattern

Use this pattern before rewriting or pruning Git history for a Hermes-backed project.

## Two independent recovery anchors

1. **Curated Hermes system snapshot** in the designated backup repository on a new timestamped branch.
   - Include: active agents' `SOUL.md`, curated skills and workflows, reusable plans, concise Markdown work memory, and restore-scope documentation.
   - Exclude: `.env`, provider/OAuth/API credentials, auth stores, session databases/transcripts, raw channel IDs, gateway logs, caches, runtime state, and cron output history.
   - Run the repository safety scanner before commit and after pushing; verify the remote branch SHA and required soul/restore files.

2. **Reachability-preserving source branches** in every repository whose history may be rewritten.
   - Push the current `HEAD` to a clear branch such as `backup/pre-history-cleanup-YYYYMMDD` before any rewrite.
   - A branch at the pre-rewrite tip retains all commits/blobs reachable from that tip, which a curated backup repo cannot reproduce without impractically large Git bundles.
   - Verify each remote ref with `git ls-remote --heads` before cleanup begins.

## Commit discipline

- Work on a new backup branch; never overwrite the backup repo's default branch.
- Document source remotes, branches, and commit IDs in an anchor file stored with the snapshot.
- If Git identity is absent in an ephemeral clone, set a repository-local bot identity only; do not change global Git configuration.
- `git diff --check` can report pre-existing Markdown trailing-space formatting. Preserve intentional Markdown line breaks in archival snapshots, but still treat safety scans and forbidden-path checks as hard gates.

## Post-backup go/no-go

Proceed with history cleanup only when all of these are true: curated snapshot branch is pushed, secret scan is clean, required restoration files are present at its pushed commit, and every rewrite-target source repo has a remotely verified preservation branch.
