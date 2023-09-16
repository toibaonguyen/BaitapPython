import math
n = int(input("Nhap n: "))
s = 0
for i in range(1, n + 1):
    s = math.sqrt(2 + s)
print("S =", '{0:.{1}f}'.format(s,2))