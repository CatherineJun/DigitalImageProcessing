import copy

import numpy as np
from struct import unpack
import cv2
import matplotlib.pyplot as plt

class BMP:
    def __init__(self,filePath):
        #打开bmp文件
        file = open(filePath,"rb")    #b表示以二进制方式读写

        #位图文件头      14Bytes
        print('\n----位图文件头----')
        #文件类型--2bytes
        self.bfType = str(file.read(2))
        #self.bfType = unpack("l",file.read(2))[0]
        print('文件类型：',self.bfType)
        #文件大小--4bytes--单位字节
        self.bfSize, = unpack("i",file.read(4))  #unpack返回值为tuple
        print('文件大小：',self.bfSize)
        #保留字1--2bytes
        self.bfReserved1, = unpack("h",file.read(2))
        print('保留字1：',self.bfReserved1)
        #保留字2--2bytes
        self.bfReserved2, = unpack("h",file.read(2))
        print('保留字2：',self.bfReserved2)
        #从文件头到实际位图数据的偏移字节数--4bytes
        self.bfOffBits, = unpack("i",file.read(4))
        print('偏移字节数：', self.bfOffBits,'\n')

        #位图信息头      40Bytes
        print('----位图信息头----')
        #结构长度，为40--4bytes
        self.bfSize, = unpack("i",file.read(4))
        print('结构长度：',self.bfSize)
        #图像宽度，单位像素--4bytes
        self.biWidth, = unpack("i",file.read(4))
        print('图像宽度：', self.biWidth)
        #图像高度，单位像素--4bytes
        self.biHeight, = unpack("i",file.read(4))
        print('图像高度：', self.biHeight)
        #位平面数，为1--2bytes
        self.biPlanes, = unpack("h",file.read(2))
        print('位平面数：', self.biPlanes)
        #颜色位数--2bytes
        self.biBitCount, = unpack("h",file.read(2))
        print('颜色位数：', self.biBitCount)
        #是否压缩--4bytes
        self.biCompression, = unpack("i",file.read(4))
        print('是否压缩：', self.biCompression)
        #实际位图数据占用的字节数--4bytes
        self.biSizeImage, = unpack("i",file.read(4))
        print('实际位图数据占用的字节数：', self.biSizeImage)
        #目标设备水平分辨率--4bytes
        self.biXPelsPerMeter, = unpack("i",file.read(4))
        print('目标设备水平分辨率：', self.biXPelsPerMeter)
        #目标设备垂直分辨率--4bytes
        self.biYPelsPerMeter, = unpack("i",file.read(4))
        print('目标设备垂直分辨率：', self.biYPelsPerMeter)
        #实际使用的颜色数--4bytes
        self.biClrUsed, = unpack("i",file.read(4))
        print('实际使用的颜色数：', self.biClrUsed)
        #图像中重要的颜色数--4bytes
        self.biClrImportant, = unpack("i",file.read(4))
        print('图像中重要的颜色数：', self.biClrImportant)

        #调色板--针对256色图像
        self.color_table = np.empty(shape=[256,4],dtype=int)
        for i in range(0,256):
            #将蓝色和红色索引值0和2交换，可用plt直接显示----plt通道为rgb，而读取时为bgr
            #本代码为210，pyqtGUI运行是012
            # 蓝色分量
            self.color_table[i][0] = unpack('B',file.read(1))[0]
            # 绿色分量
            self.color_table[i][1] = unpack('B',file.read(1))[0]
            # 红色分量
            self.color_table[i][2] = unpack('B',file.read(1))[0]
            # 保留值
            self.color_table[i][3] = unpack('B',file.read(1))[0]
            self.color_table[i][3] = 255

        #位图数据ImageData
        self.img = np.empty(shape=[self.biHeight,self.biWidth,4],dtype=int)
        count = 0
        for m in range(0,self.biHeight):
            for n in range(0,self.biWidth):
                count += 1
                index = unpack('B',file.read(1))[0]
                self.img[self.biHeight-m-1,n] = self.color_table[index]
            while count%4 != 0:
                file.read(1)
                count+=1

        file.close()


    #获取位图属性
    def getShuxing(self):
        res = '位图文件头：\n''文件类型：',self.bfType,'；文件大小：',self.bfSize,'字节；保留字1：',self.bfReserved1,\
              '；保留字2：',self.bfReserved2,'；偏移字节数：',self.bfOffBits,'字节；\n位图信息头：\n',\
              '结构长度：',self.bfSize,'字节；图像宽度：',self.biWidth,'字节；图像高度：',self.biHeight,'字节；'\
              '位平面数：',self.biPlanes,'；颜色位数：',self.biBitCount,'；是否压缩：',self.biCompression,\
              '；实际位图数据占用的字节数：',self.biSizeImage,'；目标设备水平分辨率：',self.biXPelsPerMeter,\
              '；目标设备垂直分辨率：',self.biYPelsPerMeter,'；实际使用的颜色数：',self.biClrUsed,'；图像中重要的颜色数：',self.biClrImportant
        # res = '位图文件头：\n文件类型：' + str(self.bfType) + '；文件大小：' + str(self.bfSize) + '字节；保留字1：' + str(self.bfReserved1) + \
        #       '；保留字2：' + self.bfReserved2 + '；偏移字节数：' + self.bfOffBits + '字节；\n位图信息头：\n' + \
        #       '结构长度：' + self.bfSize + '字节；图像宽度：' + self.biWidth + '字节；图像高度：' + self.biHeight + '字节；' \
        #                                                                                        '位平面数：' + self.biPlanes + '；颜色位数：' + self.biBitCount + '；是否压缩：' + self.biCompression + \
        #       '；实际位图数据占用的字节数：' + self.biSizeImage + '；目标设备水平分辨率：' + self.biXPelsPerMeter + \
        #       '；目标设备垂直分辨率：' + self.biYPelsPerMeter + '；实际使用的颜色数：' + self.biClrUsed + '；图像中重要的颜色数：' + self.biClrImportant
        return res

    #显示图像
    def showImg(self):
        # cv2.imshow("lena.bmp",self.img)
        # cv2.waitKey(0)
        plt.title("lena")
        plt.imshow(self.img)
        plt.show()


    #灰度化
    def greying(self):
        ###          用opencv解决灰度化           #####
        # img = cv2.imread("lena.BMP", cv2.IMREAD_COLOR)
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度化
        # cv2.imshow("gray", gray)
        # cv2.waitKey(0)

        ####           手动写                  ######
        picTemp = copy.deepcopy(self)
        for m in range(0,self.biHeight):
            for n in range(0,self.biWidth):
                avg = self.img[self.biHeight - m - 1, n][0]*0.299 + self.img[self.biHeight - m - 1, n][1]*0.587+self.img[self.biHeight - m - 1, n][2]*0.114
                avg = int(avg)
                picTemp.img[self.biHeight - m - 1, n][0] = avg
                picTemp.img[self.biHeight - m - 1, n][1] = avg
                picTemp.img[self.biHeight - m - 1, n][2] = avg
        return picTemp

    # 平移
    def translate(self,dx, dy):
        h = self.biHeight  # 图片行数等于高
        w = self.biWidth  # 图片列数等于宽
        nh = h + abs(dy)
        nw = w + abs(dx)
        dst = np.zeros(shape=[self.biHeight, self.biWidth, 4], dtype=int)
        for dw in range(w):
            for dh in range(h):
                nX = dw + dx
                nY = dh + dy
                if nX >= dst.shape[1] or nX < 0 or nY >= dst.shape[0] or nY < 0:
                    continue
                else:
                    dst[nY, nX] = self.img[dh, dw]
        return dst

    #填充后的平移
    def translate2(self,dx, dy):
        h = self.biHeight  # 图片行数等于高
        w = self.biWidth  # 图片列数等于宽
        nh = h + abs(dy)
        nw = w + abs(dx)
        dst = np.zeros(shape=[nh, nw, 4], dtype=int)
        for dw in range(w):
            for dh in range(h):
                nX = dw + dx
                nY = dh + dy
                dst[nY, nX] = self.img[dh, dw]
        return dst


    #图像镜像
    #图像垂直镜像
    def flip_verti(self):
        h = self.biHeight  # 图片行数等于高
        w = self.biWidth  # 图片列数等于宽
        dst = np.empty(shape=[h, w, 4], dtype=int)
        for dw in range(w):
            for dh in range(h):
                dst[w-1-dw][dh] = self.img[dw][dh]
        return dst

    #图像水平镜像
    def flip_hori(self):
        h = self.biHeight  # 图片行数等于高
        w = self.biWidth  # 图片列数等于宽
        dst = np.zeros(shape=[h, w, 4], dtype=int)
        for dw in range(w):
            for dh in range(h):
                dst[dw][h-1-dh] = self.img[dw][dh]
        return dst


    #图像缩放
    def resize(self,sx=1, sy=1):
        height, width = self.biHeight, self.biWidth
        output_h = round(height * sx)
        output_w = round(width * sy)
        dst = np.zeros((output_h, output_w, 4), dtype=int)

        for i in range(output_h):
            for j in range(output_w):
                dst[i, j] = self.img[round((i + 1) / sx - 1), round((j + 1) / sy - 1)]
        return dst






filePath = "pic/lena.BMP"
pic = BMP(filePath)
#设置中文
plt.rcParams['font.sans-serif'] = ['SimHei']

#print(pic.getShuxing())

#灰度化
# pic.showImg()
# pic.greying().showImg()

# #平移
# dst = pic.translate(100,20)
# plt.title("平移")
# plt.imshow(dst)
# plt.show()
# #填充后的平移
# dst = pic.translate2(100,20)
# plt.title("平移（填充后）")
# plt.imshow(dst)
# plt.show()

# #垂直镜像
# dst = pic.flip_verti()
# plt.title("垂直镜像")
# plt.imshow(dst)
# plt.show()
# #水平镜像
# dst = pic.flip_hori()
# plt.title("水平镜像")
# plt.imshow(dst)
# plt.show()

# #缩放
# dst = pic.resize(2,2)
# plt.title("缩放")
# plt.imshow(dst)
# plt.show()

