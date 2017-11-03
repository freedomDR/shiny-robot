# coding: utf-8
import numpy as np
import sys
import cv2 as cv

if __name__ == '__main__':
    sys.path.append('/mnt/sdb/opencv/homework/project')
    from project0201 import plt, custom_show

    original_image = cv.imread('../../../ImageMaterial/DIP3/Fig0342(a)(contact_lens_original).tif', cv.IMREAD_COLOR)
    #original_image = cv.imread('../../../ImageMaterial/DIP3/Fig0338(a)(blurry_moon).tif', cv.IMREAD_COLOR)
    custom_show(original_image, [1, 2, 1])
    res_image1 = cv.Sobel(original_image, ddepth=-1, dx=0, dy=1, ksize=3)
    #custom_show(res_image1, [1, 4, 2])
    res_image2 = cv.Sobel(original_image, ddepth=-1, dx=1, dy=0, ksize=3)
    #custom_show(res_image2, [1, 4, 3])
    res_image = np.add(res_image1, res_image2)
    res_image = cv.addWeighted(res_image1,0.5,res_image2,0.5,0)
    custom_show(res_image, [1, 2, 2])
    plt.show()
