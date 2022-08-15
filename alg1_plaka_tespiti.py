import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

def plaka_konum_don(img):

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    pr_img = cv2.medianBlur(img_gray, 5)
    pr_img = cv2.medianBlur(pr_img, 5)

    medyan = np.median(pr_img)
    low = 0.67 * medyan
    high = 1.33 * medyan

    edges = cv2.Canny(pr_img, low, high)
    edges = cv2.dilate(edges, np.ones((3, 3), np.uint8), iterations=1)

    cnt = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = cnt[0]
    cnt = sorted(cnt, key=cv2.contourArea, reverse=True)

    H, W = 500, 500
    plaka = None

    for c in cnt:
        rect = cv2.minAreaRect(c)
        (x, y), (h, w), r = rect
        if (w > h and w > h * 2) or (h > w and h > w * 2):
            box = cv2.boxPoints(rect)
            box = np.uint64(box)

            minx = np.min(box[:, 0])
            miny = np.min(box[:, 1])
            maxx = np.max(box[:, 0])
            maxy = np.max(box[:, 1])

            muh_plaka = img_gray[miny:maxy, minx:maxx].copy()
            muh_medyan = np.median(muh_plaka, )

            kon1 = muh_medyan > 85 and muh_medyan < 200
            kon2 = h < 50 and w < 150
            kon3 = w < 50 and h < 150

            print('muh_plaka medyan: {} genislik: {} yukseklik: {}'.format(muh_medyan, w, h))
            kon = False
            if (kon1 and (kon2 or kon3)):
                # plakadır
                #cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
                plaka = [int(i) for i in [minx, miny, w, h]]
                kon = True
            else:
                # plaka degildir
                #cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
                kon=False

            if (kon):
                return plaka
    return []


resim_adresleri = os.listdir("veriseti")

img = cv2.imread("veriseti/"+resim_adresleri[4])
img = cv2.resize(img, (500,500))

plaka_konumu = plaka_konum_don(img)


