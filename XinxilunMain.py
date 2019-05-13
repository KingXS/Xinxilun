# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XinxilunMain.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Zhuchuangko(object):
    def setupUi(self, Zhuchuangko):
        Zhuchuangko.setObjectName("Zhuchuangko")
        Zhuchuangko.resize(969, 748)
        Zhuchuangko.setStyleSheet("")
        self.label = QtWidgets.QLabel(Zhuchuangko)
        self.label.setGeometry(QtCore.QRect(130, 70, 711, 111))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Zhuchuangko)
        self.label_2.setGeometry(QtCore.QRect(260, 200, 471, 71))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Zhuchuangko)
        self.label_3.setGeometry(QtCore.QRect(330, 280, 291, 101))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Zhuchuangko)
        self.pushButton.setGeometry(QtCore.QRect(90, 550, 201, 101))
        self.pushButton.setStyleSheet("color:rgb(0, 170, 255);\n"
"font: 12pt \"隶书\";\n"
"\n"
"\n"
"")
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Zhuchuangko)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 550, 201, 101))
        self.pushButton_2.setStyleSheet("color:rgb(0, 170, 255);\n"
"font: 12pt \"隶书\";")
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Zhuchuangko)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 550, 201, 101))
        self.pushButton_3.setStyleSheet("color:rgb(0, 170, 255);\n"
"font: 12pt \"隶书\";")
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Zhuchuangko)
        self.label_4.setGeometry(QtCore.QRect(370, 310, 471, 71))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Zhuchuangko)
        QtCore.QMetaObject.connectSlotsByName(Zhuchuangko)

    def retranslateUi(self, Zhuchuangko):
        _translate = QtCore.QCoreApplication.translate
        Zhuchuangko.setWindowTitle(_translate("Zhuchuangko", "信息论课程设计"))
        self.label.setText(_translate("Zhuchuangko", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; font-style:italic; color:#00aaff;\">信息论课程设计</span></p></body></html>"))
        self.label_2.setText(_translate("Zhuchuangko", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("Zhuchuangko", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#00aaff;\">请选择你要操作的模块</span></p></body></html>"))
        self.pushButton.setToolTip(_translate("Zhuchuangko", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setWhatsThis(_translate("Zhuchuangko", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("Zhuchuangko", "LZW编码译码"))
        self.pushButton_2.setToolTip(_translate("Zhuchuangko", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_2.setWhatsThis(_translate("Zhuchuangko", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("Zhuchuangko", "信道容量迭代计算"))
        self.pushButton_3.setToolTip(_translate("Zhuchuangko", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_3.setWhatsThis(_translate("Zhuchuangko", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_3.setText(_translate("Zhuchuangko", "综合编码"))
        self.label_4.setText(_translate("Zhuchuangko", "<html><head/><body><p><br/></p></body></html>"))

