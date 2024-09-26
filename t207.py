n = int(input("輸入一個十進制數字: "))
x = bin(n)[2:]  # 去掉 '0b'
y = oct(n)[2:]   # 去掉 '0o'
z = hex(n)[2:].upper()  # 去掉 '0x' 轉大寫
print(f"二進制: {x}")
print(f"八進制: {y}")
print(f"十六進制: {z}")