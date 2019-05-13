# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LZW_OUT.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_LZW_OUT(object):
    def setupUi(self, LZW_OUT):
        LZW_OUT.setObjectName("LZW_OUT")
        LZW_OUT.resize(770, 481)
        self.label = QtWidgets.QLabel(LZW_OUT)
        self.label.setGeometry(QtCore.QRect(280, 20, 211, 71))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(LZW_OUT)
        self.pushButton.setGeometry(QtCore.QRect(110, 140, 201, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(LZW_OUT)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 140, 201, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(LZW_OUT)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 290, 201, 71))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(LZW_OUT)
        QtCore.QMetaObject.connectSlotsByName(LZW_OUT)

    def retranslateUi(self, LZW_OUT):
        _translate = QtCore.QCoreApplication.translate
        LZW_OUT.setWindowTitle(_translate("LZW_OUT", "LZW_OUT"))
        self.label.setText(_translate("LZW_OUT", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; font-style:italic; color:#00aaff;\">LZW译码</span></p></body></html>"))
        self.pushButton.setText(_translate("LZW_OUT", "请选择译码文件"))
        self.pushButton_2.setText(_translate("LZW_OUT", "请选择存储文件"))
        self.pushButton_3.setText(_translate("LZW_OUT", "开始译码"))

