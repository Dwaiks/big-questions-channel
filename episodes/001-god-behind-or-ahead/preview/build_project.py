"""Builds project.json for the episode 1 preview (Scenes 1-2), B2 Colorful Hand-Drawn, 16:9.

Times: video time = narration time + LEAD. Layer key times are relative to their shot.
Design plane is 1280 x 720; backgrounds are 1920 x 1080 images placed full-frame.
"""
import json

LEAD = 0.15
TAIL = 0.5
VOICE = 39.46
END = round(LEAD + VOICE + TAIL, 2)
S1_END = 18.65  # start of "Say you are standing..."
S3_START = 29.33  # "Same distance, different reference."

INK = "#3a2f28"
TERRACOTTA = "#b5603f"


def bob(times, base_y, amp=5, base_angle=0.0, tilt=0.02):
    """Gentle breathing sway for a standing character: alternating y and angle keys."""
    keys = []
    for i, t in enumerate(times):
        s = 1 if i % 2 else -1
        keys.append({"t": round(t, 2), "y": base_y + s * amp, "angle": base_angle + s * tilt})
    return keys


def frange(a, b, step):
    out, t = [], a
    while t <= b + 1e-9:
        out.append(round(t, 2))
        t += step
    return out


def merge(*key_lists):
    """Merge key lists by time; later lists override fields at equal times."""
    by_t = {}
    for kl in key_lists:
        for k in kl:
            by_t.setdefault(k["t"], {}).update(k)
    return [by_t[t] for t in sorted(by_t)]


# ---------------- Scene 1: hillside at dusk (0 - 18.65) ----------------
s1_len = S1_END
narr1_y = 275
narr1_keys = merge(
    [{"t": 0, "x": -180, "y": narr1_y, "alpha": 1}, {"t": 2.0, "x": 230, "y": narr1_y}],  # walks in
    bob(frange(2.6, 5.0, 1.2), narr1_y),
    [{"t": 5.2, "angle": 0.0}, {"t": 5.9, "angle": -0.07}, {"t": 6.7, "angle": 0.0}],  # puzzled tilt on "reference?"
    bob(frange(7.4, 12.6, 1.3), narr1_y, amp=4),
    [{"t": 12.9, "x": 230, "y": narr1_y}, {"t": 14.9, "x": 420, "y": narr1_y - 10},
     {"t": 17.0, "x": 640, "y": narr1_y - 26}, {"t": 18.6, "x": 760, "y": narr1_y - 34}],  # walks up the hill
)


def icon(id_, path, x, y, w, appear, reason):
    float_keys = [{"t": appear, "y": y + 30, "alpha": 0}, {"t": appear + 0.45, "y": y, "alpha": 1}]
    hover = [{"t": t, "y": y + (4 if i % 2 else -4)} for i, t in enumerate(frange(appear + 1.1, 11.3, 1.0))]
    gather = [{"t": 11.45, "x": x, "y": y, "w": w, "alpha": 1},
              {"t": 13.0, "x": 300 + (x - 640) * 0.15, "y": 150, "w": w * 0.45, "alpha": 0}]
    return {"type": "image", "id": id_, "path": f"art/{path}", "x": x, "y": y + 30, "w": w,
            "motion": {"role": "prop", "reason": reason},
            "keys": merge(float_keys, hover, gather)}


