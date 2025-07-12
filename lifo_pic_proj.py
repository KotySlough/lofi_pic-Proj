#!/usr/bin/env python3
import sys
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

def cartoonify_cv(img_bgr):
    # Edge detection
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
        blockSize=9, C=2
    )

    # Color smoothing
    color = img_bgr
    for _ in range(2):
        color = cv2.pyrDown(color)
    for _ in range(7):
        color = cv2.bilateralFilter(color, d=9, sigmaColor=300, sigmaSpace=300)
    for _ in range(2):
        color = cv2.pyrUp(color)

    # Combine edges and color
    color = cv2.resize(color, (img_bgr.shape[1], img_bgr.shape[0]))
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def apply_warm_pil(pil_img):
    arr = np.array(pil_img).astype(float)
    # Warm/copper tone
    arr = np.dot(arr[..., :3], [[0.4,0.6,0.2],[0.3,0.5,0.1],[0.2,0.4,0.0]])
    arr = np.clip(arr, 0,255).astype(np.uint8)
    return Image.fromarray(arr)

def add_lofi_overlays(pil_img):
    # Grain
    arr = np.array(pil_img)
    noise = np.random.normal(0, 15, arr.shape).astype(np.int16)
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    img = Image.fromarray(arr)
    # Vignette
    w, h = img.size
    mask = Image.new('L', (w,h), 0)
    for x in range(w):
        for y in range(h):
            d = ((x-w/2)**2 + (y-h/2)**2)**0.5
            mask.putpixel((x,y), int(255 - min(d/(w/2)*255,255)))
    mask = mask.filter(ImageFilter.GaussianBlur(50))
    dark = ImageEnhance.Brightness(img).enhance(0.85)
    return Image.composite(dark, img, mask)

def main(in_path, out_path):
    bgr = cv2.imread(in_path)
    if bgr is None:
        print("Error: could not read input")
        sys.exit(1)
    cartoon = cartoonify_cv(bgr)
    # Convert to PIL for warmth/grain/vignette
    pil = Image.fromarray(cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB))
    pil = apply_warm_pil(pil)
    pil = add_lofi_overlays(pil)
    pil.save(out_path)
    print(f"✔️ Saved transformed image to {out_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python lifo_pic_proj.py input.jpg output.jpg")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
