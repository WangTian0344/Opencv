import cv2

e1 = cv2.getTickCount()
image01 = cv2.imread("../../images/image01.png",1)
image02 = cv2.imread("../../images/image02.png",1)

# 图片叠加
# dst = cv2.addWeighted(image01,0.6,image02,0.4,0)

# 图片像素位运算
dst = cv2.bitwise_xor(image02,image01)

e2 = cv2.getTickCount()
print((e2-e1)/cv2.getTickFrequency())

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
