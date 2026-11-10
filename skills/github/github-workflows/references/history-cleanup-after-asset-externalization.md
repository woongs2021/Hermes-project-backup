# History cleanup after asset externalization

Use this only after high-resolution originals have been moved to a Release and the app has stable local previews plus verified external download URLs.

## Preflight the full repository, not only the migrated batch

1. Enumerate the intended migrated paths from manifests and verify each has a local preview and an external download URL returning HTTP 200.
2. Inspect **all reachable refs** for remaining large blobs before planning a rewrite. A targeted batch can be clean while another active collection still keeps multi-gigabyte 4K originals reachable.
3. Include every remote branch, tags, backup branches, worktree refs, and local preservation refs in this review. A same-repository “pre-cleanup backup branch” prevents Git object reclamation unless it is itself rewritten or removed.
4. Do not delete local originals or rewrite history as part of the first Release migration. Treat current-tree deletion and history rewriting as separately approved operations.

## Independent history preservation

If preserving complete Git history is required before a rewrite, make an independently recoverable archive first:

- Create and verify a complete `git bundle` from all intended pre-cleanup refs.
- If it exceeds a single Release-asset limit, split it into deterministic numbered parts and publish a checksum manifest.
- Verify every uploaded part is in the Release API’s `uploaded` state (not an incomplete/starter state) and that the bundle verifies locally before changing source refs.
- Record reconstruction instructions: concatenate parts in numeric order, validate the checksum, then run `git bundle verify`.

## Rewrite and publication checkpoints

1. Rewrite a disposable mirror, never the only working clone.
2. Remove only manifest-derived paths, then prove no target path remains in any retained ref; run `git fsck`.
3. Run garbage collection in the disposable mirror and measure the resulting pack size. This is the realistic minimum publication payload; do not infer it only from deleted-file byte totals.
4. Before force-pushing, compare the remaining large blobs and current-tree archive size with the desired hosting limit. If active originals remain, externalize them first rather than replacing history blindly.
5. Force-push only after explicit approval. Verify every rewritten remote branch, not just `main`, because a stale branch retains old blobs.
6. If the hosting service rejects the rewritten pack, stop retrying the same force-push. Reassess retained blobs/ref scope and choose a smaller, separately approved publication strategy. Never substitute an orphan/root-history replacement without explicit approval because it changes the public commit-history contract.

## Completion evidence

- External Release assets: names, byte sizes, state, and URLs verified.
- Webapp: data validation, lint, production build, and live Pages manifest/preview/download smoke all pass.
- Git: remote ref SHAs confirm publication; GitHub-side physical storage reclamation may occur asynchronously after unreachable objects are pruned.