scene1 = {
    "start": 0, "end": S1_END,
    "layers": [
        {"type": "image", "path": "art/s01-bg.png", "x": 0, "y": 0, "w": 1280, "h": 720},
        {"type": "text", "id": "s1-heading", "text": "CAN YOU MEASURE IT?", "x": 70, "y": 40, "size": 50,
         "color": INK, "keys": [{"t": 3.7, "alpha": 0}, {"t": 4.2, "alpha": 1}, {"t": 12.4, "alpha": 1}, {"t": 13.2, "alpha": 0}]},
        icon("icon-ruler", "icon-ruler.png", 610, 130, 175, 7.45, "A ruler appears on 'a distance'"),
        icon("icon-thermometer", "icon-thermometer.png", 850, 95, 52, 8.35, "A thermometer appears on 'a temperature'"),
        icon("icon-head", "icon-head.png", 975, 105, 120, 9.25, "A thinking head appears on 'intelligence'"),
        {"type": "line", "id": "s1-path", "points": [[400, 600], [600, 580], [800, 557], [1000, 533], [1200, 512]],
         "color": TERRACOTTA, "lineWidth": 3,
         "motion": {"role": "information", "reason": "A path appears ahead as he decides to follow the question"},
         "keys": [{"t": 13.0, "progress": 0}, {"t": 16.5, "progress": 1}]},
        {"type": "image", "id": "narrator-s1", "path": "art/s01-narrator-tape.png", "x": -180, "y": narr1_y, "w": 190,
         "motion": {"role": "actor", "reason": "The narrator arrives with his tape, is puzzled, then sets off up the hill"},
         "keys": narr1_keys},
    ],
}

# ---------------- Scene 2: park lawn (18.65 - 29.33) ----------------
d = S1_END
r = lambda t: round(t - d, 2)  # narration-video time -> shot-relative
NARR_X, NARR_Y, NARR_W = 110, 342, 240
FRIEND_Y, FRIEND_W = 345, 150
CASE_X, TAPE_Y, TAPE_FULL = 333, 432, 571
RING_W = 60

friend_keys = merge(
    [{"t": 0.1, "x": 1320, "y": FRIEND_Y}, {"t": 1.8, "x": 900, "y": FRIEND_Y}],  # walks in on "standing ten metres away"
    bob(frange(2.4, 5.0, 1.1), FRIEND_Y, amp=4, tilt=0.015),
    [{"t": r(24.0), "x": 900, "y": FRIEND_Y}, {"t": r(25.2), "x": 420, "y": FRIEND_Y}],  # walks over on "walk over to me"
    [{"t": r(26.55), "x": 420, "y": FRIEND_Y}, {"t": r(28.4), "x": 900, "y": FRIEND_Y}],  # walks back on "from where you stand"
    bob([r(28.8), r(29.3)], FRIEND_Y, amp=3, tilt=0.01),
)
narr2_keys = bob(frange(0.2, r(29.3), 1.25), NARR_Y, amp=4, tilt=0.012)

