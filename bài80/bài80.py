import math
x=int(input("Nhập x: "))
n=int(input("Nhập n: "))
s=0
for i in range(1,n+1):
    t=i*math.pow(x,i-1)
    s=s+t

print(int(s))

