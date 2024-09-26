n=str(input('請輸入一個三位數：'))
if int(n)<999:
    y=[int(x) for x in n]
    print('每位數字的總和：',sum(y))
else:
    print("error")