a=int(input('輸入一個五位數:'))
if a<99999:
    print('結果：')
    y=[int(x) for x in str(a)]
    print(y[0])
    print(y[1])
    print(y[2])
    print(y[3])
    print(y[4])
else:
    print("error")