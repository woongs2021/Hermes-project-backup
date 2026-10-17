---
name: smart-home-device-automation
description: "Use when controlling smart-home devices and scenes from Hermes, especially lights, rooms, zones, schedules, and CLI-backed home automation workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [smart-home, lights, scenes, rooms, hue, iot, automation, cli]
---

# Smart Home Device Automation

Use this umbrella when the user asks Hermes to control or schedule smart-home devices: lights, rooms, zones, scenes, brightness, color temperature, colors, bedtime/wake routines, or similar local-network home automation tasks.

## Operating principles

1. **Discover before acting.** List available devices/rooms/scenes before assuming names. Smart-home names are often case-sensitive and user-specific.
2. **Prefer scoped changes.** Target the named room, zone, scene, or device; do not apply whole-home changes unless the user explicitly asks.
3. **Verify tool availability.** Check that the required CLI or integration is installed and configured before issuing control commands.
4. **Respect physical prerequisites.** Bridges/hubs often require same-network access and first-run pairing or authorization.
5. **Use scheduled jobs for routines.** For recurring lighting changes such as bedtime dimming or morning wake-up, create a cron job with a self-contained prompt or script.
6. **Report real command outcomes.** When issuing device-control commands, summarize the actual command result and any errors; do not infer success without output or follow-up state checks.

## Philips Hue via OpenHue CLI

OpenHue controls Philips Hue lights and scenes via a Hue Bridge from the terminal.

### Prerequisites

```bash
# Linux pre-built binary
curl -sL https://github.com/openhue/openhue-cli/releases/latest/download/openhue-linux-amd64 -o ~/.local/bin/openhue && chmod +x ~/.local/bin/openhue

# macOS
brew install openhue/cli/openhue-cli
```

First run requires pressing the button on the Hue Bridge to pair. The bridge must be on the same local network as the Hermes machine.

### Discovery

```bash
openhue get light       # List all lights
openhue get room        # List all rooms
openhue get scene       # List all scenes
```

### Control lights

```bash
# Turn on/off
openhue set light "Bedroom Lamp" --on
openhue set light "Bedroom Lamp" --off

# Brightness (0-100)
openhue set light "Bedroom Lamp" --on --brightness 50

# Color temperature: warm to cool, 153-500 mirek
openhue set light "Bedroom Lamp" --on --temperature 300

# Color by name or hex
openhue set light "Bedroom Lamp" --on --color red
openhue set light "Bedroom Lamp" --on --rgb "#FF5500"
```

### Control rooms and scenes

```bash
# Turn off or dim an entire room
openhue set room "Bedroom" --off
openhue set room "Bedroom" --on --brightness 30

# Activate scenes
openhue set scene "Relax" --room "Bedroom"
openhue set scene "Concentrate" --room "Office"
```

### Common presets

```bash
# Bedtime: dim warm light
openhue set room "Bedroom" --on --brightness 20 --temperature 450

# Work mode: bright cool light
openhue set room "Office" --on --brightness 100 --temperature 250

# Movie mode: dim living-room light
openhue set room "Living Room" --on --brightness 10

# Everything off: only run when user requested all named areas
openhue set room "Bedroom" --off
openhue set room "Office" --off
openhue set room "Living Room" --off
```

### OpenHue pitfalls

- Light, room, and scene names are case-sensitive; run `openhue get light`, `openhue get room`, or `openhue get scene` to confirm exact names.
- Colors only work on color-capable bulbs; white-only bulbs can still use brightness and color temperature.
- If pairing fails, confirm the Hue Bridge is on the same LAN and that the physical bridge button was pressed during authorization.
- For recurring schedules, prefer Hermes cron jobs over ad-hoc shell loops so state, delivery, and failures are tracked.
