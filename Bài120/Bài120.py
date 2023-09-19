import math
n = int(input("Nhap n: "))
at = 2
for i in range(2, n + 1):
    ahh = 5 * at + math.sqrt(24 * math.pow(at,2) - 8)
    at = ahh
print("So hang thu n:", ahh)

