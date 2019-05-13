
class LZW_coding:
    def lzw_in(self,address_in,address_out):
        S_in = open(address_in)#用于存储打开文件的对象
        S_out = open(address_out,"r+")  #用于保存结果
        str_ = S_in.readlines()    #命名对象时，一定不能把对象名和内置函数名字重合
        length = len(str_)

        dictionary = {chr(i): i for i in range(97, 123)}

        laste = 256
        p = ""

        result = [[] for n in range(length)]

        for l in range(length):  # 对文件中的每一行进行编码
            print(l)
            #print(str[l][:-1])
            if l!=(length-1):
                print(str_[l][:-1])
                #在python中，从文本中读取的数据，默认除了最后一行外，其他行的最后一个字符是/n
                for c in str_[l][:-1]:  # 读取字符串
                    pc = p + c
                    if pc in dictionary:
                        p = pc
                    else:
                        result[l].append(dictionary[p])
                        dictionary[pc] = laste
                        laste += 1
                        p = c

            else:             #当前读取的字符串是最后一行
                print(str_[l][:])
                for c in str_[l][:]:  # 读取字符串
                    pc = p + c
                    if pc in dictionary:
                        p = pc
                    else:
                        result[l].append(dictionary[p])
                        dictionary[pc] = laste
                        laste += 1
                        p = c

            if p != '':
                result[l].append(dictionary[p])


        x=result
        str_x=list(map(str, x))
#        print(str_x)

        S_out.writelines([line + '\n' for line in str_x])
        print("1")