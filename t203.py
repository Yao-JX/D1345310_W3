'''
y=int(input('輸入數字:'))
while y%2==0:
    print(y,'是偶數')
else:
    print(y,'是奇數')
'''
a=int(input('輸入數字:'))
b=a%2!=0
c=['是偶數','是奇數']
print('結果:',a,c[b],sep='')