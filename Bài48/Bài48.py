x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
t = x
for i in range(x,x + n):
    t = t * (x + i)
print("T =", t)

