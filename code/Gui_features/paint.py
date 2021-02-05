# opencv 绘图
import cv2
import numpy as np
# 初始化图像 512*512全黑
image = np.zeros((512,512,3),np.uint8)
# 直线
image = cv2.line(image,(0,0),(511,511),(255,0,0))
# 矩形
image = cv2.rectangle(image,(384,0),(510,128),(0,255,0),3)
# 圆
image = cv2.circle(image,(312,312),50,(255,0,0),-1)
# 椭圆
image = cv2.ellipse(image,(156,156),(100,50),0,0,270,255,-1)
# 多边形
v = np.array([[100,200],[32,17],[461,254],[145,321],[196,511]],np.int32)
v.reshape(-1,1,2)       # 坐标要转化为[?,1,2]的形式
image = cv2.polylines(image,[v],True,(0,211,31))
# 文字
font = cv2.FONT_HERSHEY_PLAIN
image = cv2.putText(image,"opencv",(10,500),font,7,(0,255,0),cv2.LINE_AA)
# 显示
cv2.imshow("paint",image)
cv2.waitKey(0)
cv2.destroyAllWindows()