# Agent-team profile image asset handoff

Use this reference when Chris shares agent/profile images for a future homepage, dashboard, or team-introduction page.

## Workflow

1. Treat uploaded portraits as durable product assets, not just chat images.
2. Normalize filenames by role/name before handoff to implementation, e.g.:
   - `karina_profile.jpg`
   - `yuna_profile.jpg`
   - `goyounjung_profile.jpg`
   - `son_profile.jpg`
   - `faker_profile.jpg`
   - `muyeol_profile.jpg`
3. Store them under a clear product asset path such as `/opt/data/agent-team-assets/profile-images/`.
4. Create a `MANIFEST.md` in the asset folder with:
   - file mapping
   - visual description
   - intended usage
   - any user corrections to identity/role mapping
   - implementation notes for the future builder agent
5. If the user corrects which image belongs to which agent, update the normalized filename mapping immediately and call out the correction in the manifest.
6. For homepage/team pages, recommend circular or rounded-square portraits and keep the design restrained, premium, and non-generic.

## Current known mapping from this session

- `karina_profile.jpg` — blue background, light blue shirt.
- `yuna_profile.jpg` — pink background, light pink tweed jacket.
- `goyounjung_profile.jpg` — mauve background, burgundy blazer.
- `son_profile.jpg` — mint background, mint blazer.
- `faker_profile.jpg` — dark blue background, dark technical jacket, finger-to-lips gesture.
- `muyeol_profile.jpg` — terracotta/rust background, rust blazer and knit. Chris corrected that this is the right Muyeol image.

## Pitfalls

- Do not leave assets only in ephemeral Telegram cache names.
- Do not assume role mapping if the user corrects a filename or identity; the corrected mapping wins.
- Do not embed private platform identifiers or tokens in manifests or work logs.
