---
name: apple-ecosystem-automation
description: "Use when controlling Apple ecosystem apps and devices from Hermes: Notes, Reminders, iMessage/SMS, Find My, and general macOS UI automation."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [apple, macos, automation, notes, reminders, imessage, findmy, computer-use]
    related_skills: []
---

# Apple Ecosystem Automation

## Overview

This umbrella covers class-level workflows for operating Apple services and macOS apps from Hermes. Prefer direct CLIs for structured data, and use macOS UI automation only when the app has no reliable CLI/API path.

## When to Use

- The user asks to create, search, or update Apple Notes.
- The user asks to add, list, or complete Apple Reminders.
- The user asks to send/read iMessage or SMS from a Mac.
- The user asks to locate AirTags, Apple devices, or people through Find My.
- The user asks to interact with arbitrary macOS apps using screenshots, clicks, typing, scrolling, drag/drop, or focus management.

## Tool Ladder

1. **Structured CLI first**: use the narrow CLI built for the app (`memo`, `remindctl`, `imsg`) when installed and authorized.
2. **AppleScript / Shortcuts second**: use when the app exposes stable scripting hooks.
3. **Screenshot-driven UI automation last**: use for Find My or arbitrary GUI work where no direct API is available.

## Notes

- Use `memo` for Apple Notes create/search/edit flows.
- Confirm the target account/folder when ambiguity could create notes in the wrong place.
- For edits, read the existing note first; avoid blind replacement of user-authored content.

## Reminders

- Use `remindctl` for add/list/complete operations.
- Preserve natural-language dates when supported, but verify the parsed due date if the wording is ambiguous.
- List current reminders before marking items complete unless the user supplied an exact identifier.

## iMessage and SMS

- Use `imsg` for sending and receiving messages on macOS.
- Confirm recipient identity when the contact name is ambiguous or multiple phone/email handles exist.
- Treat message sending as an external side effect: send only the text requested, then report delivery/tool output.

## Find My

- Prefer screenshot-based Find My inspection for current locations because Apple does not expose a stable public CLI.
- Capture evidence and report uncertainty: location labels, timestamps, and whether the device appears stale/offline.
- For tracking over time, take repeated snapshots and compare timestamps rather than pretending the position is live.

## macOS Computer Use

- Start by capturing the screen and identifying the focused app/window.
- Use explicit coordinates only after visual inspection; re-screenshot after meaningful UI changes.
- For text input, prefer paste/clipboard-safe methods over simulated key-by-key typing when possible.
- Do not assume background windows accept input; bring the target window forward and verify focus.

## Common Pitfalls

1. **Using GUI automation when a CLI exists.** CLIs are more reliable and easier to verify.
2. **Not verifying macOS permissions.** Automation, screen recording, contacts, messages, and reminders may all require OS-level grants.
3. **Ambiguous contacts or lists.** Ask or inspect before sending messages or completing reminders.
4. **Stale Find My data.** Always report the displayed timestamp or offline/stale status.

## Verification Checklist

- [ ] Correct Apple service/app selected.
- [ ] Required CLI or macOS permission verified.
- [ ] Read/list/screenshot evidence collected before destructive actions.
- [ ] External side effects reported with real command/tool output.
