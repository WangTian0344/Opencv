import cv2
import numpy as np

image = cv2.imread("../../images/image01.png",1)
# print(image)
print(image.shape)      # 图片大小和色彩频道
print(image.size)
print(image.dtype)

# 硬核p图
# fire = image[500:700,100:300]
# image[100:300,100:300] = fire

# 分离和合并颜色
b, g, r = cv2.split(image)
image = cv2.merge((r,b,g))

# 边框
image = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,(0,255,0))

cv2.imshow("image01",image)
cv2.waitKey(0)
cv2.destroyAllWindows()