import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from alg1_plaka_tespiti import plaka_konum_don
from alg2_plaka_tanima import plakaTani
veriler = os.listdir("veriseti")

isim = veriler[0]
for isim in veriler:
    print("------------------------------------------------------")
    print("kaynak foto:","veriseti/"+isim)
    img = cv2.imread("veriseti/"+isim)
    img = cv2.resize(img,(500,500))

    plaka = plaka_konum_don(img)
    plakaImg,plakaKarakter = plakaTani(img,plaka)

    print("fotograftaki plaka:", ''.join(plakaKarakter))
    plt.title(f"fotograftaki plaka: {''.join(plakaKarakter)}\n")
    plt.imshow(img)
    plt.imshow(plakaImg)
    plt.show()



























