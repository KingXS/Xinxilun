# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EXOR.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EXOR(object):
    def setupUi(self, EXOR):
        EXOR.setObjectName("EXOR")
        EXOR.resize(648, 448)
        self.label = QtWidgets.QLabel(EXOR)
        self.label.setGeometry(QtCore.QRect(210, 20, 301, 81))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(EXOR)
        self.pushButton.setGeometry(QtCore.QRect(80, 130, 181, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(EXOR)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 130, 181, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(EXOR)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 280, 181, 61))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(EXOR)
        QtCore.QMetaObject.connectSlotsByName(EXOR)

    def retranslateUi(self, EXOR):
        _translate = QtCore.QCoreApplication.translate
        EXOR.setWindowTitle(_translate("EXOR", "加密编码"))
        self.label.setText(_translate("EXOR", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; font-style:italic; color:#00aaff;\">加密编码</span></p></body></html>"))
        self.pushButton.setText(_translate("EXOR", "请选择编码文件"))
        self.pushButton_2.setText(_translate("EXOR", "请选择存储文件"))
        self.pushButton_3.setText(_translate("EXOR", "开始编码"))

