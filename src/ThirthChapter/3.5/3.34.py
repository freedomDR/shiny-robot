#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

def deal(imgDst,num):
    plt.subplot(1,3,num)
    plt.xticks([]), plt.yticks([])
    plt.imshow(imgDst, cmap='Greys_r')

img = cv.imread('../../../ImageMaterial/DIP3/Fig0334(a)(hubble-original).tif',cv.IMREAD_GRAYSCALE)
deal(img, 1)
img15 = cv.blur(img, ksize=(15, 15))
deal(img15, 2)
#print np.max(img15)
ret, imgThreshold = cv.threshold(img15, np.max(img15) * 0.25, maxval=255,type=cv.THRESH_BINARY)
#print ret
deal(imgThreshold, 3)

plt.show()