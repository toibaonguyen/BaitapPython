import math
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
m = math.fabs(a)
n = math.fabs(b)
while((m * n) > 0):
    if(m > n):
        m = m - n
    else:
        n = n - m
bcnn = math.fabs(a * b)/(m + n)
print("BCNN:", bcnn)
