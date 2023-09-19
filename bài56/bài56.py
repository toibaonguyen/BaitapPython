
n = int(input("Nhập n: "))
lc = n % 10
t = n

while t != 0:
    dv = t % 10
    if dv < lc:
        lc = dv
    t = t // 10

print("Chữ số nhỏ nhất của n là:", lc)