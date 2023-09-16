import math
r = float(input("Nhap ban kinh: "))
n = float(input("Nhap so canh: "))
s = 1/2 * n * pow(r,2) * math.sin(2 * math.pi / n)
print("Dien tich cua da giac la:", '{0:.{1}f}'.format(s, 2))