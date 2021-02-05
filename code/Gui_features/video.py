# opencv 视频的读取显示

import cv2
# 读取视频文件 参数为视频路径
cap = cv2.VideoCapture("0")
# 当cap打开时，读取视频
while cap.isOpened():
    # 一帧一帧的u去
    ret, frame = cap.read()
    # 灰度
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 显示
    cv2.imshow("gray",frame)
    if cv2.waitKey(1) & 0xFF == ord(q):
        break
# 释放cap
cap.release()
cv2.destroyAllWindows()