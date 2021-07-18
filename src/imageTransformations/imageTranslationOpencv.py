import cv2
import numpy as np

image = cv2.imread("src/imageTransformations/animal1.jpg")
height, width = image.shape[:2]

quarter_height, quarter_width = height / 4, width / 4

T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

img_translation = cv2.warpAffine(image, T, (width, height))

cv2.imshow("Originalimage", image)
cv2.imshow('Translation', img_translation)
cv2.waitKey()

cv2.destroyAllWindows()
