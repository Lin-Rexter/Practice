import os

while True:
    try:
        a=int(input("請輸入第一個數字:"))
        b=int(input("請輸入第二個數字:"))
        break
    except ValueError:
        print("\n請輸入數字\n")
        
x=0
if a>b:
    c=a
else:
    c=b

for k in range(1,c+1):
    if a%k==0 and b%k==0:
        x=k
print("\n最小公倍數為:",int(a*b/x),"\n")

os.system("pause")

