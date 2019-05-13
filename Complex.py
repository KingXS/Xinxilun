# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Complex.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Complex(object):
    def setupUi(self, Complex):
        Complex.setObjectName("Complex")
        Complex.resize(642, 569)
        self.label = QtWidgets.QLabel(Complex)
        self.label.setGeometry(QtCore.QRect(190, 30, 381, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Complex)
        self.pushButton.setGeometry(QtCore.QRect(190, 180, 251, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Complex)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 100, 251, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Complex)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 270, 251, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Complex)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 350, 251, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Complex)
        self.pushButton_5.setGeometry(QtCore.QRect(190, 430, 251, 51))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Complex)
        QtCore.QMetaObject.connectSlotsByName(Complex)

    def retranslateUi(self, Complex):
        _translate = QtCore.QCoreApplication.translate
        Complex.setWindowTitle(_translate("Complex", "综合编码"))
        self.label.setText(_translate("Complex", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; font-style:italic; color:#00aaff;\">综合编码模块</span></p></body></html>"))
        self.pushButton.setText(_translate("Complex", "哈夫曼编码"))
        self.pushButton_2.setText(_translate("Complex", "游程编码"))
        self.pushButton_3.setText(_translate("Complex", "加密编码"))
        self.pushButton_4.setText(_translate("Complex", "信道编码"))
        self.pushButton_5.setText(_translate("Complex", "译码"))

