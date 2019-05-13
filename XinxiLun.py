from PyQt5 import QtCore, QtGui, QtWidgets
from XinxilunMain import Ui_Zhuchuangko
from LZW import Ui_FORM_LZW
from LZW_IN import Ui_Form
from LZW_OUT import Ui_LZW_OUT
from XindaoRL import Ui_XindaoRL
from Complex import Ui_Complex      #应用综合编码窗口
from Huffman import Ui_Huffman
from RLC import Ui_RLC      #引用RLC编码窗口
from Huffman_Node import Node
from Huffman_en import Huffman_encoding     #引入霍夫曼编码模块
from PyQt5.QtWidgets import *
from LZW_Coding import LZW_coding      #引用编码模块
from LZW_decoding import lzw_decoding    #引用信道译码模块
from txt_to_array import txt_to_arr    #引用文本转换矩阵的模块
from Xindao_2 import Xindaorl1       #引用信道容量计算模块

from EXOR import Ui_EXOR
from RLC_2 import RLC
import sys
import os
import math

#定义全局变量保存输入输出的地址
filename_lzw_in_in=""
filename_lzw_in_out=""
result_coding=""        #用于保存编码结果
#用于保存LZW译码的结果
filename_lzw_out_in=""
filename_lzw_out_out=""
#用于保存信道容量计算的文件输入输出地址
filename_XindaoRL_in=""
filename_XindaoRL_out=""
#用于保存哈夫曼编码的文件输入输出地址
filename_Huffman_in=""
filename_Huffman_out=""
#定义RLC编码窗口
filename_RLC_in=""
filename_RLC_out=""
#用于保存加密编码的输入输出地址
filename_EXOR_in=""
filename_EXOR_out=""
     #定义一个编码对象


#重载各个子窗口
#重载主窗口
class new_XinxilunMain(QtWidgets.QWidget, Ui_Zhuchuangko):
    def __init__(self):
        super(new_XinxilunMain,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Appear_LZW)
        self.pushButton_2.clicked.connect(self.Appear_XindaoRL)
        self.pushButton_3.clicked.connect(self.Appear_Complex)

    #点击按钮出现LZW译码窗口
    def Appear_LZW(self):
        LZW1.show()

    #点击按钮出现信道容量计算窗口
    def Appear_XindaoRL(self):
        XindaoRL.show()

    def Appear_Complex(self):
        Complex.show()


#重载LZW窗口
class new_LZW(QtWidgets.QWidget, Ui_FORM_LZW):
    def __init__(self):
        super(new_LZW,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Appear_LZW_IN)     #点击这个按钮出现信道编码窗口
        self.pushButton_2.clicked.connect(self.Appear_LZW_OUT)  # 点击这个按钮出现信道译码窗口

    #点击按钮，出现信道编码窗口
    def Appear_LZW_IN(self):
        LZW_IN.show()


    def Appear_LZW_OUT(self):
        LZW_OUT.show()


