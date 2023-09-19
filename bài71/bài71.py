import math
x=int(input("nhập x: "))
n=int(input("nhập n: "))
s = 0
for i in range(0,n+1):
    if(i<=2*n+1):
        t=math.pow(x,2*i + 1)
        s= s + t

print(s)    
