import math
n = int(input("Nhap n: "))
s = 0
for i in range(1,n + 1):
    s += 1/(math.sqrt(i) + math.sqrt(i + 1))
print("S =", '{0:.{1}f}'.format(s,2))

