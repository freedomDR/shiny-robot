#-*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math

def getValue(value,mode):
    return (value % math.pow(2,mode))//math.pow(2,mode-1)

img = cv.imread('../../ImageMaterial/DIP3/Fig0314(a)(100-dollars).tif',cv.IMREAD_GRAYSCALE)

plt.figure(1)
plt.subplot(3,3,1)
plt.imshow(img,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
img1 = [[getValue(img[x][y],1) for y in range(img.shape[1])]for x in range(img.shape[0])]
plt.subplot(3,3,2)
plt.imshow(img1,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
img2 = [[getValue(img[x][y],2) for y in range(img.shape[1])]for x in range(img.shape[0])]
plt.subplot(3,3,3)
plt.imshow(img2,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
img3 = [[getValue(img[x][y],3) for y in range(img.shape[1])]for x in range(img.shape[0])]
plt.subplot(3,3,4)
plt.imshow(img3,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
img4 = [[getValue(img[x][y],4) for y in range(img.shape[1])]for x in range(img.shape[0])]
plt.subplot(3,3,5)
plt.imshow(img4,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
img5 = [[getValue(img[x][y],5) for y in range(img.shape[1])]for x in range(img.shape[0])]
plt.subplot(3,3,6)
plt.imshow(img5,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
img6 = [[getValue(img[x][y],6) for y in range(img.shape[1])]for x in range(img.shape[0])]
plt.subplot(3,3,7)
plt.imshow(img6,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
img7 = [[getValue(img[x][y],7) for y in range(img.shape[1])]for x in range(img.shape[0])]
plt.subplot(3,3,8)
plt.imshow(img7,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
img8 = [[getValue(img[x][y],8) for y in range(img.shape[1])]for x in range(img.shape[0])]
plt.subplot(3,3,9)
plt.imshow(img8,cmap='Greys_r')
plt.xticks([])
plt.yticks([])

plt.show()

def addValue(val1,m1):
    return math.pow(2,m1-1)*val1

plt.figure(2)
addimg1 = [[addValue(img8[x][y],8)+addValue(img7[x][y],7) for y in range(img.shape[1])]for x in range(img.shape[0])]
plt.subplot(1,3,1)
plt.imshow(addimg1,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
plt.title('byte 7 and 8')
addimg2 = [[addValue(img8[x][y],8)+addValue(img7[x][y],7)+addValue(img6[x][y],6) for y in range(img.shape[1])]for x in range(img.shape[0])]
plt.subplot(1,3,2)
plt.imshow(addimg2,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
plt.title('byte 7 8 6')
addimg3 = [[addValue(img8[x][y],8)+addValue(img7[x][y],7)+addValue(img6[x][y],6)+addValue(img5[x][y],5) for y in range(img.shape[1])]for x in range(img.shape[0])]
plt.subplot(1,3,3)
plt.imshow(addimg3,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
plt.title('byte 7 8 6 5')

plt.suptitle('byte plane merge')
plt.show()
