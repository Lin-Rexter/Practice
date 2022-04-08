import os
import random

a = {"7":10000,"apple":500,"banana":1000,"6":5000}
b = []

def TQ():
    for j in range(3):
        pc=random.randint(0,4)
        if pc==1:
            x="7"
            print(x,end=" ")
            b.append(a[x])
        elif pc==2:
            x="apple"
            print(x,end=" ")
            b.append(a[x])
        elif pc==3:
            x="banana"
            print(x,end=" ")
            b.append(a[x])
        else:
            x="6"
            print(x,end=" ")
            b.append(a[x])

    b.sort()
    if b[0]==b[1]==b[2]:
        num=b[0]*b[1]*b[2]
    elif b[0]==b[1]!=b[2]:
        num=b[0]*b[1]+b[2]
    elif b[0]!=b[1]==b[2]:
        num=b[1]*b[2]+b[0]
    elif b[0]!=b[1]!=b[2]:
        num=b[0]+b[1]+b[2]
    
    print()
    print(b)
    print(num)
    
TQ()

os.system("pause")





