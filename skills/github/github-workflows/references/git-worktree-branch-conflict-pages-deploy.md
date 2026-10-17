# Git worktree branch conflict during Pages deploy

Use this when deploying Chris's curated webapp/Pages repo from a secondary worktree or temporary worktree.

## Problem shape

A feature branch is checked out in one worktree, while `main` is already checked out in another worktree. Running `git checkout main` from the feature worktree can fail with:

```text
fatal: 'main' is already used by worktree at '<other path>'
```

This is a normal Git worktree guard, not a repo corruption signal.

## Safe deployment pattern

1. Confirm the working tree and remote target:
   - `git rev-parse --show-toplevel`
   - `git status --short`
   - `git branch --show-current`
   - `git remote -v`
2. Run the project's validation/build checks before committing.
3. Commit on the active feature branch.
4. Push the feature branch normally:
   - `git push origin <feature-branch>`
5. If Chris approved direct deployment and the branch should fast-forward `main`, avoid checking out `main` in the same worktree. Push the feature branch ref directly to `main`:
   - `git push origin <feature-branch>:main`
6. Verify both remote refs point to the same commit:
   - `git ls-remote origin refs/heads/main refs/heads/<feature-branch>`
7. Wait for GitHub Pages to publish, then verify the live URL with an HTTP/smoke check against the deployed asset and expected content markers.

## Pitfalls

- Do not treat inability to `checkout main` as a reason to skip deployment if Chris approved and a direct refspec push is appropriate.
- Do not report Pages success from `git push` alone; wait for the live site to show the new asset/content markers.
- Do not stage broad runtime folders, `node_modules/`, or `dist/` unless the repo explicitly expects them.
