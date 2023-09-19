import math
n = int(input("Nhap n: "))
s = 0
t = 1
for i in range(1, n + 1):
    t = t * i
    s = math.sqrt(t + s)
print("S =", '{0:.{1}f}'.format(s,2))

