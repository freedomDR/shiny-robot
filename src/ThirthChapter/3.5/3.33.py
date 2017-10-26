# -*- coding: utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('../../../ImageMaterial/DIP3/Fig0333(a)(test_pattern_blurring_orig).tif', cv.IMREAD_COLOR)
print img.shape
img = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
print img.shape
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='Greys_r')
plt.xticks([]), plt.yticks([])

img3 = cv.boxFilter(img, ddepth=-1, ksize=(3, 3), normalize=True)
plt.subplot(2, 3, 2)
plt.imshow(img3, cmap='Greys_r')
plt.xticks([]), plt.yticks([])

img5 = cv.boxFilter(img, ddepth=-1, ksize=(5, 5), normalize=True)
plt.subplot(2, 3, 3)
plt.imshow(img5, cmap='Greys_r')
plt.xticks([]), plt.yticks([])

img9 = cv.boxFilter(img, ddepth=-1, ksize=(9, 9), normalize=True)
plt.subplot(2, 3, 4)
plt.imshow(img9, cmap='Greys_r')
plt.xticks([]), plt.yticks([])

img15 = cv.boxFilter(img, ddepth=-1, ksize=(15, 15), normalize=True)
plt.subplot(2, 3, 5)
plt.imshow(img15, cmap='Greys_r')
plt.xticks([]), plt.yticks([])

img35 = cv.boxFilter(img, ddepth=-1, ksize=(35, 35), normalize=True)
plt.subplot(2, 3, 6)
plt.imshow(img35, cmap='Greys_r')
plt.xticks([]), plt.yticks([])

plt.show()