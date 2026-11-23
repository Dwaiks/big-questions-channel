# Production hand-off to directing-stickman-videos (B2)

Rendering needs a Claude Code session with the **directing-stickman-videos** skill installed, Node 20+ and FFmpeg, plus the channel's voice, image and music services configured as environment secrets. In claude.ai, stop at the scene plan and tell the author to continue in Claude Code.

## Channel defaults (do not re-ask once set)

| Setting | Value |
|---|---|
| Mode / style | B · Autopilot, B2 Colorful Hand-Drawn |
| Long video | 16:9, 8–12 min |
| Shorts | 9:16, 30–55 s, separate native projects |
| Language | English (dubbing added later in YouTube Studio) |
| Narrator | the channel voice: provider, voice ID and settings recorded in `channel-settings.json` once chosen (not yet chosen on 22 Nov 2026) |
| Music | one continuous licensed track per video, under the narration |
| Captions | B2's own single-line semantic captions |

## Steps
1. Follow directing-stickman-videos' own workflow for B2: run its `workflow --style B2 --ratio 16:9` command and read the references it names. Its quality gates and review steps apply in full; this file only supplies channel defaults.
2. Keep each video in its own project folder named `<tracker #>-<short-slug>` (e.g. `056-time-is-counting`), outside the skill directory.
3. Generate the narration once from the approved script with the channel voice. Never re-voice approved audio automatically.
4. Scene plan → illustrations. Every scene's art is drawn for this story; reuse only the channel's recurring narrator character design and palette, never whole scenes.
5. Make the 20-second preview with sound; the author approves it before the full render.
6. Render the full film, then the Shorts as separate 9:16 projects.
7. Deliver the MP4, SRT, thumbnail concepts and the publishing pack, and update the tracker status.

## Scene plan format (from the approved script)

| Scene | Narration (exact words) | What is drawn | What moves | Sound |
|---|---|---|---|---|
| 1 | "…" | … | … | … |

One scene per idea, roughly 2–4 seconds of narration each; longer holds only for reading or a reaction.
