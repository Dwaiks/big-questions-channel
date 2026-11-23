# Episode 1: Flow image prompts for the 20-second preview (Scenes 1–2)

8 images. Generate each in Google Flow as an **image**, landscape **16:9**, and attach `style-reference/b2-style-character.jpg` as the style reference (ingredient) for every image. Pick the best result, download it as PNG and upload it to `art/upload/` with the file name given (GitHub: open the folder → Add file → Upload files).

Two kinds of image:
- **Backgrounds**: the empty scene, no characters.
- **Cut-outs**: one character or prop on a **solid flat chroma-key green background**. Claude removes the green and layers the cut-out over the background so it can move. Keep the green flat: no shadows, no texture, nothing touching the edges.

If an image has stray letters or words in it, regenerate it: text is added by the video tool, never drawn.

---

## Style block (already included in every prompt below)

> Hand-drawn 2D illustration in a calm editorial explainer style: warm off-white paper texture, fine slightly irregular dark-brown ink outlines, flat muted colours (dusty blue, terracotta, sage green, ochre, warm beige), simple graphic depth, generous empty space. No text, no letters, no numbers, no watermark.

## Character block (in every prompt with a character)

> A simple stickman: a round head drawn as an ink circle filled with warm ivory, two small dot eyes and a short line mouth, a single-line body, thin single-line arms and legs, no clothes, no hair, no fill on the body. Same proportions as the reference.

---

## Scene 1: Can you measure it?

**1. `s01-bg-hillside.png`** (background)
> Hand-drawn 2D illustration in a calm editorial explainer style: warm off-white paper texture, fine slightly irregular dark-brown ink outlines, flat muted colours (dusty blue, terracotta, sage green, ochre, warm beige), simple graphic depth, generous empty space. No text, no letters, no numbers, no watermark. A wide, empty grassy hillside at dusk, gentle sage-green slope in the lower third rising to the right, a soft dusty-blue and warm peach evening sky with one or two faint early stars, a few tiny distant trees on the horizon. No people. Leave the left half and the upper area calm and empty.

**2. `s01-narrator-tape.png`** (cut-out)
> Hand-drawn 2D illustration in a calm editorial explainer style, fine slightly irregular dark-brown ink outlines, flat muted colours. No text, no letters, no numbers, no watermark. A simple stickman: a round head drawn as an ink circle filled with warm ivory, two small dot eyes and a short line mouth, a single-line body, thin single-line arms and legs, no clothes, no hair, no fill on the body. Standing, full body, facing slightly right, holding a small ochre-yellow measuring-tape case in one hand; the tape is pulled out about an arm's length and its loose end droops and curls down limply in the air. Puzzled expression. Centered, whole figure visible with space around it, on a solid flat chroma-key green background, no shadow.

**3. `s01-icons.png`** (cut-out, three props)
> Hand-drawn 2D illustration in a calm editorial explainer style, fine slightly irregular dark-brown ink outlines, flat muted colours. No text, no letters, no numbers, no watermark. Three small separate icons in a row with wide gaps between them: a wooden ruler with plain tick marks and no numbers; a classic thermometer with a terracotta-red bulb and no numbers; a simple head outline in profile with a small glowing ochre spark inside. Each icon the same size, not touching, on a solid flat chroma-key green background, no shadows.

---

## Scene 2: Ten metres from whom?

**4. `s02-bg-park.png`** (background)
> Hand-drawn 2D illustration in a calm editorial explainer style: warm off-white paper texture, fine slightly irregular dark-brown ink outlines, flat muted colours (dusty blue, terracotta, sage green, ochre, warm beige), simple graphic depth, generous empty space. No text, no letters, no numbers, no watermark. A sunny park lawn in late morning seen from the side: a flat sage-green lawn across the lower third, two simple rounded trees at the far left and far right edges, a pale dusty-blue sky with one soft cloud, a thin path line in the distance. No people. The middle of the frame is open and empty.

**5. `s02-narrator-hook.png`** (cut-out)
> Hand-drawn 2D illustration in a calm editorial explainer style, fine slightly irregular dark-brown ink outlines, flat muted colours. No text, no letters, no numbers, no watermark. A simple stickman: a round head drawn as an ink circle filled with warm ivory, two small dot eyes and a short line mouth, a single-line body, thin single-line arms and legs, no clothes, no hair, no fill on the body. Standing in side view facing right, one hand holding the end of a measuring tape against the middle of his own chest, the other arm stretched out to the right holding the ochre-yellow tape case. Calm, confident expression. Whole figure, on a solid flat chroma-key green background, no shadow.

**6. `s02-friend.png`** (cut-out)
> Hand-drawn 2D illustration in a calm editorial explainer style, fine slightly irregular dark-brown ink outlines, flat muted colours. No text, no letters, no numbers, no watermark. A second simple stickman, the same drawing style as the reference: a round head drawn as an ink circle filled with warm ivory, two small dot eyes and a short line mouth, single-line body and limbs, no clothes, but wearing a small dusty-blue cap so he is easy to tell apart. Standing in side view facing left, one arm reaching forward as if to receive something. Friendly expression. Whole figure, on a solid flat chroma-key green background, no shadow.

**7. `s02-tape-long.png`** (cut-out, prop)
> Hand-drawn 2D illustration in a calm editorial explainer style, fine slightly irregular dark-brown ink outlines, flat muted colours. No text, no letters, no numbers, no watermark. One long straight ochre-yellow measuring tape stretched horizontally across almost the full width of the image, with evenly spaced small dark tick marks and no numbers, a small metal hook at the left end. On a solid flat chroma-key green background, no shadow.

**8. `s02-zero-ring.png`** (cut-out, prop)
> Hand-drawn 2D illustration in a calm editorial explainer style, fine slightly irregular dark-brown ink outlines, flat muted colours. No text, no letters, no numbers, no watermark. A single small glowing ring, like a hand-drawn circle of soft warm ochre light with a thin ink outline and a few short radiating strokes around it, centered. On a solid flat chroma-key green background, no shadow.

---

## Tips for Flow
- Generate 2–4 variations per prompt and keep the one closest to the reference's line weight and colours.
- Use the **same seed or the first good narrator** as an extra reference for image 5, so both narrator poses look like the same character.
- If Flow draws hands with fingers, add "simple line hands, no fingers" to the prompt.
