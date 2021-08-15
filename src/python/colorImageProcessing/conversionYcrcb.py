import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('src/python/colorImageProcessing/img/baboon.png')
ycrcb = cv.cvtColor(img1, cv.COLOR_BGR2YCrCb)
plt.imshow(ycrcb)
plt.title('YCrCb Image Baboon')
plt.show()

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr1 = cv.calcHist([ycrcb], [i], None, [256], [0, 256])
    plt.plot(histr1, color=col)
    plt.xlim([0, 256])
plt.title('Histogram YCrCb Baboon')
plt.show()

img2 = cv.imread('src/python/colorImageProcessing/img/chips.png')
ycrcb2 = cv.cvtColor(img2, cv.COLOR_BGR2YCrCb)
plt.imshow(ycrcb2)
plt.title('YCrCb Image Chips')
plt.show()

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr2 = cv.calcHist([ycrcb2], [i], None, [256], [0, 256])
    plt.plot(histr2, color=col)
    plt.xlim([0, 256])
plt.title('Histogram YCrCb Chips')
plt.show()

img3 = cv.imread('src/python/colorImageProcessing/img/rgbcube_kBKG.png')
ycrcb3 = cv.cvtColor(img3, cv.COLOR_BGR2YCrCb)
plt.imshow(ycrcb3)
plt.title('YCrCb Image rgbcube_kBKG')
plt.show()

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr3 = cv.calcHist([ycrcb3], [i], None, [256], [0, 256])
    plt.plot(histr3, color=col)
    plt.xlim([0, 256])
plt.title('Histogram YCrCb rgbcube_kBKG')
plt.show()

cv.destroyAllWindows()
