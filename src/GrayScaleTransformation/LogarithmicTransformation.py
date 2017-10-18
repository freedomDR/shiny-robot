# -*- coding: utf-8 -*-
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../../ImageMaterial/DIP3/Fig0305(a)(DFT_no_log).tif',cv2.IMREAD_COLOR)

plt.subplot(2,2,1)
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.title('original image')

#对数变换 s = clog(1+r)
c = 1
middle = img.shape
imgCopy = [[[ c*math.log(img[x][y][z] + 1)for z in range(middle[2])]for y in range(middle[1])]for x in range(middle[0])]
plt.subplot(2,2,2)
plt.imshow(imgCopy)
plt.xticks([])
plt.yticks([])
plt.title('logarithmic image')

plt.subplot(2,2,3)
x = np.arange(1,10,0.5)
print x
y = [math.log(v) for v in x]
plt.plot(x,y,'.-')

plt.subplot(2,2,4)
plt.yscale('log')
plt.show()


