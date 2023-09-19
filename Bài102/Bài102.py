import math
n = int(input("Nhap n: "))
s = 0
e = 0.5
for i in range(2, 2*n + 2, 2):
    if(e >= math.pow(10,-6)):
        e = 1/i
        s = s + e
    else:
        print("S =", '{0:.{1}f}'.format(s,2))
        break
print("S =", '{0:.{1}f}'.format(s,2))

