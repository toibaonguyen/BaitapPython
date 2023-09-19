x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
s = 1
t = 1
for i in range(1, n + 1):
    t = t * x
    s += t
print("S =", s)

