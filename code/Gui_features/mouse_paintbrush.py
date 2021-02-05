# 鼠标移动绘图
import cv2
import numpy as np

drawing = False     # 是否绘画
mode = True         # 模式 True矩形 False圆形
ix, iy = -1, -1     # 初始化
# 鼠标事件相应函数
def draw_circle(event,x,y,flags,param):
    global drawing,mode,ix,iy
    # 当鼠标左键点击时进入绘画模式
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y   # 记住当前点击坐标x y
    # 鼠标移动
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
    # 鼠标左键松开时关闭绘画模式
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

if __name__ == "__main__":
    # 初始化
    img = np.zeros((512,512,3),np.uint8)
    cv2.namedWindow("image")
    # 绑定相应函数
    cv2.setMouseCallback("image",draw_circle)
    # 绘画
    while True:
        cv2.imshow("image",img)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:             # 推出
            break
        elif k == ord('m'):     # 切换模式
            mode = not mode
        elif k == ord('q'):     # 清空
            img = np.zeros((512, 512, 3), np.uint8)
    cv2.destroyAllWindows()
