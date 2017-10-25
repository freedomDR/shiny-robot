import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../../ImageMaterial/DIP3/Fig0323(a)(mars_moon_phobos).tif', cv.IMREAD_COLOR)
img = cv.cvtColor(img, code=cv.COLOR_BGR2GRAY)
plt.subplot(1, 2, 1)
plt.xticks([]), plt.yticks([])
plt.imshow(img, cmap='Greys_r')

plt.subplot(1, 2, 2)
plt.hist(img.ravel(), bins=256, range=[0, 256], density=True)
plt.xticks([]), plt.yticks([])
plt.tight_layout()

plt.show()

