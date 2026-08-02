---
name: media-content-production
description: "Use when searching or producing lightweight media assets and transformations: YouTube transcript content, GIF search, audio feature visualizations, and AI song/music workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [media, youtube, gifs, audio, music, transcripts, spectrograms]
    related_skills: []
---

# Media Content Production

## Overview

This umbrella covers lightweight media retrieval, transformation, and content workflows. Use dedicated tools for raw extraction/search, then convert outputs into the user's requested artifact: summary, thread, blog post, GIF file, spectrogram, feature report, lyrics, or music-generation prompt.

## When to Use

- The user asks for YouTube transcripts, summaries, threads, or blog-style repurposing.
- The user asks to search for or download GIFs.
- The user asks for audio spectrograms or audio feature analysis.
- The user asks for songwriting help or Suno/HeartMuLa-style music prompts.

## YouTube Content

- Fetch transcripts before summarizing; do not infer video content from the title alone.
- Preserve timestamps when the user needs quotes, clips, or evidence.
- Use the transcript fetch script under `scripts/youtube-content-fetch_transcript.py` when available.
- Choose output format deliberately: concise summary, outline, tweet/thread, blog post, or action list.

## GIF Search

- Search/download via the Tenor-oriented CLI/curl workflow when configured.
- Return a usable URL or local file path and include the query used.
- For reaction GIFs, bias toward safe, broadly recognizable results unless the user requests a specific style.

## Audio Features and Spectrograms

- Use Songsee-style CLI workflows for mel spectrograms, chroma, MFCCs, and other feature visualizations.
- Report file paths for generated images/data and note the audio segment analyzed.
- Do not overinterpret features as subjective musical judgments without evidence.

## Songwriting and AI Music

- Separate craft work (lyrics, structure, rhyme, hook, emotional arc) from model prompt formatting.
- For Suno/HeartMuLa-like tools, provide tags, style descriptors, structure markers, and clean lyrics.
- Keep generated prompts concise enough for the target service.

## Common Pitfalls

1. **Summarizing without extraction.** Fetch the transcript or media-derived data first.
2. **No durable handle.** Media tasks should end with a URL/path/file, not just a description.
3. **Copyright-sensitive requests.** Avoid reproducing long copyrighted lyrics or transcripts beyond allowed excerpts.
4. **Overbroad style prompts.** Music prompts work better with a few concrete genre, tempo, mood, and instrumentation tags.

## Verification Checklist

- [ ] Source URL/file/query captured.
- [ ] Extraction/search/generation tool actually ran.
- [ ] Output path, URL, or transformed text delivered.
- [ ] Limitations and uncertain interpretations labeled.
