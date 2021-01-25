import cv2
import numpy as np
import scipy
import scipy.signal as sig
import matplotlib.pyplot as plt
import functools
import skimage.segmentation
from skimage.color import rgb2yiq

img = cv2.imread("../../data/manu-2013.png", 0)  # read in black & white
img = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)  # normalize the image

segment_mask1 = skimage.segmentation.felzenszwalb(img, scale=100)
segment_mask2 = skimage.segmentation.felzenszwalb(img, scale=1000)

fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.imshow(segment_mask1)
ax1.set_xlabel("k=100")
ax2.imshow(segment_mask2)
ax2.set_xlabel("k=1000")
fig.suptitle("Felsenszwalb's efficient graph based image segmentation")
plt.tight_layout()
plt.show()


# show the number of segmented regions
len(np.unique(segment_mask1))
len(np.unique(segment_mask2))

# Efficient Graph-Based Image Segmentation in Python
import numpy as np
from scipy import signal
import matplotlib.image as mpimg

