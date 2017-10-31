import cv2 as cv
import matplotlib.pyplot as plt


def show(img_show, position):
    plt.subplot(position[0], position[1], position[2])
    plt.imshow(img_show, cmap='Greys_r')
    plt.xticks([]), plt.yticks([])
    plt.title(position)
    # plt.tight_layout()

if __name__ == '__main__':
    plt.figure(1)
    img = cv.imread('../../ImageMaterial/DIP3E_Original_Images_CH02/Fig0221(a)(ctskull-256).tif', cv.IMREAD_GRAYSCALE)
    k = 2
    img128 = [[img[x][y] - img[x][y] % k for y in range(img.shape[1])] for x in range(img.shape[0])]

    k = 4
    img64 = [[img[x][y] - img[x][y] % k for y in range(img.shape[1])] for x in range(img.shape[0])]

    k = 8
    img32 = [[img[x][y] - img[x][y] % k for y in range(img.shape[1])] for x in range(img.shape[0])]

    k = 16
    img16 = [[img[x][y] - img[x][y] % k for y in range(img.shape[1])] for x in range(img.shape[0])]
    k = 32
    img8 = [[img[x][y] - img[x][y] % k for y in range(img.shape[1])] for x in range(img.shape[0])]

    k = 64
    img4 = [[img[x][y] - img[x][y] % k for y in range(img.shape[1])] for x in range(img.shape[0])]

    k = 128
    img2 = [[img[x][y] - img[x][y] % k for y in range(img.shape[1])] for x in range(img.shape[0])]

    show(img, [2, 4, 1])
    show(img128, [2, 4, 2])
    show(img64, [2, 4, 3])
    show(img32, [2, 4, 4])
    show(img16, [2, 4, 5])
    show(img8, [2, 4, 6])
    show(img4, [2, 4, 7])
    show(img2, [2, 4, 8])
    plt.show()
