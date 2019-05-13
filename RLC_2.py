num_1=0     #子字符串中的起始位置
#num=1       #重复的字符的个数
new_len=0   #字符串中不和前一个字符重复的字符的起始位置

class RLC:
    def rlc(self,address_in,address_out):
        S_in=open(address_in)
        S_out=open(address_out,"a")
        global num_1
        global new_len
        textbefore = S_in.readline()
        textafter = ""
        c = ""
        len_textbefore = len(textbefore)
        print("字符串的长度是： ",len_textbefore)
        try:
            while (new_len<len_textbefore):
                num=1
                num_1=new_len    #令子字符串的位置重新回到当前的主字符串的位置
                print("1")
                while (textbefore[num_1]==textbefore[num_1+1]):  #判断字符串的第一个字符和下一个字符是否相等
                    num_1+=1
                    num+=1


                num_str=str(num)
                S_out.writelines(textbefore[num_1]+" "+num_str+"\n")   #统计重复的字符以及个数
                new_len+=num
                print("当前主字符串的起始位置是： ",new_len)
        except:
            print("呵呵")