# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LZW.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_FORM_LZW(object):
    def setupUi(self, FORM_LZW):
        FORM_LZW.setObjectName("FORM_LZW")
        FORM_LZW.resize(642, 453)
        self.label = QtWidgets.QLabel(FORM_LZW)
        self.label.setGeometry(QtCore.QRect(240, 30, 381, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(FORM_LZW)
        self.pushButton.setGeometry(QtCore.QRect(200, 140, 251, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(FORM_LZW)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 270, 251, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(FORM_LZW)
        QtCore.QMetaObject.connectSlotsByName(FORM_LZW)

    def retranslateUi(self, FORM_LZW):
        _translate = QtCore.QCoreApplication.translate
        FORM_LZW.setWindowTitle(_translate("FORM_LZW", "LZW"))
        self.label.setText(_translate("FORM_LZW", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; font-style:italic; color:#00aaff;\">LZW模块</span></p></body></html>"))
        self.pushButton.setText(_translate("FORM_LZW", "编码"))
        self.pushButton_2.setText(_translate("FORM_LZW", "译码"))

