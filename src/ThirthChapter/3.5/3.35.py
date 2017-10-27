import cv2 as cv
import matplotlib.pyplot as plt

def deal(imgT, position):
    plt.subplot(1, 3, position)
    plt.imshow(imgT, cmap='Greys_r')
    plt.xticks([]), plt.yticks([])

img = cv.imread('../../../ImageMaterial/DIP3/Fig0335(a)(ckt_board_saltpep_prob_pt05).tif',cv.IMREAD_GRAYSCALE)
deal(img, 1)
img2 = cv.boxFilter(img, -1, (3,3))
deal(img2, 2)
img3 = cv.medianBlur(img, 3)
deal(img3, 3)

plt.show()