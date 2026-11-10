# Git history rewrite with independent Release archive

Use when large historical blobs must be removed from a GitHub repository but the pre-rewrite history must remain recoverable.

## Why a same-repo backup branch is insufficient
A branch inside the repository keeps every object reachable. If it still points to the old history, GitHub cannot reclaim the large blobs. Before rewriting, move the complete history to an **independent** location (for Chris: a Release in `Hermes-project-backup`), then rewrite or repoint all source-repository refs that reach those blobs.

## Verified flow
1. Create `git bundle create <archive>.bundle --all` from the source repository and run `git -C <repo> bundle verify <archive>.bundle`.
2. Hash it with SHA-256. If it exceeds GitHub Release per-asset limits, split into numbered parts below the limit and upload all parts plus the checksum to a Release in the backup repo. Verify every asset has the expected byte size and `uploaded` state; a Release asset in `starter` state is incomplete and must be deleted then re-uploaded.
3. Use an isolated no-hardlink mirror for the rewrite. Fetch every remote head that may retain the blobs; inspect all refs, not only `main`.
4. Generate an exact NUL-delimited path allowlist from the migration inventory and run a history rewrite that removes only those paths. Validate every inventory path has zero occurrences in retained refs. Remove rewrite-created `refs/original/*`, expire reflogs, run `git gc --prune=now`, then `git fsck`.
5. Compare local rewritten heads with remote heads. Force-push **every rewritten branch/ref that can retain the target blobs**, not just `main`. An explicit user confirmation is required immediately before the force-push.
6. Refresh a clean working clone to the rewritten `main`, run normal build/data checks, verify remote refs, and then verify the deployed site.

## Guardrails
- A GitHub repository’s displayed size can lag after rewriting while GitHub garbage-collects unreachable objects.
- Do not claim the archive is complete from a release asset’s presence alone: check all parts, exact byte sizes, and state `uploaded`.
- Do not overwrite a user’s working tree; perform rewrite in a disposable mirror.
