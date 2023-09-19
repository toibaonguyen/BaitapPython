x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
s = 1
t = 1
m = 1
for i in range(2, (2*n)+2, 2):
    t = t * x * x
    m = m * i * (i - 1)
    s = s + t/m
print("S =", '{0:.{1}f}'.format(s,2))

