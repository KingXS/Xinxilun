class text_to_array:
    def tta(self,address):
        S=open("信道容量迭代计算.txt")#打开存放数组的文件
        str=S.readlines()#这是一个字符串数组
        #print(str)
        length=len(str)#字符串数组的长度
        p=[[0 for m in range(2)] for n in range(2)]
        for i in range(length-1):
            lis1=str[i][:-1] #定义变量保存数组中每一行的值
            lis2=lis1.split(" ") #将每一行的值按空格进行分割
            #print(lis2)
            lis3= list(map(float,lis2))
            p[i] = list(lis3)

        return p



