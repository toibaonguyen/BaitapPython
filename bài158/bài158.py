n = int(input("Nhập số nguyên dương n: "))

m = -1
count = 0

while n > 0:
    d = n % 10
    if d > m:
        m = d
        count = 1
    elif d == m:
        count += 1
    n = n // 10

print("Số lượng chữ số lớn nhất của", n, "là", count)