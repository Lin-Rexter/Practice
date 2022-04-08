import os

while True:
    try:
        a=int(input("請輸入範圍1~1000內的數字:"))
        if 1 <= a <= 1000:
            break
        else:
            print("\n請輸入範圍內的數字\n")
    except ValueError:
        print("\n請輸入數字\n")
  
if a%2==0:
     print("\n偶數\n")
else:
     print("\n奇數\n")

os.system("pause")


