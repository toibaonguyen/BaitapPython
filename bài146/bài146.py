n = int(input("Nhập số nguyên dương n: "))
dn = 0
t = n

while t > 0:
    dv = t % 10
    dn = dn * 10 + dv
    t = t // 10

if n == dn:
    print(n, "là số đối xứng.")
else:
    print(n, "không là số đối xứng.")