#重载LZW_IN窗口
class new_LZW_IN(QtWidgets.QWidget, Ui_Form):
    # 用于保存LZW编码的地址



    def __init__(self):
        super(new_LZW_IN,self).__init__()
        self.setupUi(self)
        #filename1=""     #用于保存需要进行数据输入的文件
        #filename2=""      #用于保存需要进行数据存放的文件
        self.pushButton.clicked.connect(self.Choose_txt_in)           #点击此按钮，选择要进行数据输入的窗口
        self.pushButton_2.clicked.connect(self.Choose_txt_out)         #选择此窗口，选择需要保存结果的窗口
        self.pushButton_3.clicked.connect(self.Start_coding)

    def Choose_txt_in(self,event):
        global filename_lzw_in_in
        filename_lzw_in_in, selectedfilter1 = QFileDialog.getOpenFileName(
            self, ("标题"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )

        print(type(filename_lzw_in_in))

    def Choose_txt_out(self,event):
        global filename_lzw_in_out
        filename_lzw_in_out, selectedfilter2 = QFileDialog.getOpenFileName(
            self, ("标题"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )

        print(filename_lzw_in_out)

    def Start_coding(self):
        global filename_lzw_in_in
        global filename_lzw_in_out
        global result_coding
#        print("1")
#        print(filename_lzw_in_out)
        out = open(filename_lzw_in_out, "r+")  # 用于保存结果
#        print(filename_lzw_in_in)
#        print("1"
        k = LZW_coding
        x = k.lzw_in(k,filename_lzw_in_in,filename_lzw_in_out)
        reply = QMessageBox.information(self,
                                         "结果",
                                         "编码成功！！",
                                          QMessageBox.Yes | QMessageBox.No)




        #重载LZW_OUT窗口
class new_LZW_OUT(QtWidgets.QWidget, Ui_LZW_OUT):
    def __init__(self):
        super(new_LZW_OUT,self).__init__()
        self.setupUi(self)
#定义要进行的操作
        self.pushButton.clicked.connect(self.Choose_txt_in)  # 点击此按钮，选择要进行数据输入的窗口
        self.pushButton_2.clicked.connect(self.Choose_txt_out)  # 选择此窗口，选择需要保存结果的窗口
        self.pushButton_3.clicked.connect(self.Start_decoding)


    def Choose_txt_in(self,event):
        global filename_lzw_out_in
        filename_lzw_out_in, selectedfilter1 = QFileDialog.getOpenFileName(
            self, ("标题"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )

        print(type(filename_lzw_out_in))

    def Choose_txt_out(self,event):
        global filename_lzw_out_out
        filename_lzw_out_out, selectedfilter2 = QFileDialog.getOpenFileName(
            self, ("标题"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )

        print(filename_lzw_out_out)

    def Start_decoding(self):
        global filename_lzw_out_in
        global filename_lzw_out_out
        print(filename_lzw_out_in)
        print(filename_lzw_out_out)
        decoding = lzw_decoding
        decoding.lzw_out1(decoding, filename_lzw_out_in, filename_lzw_out_out)
        reply = QMessageBox.information(self,
                                          "结果",
                                         "译码成功！！",
                                         QMessageBox.Yes | QMessageBox.No)


#重载XindaoRL窗口
class new_XindaoRL(QtWidgets.QWidget, Ui_XindaoRL):
    def __init__(self):
        super(new_XindaoRL,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Choose_txt_in)
        self.pushButton_2.clicked.connect(self.Choose_txt_out)
        self.pushButton_3.clicked.connect(self.Start_calculate)

    #打开要进行计算的文本
    def Choose_txt_in(self,event):
        global filename_XindaoRL_in
        filename_XindaoRL_in, selectedfilter2 = QFileDialog.getOpenFileName(
            self, ("标题"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )
        print(filename_XindaoRL_in)

    #选择要把文件存到什么地方
    def Choose_txt_out(self,event):
        global filename_XindaoRL_out
        filename_XindaoRL_out, selectedfilter2 = QFileDialog.getOpenFileName(
            self, ("标题"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )
        print(filename_XindaoRL_out)


    #开始计算信道容量
    def Start_calculate(self):
        #引用存放全局变量的数组
        global filename_XindaoRL_in
        global filename_XindaoRL_out
        print(filename_XindaoRL_in,filename_XindaoRL_out)
        #从文本中得到数组
        TTA = txt_to_arr
        channel1 = TTA.txt_to(TTA, filename_XindaoRL_in)
        length = len(channel1)
        print(length)
        print("1")
        for i in range(length):
            channel = channel1[i][:][:]
            # 开始计算
            Xin = Xindaorl1
            Xin.xindaorl(Xin, channel, filename_XindaoRL_out)

        reply = QMessageBox.information(self,
                                        "结果",
                                        "计算成功！！",
                                        QMessageBox.Yes | QMessageBox.No)

#重载综合编码窗口
class new_Complex(QtWidgets.QWidget, Ui_Complex):
    def __init__(self):
        super(new_Complex,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Appear_Huffman)      #哈夫曼编码
        self.pushButton_2.clicked.connect(self.Appear_RLC)     #游程编码
        self.pushButton_3.clicked.connect(self.Appear_EXOR)  # 加密编码

    #哈夫曼编码
    def Appear_Huffman(self):
        Huffman.show()

    #游程编码
    def Appear_RLC(self):
        RLC1.show()

    def Appear_EXOR(self):
        Exor.show()


class new_Huffman(QtWidgets.QWidget, Ui_Huffman):
    def __init__(self):
        super(new_Huffman,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Choose_txt_in)
        self.pushButton_2.clicked.connect(self.Choose_txt_out)
        self.pushButton_3.clicked.connect(self.Start_coding)

    def Choose_txt_in(self):
        global filename_Huffman_in
        filename_Huffman_in, selectedfilter2 = QFileDialog.getOpenFileName(
            self, ("标题"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )


    def Choose_txt_out(self):
        global filename_Huffman_out
        filename_Huffman_out, selectedfilter2 = QFileDialog.getOpenFileName(
            self, ("标题"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )

    def Start_coding(self):
        global filename_Huffman_in
        global filename_Huffman_out
        huff = Huffman_encoding
        huff.start_encoding(huff, filename_Huffman_in, filename_Huffman_out)
        reply = QMessageBox.information(self,
                                        "结果",
                                        "计算成功！！",
                                        QMessageBox.Yes | QMessageBox.No)


class new_EXOR(QtWidgets.QWidget, Ui_EXOR):
    def __init__(self):
        super(new_EXOR,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Choose_txt_in)
        self.pushButton_2.clicked.connect(self.Choose_txt_out)
        self.pushButton_3.clicked.connect(self.Start_coding)

    def Choose_txt_in(self):
        global filename_EXOR_in
        filename_EXOR_in, selectedfilter2 = QFileDialog.getOpenFileName(
            self, ("请选择加密编码文件"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )


    def Choose_txt_out(self):
        global filename_EXOR_out
        filename_EXOR_out, selectedfilter2 = QFileDialog.getOpenFileName(
            self, ("请选择加密编码存储文件"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )


    def Start_coding(self):
        global filename_EXOR_in
        global filename_EXOR_out
        print(filename_EXOR_in,filename_EXOR_out)
        S_in = open(filename_EXOR_in)
        S_out = open(filename_EXOR_out, "a")
        #开始编码
        p = 0
        EX = S_in.readlines()
   #     print(EX)
        len_EX1 = len(EX)
  #      print(len_EX1)
    #    print(EX[len_EX1 - 1])
        len_EX = len(EX[len_EX1 - 1])
 #       print(len_EX)
        EXp = [0 for i in range(len_EX)]
        for i in EX[len_EX1 - 1]:
            EXp[p] = int(i)
            p += 1
#        print(EXp)

 #       print(len(EXp))
        for i in range(len(EXp)):
            EXp.append(EXp.pop(1))
        S_out.writelines("加密操作之后：")
        for i in range(len(EXp)):
            S_out.writelines(str(EXp[i]))

        reply = QMessageBox.information(self,
                                        "加密编码结果",
                                        "计算成功！！",
                                        QMessageBox.Yes | QMessageBox.No)



class new_RLC(QtWidgets.QWidget, Ui_RLC):
    def __init__(self):
        super(new_RLC,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Choose_txt_in)
        self.pushButton_2.clicked.connect(self.Choose_txt_out)
        self.pushButton_3.clicked.connect(self.Start_coding)

    def Choose_txt_in(self):
        global filename_RLC_in
        filename_RLC_in, selectedfilter2 = QFileDialog.getOpenFileName(
            self, ("请选择RLC输入文件"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )


    def Choose_txt_out(self):
        global filename_RLC_out
        filename_RLC_out, selectedfilter2 = QFileDialog.getOpenFileName(
            self, ("请选择RLC输出文件"), ("D：\PyQt"), ("文本过滤(* .txt)"), None
        )


    def Start_coding(self):
        global filename_RLC_in
        global filename_RLC_out
        print(filename_RLC_in,filename_RLC_out)
        Rlc = RLC
        Rlc.rlc(Rlc, filename_RLC_in, filename_RLC_out)
        reply = QMessageBox.information(self,
                                        "RLC结果",
                                        "计算成功！！",
                                        QMessageBox.Yes | QMessageBox.No)



if __name__=='__main__':

    app=QtWidgets.QApplication(sys.argv)
    Xinxilun=new_XinxilunMain()   #构造主窗口对象
    LZW1=new_LZW()     #构造LZW窗口对象
    LZW_IN=new_LZW_IN()   #构造编码对象
    LZW_OUT=new_LZW_OUT()     #构造译码对象
    XindaoRL=new_XindaoRL()      #构造信道容量计算对象
    Complex=new_Complex()       #构造综合编码窗口
    Huffman=new_Huffman()       #构造哈夫曼编码窗口
    RLC1=new_RLC()       #构造RLC窗口
    Exor=new_EXOR()     #构造加密编码模块

    Xinxilun.show()
#    x = k.lzw_in(k,"D:/PyQt/信息论课设/LZW_in.txt")
#    print(x)
    sys.exit(app.exec_())
