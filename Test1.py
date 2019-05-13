"""
#LZW加密算法实现
from LZW_Coding import LZW_coding
address_in="LZW_in.txt"
address_out="D:/PyQt/信息论课设/指定目录打开.txt"
S_out = open(address_out,"r+")  #用于保存结果
k=LZW_coding
k.lzw_in(k,address_in,address_out)
#str_x=list(map(str,x))
#S_out.writelines([line + '\n' for line in str_x])




#字符串定义
a=[[0.0 for m in range(10)] for n in range(10)]
print(a)
print(4/3)
b=[[1,2],[3,4]]
c=b[0][1]*b[1][0]
print(c)

#获取整形数据的输入
a=float(input("请输入a:"))
b=float(input("请输入b:"))
c=a*b
print(c)

#同时输入多个数据
a,b,c=(int(x) for x in input("请输入你想输入的数据：").split(' '))
print(a+b+c)

a,b,c=(int(x) for x in input("请输入你想输入的数据：").split(' '))
print(a+b+c)


#p=[[0 for m in range(2)] for n in range(2)]
#for m in range(2):
    #for n in range(2)
 #   p[m]=(int(x) for x in input("请输入你想输入的数据：").split(' '))
 #   print(p[m])


#列表整体转换
p=[[]]
numbers=input("请输入你想输入的数据：").split(" ")
numbers2 = list(map(float, numbers))
p[0]+=list(numbers2)
print(p[0][1]*p[0][0])


from Text_to_Array import text_to_array
t1=text_to_array()
x=t1.tta()
for i in range(2):
    for j in range(3):
        print(x[i][j])



import math
print(math.e)
for i in range(3):
    print(i)



aList = [123, 'xyz', 'zara', 'abc'];

print ("A List : ", aList.pop())
print ("B List : ", aList.pop(2))
print(aList)


#实验
from LZW_Coding import LZW_coding
lzw_in_role=LZW_coding()

lzw_in_role.lzw_in1("D:\PyQt\LZW_in.txt","D:\PyQt\信息论课设\指定目录打开.txt")

#LZW译码
from LZW_decoding import lzw_decoding
address_in="LZW_out.txt"
address_out="保存记录结果.txt"
k=lzw_decoding
k.lzw_out1(k,address_in,address_out)


from txt_to_array import txt_to_arr    #引用文本转换矩阵的模块
from Xindao_2 import Xindaorl1

filename_XindaoRL_in="D:/PyQt/信息论课设/多组数组分割.txt"
filename_XindaoRL_out="D:/PyQt/信息论课设/指定目录打开.txt"
print(filename_XindaoRL_in,filename_XindaoRL_out)
#从文本中得到数组
TTA=txt_to_arr
channel1=TTA.txt_to(TTA,filename_XindaoRL_in)
length=len(channel1)
print(length)
print("1")
for i in range(length):
    channel=channel1[i][:][:]
    #开始计算
    Xin=Xindaorl1
    Xin.xindaorl(Xin,channel,filename_XindaoRL_out)






from Huffman_en import Huffman_encoding
address_in="哈夫曼编码输入.txt"
address_out="哈夫曼编码输出.txt"
huff=Huffman_encoding
huff.start_encoding(huff,address_in,address_out)


str_x="dsdsdasdsdasd"
print(str_x[2])

from RLC_2 import RLC
filename_RLC_in="D:/PyQt/信息论课设/RLC.txt"
filename_RLC_out="D:/PyQt/信息论课设/指定目录打开.txt"
Rlc = RLC
Rlc.rlc(Rlc, filename_RLC_in, filename_RLC_out)


S_in=open("异或操作输入.txt")
S_out=("异或操作输出.txt")
p=0
EX=S_in.readline()
len_EX=len(EX)
EXp=[0 for i in range(len_EX)]
for i in EX:
    EXp[p]=int(i)
    p+=1
w="0b11100101010"
w_int=int(w)
w_bin=bin(w_int)
print(w_)



S_in=open("异或操作输入.txt","wb")        #写二进制
S_out=open("异或操作输出.txt")        #读二进制
S_in.writelines('0b111100110101')
x=S_out.readline()
print(x)

x=~0b1
print(x)
y=bin(x)
print(y)
y_str=str(y)
print(y_str)

f=[1,0,1,1,0,1]
print(type(f[2]))
print(type(bin(f[2])))

"""
num=8
num_=8*0.25
print(num_)