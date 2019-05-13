# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Huffman.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Huffman(object):
    def setupUi(self, Huffman):
        Huffman.setObjectName("Huffman")
        Huffman.resize(642, 453)
        self.label = QtWidgets.QLabel(Huffman)
        self.label.setGeometry(QtCore.QRect(190, 30, 381, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Huffman)
        self.pushButton.setGeometry(QtCore.QRect(50, 120, 221, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Huffman)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 120, 221, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Huffman)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 310, 221, 51))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Huffman)
        QtCore.QMetaObject.connectSlotsByName(Huffman)

    def retranslateUi(self, Huffman):
        _translate = QtCore.QCoreApplication.translate
        Huffman.setWindowTitle(_translate("Huffman", "哈夫曼编码"))
        self.label.setText(_translate("Huffman", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; font-style:italic; color:#00aaff;\">哈夫曼编码</span></p></body></html>"))
        self.pushButton.setText(_translate("Huffman", "请选择编码文件"))
        self.pushButton_2.setText(_translate("Huffman", "请选择保存文件"))
        self.pushButton_3.setText(_translate("Huffman", "开始编码"))

