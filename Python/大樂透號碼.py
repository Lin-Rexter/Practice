import os
import random
while True:
  try:
    me=list(map(int, input("請輸入6位號碼（記得分開）：").split(' '))) 
    mee=set(me)
    if len(me)!=len(mee):
        print("輸入的號碼有重複","\n")
    elif len(list(me))==6:
        print("你的號碼為：",me)
        pc=list(random.sample(range(1,50),6))
        print("大樂透號碼為：",pc)
        i=100
        lon=len(set(pc) & set(me))
        ln=(set(pc) & set(me))
        if lon==1:
          print("恭喜獲得",i,"元")
          print("你對中的號碼為：",ln,"\n")
          continue
        elif lon==2:
          print("恭喜獲得",i*10,"元")
          print("你對中的號碼為：",ln,"\n")
          continue
        elif lon==3:
          print("恭喜獲得",i*100,"元")
          print("你對中的號碼為：",ln,"\n")
          continue         
        elif lon==4:
          print("恭喜獲得",i*1000,"元")
          print("你對中的號碼為：",ln,"\n")
          continue    
        elif lon==5:
          print("恭喜獲得",i*10000,"元")  
          print("你對中的號碼為：",ln,"\n")
          continue    
        elif lon==6:
          print("恭喜獲得",i*100000,"元")
          print("你對中的號碼為：",ln,"\n")
          continue
        else:
          print("可惜未中 再接再厲！！","\n")          
          continue
    else:  
        print("請輸入6位號碼 且 號碼需在1~49內","\n")
        continue
  except ValueError:
    print("輸入內容有誤，請確認內容是否為數字","\n")