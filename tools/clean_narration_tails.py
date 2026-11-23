# Trims each narration clip just after its last spoken word, with a short fade (removes end clicks).
# Usage: python3 tools/clean_narration_tails.py <raw-dir> <out-dir>
import sys, os, subprocess, numpy as np
src, dst = sys.argv[1], sys.argv[2]
sr=44100; w=int(0.02*sr)
for f in sorted(os.listdir(src)):
    if not f.endswith('.mp3'): continue
    raw=subprocess.run(['ffmpeg','-v','error','-i',os.path.join(src,f),'-ac','1','-ar',str(sr),'-f','s16le','-'],capture_output=True).stdout
    x=np.frombuffer(raw,dtype=np.int16).astype(np.float32)/32768
    n=len(x)//w; db=20*np.log10(np.sqrt((x[:n*w].reshape(n,w)**2).mean(1))+1e-9)
    loud=np.where(db>-40)[0]
    runs=[];s=p=loud[0]
    for i in loud[1:]:
        if i-p>3: runs.append((s,p)); s=i
        p=i
    runs.append((s,p))
    # last real speech = last run longer than 200 ms
    end=[r for r in runs if (r[1]-r[0]+1)*20>200][-1][1]
    cut=min(len(x), (end+1)*w + int(0.30*sr))
    dur=cut/sr
    subprocess.run(['ffmpeg','-v','error','-y','-i',os.path.join(src,f),'-af',f'atrim=0:{dur:.3f},afade=t=out:st={dur-0.12:.3f}:d=0.12','-ar','44100','-ac','1','-c:a','libmp3lame','-b:a','128k',os.path.join(dst,f)],check=True)
    print(f, f'{len(x)/sr:.2f}s -> {dur:.2f}s')
