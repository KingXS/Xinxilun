class txt_to_arr:
    def txt_to(self,address_in):

        S_file=open(address_in)#打开存放数组的文件
        str_=S_file.readlines()#这是一个字符串数组
        length=len(str_)#字符串数组的长度
        #print(str_)
        num_array=len(str_)#字符串数组的长度,即数组的个数
        p=[[[0 for col in range(5)] for row in range(5)] for x in range(length)]
        for i_1 in range(num_array):
            array = str_[i_1].strip('\n').split(',')   #一行中所有的数据
            p[i_1][:][:]=array
            len_array=len(array)            #统计数组的行数
            print("数组是：",array,"长度是：",len_array)
            for i_2 in range(len_array ):#开始把每一行中的数据进行类型转换
                #print(i_2)
                lis1 = array[i_2][:]  # 定义变量保存数组中每一行的值
                lis2 = lis1.split(" ")  # 将每一行的值按空格进行分割
                #print(lis2)
                lis3 = list(map(float, lis2))
                p[i_1][i_2][:]=lis3


        return p

