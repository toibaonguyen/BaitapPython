n = int(input("Nhap n: "))
s = 0
for i in range(1,n):
    if (n % i == 0):
        s += i
print("Tong cac uoc so nho hon n =", s)