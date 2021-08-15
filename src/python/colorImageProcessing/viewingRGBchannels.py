import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('src/python/colorImageProcessing/img/baboon.png')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr1 = cv.calcHist([img1], [i], None, [256], [0, 256])
    plt.plot(histr1, color=col)
    plt.xlim([0, 256])
plt.title('Baboon')
plt.show()

img2 = cv.imread('src/python/colorImageProcessing/img/chips.png')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr2 = cv.calcHist([img2], [i], None, [256], [0, 256])
    plt.plot(histr2, color=col)
    plt.xlim([0, 256])
plt.title('Chips')
plt.show()

img3 = cv.imread('src/python/colorImageProcessing/img/rgbcube_kBKG.png')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr3 = cv.calcHist([img3], [i], None, [256], [0, 256])
    plt.plot(histr3, color=col)
    plt.xlim([0, 256])
plt.title('RGBCube_kBKG')
plt.show()

cv.destroyAllWindows()
