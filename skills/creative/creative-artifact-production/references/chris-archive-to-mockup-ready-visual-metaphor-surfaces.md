# Chris Archive visual-reference to mockup-ready motif workflow

Use when Chris says generated outputs are too close to the reference images, too literal, or too much like named object metaphors, and asks for design-DNA assets that still reference Chris Archive but can be applied to future mockups.

## Correction captured

Chris corrected the workflow twice:

1. New Chris Archive items should not be used as near-copy image references. Generated candidates should not look like the poster, helix, orb, neon landscape, or phone UI that inspired them.
2. A named metaphor object such as “protective veil,” “memory strata,” or “signal garden” may still feel too concept-art-like. For mockup work, Chris often wants **visual metaphor surfaces**: graphic skins/material systems that can be applied to packages, phone backgrounds, cards, labels, or brand assets.

## Preferred approach

Use Chris Archive as hidden design DNA, not as a template:

- Extract: color tension, material mood, density, rhythm, protected/inner-energy feeling, tactile editorial surface, warm-cool intelligence.
- Do not copy: exact composition, object silhouette, poster layout, third-party text, UI screen, helix/orb/sun/phone forms.
- Avoid passing source archive images as `--image-references` when Chris explicitly asks for reinterpretation; image refs can anchor the model too literally.
- Generate as surface/material/motif families that can be cropped, masked, overlaid, repeated, or placed on a mockup.

## Prompt framing shift

Avoid:

```text
Create a motif based on this poster / helix / orb / phone reference...
```

Prefer:

```text
Create an original 1:1 mockup-ready visual metaphor surface for Design DNA. Use Chris Archive as hidden visual DNA only: tactile editorial surfaces, warm/cool intelligence, restrained signal color, protected human context, optical material mood, dense-but-calm information rhythm. Do not directly copy any Chris Archive image. No poster, no helix, no orb pair, no landscape, no phone UI, no literal metaphor object. Must be crop-friendly, mask-friendly, overlay-friendly, and repeat/placement-ready.
```

## Useful style families

When Chris asks for “다른 스타일” or says prior outputs feel repetitive, change the underlying graphic family, not just the palette:

- Low-noise editorial signal skin — paper/vellum/charcoal/coral tension for package/card surfaces.
- Chromatic compression surface — controlled warm-cool optical pressure for phone/digital hero surfaces.
- Raster fabric intelligence field — information density translated into textile/riso/raster material, not UI/data screen.
- Organic plaster color pond — broad matte color fields rather than poster cut-outs.
- Offset hinge-block geometry — flat modular slot/block structures rather than line/aperture overlays.

## QA checklist

- Does it avoid visible reference-copying? No poster, helix, orb-pair, red sun landscape, phone UI, or diagnostic screen.
- Is it mockup-ready? It should work on a package panel, card, label, phone hero background, or brand-surface crop.
- Is it not merely a standalone artwork? Prefer surface fields, repeatable skins, color/material systems, or modular graphic motifs.
- No readable text, logos, UI chrome, product mockups, people, or fake interface details.
- If Chris says 1/2 feel like old directions, regenerate only those numbers with a different graphic family, and save already-approved numbers first if requested.

## Save-gated handling

Unselected candidates remain temporary. If Chris says `3,4번 저장해줘`, publish only those selected candidates to Design DNA → DNA Dashboard, then separately regenerate rejected numbers if he asked for revisions. Do not publish the revision set until Chris explicitly selects it.