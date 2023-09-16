import math
n = int(input("Nhap n: "))
dt = math.fabs(n)
while(dt >= 10):
    dt = dt // 10
print("Chu so dau tien cua n:", dt)