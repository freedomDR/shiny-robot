# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def customShow(img, position):
    plt.subplot(position[0], position[1], position[2])
    plt.imshow(img, cmap='Greys_r')
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    pass


originImage = cv.imread('../../../ImageMaterial/DIP3/Fig0340(a)(dipxe_text).tif', cv.IMREAD_GRAYSCALE)
customShow(originImage, [1, 5, 1])
gaussImg = cv.GaussianBlur(originImage, (5, 5), sigmaX=3, sigmaY=3)
customShow(gaussImg, [1, 5, 2])
# 非锐化图像
xLen, yLen = originImage.shape[0], originImage.shape[1]
imgG = [[gaussImg[x][y] - originImage[x][y] for y in range(yLen)] for x in range(xLen)]
customShow(imgG, [1, 5, 3])
img2 = [[originImage[x][y] + imgG[x][y] for y in range(yLen)] for x in range(xLen)]
customShow(img2, [1, 5, 4])
img3 = [[originImage[x][y] + 4.5 * imgG[x][y] for y in range(yLen)] for x in range(xLen)]
customShow(img3, [1, 5, 5])
plt.show()

# cv.imshow('original', originImage)
# cv.imshow('gauss', gaussImg)
# img1 = np.array(imgG)
# img2 = np.array(img2)
# img3 = np.array(img3)
# cv.imshow('diff',img1)
# cv.imshow('k=1',img2)
# cv.imshow('k=4.5',img3)

# cv.waitKey(0)
