# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LZW_IN.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(648, 448)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 10, 301, 81))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 130, 181, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 130, 181, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 280, 181, 61))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LZW_IN"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; font-style:italic; color:#00aaff;\">LZW编码</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "请选择编码文件"))
        self.pushButton_2.setText(_translate("Form", "请选择存储文件"))
        self.pushButton_3.setText(_translate("Form", "开始编码"))



