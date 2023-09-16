
import math
x=int(input("x:"))
n=int(input("n:"))
s=0
t=1
i=1
dau=+1
while i<=n:
    t=t*x
    s=s+dau*t
    i=i+1
    dau=-dau
print("s:",s)
