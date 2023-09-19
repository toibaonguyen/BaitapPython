import math
n=int(input("nhập n: "))
s=int(0)
for i in range(1,n+1):
 if (i<=n):
    s=s+math.pow(i,4)
print(int(s))