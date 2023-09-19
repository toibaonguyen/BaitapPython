
import math
x=int(input("Nhập x: "))
n=int(input("nhập n: "))
s=0
t=1
for i in range(1,n+1):
    t=t*x
    s=s+math.sin(t)

print(s)


