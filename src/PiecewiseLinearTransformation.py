#coding=utf-8
import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('ImageMaterial/DIP3/Fig0310(b)(washed_out_pollen_image).tif',cv2.IMREAD_COLOR)

plt.figure(1)
plt.subplot(1,4,1)
plt.plot([0,20,200,255],[0,10,220,255],'ro-')

plt.subplot(1,4,2)
plt.xticks([])
plt.yticks([])
plt.imshow(img,cmap='Greys_r')
plt.title('original image')

img = cv2.imread('ImageMaterial/DIP3/Fig0310(b)(washed_out_pollen_image).tif',cv2.IMREAD_GRAYSCALE)
middle = img.shape

# s = (s2-s1)/(r2-r1) * r

r1 = np.min(img)
s1 = 0.0
r2 = np.max(img)
s2 = 255.0
k = (s2-s1)//(r2-r1)
img1 = [[k*img[x][y] for y in range(middle[1])]for x in range(middle[0])]
plt.subplot(1,4,3)
plt.xticks([])
plt.yticks([])
plt.imshow(img1,cmap='Greys_r')
plt.title('linear transformation')

r1=r2=np.mean(img)
img2 = [[250*np.int(img[x][y]//r1) for y in range(middle[1])]for x in range(middle[0])]
#print img2
plt.subplot(1,4,4)
plt.xticks([])
plt.yticks([])
plt.imshow(img2,cmap='Greys_r')
plt.title('threshold deal')

plt.suptitle('linear transformation function')


#------------------------------------------------------------------------------------


plt.show()
