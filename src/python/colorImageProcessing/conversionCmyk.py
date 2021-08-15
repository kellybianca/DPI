import numpy as np
import matplotlib.pyplot as plt
import cv2

img = plt.imread("src/python/colorImageProcessing/img/baboon.png")
bgr = img.astype(float)/255.

with np.errstate(invalid='ignore', divide='ignore'):
    K = 1 - np.max(bgr, axis=2)
    C = (1-bgr[..., 2] - K)/(1-K)
    M = (1-bgr[..., 1] - K)/(1-K)
    Y = (1-bgr[..., 0] - K)/(1-K)

CMYK = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)

Y, M, C, K = cv2.split(CMYK)

np.isfinite(C).all()
np.isfinite(M).all()
np.isfinite(K).all()
np.isfinite(Y).all()

cv2.imwrite('src/python/colorImageProcessing/output/BaboonC.jpg', C)
cv2.imwrite('src/python/colorImageProcessing/output/BaboonM.jpg', M)
cv2.imwrite('src/python/colorImageProcessing/output/BaboonY.jpg', Y)
cv2.imwrite('src/python/colorImageProcessing/output/BaboonK.jpg', K)


histC = cv2.calcHist([C], [0], None, [256], [0, 256])
plt.plot(histC), plt.title('Histogram Baboon C'), plt.show()

histM = cv2.calcHist([M], [0], None, [256], [0, 256])
plt.plot(histM), plt.title('Histogram Baboon M'), plt.show()

histY = cv2.calcHist([Y], [0], None, [256], [0, 256])
plt.plot(histY), plt.title('Histogram Baboon Y'), plt.show()

histK = cv2.calcHist([K], [0], None, [256], [0, 256])
plt.plot(histK), plt.title('Histogram Baboon K'), plt.show()


img2 = plt.imread("src/python/colorImageProcessing/img/chips.png")
bgr = img2.astype(float)/255.

with np.errstate(invalid='ignore', divide='ignore'):
    K = 1 - np.max(bgr, axis=2)
    C = (1-bgr[..., 2] - K)/(1-K)
    M = (1-bgr[..., 1] - K)/(1-K)
    Y = (1-bgr[..., 0] - K)/(1-K)

CMYK = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)

Y, M, C, K = cv2.split(CMYK)

np.isfinite(C).all()
np.isfinite(M).all()
np.isfinite(K).all()
np.isfinite(Y).all()

cv2.imwrite('src/python/colorImageProcessing/output/ChipsC.jpg', C)
cv2.imwrite('src/python/colorImageProcessing/output/ChipsM.jpg', M)
cv2.imwrite('src/python/colorImageProcessing/output/ChipsY.jpg', Y)
cv2.imwrite('src/python/colorImageProcessing/output/ChipsK.jpg', K)


histC = cv2.calcHist([C], [0], None, [256], [0, 256])
plt.plot(histC), plt.title('Histogram Chips C'), plt.show()

histM = cv2.calcHist([M], [0], None, [256], [0, 256])
plt.plot(histM), plt.title('Histogram Chips M'), plt.show()

histY = cv2.calcHist([Y], [0], None, [256], [0, 256])
plt.plot(histY), plt.title('Histogram Chips Y'), plt.show()

histK = cv2.calcHist([K], [0], None, [256], [0, 256])
plt.plot(histK), plt.title('Histogram Chips K'), plt.show()


img3 = plt.imread("src/python/colorImageProcessing/img/rgbcube_kBKG.png")
bgr = img3.astype(float)/255.

with np.errstate(invalid='ignore', divide='ignore'):
    K = 1 - np.max(bgr, axis=2)
    C = (1-bgr[..., 2] - K)/(1-K)
    M = (1-bgr[..., 1] - K)/(1-K)
    Y = (1-bgr[..., 0] - K)/(1-K)

CMYK = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)

Y, M, C, K = cv2.split(CMYK)

np.isfinite(C).all()
np.isfinite(M).all()
np.isfinite(K).all()
np.isfinite(Y).all()

cv2.imwrite('src/python/colorImageProcessing/output/rgbcube_kBKGC.jpg', C)
cv2.imwrite('src/python/colorImageProcessing/output/rgbcube_kBKGM.jpg', M)
cv2.imwrite('src/python/colorImageProcessing/output/rgbcube_kBKGY.jpg', Y)
cv2.imwrite('src/python/colorImageProcessing/output/rgbcube_kBKGK.jpg', K)


histC = cv2.calcHist([C], [0], None, [256], [0, 256])
plt.plot(histC), plt.title('Histogram rgbcube_kBKG C'), plt.show()

histM = cv2.calcHist([M], [0], None, [256], [0, 256])
plt.plot(histM), plt.title('Histogram rgbcube_kBKG M'), plt.show()

histY = cv2.calcHist([Y], [0], None, [256], [0, 256])
plt.plot(histY), plt.title('Histogram rgbcube_kBKG Y'), plt.show()

histK = cv2.calcHist([K], [0], None, [256], [0, 256])
plt.plot(histK), plt.title('Histogram rgbcube_kBKG K'), plt.show()

cv2.destroyAllWindows()
