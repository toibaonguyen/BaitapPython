import math
x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
s = 1
t = 1
m = 1
e = 1
for i in range(1, n + 1):
    if(e >= math.pow(10,-6)):
        t = t * x
        m = m * i
        e = t/m
        s += e
    else:
        print("S =", '{0:.{1}f}'.format(s,2))
        break
print("S =", '{0:.{1}f}'.format(s,2))