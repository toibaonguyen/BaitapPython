n = int(input("Nhập n: "))
s = float(0)

for i in range(1, n + 1):
    if i <= n:
        s = s + 1 / i

print("Tổng là:", round(s,2))


