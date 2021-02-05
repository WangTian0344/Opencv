# 滑动条调节颜色
import cv2
import numpy as np
# 滑动条绑定函数 滑动条只获取数值，函数不需要做额外操作
def nothing(x):
    pass

img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# 创建颜色滑动条
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# 创建开关
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while True:
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:     # 退出
        break
    elif k == ord('o'): # 开关打开与关闭设置
        cv2.setTrackbarPos(switch,'image',not cv2.getTrackbarPos(switch,'image'))

    # 获取滑动条数值
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:          # 关闭
        img[:] = 0
    else:               # 打开
        img[:] = [b,g,r]

cv2.destroyAllWindows()