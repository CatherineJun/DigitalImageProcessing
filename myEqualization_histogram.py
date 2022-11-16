import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

##仅适用于灰度图像，见数字图像处理第五章PPT 114页
# f:原图像 -------- 对应灰度直方图：h（256维的向量） ----- hs:每个灰度级的像素个数占整个图像的百分比
# g:处理后的图像


#求灰度直方图
def create_histogram(img):
    height,width = img.shape[:2]
    histogram = np.zeros(shape=[256],dtype=int)
    for i in range(height):
        for j in range(width):
            histogram[img[i][j]] += 1
    return histogram

#计算灰度分布概率
def distribution_probability(img,histogram):
    # 图像f的总体像素个数
    height = img.shape[0]
    width = img.shape[1]
    nf =  height * width

    # 计算每个灰度级的像素个数占整个图像的百分比hs
    hs = np.zeros(shape=[256],dtype=float)
    for i in range(256):
        hs[i] = histogram[i] / nf
    return hs


#计算灰度级的累计分布hp
def cumulative_distribution(f,hs):
    hp = np.zeros([256],dtype=int)
    temp = 0
    for i in range(256):
        temp += hs[i]
        hp[i] = int(f.max() * temp)
    return hp

#计算新图像的灰度值
def caculate_gray(f,hp):
    dst = np.zeros(shape=[f.shape[0], f.shape[1]], dtype=int)
    for i in range(f.shape[0]):
        for j in range(f.shape[1]):
            dst[i][j] = hp[f[i][j]]
    return dst

def myMain(filepath):
    f = cv2.imread(filepath)
    # 灰度化
    f = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    # 1.求原图f的灰度直方图h
    h = create_histogram(f)
    # 2.计算灰度分布概率hs
    hs = distribution_probability(f, h)
    # 3.计算灰度级的累计分布hp
    hp = cumulative_distribution(f, hs)
    # 4.计算新图像的灰度值--得到新图像
    g = caculate_gray(f, hp)
    # 5.计算新图像灰度直方图
    h_new = create_histogram(g)
    return g

if __name__ == '__main__':
    # 读入图像
    f = cv2.imread("pic/lena.BMP")
    # 灰度化
    f = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    # 1.求原图f的灰度直方图h
    h = create_histogram(f)
    # 2.计算灰度分布概率hs
    hs = distribution_probability(f, h)
    # 3.计算灰度级的累计分布hp
    hp = cumulative_distribution(f, hs)
    # 4.计算新图像的灰度值--得到新图像
    g = caculate_gray(f, hp)
    # 5.计算新图像灰度直方图
    h_new = create_histogram(g)


    # 设置中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 绘制灰度直方图
    x = np.arange(256)
    plt.figure(num=1)
    plt.subplot(2, 2, 1)
    plt.plot(x, h, linewidth=2, c='black')
    plt.title("原图")
    plt.ylabel("number of pixels")
    plt.subplot(2, 2, 2)
    plt.plot(x, h_new, linewidth=2, c='black')
    plt.title("直方图均衡化后的图片")
    plt.ylabel("number of pixels")
    plt.subplot(2, 2, 3)
    plt.imshow(f, cmap=plt.cm.gray)
    plt.subplot(2, 2, 4)
    plt.imshow(g, cmap=plt.cm.gray)
    plt.show()


