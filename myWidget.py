import sys

import cv2
import matplotlib
from PIL.Image import Image
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from matplotlib import pyplot as plt
from pyqt5_plugins.examplebuttonplugin import QtGui

from BMPClass import BMP
from filter import mean_filter, median_filter
from myEqualization_histogram import myMain
from widget import Ui_Form

class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):

        self.filepath = 'pic//lena.BMP'
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)

        bk = QPixmap('pic/background.jpg')
        self.lblbk.setPixmap(bk)
        self.lblbk.setScaledContents(True)

        # treeWidget
        self.treeWidget.setColumnCount(1)   # 设置列数
        self.treeWidget.setHeaderLabel("数字图像处理实验")     #设置头的标题
        self.treeWidget.setHeaderHidden(True)
        #self.treeWidget.setFixedSize(14)
        self.treeWidget.setFont(QFont("wenquanyi",13))
        # self.treeWidget.setWindowOpacity(1)
        # self.treeWidget.setAttribute()
        #self.treeWidget.setStyleSheet("#treeWidget{background-image:url(pic/background.jpg)}")
        self.treeWidget.setStyleSheet("#treeWidget{background-color: rgba(255, 255, 255,0.5)}")

        root1 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        root1.setText(0, '1 BMP位图显示与属性')
        child1 = QtWidgets.QTreeWidgetItem(root1)
        child1.setText(0,'1.1 位图属性')
        child2 = QtWidgets.QTreeWidgetItem(root1)
        child2.setText(0, '1.2 位图显示')

        root2 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        root2.setText(0, '2 图像的灰度化')
        child3 = QtWidgets.QTreeWidgetItem(root2)
        child3.setText(0, '2.1 灰度化')

        root3 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        root3.setText(0, '3 图像的几何变换')
        child4 = QtWidgets.QTreeWidgetItem(root3)
        child4.setText(0, '3.1 图像平移（不填充）')
        child5 = QtWidgets.QTreeWidgetItem(root3)
        child5.setText(0, '3.2 图像平移（填充）')
        child6 = QtWidgets.QTreeWidgetItem(root3)
        child6.setText(0, '3.3 图像垂直镜像')
        child7 = QtWidgets.QTreeWidgetItem(root3)
        child7.setText(0, '3.4 图像水平镜像')
        child8 = QtWidgets.QTreeWidgetItem(root3)
        child8.setText(0, '3.5 图像缩放')

        root4 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        root4.setText(0, '4 灰度直方图')
        child9 = QtWidgets.QTreeWidgetItem(root4)
        child9.setText(0, '4.1 灰度直方图均衡化')

        root5 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        root5.setText(0, '5 滤波器')
        child10 = QtWidgets.QTreeWidgetItem(root5)
        child10.setText(0, '5.1 均值滤波器')
        child11 = QtWidgets.QTreeWidgetItem(root5)
        child11.setText(0, '5.2 中值滤波器')

        self.treeWidget.expandAll()     #展开
        self.treeWidget.clicked.connect(self.onTreeClicked)

        self.lbl.setVisible(False)
        self.lblX.setVisible(False)
        self.lblY.setVisible(False)
        self.txtX.setVisible(False)
        self.txtY.setVisible(False)
        self.btnOK.setVisible(False)




    def btnreload_Click(self):
        self.filepath, imgType = QFileDialog.getOpenFileName(self, "打开图片", "","*.bmp")
                                                      # "*.bmp;;*.jpg;;*.png;;All Files(*)")  # 弹出一个文件选择框，第一个返回值imgName记录选中的文件路径+文件名，第二个返回值imgType记录文件的类型
        print(imgType)
        src = QPixmap(self.filepath)#.scaled(self.label.width(),self.label.height())  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长款
        self.label.setPixmap(src)  # 在label控件上显示选择的图片
        self.label.setScaledContents(True)  # 是否将缩放其内容以填充所有可用空间


    def onTreeClicked(self):
        self.label.setGeometry(450, 260, 500, 500)
        self.lbl.setVisible(False)
        self.lblX.setVisible(False)
        self.lblY.setVisible(False)
        self.txtX.setVisible(False)
        self.txtY.setVisible(False)
        self.btnOK.setVisible(False)

        pix = QPixmap(self.filepath)
        pic = BMP(self.filepath)
        item = self.treeWidget.currentItem()

        if item.text(0) == "1.1 位图属性":
            self.label.setText(str(pic.getShuxing()))
            self.label.setWordWrap(True)
        elif item.text(0) == "1.2 位图显示":
            #self.label.setGeometry(450, 260, 500, 500)
            self.label.setPixmap(pix)
            #self.label.setStyleSheet("border: 2px solid red")
            self.label.setScaledContents(True)  #是否将缩放其内容以填充所有可用空间
        elif item.text(0) == "2.1 灰度化":
            img = pic.greying().img
            # numpy类型转QPixmap
            img = img.astype("uint8")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap(img))
            self.label.setScaledContents(True)  # 是否将缩放其内容以填充所有可用空间
        elif item.text(0) == "3.1 图像平移（不填充）":
            # 默认显示原图
            self.label.setPixmap(pix)
            self.label.setScaledContents(True)  # 是否将缩放其内容以填充所有可用空间
            #显示组件
            self.lbl.setText("需要平移的像素偏移量：")
            self.txtX.setText("0")
            self.txtY.setText("0")
            self.lbl.setVisible(True)
            self.lblX.setVisible(True)
            self.lblY.setVisible(True)
            self.txtX.setVisible(True)
            self.txtY.setVisible(True)
            self.btnOK.setVisible(True)
        elif item.text(0) == "3.2 图像平移（填充）":
            # 默认显示原图
            self.label.setPixmap(pix)
            self.label.setScaledContents(True)  # 是否将缩放其内容以填充所有可用空间
            # 显示组件
            self.lbl.setText("需要平移的像素偏移量：")
            self.txtX.setText("0")
            self.txtY.setText("0")
            self.lbl.setVisible(True)
            self.lblX.setVisible(True)
            self.lblY.setVisible(True)
            self.txtX.setVisible(True)
            self.txtY.setVisible(True)
            self.btnOK.setVisible(True)
        elif item.text(0) == "3.3 图像垂直镜像":
            img = pic.flip_verti()
            # numpy类型转QPixmap
            img = img.astype("uint8")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap(img))
            self.label.setScaledContents(True)  # 是否将缩放其内容以填充所有可用空间
        elif item.text(0) == "3.4 图像水平镜像":
            img = pic.flip_hori()
            # numpy类型转QPixmap
            img = img.astype("uint8")
            # im = Image.fromarray(img)
            # img = im.toqpixmap()
            # self.label.setPixmap(img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap(img))
            self.label.setScaledContents(True)  # 是否将缩放其内容以填充所有可用空间
        elif item.text(0) == "3.5 图像缩放":
            # 默认显示原图
            self.label.setPixmap(pix)
            self.label.setScaledContents(True)  # 是否将缩放其内容以填充所有可用空间
            # 显示组件
            self.lbl.setText("需要缩放的倍数：")
            self.txtX.setText("1")
            self.txtY.setText("1")
            self.lbl.setVisible(True)
            self.lblX.setVisible(True)
            self.lblY.setVisible(True)
            self.txtX.setVisible(True)
            self.txtY.setVisible(True)
            self.btnOK.setVisible(True)
        elif item.text(0) == '4.1 灰度直方图均衡化':
            img = myMain(self.filepath)
            img = img.astype("uint8")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap(img))
            self.label.setScaledContents(True)
        elif item.text(0) == '5.1 均值滤波器':
            img = mean_filter(self.filepath)
            img = img.astype("uint8")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap(img))
            self.label.setScaledContents(True)
        elif item.text(0) == '5.2 中值滤波器':
            img = median_filter(self.filepath)
            img = img.astype("uint8")
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap(img))
            self.label.setScaledContents(True)



    def btnOK_Click(self):
        self.label.setGeometry(450, 260, 500, 500)
        pix = QPixmap(self.filepath)
        pic = BMP(self.filepath)
        item = self.treeWidget.currentItem()
        x = self.txtX.toPlainText().split()
        y = self.txtY.toPlainText().split()
        x = "".join(str(i) for i in x)  # 去掉列表外的方括号
        y = "".join(str(i) for i in y)  # 去掉列表外的方括号
        # print(x)
        # print(y)
        try:
            x_int = float(x)
            y_int = float(y)
        except:
            msg_box = QMessageBox(QMessageBox.Warning, 'ERROR', '输入不合法！')
            msg_box.exec_()
        else:
            if item.text(0) == "3.1 图像平移（不填充）":
                x_int = int(x_int)
                y_int = int(y_int)
                img = pic.translate(x_int,y_int)
                img = img.astype("uint8")
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
                self.label.setPixmap(QtGui.QPixmap(img))
                self.label.setScaledContents(True)  # 是否将缩放其内容以填充所有可用空间
            elif item.text(0) == '3.2 图像平移（填充）':
                x_int = int(x_int)
                y_int = int(y_int)
                img = pic.translate2(x_int, y_int)
                img = img.astype("uint8")
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
                self.label.setPixmap(QtGui.QPixmap(img))
                self.label.setScaledContents(True)  # 是否将缩放其内容以填充所有可用空间
            elif item.text(0) == '3.5 图像缩放':
                img = pic.resize(x_int,y_int)
                self.label.setGeometry(450, 260, round(500 * x_int), round(500 * y_int))
                img = img.astype("uint8")
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = QtGui.QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
                self.label.setPixmap(QtGui.QPixmap(img))
                self.label.setScaledContents(True)  # 是否将缩放其内容以填充所有可用空间
            #matplotlib.use('Agg')




if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.setWindowIcon(QIcon('pic/qq.bmp'))
    my_pyqt_form.setObjectName("202000800118陈香君")
    #my_pyqt_form.setStyleSheet("#wkWgt {border-image:url(D:\python\DigitalImageProcessing\pic)}")
    my_pyqt_form.show()
    sys.exit(app.exec_())
