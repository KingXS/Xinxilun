S_in=open("异或操作输入.txt")
S_out=open("异或操作输出.txt","a")


class
p=0
EX=S_in.readlines()
print(EX)
len_EX1=len(EX)
print(len_EX1)
print(EX[len_EX1-1])
len_EX=len(EX[len_EX1-1])
print(len_EX)
EXp=[0 for i in range(len_EX)]
for i in EX[len_EX1-1]:
    EXp[p]=int(i)
    p+=1
print(EXp)

print(len(EXp))
for i in range(len(EXp)):
    EXp.append(EXp.pop(1))
S_out.writelines("加密操作之后：")
for i in range(len(EXp)):
    S_out.writelines(str(EXp[i]))