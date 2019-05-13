# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XindaoRL.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_XindaoRL(object):
    def setupUi(self, XindaoRL):
        XindaoRL.setObjectName("XindaoRL")
        XindaoRL.resize(790, 477)
        self.label = QtWidgets.QLabel(XindaoRL)
        self.label.setGeometry(QtCore.QRect(200, 0, 411, 131))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(XindaoRL)
        self.pushButton.setGeometry(QtCore.QRect(140, 150, 211, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(XindaoRL)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 150, 201, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(XindaoRL)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 300, 211, 71))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(XindaoRL)
        QtCore.QMetaObject.connectSlotsByName(XindaoRL)

    def retranslateUi(self, XindaoRL):
        _translate = QtCore.QCoreApplication.translate
        XindaoRL.setWindowTitle(_translate("XindaoRL", "信道容量迭代计算"))
        self.label.setText(_translate("XindaoRL", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; font-style:italic; color:#00aaff;\">信道容量迭代计算</span></p></body></html>"))
        self.pushButton.setText(_translate("XindaoRL", "请选择信道存储文本"))
        self.pushButton_2.setText(_translate("XindaoRL", "请选择计算结果存储文本"))
        self.pushButton_3.setText(_translate("XindaoRL", "开始计算"))




