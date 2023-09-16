import math
x=input("x:")
n=input("n:")
s=0
t=1
i=1
while i<=n:
    t=t*x
    s=math.sqrt(t+s)
    i=i+1
print("s:",s)
