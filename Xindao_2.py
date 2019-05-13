import math


class Xindaorl1:
    def xindaorl(self,channel,address_out):

        C=0.0
        cishu=0;
        N=2     #int(input("请输入行数："))
        M=3     #int(input("请输入列数："))

        S=[0 for m in range(N+1)]
        SS=[0 for m in range(N+1)]

        #状态转移矩阵的输入，从已有的文本文档中调用
        p=channel

        for i in range(N):
            #print(i)
            S[i]=1.0/N #赋值
            #print(S[i])
        #print(S)
        #迭代
        flag=True
        #定义二维数组
        fa=[[0 for m in range(M+1)] for n in range(N+1)]
        while(flag):
            #首先计算fa,ji
            for j in range(M):
                sum=0.0
                for i in range(N):
                    sum=sum+S[i]*p[i][j]
                # print(sum)
                for i in range(N):
                    fa[j][i]=(S[i]*p[i][j])/sum

            #迭代计算S
            #计算分母
            sum1=0.0
            for i in range(N):
                flag3=True
                sum2=0.0
                for j in range(M):
                    if fa[j][i]!=0:
                        sum2=sum2+p[i][j]*(math.log(fa[j][i])/math.log(math.e))
                    elif (fa[j][i]==0) and (p[i][j]!=0):
                        flag3=False
                    elif (fa[j][i] == 0) and (p[i][j] == 0):
                        sum2 = sum2 + 0
                if flag3:
                    sum1=sum1+math.exp(sum2)
                else:
                    sum1=sum1+0
        #计算SS[i]
            for i in range(N):
                flag1=True  #若有无穷比无穷
                sum6=0.0
                for j in range(M):
                    if fa[i][j]!=0:
                        sum6=sum6+p[i][j]*(math.log(fa[j][i])/math.log(math.e))
                    elif fa[j][i]==0 and p[i][j]!=0:
                        flag1=False
                    elif fa[j][i]==0 and p[i][j]==0:
                        sum6 = sum6 + 0
                if flag1:
                    SS[i]=math.exp(sum6)/sum1
                else:
                    SS[i]=0

            distance=0.0
            for i in range(N+1):
                distance=distance+math.pow(SS[i]-S[i],2)  #计算范数
            if distance<0.00001:
                flag=False
            else:
                for i in range(N+1):
                    S[i]=SS[i]
            C=math.log(sum1)/math.log(2)
            cishu+=1

        C_str=str(C)
        S_input=open(address_out,"a")
        S_input.writelines("信道容量为："+C_str+"\n")
 #       print("其信道容量为：" ,C)

