# Assembles silent Flow clips into a narrated video.
# Each clip is fitted to its narration slot: slowed down to at most MIN_SPEED (75%) and, if still short,
# its last frame is held; if long, it is trimmed. Then narration, music, ambience and burned-in captions
# are added and loudness is normalised for YouTube (about -14 LUFS).
#
# Usage: python3 tools/assemble_clips.py <plan.json>
# plan.json: {"clips": [{"file", "start", "end", "crop_top"?, "skip"?}], "narration", "captions",
#             "caption_offset", "music", "music_db", "ambience"?, "ambience_db"?, "output", "work_dir"}
import json, os, subprocess, sys

MIN_SPEED = 0.75
FPS = 30
W, H = 1920, 1080


def run(cmd):
    subprocess.run(cmd, check=True)


def duration(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path],
                         capture_output=True, text=True, check=True).stdout
    return float(out.strip())


def fit_clip(c, work, idx):
    slot = c['end'] - c['start']
    src = c['file']
    skip = c.get('skip', 0.0)
    length = duration(src) - skip
    speed = max(MIN_SPEED, min(1.0, length / slot))
    played = length / speed
    hold = max(0.0, slot - played)
    crop = c.get('crop_top', 0)
    vf = []
    if skip:
        vf.append(f'trim=start={skip},setpts=PTS-STARTPTS')
    if crop:
        vf.append(f'crop=iw:ih-{crop}:0:{crop}')
    vf += [f'scale={W}:{H}:force_original_aspect_ratio=increase', f'crop={W}:{H}',
           f'setpts=PTS/{speed:.4f}', f'fps={FPS}']
    if hold > 0:
        vf.append(f'tpad=stop_mode=clone:stop_duration={hold:.3f}')
    vf.append(f'trim=duration={slot:.3f},setpts=PTS-STARTPTS')
    out = os.path.join(work, f'fit-{idx:02d}.mp4')
    run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-an', '-vf', ','.join(vf), '-c:v', 'libx264', '-preset', 'medium',
         '-crf', '18', '-pix_fmt', 'yuv420p', out])
    return out, speed, hold


def ass_time(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f'{h}:{m:02d}:{s:05.2f}'


def write_ass(captions, offset, path, font_dir):
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Noto Sans,54,&H00262B33,&H00262B33,&H00E3F0F6,&H00E3F0F6,0,0,0,0,100,100,0,0,3,14,0,2,80,80,60,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = [f"Dialogue: 0,{ass_time(c['start'] + offset)},{ass_time(c['end'] + offset)},Cap,,0,0,0,,{c['text']}"
             for c in captions]
    open(path, 'w').write(head + '\n'.join(lines) + '\n')


def main():
    plan = json.load(open(sys.argv[1]))
    base = os.path.dirname(os.path.abspath(sys.argv[1]))
    p = lambda x: x if os.path.isabs(x) else os.path.join(base, x)
    work = p(plan['work_dir']); os.makedirs(work, exist_ok=True)
    parts = []
    for i, c in enumerate(plan['clips'], 1):
        c = dict(c, file=p(c['file']))
        out, speed, hold = fit_clip(c, work, i)
        parts.append(out)
        print(f"{os.path.basename(c['file'])}: slot {c['end'] - c['start']:.2f}s, speed {speed:.2f}, hold {hold:.2f}s")
    listing = os.path.join(work, 'list.txt')
    open(listing, 'w').write(''.join(f"file '{x}'\n" for x in parts))
    video = os.path.join(work, 'video.mp4')
    run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', listing, '-c', 'copy', video])
    total = plan['clips'][-1]['end']
    ass = os.path.join(work, 'captions.ass')
    write_ass(json.load(open(p(plan['captions']))), plan.get('caption_offset', 0.0), ass, plan.get('font_dir'))
    font_dir = plan.get('font_dir')
    sub = f"subtitles={ass}" + (f":fontsdir={font_dir}" if font_dir else '')
    inputs = ['-i', video, '-i', p(plan['narration']), '-stream_loop', '-1', '-i', p(plan['music'])]
    mix = (f"[1:a]aresample=48000,apad[n];"
           f"[2:a]aresample=48000,volume={plan.get('music_db', -24)}dB,afade=t=in:d=1.5,"
           f"afade=t=out:st={total - 2.5:.2f}:d=2.5[m];")
    labels = '[n][m]'
    if plan.get('ambience'):
        inputs += ['-stream_loop', '-1', '-i', p(plan['ambience'])]
        mix += (f"[3:a]aresample=48000,volume={plan.get('ambience_db', -30)}dB,afade=t=in:d=1,"
                f"afade=t=out:st={total - 2:.2f}:d=2[a];")
        labels += '[a]'
    n = labels.count('[')
    mix += f"{labels}amix=inputs={n}:duration=first:normalize=0,atrim=0:{total:.3f},loudnorm=I=-14:TP=-1.5:LRA=11[out]"
    run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', mix, '-map', '0:v', '-map', '[out]',
         '-vf', sub, '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p',
         '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-t', f'{total:.3f}', p(plan['output'])])
    print('wrote', p(plan['output']))


if __name__ == '__main__':
    main()
