import math
a = float(input("輸入係數 a: "))
b = float(input("輸入係數 b: "))
c = float(input("輸入係數 c: "))
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"方程式的根為: x1 = {x1:.1f}, x2 = {x2:.1f}")
elif D == 0:
    x = -b / (2*a)
    print(f"方程式有一個重根: x = {x:.1f}")
else:
    print("方程式沒有實數根")
