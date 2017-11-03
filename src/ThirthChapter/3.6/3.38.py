import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def deal(imgT, position):
    plt.subplot(1, 5, position)
    plt.imshow(imgT, cmap='Greys_r')
    plt.xticks([]), plt.yticks([])
    plt.tight_layout()

def filter(imgM, myFilter,num,c,flag):
    x, y = map(int, list(imgM.shape))
    img = np.zeros((x-4,y-4))
    for i in range(2,x-2):
        for j in range(2,y-2):
            res = 0
            for k in range(3):
                for l in range(3):
                    res += myFilter[k][l]*imgM[i+k-1][j+l-1]
            if flag == True:
                img[i-2][j-2] = imgM[i-2][j-2] + res*c
            else:
                img[i-2][j-2] = res
    return np.copy(img)
img = cv.imread('../../../ImageMaterial/DIP3/Fig0338(a)(blurry_moon).tif',cv.IMREAD_GRAYSCALE)
#img = cv.imread('../../../ImageMaterial/DIP3/Fig0342(a)(contact_lens_original).tif',cv.IMREAD_GRAYSCALE)
deal(img ,1)
xLen, yLen = map(int, list(img.shape))
imgT = np.zeros((xLen+4,yLen+4))
myFilter = np.array([[1,1,1],[1,-8,1],[1,1,1]])
for x in range(xLen):
    imgT[x+2][2:yLen+2] = img[x][:]
imgM = filter(imgT, myFilter, 2,-1,False)
deal(imgM,2)

minn = np.min(imgM)
maxx = np.max(imgM)
maxf = maxx - minn

if maxf == 0:
    maxf += 1
for x in range(xLen):
    for y in range(yLen):
        imgM[x][y] = ((imgM[x][y] - minn)/maxf)*255

deal(imgM, 3)
myFilter = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
imgM = filter(img, myFilter, 4, 1, True)
deal(imgM, 4)
myFilter = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
imgM = filter(img, myFilter, 5, 1, True)
deal(imgM, 5)

plt.show()
