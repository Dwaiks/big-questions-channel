# Big Questions channel

Production repository for a faceless YouTube channel. Use the `big-questions-channel` skill in `.claude/skills/` for every channel task; it hands rendering off to the `directing-stickman-videos` skill (style B2), which is installed per session (not stored here).

- `channel-settings.json`: fixed channel voice (ElevenLabs Jon, speed 0.95) and production defaults. Do not change the voice without the author's approval.
- `episodes/<NNN-slug>/`: one folder per episode. `narration/text/` holds the approved narration per scene; `narration/audio/` the recordings; `art/upload/` the author's Flow images.
- Scripts are written and approved in Claude Docs (links in each episode's README); the text files here are the approved snapshot used for recording.
- The ElevenLabs key lives in the cloud environment's network secrets; never commit keys.
- Commit and push only when the author asks.
