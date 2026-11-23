# Removes the flat chroma-key green from Flow cut-outs and crops to the drawing.
# Usage: python3 tools/key_green.py <upload-dir> <layers-dir>
import sys, os, numpy as np
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
for f in sorted(os.listdir(src)):
    if not f.endswith('.png') or 'bg-' in f: continue
    im=np.asarray(Image.open(os.path.join(src,f)).convert('RGB')).astype(np.float32)
    r,g,b=im[...,0],im[...,1],im[...,2]
    green=g-np.maximum(r,b)
    a=np.clip((90-green)/(90-40),0,1)
    # despill: pull green down to the other channels where the key was partial
    spill=(a<1)|(green>15)
    g2=np.where(spill, np.minimum(g, np.maximum(r,b)+10), g)
    out=np.dstack([r,g2,b,a*255]).astype(np.uint8)
    img=Image.fromarray(out,'RGBA'); bbox=img.getbbox()
    img=img.crop(bbox); img.save(os.path.join(dst,f))
    print(f, 'cut-out size', img.size, 'from bbox', bbox)
