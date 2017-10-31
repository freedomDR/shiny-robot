# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def generate(img, x, y):
    step = 256 / 10
    if img[x][y] < step:
        img[x - 1][y - 1], img[x - 1][y], img[x - 1][y + 1], img[x][y - 1], img[x][y], img[x][y + 1], img[x + 1][y - 1], \
        img[x + 1][y], \
        img[x + 1][y + 1] = 0, 0, 0, 0, 0, 0, 0, 0, 0
    elif img[x][y] < step * 2:
        img[x - 1][y - 1], img[x - 1][y], img[x - 1][y + 1], img[x][y - 1], img[x][y], img[x][y + 1], img[x + 1][y - 1], \
        img[x + 1][y], \
        img[x + 1][y + 1] = 0, 255, 0, 0, 0, 0, 0, 0, 0
    elif img[x][y] < step * 3:
        img[x - 1][y - 1], img[x - 1][y], img[x - 1][y + 1], img[x][y - 1], img[x][y], img[x][y + 1], img[x + 1][y - 1], \
        img[x + 1][y], \
        img[x + 1][y + 1] = 0, 255, 0, 0, 0, 0, 0, 0, 255
    elif img[x][y] < step * 4:
        img[x - 1][y - 1], img[x - 1][y], img[x - 1][y + 1], img[x][y - 1], img[x][y], img[x][y + 1], img[x + 1][y - 1], \
        img[x + 1][y], \
        img[x + 1][y + 1] = 255, 255, 0, 0, 0, 0, 0, 0, 255
    elif img[x][y] < step * 5:
        img[x - 1][y - 1], img[x - 1][y], img[x - 1][y + 1], img[x][y - 1], img[x][y], img[x][y + 1], img[x + 1][y - 1], \
        img[x + 1][y], \
        img[x + 1][y + 1] = 255, 255, 0, 0, 0, 0, 255, 0, 255
    elif img[x][y] < step * 6:
        img[x - 1][y - 1], img[x - 1][y], img[x - 1][y + 1], img[x][y - 1], img[x][y], img[x][y + 1], img[x + 1][y - 1], \
        img[x + 1][y], \
        img[x + 1][y + 1] = 255, 255, 255, 0, 0, 0, 255, 0, 255
    elif img[x][y] < step * 7:
        img[x - 1][y - 1], img[x - 1][y], img[x - 1][y + 1], img[x][y - 1], img[x][y], img[x][y + 1], img[x + 1][y - 1], \
        img[x + 1][y], \
        img[x + 1][y + 1] = 255, 255, 255, 0, 0, 255, 255, 0, 255
    elif img[x][y] < step * 8:
        img[x - 1][y - 1], img[x - 1][y], img[x - 1][y + 1], img[x][y - 1], img[x][y], img[x][y + 1], img[x + 1][y - 1], \
        img[x + 1][y], \
        img[x + 1][y + 1] = 255, 255, 255, 0, 0, 255, 255, 255, 255
    elif img[x][y] < step * 9:
        img[x - 1][y - 1], img[x - 1][y], img[x - 1][y + 1], img[x][y - 1], img[x][y], img[x][y + 1], img[x + 1][y - 1], \
        img[x + 1][y], \
        img[x + 1][y + 1] = 255, 255, 255, 255, 0, 255, 255, 255, 255
    else:
        img[x - 1][y - 1], img[x - 1][y], img[x - 1][y + 1], img[x][y - 1], img[x][y], img[x][y + 1], img[x + 1][y - 1], \
        img[x + 1][y], \
        img[x + 1][y + 1] = 255, 255, 255, 255, 255, 255, 255, 255, 255


#色调处理函数
def halftoning(img,position):
    resImg = np.zeros([img.shape[0] * 3, img.shape[1] * 3])
    for x in range(1, resImg.shape[0], 3):
        for y in range(1, resImg.shape[1], 3):
            resImg[x][y] = img[(x-1)//3][(y-1)//3]
            generate(resImg, x, y)
    custom_show(resImg,position)


def custom_show(img_show, position):
    plt.subplot(position[0],position[1],position[2])
    plt.imshow(img_show, cmap='Greys_r')
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()


#身成图像

img = [[y for y in range(256)]for x in range(256)]
img = np.array(img)
plt.figure(1)
halftoning(img,[1,1,1])
plt.figure(2)
img = cv.imread('../../ImageMaterial/DIP3E_Original_Images_CH02/Fig0222(a)(face).tif',cv.IMREAD_GRAYSCALE)
halftoning(img,[1,1,1])
plt.figure(3)
img = cv.imread('../../ImageMaterial/DIP3E_Original_Images_CH02/Fig0222(b)(cameraman).tif',cv.IMREAD_GRAYSCALE)
halftoning(img,[1,1,1])
plt.figure(4)
img = cv.imread('../../ImageMaterial/DIP3E_Original_Images_CH02/Fig0222(c)(crowd).tif',cv.IMREAD_GRAYSCALE)
halftoning(img,[1,1,1])
plt.show()

