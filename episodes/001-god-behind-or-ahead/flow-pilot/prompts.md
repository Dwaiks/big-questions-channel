# Episode 1 · Flow video pilot (Scenes 1–2, 40 s)

Look: **(a) rich illustrated cartoon**, our own design. Silent clips; Claude adds Jon's narration, captions, music and ambience afterwards and fits each clip to its slot.

## How to generate

1. **Character sheets first (images).** In Flow, create an *image* at 16:9 for each sheet below. Keep the best one; download as PNG; upload to `flow-pilot/upload/` with the given name.
2. **Clips (videos).** For each clip: attach the needed character sheet(s) as **ingredients / reference images**, paste the prompt, 16:9, 720p, 8–10 seconds. Use the model you used for the EPM video. If Flow adds sound, that's fine — Claude removes it.
3. Upload each chosen clip as `flow-pilot/upload/c01.mp4` … `c07.mp4`.
4. Reject and regenerate a clip if: any text/letters appear, a character changes design, extra limbs or melting faces, or the action doesn't match.

Every prompt repeats the same **style block** word for word, for consistency.

---

## Character sheets (images)

**`sheet-narrator.png`**
```text
Character design sheet, richly detailed hand-drawn 2D cartoon illustration, clean confident dark ink outlines, warm natural colours with soft painterly shading, plain light warm-grey background. One original character shown four times in a row: front view, three-quarter view, side view, and a close-up of the face with three expressions (curious, surprised, delighted). The character: a friendly cartoon stick-figure man with a large round ivory-white head, big expressive oval eyes with dark pupils, thick expressive eyebrows, a small curl of dark brown hair on top of the head, a simple line mouth that changes with emotion; a thin black stick body and stick arms and legs with simple four-fingered cartoon hands; he wears a mustard-yellow knitted scarf. Consistent proportions in every view. No text, no letters, no labels, no logos.
```

**`sheet-friend.png`**
```text
Character design sheet, richly detailed hand-drawn 2D cartoon illustration, clean confident dark ink outlines, warm natural colours with soft painterly shading, plain light warm-grey background. One original character shown four times in a row: front view, three-quarter view, side view, and a close-up of the face with three expressions (puzzled, amused, thoughtful). The character: a cheerful cartoon stick-figure man, slightly taller than average, with a large round ivory-white head, big expressive oval eyes with dark pupils, expressive eyebrows, a small round nose, wearing a dusty-blue knitted beanie; thin black stick body, arms and legs with simple four-fingered cartoon hands. Consistent proportions in every view. No text, no letters, no labels, no logos.
```

---

## Style block (inside every clip prompt)

> Richly detailed hand-drawn 2D cartoon animation, clean confident dark ink outlines, warm natural colours, soft painterly shading, textured detailed backgrounds, gentle cinematic lighting, expressive faces, smooth animation. Characters exactly as in the attached character sheets. No text, no letters, no subtitles, no logos. Silent: no dialogue, no lip-sync, no music.

---

## Clips (videos) — slot = where it sits in Jon's narration

**`c01.mp4`** · slot 0.0–6.9 s · narration: *"Here is a question that sounds too simple to be interesting. Can you measure anything on its own without having a reference?"* · ingredients: narrator sheet
```text
Richly detailed hand-drawn 2D cartoon animation, clean confident dark ink outlines, warm natural colours, soft painterly shading, textured detailed backgrounds, gentle cinematic lighting, expressive faces, smooth animation. Characters exactly as in the attached character sheets. No text, no letters, no subtitles, no logos. Silent: no dialogue, no lip-sync, no music. A wide grassy hillside at dusk, peach and dusty-blue sky, first stars appearing. The narrator character (round ivory head, curl of hair, mustard scarf) stands on the slope holding a small yellow measuring tape. He pulls the tape out and tries to measure the empty air in front of him; the loose end droops and curls because there is nothing to hook it to. He looks at the floppy tape, raises one eyebrow and scratches his head, clearly puzzled. Slow gentle camera push-in. 16:9.
```

**`c02.mp4`** · slot 6.9–11.0 s · *"A distance, a temperature, intelligence?"* · ingredients: narrator sheet
```text
Richly detailed hand-drawn 2D cartoon animation, clean confident dark ink outlines, warm natural colours, soft painterly shading, textured detailed backgrounds, gentle cinematic lighting, expressive faces, smooth animation. Characters exactly as in the attached character sheets. No text, no letters, no subtitles, no logos. Silent: no dialogue, no lip-sync, no music. Same dusk hillside. Close-medium shot of the narrator character holding his yellow measuring tape. Three glowing hand-drawn objects pop into the air beside him one after another: first a wooden ruler, then a thermometer, then a translucent outline of a head with a small golden spark inside. With each one his eyes widen more; he tries to hold the tape up to each object and the tape flops every time. Playful, curious mood. Static camera with a slight drift. 16:9.
```

