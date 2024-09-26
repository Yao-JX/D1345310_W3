n=str(input('輸入三位數：'))
if int(n)<999:
    y=[int(x) for x in n]
    y[0],y[2]=y[2],y[0]
    print('結果：',''.join(map(str,y)))#print(y[0],y[1],y[2],y[3])會有空格
else:
    print("error")