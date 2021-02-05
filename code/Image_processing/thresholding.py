import cv2

img = cv2.imread("../../images/image01.png")

# 基本阙值处理
_, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

# 适应性阙值处理
th6 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,10,2)

cv2.imshow("th1",th1)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)
cv2.imshow("th4",th4)
cv2.imshow("th5",th5)
cv2.imshow("th6",th6)
cv2.waitKey(0)
cv2.destroyAllWindows()
