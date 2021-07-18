import numpy as np
import argparse
import cv2

image = cv2.imread("src/imageTransformations/animal1.jpg")
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
cv2.imshow("Rectangular Mask", mask)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# mask = np.zeros(image.shape[:2], dtype="uint8")
# cv2.circle(mask, (145, 200), 100, 255, -1)
# masked = cv2.bitwise_and(image, image, mask=mask)
# # show the output images
# cv2.imshow("Circular Mask", mask)
# cv2.imshow("Mask Applied to Image", masked)
# cv2.waitKey(0)