import math
x1 = float(input("Nhập x1: "))
y1 = float(input("Nhập y1: "))
x2 = float(input("Nhập x2: "))
y2 = float(input("Nhập y2: "))
x3 = float(input("Nhập x3: "))
y3 = float(input("Nhập y3: "))


a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b=  math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
c= math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
p=a+b+c
print("p:",p)