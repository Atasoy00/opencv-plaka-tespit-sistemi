import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from alg1_plaka_tespiti import plaka_konum_don

veri = os.listdir("veriseti")
isim = veri[5]

img = cv2.imread("veriseti/"+isim)
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

cnt = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt = cnt[0]
cnt = sorted(cnt, key=cv2.contourArea, reverse=True) [:15]

for i,c in enumerate(cnt):
    rect = cv2.minAreaRect(c)
    (x,y),(w,h),r = rect

    kon1 = max([w,h]) < W/4
    kon2 = w*h > 200

    if(kon1 and kon2):
        print("karakter ... ",x,y,w,h)
        box = cv2.boxPoints(rect)
        box = np.int64(box)

        minx = np.min(box[:, 0])
        miny = np.min(box[:, 1])
        maxx = np.max(box[:, 0])
        maxy = np.max(box[:, 1])

        odak = 2

        minx = max(0, minx-odak)
        miny = max(0, miny-odak)
        maxx = min(W, maxx+odak)
        maxy = min(H, maxy+odak)

        kesit = plaka_bgr[miny:maxy, minx:maxx].copy()

        try:
            cv2.imwrite(f"karakterler/{isim}_{i}.jpg", kesit)
        except:
            pass

        yaz = plaka_bgr.copy()
        cv2.drawContours(yaz, [box], 0, (0,255,0), 1)

        plt.imshow(yaz)
        plt.show()