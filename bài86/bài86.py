
x = int(input("Nhập giá trị của x: "))
n = int(input("Nhập giá trị của n: "))

result = 0

for i in range(n+1):
    term = (-1)**i * x**(2*i)
    result += term

print("Kết quả của dãy là:", float(result))