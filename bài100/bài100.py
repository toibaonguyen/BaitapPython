
import math
n=input("n:")
s=0
t=1
i=1
while i<=n:
    t=t*i
    s=math.pow(t+s, 1 / (i + 1))
    i=i+1
    
print("s:",s)