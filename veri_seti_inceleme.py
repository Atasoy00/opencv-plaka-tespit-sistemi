import os
import cv2
import matplotlib.pyplot as plt

veri = os.listdir("veriseti")

for image_url in veri:
    img = cv2.imread("veriseti/"+image_url)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (640,480))
    plt.imshow(img)
    plt.show()