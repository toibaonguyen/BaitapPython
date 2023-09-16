import math
n = int(input("Nhap n: "))
s = 0
m = 0
e = 1
for i in range(1, n + 1):
    if(e >= math.pow(10,-6)):
        m += i
        e = 1/m
        s += e
    else:
        print("S =", '{0:.{1}f}'.format(s,2))
        break
print("S =", '{0:.{1}f}'.format(s,2))