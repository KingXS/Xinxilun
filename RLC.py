# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RLC.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RLC(object):
    def setupUi(self, RLC):
        RLC.setObjectName("RLC")
        RLC.resize(642, 453)
        self.label = QtWidgets.QLabel(RLC)
        self.label.setGeometry(QtCore.QRect(220, 30, 381, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(RLC)
        self.pushButton.setGeometry(QtCore.QRect(50, 120, 221, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(RLC)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 120, 221, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(RLC)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 310, 221, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(RLC)
        QtCore.QMetaObject.connectSlotsByName(RLC)

    def retranslateUi(self, RLC):
        _translate = QtCore.QCoreApplication.translate
        RLC.setWindowTitle(_translate("RLC", "游程编码"))
        self.label.setText(_translate("RLC", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; font-style:italic; color:#00aaff;\">游程编码</span></p></body></html>"))
        self.pushButton.setText(_translate("RLC", "请选择编码文件"))
        self.pushButton_2.setText(_translate("RLC", "请选择保存文件"))
        self.pushButton_3.setText(_translate("RLC", "开始编码"))

