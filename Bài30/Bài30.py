n = int(input("Nhap n: "))
s = 0
for i in range(2,2 * n + 2,2):
    s += 1/i
print("S =", '{0:.{1}f}'.format(s,2))

