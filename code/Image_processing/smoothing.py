import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../../images/image02.png")
kernel = np.ones((5,5),np.float32)/25

ave = cv2.filter2D(img,-1,kernel)           # 二维卷积

blur = cv2.blur(img,(5,5))                  # 普通滤波
blur = cv2.GaussianBlur(img,(5,5),0)        # 高斯滤波
blur = cv2.medianBlur(img,5)                # 中值滤波
blur = cv2.bilateralFilter(img,9,75,75)     # 双边滤波

plt.subplot(221)
plt.imshow(img)
plt.title("Original")
plt.xticks([])
plt.yticks([])

plt.subplot(222)
plt.imshow(ave)
plt.title("Averaging")
plt.xticks([])
plt.yticks([])

plt.subplot(223)
plt.imshow(blur)
plt.title("Blurred")
plt.xticks([])
plt.yticks([])

plt.show()

