x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
s = x
t = x
dau = -1
for i in range(3, 2*n + 3,2):
    t = t * x * x
    s += dau * t
    dau = -dau
print("S =", s)

