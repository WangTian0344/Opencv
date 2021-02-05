# opencv 图片的读取显示保存
import cv2
import matplotlib.pyplot as plt

# 读取图片 图片路径后有三个参数颜色显示、灰度显示和透明度，分别用1、0、-1代替
image01 = cv2.imread("../../images/image01.png", 0)
# 命名显示窗口，第二个参数可以设置窗口大小
cv2.namedWindow("image01",cv2.WINDOW_NORMAL)
# 显示图片
cv2.imshow("image01",image01)
# 等待按下键盘‘0’ 执行下面的代码
cv2.waitKey(0)
# 关闭窗口
cv2.destroyAllWindows()
# 保存图片
# cv2.imwrite("/fsfs",image01)
# matplotlib显示图片
plt.imshow(image01,cmap="gray",interpolation = 'bicubic')
# 去掉坐标轴
plt.xticks([])
plt.yticks([])
plt.show()


