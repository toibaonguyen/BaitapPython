n = int(input("Nhap n: "))
t = 1
for i in range(1,n + 1):
    t = t * (1 + 1/pow(i,2))
print("T =", '{0:.{1}f}'.format(t,2))

