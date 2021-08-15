import numpy as np
import scipy.misc
from scipy import ndimage
import matplotlib.pyplot as plt

face = scipy.misc.face(gray=True)

rotate_face = ndimage.rotate(face, 45)

plt.figure(figsize=(12.5, 2.5))
plt.subplot(151)
plt.imshow(face, cmap=plt.cm.gray)
plt.title('Original')
plt.axis('off')
plt.subplot(152)
plt.imshow(rotate_face, cmap=plt.cm.gray)
plt.title('Rotate')
plt.axis('off')

plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0,
                    right=1)

plt.show()
