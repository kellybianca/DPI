import numpy as np
import cv2
import matplotlib.pyplot as plt

rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)
    
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)
bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

# plt.subplot(151)
# plt.imshow(circle)
# plt.title('Circle')
# plt.axis('off')


# plt.subplot(152)    
# bitwiseAnd = cv2.bitwise_and(rectangle, circle)
# plt.imshow(bitwiseAnd)
# plt.title('AND')
# plt.axis('off')


# plt.subplot(153)    
# bitwiseOr = cv2.bitwise_or(rectangle, circle)
# plt.imshow(bitwiseOr)
# plt.title('OR')
# plt.axis('off')

# plt.subplot(154)    
# bitwiseXor = cv2.bitwise_xor(rectangle, circle)
# plt.imshow(bitwiseXor)
# plt.title('XOR')
# plt.axis('off')

# plt.show()