import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from alg1_plaka_tespiti import plaka_konum_don

veri = os.listdir("veriseti")
foo = veri[1]

img = cv2.imread("veriseti/"+foo)
img = cv2.resize(img, (500, 500))

plaka = plaka_konum_don(img)
x, y, w, h = plaka

if (w > h):
    plaka_bgr = img[y:y + h, x:x + w].copy()
else:
    plaka_bgr = img[y:y + w, x:x + h].copy()

plt.imshow(plaka_bgr)
plt.show()

H,W = plaka_bgr.shape[:2]
print('orjinal boyut {},{}'.format(W, H))
H,W = H*2,W*2
print('yeni boyut    {},{}'.format(W, H))
plaka_bgr = cv2.resize(plaka_bgr, (W,H))

plt.imshow(plaka_bgr)
plt.show()

plaka_resim = cv2.cvtColor(plaka_bgr, cv2.COLOR_BGR2GRAY)

plt.imshow(plaka_resim, cmap="gray")
plt.show()

thresh = cv2.adaptiveThreshold(plaka_resim, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

plt.imshow(thresh, cmap="gray")
plt.show()

kernel = np.ones((3,3),np.uint8)
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

plt.imshow(thresh, cmap="gray")
plt.show()


