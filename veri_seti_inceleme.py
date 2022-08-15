import os
import cv2
import matplotlib.pyplot as plt
from alg1_plaka_tespiti import plaka_konum_don

# 1.alg veri seti inceleme

"""
veri = os.listdir("veriseti")

for image_url in veri:
    img = cv2.imread("veriseti/"+image_url)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (500,500))
    plt.imshow(img)
    plt.show()
"""



# 2.alg veri seti inceleme

veri = os.listdir("veriseti")

for image_url in veri:
    img = cv2.imread("veriseti/"+image_url)
    img = cv2.resize(img, (500,500))

    plaka = plaka_konum_don(img) # x,y,w,h
    x,y,w,h = plaka

    if(w>h):
        plaka_bgr = img[y:y+h,x:x+w].copy()
    else:
        plaka_bgr = img[y:y+w, x:x+h].copy()

    img = cv2.cvtColor(plaka_bgr, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()