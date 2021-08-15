import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img1 = cv.imread('src/python/colorImageProcessing/img/baboon.png')
hsv1 = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
plt.imshow(hsv1), plt.title('HSV Image Baboon'), plt.show()

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr1 = cv.calcHist([hsv1], [i], None, [256], [0, 256])
    plt.plot(histr1, color=col)
    plt.xlim([0, 256])
plt.title('Histogram HSV Baboon'), plt.show()

img2 = cv.imread('src/python/colorImageProcessing/img/chips.png')
hsv2 = cv.cvtColor(img2, cv.COLOR_BGR2HSV)
plt.imshow(hsv2), plt.title('HSV Image Chips'), plt.show()

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr2 = cv.calcHist([hsv1], [i], None, [256], [0, 256])
    plt.plot(histr2, color=col)
    plt.xlim([0, 256])
plt.title('Histogram HSV Chips'), plt.show()

img3 = cv.imread('src/python/colorImageProcessing/img/rgbcube_kBKG.png')
hsv3 = cv.cvtColor(img3, cv.COLOR_BGR2HSV)
plt.imshow(hsv3)
plt.title('HSV Image rgbcube_kBKG')
plt.show()

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr3 = cv.calcHist([hsv1], [i], None, [256], [0, 256])
    plt.plot(histr3, color=col)
    plt.xlim([0, 256])
plt.title('Histogram HSV rgbcube_kBKG'), plt.show()

cv.destroyAllWindows()
