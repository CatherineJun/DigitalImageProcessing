import cv2
import numpy as np

#均值滤波
from numpy import median, uint8


def mean_filter(filepath, filter_size = 3):
    img = cv2.imread(filepath)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    filter = np.ones((filter_size, filter_size))  # 空间滤波器模板 卷积核
    pad_num = int((filter_size - 1) / 2)  # 输入图像需要填充的尺寸
    img = np.pad(img, (pad_num, pad_num), mode="constant", constant_values=0)  # 填充输入图像
    m = img.shape[0]  # 获取填充后的输入图像的大小
    n = img.shape[1]
    dst = np.copy(img)  # 输出图像

    # 空间滤波
    for i in range(pad_num, m - pad_num):
        for j in range(pad_num, n - pad_num):
            # 卷积运算，并计算灰度均值返回到原来的像素点
            dst[i, j] = np.sum(
                filter * img[i - pad_num:i + pad_num + 1, j - pad_num:j + pad_num + 1]) / (
                                             filter_size ** 2)

    dst = dst[pad_num:m - pad_num, pad_num:n - pad_num]  # 还原填充零之前的图像形状大小
    return dst

#中值滤波
def median_filter(filepath,filter_size = 3):
    img = cv2.imread(filepath);
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pad_num = int((filter_size - 1) / 2)  # 输入图像需要填充的尺寸
    img = np.pad(img, (pad_num, pad_num), mode="constant", constant_values=0)  # 填充输入图像
    m = img.shape[0]  # 获取填充后的输入图像的大小
    n = img.shape[1]

    for i in range(1+filter_size,m+filter_size):
        for j in range(1+filter_size,n+filter_size):
            sub_image = img[i - filter_size:i + filter_size, j - filter_size: j + filter_size]
            temp = median(sub_image[:])
            img[i-filter_size,j-filter_size] = uint8(temp)

    dst = img[pad_num:m - pad_num, pad_num:n - pad_num]  # 还原填充零之前的图像形状大小
    return dst




if __name__ == '__main__':
    filepath = 'pic/lena.BMP'
    dst = mean_filter(filepath)
    dst1 = median_filter(filepath)
    cv2.imshow('dst',dst)
    cv2.imshow('dst1',dst1)
    cv2.waitKey(0)
