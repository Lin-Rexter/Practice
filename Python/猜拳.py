import os
import random

me=0
pc=0
i=0

while True:
    i+=1
    a=int(input("0:剪刀、1:石頭、2:布："))
    b=random.randint(0,2)
    print("電腦出拳是：%d"%b)
    if(a==b):
        print("遊戲結果：平手！")
        print("\n")
    elif(a-b==-1 or a-b==2):
        print("您輸了，電腦贏了！")
        pc+=1
        print("\n")
    elif(a-b==1 or a-b==-2):
        print("您贏了，電腦輸了！")
        me+=1
        print("\n")
    if i==5:
        break
        
if pc > me:
      print("電腦獲勝次數最高,電腦獲勝!")
elif me > pc:
    print("玩家獲勝次數最高,玩家獲勝!")

os.system("pause")




