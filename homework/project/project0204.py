# coding: utf-8
from project0201 import plt, custom_show
import numpy as np
import cv2 as cv


# import matplotlib.pyplot as plt


def zoom(img, number):
    #img = cv.resize(img, (img.shape[1] * number, img.shape[0] * number))
    #img_res = np.zeros([img.shape[0]*number,img.shape[1]*number])
    #for x in range(img.shape[0]):
    #    for y in range(img.shape[1]):
    #        for i in range(number):
    #            for j in range(number):
    #                img_res[x*number+i][y*number+j] = img[x][y]
    img_res = cv.resize(img, (img.shape[1] * number, img.shape[0] * number), cv.INTER_LINEAR)
    return img_res
    pass


def shrink(img, number):
    #img = cv.resize(img, (img.shape[1] // number, img.shape[0] // number), dst=img)
    #img_res = np.zeros([img.shape[0]//number,img.shape[1]//number])
    #for x in range(img_res.shape[0]):
    #    for y in range(img_res.shape[1]):
    #        for i in range(number):
    #            for j in range(number):
    #                img_res[x][y] += img[x*number+i][y*number+j]/(number*2)
    img_res = cv.resize(img, (img.shape[1]//number,img.shape[0]//number),interpolation=cv.INTER_LINEAR)
    return img_res
    pass


if __name__ == '__main__':
    originImage = cv.imread(
        '../../ImageMaterial/DIP3E_Original_Images_CH02/Fig0220(a)(chronometer 3692x2812  2pt25 inch 1250 dpi).tif',
        cv.IMREAD_GRAYSCALE)
    custom_show(originImage, [1, 3, 1])
    imgShrink = np.copy(originImage)
    imgShrink = shrink(imgShrink, 10)
    custom_show(imgShrink, [1, 3, 2])
    imgZoom = np.copy(imgShrink)
    imgZoom = zoom(imgZoom, 10)
    custom_show(imgZoom, [1, 3, 3])
    print originImage.shape
    print imgShrink.shape
    print imgZoom.shape
    plt.show()
    pass
