# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        font = QtGui.QFont()
        font.setPointSize(15)
        Form.setFont(font)
        self.btnreload = QtWidgets.QPushButton(Form)
        self.btnreload.setGeometry(QtCore.QRect(760, 80, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnreload.setFont(font)
        self.btnreload.setObjectName("btnreload")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(450, 240, 500, 500))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(-5, 70, 381, 731))
        self.treeWidget.setObjectName("treeWidget")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(-3, 59, 1051, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lblX = QtWidgets.QLabel(Form)
        self.lblX.setGeometry(QtCore.QRect(440, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.lblX.setFont(font)
        self.lblX.setObjectName("lblX")
        self.lblY = QtWidgets.QLabel(Form)
        self.lblY.setGeometry(QtCore.QRect(630, 160, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.lblY.setFont(font)
        self.lblY.setObjectName("lblY")
        self.txtX = QtWidgets.QTextEdit(Form)
        self.txtX.setGeometry(QtCore.QRect(480, 150, 111, 51))
        self.txtX.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtX.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtX.setObjectName("txtX")
        self.txtY = QtWidgets.QTextEdit(Form)
        self.txtY.setGeometry(QtCore.QRect(680, 150, 111, 51))
        self.txtY.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtY.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtY.setObjectName("txtY")
        self.btnOK = QtWidgets.QPushButton(Form)
        self.btnOK.setGeometry(QtCore.QRect(860, 150, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.btnOK.setFont(font)
        self.btnOK.setObjectName("btnOK")
        self.lbl = QtWidgets.QLabel(Form)
        self.lbl.setGeometry(QtCore.QRect(410, 90, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl.setFont(font)
        self.lbl.setObjectName("lbl")
        self.lblbk = QtWidgets.QLabel(Form)
        self.lblbk.setGeometry(QtCore.QRect(3, 1, 1011, 811))
        self.lblbk.setText("")
        self.lblbk.setObjectName("lblbk")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(440, 10, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lblbk.raise_()
        self.btnreload.raise_()
        self.label.raise_()
        self.treeWidget.raise_()
        self.line.raise_()
        self.lblX.raise_()
        self.lblY.raise_()
        self.txtX.raise_()
        self.txtY.raise_()
        self.btnOK.raise_()
        self.lbl.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)
        self.btnreload.clicked.connect(Form.btnreload_Click)
        self.btnOK.clicked.connect(Form.btnOK_Click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnreload.setText(_translate("Form", "??????????????????"))
        self.lblX.setText(_translate("Form", "X:"))
        self.lblY.setText(_translate("Form", "Y:"))
        self.btnOK.setText(_translate("Form", "OK"))
        self.lbl.setText(_translate("Form", "?????????????????????????????????"))
        self.label_2.setText(_translate("Form", "??????????????????"))
