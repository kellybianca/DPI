import cv2
import scipy as ndimage
import matplotlib.pyplot as plt

path = r'src/imageTransformations/animal1.jpg'
face = cv2.imread("src/imageTransformations/animal1.jpg")

src = cv2.imread(path)

image = cv2.rotate(src, cv2.ROTATE_180)
image2 = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('Rotation image 180º', image)
cv2.imshow('Rotation image 90', image2)

cv2.waitKey(0)
