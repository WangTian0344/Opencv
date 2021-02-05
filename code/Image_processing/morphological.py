import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("../../images/image02.png")
kernel = np.ones((5,5),np.uint8)

img1 = cv2.erode(img,kernel,iterations=1)
img2 = cv2.dilate(img,kernel,iterations=1)
img3 = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

plt.subplot(221)
plt.title("Original")
plt.imshow(img)
plt.xticks([])
plt.yticks([])

plt.subplot(222)
plt.title("Erode")
plt.imshow(img1)
plt.xticks([])
plt.yticks([])

plt.subplot(223)
plt.title("dilation")
plt.imshow(img2)
plt.xticks([])
plt.yticks([])

plt.subplot(224)
plt.title("morphology")
plt.imshow(img3)
plt.xticks([])
plt.yticks([])

plt.show()

