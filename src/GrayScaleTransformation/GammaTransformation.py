#-*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
import cv2
import math

img = cv2.imread('../../ImageMaterial/DIP3/Fig0307(a)(intensity_ramp).tif',cv2.IMREAD_GRAYSCALE)
#print cv2.IMREAD_GRAYSCALE,cv2.IMREAD_COLOR,cv2.IMREAD_ANYCOLOR
plt.subplot(1,2,1)
plt.imshow(img,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
plt.title('original image')

#伽马变换 s=cr的k次方
c = 1.0
k = 0.4
middle = img.shape
#print middle
#imgCopy = [[[c*math.pow(img[x][y][z],k) for z in range(middle[2])]for y in range(middle[1])]for x in range(middle[0])]
imgCopy = [[c*math.pow(img[x][y],k)for y in range(middle[1])]for x in range(middle[0])]
plt.subplot(1,2,2)
plt.imshow(imgCopy,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
plt.title('gamma transformation image')

plt.show()

imgTwo = cv2.imread('../../ImageMaterial/DIP3/Fig0308(a)(fractured_spine).tif',cv2.IMREAD_GRAYSCALE)

plt.subplot(2,2,1)
plt.imshow(imgTwo,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
plt.title('original image')

middle = imgTwo.shape

k = 0.6
imgTwo1 = [[c*math.pow(imgTwo[x][y],k) for y in range(middle[1])]for x in range(middle[0])]
plt.subplot(2,2,2)
plt.imshow(imgTwo1,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
plt.title('k = 0.6')

k = 0.4
imgTwo2 = [[c*math.pow(imgTwo[x][y],k) for y in range(middle[1])]for x in range(middle[0])]
plt.subplot(2,2,3)
plt.imshow(imgTwo2,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
plt.title('k = 0.4')

k = 0.3
imgTwo3 = [[c*math.pow(imgTwo[x][y],k) for y in range(middle[1])]for x in range(middle[0])]
plt.subplot(2,2,4)
plt.imshow(imgTwo3,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
plt.title('k = 0.3')

plt.show()

imgThree = cv2.imread('../../ImageMaterial/DIP3/Fig0309(a)(washed_out_aerial_image).tif',cv2.IMREAD_GRAYSCALE)

plt.subplot(2,2,1)
plt.imshow(imgThree,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
plt.title('original image')

middle = imgThree.shape

k = 3.0
imgThree1 = [[c*math.pow(imgThree[x][y],k) for y in range(middle[1])]for x in range(middle[0])]
plt.subplot(2,2,2)
plt.imshow(imgThree1,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
plt.title('k = 3.0')

k = 4.0
imgThree2 = [[c*math.pow(imgThree[x][y],k) for y in range(middle[1])]for x in range(middle[0])]
plt.subplot(2,2,3)
plt.imshow(imgThree2,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
plt.title('k = 4.0')
k = 5.0
imgThree3 = [[c*math.pow(imgThree[x][y],k) for y in range(middle[1])]for x in range(middle[0])]
plt.subplot(2,2,4)
plt.imshow(imgThree3,cmap='Greys_r')
plt.xticks([])
plt.yticks([])
plt.title('k = 5.0')

plt.show()