scene2 = {
    "start": S1_END, "end": S3_START,
    "layers": [
        {"type": "image", "path": "art/s02-bg.png", "x": 0, "y": 0, "w": 1280, "h": 720},
        {"type": "text", "id": "s2-heading", "text": "TEN METRES FROM WHOM?", "x": 70, "y": 40, "size": 50, "color": INK,
         "keys": [{"t": 0.2, "alpha": 0}, {"t": 0.8, "alpha": 1}]},
        {"type": "image", "id": "tape-1", "path": "art/s02-tape-long.png", "x": CASE_X, "y": TAPE_Y, "w": 10,
         "motion": {"role": "prop", "reason": "The tape runs out to the friend, then rolls back as he walks over"},
         "keys": [{"t": r(22.95), "w": 10, "alpha": 0}, {"t": r(23.05), "alpha": 1},
                  {"t": r(23.9), "w": TAPE_FULL}, {"t": r(24.1), "w": TAPE_FULL},
                  {"t": r(24.6), "alpha": 1}, {"t": r(25.2), "w": 200, "alpha": 0}]},
        {"type": "image", "id": "tape-2", "path": "art/s02-tape-long.png", "x": CASE_X + TAPE_FULL - 10, "y": TAPE_Y + 18, "w": 10,
         "motion": {"role": "prop", "reason": "Measured again from the friend's side: same gap, new zero"},
         "keys": [{"t": r(28.1), "x": CASE_X + TAPE_FULL - 10, "w": 10, "alpha": 0}, {"t": r(28.2), "alpha": 1},
                  {"t": r(29.25), "x": CASE_X, "w": TAPE_FULL}]},
        {"type": "image", "id": "narrator-s2", "path": "art/s02-narrator-hook.png", "x": NARR_X, "y": NARR_Y, "w": NARR_W,
         "motion": {"role": "actor", "reason": "The narrator holds the zero of the tape against his chest"},
         "keys": narr2_keys},
        {"type": "image", "id": "friend", "path": "art/s02-friend.png", "x": 1320, "y": FRIEND_Y, "w": FRIEND_W,
         "motion": {"role": "actor", "reason": "The friend stands ten metres away, walks over, then measures from his own spot"},
         "keys": friend_keys},
        {"type": "image", "id": "ring-me", "path": "art/s02-zero-ring.png", "x": 137, "y": 434, "w": RING_W,
         "motion": {"role": "information", "reason": "The glowing zero marks the narrator as the reference"},
         "keys": [{"t": r(22.4), "alpha": 0, "w": 30, "x": 152, "y": 449}, {"t": r(22.75), "alpha": 1, "w": 70, "x": 132, "y": 429},
                  {"t": r(23.05), "w": RING_W, "x": 137, "y": 434}, {"t": r(27.6), "alpha": 1}, {"t": r(28.0), "alpha": 0}]},
        {"type": "image", "id": "ring-friend", "path": "art/s02-zero-ring.png", "x": 972, "y": 431, "w": RING_W,
         "motion": {"role": "information", "reason": "The zero jumps to the friend: now he is the reference"},
         "keys": [{"t": r(28.35), "alpha": 0, "w": 30, "x": 987, "y": 446}, {"t": r(28.7), "alpha": 1, "w": 70, "x": 967, "y": 426},
                  {"t": r(29.0), "w": RING_W, "x": 972, "y": 431}]},
    ],
}

# ---------------- Scene 2 ending: same gap, two references (29.33 - end) ----------------
e = S3_START
q = lambda t: round(t - e, 2)
scene3 = {
    "start": S3_START, "end": END,
    "layers": [
        {"type": "image", "path": "art/s02-bg.png", "x": 0, "y": 0, "w": 1280, "h": 720},
        {"type": "text", "id": "s3-heading", "text": "TEN METRES FROM WHOM?", "x": 70, "y": 40, "size": 50, "color": INK},
        {"type": "image", "id": "tape-both", "path": "art/s02-tape-long.png", "x": CASE_X, "y": TAPE_Y + 18, "w": TAPE_FULL},
        {"type": "image", "id": "narrator-s3", "path": "art/s02-narrator-hook.png", "x": NARR_X, "y": NARR_Y, "w": NARR_W,
         "motion": {"role": "actor", "reason": "Both men stand at the two ends of the same gap"},
         "keys": bob(frange(0.1, q(END), 1.25), NARR_Y, amp=4, tilt=0.012)},
        {"type": "image", "id": "friend-s3", "path": "art/s02-friend.png", "x": 900, "y": FRIEND_Y, "w": FRIEND_W,
         "motion": {"role": "actor", "reason": "The friend holds the other end"},
         "keys": bob(frange(0.6, q(END), 1.1), FRIEND_Y, amp=4, tilt=0.015)},
        {"type": "image", "id": "ring-me-2", "path": "art/s02-zero-ring.png", "x": 137, "y": 434, "w": RING_W,
         "motion": {"role": "information", "reason": "'Same distance': the zero returns to the narrator"},
         "keys": [{"t": 0.05, "alpha": 0, "w": 30, "x": 152, "y": 449}, {"t": 0.4, "alpha": 1, "w": 70, "x": 132, "y": 429},
                  {"t": 0.7, "w": RING_W, "x": 137, "y": 434}]},
        {"type": "image", "id": "ring-friend-2", "path": "art/s02-zero-ring.png", "x": 972, "y": 431, "w": RING_W,
         "motion": {"role": "information", "reason": "'Different reference': the friend's zero pulses"},
         "keys": [{"t": 0.9, "w": RING_W, "x": 972, "y": 431}, {"t": 1.2, "w": 76, "x": 964, "y": 423},
                  {"t": 1.55, "w": RING_W, "x": 972, "y": 431}]},
        {"type": "text", "id": "label-10m", "text": "10 m", "x": 590, "y": 300, "size": 58, "color": TERRACOTTA,
         "keys": [{"t": q(31.7), "alpha": 0, "y": 320}, {"t": q(32.2), "alpha": 1, "y": 300}]},
        {"type": "text", "id": "label-from", "text": "...from where?", "x": 545, "y": 368, "size": 40, "color": INK,
         "keys": [{"t": q(36.0), "alpha": 0, "y": 384}, {"t": q(36.5), "alpha": 1, "y": 368}]},
        {"type": "arrow", "id": "arrow-me", "x": 532, "y": 392, "w": 326, "angle": 2.994, "color": TERRACOTTA, "lineWidth": 3,
         "motion": {"role": "information", "reason": "The place it was measured from: here"},
         "keys": [{"t": q(37.9), "progress": 0}, {"t": q(38.6), "progress": 1}]},
        {"type": "arrow", "id": "arrow-friend", "x": 760, "y": 392, "w": 206, "angle": 0.236, "color": TERRACOTTA, "lineWidth": 3,
         "motion": {"role": "information", "reason": "...or here"},
         "keys": [{"t": q(38.5), "progress": 0}, {"t": q(39.2), "progress": 1}]},
    ],
}

