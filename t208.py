a=int(input('輸入一個五位數:'))
if a<99999:
    print('結果：')
    y=[int(x) for x in str(a)]
    print(y[0],'\n',y[1],'\n',y[2],'\n',y[3],'\n',y[4],'\n',sep='')
else:
    print("error")