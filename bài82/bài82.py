import math
x=int(input("x:"))
n=int(input("n:"))
s=0
t=1
i=1
while i<=n:
    t=t*math.sin(x)
    s=s+t
    i=i+1
print("s:",s)
