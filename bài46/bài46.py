
import math


n=float(input("n:"))
s=0
i=1
while i<=n:
    s=s+1/((i+1)*math.sqrt(i)+i*math.sqrt(i+1))
    i=i+1
print("s:",s)
