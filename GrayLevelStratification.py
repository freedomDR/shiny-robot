import numpy as np
import matplotlib.pyplot as plt
import cv2

plt.figure(1)

plt.subplot(1,2,1)
x = [0,2,2,3.5,3.5,5]
y = [0.5,0.5,3,3,0.5,0.5]
plt.plot(x,y,'-')
plt.axis([0,5,0,5])
plt.gca().set_aspect(1)

plt.subplot(1,2,2)
x = [0,1.5,1.5,2.5,2.5,5]
y = [0,1.5,4,4,2.5,5]
plt.plot(x,y,'-')
plt.axis([0,5,0,5])
plt.gca().set_aspect(1)

plt.figure(2)

img = cv2.imread('ImageMaterial/DIP3/Fig0312(a)(kidney).tif',cv2.IMREAD_GRAYSCALE)
plt.subplot(1,3,1)
plt.imshow(img,cmap='Greys_r')



mean = np.mean(img)
a,b = 3.9,4
left,right = mean-(np.max(img)-np.min(img))/a, mean+(np.max(img)-np.min(img))/b
def getValue(value):
    if value >= left and value <= right:
        return 1
    else:
        return 255

plt.subplot(1,3,2)
img1 = [[1*getValue(img[x][y])for y in range(img.shape[1])]for x in range(img.shape[0])]
plt.imshow(img1,cmap='Greys_r')

a,b = 5,5
left,right = mean-(np.max(img)-np.min(img))/a, mean+(np.max(img)-np.min(img))/b
plt.subplot(1,3,3)
img2 = [[img[x][y]*getValue(img[x][y])for y in range(img.shape[1])]for x in range(img.shape[0])]
plt.imshow(img2,cmap='Greys_r')

plt.show()