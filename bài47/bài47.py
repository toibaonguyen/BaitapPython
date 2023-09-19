
import math
n=int(input("Nhập n: "))
s=int(0)
for i in range(1,n+1):
    if(i<=n):
        s=s + math.sqrt(1+1/math.pow(i,2) + 1/(math.pow(i+1,2)))
print(float("{:.2f}".format(s)))