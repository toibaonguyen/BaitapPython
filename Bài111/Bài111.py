import math
n = int(input("Nhap n: "))
s = 3
e = 3
dau = 1
for i in range(2, 2*n + 2, 2):
    if(e >= math.pow(10,-6)):
        e = 4/(i * (i + 1) * (i + 2))
        s = s + dau * e
        dau = -dau
    else:
        print("S =", '{0:.{1}f}'.format(s,2))
        break
print("S =", '{0:.{1}f}'.format(s,2))

