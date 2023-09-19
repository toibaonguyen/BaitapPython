
n = int(input("Nhập số nguyên dương n: "))

i = True
d = 0

while n > 0:
    dv = n % 10
    if dv < d:
        i = False
        break
    d = dv
    n = n // 10

if i:
    print("Các chữ số của", n, "tăng dần từ trái sang phải.")
else:
    print("Các chữ số của", n, "không tăng dần từ trái sang phải.")