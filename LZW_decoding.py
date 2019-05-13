class lzw_decoding:
    def lzw_out1(self,address_in,address_out):
        S_in=open(address_in)#打开存放数组的文件
        S_out=open(address_out,"r+")
        str_=S_in.readlines()#这是一个字符串数组
        length=len(str_)#字符串数组的长度
#        print(length)
        p=[[0 for m in range(length)] for n in range(length)]  #定义一个二维数组存放读取出来的数据
        for i in range(length):
            #print(i)
            #print(str[i][:-1])
            if i != (length - 1):#除了最后一行外，其它行的最后一个字符均是‘/n’
                lis1=str_[i][:-1] #定义变量保存数组中每一行的值
                lis2=lis1.split(" ") #将每一行的值按
                lis3= list(map(int,lis2))
                p[i] = list(lis3)

            else:       #
                lis1 = str_[i][:]  # 定义变量保存数组中每一行的值
                lis2 = lis1.split(" ")  # 将每一行的值按
                lis3 = list(map(int, lis2))
                p[i] = list(lis3)

#            print(p)


        dictionary = {i: chr(i) for i in range(97, 123)}
        last = 256
        arr = p          #[97, 97, 98, 256, 258, 257, 259]


        result = [[ ] for n in range(length)]   #定义二维数组存放结果
        final_result=[]   #定义二维数组存放修改完的结果
        for i in range(length):
            q = arr[i].pop(0)
            result[i].append(dictionary[q])


            for c in arr[i]:
                if c in dictionary:
                    entry = dictionary[c]
                result[i].append(entry)
                dictionary[last] = dictionary[q] + entry[0]
                last += 1
                q = c

            x=''.join(result[i])
            S_out.writelines(x+'\n')
 #           print(''.join(result[i]))