project = {
    "version": 1,
    "style": "B2",
    "width": 1920, "height": 1080, "fps": 30,
    "voice": {"path": "narration.wav", "lead": LEAD, "tail": TAIL},
    "captions": json.load(open("captions.json")),
    "shots": [scene1, scene2, scene3],
    "music": {"path": "../music/Snowfall - Asher Fulero.mp3", "gain": 0.06},
    # CC0 outdoor bed (Kresiek The Furry, "AMB Outside 1", opengameart.org), kept very low
    "ambience": [
        {"path": "sound/ambience-outdoor-cc0.ogg", "start": 0, "end": S1_END, "gain": 0.025, "fadeIn": 1.0, "fadeOut": 0.6},
        {"path": "sound/ambience-outdoor-cc0.ogg", "start": S1_END, "end": END, "gain": 0.035, "offset": 8.0, "fadeIn": 0.6, "fadeOut": 1.0},
    ],
    "sfx": [
        {"time": 3.8, "kind": "paper", "gain": 0.05},
        {"time": 7.5, "kind": "pop", "gain": 0.02},
        {"time": 8.4, "kind": "pop", "gain": 0.02},
        {"time": 9.3, "kind": "pop", "gain": 0.02},
        {"time": 18.85, "kind": "paper", "gain": 0.05},
        {"time": 22.55, "kind": "chime", "gain": 0.03},
        {"time": 23.1, "kind": "tap", "gain": 0.04},
        {"time": 28.4, "kind": "chime", "gain": 0.03},
        {"time": 29.45, "kind": "chime", "gain": 0.025},
        {"time": 31.75, "kind": "paper", "gain": 0.05},
    ],
    "reference_review": {
        "author_id": "claude-code-session",
        "capability": {
            "mode": "sample_target",
            "environment": "Claude Code cloud session; illustrations generated by the author in Google Flow and cut out locally",
            "limitations": [
                "Characters are flat cut-outs without articulated limbs; motion is whole-figure movement",
                "The agent cannot listen to audio; the mix must be checked by ear by the author",
            ],
        },
    },
}
json.dump(project, open("project.json", "w"), indent=1)
print("project.json written, end", END)
