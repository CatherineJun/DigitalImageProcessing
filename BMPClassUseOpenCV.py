import cv2

####      用opencv读取图像并显示        #####
# img = cv2.imread("lena.BMP", cv2.IMREAD_COLOR)
# cv2.imshow("img", img)
# cv2.waitKey(0)

###          用opencv解决灰度化           #####
# img = cv2.imread("lena.BMP", cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度化
# cv2.imshow("gray", gray)
# cv2.waitKey(0)

# #######      镜像      #########
# #加载图片
# img = cv2.imread('lena.BMP')
# #图片-水平镜像
# img_H = cv2.flip(img, 1, dst=None)
# #图片-垂直镜像
# img_V = cv2.flip(img, 0, dst=None)
# #图片-对角镜像
# img_HV = cv2.flip(img, -1, dst=None)
# #显示测试
# cv2.imshow("img", img)
# cv2.imshow("img_H", img_H)
# cv2.imshow("img_V", img_V)
# cv2.imshow("img_HV", img_HV)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ######    用OpenCV旋转图像    ##########
# img = cv2.imread("lena.BMP")
# rotate_90_cv = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# rotate_180_cv = cv2.rotate(img, cv2.ROTATE_180)
# rotate_270_cv = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.imshow("img", img)
# cv2.imshow("rotate_90_cv", rotate_90_cv)
# cv2.imshow("rotate_180_cv", rotate_180_cv)
# cv2.imshow("rotate_270_cv", rotate_270_cv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# #缩放
# import numpy as np
# img = cv2.imread("lena.BMP")
# result = cv2.resize(img, (200,100))
# cv2.imshow("img", img)
# cv2.imshow("result", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# #直方图均衡化
# def hisEqulColor(img):
#     ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
#     channels = cv2.split(ycrcb)
#     print(len(channels))
#     cv2.equalizeHist(channels[0], channels[0])
#     cv2.merge(channels, ycrcb)
#     cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img)
#     return img
#
# im = cv2.imread('data/2.jpg')
# print(np.shape(im))
# im=cv2.resize(im,(800,600))#小于或等于屏幕分辨率
#
# cv2.imshow('im1', im)
# cv2.waitKey(0)
# eq = hisEqulColor(im)
# cv2.imshow('image2',eq )
# cv2.waitKey(0)

img = cv2.imread('pic/lena.BMP')
cv2.blur(img,(3,3))
cv2.imshow("均值滤波",img)
cv2.waitKey(0)