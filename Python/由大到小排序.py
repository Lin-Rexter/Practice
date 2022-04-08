import os
import random

arr=list(map(int, input("請輸入多個任意數字（記得分開）：").split(' '))) 

print("原始: ",arr,"\n")
n=len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1],arr[j]

print("轉換後: ",arr,"\n")

os.system("pause")



