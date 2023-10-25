#test5
origin=['1','2','3','4','5','6','7','8','9']

def str2int(list,i,j):
    ret=0
    for idx in range(i,j+1):
        ret=ret*10+int(list[idx])
    return ret

def cal(list):
    ret=0
    left=0
    flag=0
    length=len(list)
    for i in range(length):
        if(list[i]=='+' or list[i]=='-'):
            if(flag==0):
                ret=ret+str2int(list,left,i-1)
            elif(flag==1):
                ret=ret-str2int(list,left,i-1)
            left=i+1
            if(list[i]=='+'):
                flag=0
            if(list[i]=='-'):
                flag=1
    if (flag == 0):
        ret = ret + str2int(list,left, length-1)
    elif (flag == 1):
        ret = ret - str2int(list,left, length - 1)
    return ret

number=[]
data=[]
result=[]

def insert(list,idx,type):
    if(idx>=len(list)):
        if(type==0):
            data.append(list)
            result.append(cal(list))
    else:
        if(type==1):
            list.insert(idx,'+')
        elif(type==2):
            list.insert(idx, '-')
        tmp1 = list.copy()
        tmp2 = list.copy()
        tmp3 = list.copy()
        if(type!=0):
            insert(tmp1, idx + 2, 0)
            insert(tmp2, idx + 2, 1)
            insert(tmp3, idx + 2, 2)
        else:
            insert(tmp1, idx + 1, 0)
            insert(tmp2, idx + 1, 1)
            insert(tmp3, idx + 1, 2)
        if(type!=0):
            del list[idx]

def bti():
    for i in range(9):
        number.append([])
        for j in range(9):
            number[i].append(str2int(origin,i,j))
    insert(['1','2','3','4','5','6','7','8','9'],1,0)
    insert(['1','2','3','4','5','6','7','8','9'], 1, 1)
    insert(['1','2','3','4','5','6','7','8','9'], 1, 2)

def Find_expression(x):
    list=[]
    length=len(result)
    for idx in range(length):
        tmp=''
        if(x==result[idx]):
            for item in data[idx]:
                tmp+=item
            tmp=tmp+'='+str(x)
            list.append(tmp)
    return list

if __name__ == '__main__':
    bti()
    x=Find_expression(50)
    for item in x:
        print(item)
    Total_solutions=[]
    for i in range(1,101):
        Total_solutions.append(len(Find_expression(i)))
    min=Total_solutions[0]
    max=Total_solutions[0]
    for item in Total_solutions:
        if(item<min):
            min=item
        if(item>max):
            max=item
    for i in range(100):
        if(Total_solutions[i]==min):
            print(i+1,end=" ")
    print()
    for i in range(100):
        if(Total_solutions[i]==max):
            print(i+1,end=" ")

