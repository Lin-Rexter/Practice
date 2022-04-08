x={"A":"台北市","B":"台中市",
   "C":"基隆市","D":"台南市",
   "E":"高雄市","F":"台北縣",
   "G":"宜蘭縣","H":"桃園縣",
   "I":"嘉義市","J":"新竹縣",
   "K":"苗栗縣","L":"台中縣",
   "M":"南投縣","N":"彰化縣",
   "O":"新竹市","P":"雲林縣",
   "Q":"嘉義縣","R":"台南縣",
   "S":"高雄縣","T":"屏東縣",
   "U":"花蓮縣","V":"台東縣",
   "W":"金門縣","X":"澎湖縣",
   "Y":"陽明山","Z":"連江縣"}
while True:
    try:
        a=str(input("請輸入身分證號碼:"))
        b=a[:1]
        if len(a)==10:
            if a[1:2]=='1':
                print("男生")    
            elif a[1:2]=='2':
                print("女生")
            if b=='A':
                print(x["A"])
            elif b=='B':
                print(x["B"])
            elif b=='C':
                print(x["C"])
            elif b=='D':
                print(x["D"])
            elif b=='E':
                print(x["E"])
            elif b=='F':
                print(x["F"])
            elif b=='G':
                print(x["G"])
            elif b=='H':
                print(x["H"])
            elif b=='I':
                print(x["I"])
            elif b=='J':
                print(x["J"])
            elif b=='K':
                print(x["K"])
            elif b=='L':
                print(x["L"])
            elif b=='M':
                print(x["M"])
            elif b=='N':
                print(x["N"])
            elif b=='O':
                print(x["O"])
            elif b=='P':
                print(x["P"])
            elif b=='Q':
                print(x["Q"])
            elif b=='R':
                print(x["R"])
            elif b=='S':
                print(x["S"])
            elif b=='T':
                print(x["T"])
            elif b=='U':
                print(x["U"])
            elif b=='V':
                print(x["V"])
            elif b=='W':
                print(x["W"])
            elif b=='X':
                print(x["X"])
            elif b=='Y':
                print(x["Y"])
            elif b=='Z':
                print(x["Z"])
        else:
            print("身分證號碼錯誤 請輸入10位數字")
            continue
    except ValueError:
        print("請輸入數字")