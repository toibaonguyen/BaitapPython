n = int(input("Nhap n: "))
at = 2
bt = 1
for i in range(2, n + 1):
    ahh = 3 * bt + 2 * at
    bhh = at + 3 * bt
    at = ahh
    bt = bhh
print("So hang thu n:", ahh, "va", bhh)