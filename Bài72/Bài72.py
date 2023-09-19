n = int(input("Nhap n: "))
s = 0
m = 0
for i in range(1, n + 1):
    m += i
    s += 1/m
print("S =", '{0:.{1}f}'.format(s,2))

