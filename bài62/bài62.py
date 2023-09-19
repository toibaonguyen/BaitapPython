n = int(input("Nhập n: "))
s = 0
t = n

while t != 0:
    dv = t % 10
    if dv % 2 == 0:
        s += dv
    t //= 10

print("Tổng các chữ số chẵn của n là:", s)
