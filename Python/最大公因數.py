import os

while True:
    try:
        a=int(input("請輸入第一個數字:"))
        b=int(input("請輸入第二個數字:"))
        break
    except ValueError:
        print("\n請輸入數字\n")
  
if a>b:
    c=a
else:
    c=b
    
for k in range(1,c+1):
    if a%k==0 and b%k==0:
        c=k
print("\n最大公因數為:",c,"\n")

os.system("pause")



