n = int(input("Nhap n: "))
s = 0
for i in range(2,n + 1, 2):
    if (n % i == 0):
        s += i
print("Tong cac uoc chan =", s)