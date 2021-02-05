import cv2
import numpy as np

image01 = cv2.imread("../../images/image01.png")
image02 = cv2.imread("../../images/image02.png")
# 改变颜色模式
image1 = cv2.cvtColor(image01,cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(image02,cv2.COLOR_BGR2HSV)
lower = np.array([0,5,255])
higher = np.array([50,255,255])
image3 = cv2.inRange(image2,lower,higher)       # 将hsv模式下的低于lower和高于higher的变为0，中间的变255
cv2.imshow("image01",image1)
cv2.imshow("image02",image2)
cv2.imshow("image-3",image3)
cv2.waitKey(0)
cv2.destroyAllWindows()