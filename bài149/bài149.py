a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

gcd = a

print("Ước chung lớn nhất của", a, "và", b, "là", gcd)
