import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from scipy import misc

face = misc.face(gray=True)
lx, ly = face.shape
crop_face = face[lx//4:-lx//4, ly//4:-ly//4]
flip_ud_face = np.flipud(face)

plt.subplot(151)
plt.imshow(face, cmap=plt.cm.gray)
plt.title('original')
plt.axis('off')

plt.subplot(152)
plt.imshow(crop_face, cmap=plt.cm.gray)
plt.title('crop image')
plt.axis('off')

plt.subplot(153)
plt.imshow(flip_ud_face, cmap=plt.cm.gray)
plt.title('flip image')
plt.axis('off')

plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0,
                    right=1)

plt.show()
