# coding: utf-8
import numpy as np
import cv2 as cv
import sys

if __name__ == '__main__':
    sys.path.append('/mnt/sdb/opencv/homework/project')
    from project0201 import plt, custom_show

    original_image = cv.imread('../../../ImageMaterial/DIP3/Fig0343(a)(skeleton_orig).tif', cv.IMREAD_GRAYSCALE)
    plt.figure(1)
    custom_show(original_image, [1, 4, 1])
    laplacian_image = cv.Laplacian(original_image, ddepth=-1, ksize=3)
    custom_show(laplacian_image, [1, 4, 2])
    add_image = np.add(original_image, laplacian_image)
    custom_show(add_image, [1, 4, 3])
    sobel_image_y = cv.Sobel(original_image, ddepth=-1, dx=0, dy=1, ksize=3)
    sobel_image_x = cv.Sobel(original_image, ddepth=-1, dx=1, dy=0, ksize=3)
    sobel_image = cv.addWeighted(sobel_image_x, 0.5, sobel_image_y, 0.5, 0)
    #sobel_image = np.add(sobel_image, original_image)
    custom_show(sobel_image, [1, 4, 4])

    plt.figure(2)
    blur_image = cv.blur(sobel_image, ksize=(5, 5))
    custom_show(blur_image, [1, 4, 1])
    mutil_image = cv.addWeighted(sobel_image, 0.5,blur_image,0.5,0)
    '''
    for x in range(mutil_image.shape[0]):
        for y in range(mutil_image.shape[1]):
            mutil_image[x][y] = sobel_image[x][y] + blur_image[x][y]
            if mutil_image[x][y] > 255:
                mutil_image[x][y] = 255
    '''
    custom_show(mutil_image, [1, 4, 2])
    final_add_image = cv.addWeighted(original_image, 1,mutil_image,1,0)
    for x in range(final_add_image.shape[0]):
        for y in range(final_add_image.shape[1]):
            if final_add_image[x][y] > 255:
                final_add_image[x][y] = 255
    custom_show(final_add_image, [1, 4, 3])
    r, c = 0.5, 1
    final_image = np.copy(final_add_image)
    for x in range(final_image.shape[0]):
        for y in range(final_add_image.shape[1]):
            final_image[x][y] = c * np.power(final_image[x][y], r)
            if final_image[x][y] > 255:
                final_image[x][y] = 255
            if final_image[x][y] < 0:
                final_image[x][y] = 0
    custom_show(final_image, [1, 4, 4])
    plt.figure(3)
    custom_show(sobel_image,[1,1,1])
    plt.figure(4)
    custom_show(blur_image,[1,1,1])
    plt.show()
