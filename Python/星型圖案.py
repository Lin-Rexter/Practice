import os
import random

n=int(input("請輸入層數:"))

print("\n")
print("金字塔型:","\n")
for i in range(n+1):
        print(' '*(n-i)+'*'*(2*i-1))
print("\n")

print("倒金字塔型:","\n")
for i in range(n+1):
        print(' '*(n-n+i)+'*'*(2*n-i*2-1))
print("\n")

print("三角形:","\n")
for i in range(n+1):
        print(' '*(n-i)+'*'*(i))
print("\n")

print("倒三角形:","\n")
for i in range(n+1):
        print(' '*(n-n+i)+'*'*(n-i))
print("\n")


os.system("pause")




