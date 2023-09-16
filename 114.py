n = int(input("Nhap n: "))
at = -2
tt = 3
pp = 7
for i in range(2, n + 1):
    tt = tt * 3
    pp = pp * 7
    ahh = 5 * at + 2 * tt - 6 * pp + 12
    at = ahh
print("So hang thu n:", ahh)