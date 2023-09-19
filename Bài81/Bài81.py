x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
s = 0
m = 1
for i in range(0, n + 1):
    m = m * (x + i)
    s += 1/m
print("S =", '{0:.{1}f}'.format(s,2))

