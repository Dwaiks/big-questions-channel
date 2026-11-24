# Production hand-off

The channel's production route (since 24 Nov 2026) is **silent Google Flow video clips, assembled to one continuous narration**. The author generates the clips in Flow by hand; Claude writes the prompts, records the narration, and assembles everything with `tools/assemble_clips.py`. The earlier B2 illustrated route (directing-stickman-videos) is archived in `episodes/001-god-behind-or-ahead/archive/b2-trial/` and is only a fallback.

## Channel defaults (do not re-ask once set)

| Setting | Value |
|---|---|
| Long video | 16:9, 1920×1080, 24 fps (Flow's native rate; never convert to 30) |
| Look | Rich illustrated 2D cartoon, expressive faces, detailed lit settings; characters drawn inside the scene |
| Cast | Narrator (round ivory head, big expressive eyes; clothes may change) and the blonde girl; reference images uploaded by the author |
| Narrator voice | ElevenLabs Jon, settings in `channel-settings.json` |
| Music | One continuous licensed track per video (YouTube Audio Library); credit if marked CC |
| Captions | Phrase-by-phrase, burned in, light label |
| Loudness | About -14 LUFS |

## Steps for one episode

1. **Narration first.** Record the approved script per scene with the channel voice, trim end clicks (`tools/clean_narration_tails.py`), and get word timings (ElevenLabs forced alignment).
2. **Shot list from the word timings.** Cut the narration into slots at natural pauses. **Each slot must be at most the Flow clip length (default 8 s)**; split longer passages into two shots.
3. **Flow prompts.** One prompt per shot (see the rules below), plus the reference images to attach.
4. **Author generates** clips in Flow (8 s, 16:9, 720p) and uploads them to `episodes/<ep>/clips/upload/`. File names don't matter: Claude identifies each clip by its content and renames it.
5. **Assemble** with `tools/assemble_clips.py` and a `plan.json` (slots, narration, captions, music, ambience). Check frames for glitches (extra limbs, text, costume swaps) and list clips to regenerate.
6. **Deliver** the MP4, SRT, trimmed clips (for manual editing), thumbnail concepts and the publishing pack; update the tracker.

## Rules for every Flow clip prompt

- **State the exact length** at the start: "8-second clip". The model then paces the action to fill it.
- **Timed beats that fill the whole clip**, matched to the narration it covers: `[0–3 s] … [3–6 s] … [6–8 s] …`. The last beat contains real action or a deliberate settle (e.g. "he stops and looks back, smiling"), never nothing; idle endings become frozen frames.
- **Action that matches the slot:** if the narration slot is shorter than the clip, put the key moment in the first part; the assembler trims the end.
- Repeat the **style block** word for word in every prompt; name each character by a visual description that matches the attached reference.
- **Silent:** no dialogue, no lip-sync, no music. **No text,** letters or numbers anywhere.
- For shots where costumes or props must not swap, use **Frames to video**: first make a still of the opening moment with the reference images, then animate it.

## How the assembler fits clips

- Stays at 24 fps; slows a clip down to at most 70% speed with motion interpolation (smooth, no repeated frames).
- Extra time goes at the **start** of the clip (before the action), never as a frozen last frame mid-action; a slow 4% camera push masks it. Per clip, `"hold_at": "end"` is allowed for closing shots.
- Clips longer than their slot are trimmed at the end.