**`c03.mp4`** · slot 11.0–18.3 s · *"Hold on to that question, because if we follow it honestly step by step, it takes us somewhere I did not expect."* · ingredients: narrator sheet
```text
Richly detailed hand-drawn 2D cartoon animation, clean confident dark ink outlines, warm natural colours, soft painterly shading, textured detailed backgrounds, gentle cinematic lighting, expressive faces, smooth animation. Characters exactly as in the attached character sheets. No text, no letters, no subtitles, no logos. Silent: no dialogue, no lip-sync, no music. Same dusk hillside, wider view. The narrator character rolls his measuring tape back in, puts it in his pocket, takes a determined breath and starts walking up the hill toward the horizon. A faint glowing path of light appears on the grass ahead of him, step by step, leading over the hilltop into the evening sky where the first stars shine. He looks back toward the viewer once with a curious, slightly excited expression, then continues walking. Slow camera tracking to the right. 16:9.
```

**`c04.mp4`** · slot 18.3–23.6 s · *"Say you are standing ten metres away from me. I am the starting point, the zero on the tape."* · ingredients: narrator + friend sheets
```text
Richly detailed hand-drawn 2D cartoon animation, clean confident dark ink outlines, warm natural colours, soft painterly shading, textured detailed backgrounds, gentle cinematic lighting, expressive faces, smooth animation. Characters exactly as in the attached character sheets. No text, no letters, no subtitles, no logos. Silent: no dialogue, no lip-sync, no music. A sunny park in late morning: green lawn, two leafy trees, a winding path, soft clouds. Side view: the narrator character (mustard scarf) stands on the left, the friend character (dusty-blue beanie) stands on the right, far apart. The narrator holds the end of a yellow measuring tape against the middle of his own chest and stretches it toward the friend. A small warm golden glowing ring appears on the narrator's chest exactly where the tape starts, and he taps it proudly with a confident smile. The friend tilts his head, amused. Camera slowly slides along from the narrator toward the friend. 16:9.
```

**`c05.mp4`** · slot 23.6–29.0 s · *"Now walk over to me, hand me the tape, and measure the same gap from where you stand."* · ingredients: narrator + friend sheets
```text
Richly detailed hand-drawn 2D cartoon animation, clean confident dark ink outlines, warm natural colours, soft painterly shading, textured detailed backgrounds, gentle cinematic lighting, expressive faces, smooth animation. Characters exactly as in the attached character sheets. No text, no letters, no subtitles, no logos. Silent: no dialogue, no lip-sync, no music. Same sunny park, same side view. The friend character (dusty-blue beanie) walks over to the narrator character (mustard scarf), who hands him the yellow measuring tape. The friend walks back to his original spot on the right, holds the end of the tape against his own chest and stretches it back toward the narrator; the small golden glowing ring now appears on the friend's chest instead. The narrator gestures with an open hand as if saying "see?". Smooth natural walking, expressive faces. Static wide camera. 16:9.
```

**`c06.mp4`** · slot 29.0–33.4 s · *"Same distance, different reference. Nothing is measured absolutely."* · ingredients: narrator + friend sheets
```text
Richly detailed hand-drawn 2D cartoon animation, clean confident dark ink outlines, warm natural colours, soft painterly shading, textured detailed backgrounds, gentle cinematic lighting, expressive faces, smooth animation. Characters exactly as in the attached character sheets. No text, no letters, no subtitles, no logos. Silent: no dialogue, no lip-sync, no music. Same sunny park, wide side view, the yellow measuring tape stretched between the narrator character on the left and the friend character on the right. Golden glowing rings pulse on both of their chests, first the narrator's, then the friend's. Both look at the tape, then at each other with thoughtful, slightly amazed expressions. Gentle camera pull-back to show the whole park. 16:9.
```

**`c07.mp4`** · slot 33.4–39.5 s · *"Every number we ever write down quietly carries a second piece of information: the place it was measured from."* · ingredients: narrator sheet
```text
Richly detailed hand-drawn 2D cartoon animation, clean confident dark ink outlines, warm natural colours, soft painterly shading, textured detailed backgrounds, gentle cinematic lighting, expressive faces, smooth animation. Characters exactly as in the attached character sheets. No text, no letters, no subtitles, no logos. Silent: no dialogue, no lip-sync, no music. Close-up of an old wooden desk in warm light: a notebook full of hand-drawn sketches and blank number boxes, a pencil, a measuring tape. A small golden glowing dot sits beside each sketch like a pin, quietly glowing. The narrator character's hand slides the pencil along the notebook and taps each glowing dot. Then the camera rises slowly to show the narrator himself leaning over the desk, looking up with a thoughtful, curious expression. No readable text or numbers anywhere. 16:9.
```
